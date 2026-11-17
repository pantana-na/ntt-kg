# Plan Progress Report — Dataplex REST Hardening & Sandbox Deployment (`2026-11-17`)

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
| **Automated Test Suite** | `pytest` (`tests/unit/` + `tests/property/`) | `12/12` tests passing (`100%`) |

## Console Demo URLs
- **Spanner Studio (Hybrid Search SQL + Visual Property Graph GQL):**
  `https://console.cloud.google.com/spanner/instances/ntt-kg-demo/databases/plant-kg/studio?project=<YOUR_GCP_PROJECT_ID>`
- **Dataplex Knowledge Catalog (Natural Language Search):**
  `https://console.cloud.google.com/dataplex/search?project=<YOUR_GCP_PROJECT_ID>`

## Root Cause Analysis (RCA) Log (Rule 13)
- **RCA-06 (Dataplex gRPC `8192`-byte trailing metadata soft limit on `get_glossary_term` 404):** Switched `CatalogServiceClient` and `BusinessGlossaryServiceClient` to `transport="rest"` in `scripts/04_load_dataplex.py` and `scripts/05_verify_demo.py`, and replaced per-term `get_glossary_term` 404 probes with single `list_glossaries` / `list_glossary_terms` lookups (`test_seed_business_glossary_uses_list_without_404_probes`).
- **RCA-07 (REST HTTP `409 Conflict` exception mapping on Dataplex re-runs):** Added `upsert_catalog_entries()` with single `list_entries` pre-check and `(gcp_exceptions.AlreadyExists, gcp_exceptions.Conflict)` handling across both REST and gRPC transports (`test_upsert_catalog_entries_prelists_and_handles_rest_conflict`).
