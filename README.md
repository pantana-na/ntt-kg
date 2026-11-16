# Plant Knowledge Graph & Knowledge Catalog Demo

## What Is This Demo? (In Plain English)

Imagine an industrial plant or factory with **hundreds of equipment manuals, piping diagrams, and safety checklists**. Today, when someone asks a simple question—*"Which heat exchangers cool the plant during shutdown, where did that data come from, and do any of our upstream blueprints contradict each other?"*—answering it takes hours of hunting through folders, PDFs, and databases.

This repository sets up a **5–7 minute live demo** directly inside the **Google Cloud Console** (no custom website or app to maintain) showing two capabilities working together:

1. **Google Cloud Knowledge Catalog (Dataplex) — *"Plain-English Discovery & End-to-End Data Lineage"* (~3 mins):**
   - Anyone (even non-technical users) can type a **plain-English question** in the search bar to find equipment, safety sensors, upstream engineering blueprints, and live database lineage tables in one place.
   - Every catalog card traces **3-stage data lineage & provenance**: from **upstream raw P&ID blueprints** (`ML101620329 Part 1 & Part 2`, `PID-1-SI-LR20448`, `PID-1-SI-LR20449`) $\rightarrow$ **curated Cloud Storage Markdown specs** (`gcs_markdown_uri`) $\rightarrow$ **downstream Cloud Spanner Graph & Lineage tables** (`EQ:RH-E-9A`, `EquipmentDocumentLineage`)—immediately flagging **discrepancy warnings** when two upstream engineering drawings disagree.
2. **Google Cloud Spanner — *"Smart Hybrid Search + Visual Equipment Map"* (~3 mins):**
   - **Hybrid Search:** Combines **exact code matching** (like `Ctrl+F` for part numbers such as `FIS-610`) with **AI meaning search** (understanding concepts like *"prevent pump overheating or low-flow damage"*) in one step so the right answer always rises to the top.
   - **Visual Knowledge Graph:** Draws an interactive, color-coded map of how tanks, pipes, pumps, heat exchangers, safety alarms, and source governance documents connect to each other—so you can visually trace upstream and downstream impact in one click.

---

## Key Links in This Repo

- **[5–7 Minute Presenter Script & Talk-Track (`docs/DEMO_SCRIPT_AND_INTRO.md`)](./docs/DEMO_SCRIPT_AND_INTRO.md)** — Step-by-step "[Click Here]" and "[Say This]" guide focused on **Knowledge Catalog Data Lineage** + **Spanner Hybrid Search & Graph**.
- **[Visual Architecture Diagram (`docs/ntt-kg-demo-architecture.html`)](./docs/ntt-kg-demo-architecture.html)** — Open in any web browser to show the high-level picture during your 1-minute intro.
- **[Extra Copy-Paste Queries (`sql/demo_queries_spanner.sql`)](./sql/demo_queries_spanner.sql)** — Ready-to-run queries for Spanner Studio (including visual document-lineage blast-radius queries).

---

## What Gets Loaded from `okf_bundle/`?

The [`okf_bundle/`](./okf_bundle) folder contains **100 real-world plant engineering records** (from public power-plant piping diagrams and safety standards) with complete **document-to-database lineage**:
- **61 Pieces of Equipment** (Pumps, Heat Exchangers, Storage Sumps, Filters, Fans)
- **212 Safety Sensors & Gauges** (Flow switches, pressure sensors, radiation monitors, safety interlocks)
- **11 Upstream Source Blueprints & Safety Standards** (`ML101620329` P&ID packages, IEC 61882 HAZOP & Risk Assessment standards) linked via `EquipmentDocumentLineage`, `InstrumentDocumentLineage`, and `UnitDocumentLineage`
- **885 Graph & Lineage Connections** tracing both how water/steam flows between equipment and which upstream drawings each asset was extracted from
- **Built-in "Lineage Spotlights the Conflict" Story:** Two heat exchangers (`RH-E-9A` and `RH-E-9B`) trace back to **two conflicting upstream P&ID drawings** (`PID-1-SI-LR20448` vs. `PID-1-SI-LR20449`)—showing how data lineage catches dangerous blueprint mismatches before HAZOP review!

---

## Setup in 3 Easy Steps (One-Time Before Your Demo)

### Step 1: Configure Your Google Cloud Project ID
Copy the example settings file to `.env` (`.env` stays private on your computer and is never uploaded to Git):
```bash
cp .env.example .env
```
Open `.env` in any text editor and replace `your-gcp-project-id` on these two lines with your own Google Cloud Project ID:
```ini
GCP_PROJECT=your-gcp-project-id
NONPROD_GCS_BUCKET=your-gcp-project-id-okf-bundle
```

### Step 2: Sign In to Google Cloud
```bash
gcloud auth login
gcloud auth application-default login
gcloud config set project "YOUR_GCP_PROJECT_ID"
```

### Step 3: Run the 1-Command Installer
```bash
bash scripts/deploy_all.sh
```
*(Takes ~4–5 minutes. It turns on the required Google Cloud services, creates a small low-cost Spanner database, generates AI search embeddings, loads the 100 Knowledge Catalog cards, and prints the exact **Google Cloud Console links** to open in your browser!)*

---

## Clean Up After Your Demo (Stop Cloud Charges)

When you are finished presenting, run this single command to delete the demo database and stop ongoing cloud costs:
```bash
bash scripts/99_teardown.sh --yes
```

*(Optional for developers: run `.venv/bin/pytest -v` to run the automated test suite, or see [`specs/features/SPEC-20261116-NTT-KG-DEMO.md`](./specs/features/SPEC-20261116-NTT-KG-DEMO.md) for the technical design spec.)*
