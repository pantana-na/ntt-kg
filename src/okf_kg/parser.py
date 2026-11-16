"""Deterministic parser for Open Knowledge Format (OKF v0.2) Markdown bundles."""

from __future__ import annotations

import hashlib
from pathlib import Path
import re
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

import yaml

from .models import (
    CatalogEntrySpec,
    DocumentLineageEdge,
    EquipmentNode,
    FlowStreamEdge,
    GovernanceDocNode,
    InstrumentMonitorEdge,
    InstrumentNode,
    OkfChunkRecord,
    ParsedOkfBundle,
    PlantUnitNode,
    ProcessBoundaryNode,
    SafetyGovernanceEdge,
    UnitEquipmentEdge,
)
from .rrf import make_dataplex_entry_id

DEFAULT_UNIT_TITLES: Dict[str, str] = {
    "SI": "Seabrook Station Safety Injection System (SI)",
    "SW": "Seabrook Station Service Water System (SW)",
    "SWA": "Seabrook Station Service Water Air Handling System (SWA)",
    "SF": "Seabrook Station Spent Fuel Pool Cooling & Cleanup System (SF)",
    "SS": "Seabrook Station Nuclear & Steam Generator Sample System (SS)",
    "RH": "Residual Heat Removal Subsystem (RH)",
    "CS": "Chemical and Volume Control / Charging Subsystem (CS)",
    "CBS": "Containment Building Spray & Recirculation Sump Subsystem (CBS)",
    "CC": "Primary Component Cooling Water System (CC)",
    "SCC": "Secondary Component Cooling Water System (SCC)",
    "DG": "Emergency Diesel Generator Jacket Water System (DG)",
}


def _edge_hash(prefix: str, *parts: str) -> str:
    digest = hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()[:20]
    return f"{prefix}:{digest}"


def _split_frontmatter(raw_text: str) -> Tuple[Optional[Dict[str, Any]], str]:
    if not raw_text.startswith("---\n"):
        return None, raw_text
    parts = raw_text.split("---\n", 2)
    if len(parts) < 3:
        return None, raw_text
    fm = yaml.safe_load(parts[1])
    if not isinstance(fm, dict):
        return None, raw_text
    return fm, parts[2]


def _extract_markdown_table_field(body: str, field_patterns: Sequence_or_Iterable) -> Optional[str]:
    for line in body.splitlines():
        if "|" not in line:
            continue
        cells = [c.strip().strip("*").strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        key_lower = cells[0].lower()
        for pat in field_patterns:
            if pat in key_lower and cells[1] and cells[1] not in ("—", "-", ":---"):
                return cells[1]
    return None


Sequence_or_Iterable = Iterable[str]


def _detect_conflict(body: str) -> Tuple[bool, Optional[str]]:
    conflict_lines: List[str] = []
    for line in body.splitlines():
        stripped = line.strip().lstrip(">").strip()
        if "⚠️" in stripped or "CONFLICT" in stripped or "CRITICAL PROCESS SAFETY / DISCREPANCY WARNING" in stripped:
            conflict_lines.append(stripped)
    if not conflict_lines:
        return False, None
    # Also grab following blockquote explanation line if warning header was generic
    lines = body.splitlines()
    for idx, line in enumerate(lines):
        if "CRITICAL PROCESS SAFETY / DISCREPANCY WARNING" in line and idx + 1 < len(lines):
            nxt = lines[idx + 1].strip().lstrip(">").strip()
            if nxt and nxt not in conflict_lines:
                conflict_lines.append(nxt)
                break
    return True, " ".join(conflict_lines)[:800]


def _extract_pid_drawings(fm: Dict[str, Any], body: str) -> List[str]:
    em = fm.get("entity_metadata") or {}
    found: List[str] = []
    for key in ("associated_drawings", "drawing_numbers", "pids"):
        val = em.get(key)
        if isinstance(val, list):
            found.extend(str(x).strip() for x in val if x)
    for m in re.findall(r"\bPID-1-[A-Z0-9-]+|\bML101620329(?:-part-\d+)?", body):
        if m not in found:
            found.append(m)
    return found[:15]


def _chunk_markdown_sections(
    entity_id: str,
    entity_label: str,
    tag: str,
    title: str,
    unit_code: Optional[str],
    safety_classification: Optional[str],
    has_conflict: bool,
    gcs_uri: str,
    description: str,
    body: str,
    max_chars: int = 2800,
) -> List[OkfChunkRecord]:
    """Split Markdown body by ## headings into context-prefixed chunks for Hybrid Search."""
    header_prefix = (
        f"[{entity_label}] Tag: {tag} | Title: {title}"
        + (f" | Unit: {unit_code}" if unit_code else "")
        + (f" | Safety: {safety_classification}" if safety_classification else "")
        + (" | WARNING/CONFLICT: YES" if has_conflict else "")
    )

    sections: List[Tuple[str, List[str]]] = []
    current_heading = "Overview & Summary"
    current_lines: List[str] = [description] if description else []

    for line in body.splitlines():
        m = re.match(r"^#{1,3}\s+(.+)$", line.strip())
        if m:
            content_str = "\n".join(current_lines).strip()
            if content_str:
                sections.append((current_heading, current_lines))
            current_heading = m.group(1).strip()
            current_lines = []
        else:
            current_lines.append(line)

    if "\n".join(current_lines).strip():
        sections.append((current_heading, current_lines))

    if not sections:
        sections = [("Overview & Summary", [description or title])]

    chunks: List[OkfChunkRecord] = []
    chunk_idx = 0
    for heading, lines in sections:
        raw_section = "\n".join(lines).strip()
        if not raw_section:
            continue
        # Sub-split very large sections deterministically on paragraph boundaries
        for offset in range(0, len(raw_section), max_chars):
            slice_text = raw_section[offset : offset + max_chars].strip()
            if not slice_text:
                continue
            part_heading = heading if offset == 0 else f"{heading} (cont.)"
            full_chunk = f"{header_prefix}\nSection: {part_heading}\n\n{slice_text}"
            chunks.append(
                OkfChunkRecord(
                    chunk_id=f"{entity_id}#sec-{chunk_idx}",
                    entity_id=entity_id,
                    entity_label=entity_label,
                    chunk_index=chunk_idx,
                    section_heading=part_heading[:500],
                    tag=tag,
                    title=title[:500],
                    unit_code=unit_code,
                    safety_classification=safety_classification,
                    has_conflict=has_conflict,
                    gcs_uri=gcs_uri,
                    chunk_text=full_chunk,
                )
            )
            chunk_idx += 1

    return chunks


def _split_unit_codes(raw_unit: Optional[str]) -> List[str]:
    if not raw_unit:
        return []
    codes: List[str] = []
    for part in re.split(r"[/,&]+|\band\b", str(raw_unit)):
        cleaned = part.strip().upper()
        if cleaned and len(cleaned) <= 12 and re.match(r"^[A-Z0-9-]+$", cleaned):
            if cleaned not in codes:
                codes.append(cleaned)
    return codes


def _classify_boundary(tag: str) -> str:
    upper = tag.upper()
    if upper.startswith("X-") or "PENETRATION" in upper:
        return "PENETRATION"
    if "LOOP" in upper or "HDR" in upper or "HEADER" in upper or "SUP" in upper or "RET" in upper:
        return "HEADER"
    if "SUMP" in upper or "FLOOR" in upper or "POOL" in upper or "RWST" in upper:
        return "SUMP_OR_RESERVOIR"
    if "ATMOSPHERE" in upper or "VENT" in upper or "DRAIN" in upper:
        return "VENT_OR_DRAIN"
    return "PROCESS_BOUNDARY"


def parse_okf_bundle(
    bundle_dir: Path,
    gcs_bucket: str = "your-gcp-project-id-okf-bundle",
    gcs_prefix: str = "okf_bundle",
) -> ParsedOkfBundle:
    """
    Parse an OKF v0.2 Markdown directory into:
      - 5 Domain Node dictionaries (PlantUnits, Equipment, Instruments, ProcessBoundaries, GovernanceDocs)
      - 5 Typed Edge collections (BELONGS_TO_UNIT, FLOWS_TO, MONITORS, EXTRACTED_FROM, GOVERNED_BY)
      - Section-level OkfChunkRecords for Spanner Hybrid Search (FTS + Vector + RRF)
      - 100 Dataplex Knowledge Catalog Entry + Aspect specifications
    """
    if not bundle_dir.exists():
        raise FileNotFoundError(f"OKF bundle directory not found: {bundle_dir}")

    md_files = sorted(bundle_dir.rglob("*.md"))

    units: Dict[str, PlantUnitNode] = {}
    equipment: Dict[str, EquipmentNode] = {}
    instruments: Dict[str, InstrumentNode] = {}
    boundaries: Dict[str, ProcessBoundaryNode] = {}
    governance_docs: Dict[str, GovernanceDocNode] = {}

    unit_edges_map: Dict[str, UnitEquipmentEdge] = {}
    flow_edges_map: Dict[str, FlowStreamEdge] = {}
    monitor_edges_map: Dict[str, InstrumentMonitorEdge] = {}
    lineage_edges_map: Dict[str, DocumentLineageEdge] = {}
    governance_edges_map: Dict[str, SafetyGovernanceEdge] = {}
    chunks: List[OkfChunkRecord] = []
    catalog_entries: List[CatalogEntrySpec] = []

    # Keep parsed raw docs for second-pass relationship resolution
    parsed_items: List[Tuple[Path, str, Dict[str, Any], str, str]] = []
    source_resource_to_doc_id: Dict[str, str] = {}

    for path in md_files:
        rel_path = path.relative_to(bundle_dir).as_posix()
        gcs_uri = f"gs://{gcs_bucket}/{gcs_prefix.strip('/')}/{rel_path}"
        raw_text = path.read_text(encoding="utf-8")
        fm, body = _split_frontmatter(raw_text)
        if fm is None:
            continue
        parsed_items.append((path, rel_path, fm, body, gcs_uri))

    # Pass 1: Register Nodes & Chunks + CatalogEntrySpecs for all 100 frontmatter entities
    for path, rel_path, fm, body, gcs_uri in parsed_items:
        doc_type = str(fm.get("type") or "Concept").strip()
        title = str(fm.get("title") or path.stem).strip()
        description = str(fm.get("description") or "").strip()
        em = fm.get("entity_metadata") if isinstance(fm.get("entity_metadata"), dict) else {}
        has_conflict, conflict_summary = _detect_conflict(body)
        pid_drawings = _extract_pid_drawings(fm, body)
        labels = [str(t).strip() for t in (fm.get("tags") or []) if t]

        if doc_type == "Unit Overview":
            raw_uc = str(em.get("unit_code") or em.get("system_prefix") or "").strip().rstrip("-")
            if not raw_uc or len(raw_uc) > 10:
                if "service-water" in path.stem:
                    raw_uc = "SW"
                elif "steam-generator-sample" in path.stem:
                    raw_uc = "SS"
                elif "spent-fuel" in path.stem:
                    raw_uc = "SF"
                elif "safety-injection" in path.stem:
                    raw_uc = "SI"
                else:
                    raw_uc = path.stem.upper()[:10]
            unit_code = raw_uc.upper()
            unit_id = f"UNIT:{unit_code}"
            safety_cls = str(
                em.get("safety_classification")
                or _extract_markdown_table_field(body, ["safety classification"])
                or "Nuclear Safety Related / Mixed"
            ).strip()
            facility = str(em.get("facility") or "Seabrook Station").strip()

            units[unit_id] = PlantUnitNode(
                unit_id=unit_id,
                unit_code=unit_code,
                title=title,
                facility=facility,
                safety_classification=safety_cls,
                description=description,
                has_warning=has_conflict,
                gcs_uri=gcs_uri,
            )
            chunks.extend(
                _chunk_markdown_sections(
                    entity_id=unit_id,
                    entity_label="PlantUnit",
                    tag=unit_code,
                    title=title,
                    unit_code=unit_code,
                    safety_classification=safety_cls,
                    has_conflict=has_conflict,
                    gcs_uri=gcs_uri,
                    description=description,
                    body=body,
                )
            )
            catalog_entries.append(
                CatalogEntrySpec(
                    entry_id=make_dataplex_entry_id("unit", rel_path),
                    spanner_entity_id=unit_id,
                    entity_type=doc_type,
                    tag=unit_code,
                    display_name=title[:200],
                    description=description[:1500],
                    unit_code=unit_code,
                    equipment_or_instrument_class="Plant System / Unit",
                    safety_classification=safety_cls,
                    has_discrepancy_warning=has_conflict,
                    governing_standard_or_drawing=", ".join(pid_drawings[:4]) or "10 CFR 54",
                    gcs_markdown_uri=gcs_uri,
                    overview_markdown=body[:8000],
                    labels=labels,
                )
            )

        elif doc_type == "Equipment Concept":
            tag = str(em.get("tag") or path.stem).strip()
            eq_id = f"EQ:{tag}"
            eq_class = str(em.get("equipment_class") or "Equipment").strip()
            unit_raw = str(em.get("unit") or "PLANT").strip()
            safety_cls = str(
                em.get("safety_classification")
                or _extract_markdown_table_field(body, ["safety classification"])
                or "Unspecified"
            ).strip()

            equipment[eq_id] = EquipmentNode(
                equipment_id=eq_id,
                tag=tag,
                title=title,
                equipment_class=eq_class,
                unit_code=unit_raw,
                safety_classification=safety_cls,
                has_conflict=has_conflict,
                conflict_summary=conflict_summary,
                description=description,
                gcs_uri=gcs_uri,
            )
            chunks.extend(
                _chunk_markdown_sections(
                    entity_id=eq_id,
                    entity_label="Equipment",
                    tag=tag,
                    title=title,
                    unit_code=unit_raw,
                    safety_classification=safety_cls,
                    has_conflict=has_conflict,
                    gcs_uri=gcs_uri,
                    description=description,
                    body=body,
                )
            )
            catalog_entries.append(
                CatalogEntrySpec(
                    entry_id=make_dataplex_entry_id("eq", tag),
                    spanner_entity_id=eq_id,
                    entity_type=doc_type,
                    tag=tag,
                    display_name=title[:200],
                    description=description[:1500],
                    unit_code=unit_raw,
                    equipment_or_instrument_class=eq_class,
                    safety_classification=safety_cls,
                    has_discrepancy_warning=has_conflict,
                    governing_standard_or_drawing=", ".join(pid_drawings[:4]) or "Seabrook LR P&ID",
                    gcs_markdown_uri=gcs_uri,
                    overview_markdown=body[:8000],
                    labels=labels,
                )
            )

        elif doc_type == "Instrument Specification":
            raw_tag = str(
                em.get("tag")
                or _extract_markdown_table_field(body, ["instrument tag"])
                or title.split("—")[0].split("/")[0].strip()
                or path.stem.upper()
            ).strip()
            # Normalize multi-tag like "LE-2384-1 / LE-2384-2" -> primary tag "LE-2384-1"
            tag = raw_tag.split("/")[0].strip()
            inst_id = f"INST:{tag}"
            inst_type = str(
                em.get("instrument_type")
                or _extract_markdown_table_field(body, ["instrument type", "primary sensing", "associated primary"])
                or "Process Instrument"
            ).strip()
            unit_code = str(em.get("system") or "").strip() or None
            safety_cls = str(
                em.get("safety_classification")
                or _extract_markdown_table_field(body, ["safety classification"])
                or "Unspecified"
            ).strip()
            location = str(
                em.get("location")
                or _extract_markdown_table_field(body, ["physical location", "location"])
                or ""
            ).strip() or None
            interlock = str(
                _extract_markdown_table_field(body, ["interlock", "function / service"])
                or em.get("service")
                or ""
            ).strip() or None

            instruments[inst_id] = InstrumentNode(
                instrument_id=inst_id,
                tag=tag,
                title=title,
                instrument_type=inst_type[:120],
                unit_code=unit_code,
                safety_classification=safety_cls[:120],
                location=location[:250] if location else None,
                setpoint_or_range=None,
                interlock_or_alarm=interlock[:300] if interlock else None,
                has_warning=has_conflict,
                is_full_spec=True,
                description=description,
                gcs_uri=gcs_uri,
            )
            chunks.extend(
                _chunk_markdown_sections(
                    entity_id=inst_id,
                    entity_label="Instrument",
                    tag=tag,
                    title=title,
                    unit_code=unit_code,
                    safety_classification=safety_cls,
                    has_conflict=has_conflict,
                    gcs_uri=gcs_uri,
                    description=description,
                    body=body,
                )
            )
            catalog_entries.append(
                CatalogEntrySpec(
                    entry_id=make_dataplex_entry_id("inst", rel_path),
                    spanner_entity_id=inst_id,
                    entity_type=doc_type,
                    tag=tag,
                    display_name=title[:200],
                    description=description[:1500],
                    unit_code=unit_code or "PLANT",
                    equipment_or_instrument_class=inst_type[:120],
                    safety_classification=safety_cls[:120],
                    has_discrepancy_warning=has_conflict,
                    governing_standard_or_drawing=", ".join(pid_drawings[:4]) or "Seabrook LR P&ID",
                    gcs_markdown_uri=gcs_uri,
                    overview_markdown=body[:8000],
                    labels=labels,
                )
            )

        else:
            # GovernanceDocs: HAZOP Protocol, Risk Assessment Protocol, SOP, Workflow Procedure, Engineering Standard, Source Document
            slug = rel_path[:-3] if rel_path.endswith(".md") else rel_path
            doc_id = f"DOC:{slug}"
            tag = path.stem.upper()
            gov_stds = em.get("governing_standards") or em.get("governing_standard") or em.get("standard_code")
            if isinstance(gov_stds, list):
                gov_std_str = ", ".join(str(x) for x in gov_stds)
            elif gov_stds:
                gov_std_str = str(gov_stds)
            elif pid_drawings:
                gov_std_str = ", ".join(pid_drawings[:4])
            else:
                gov_std_str = "IEC 61882 / 10 CFR 54"

            governance_docs[doc_id] = GovernanceDocNode(
                doc_id=doc_id,
                doc_type=doc_type,
                tag=tag,
                title=title,
                governing_standard=gov_std_str[:250],
                has_warning=has_conflict,
                description=description,
                gcs_uri=gcs_uri,
            )

            # Map raw source PDF paths (e.g., reference/raw/pid/ML101620329-part-1.pdf) to Source Document nodes
            if doc_type == "Source Document":
                for src in fm.get("sources") or []:
                    if isinstance(src, dict) and src.get("resource"):
                        source_resource_to_doc_id[str(src["resource"]).strip()] = doc_id
                    if isinstance(src, dict) and src.get("title"):
                        source_resource_to_doc_id[str(src["title"]).strip()] = doc_id

            chunks.extend(
                _chunk_markdown_sections(
                    entity_id=doc_id,
                    entity_label="GovernanceDoc",
                    tag=tag,
                    title=title,
                    unit_code=None,
                    safety_classification=None,
                    has_conflict=has_conflict,
                    gcs_uri=gcs_uri,
                    description=description,
                    body=body,
                )
            )
            catalog_entries.append(
                CatalogEntrySpec(
                    entry_id=make_dataplex_entry_id("doc", slug),
                    spanner_entity_id=doc_id,
                    entity_type=doc_type,
                    tag=tag,
                    display_name=title[:200],
                    description=description[:1500],
                    unit_code="GOVERNANCE",
                    equipment_or_instrument_class=doc_type,
                    safety_classification="Process Safety Governance",
                    has_discrepancy_warning=has_conflict,
                    governing_standard_or_drawing=gov_std_str[:120],
                    gcs_markdown_uri=gcs_uri,
                    overview_markdown=body[:8000],
                    labels=labels,
                )
            )

    # Ensure every unit code referenced by Equipment exists in PlantUnits
    eq_by_tag: Dict[str, str] = {eq.tag: eq_id for eq_id, eq in equipment.items()}
    # Sort tags longest-first to prevent substring collisions (e.g. P-41A vs P-41)
    sorted_eq_tags = sorted(eq_by_tag.keys(), key=len, reverse=True)

    for eq_id, eq in equipment.items():
        codes = _split_unit_codes(eq.unit_code) or ["PLANT"]
        for idx, code in enumerate(codes):
            uid = f"UNIT:{code}"
            if uid not in units:
                units[uid] = PlantUnitNode(
                    unit_id=uid,
                    unit_code=code,
                    title=DEFAULT_UNIT_TITLES.get(code, f"Plant Subsystem {code}"),
                    facility="Seabrook Station",
                    safety_classification=eq.safety_classification,
                    description=f"Plant engineering subsystem {code} referenced by equipment specifications.",
                    has_warning=False,
                    gcs_uri=None,
                )
            edge_id = _edge_hash("UE", eq_id, uid)
            unit_edges_map[edge_id] = UnitEquipmentEdge(
                edge_id=edge_id,
                equipment_id=eq_id,
                unit_id=uid,
                relationship_role="PRIMARY_UNIT" if idx == 0 else "CROSS_TIE_UNIT",
            )

    def _resolve_endpoint_tags(raw_endpoint: str) -> List[Tuple[str, str]]:
        """
        Resolve a P&ID connection endpoint string to one or more (node_id, kind) pairs.
        Matches exact Equipment tags first, then embedded canonical Equipment tags inside
        compound labels (e.g., 'RH-P-8A / CBS-P-9A Suction' -> EQ:RH-P-8A), otherwise
        registers a ProcessBoundaryNode ('BND:...').
        """
        cleaned = (raw_endpoint or "UNSPECIFIED").strip()
        if cleaned in eq_by_tag:
            return [(eq_by_tag[cleaned], "EQUIPMENT")]

        matched_eqs: List[Tuple[str, str]] = []
        for etag in sorted_eq_tags:
            pattern = rf"(?<![A-Z0-9-]){re.escape(etag)}(?![A-Z0-9-])"
            if re.search(pattern, cleaned):
                matched_eqs.append((eq_by_tag[etag], "EQUIPMENT"))

        if matched_eqs:
            return matched_eqs

        norm_slug = re.sub(r"[^A-Z0-9]+", "-", cleaned.upper()).strip("-")[:96] or "EXTERNAL"
        bnd_id = f"BND:{norm_slug}"
        if bnd_id not in boundaries:
            boundaries[bnd_id] = ProcessBoundaryNode(
                boundary_id=bnd_id,
                tag=cleaned[:120],
                boundary_type=_classify_boundary(cleaned),
                description=f"P&ID process header, penetration, or system boundary: {cleaned}",
            )
        return [(bnd_id, "BOUNDARY")]

    # Identify HAZOP and RAM governance doc IDs for safety governance links
    hazop_doc_ids = [
        did
        for did, d in governance_docs.items()
        if "hazop" in did.lower() or "ram" in did.lower() or "risk-assessment" in did.lower()
    ]

    # Pass 2: Build FLOWS_TO, MONITORS, EXTRACTED_FROM, and GOVERNED_BY edges
    for path, rel_path, fm, body, _ in parsed_items:
        doc_type = str(fm.get("type") or "").strip()
        em = fm.get("entity_metadata") if isinstance(fm.get("entity_metadata"), dict) else {}
        has_conflict, _ = _detect_conflict(body)

        entity_id: Optional[str] = None
        entity_kind: Optional[str] = None
        if doc_type == "Equipment Concept":
            tag = str(em.get("tag") or path.stem).strip()
            entity_id = f"EQ:{tag}"
            entity_kind = "EQUIPMENT"

            # 2a. Inline instruments on Equipment -> InstrumentNodes + MONITORS edges
            for inst_item in em.get("instruments") or []:
                if not isinstance(inst_item, dict):
                    continue
                itag = str(inst_item.get("tag") or "").strip()
                if not itag:
                    continue
                inst_id = f"INST:{itag}"
                itype = str(inst_item.get("type") or "P&ID Loop Instrument").strip()
                loc = str(inst_item.get("location") or "").strip() or None
                setpoint = str(inst_item.get("setpoint_or_range") or "").strip() or None
                interlock = str(inst_item.get("interlock_or_alarm") or "").strip() or None
                src_dwg = str(inst_item.get("source") or "").strip() or None
                svc = str(inst_item.get("service") or f"Loop instrument on {tag}").strip()

                if inst_id not in instruments:
                    instruments[inst_id] = InstrumentNode(
                        instrument_id=inst_id,
                        tag=itag,
                        title=f"{itag} — {svc}"[:250],
                        instrument_type=itype[:120],
                        unit_code=str(em.get("unit") or "").strip() or None,
                        safety_classification=equipment[entity_id].safety_classification,
                        location=loc[:250] if loc else None,
                        setpoint_or_range=setpoint[:200] if setpoint else None,
                        interlock_or_alarm=interlock[:300] if interlock else None,
                        has_warning=False,
                        is_full_spec=False,
                        description=svc,
                        gcs_uri=None,
                    )
                medge_id = _edge_hash("MON", inst_id, entity_id, svc)
                monitor_edges_map[medge_id] = InstrumentMonitorEdge(
                    edge_id=medge_id,
                    instrument_id=inst_id,
                    equipment_id=entity_id,
                    loop_role="INTERLOCK_CONTROL" if (interlock and "interlock" in interlock.lower()) else "PROCESS_MONITORING",
                    location=loc[:250] if loc else None,
                    setpoint_or_range=setpoint[:200] if setpoint else None,
                    interlock_or_alarm=interlock[:300] if interlock else None,
                    source_drawing=src_dwg[:120] if src_dwg else None,
                )

            # 2b. P&ID Connections -> FLOWS_TO edges
            for idx, conn in enumerate(em.get("connections") or []):
                if not isinstance(conn, dict):
                    continue
                src_raw = str(conn.get("source_tag") or tag).strip()
                dst_raw = str(conn.get("target_tag") or tag).strip()
                stream_id = str(conn.get("stream_id") or f"{tag}-STR-{idx}").strip()
                direction = str(conn.get("direction") or "PROCESS").strip()
                line_size = str(conn.get("line_size") or "").strip() or None
                inline_val = conn.get("inline_components")
                if isinstance(inline_val, list):
                    inline_str = ", ".join(str(x) for x in inline_val if x) or None
                else:
                    inline_str = str(inline_val).strip() if inline_val else None
                temp = str(conn.get("temperature") or "").strip() or None
                press = str(conn.get("pressure") or "").strip() or None
                src_dwg = str(conn.get("source") or "").strip() or None
                desc = str(conn.get("description") or "").strip() or None

                src_endpoints = _resolve_endpoint_tags(src_raw)
                dst_endpoints = _resolve_endpoint_tags(dst_raw)
                for s_id, s_kind in src_endpoints:
                    for d_id, d_kind in dst_endpoints:
                        if s_id == d_id:
                            continue
                        # Property Graph supports Equipment<->Equipment, Boundary->Equipment, Equipment->Boundary
                        if s_kind == "BOUNDARY" and d_kind == "BOUNDARY":
                            # Anchor through the owning Equipment node
                            s_id, s_kind = entity_id, "EQUIPMENT"
                        fedge_id = _edge_hash("FLOW", s_id, d_id, stream_id, direction)
                        flow_edges_map[fedge_id] = FlowStreamEdge(
                            edge_id=fedge_id,
                            src_id=s_id,
                            dst_id=d_id,
                            src_kind=s_kind,
                            dst_kind=d_kind,
                            stream_id=stream_id[:120],
                            direction=direction[:64],
                            line_size=line_size[:120] if line_size else None,
                            inline_components=inline_str[:800] if inline_str else None,
                            temperature=temp[:120] if temp else None,
                            pressure=press[:120] if press else None,
                            source_drawing=src_dwg[:250] if src_dwg else None,
                            description=desc[:800] if desc else None,
                        )

        elif doc_type == "Instrument Specification":
            raw_tag = str(
                em.get("tag")
                or _extract_markdown_table_field(body, ["instrument tag"])
                or str(fm.get("title") or path.stem).split("—")[0].split("/")[0].strip()
            ).strip()
            tag = raw_tag.split("/")[0].strip()
            entity_id = f"INST:{tag}"
            entity_kind = "INSTRUMENT"

            # Link full Instrument Spec to referenced Equipment via Markdown links + frontmatter + tag scan
            linked_eq_ids: Set[str] = set()
            for m in re.findall(r"equipment/([A-Za-z0-9-]+)\.md", body):
                if m in eq_by_tag:
                    linked_eq_ids.add(eq_by_tag[m])
            for key in ("associated_equipment", "equipment"):
                val = em.get(key)
                if isinstance(val, list):
                    for item in val:
                        for s_id, s_kind in _resolve_endpoint_tags(str(item)):
                            if s_kind == "EQUIPMENT":
                                linked_eq_ids.add(s_id)
                elif isinstance(val, str):
                    for s_id, s_kind in _resolve_endpoint_tags(val):
                        if s_kind == "EQUIPMENT":
                            linked_eq_ids.add(s_id)
            if not linked_eq_ids:
                for etag in sorted_eq_tags:
                    if re.search(rf"(?<![A-Z0-9-]){re.escape(etag)}(?![A-Z0-9-])", body):
                        linked_eq_ids.add(eq_by_tag[etag])

            inst_node = instruments[entity_id]
            for target_eq_id in sorted(linked_eq_ids):
                medge_id = _edge_hash("MON", entity_id, target_eq_id, "SPEC_LINK")
                monitor_edges_map[medge_id] = InstrumentMonitorEdge(
                    edge_id=medge_id,
                    instrument_id=entity_id,
                    equipment_id=target_eq_id,
                    loop_role="SAFETY_INTERLOCK_SPEC" if inst_node.has_warning else "INSTRUMENT_SPEC",
                    location=inst_node.location,
                    setpoint_or_range=inst_node.setpoint_or_range,
                    interlock_or_alarm=inst_node.interlock_or_alarm,
                    source_drawing=None,
                )

        elif doc_type == "Unit Overview":
            # Match unit node created in Pass 1
            for uid, unode in units.items():
                if unode.gcs_uri and unode.gcs_uri.endswith(rel_path):
                    entity_id = uid
                    entity_kind = "UNIT"
                    break

        # 2c. Provenance Lineage (EXTRACTED_FROM -> Source Document GovernanceDocs)
        if entity_id and entity_kind:
            for src in fm.get("sources") or []:
                if not isinstance(src, dict):
                    continue
                res = str(src.get("resource") or "").strip()
                stitle = str(src.get("title") or "").strip()
                target_doc_id = source_resource_to_doc_id.get(res) or source_resource_to_doc_id.get(stitle)
                if target_doc_id and target_doc_id in governance_docs:
                    ledge_id = _edge_hash("LIN", entity_id, target_doc_id, res or stitle)
                    lineage_edges_map[ledge_id] = DocumentLineageEdge(
                        edge_id=ledge_id,
                        entity_id=entity_id,
                        entity_kind=entity_kind,
                        doc_id=target_doc_id,
                        source_ref=(res or stitle)[:250],
                        has_conflict=has_conflict,
                    )

            # 2d. Safety & HAZOP Governance (GOVERNED_BY -> HAZOP / RAM standards)
            if entity_kind in ("EQUIPMENT", "INSTRUMENT") and has_conflict:
                for hdoc_id in hazop_doc_ids:
                    gedge_id = _edge_hash("GOV", entity_id, hdoc_id)
                    governance_edges_map[gedge_id] = SafetyGovernanceEdge(
                        edge_id=gedge_id,
                        entity_id=entity_id,
                        entity_kind=entity_kind,
                        doc_id=hdoc_id,
                        governance_reason="Requires IEC 61882 HAZOP / RAM discrepancy & safeguard verification",
                    )

    return ParsedOkfBundle(
        units=units,
        equipment=equipment,
        instruments=instruments,
        boundaries=boundaries,
        governance_docs=governance_docs,
        unit_edges=sorted(unit_edges_map.values(), key=lambda e: e.edge_id),
        flow_edges=sorted(flow_edges_map.values(), key=lambda e: e.edge_id),
        monitor_edges=sorted(monitor_edges_map.values(), key=lambda e: e.edge_id),
        lineage_edges=sorted(lineage_edges_map.values(), key=lambda e: e.edge_id),
        governance_edges=sorted(governance_edges_map.values(), key=lambda e: e.edge_id),
        chunks=chunks,
        catalog_entries=sorted(catalog_entries, key=lambda c: c.entry_id),
    )
