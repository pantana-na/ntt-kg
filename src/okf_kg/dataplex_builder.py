"""Builders for Google Cloud Dataplex Knowledge Catalog (Universal Catalog) protobufs."""

from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Dict, List

from google.cloud import dataplex_v1
from google.protobuf import struct_pb2

from .config import DemoSettings
from .models import CatalogEntrySpec


@dataclass(frozen=True)
class GlossaryTermSpec:
    term_id: str
    display_name: str
    description: str


CANONICAL_GLOSSARY_TERMS: List[GlossaryTermSpec] = [
    GlossaryTermSpec(
        term_id="safety-injection-system",
        display_name="Safety Injection System (SI / ECCS)",
        description=(
            "Multi-tier Emergency Core Cooling System (High Head CS-P-2A/B, Intermediate Head SI-P-6A/B, "
            "and Low Head RHR RH-P-8A/B) delivering borated coolant to the Reactor Coolant System during LOCAs."
        ),
    ),
    GlossaryTermSpec(
        term_id="residual-heat-removal",
        display_name="Residual Heat Removal (RHR)",
        description=(
            "Dual-purpose nuclear safety subsystem removing decay heat during normal reactor shutdown/cooldown "
            "via RH-P-8A/B and RH-E-9A/B and providing low-head safety injection from Containment Sumps CBS-TK-10A/B."
        ),
    ),
    GlossaryTermSpec(
        term_id="containment-recirculation-sump",
        display_name="Containment Recirculation Sump (CBS-TK-10A / 10B)",
        description=(
            "Safety Class 2 post-LOCA emergency suction reservoir inside containment enclosed externally by "
            "Protective Chambers CBS-TK-101A/B, Expansion Bellows CBS-EP-36A/B, and leak switches LS-2356/2357."
        ),
    ),
    GlossaryTermSpec(
        term_id="spent-fuel-pool-cleanup",
        display_name="Spent Fuel Pool Cooling & Cleanup (SF)",
        description=(
            "Purification and cooling loop using Skimmer Pump P-12, Prefilter F-33, Deep-Bed Demineralizer DM-8, "
            "and Postfilter F-34 to maintain boron chemistry, water clarity, and radionuclide removal."
        ),
    ),
    GlossaryTermSpec(
        term_id="service-water-ultimate-heat-sink",
        display_name="Service Water & Ultimate Heat Sink (SW / SWA)",
        description=(
            "Safety-related open-loop cooling system transferring heat from CC-E-17A/B and Diesel Generators DG-E-42A/B "
            "to the Atlantic Ocean (P-41A..D) or Cooling Tower backup (P-110A/B, FN-51A/B)."
        ),
    ),
    GlossaryTermSpec(
        term_id="hazop-guide-words",
        display_name="HAZOP Guide Words (IEC 61882)",
        description=(
            "Structured process hazard analysis prompts (No/Not, More, Less, As Well As, Part Of, Reverse, Other Than, "
            "Early, Late, Before, After) combined with process parameters to uncover design deviations and safeguards."
        ),
    ),
    GlossaryTermSpec(
        term_id="risk-assessment-code",
        display_name="Risk Assessment Matrix & Code (RAM / RAC)",
        description=(
            "Qualitative risk ranking standard combining Severity and Probability levels into a Risk Assessment Code "
            "(RAC) to prioritize engineered interlocks and operational mitigations."
        ),
    ),
    GlossaryTermSpec(
        term_id="open-knowledge-format",
        display_name="Open Knowledge Format (OKF v0.2)",
        description=(
            "Structured YAML-frontmatter + Markdown engineering knowledge representation capturing verified P&ID "
            "equipment, instruments, stream connections, source lineage, and cross-drawing safety discrepancies."
        ),
    ),
]


def sanitize_dataplex_labels(raw_tags: List[str]) -> Dict[str, str]:
    """Convert OKF tags into valid GCP resource labels (lowercase `[a-z0-9_-]{1,63}`)."""
    labels: Dict[str, str] = {"corpus": "okf-v0-2", "domain": "plant-engineering"}
    for idx, tag in enumerate(raw_tags[:8]):
        val = re.sub(r"[^a-z0-9_-]+", "-", tag.lower()).strip("-_")[:63]
        if val:
            labels[f"tag_{idx + 1}"] = val
    return labels


def build_okf_aspect_type(settings: DemoSettings) -> dataplex_v1.AspectType:
    """Construct the Dataplex Custom AspectType schema (`okf-plant-asset-aspect`)."""
    fields = [
        dataplex_v1.AspectType.MetadataTemplate(
            name="entity_type",
            type_="string",
            index=1,
            annotations=dataplex_v1.AspectType.MetadataTemplate.Annotations(
                description="OKF Concept Type (Equipment Concept, Instrument Specification, Unit Overview, HAZOP Protocol, etc.)"
            ),
            constraints=dataplex_v1.AspectType.MetadataTemplate.Constraints(required=True),
        ),
        dataplex_v1.AspectType.MetadataTemplate(
            name="tag",
            type_="string",
            index=2,
            annotations=dataplex_v1.AspectType.MetadataTemplate.Annotations(
                description="Canonical P&ID or engineering tag (e.g., 1-SS-E-14A, RH-E-9A, FIS-610)"
            ),
            constraints=dataplex_v1.AspectType.MetadataTemplate.Constraints(required=True),
        ),
        dataplex_v1.AspectType.MetadataTemplate(
            name="unit_code",
            type_="string",
            index=3,
            annotations=dataplex_v1.AspectType.MetadataTemplate.Annotations(
                description="Plant unit / subsystem code (SI, RH, CS, CBS, SW, SWA, SF, SS, CC, SCC, DG)"
            ),
        ),
        dataplex_v1.AspectType.MetadataTemplate(
            name="equipment_or_instrument_class",
            type_="string",
            index=4,
            annotations=dataplex_v1.AspectType.MetadataTemplate.Annotations(
                description="Asset class (Pump, Heat Exchanger, Vessel, Filter, Flow Indicating Switch, etc.)"
            ),
        ),
        dataplex_v1.AspectType.MetadataTemplate(
            name="safety_classification",
            type_="string",
            index=5,
            annotations=dataplex_v1.AspectType.MetadataTemplate.Annotations(
                description="Nuclear / process safety class (e.g., Safety Class 2, Safety Class 3, Safety Class NNS)"
            ),
        ),
        dataplex_v1.AspectType.MetadataTemplate(
            name="has_discrepancy_warning",
            type_="bool",
            index=6,
            annotations=dataplex_v1.AspectType.MetadataTemplate.Annotations(
                description="True if cross-drawing P&ID conflict or critical process safety warning is flagged"
            ),
            constraints=dataplex_v1.AspectType.MetadataTemplate.Constraints(required=True),
        ),
        dataplex_v1.AspectType.MetadataTemplate(
            name="governing_standard_or_drawing",
            type_="string",
            index=7,
            annotations=dataplex_v1.AspectType.MetadataTemplate.Annotations(
                description="Primary P&ID drawing numbers (PID-1-SI-LR20448) or governing standard (IEC 61882)"
            ),
        ),
        dataplex_v1.AspectType.MetadataTemplate(
            name="gcs_markdown_uri",
            type_="string",
            index=8,
            annotations=dataplex_v1.AspectType.MetadataTemplate.Annotations(
                description="Cloud Storage URI of the canonical OKF Markdown specification"
            ),
        ),
        dataplex_v1.AspectType.MetadataTemplate(
            name="spanner_entity_id",
            type_="string",
            index=9,
            annotations=dataplex_v1.AspectType.MetadataTemplate.Annotations(
                description="Primary key in Cloud Spanner PlantKnowledgeGraph (e.g., EQ:RH-E-9A, INST:FIS-610)"
            ),
            constraints=dataplex_v1.AspectType.MetadataTemplate.Constraints(required=True),
        ),
    ]

    template = dataplex_v1.AspectType.MetadataTemplate(
        name="okf_plant_asset_template",
        type_="record",
        record_fields=fields,
    )

    return dataplex_v1.AspectType(
        display_name="OKF Plant Engineering Asset Aspect",
        description=(
            "Structured engineering metadata extracted from Open Knowledge Format (OKF v0.2) "
            "for P&ID equipment, safety instruments, plant units, and HAZOP governance documents."
        ),
        metadata_template=template,
        labels={
            "env": settings.environment_name,
            "service": settings.finops_service,
            "owner": settings.finops_owner,
            "cost_center": settings.finops_cost_center,
        },
    )


def build_okf_entry_group(settings: DemoSettings) -> dataplex_v1.EntryGroup:
    return dataplex_v1.EntryGroup(
        display_name="OKF Plant Engineering Knowledge Catalog",
        description=(
            "Seabrook Station P&ID Equipment, Safety Interlock Instruments, Plant Units, "
            "and IEC 61882 HAZOP / Risk Assessment Standards synchronized with Spanner Knowledge Graph."
        ),
        labels={
            "env": settings.environment_name,
            "service": settings.finops_service,
            "owner": settings.finops_owner,
            "cost_center": settings.finops_cost_center,
        },
    )


ALLOWED_DATAPLEX_TYPE_ALIASES = frozenset(
    {
        "AGENT", "BUCKET", "CATALOG", "CLUSTER", "CODE_ASSET", "CONNECTION",
        "CONNECTION_PROFILE", "CONTEXT", "DASHBOARD", "DASHBOARD_ELEMENT",
        "DATABASE", "DATABASE_SCHEMA", "DATASET", "DATA_DOMAIN", "DATA_EXCHANGE",
        "DATA_PRODUCT", "DATA_SOURCE_CONNECTION", "DATA_STREAM", "EDGE", "EXPLORE",
        "FEATURE_GROUP", "FEATURE_ONLINE_STORE", "FEATURE_VIEW", "FILESET", "FOLDER",
        "FUNCTION", "GLOSSARY", "GLOSSARY_CATEGORY", "GLOSSARY_TERM", "GRAPH",
        "INSTANCE", "LISTING", "LOOK", "LOOKML_DASHBOARD", "LOOKML_DASHBOARD_ELEMENT",
        "LOOKML_PROJECT", "MODEL", "NAMESPACE", "NODE", "PIPELINE", "POLICY",
        "PROCEDURE", "REPOSITORY", "RESOURCE", "ROUTINE", "RULE_TEMPLATE",
        "SERVICE", "TABLE", "TOPIC", "TYPE", "VIEW",
    }
)


def build_okf_entry_type(settings: DemoSettings) -> dataplex_v1.EntryType:
    aspect_type_path = (
        f"projects/{settings.gcp_project}/locations/{settings.dataplex_location}"
        f"/aspectTypes/{settings.dataplex_aspect_type}"
    )
    return dataplex_v1.EntryType(
        display_name="OKF Plant Knowledge Asset",
        description="Plant engineering equipment, safety instrument, unit overview, or HAZOP standard entry.",
        platform="Google Cloud Spanner + GCS",
        system="Open Knowledge Format (OKF v0.2)",
        type_aliases=["NODE", "RESOURCE"],
        required_aspects=[
            dataplex_v1.EntryType.AspectInfo(type_=aspect_type_path),
        ],
        labels={
            "env": settings.environment_name,
            "service": settings.finops_service,
        },
    )


def build_dataplex_entry(spec: CatalogEntrySpec, settings: DemoSettings) -> dataplex_v1.Entry:
    """Construct a Dataplex `Entry` with Custom Aspect + rich EntrySource for Natural Language Search."""
    entry_type_path = (
        f"projects/{settings.gcp_project}/locations/{settings.dataplex_location}"
        f"/entryTypes/{settings.dataplex_entry_type}"
    )
    aspect_type_path = (
        f"projects/{settings.gcp_project}/locations/{settings.dataplex_location}"
        f"/aspectTypes/{settings.dataplex_aspect_type}"
    )
    aspect_key = f"{settings.gcp_project}.{settings.dataplex_location}.{settings.dataplex_aspect_type}"

    aspect_struct = struct_pb2.Struct()
    aspect_struct.update(
        {
            "entity_type": spec.entity_type,
            "tag": spec.tag,
            "unit_code": spec.unit_code or "PLANT",
            "equipment_or_instrument_class": spec.equipment_or_instrument_class or "Asset",
            "safety_classification": spec.safety_classification or "Unspecified",
            "has_discrepancy_warning": bool(spec.has_discrepancy_warning),
            "governing_standard_or_drawing": spec.governing_standard_or_drawing or "Seabrook LR P&ID",
            "gcs_markdown_uri": spec.gcs_markdown_uri,
            "spanner_entity_id": spec.spanner_entity_id,
        }
    )

    aspects_map: Dict[str, dataplex_v1.Aspect] = {
        aspect_key: dataplex_v1.Aspect(
            aspect_type=aspect_type_path,
            data=aspect_struct,
        )
    }

    fqn_slug = re.sub(r"[^a-zA-Z0-9_.-]+", "_", spec.spanner_entity_id)
    return dataplex_v1.Entry(
        entry_type=entry_type_path,
        fully_qualified_name=f"custom:okf.{settings.gcp_project}.{fqn_slug}",
        entry_source=dataplex_v1.EntrySource(
            resource=spec.gcs_markdown_uri,
            system="Open Knowledge Format (OKF v0.2)",
            platform="Spanner Knowledge Graph",
            display_name=spec.display_name[:200],
            description=spec.description[:1500],
            location=settings.gcp_region,
            labels=sanitize_dataplex_labels(spec.labels),
        ),
        aspects=aspects_map,
    )
