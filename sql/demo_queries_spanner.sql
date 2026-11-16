-- ============================================================================
-- demo_queries_spanner.sql — Live-Verified Google Cloud Console Queries
-- Project: <YOUR_GCP_PROJECT_ID> | Instance: ntt-kg-demo | Database: plant-kg
-- ============================================================================

-- ----------------------------------------------------------------------------
-- DEMO QUERY 1: Keyword / Full-Text Search (Exact P&ID Tag & Interlock Codes)
-- Why it matters: Engineers often search exact drawing numbers ("PID-1-SI-LR20448"),
-- valve tags ("RH-FCV-610"), or interlock IDs ("Interlock G") where pure vector
-- embeddings lose exact alphanumeric precision.
-- ----------------------------------------------------------------------------
@{OPTIMIZER_VERSION=7}
SELECT
  Tag,
  EntityLabel,
  UnitCode,
  SectionHeading,
  HasConflict,
  ROUND(SCORE(ChunkTokens, 'PID-1-SI-LR20448 OR RH-FCV-610 OR "Interlock G"'), 4) AS keyword_score,
  SUBSTR(ChunkText, 1, 260) AS snippet
FROM OkfChunks
WHERE SEARCH(ChunkTokens, 'PID-1-SI-LR20448 OR RH-FCV-610 OR "Interlock G"')
ORDER BY keyword_score DESC
LIMIT 8;


-- ----------------------------------------------------------------------------
-- DEMO QUERY 2: Spanner Native Semantic Vector Search (Zero External Code!)
-- Why it matters: Operators describe physical symptoms ("prevent charging pump
-- deadheading overheating at low discharge flow") without knowing the exact tag
-- (CS-P-2A / FIS-7325 / CS-V196). Spanner calls Vertex AI text-embedding-005
-- natively inside SQL via ML.PREDICT!
-- ----------------------------------------------------------------------------
WITH QueryVector AS (
  SELECT embeddings.values AS q_vec
  FROM ML.PREDICT(
    MODEL OkfEmbeddingModel,
    (SELECT 'prevent centrifugal pump deadheading overheating when discharge flow drops low' AS content)
  )
)
SELECT
  c.Tag,
  c.EntityLabel,
  c.Title,
  c.SectionHeading,
  ROUND(COSINE_DISTANCE(c.Embedding, q.q_vec), 4) AS cosine_distance,
  ROUND(1.0 - COSINE_DISTANCE(c.Embedding, q.q_vec), 4) AS semantic_similarity,
  SUBSTR(c.ChunkText, 1, 260) AS snippet
FROM OkfChunks AS c
CROSS JOIN QueryVector AS q
WHERE c.Embedding IS NOT NULL
ORDER BY cosine_distance ASC
LIMIT 8;


-- ----------------------------------------------------------------------------
-- DEMO QUERY 3 (HERO): Spanner Hybrid Search with Reciprocal Rank Fusion (RRF)
-- Why it matters: Real engineering questions mix exact nomenclature ("Interlock G",
-- "Safety Class 2") with conceptual failure modes ("heat exchanger bypass valve
-- misalignment causing pump cavitation during cooldown").
-- RRF fuses Full-Text Rank and Vector Rank into one unified score:
--   RRF_Score = 1/(60 + fts_rank) + 1/(60 + vec_rank)
-- ----------------------------------------------------------------------------
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
      ROUND(v.cosine_dist, 4) AS cosine_dist,
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
  SUBSTR(c.ChunkText, 1, 280) AS grounded_excerpt
FROM RrfFused AS f
JOIN OkfChunks AS c
  ON c.ChunkId = f.ChunkId
ORDER BY f.rrf_score DESC
LIMIT 10;


-- ----------------------------------------------------------------------------
-- DEMO QUERY 4 (VISUAL GRAPH): Multi-Hop Post-LOCA Sump -> RHR Flow & Interlocks
-- Console Tip: Run this query in Spanner Studio, then click the "Graph" tab
-- in the Results pane (and toggle "Schema View") to explore the 5-node ontology!
-- ----------------------------------------------------------------------------
GRAPH PlantKnowledgeGraph
MATCH p1 = (sump:Equipment)-[:FLOWS_TO]->{1,3}(hx:Equipment)
WHERE sump.Tag IN ('CBS-TK-10A', 'CBS-TK-10B')
RETURN SAFE_TO_JSON(p1) AS graph_path
UNION ALL
MATCH p2 = (inst:Instrument)-[:MONITORS]->(eq:Equipment)-[:BELONGS_TO_UNIT]->(u:PlantUnit)
WHERE eq.Tag IN ('CBS-TK-10A', 'CBS-TK-101A', 'RH-P-8A', 'RH-E-9A')
  AND inst.IsFullSpec = TRUE
RETURN SAFE_TO_JSON(p2) AS graph_path;


-- ----------------------------------------------------------------------------
-- DEMO QUERY 5 (VISUAL GRAPH): Engineering Drawing Conflict & HAZOP Blast Radius
-- Finds equipment flagged with cross-drawing P&ID conflicts (RH-E-9A / RH-E-9B)
-- and visualizes connected P&ID streams, safety instruments, source P&IDs, and
-- governing IEC 61882 HAZOP / RAM standards.
-- ----------------------------------------------------------------------------
GRAPH PlantKnowledgeGraph
MATCH path_flow = (upstream:Equipment)-[:FLOWS_TO]->(conflict_eq:Equipment {HasConflict: TRUE})
RETURN SAFE_TO_JSON(path_flow) AS conflict_blast_radius
UNION ALL
MATCH path_inst = (inst:Instrument)-[:MONITORS]->(conflict_eq:Equipment {HasConflict: TRUE})
RETURN SAFE_TO_JSON(path_inst) AS conflict_blast_radius
UNION ALL
MATCH path_gov = (conflict_eq:Equipment {HasConflict: TRUE})-[:EXTRACTED_FROM|GOVERNED_BY]->(doc:GovernanceDoc)
RETURN SAFE_TO_JSON(path_gov) AS conflict_blast_radius;


-- ----------------------------------------------------------------------------
-- DEMO QUERY 6 (HYBRID + GRAPH CONVERGENCE): RRF Hybrid Search -> GQL Expansion
-- In ONE single Spanner query:
--   Step 1: Find top equipment/instrument chunks via RRF Hybrid Search
--   Step 2: Traverse PlantKnowledgeGraph to pull connected P&ID neighbors & interlocks!
-- ----------------------------------------------------------------------------
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
