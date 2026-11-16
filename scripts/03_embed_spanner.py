#!/usr/bin/env python3
"""Populate OkfChunks.Embedding natively inside Cloud Spanner via batched SQL ML.PREDICT + batch.update and build Vector Index."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import random
import sys
import time
from typing import List, Tuple

from google.api_core import exceptions as gcp_exceptions
from google.cloud import spanner
from google.cloud.spanner_v1 import param_types

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "src"))

from okf_kg.config import load_settings
from okf_kg.rrf import chunk_batches
from okf_kg.sql_templates import render_ddl_statements


def main() -> int:
    ap = argparse.ArgumentParser(description="Backfill Spanner native embeddings via ML.PREDICT and build Vector Index")
    ap.add_argument("--env-file", type=Path, default=None)
    ap.add_argument("--env", choices=["nonprod", "prod"], default=None)
    ap.add_argument("--skip-vector-index", action="store_true", help="Skip CREATE VECTOR INDEX after embedding")
    args = ap.parse_args()

    settings = load_settings(env_file=args.env_file, override_env=args.env)
    client = spanner.Client(project=settings.gcp_project)
    instance = client.instance(settings.spanner_instance)
    database = instance.database(settings.spanner_database)

    with database.snapshot() as snap:
        pending_ids: List[str] = [
            row[0]
            for row in snap.execute_sql(
                "SELECT ChunkId FROM OkfChunks WHERE Embedding IS NULL ORDER BY ChunkId"
            )
        ]

    print(f"[EMBED] Found {len(pending_ids)} chunks requiring native Spanner ML.PREDICT embeddings.")
    batches = chunk_batches(pending_ids, batch_size=settings.spanner_embed_batch_size)

    predict_sql = f"""
    SELECT
      ChunkId,
      embeddings.values AS vec
    FROM ML.PREDICT(
      MODEL {settings.spanner_model_name},
      (
        SELECT ChunkId, ChunkText AS content
        FROM OkfChunks
        WHERE ChunkId IN UNNEST(@chunk_ids)
          AND Embedding IS NULL
      )
    )
    """

    completed = 0
    for idx, batch_ids in enumerate(batches, start=1):
        for attempt in range(1, settings.max_retry_attempts + 1):
            try:
                with database.snapshot() as snap:
                    predicted_rows: List[Tuple[str, List[float]]] = [
                        (row[0], list(row[1]))
                        for row in snap.execute_sql(
                            predict_sql,
                            params={"chunk_ids": batch_ids},
                            param_types={"chunk_ids": param_types.Array(param_types.STRING)},
                        )
                    ]

                if predicted_rows:
                    commit_ts = spanner.COMMIT_TIMESTAMP
                    with database.batch() as batch:
                        batch.update(
                            table="OkfChunks",
                            columns=["ChunkId", "Embedding", "UpdatedAt"],
                            values=[(cid, vec, commit_ts) for cid, vec in predicted_rows],
                        )

                completed += len(predicted_rows)
                print(
                    f"[EMBED] Batch {idx}/{len(batches)}: embedded {len(predicted_rows)} chunks "
                    f"({completed}/{len(pending_ids)} total)"
                )
                break
            except (
                gcp_exceptions.ResourceExhausted,
                gcp_exceptions.ServiceUnavailable,
                gcp_exceptions.DeadlineExceeded,
                gcp_exceptions.Aborted,
                gcp_exceptions.PermissionDenied,
            ) as exc:
                if attempt >= settings.max_retry_attempts:
                    print(
                        json.dumps(
                            {
                                "status": "UPSTREAM_UNAVAILABLE_DEGRADED",
                                "step": "03_embed_spanner",
                                "completed_chunks": completed,
                                "remaining_chunks": len(pending_ids) - completed,
                                "error": str(exc),
                            }
                        ),
                        file=sys.stderr,
                    )
                    return 3
                wait_s = min(45.0, (2 ** attempt) + random.uniform(0.2, 1.2))
                print(f"[RETRY] Batch {idx} attempt {attempt} waiting {wait_s:.1f}s ({exc})")
                time.sleep(wait_s)

    if not args.skip_vector_index:
        vec_ddls = render_ddl_statements(REPO_ROOT / "sql" / "02_vector_index.sql", settings)
        print("[VECTOR INDEX] Ensuring OkfChunksEmbeddingIdx (COSINE) is created...")
        op = database.update_ddl(vec_ddls)
        op.result(timeout=600)
        print("[VECTOR INDEX] OkfChunksEmbeddingIdx ready.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
