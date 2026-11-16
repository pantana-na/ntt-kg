# Plan Progress Report — NTT Plant Knowledge Graph & Knowledge Catalog Demo (`2026-11-16`)

- **Linked Specification:** [`specs/features/SPEC-20261116-NTT-KG-DEMO.md`](../features/SPEC-20261116-NTT-KG-DEMO.md) (`Version 1.1`, `Implemented`)
- **Architecture Diagram:** [`docs/ntt-kg-demo-architecture.md`](../../docs/ntt-kg-demo-architecture.md) & [`docs/ntt-kg-demo-architecture.html`](../../docs/ntt-kg-demo-architecture.html)
- **Live Demo Script & Intro:** [`docs/DEMO_SCRIPT_AND_INTRO.md`](../../docs/DEMO_SCRIPT_AND_INTRO.md)
- **GCP Project / Region:** `<YOUR_GCP_PROJECT_ID>` / `asia-southeast1` (`100 PU` Spanner Enterprise)
- **Target GitHub Repository:** `https://github.com/pantana-na/ntt-kg.git`
- **Current Lifecycle Phase:** `Phase 3 Complete — Deployed & Verified HEALTHY on <YOUR_GCP_PROJECT_ID>`

## Live Deployment & Verification Telemetry (`05_verify_demo.py` -> `HEALTHY`)

| Component | Live Resource Identifier | Verified Live Telemetry |
| :--- | :--- | :--- |
| **Cloud Storage Corpus** | `gs://<YOUR_GCP_PROJECT_ID>-okf-bundle/okf_bundle/` | `109/109` Markdown files synced (`813.9 KiB`), uniform bucket-level access, public access prevented |
| **Cloud Spanner Enterprise** | `projects/<YOUR_GCP_PROJECT_ID>/instances/ntt-kg-demo/databases/plant-kg` | `100 PU` (`asia-southeast1`), `optimizer_version = 7`, `OkfEmbeddingModel` (`text-embedding-005`), `OkfChunksSearchIdx`, `OkfChunksEmbeddingIdx` (`COSINE`) |
| **Spanner Property Graph** | `PlantKnowledgeGraph` (ISO GQL) | `426` Nodes (`11` Units, `61` Equipment, `212` Instruments, `131` Boundaries, `11` Docs) + `885` Edges; `RH-E-9A` (`9` monitors) & `RH-E-9B` (`8` monitors) verified |
| **Spanner Hybrid Search** | `OkfChunks` (`762` chunks, `0` null embeddings) | Live RRF Hybrid top hits: `RH-E-9A` (*Hazards & Safeguards*), `FIS-610` (*Bypass Interlock*), `RH-P-8A` (*Hazards & Safeguards*) |
| **Dataplex Knowledge Catalog** | `projects/<YOUR_GCP_PROJECT_ID>/locations/asia-southeast1/entryGroups/okf-plant-knowledge` | `100/100` Custom Entries + `okf-plant-asset-aspect` + `8/8` Business Glossary terms (`okf-plant-glossary`); live NL search returning `RH-E-9B`, `RH-E-9A`, `CC-E-17A`, `SS-E-106`, `SCC-E-29A` |

## Console Demo URLs
- **Spanner Studio (Hybrid Search SQL + Visual Property Graph GQL):**
  `https://console.cloud.google.com/spanner/instances/ntt-kg-demo/databases/plant-kg/studio?project=<YOUR_GCP_PROJECT_ID>`
- **Dataplex Knowledge Catalog (Natural Language Search):**
  `https://console.cloud.google.com/dataplex/search?project=<YOUR_GCP_PROJECT_ID>`

## Root Cause Analysis (RCA) Log (Rule 13)
- **RCA-01 (`test_demo_queries_and_playbook_reference_real_entities`):** Embedded complete copy-pasteable Demo Query 6 (`RRF + GRAPH_TABLE`) directly into `docs/DEMO_SCRIPT_AND_INTRO.md` Step 3.3 (`10/10` pytest pass).
- **RCA-02 (Spanner `instance.display_name` 30-char limit):** Added validated `NONPROD_SPANNER_DISPLAY_NAME="NTT Plant Knowledge Graph"` (`25` chars) to `.env`, `.env.example`, `config.py`, and unit tests.
- **RCA-03 (Spanner GoogleSQL DML `UPDATE ... FROM` join constraint):** Replaced `UPDATE ... FROM ML.PREDICT` with batched `SELECT ChunkId, embeddings.values FROM ML.PREDICT(...)` + `database.batch().update(...)`, embedding all `762/762` chunks cleanly.
- **RCA-04 (Dataplex `EntryType.type_aliases` enum & `GlossaryTerm.parent`):** Mapped `type_aliases=["NODE", "RESOURCE"]` with unit-test guard, set `GlossaryTerm.parent`, and used `UpdateEntryRequest` for idempotent re-runs.
- **RCA-05 (Spanner Live Dialect for `SCORE()`, `UNNEST WITH OFFSET`, & GQL `UNION ALL`):** Enabled DB-level `optimizer_version = 7` + `@{OPTIMIZER_VERSION=7}` statement prefix, used `UNNEST(ARRAY(SELECT AS STRUCT ...)) WITH OFFSET` for 1-indexed RRF ranking, and single `GRAPH PlantKnowledgeGraph` header across GQL `UNION ALL` queries.
