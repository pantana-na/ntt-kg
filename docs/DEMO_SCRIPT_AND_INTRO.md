# 5–7 Minute Executive Demo Script & Introduction

- **Demo Title:** *From Static P&IDs to Living Plant Intelligence: Dataplex Knowledge Catalog & Cloud Spanner Hybrid Search + Graph*
- **Total Run Time:** **5–7 Minutes** (`1–2 min` Intro &bull; `~3 min` Knowledge Catalog &bull; `~3 min` Cloud Spanner)
- **Presentation Surface:** **100% Native Google Cloud Console** (**Dataplex Knowledge Catalog Search** & **Spanner Studio**) — Zero Custom UI
- **Dataset:** [`okf_bundle/`](../okf_bundle) — Open Knowledge Format (OKF v0.2) for Nuclear/Process Plant Engineering (`100` governed entities, `61` Equipment specs, `24` SIS Instrument specs, `288` P&ID stream connections, IEC 61882 HAZOP standards, and cross-drawing `⚠️ CONFLICT` discrepancies)

---

## Pre-Demo Browser Tabs (Open Before Starting)

1. **Tab 1 — Architecture Visual:** [`docs/ntt-kg-demo-architecture.html`](./ntt-kg-demo-architecture.html)
2. **Tab 2 — Dataplex Knowledge Catalog Search:**
   `https://console.cloud.google.com/dataplex/search?project=<YOUR_GCP_PROJECT_ID>` *(Ensure **Natural language search** toggle is **ON**)*
3. **Tab 3 — Cloud Spanner Studio (`ntt-kg-demo` / `plant-kg`):**
   `https://console.cloud.google.com/spanner/instances/ntt-kg-demo/databases/plant-kg/studio?project=<YOUR_GCP_PROJECT_ID>` *(Pre-paste **Query A** and **Query B** below into two editor tabs so zero typing is needed live)*

---

## Segment 1: Executive Introduction (`1–2 Minutes`)

### 1.1 The Business Problem & Hook (`~60s`)
> *"Industrial and energy enterprises sit on thousands of P&IDs, equipment datasheets, safety interlocks, and HAZOP manuals. When an engineer asks, **'What protects our Residual Heat Removal heat exchanger if suction flow drops during reactor cooldown—and do our drawings agree?'**, traditional tools break down:*
> - *A **Keyword Engine** matches exact tags like `RH-FCV-610` or `Interlock G`, but misses documents describing 'cooldown bypass cavitation' in plain words.*
> - *A **Vector Database** understands conceptual symptoms, but loses exact alphanumeric precision on P&ID tags and drawing numbers.*
> - *Neither one can trace **multi-hop piping and safety interlocks**—and across the enterprise, engineers need a governed **Knowledge Catalog** where anyone can search plant knowledge in plain English.*
>
> *In the next 5 minutes—with **zero custom UI**, right inside the **Google Cloud Console**—we'll show how **Dataplex Knowledge Catalog** and **Cloud Spanner** solve discovery, hybrid retrieval, and graph reasoning together."*

### 1.2 Architecture Glance (`~30s` — Tab 1)
Point briefly to [`docs/ntt-kg-demo-architecture.html`](./ntt-kg-demo-architecture.html):
- **Pillar 1 — Dataplex Knowledge Catalog:** 100 curated OKF plant entries + Custom Aspect (`okf-plant-asset-aspect`) + Business Glossary + auto-cataloged Spanner tables, searchable via **Global Natural Language Search**.
- **Pillar 2 — Cloud Spanner Multi-Model Engine:** Native SQL embeddings (`ML.PREDICT` calling Vertex AI `text-embedding-005`), Full-Text Search, Vector Search, **Reciprocal Rank Fusion (RRF) Hybrid Search**, and a 5-Node **ISO GQL Property Graph**—all in one database.

---

## Segment 2: Dataplex Knowledge Catalog — Natural Language Search (`~2.5–3 Minutes`)

Switch to **Tab 2 (Dataplex Knowledge Catalog $\rightarrow$ Search)**.

### Beat 2.1 — Natural Language Semantic Discovery (`~1.5 min`)
1. With **Natural language search** toggled **ON**, paste and run:
   ```text
   heat exchangers that cool reactor coolant during shutdown or post-accident sump recirculation
   ```
2. **Talk-Track:**
   - *"Notice I didn't type a single tag code like `RH-E-9A` or `SS-E-106`. Knowledge Catalog understands engineering intent and surfaces **RHR Loop A & B Heat Exchangers (`RH-E-9A`, `RH-E-9B`)** and **Post Accident Sample Heat Exchanger (`SS-E-106`)**—right alongside our physical Spanner tables."*
3. Click **`RH-E-9A — RHR Loop A Heat Exchanger`** $\rightarrow$ open **Details / Aspects**:
   - Highlight **`OKF Plant Engineering Asset Aspect` (`okf-plant-asset-aspect`)**:
     - `tag`: `RH-E-9A` | `unit_code`: `RH / SI` | `safety_classification`: `Safety Class 2 and 3`
     - `has_discrepancy_warning`: **`true`** *(instant governance signal that two NRC drawings conflict on this asset!)*
     - `gcs_markdown_uri` & `spanner_entity_id`: `EQ:RH-E-9A` *(end-to-end lineage from raw Markdown in GCS to the Spanner Graph node).*

### Beat 2.2 — Hybrid Natural Language + Custom Aspect Filtering (`~1–1.5 min`)
1. Back in the Knowledge Catalog search bar, blend natural language with a structured custom aspect predicate:
   ```text
   safety interlock AND okf-plant-asset-aspect.has_discrepancy_warning:true
   ```
   *(Or run `flow switches that prevent charging pump deadheading or cavitation` to surface `FIS-7325`, `FIS-7326`, and `FIS-610`.)*
2. **Transition Line to Spanner:**
   > *"Knowledge Catalog lets any engineer or data steward discover governed plant knowledge in plain English and spot flagged safety warnings (`RH-E-9A` & `FIS-610`). Now let's jump into **Cloud Spanner Studio** to run deep **Hybrid Search** and **multi-hop P&ID Graph analysis** on those exact assets."*

---

## Segment 3: Cloud Spanner — Hybrid Search (RRF) & Property Graph (`~2.5–3 Minutes`)

Switch to **Tab 3 (Cloud Spanner Studio)**.

### Beat 3.1 — Hero Query: Spanner Hybrid Search with Reciprocal Rank Fusion (`~1.5 min`)
Run **Editor Tab A** (pre-pasted):
```sql
@{OPTIMIZER_VERSION=7}
WITH
  QueryVector AS (
    SELECT embeddings.values AS q_vec
    FROM ML.PREDICT(
      MODEL OkfEmbeddingModel,
      (SELECT 'Interlock G RHR heat exchanger bypass low suction flow cavitation Safety Class 2' AS content)
    )
  ),
  KeywordCandidates AS (
    SELECT item.ChunkId, off + 1 AS fts_rank
    FROM UNNEST(
      ARRAY(
        SELECT AS STRUCT c.ChunkId
        FROM OkfChunks AS c
        WHERE SEARCH(c.ChunkTokens, '"Interlock G" OR cavitation OR "Safety Class 2" OR bypass OR RH-FCV-610')
        ORDER BY SCORE(c.ChunkTokens, '"Interlock G" OR cavitation OR "Safety Class 2" OR bypass OR RH-FCV-610') DESC, c.ChunkId
        LIMIT 30
      )
    ) AS item WITH OFFSET AS off
  ),
  VectorCandidates AS (
    SELECT item.ChunkId, item.cosine_dist, off + 1 AS vec_rank
    FROM UNNEST(
      ARRAY(
        SELECT AS STRUCT c.ChunkId, COSINE_DISTANCE(c.Embedding, q.q_vec) AS cosine_dist
        FROM OkfChunks AS c
        CROSS JOIN QueryVector AS q
        WHERE c.Embedding IS NOT NULL
        ORDER BY cosine_dist ASC, c.ChunkId
        LIMIT 30
      )
    ) AS item WITH OFFSET AS off
  ),
  RrfFused AS (
    SELECT
      COALESCE(k.ChunkId, v.ChunkId) AS ChunkId,
      k.fts_rank,
      v.vec_rank,
      (
        IF(k.fts_rank IS NOT NULL, 1.0 / (60.0 + k.fts_rank), 0.0) +
        IF(v.vec_rank IS NOT NULL, 1.0 / (60.0 + v.vec_rank), 0.0)
      ) AS rrf_score
    FROM KeywordCandidates AS k
    FULL OUTER JOIN VectorCandidates AS v
      ON k.ChunkId = v.ChunkId
  )
SELECT
  c.Tag,
  c.EntityLabel,
  c.UnitCode,
  c.SectionHeading,
  c.HasConflict,
  f.fts_rank,
  f.vec_rank,
  ROUND(f.rrf_score, 5) AS rrf_hybrid_score,
  SUBSTR(c.ChunkText, 1, 240) AS grounded_excerpt
FROM RrfFused AS f
JOIN OkfChunks AS c ON c.ChunkId = f.ChunkId
ORDER BY f.rrf_score DESC
LIMIT 8;
```
- **2 Points to Highlight (`60s`):**
  1. **Native In-Database Embeddings (`ML.PREDICT`):** No Python client or external vector DB—Spanner calls Vertex AI `text-embedding-005` directly inside SQL (`QueryVector` CTE).
  2. **Reciprocal Rank Fusion (`fts_rank` + `vec_rank` $\rightarrow$ `rrf_hybrid_score`):** Point to the result columns: **`RH-E-9A`** (`fts_rank = 5`, `vec_rank = 1`, `rrf = 0.03178`) and **`FIS-610`** (`fts_rank = 4`, `vec_rank = 7`, `rrf = 0.03055`) combine exact `"Interlock G"` / `"Safety Class 2"` keyword precision with semantic *"low suction flow cavitation"* matching to rank `#1` and `#2`!

### Beat 3.2 — Visual Multi-Hop P&ID Flow & Safety Interlock Graph (`~1.5 min`)
Switch to **Editor Tab B** and click **Run**:
```sql
GRAPH PlantKnowledgeGraph
MATCH p1 = (sump:Equipment)-[:FLOWS_TO]->{1,3}(hx:Equipment)
WHERE sump.Tag IN ('CBS-TK-10A', 'CBS-TK-10B')
RETURN SAFE_TO_JSON(p1) AS graph_path
UNION ALL
MATCH p2 = (inst:Instrument)-[:MONITORS]->(eq:Equipment)-[:BELONGS_TO_UNIT]->(u:PlantUnit)
WHERE eq.Tag IN ('CBS-TK-10A', 'CBS-TK-101A', 'RH-P-8A', 'RH-E-9A')
  AND inst.IsFullSpec = TRUE
RETURN SAFE_TO_JSON(p2) AS graph_path;
```
1. Click the **`Graph`** tab in the Results pane (and briefly click **`Schema View`** for 5 seconds to show the 5 color-coded node types: `PlantUnit`, `Equipment`, `Instrument`, `ProcessBoundary`, `GovernanceDoc`).
2. Click along the live emergency cooling chain on the canvas:
   `CBS-TK-10A` *(Sump A, `LE-2384-1`)* $\rightarrow$ `CBS-TK-101A` *(Chamber A, leak switch `LS-2356`)* & `CBS-EP-36A` *(Bellows)* $\rightarrow$ `RH-P-8A` *(RHR Pump A, interlocked with `FIS-610`)* $\rightarrow$ `RH-E-9A` *(RHR Heat Exchanger A)*.

### Closing Takeaway (`15s`)
> *"Normally, building this requires stitching together Elasticsearch for keywords, a separate vector DB, a separate graph DB, sync pipelines that drift out of date, plus a standalone catalog. On Google Cloud, **Dataplex Knowledge Catalog** gives business and engineering users **Global Natural Language Search**, while **Cloud Spanner** runs **Full-Text, Native Vector Embeddings, RRF Hybrid Search, and ISO GQL Graphs** in a single strongly consistent engine."*

---

## Appendix: Optional Q&A Deep-Dive Queries (`If Audience Asks`)

### Q&A Bonus — Single-Query Hybrid Search + Graph Expansion (`RRF` + `GRAPH_TABLE`)
*"Can you join Hybrid Search and Graph traversal in a single SQL query?"* — Yes (`DM-8` Fuel Pool Demineralizer, `F-33` Prefilter, `F-34` Postfilter + `PDIS-2622/2623/2624` & `FISL-2626`):
```sql
@{OPTIMIZER_VERSION=7}
WITH
  QueryVec AS (
    SELECT embeddings.values AS q_vec
    FROM ML.PREDICT(
      MODEL OkfEmbeddingModel,
      (SELECT 'Spent fuel pool resin fines filtration and demineralizer differential pressure' AS content)
    )
  ),
  FtsHits AS (
    SELECT item.ChunkId, off + 1 AS r_fts
    FROM UNNEST(
      ARRAY(
        SELECT AS STRUCT ChunkId
        FROM OkfChunks
        WHERE SEARCH(ChunkTokens, 'demineralizer OR postfilter OR "resin fines" OR DM-8')
        ORDER BY SCORE(ChunkTokens, 'demineralizer OR postfilter OR "resin fines" OR DM-8') DESC, ChunkId
        LIMIT 20
      )
    ) AS item WITH OFFSET AS off
  ),
  VecHits AS (
    SELECT item.ChunkId, off + 1 AS r_vec
    FROM UNNEST(
      ARRAY(
        SELECT AS STRUCT c.ChunkId
        FROM OkfChunks AS c CROSS JOIN QueryVec AS q
        WHERE c.Embedding IS NOT NULL
        ORDER BY COSINE_DISTANCE(c.Embedding, q.q_vec) ASC, c.ChunkId
        LIMIT 20
      )
    ) AS item WITH OFFSET AS off
  ),
  TopHybridEntities AS (
    SELECT
      c.EntityId,
      c.Tag,
      MAX(
        IF(f.r_fts IS NOT NULL, 1.0 / (60.0 + f.r_fts), 0.0) +
        IF(v.r_vec IS NOT NULL, 1.0 / (60.0 + v.r_vec), 0.0)
      ) AS best_rrf_score
    FROM FtsHits AS f
    FULL OUTER JOIN VecHits AS v USING (ChunkId)
    JOIN OkfChunks AS c USING (ChunkId)
    GROUP BY c.EntityId, c.Tag
    ORDER BY best_rrf_score DESC
    LIMIT 5
  ),
  GraphContext AS (
    SELECT *
    FROM GRAPH_TABLE (
      PlantKnowledgeGraph
      MATCH (inst:Instrument)-[m:MONITORS]->(eq:Equipment)-[fl:FLOWS_TO]->(downstream)
      RETURN
        eq.EquipmentId AS EntityId,
        eq.Tag AS EquipmentTag,
        eq.Title AS EquipmentTitle,
        inst.Tag AS MonitoringInstrument,
        m.InterlockOrAlarm AS AlarmOrInterlock,
        fl.StreamId AS OutgoingStream,
        downstream.Tag AS FlowsToTag
    )
  )
SELECT
  h.Tag AS matched_tag,
  ROUND(h.best_rrf_score, 5) AS rrf_score,
  g.EquipmentTitle,
  g.MonitoringInstrument,
  g.AlarmOrInterlock,
  g.OutgoingStream,
  g.FlowsToTag
FROM TopHybridEntities AS h
JOIN GraphContext AS g
  ON h.EntityId = g.EntityId
ORDER BY h.best_rrf_score DESC, g.MonitoringInstrument;
```
*(Additional standalone Keyword-only, Vector-only (`CS-P-2A` / `FIS-7325`), and Conflict Blast Radius queries are available in [`sql/demo_queries_spanner.sql`](../sql/demo_queries_spanner.sql).)*
