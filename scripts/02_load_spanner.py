#!/usr/bin/env python3
"""Load OKF v0.2 nodes, typed relationships, and chunks into Cloud Spanner."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import random
import sys
import time
from typing import Callable, Sequence, Tuple, TypeVar

from google.api_core import exceptions as gcp_exceptions
from google.cloud import spanner

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "src"))

from okf_kg.config import DemoSettings, load_settings
from okf_kg.parser import parse_okf_bundle
from okf_kg.rrf import chunk_batches
from okf_kg.sql_templates import render_ddl_statements

T = TypeVar("T")


def _run_with_backoff(fn: Callable[[], T], max_attempts: int = 5, label: str = "spanner_op") -> T:
    for attempt in range(1, max_attempts + 1):
        try:
            return fn()
        except (
            gcp_exceptions.ServiceUnavailable,
            gcp_exceptions.ResourceExhausted,
            gcp_exceptions.DeadlineExceeded,
            gcp_exceptions.Aborted,
        ) as exc:
            if attempt >= max_attempts:
                print(
                    json.dumps(
                        {
                            "status": "UPSTREAM_UNAVAILABLE_DEGRADED",
                            "operation": label,
                            "attempts": attempt,
                            "error": str(exc),
                        }
                    ),
                    file=sys.stderr,
                )
                raise SystemExit(3) from exc
            sleep_s = min(30.0, (2 ** (attempt - 1)) + random.uniform(0.1, 0.7))
            print(f"[RETRY] {label} attempt {attempt}/{max_attempts} after {sleep_s:.1f}s ({exc})")
            time.sleep(sleep_s)
    raise RuntimeError("Unreachable")


def _existing_tables(database) -> set[str]:
    with database.snapshot() as snap:
        rows = snap.execute_sql(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = ''"
        )
        return {r[0] for r in rows}


def apply_base_schema(database, settings: DemoSettings, skip_if_present: bool = False) -> None:
    existing = _existing_tables(database)
    if skip_if_present and "OkfChunks" in existing and "Equipment" in existing:
        print("[DDL] Base tables already present in Spanner; skipping 01_schema.sql.")
        return

    ddl_statements = render_ddl_statements(REPO_ROOT / "sql" / "01_schema.sql", settings)
    print(f"[DDL] Applying {len(ddl_statements)} DDL statements from sql/01_schema.sql...")
    op = database.update_ddl(ddl_statements)
    op.result(timeout=600)
    print("[DDL] Base Spanner schema + PlantKnowledgeGraph + OkfEmbeddingModel applied.")


def _upsert_rows(
    database,
    table: str,
    columns: Sequence[str],
    rows: Sequence[Tuple],
    batch_size: int,
    max_attempts: int,
) -> int:
    if not rows:
        return 0
    batches = chunk_batches(rows, batch_size=batch_size, cols_per_row=len(columns))
    for b in batches:
        def _write(batch_rows=b):
            with database.batch() as batch:
                batch.insert_or_update(table=table, columns=columns, values=batch_rows)

        _run_with_backoff(_write, max_attempts=max_attempts, label=f"upsert:{table}")
    return len(rows)


def main() -> int:
    ap = argparse.ArgumentParser(description="Apply Spanner DDL and load OKF Graph + Chunks")
    ap.add_argument("--env-file", type=Path, default=None, help="Optional path to .env file")
    ap.add_argument("--env", choices=["nonprod", "prod"], default=None, help="Override ACTIVE_ENV")
    ap.add_argument("--ddl-only", action="store_true", help="Apply sql/01_schema.sql and exit")
    ap.add_argument("--ddl-if-missing", action="store_true", help="Apply sql/01_schema.sql only if tables missing")
    ap.add_argument("--dry-run", action="store_true", help="Parse okf_bundle and validate DDL locally without GCP calls")
    args = ap.parse_args()

    settings = load_settings(env_file=args.env_file, override_env=args.env)
    bundle_path = (
        settings.okf_bundle_dir
        if settings.okf_bundle_dir.is_absolute()
        else REPO_ROOT / settings.okf_bundle_dir
    )
    bundle = parse_okf_bundle(
        bundle_dir=bundle_path,
        gcs_bucket=settings.gcs_bucket,
        gcs_prefix=settings.gcs_prefix,
    )
    ddl_statements = render_ddl_statements(REPO_ROOT / "sql" / "01_schema.sql", settings)

    summary = {
        "project": settings.gcp_project,
        "region": settings.gcp_region,
        "spanner_instance": settings.spanner_instance,
        "spanner_database": settings.spanner_database,
        "ddl_statements": len(ddl_statements),
        "units": len(bundle.units),
        "equipment": len(bundle.equipment),
        "instruments": len(bundle.instruments),
        "process_boundaries": len(bundle.boundaries),
        "governance_docs": len(bundle.governance_docs),
        "unit_edges": len(bundle.unit_edges),
        "flow_edges": len(bundle.flow_edges),
        "monitor_edges": len(bundle.monitor_edges),
        "lineage_edges": len(bundle.lineage_edges),
        "governance_edges": len(bundle.governance_edges),
        "chunks": len(bundle.chunks),
    }
    print(json.dumps({"event": "okf_parsed", **summary}, indent=2))

    if args.dry_run:
        return 0

    client = spanner.Client(project=settings.gcp_project)
    instance = client.instance(settings.spanner_instance)
    database = instance.database(settings.spanner_database)

    if args.ddl_only:
        apply_base_schema(database, settings, skip_if_present=False)
        return 0
    if args.ddl_if_missing:
        apply_base_schema(database, settings, skip_if_present=True)
        return 0

    apply_base_schema(database, settings, skip_if_present=True)

    commit_ts = spanner.COMMIT_TIMESTAMP
    bsize = settings.spanner_mutation_batch_size
    retries = settings.max_retry_attempts

    # 1. Node Tables
    _upsert_rows(
        database,
        "PlantUnits",
        ["UnitId", "UnitCode", "Title", "Facility", "SafetyClassification", "Description", "HasWarning", "GcsUri", "UpdatedAt"],
        [
            (u.unit_id, u.unit_code, u.title, u.facility, u.safety_classification, u.description, u.has_warning, u.gcs_uri, commit_ts)
            for u in bundle.units.values()
        ],
        bsize,
        retries,
    )
    _upsert_rows(
        database,
        "Equipment",
        ["EquipmentId", "Tag", "Title", "EquipmentClass", "UnitCode", "SafetyClassification", "HasConflict", "ConflictSummary", "Description", "GcsUri", "UpdatedAt"],
        [
            (e.equipment_id, e.tag, e.title, e.equipment_class, e.unit_code, e.safety_classification, e.has_conflict, e.conflict_summary, e.description, e.gcs_uri, commit_ts)
            for e in bundle.equipment.values()
        ],
        bsize,
        retries,
    )
    _upsert_rows(
        database,
        "Instruments",
        ["InstrumentId", "Tag", "Title", "InstrumentType", "UnitCode", "SafetyClassification", "Location", "SetpointOrRange", "InterlockOrAlarm", "HasWarning", "IsFullSpec", "Description", "GcsUri", "UpdatedAt"],
        [
            (i.instrument_id, i.tag, i.title, i.instrument_type, i.unit_code, i.safety_classification, i.location, i.setpoint_or_range, i.interlock_or_alarm, i.has_warning, i.is_full_spec, i.description, i.gcs_uri, commit_ts)
            for i in bundle.instruments.values()
        ],
        bsize,
        retries,
    )
    _upsert_rows(
        database,
        "ProcessBoundaries",
        ["BoundaryId", "Tag", "BoundaryType", "Description", "UpdatedAt"],
        [(b.boundary_id, b.tag, b.boundary_type, b.description, commit_ts) for b in bundle.boundaries.values()],
        bsize,
        retries,
    )
    _upsert_rows(
        database,
        "GovernanceDocs",
        ["DocId", "DocType", "Tag", "Title", "GoverningStandard", "HasWarning", "Description", "GcsUri", "UpdatedAt"],
        [(d.doc_id, d.doc_type, d.tag, d.title, d.governing_standard, d.has_warning, d.description, d.gcs_uri, commit_ts) for d in bundle.governance_docs.values()],
        bsize,
        retries,
    )
    print("[SPANNER] All 5 Domain Node tables loaded.")

    # 2. Edge Tables
    _upsert_rows(
        database,
        "UnitEquipment",
        ["EdgeId", "EquipmentId", "UnitId", "RelationshipRole"],
        [(e.edge_id, e.equipment_id, e.unit_id, e.relationship_role) for e in bundle.unit_edges],
        bsize,
        retries,
    )

    flow_cols = ["EdgeId", "SrcId", "DstId", "StreamId", "Direction", "LineSize", "InlineComponents", "Temperature", "Pressure", "SourceDrawing", "Description"]
    eq_flows = [e for e in bundle.flow_edges if e.src_kind == "EQUIPMENT" and e.dst_kind == "EQUIPMENT"]
    bnd_to_eq = [e for e in bundle.flow_edges if e.src_kind == "BOUNDARY" and e.dst_kind == "EQUIPMENT"]
    eq_to_bnd = [e for e in bundle.flow_edges if e.src_kind == "EQUIPMENT" and e.dst_kind == "BOUNDARY"]

    for tbl_name, edge_subset in (
        ("EquipmentFlows", eq_flows),
        ("BoundaryToEquipmentFlows", bnd_to_eq),
        ("EquipmentToBoundaryFlows", eq_to_bnd),
    ):
        _upsert_rows(
            database,
            tbl_name,
            flow_cols,
            [
                (e.edge_id, e.src_id, e.dst_id, e.stream_id, e.direction, e.line_size, e.inline_components, e.temperature, e.pressure, e.source_drawing, e.description)
                for e in edge_subset
            ],
            bsize,
            retries,
        )

    _upsert_rows(
        database,
        "InstrumentMonitorsEquipment",
        ["EdgeId", "InstrumentId", "EquipmentId", "LoopRole", "Location", "SetpointOrRange", "InterlockOrAlarm", "SourceDrawing"],
        [
            (e.edge_id, e.instrument_id, e.equipment_id, e.loop_role, e.location, e.setpoint_or_range, e.interlock_or_alarm, e.source_drawing)
            for e in bundle.monitor_edges
        ],
        bsize,
        retries,
    )

    lin_cols = ["EdgeId", "EntityId", "DocId", "SourceRef", "HasConflict"]
    for tbl_name, kind in (
        ("EquipmentDocumentLineage", "EQUIPMENT"),
        ("InstrumentDocumentLineage", "INSTRUMENT"),
        ("UnitDocumentLineage", "UNIT"),
    ):
        _upsert_rows(
            database,
            tbl_name,
            lin_cols,
            [(e.edge_id, e.entity_id, e.doc_id, e.source_ref, e.has_conflict) for e in bundle.lineage_edges if e.entity_kind == kind],
            bsize,
            retries,
        )

    gov_cols = ["EdgeId", "EntityId", "DocId", "GovernanceReason"]
    for tbl_name, kind in (
        ("EquipmentSafetyGovernance", "EQUIPMENT"),
        ("InstrumentSafetyGovernance", "INSTRUMENT"),
    ):
        _upsert_rows(
            database,
            gov_cols and tbl_name,
            gov_cols,
            [(e.edge_id, e.entity_id, e.doc_id, e.governance_reason) for e in bundle.governance_edges if e.entity_kind == kind],
            bsize,
            retries,
        )
    print("[SPANNER] All 10 Typed Relationship Edge tables loaded.")

    # 3. Hybrid Search Chunks (preserve existing Embedding if re-run by checking existing ChunkIds)
    existing_embedded_ids: set[str] = set()
    with database.snapshot() as snap:
        for row in snap.execute_sql("SELECT ChunkId FROM OkfChunks WHERE Embedding IS NOT NULL"):
            existing_embedded_ids.add(row[0])

    chunks_without_embed = [c for c in bundle.chunks if c.chunk_id not in existing_embedded_ids]
    chunks_already_embedded = [c for c in bundle.chunks if c.chunk_id in existing_embedded_ids]

    if chunks_without_embed:
        _upsert_rows(
            database,
            "OkfChunks",
            ["ChunkId", "EntityId", "EntityLabel", "ChunkIndex", "SectionHeading", "Tag", "Title", "UnitCode", "SafetyClassification", "HasConflict", "GcsUri", "ChunkText", "UpdatedAt"],
            [
                (c.chunk_id, c.entity_id, c.entity_label, c.chunk_index, c.section_heading, c.tag, c.title, c.unit_code, c.safety_classification, c.has_conflict, c.gcs_uri, c.chunk_text, commit_ts)
                for c in chunks_without_embed
            ],
            bsize,
            retries,
        )
    if chunks_already_embedded:
        # Update metadata columns without wiping already computed Embedding column
        _upsert_rows(
            database,
            "OkfChunks",
            ["ChunkId", "EntityId", "EntityLabel", "ChunkIndex", "SectionHeading", "Tag", "Title", "UnitCode", "SafetyClassification", "HasConflict", "GcsUri", "ChunkText", "UpdatedAt"],
            [
                (c.chunk_id, c.entity_id, c.entity_label, c.chunk_index, c.section_heading, c.tag, c.title, c.unit_code, c.safety_classification, c.has_conflict, c.gcs_uri, c.chunk_text, commit_ts)
                for c in chunks_already_embedded
            ],
            bsize,
            retries,
        )

    print(
        f"[SPANNER] Loaded {len(bundle.chunks)} OkfChunks "
        f"({len(existing_embedded_ids)} already had embeddings preserved)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
