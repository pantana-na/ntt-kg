# Plant Engineering Knowledge Graph & Knowledge Catalog Demo

Operationalizes the **Open Knowledge Format (OKF v0.2)** industrial/nuclear plant engineering bundle ([`okf_bundle/`](./okf_bundle) — public NRC License Renewal P&IDs `ML101620329` Parts 1–3, Safety Interlocks, and IEC 61882 HAZOP / Risk Assessment Matrix standards) into **Google Cloud Spanner** (**Vector + Full-Text + Reciprocal Rank Fusion Hybrid Search + ISO GQL Property Graph**) and **Dataplex Knowledge Catalog (Universal Catalog Natural Language Search)**—experienced **100% natively in the Google Cloud Console** with zero custom UI.

- **5–7 Minute Live Demo Playbook & Intro:** [`docs/DEMO_SCRIPT_AND_INTRO.md`](./docs/DEMO_SCRIPT_AND_INTRO.md)
- **System Architecture & Visual Diagram:** [`docs/ntt-kg-demo-architecture.md`](./docs/ntt-kg-demo-architecture.md) & [`docs/ntt-kg-demo-architecture.html`](./docs/ntt-kg-demo-architecture.html)
- **Spanner Studio SQL & GQL Query Pack:** [`sql/demo_queries_spanner.sql`](./sql/demo_queries_spanner.sql)
- **Feature SDD Specification:** [`specs/features/SPEC-20261116-NTT-KG-DEMO.md`](./specs/features/SPEC-20261116-NTT-KG-DEMO.md)

---

## 1. Corpus & Knowledge Graph Summary (`okf_bundle/`)

| Layer | Loaded Artifacts | Key Capabilities Demonstrated |
| :--- | :--- | :--- |
| **Dataplex Knowledge Catalog** *(~3 min)* | **100 Governed Custom Entries** + Custom Aspect Type `okf-plant-asset-aspect` + **8 Business Glossary Terms** + Cloud Storage Markdown lineage (`gs://<YOUR_BUCKET>/okf_bundle`) + auto-cataloged Spanner tables | **Global Natural Language Search** blended with structured engineering aspect filters (`safety_classification`, `unit_code`, `has_discrepancy_warning`) in Google Cloud Console |
| **Spanner Hybrid Search (`OkfChunks`)** *(~1.5 min)* | **762 Contextualized Section Chunks** with `TOKENIZE_FULLTEXT` + `TOKENIZE_SUBSTRING` `SEARCH INDEX`, `768`-dim `ARRAY<FLOAT32>`, `COSINE` `VECTOR INDEX`, and native `CREATE MODEL OkfEmbeddingModel` (`text-embedding-005`) | Live SQL `ML.PREDICT` semantic search + exact tag/P&ID keyword search fused via **Reciprocal Rank Fusion (RRF)**—zero external embedding code at query time |
| **Spanner Property Graph (`PlantKnowledgeGraph`)** *(~1.5 min)* | **426 Nodes** across 5 color-coded labels (`11` `PlantUnit`, `61` `Equipment`, `212` `Instrument`, `131` `ProcessBoundary`, `11` `GovernanceDoc`) + **885 Directed Edges** (`BELONGS_TO_UNIT`, `FLOWS_TO`, `MONITORS`, `EXTRACTED_FROM`, `GOVERNED_BY`) | Multi-hop P&ID stream traversal (`SAFE_TO_JSON`), safety interlock blast-radius analysis (`Interlock G/H/B`), and cross-drawing discrepancy inspection (`⚠️ CONFLICT` on `RH-E-9A` / `RH-E-9B`) in **Spanner Studio Graph UI** |

---

## 2. Quickstart (1-Command Provisioning & Seeding)

### Prerequisites
1. Copy [`.env.example`](./.env.example) to `.env` (which is git-ignored) and set your target `GCP_PROJECT` and `NONPROD_GCS_BUCKET`:
   ```bash
   cp .env.example .env
   # Edit .env: set GCP_PROJECT=<YOUR_GCP_PROJECT_ID> and NONPROD_GCS_BUCKET=<YOUR_BUCKET_NAME>
   ```
2. Authenticate `gcloud` and Application Default Credentials:
   ```bash
   gcloud auth login
   gcloud auth application-default login
   gcloud config set project "<YOUR_GCP_PROJECT_ID>"
   ```

### Deploy Everything
```bash
bash scripts/deploy_all.sh
```

Or run individual idempotent stages:
```bash
bash scripts/01_provision_infra.sh              # Enable APIs, create GCS bucket, grant Spanner SA Vertex AI role, create 100 PU Spanner Enterprise + DDL
.venv/bin/python scripts/02_load_spanner.py     # Upsert 5 Node tables, 10 Edge tables, and 762 OkfChunks
.venv/bin/python scripts/03_embed_spanner.py    # Backfill 768-dim vectors natively in Spanner via SQL ML.PREDICT + create COSINE Vector Index
.venv/bin/python scripts/04_load_dataplex.py    # Seed AspectType, EntryGroup, EntryType, 100 Entries + Aspects, and Business Glossary
.venv/bin/python scripts/05_verify_demo.py      # Run live RRF Hybrid, GQL Graph, and Dataplex NL Search verification + print Console URLs
```

---

## 3. Running the 5–7 Minute Live Console Demo

Follow [`docs/DEMO_SCRIPT_AND_INTRO.md`](./docs/DEMO_SCRIPT_AND_INTRO.md) for the **tight 5–7 minute flow**:
1. **Intro (`1–2 min`):** Problem hook & architecture overview ([`docs/ntt-kg-demo-architecture.html`](./docs/ntt-kg-demo-architecture.html)).
2. **Knowledge Catalog (`~3 min`):** Natural Language Search + `okf-plant-asset-aspect` discrepancy inspection (`https://console.cloud.google.com/dataplex/search?project=<YOUR_GCP_PROJECT_ID>`).
3. **Cloud Spanner (`~3 min`):** RRF Hybrid Search (`SEARCH` + `ML.PREDICT` `COSINE_DISTANCE`) + Interactive 5-Node Visual Property Graph in Spanner Studio (`https://console.cloud.google.com/spanner/instances/ntt-kg-demo/databases/plant-kg/studio?project=<YOUR_GCP_PROJECT_ID>`).

---

## 4. Testing & Teardown

```bash
# Run deterministic unit tests + Hypothesis property-based tests + dry-run checks
.venv/bin/pytest -v
.venv/bin/python scripts/02_load_spanner.py --dry-run
.venv/bin/python scripts/04_load_dataplex.py --dry-run

# Tear down Spanner instance & Dataplex Catalog after the demo ($0 idle spend)
bash scripts/99_teardown.sh --yes
```
