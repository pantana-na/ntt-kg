#!/usr/bin/env python3
"""Verify live Spanner Hybrid Search + Property Graph GQL and Dataplex Knowledge Catalog readiness."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from google.cloud import dataplex_v1
from google.cloud import spanner

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "src"))

from okf_kg.config import load_settings


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify Spanner Hybrid/Graph + Dataplex Knowledge Catalog live readiness")
    ap.add_argument("--env-file", type=Path, default=None)
    ap.add_argument("--env", choices=["nonprod", "prod"], default=None)
    args = ap.parse_args()

    settings = load_settings(env_file=args.env_file, override_env=args.env)

    sp_client = spanner.Client(project=settings.gcp_project)
    db = sp_client.instance(settings.spanner_instance).database(settings.spanner_database)

    # 1. Check table counts & embedding completeness
    with db.snapshot(multi_use=True) as snap:
        eq_cnt = list(snap.execute_sql("SELECT COUNT(*) FROM Equipment"))[0][0]
        inst_cnt = list(snap.execute_sql("SELECT COUNT(*) FROM Instruments"))[0][0]
        chunk_cnt, null_emb_cnt = list(
            snap.execute_sql(
                "SELECT COUNT(*), COUNTIF(Embedding IS NULL) FROM OkfChunks"
            )
        )[0]

    # 2. Live RRF Hybrid Search Smoke Check
    rrf_sql = f"""@{{OPTIMIZER_VERSION=7}}
    WITH
      QueryVec AS (
        SELECT embeddings.values AS q_vec
        FROM ML.PREDICT(
          MODEL {settings.spanner_model_name},
          (SELECT 'Interlock G RHR heat exchanger bypass low suction flow cavitation Safety Class 2' AS content)
        )
      ),
      K AS (
        SELECT item.ChunkId, off + 1 AS rk
        FROM UNNEST(
          ARRAY(
            SELECT AS STRUCT ChunkId
            FROM OkfChunks
            WHERE SEARCH(ChunkTokens, '"Interlock G" OR cavitation OR "Safety Class 2" OR RH-FCV-610')
            ORDER BY SCORE(ChunkTokens, '"Interlock G" OR cavitation OR "Safety Class 2" OR RH-FCV-610') DESC, ChunkId
            LIMIT 20
          )
        ) AS item WITH OFFSET AS off
      ),
      V AS (
        SELECT item.ChunkId, off + 1 AS rv
        FROM UNNEST(
          ARRAY(
            SELECT AS STRUCT c.ChunkId
            FROM OkfChunks AS c CROSS JOIN QueryVec AS q
            WHERE c.Embedding IS NOT NULL
            ORDER BY COSINE_DISTANCE(c.Embedding, q.q_vec) ASC, c.ChunkId
            LIMIT 20
          )
        ) AS item WITH OFFSET AS off
      )
    SELECT c.Tag, c.SectionHeading
    FROM K FULL OUTER JOIN V USING (ChunkId)
    JOIN OkfChunks AS c USING (ChunkId)
    ORDER BY (IF(K.rk IS NOT NULL, 1.0/(60+K.rk), 0) + IF(V.rv IS NOT NULL, 1.0/(60+V.rv), 0)) DESC
    LIMIT 5
    """
    with db.snapshot() as snap:
        top_hybrid = [(r[0], r[1]) for r in snap.execute_sql(rrf_sql)]

    # 3. Live Spanner Property Graph GQL Smoke Check
    gql_sql = f"""
    GRAPH {settings.spanner_graph_name}
    MATCH (inst:Instrument)-[:MONITORS]->(eq:Equipment {{HasConflict: TRUE}})
    RETURN eq.Tag, COUNT(inst) AS monitor_count
    GROUP BY eq.Tag
    ORDER BY eq.Tag
    """
    with db.snapshot() as snap:
        conflict_graph_hits = [(r[0], r[1]) for r in snap.execute_sql(gql_sql)]

    # 4. Live Dataplex Knowledge Catalog Natural Language Search Check
    dp_client = dataplex_v1.CatalogServiceClient()
    search_req = dataplex_v1.SearchEntriesRequest(
        name=f"projects/{settings.gcp_project}/locations/global",
        scope=f"projects/{settings.gcp_project}",
        query="heat exchangers that cool reactor coolant during shutdown",
        page_size=5,
        semantic_search=True,
    )
    dp_hits = [res.dataplex_entry.entry_source.display_name for res in dp_client.search_entries(request=search_req)]

    report = {
        "status": "HEALTHY" if (eq_cnt == 61 and null_emb_cnt == 0 and len(top_hybrid) > 0 and len(dp_hits) > 0) else "DEGRADED",
        "project": settings.gcp_project,
        "region": settings.gcp_region,
        "spanner": {
            "instance": settings.spanner_instance,
            "database": settings.spanner_database,
            "equipment_nodes": eq_cnt,
            "instrument_nodes": inst_cnt,
            "total_chunks": chunk_cnt,
            "null_embeddings": null_emb_cnt,
            "sample_rrf_hybrid_top5": top_hybrid,
            "conflict_equipment_graph_monitors": conflict_graph_hits,
        },
        "dataplex_knowledge_catalog": {
            "entry_group": settings.dataplex_entry_group,
            "aspect_type": settings.dataplex_aspect_type,
            "sample_nl_search_hits": dp_hits[:5],
        },
        "console_urls": {
            "spanner_studio": (
                f"https://console.cloud.google.com/spanner/instances/{settings.spanner_instance}"
                f"/databases/{settings.spanner_database}/studio?project={settings.gcp_project}"
            ),
            "knowledge_catalog_search": (
                f"https://console.cloud.google.com/dataplex/search?project={settings.gcp_project}"
            ),
        },
    }
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "HEALTHY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
