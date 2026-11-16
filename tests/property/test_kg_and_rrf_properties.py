"""Generative Property-Based Tests (PBT via Hypothesis) verifying mathematical and graph invariants."""

from __future__ import annotations

from pathlib import Path
import re
import tempfile
from typing import List

from hypothesis import given, settings as hyp_settings, strategies as st
import yaml

from okf_kg.dataplex_builder import sanitize_dataplex_labels
from okf_kg.parser import parse_okf_bundle
from okf_kg.rrf import chunk_batches, compute_rrf_scores, make_dataplex_entry_id


@given(
    fts_ids=st.lists(st.text(alphabet="abcdefghij0123456789", min_size=1, max_size=8), max_size=25, unique=True),
    vec_ids=st.lists(st.text(alphabet="abcdefghij0123456789", min_size=1, max_size=8), max_size=25, unique=True),
    k=st.integers(min_value=1, max_value=200),
)
@hyp_settings(max_examples=80)
def test_pbt_rrf_bounds_symmetry_and_dominance(fts_ids: List[str], vec_ids: List[str], k: int) -> None:
    fused = compute_rrf_scores(fts_ids, vec_ids, k=k)
    expected_union = set(fts_ids) | set(vec_ids)
    assert {c.item_id for c in fused} == expected_union

    upper_bound = 2.0 / float(k + 1) + 1e-12
    scores = [c.rrf_score for c in fused]
    # Monotonically non-increasing order
    assert scores == sorted(scores, reverse=True)
    for c in fused:
        assert 0.0 < c.rrf_score <= upper_bound

    # Symmetry invariant: swapping equal-weight inputs yields identical score map
    swapped = compute_rrf_scores(vec_ids, fts_ids, k=k)
    assert {c.item_id: round(c.rrf_score, 12) for c in fused} == {
        c.item_id: round(c.rrf_score, 12) for c in swapped
    }

    # Dominance invariant: an item ranked #1 in BOTH lists achieves maximum theoretical RRF score
    if fts_ids and vec_ids and fts_ids[0] == vec_ids[0]:
        assert fused[0].item_id == fts_ids[0]
        assert abs(fused[0].rrf_score - (2.0 / float(k + 1))) < 1e-12


@given(
    items=st.lists(st.integers(), max_size=250),
    batch_size=st.integers(min_value=1, max_value=50),
    cols_per_row=st.integers(min_value=1, max_value=25),
    max_cells=st.integers(min_value=25, max_value=500),
)
@hyp_settings(max_examples=80)
def test_pbt_spanner_chunk_batches_order_and_cell_cap(
    items: List[int],
    batch_size: int,
    cols_per_row: int,
    max_cells: int,
) -> None:
    batches = chunk_batches(items, batch_size=batch_size, max_cells_per_batch=max_cells, cols_per_row=cols_per_row)
    flattened = [x for b in batches for x in b]
    assert flattened == items
    for b in batches:
        assert 1 <= len(b) <= batch_size
        assert len(b) * cols_per_row <= max_cells


@given(
    prefix=st.text(min_size=0, max_size=20),
    raw_id=st.text(min_size=0, max_size=120),
    raw_tags=st.lists(st.text(min_size=0, max_size=80), max_size=12),
)
@hyp_settings(max_examples=100)
def test_pbt_dataplex_entry_id_and_label_conformance(prefix: str, raw_id: str, raw_tags: List[str]) -> None:
    eid1 = make_dataplex_entry_id(prefix, raw_id)
    eid2 = make_dataplex_entry_id(prefix, raw_id)
    assert eid1 == eid2
    assert 1 <= len(eid1) <= 63
    assert re.match(r"^[a-z0-9][a-z0-9-]{0,62}$", eid1)

    labels = sanitize_dataplex_labels(raw_tags)
    for k, v in labels.items():
        assert re.match(r"^[a-z][a-z0-9_-]{0,62}$", k)
        assert re.match(r"^[a-z0-9_-]{1,63}$", v)


@given(
    eq_tags=st.lists(
        st.from_regex(r"[A-Z]{2}-[P|E|TK]-[1-9][0-9]{0,2}[A-B]?", fullmatch=True),
        min_size=2,
        max_size=6,
        unique=True,
    ),
    ext_boundary=st.text(alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -/", min_size=3, max_size=30),
    include_conflict=st.booleans(),
)
@hyp_settings(max_examples=30)
def test_pbt_synthetic_okf_bundle_referential_integrity(
    eq_tags: List[str],
    ext_boundary: str,
    include_conflict: bool,
) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "equipment").mkdir()
        (root / "hazop").mkdir()

        hazop_fm = {
            "type": "HAZOP Protocol",
            "title": "Synthetic HAZOP Guide",
            "description": "IEC 61882 guide words",
            "tags": ["hazop"],
            "entity_metadata": {"governing_standards": ["IEC 61882"]},
        }
        (root / "hazop" / "guide.md").write_text(
            f"---\n{yaml.safe_dump(hazop_fm)}---\n# Guide\nBody text.\n",
            encoding="utf-8",
        )

        for idx, tag in enumerate(eq_tags):
            next_target = eq_tags[(idx + 1) % len(eq_tags)] if idx == 0 else ext_boundary
            eq_fm = {
                "type": "Equipment Concept",
                "title": f"{tag} — Synthetic Asset",
                "description": f"Synthetic equipment {tag}",
                "tags": ["equipment"],
                "entity_metadata": {
                    "tag": tag,
                    "equipment_class": "Pump",
                    "unit": "SI / RH",
                    "instruments": [{"tag": f"FI-{idx + 100}", "type": "Flow Indicator", "service": "Flow"}],
                    "connections": [
                        {
                            "stream_id": f"STR-{idx}",
                            "direction": "OUTLET",
                            "source_tag": tag,
                            "target_tag": next_target,
                        }
                    ],
                },
            }
            warn = "\n> ⚠️ CONFLICT — synthetic drawing discrepancy\n" if include_conflict else ""
            (root / "equipment" / f"{tag}.md").write_text(
                f"---\n{yaml.safe_dump(eq_fm)}---\n# {tag}\n{warn}## Design\nDetails.\n",
                encoding="utf-8",
            )

        parsed = parse_okf_bundle(root)
        assert len(parsed.equipment) == len(eq_tags)
        assert len(parsed.catalog_entries) == len(eq_tags) + 1

        for fe in parsed.flow_edges:
            if fe.src_kind == "EQUIPMENT":
                assert fe.src_id in parsed.equipment
            else:
                assert fe.src_id in parsed.boundaries
            if fe.dst_kind == "EQUIPMENT":
                assert fe.dst_id in parsed.equipment
            else:
                assert fe.dst_id in parsed.boundaries
