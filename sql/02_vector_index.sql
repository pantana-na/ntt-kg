-- ============================================================================
-- 02_vector_index.sql — Post-Backfill ScaNN COSINE Vector Index
-- Applied automatically by scripts/03_embed_spanner.py after ML.PREDICT backfill
-- ============================================================================

CREATE VECTOR INDEX IF NOT EXISTS OkfChunksEmbeddingIdx
  ON OkfChunks(Embedding)
  WHERE Embedding IS NOT NULL
  OPTIONS (distance_type = 'COSINE');
