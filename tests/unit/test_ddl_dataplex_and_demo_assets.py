"""Deterministic unit tests for Spanner DDL templates, Dataplex builders, and Demo queries."""

from __future__ import annotations

from pathlib import Path
import re

from okf_kg.config import load_settings
from okf_kg.dataplex_builder import (
    ALLOWED_DATAPLEX_TYPE_ALIASES,
    CANONICAL_GLOSSARY_TERMS,
    build_dataplex_entry,
    build_okf_aspect_type,
    build_okf_entry_group,
    build_okf_entry_type,
)
from okf_kg.parser import parse_okf_bundle
from okf_kg.sql_templates import render_ddl_statements

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_spanner_ddl_rendering_and_graph_schema() -> None:
    settings = load_settings(env_file=REPO_ROOT / ".env.example", override_env="nonprod", extra_environ={})
    stmts = render_ddl_statements(REPO_ROOT / "sql" / "01_schema.sql", settings)
    joined = ";\n".join(stmts)

    assert "${" not in joined
    assert "CREATE MODEL OkfEmbeddingModel" in joined
    assert "projects/your-gcp-project-id/locations/asia-southeast1/publishers/google/models/text-embedding-005" in joined
    assert "CREATE OR REPLACE PROPERTY GRAPH PlantKnowledgeGraph" in joined
    assert "CREATE SEARCH INDEX OkfChunksSearchIdx" in joined
    assert "TOKENLIST_CONCAT" not in joined

    for table_name in (
        "PlantUnits",
        "Equipment",
        "Instruments",
        "ProcessBoundaries",
        "GovernanceDocs",
        "UnitEquipment",
        "EquipmentFlows",
        "BoundaryToEquipmentFlows",
        "EquipmentToBoundaryFlows",
        "InstrumentMonitorsEquipment",
        "EquipmentDocumentLineage",
        "InstrumentDocumentLineage",
        "UnitDocumentLineage",
        "EquipmentSafetyGovernance",
        "InstrumentSafetyGovernance",
        "OkfChunks",
    ):
        assert f"CREATE TABLE {table_name}" in joined

    vec_stmts = render_ddl_statements(REPO_ROOT / "sql" / "02_vector_index.sql", settings)
    assert len(vec_stmts) == 1
    assert "CREATE VECTOR INDEX" in vec_stmts[0]
    assert "WHERE Embedding IS NOT NULL" in vec_stmts[0]


def test_dataplex_catalog_protobufs_for_all_100_entries() -> None:
    settings = load_settings(env_file=REPO_ROOT / ".env.example", override_env="nonprod", extra_environ={})
    bundle = parse_okf_bundle(REPO_ROOT / "okf_bundle", gcs_bucket=settings.gcs_bucket, gcs_prefix=settings.gcs_prefix)

    aspect_type = build_okf_aspect_type(settings)
    assert len(aspect_type.metadata_template.record_fields) == 9
    entry_group = build_okf_entry_group(settings)
    assert "Seabrook" in entry_group.description
    entry_type = build_okf_entry_type(settings)
    assert len(entry_type.required_aspects) == 1
    assert set(entry_type.type_aliases) <= ALLOWED_DATAPLEX_TYPE_ALIASES
    assert len(CANONICAL_GLOSSARY_TERMS) >= 8

    expected_aspect_key = "your-gcp-project-id.asia-southeast1.okf-plant-asset-aspect"
    seen_entry_ids = set()
    for spec in bundle.catalog_entries:
        assert re.match(r"^[a-z0-9][a-z0-9-]{0,62}$", spec.entry_id)
        assert spec.entry_id not in seen_entry_ids
        seen_entry_ids.add(spec.entry_id)

        proto = build_dataplex_entry(spec, settings)
        assert expected_aspect_key in proto.aspects
        aspect_data = dict(proto.aspects[expected_aspect_key].data)
        assert aspect_data["tag"] == spec.tag
        assert aspect_data["entity_type"] == spec.entity_type
        assert isinstance(aspect_data["has_discrepancy_warning"], bool)
        assert str(aspect_data["gcs_markdown_uri"]).startswith("gs://your-gcp-project-id-okf-bundle/")


def test_demo_queries_and_playbook_reference_real_entities() -> None:
    bundle = parse_okf_bundle(REPO_ROOT / "okf_bundle")
    known_tags = (
        {e.tag for e in bundle.equipment.values()}
        | {i.tag for i in bundle.instruments.values()}
        | {u.unit_code for u in bundle.units.values()}
    )

    demo_sql = (REPO_ROOT / "sql" / "demo_queries_spanner.sql").read_text(encoding="utf-8")
    demo_doc = (REPO_ROOT / "docs" / "DEMO_SCRIPT_AND_INTRO.md").read_text(encoding="utf-8")

    for tag in ("CBS-TK-10A", "CBS-TK-101A", "CBS-EP-36A", "RH-P-8A", "RH-E-9A", "FIS-610", "FIS-7325", "DM-8"):
        assert tag in known_tags
        assert tag in demo_doc

    assert "ML.PREDICT" in demo_sql
    assert "PlantKnowledgeGraph" in demo_sql
    assert "OkfChunks" in demo_sql
