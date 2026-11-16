# Easy 5–7 Minute Demo Guide (Plain-English Presenter Script)

- **Total Time:** **5–7 Minutes**
  - **Part 1 — Intro:** `1–2 minutes` *(Set the story around plain-English discovery, data lineage & connected equipment)*
  - **Part 2 — Knowledge Catalog (Data Lineage Focus):** `~3 minutes` *(Search in plain English & trace 3-stage data lineage from upstream blueprints $\rightarrow$ Cloud Storage $\rightarrow$ Spanner)*
  - **Part 3 — Cloud Spanner:** `~3 minutes` *(Click "Run" on 2 pre-pasted queries: Hybrid Search + Visual Map)*
- **No Coding Live:** You will **not** write any code during the demo. Everything is either plain-English search or clicking the blue **Run** button on two pre-pasted tabs!

---

## Quick Dictionary (In Case Someone Asks What an Equipment or Drawing Code Means)

You don't need to be an engineer! Only a few items appear on screen—think of them like parts of a home heating/cooling system plus their original blueprints:
- **`ML101620329 Part 1` & `Part 2` (`PID-1-SI-LR20448` / `PID-1-SI-LR20449`)** = **Upstream Plant Blueprints (PDF Packages)** *(where the equipment rules were extracted from—and where two drawings disagree!)*
- **`CBS-TK-10A`** = **Emergency Water Tank (Sump)** *(stores cooling water)* -> protected by chamber `CBS-TK-101A` and flexible pipe joint `CBS-EP-36A`
- **`RH-P-8A`** = **Cooling Water Pump** *(pumps water out of the tank)*
- **`RH-E-9A`** = **Heat Exchanger (Cooler)** *(cools the hot water down—and carries a **red-flag lineage conflict** between those two upstream blueprints!)*
- **`FIS-610`** & **`FIS-7325`** = **Smart Flow Safety Switches** *(sensors that automatically open a bypass valve if water flow drops too low so the pump doesn't overheat)*

---

## 2-Minute Prep Before Your Meeting Starts

Open these **3 browser tabs** ahead of time so your demo is effortless:

1. **Tab 1 (The Big Picture Diagram):** Open [`docs/ntt-kg-demo-architecture.html`](./ntt-kg-demo-architecture.html) in your browser.
2. **Tab 2 (Knowledge Catalog):** Go to **Google Cloud Console $\rightarrow$ Dataplex $\rightarrow$ Search**
   `https://console.cloud.google.com/dataplex/search?project=<YOUR_GCP_PROJECT_ID>`
   - *Check:* Make sure the **"Natural language search"** toggle switch near the search bar is turned **ON** (leave it **ON** for all Knowledge Catalog steps!).
3. **Tab 3 (Spanner Studio):** Go to **Google Cloud Console $\rightarrow$ Spanner $\rightarrow$ `ntt-kg-demo` $\rightarrow$ `plant-kg` $\rightarrow$ Spanner Studio**
   `https://console.cloud.google.com/spanner/instances/ntt-kg-demo/databases/plant-kg/studio?project=<YOUR_GCP_PROJECT_ID>`
   - *Prep Trick:* Click **`+` (New SQL editor tab)** twice and copy-paste **Query 1** (from Part 3A below) into the first tab and **Query 2** (from Part 3B below) into the second tab *before* the call. During the demo, all you do is click **Run**!

---

## Part 1: Introduction (`1–2 Minutes`)

### What to Show
Start on **Tab 1** (the visual diagram).

### What to Say (Plain-English Story)
> *"Think about how much critical knowledge inside a company is trapped in hundreds of manuals, PDFs, and engineering diagrams.*
>
> *When someone asks a real-world question—like **'Which cooler handles shutdown cooling, where did that specification come from, and do all our upstream blueprints agree?'**—ordinary tools struggle for three reasons:*
> 1. ***Zero data lineage across documents and databases:** Once numbers are copied from PDF blueprints into a database or AI index, nobody knows which blueprint a rule came from—or when two source drawings contradict each other.*
> 2. ***Keyword vs. AI search trade-offs:** Normal `Ctrl+F` keyword search needs exact part numbers like `FIS-610`, while pure AI vector search understands concepts like 'prevent pump overheating' but often mixes up similar part codes.*
> 3. ***Hidden downstream impact:** Standard search lists isolated files instead of mapping how tanks, pumps, coolers, sensors, and source documents connect.*
>
> *In the next 5 minutes, right inside the standard Google Cloud Console with zero custom apps, I'll show you two tools working together:*
> - *First, **Knowledge Catalog**—giving anyone plain-English discovery plus **end-to-end data lineage** from upstream engineering PDFs $\rightarrow$ curated Cloud Storage specs $\rightarrow$ live Spanner database tables, immediately flagging blueprint conflicts.*
> - *Second, **Cloud Spanner**—combining exact part-number search, AI meaning search, and a clickable visual equipment & lineage map all in one database."*

---

## Part 2: Knowledge Catalog — Plain-English Discovery & End-to-End Data Lineage (`~3 Minutes`)

Switch to **Tab 2 (Dataplex Knowledge Catalog $\rightarrow$ Search)** *(keep **"Natural language search" ON**)*.

### Step 2A: Discover the Asset & Trace Its 3-Stage Data Lineage (`~1.5 mins`)
1. **[Click & Paste]** into the top search bar and press **Enter**:
   ```text
   heat exchangers that cool reactor coolant during shutdown or post-accident sump recirculation
   ```
2. **[What You'll See]:** Right at the top, you'll see **`RH-E-9A — RHR Loop A Heat Exchanger`** and **`RH-E-9B`**.
3. **[Click]** on **`RH-E-9A — RHR Loop A Heat Exchanger`** and scroll slightly down to the **Aspects (`OKF Plant Engineering Asset Aspect`)** box to walk through the **3-Stage Data Lineage Trail**:
   - **Stage 1 — Upstream Source Blueprints (`governing_standard_or_drawing` + `has_discrepancy_warning`):**
     - Point out `governing_standard_or_drawing`: **`PID-1-SI-LR20449, PID-1-SI-LR20448, ML101620329-part-1, ML101620329-part-2`**.
     - Point out `has_discrepancy_warning`: **`true`** (alongside `safety_classification`: `Safety Class 2 (Tube Side) & Safety Class 3 (Shell Side)`).
   - **Stage 2 — Curated Cloud Storage Knowledge File (`gcs_markdown_uri`):**
     - Point out `gcs_markdown_uri`: **`gs://<YOUR_GCP_PROJECT_ID>-okf-bundle/okf_bundle/equipment/RH-E-9A.md`** *(the verified Open Knowledge Format spec extracted from those PDFs)*.
   - **Stage 3 — Downstream Database Node (`spanner_entity_id` & `Platform`):**
     - Point out `spanner_entity_id`: **`EQ:RH-E-9A`** inside **`Spanner Knowledge Graph`**.
4. **[Say This]:**
   > *"With one plain-English search—no part codes needed—Knowledge Catalog found `RH-E-9A` and shows its complete **3-stage data lineage** on one card:*
   > 1. ***Upstream origin:** It traces straight back to the exact engineering PDF packages (`ML101620329-part-1` and `part-2`) and drawing sheets (`PID-1-SI-LR20448` and `PID-1-SI-LR20449`)—and flags **`has_discrepancy_warning: true`** because those two upstream blueprints disagree!*
   > 2. ***Curated middle layer:** It links to the exact human-verified Markdown specification in Cloud Storage (`gcs_markdown_uri`).*
   > 3. ***Downstream target:** It gives us the exact primary key (`EQ:RH-E-9A`) where this asset lands inside Cloud Spanner."*

### Step 2B: Follow the Lineage Upstream to Source PDFs & Downstream to Spanner Lineage Tables (`~1.5 mins`)
1. **[Trace Upstream — Click Back to Search Bar, Paste & Press Enter]:**
   ```text
   source P&ID packages covering Residual Heat Removal and Safety Injection
   ```
   - **[What You'll See]:** Surfaces **`P&ID Package: ML101620329 Part 2 (Seabrook Station LR P&IDs)`** and **`P&ID Package: ML101620329 Part 1 (Seabrook Station LR P&IDs)`** right at the top!
   - **[Say This]:** *"If an auditor or safety engineer asks 'Show me the exact upstream blueprint packages behind `RH-E-9A`', we type that in plain English and immediately pull up cataloged `Source Document` entries for **Part 1** (`PID-1-SI-LR20448`) and **Part 2** (`PID-1-SI-LR20449`)."*
2. **[Trace Downstream — Paste into Search Bar & Press Enter]:**
   ```text
   Spanner document lineage tables
   ```
   - **[What You'll See]:** Surfaces the system-cataloged `CLOUD_SPANNER` tables **`InstrumentDocumentLineage`**, **`UnitDocumentLineage`**, **`EquipmentDocumentLineage`**, and **`GovernanceDocs`**.
   - **[Say This]:** *"And looking downstream, Knowledge Catalog automatically catalogs the live **Cloud Spanner lineage tables** (`EquipmentDocumentLineage`, `InstrumentDocumentLineage`, `GovernanceDocs`) side-by-side with our unstructured engineering documents."*
3. **[Optional 15-Second Sensor Check]:** You can also find safety sensors by symptom without knowing part numbers:
   ```text
   flow switches that prevent charging pump deadheading or cavitation
   ```
   *(Surfaces safety flow switches `FIS-7325` and `FIS-610` immediately!)*
4. **[Transition to Spanner — Say This]:**
   > *"Knowledge Catalog just gave us plain-English discovery and full document-to-database lineage around `RH-E-9A` and `FIS-610`. Now let's switch to **Cloud Spanner** to search inside the engineering text and visually map the connected pipes and lineage edges."*

---

## Part 3: Cloud Spanner — Hybrid Search & Visual Equipment Map (`~3 Minutes`)

Switch to **Tab 3 (Spanner Studio)**.

### Step 3A: Spanner Hybrid Search — Exact Codes + AI Meaning Together (`~1.5 mins`)
1. **[Click]** your pre-pasted **Editor Tab 1** and click the blue **Run** button:
   ```sql
   @{OPTIMIZER_VERSION=7}
   WITH
     -- 1) Turn our plain-English question into AI meaning numbers right inside SQL
     QueryVector AS (
       SELECT embeddings.values AS q_vec
       FROM ML.PREDICT(
         MODEL OkfEmbeddingModel,
         (SELECT 'Interlock G RHR heat exchanger bypass low suction flow cavitation Safety Class 2' AS content)
       )
     ),
     -- 2) Exact Keyword Search: pass the EXACT SAME plain-English question into SEARCH()
     KeywordCandidates AS (
       SELECT item.ChunkId, off + 1 AS fts_rank
       FROM UNNEST(
         ARRAY(
           SELECT AS STRUCT c.ChunkId
           FROM OkfChunks AS c
           WHERE SEARCH(c.ChunkTokens, 'Interlock G RHR heat exchanger bypass low suction flow cavitation Safety Class 2')
           ORDER BY SCORE(c.ChunkTokens, 'Interlock G RHR heat exchanger bypass low suction flow cavitation Safety Class 2') DESC, c.ChunkId
           LIMIT 30
         )
       ) AS item WITH OFFSET AS off
     ),
     -- 3) AI Meaning Search: find Top 30 matches by concept similarity (#1, #2, #3...)
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
     -- 4) Fair Rank Merger (RRF): blend both rank lists into one combined score
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
   -- 5) Show the Top 8 winning paragraphs with side-by-side rankings
   SELECT
     c.Tag,
     c.EntityLabel,
     c.SectionHeading,
     c.HasConflict,
     f.fts_rank AS exact_keyword_rank,
     f.vec_rank AS ai_meaning_rank,
     ROUND(f.rrf_score, 5) AS combined_hybrid_score,
     SUBSTR(c.ChunkText, 1, 220) AS snippet
   FROM RrfFused AS f
   JOIN OkfChunks AS c ON c.ChunkId = f.ChunkId
   ORDER BY f.rrf_score DESC
   LIMIT 8;
   ```
2. **How Query 3A Works (Explain in ~25 Seconds):**
   > *"Notice we pass the **exact same plain-English question** into four building blocks inside one database call:*
   > 1. ***`QueryVector` (`ML.PREDICT`):** Spanner calls Google's Vertex AI model directly inside SQL to turn our question into 'meaning numbers' (an embedding)—no extra Python server needed.*
   > 2. ***`KeywordCandidates` (`SEARCH` + `SCORE`):** Runs a strict `Ctrl+F` keyword search on that exact same question—requiring every word to appear in the paragraph.*
   > 3. ***`VectorCandidates` (`COSINE_DISTANCE`):** Simultaneously runs an AI meaning search, finding passages that match the engineering concept even when the wording differs.*
   > 4. ***`RrfFused` (Reciprocal Rank Fusion):** Fairly blends their finishing positions (`1 / (60 + rank)`) so neither side's blind spot loses critical safety answers."*
3. **What to Point Out in the Results Table:**
   > *"Look at rows 1 and 2—this visually proves why you need Hybrid Search:*
   > - ***Row 1 (`FIS-610`):** Pure AI search buried this flow switch down at **#11**, while exact keyword search ranked it **#1**—so Hybrid Search puts it right at **#1**.*
   > - ***Row 2 (`RH-E-9A`, `HasConflict = true`):** Strict keyword search **completely missed it (`null`)** because the manual didn't use the literal word 'cavitation', while AI meaning search ranked it **#1**—so Hybrid Search rescues it right into **#2**!"*

### Step 3B: Spanner Graph — Clickable Visual Equipment Map (`~1.5 mins`)
1. **[Click]** your pre-pasted **Editor Tab 2** and click the blue **Run** button:
   ```sql
   GRAPH PlantKnowledgeGraph
   -- Part 1: Start at the emergency water tanks and follow pipes 1 to 3 hops downstream
   MATCH p1 = (sump:Equipment)-[:FLOWS_TO]->{1,3}(hx:Equipment)
   WHERE sump.Tag IN ('CBS-TK-10A', 'CBS-TK-10B')
   RETURN SAFE_TO_JSON(p1) AS graph_path
   UNION ALL
   -- Part 2: Attach the safety sensors monitoring that equipment and their plant systems
   MATCH p2 = (inst:Instrument)-[:MONITORS]->(eq:Equipment)-[:BELONGS_TO_UNIT]->(u:PlantUnit)
   WHERE eq.Tag IN ('CBS-TK-10A', 'CBS-TK-101A', 'RH-P-8A', 'RH-E-9A')
     AND inst.IsFullSpec = TRUE
   RETURN SAFE_TO_JSON(p2) AS graph_path;
   ```
2. **How Query 3B Works (Explain in ~20 Seconds):**
   > *"Notice how short and visual this graph query is compared to writing messy SQL table joins:*
   > 1. ***`GRAPH PlantKnowledgeGraph`:** Tells Spanner to read the exact same database tables as a connected network of equipment and pipes—no separate graph database or data copy required.*
   > 2. ***`MATCH p1 = (sump)-[:FLOWS_TO]->{1,3}(hx)`:** Reads just like arrows on a whiteboard! It starts at the emergency water tanks (`CBS-TK-10A`, `CBS-TK-10B`) and automatically hops **1 to 3 pipe connections downstream** (`->{1,3}`) to trace where the water goes.*
   > 3. ***`UNION ALL MATCH p2 = (inst)-[:MONITORS]->(eq)-[:BELONGS_TO_UNIT]->(u)`:** Layers on every full-spec safety sensor (`MONITORS`) watching over those parts plus the plant unit (`BELONGS_TO_UNIT`) each piece belongs to, and **`SAFE_TO_JSON`** packages those paths so Spanner Studio draws an interactive map."*
3. **[IMPORTANT CLICK]:** In the bottom **Results** area, switch from `Table` to the **`Graph`** tab! *(Optional: click **`Schema View`** for 3 seconds to show the 5 color-coded categories: Units, Equipment, Instruments, Boundaries, and Documents, then switch back to the graph).*
4. **[Click Nodes on the Map & Say This]:**
   > *"Instead of flipping through 10 separate piping manuals, watch how easy it is to follow the water path right on screen:*
   > - *Here is the emergency water tank (`CBS-TK-10A`), passing through its protective chamber (`CBS-TK-101A`) and flexible joint (`CBS-EP-36A`), straight into the cooling pump (`RH-P-8A`), and into our heat exchanger (`RH-E-9A`).*
   > - *And branching right off them are the exact safety sensors watching over each step—including flow switch `FIS-610`!"*

### Wrap-Up Sentence (`15 Seconds`)
> *"To sum up: normally, companies have to stitch together four separate systems—a keyword search tool, an AI vector database, a graph database, and a lineage catalog—and lose track of where engineering numbers came from. With Google Cloud, **Knowledge Catalog** gives everyone plain-English discovery plus **end-to-end document-to-database data lineage**, and **Cloud Spanner** handles **exact keywords, AI meaning search, and visual relationship maps** all inside one trusted database."*

---

## Optional Backup Queries (Only If Someone Asks in Q&A!)

### Q&A Option 1: "Can we also visualize that upstream document lineage (`EXTRACTED_FROM` / `GOVERNED_BY`) on the Spanner Graph?"
Yes! Paste this query and click the **`Graph`** tab—it visually connects our flagged coolers (`RH-E-9A` and `RH-E-9B`) to their upstream P&ID source packages (`ML101620329 Part 1` & `Part 2`), IEC 61882 HAZOP governance standards, and connected pipes/sensors:
```sql
GRAPH PlantKnowledgeGraph
MATCH path_flow = (upstream:Equipment)-[:FLOWS_TO]->(conflict_eq:Equipment {HasConflict: TRUE})
RETURN SAFE_TO_JSON(path_flow) AS conflict_blast_radius
UNION ALL
MATCH path_inst = (inst:Instrument)-[:MONITORS]->(conflict_eq:Equipment {HasConflict: TRUE})
RETURN SAFE_TO_JSON(path_inst) AS conflict_blast_radius
UNION ALL
MATCH path_gov = (conflict_eq:Equipment {HasConflict: TRUE})-[:EXTRACTED_FROM|GOVERNED_BY]->(doc:GovernanceDoc)
RETURN SAFE_TO_JSON(path_gov) AS conflict_blast_radius;
```

### Q&A Option 2: "Can Spanner run Hybrid Search AND walk the Equipment Graph in a single step?"
Yes! Paste this query—it uses Hybrid Search to find the water purifier (**`DM-8`**, prefilter `F-33`, postfilter `F-34`) and automatically pulls every connected pressure sensor and pipe in the exact same query:
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
  ROUND(h.best_rrf_score, 5) AS hybrid_score,
  g.EquipmentTitle,
  g.MonitoringInstrument,
  g.AlarmOrInterlock,
  g.FlowsToTag
FROM TopHybridEntities AS h
JOIN GraphContext AS g
  ON h.EntityId = g.EntityId
ORDER BY h.best_rrf_score DESC, g.MonitoringInstrument;
```
