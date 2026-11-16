"""Deterministic unit tests for unified .env config and OKF v0.2 parser."""

from __future__ import annotations

from pathlib import Path
import pytest

from okf_kg.config import load_settings
from okf_kg.parser import parse_okf_bundle

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_load_settings_nonprod_and_prod() -> None:
    env_example = REPO_ROOT / ".env.example"
    nonprod = load_settings(env_file=env_example, override_env="nonprod", extra_environ={})
    assert nonprod.gcp_project == "your-gcp-project-id"
    assert nonprod.gcp_region == "asia-southeast1"
    assert nonprod.embedding_model == "text-embedding-005"
    assert nonprod.embedding_dimension == 768
    assert nonprod.github_repo == "https://github.com/pantana-na/ntt-kg.git"
    assert nonprod.spanner_instance == "ntt-kg-demo"
    assert nonprod.spanner_processing_units == 100
    assert nonprod.spanner_edition == "ENTERPRISE"
    assert "asia-southeast1/publishers/google/models/text-embedding-005" in nonprod.spanner_model_endpoint

    prod = load_settings(env_file=env_example, override_env="prod", extra_environ={})
    assert prod.environment_name == "production"
    assert prod.spanner_instance == "ntt-kg-prod"
    assert prod.spanner_processing_units == 1000


def test_load_settings_rejects_invalid_env_or_pu() -> None:
    env_example = REPO_ROOT / ".env.example"
    with pytest.raises(ValueError, match="ACTIVE_ENV"):
        load_settings(env_file=env_example, override_env="staging", extra_environ={})

    with pytest.raises(ValueError, match="multiple of 100"):
        load_settings(
            env_file=env_example,
            override_env="nonprod",
            extra_environ={"NONPROD_SPANNER_PROCESSING_UNITS": "50"},
        )

    with pytest.raises(ValueError, match="SPANNER_DISPLAY_NAME"):
        load_settings(
            env_file=env_example,
            override_env="nonprod",
            extra_environ={"NONPROD_SPANNER_DISPLAY_NAME": "This Display Name Exceeds Thirty Characters Limit"},
        )


def test_real_okf_bundle_counts_and_foreign_key_integrity() -> None:
    bundle = parse_okf_bundle(REPO_ROOT / "okf_bundle")

    # Exact domain entity counts from okf_bundle
    assert len(bundle.equipment) == 61
    assert len(bundle.catalog_entries) == 100
    assert sum(1 for i in bundle.instruments.values() if i.is_full_spec) == 24
    assert len(bundle.instruments) >= 200
    assert len(bundle.governance_docs) == 11
    assert len(bundle.units) >= 10
    assert len(bundle.chunks) >= 500

    # Verify cross-drawing engineering conflict detection on RH-E-9A & RH-E-9B
    assert bundle.equipment["EQ:RH-E-9A"].has_conflict is True
    assert bundle.equipment["EQ:RH-E-9B"].has_conflict is True
    assert "PID-1-SI-LR20448" in (bundle.equipment["EQ:RH-E-9A"].conflict_summary or "")

    # Verify compound stream resolution creates direct Equipment -> Equipment hops
    eq_to_eq_pairs = {
        (e.src_id, e.dst_id)
        for e in bundle.flow_edges
        if e.src_kind == "EQUIPMENT" and e.dst_kind == "EQUIPMENT"
    }
    assert ("EQ:CBS-TK-10A", "EQ:CBS-EP-36A") in eq_to_eq_pairs
    assert ("EQ:CBS-EP-36A", "EQ:RH-P-8A") in eq_to_eq_pairs
    assert ("EQ:RH-P-8A", "EQ:RH-E-9A") in eq_to_eq_pairs

    # Verify 100% Spanner Foreign Key Referential Integrity across all 10 Edge tables
    for ue in bundle.unit_edges:
        assert ue.equipment_id in bundle.equipment
        assert ue.unit_id in bundle.units

    for fe in bundle.flow_edges:
        if fe.src_kind == "EQUIPMENT":
            assert fe.src_id in bundle.equipment
        else:
            assert fe.src_id in bundle.boundaries
        if fe.dst_kind == "EQUIPMENT":
            assert fe.dst_id in bundle.equipment
        else:
            assert fe.dst_id in bundle.boundaries

    for me in bundle.monitor_edges:
        assert me.instrument_id in bundle.instruments
        assert me.equipment_id in bundle.equipment

    for le in bundle.lineage_edges:
        assert le.doc_id in bundle.governance_docs
        if le.entity_kind == "EQUIPMENT":
            assert le.entity_id in bundle.equipment
        elif le.entity_kind == "INSTRUMENT":
            assert le.entity_id in bundle.instruments
        elif le.entity_kind == "UNIT":
            assert le.entity_id in bundle.units

    for ge in bundle.governance_edges:
        assert ge.doc_id in bundle.governance_docs
        if ge.entity_kind == "EQUIPMENT":
            assert ge.entity_id in bundle.equipment
        else:
            assert ge.entity_id in bundle.instruments
