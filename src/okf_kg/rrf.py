"""Reciprocal Rank Fusion (RRF) and batch partitioning utilities."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class RankedCandidate:
    item_id: str
    fts_rank: int | None
    vec_rank: int | None
    rrf_score: float


def compute_rrf_scores(
    fts_ordered_ids: Sequence[str],
    vec_ordered_ids: Sequence[str],
    k: int = 60,
    fts_weight: float = 1.0,
    vec_weight: float = 1.0,
) -> List[RankedCandidate]:
    """
    Combine Full-Text Search ranked IDs and Vector Search ranked IDs via
    Reciprocal Rank Fusion:
      score(d) = fts_weight / (k + rank_fts(d)) + vec_weight / (k + rank_vec(d))
    Ranks are 1-indexed.
    """
    if k <= 0:
        raise ValueError(f"RRF smoothing constant k must be > 0, got {k}")
    if fts_weight < 0 or vec_weight < 0:
        raise ValueError("RRF weights must be non-negative")

    fts_ranks: Dict[str, int] = {}
    for idx, doc_id in enumerate(fts_ordered_ids, start=1):
        if doc_id not in fts_ranks:
            fts_ranks[doc_id] = idx

    vec_ranks: Dict[str, int] = {}
    for idx, doc_id in enumerate(vec_ordered_ids, start=1):
        if doc_id not in vec_ranks:
            vec_ranks[doc_id] = idx

    all_ids = list(dict.fromkeys([*fts_ranks.keys(), *vec_ranks.keys()]))
    results: List[RankedCandidate] = []
    for doc_id in all_ids:
        fr = fts_ranks.get(doc_id)
        vr = vec_ranks.get(doc_id)
        score = 0.0
        if fr is not None:
            score += fts_weight / float(k + fr)
        if vr is not None:
            score += vec_weight / float(k + vr)
        results.append(
            RankedCandidate(
                item_id=doc_id,
                fts_rank=fr,
                vec_rank=vr,
                rrf_score=score,
            )
        )

    results.sort(
        key=lambda c: (
            -c.rrf_score,
            c.fts_rank if c.fts_rank is not None else 10**9,
            c.vec_rank if c.vec_rank is not None else 10**9,
            c.item_id,
        )
    )
    return results


def chunk_batches(items: Sequence[T], batch_size: int, max_cells_per_batch: int = 40000, cols_per_row: int = 1) -> List[List[T]]:
    """Partition items into deterministic batches respecting both row count and Spanner cell mutation caps."""
    if batch_size <= 0:
        raise ValueError("batch_size must be > 0")
    if cols_per_row <= 0:
        raise ValueError("cols_per_row must be > 0")
    if max_cells_per_batch < cols_per_row:
        raise ValueError("max_cells_per_batch must be >= cols_per_row")

    effective_size = min(batch_size, max(1, max_cells_per_batch // cols_per_row))
    return [list(items[i : i + effective_size]) for i in range(0, len(items), effective_size)]


def make_dataplex_entry_id(prefix: str, raw_identifier: str) -> str:
    """
    Build a deterministic Dataplex-compliant entry_id matching ^[a-z0-9][a-z0-9_-]{0,62}$
    (Dataplex Entry IDs require lowercase alphanumeric + hyphens/underscores, starting with [a-z0-9], max 63 chars).
    """
    import hashlib
    import re

    combined = f"{prefix}-{raw_identifier}".lower()
    slug = re.sub(r"[^a-z0-9]+", "-", combined).strip("-")
    if not slug or not slug[0].isalnum():
        slug = f"e-{slug}".strip("-")
    digest = hashlib.sha256(f"{prefix}:{raw_identifier}".encode("utf-8")).hexdigest()[:8]
    max_base = 63 - len(digest) - 1
    slug = slug[:max_base].rstrip("-")
    if not slug:
        slug = "entry"
    return f"{slug}-{digest}"
