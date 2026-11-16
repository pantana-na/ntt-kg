# Easy 5–7 Minute Demo Guide (Plain-English Presenter Script)

- **Total Time:** **5–7 Minutes**
  - **Part 1 — Intro:** `1–2 minutes` *(Set the story in everyday words)*
  - **Part 2 — Knowledge Catalog:** `~3 minutes` *(Search in plain English—no code at all)*
  - **Part 3 — Cloud Spanner:** `~3 minutes` *(Click "Run" on 2 pre-pasted queries: Hybrid Search + Visual Map)*
- **No Coding Live:** You will **not** write any code during the demo. Everything is either plain-English search or clicking the blue **Run** button on two pre-pasted tabs!

---

## Quick Dictionary (In Case Someone Asks What an Equipment Code Means)

You don't need to be an engineer! Only 4 items appear on screen—think of them like parts of a home heating/cooling system:
- **`CBS-TK-10A`** = **Emergency Water Tank (Sump)** *(stores cooling water)* -> protected by chamber `CBS-TK-101A` and flexible pipe joint `CBS-EP-36A`
- **`RH-P-8A`** = **Cooling Water Pump** *(pumps water out of the tank)*
- **`RH-E-9A`** = **Heat Exchanger (Cooler)** *(cools the hot water down—and has a **red-flag conflict** between two plant blueprints!)*
- **`FIS-610`** & **`FIS-7325`** = **Smart Flow Safety Switches** *(sensors that automatically open a bypass valve if water flow drops too low so the pump doesn't overheat)*

---

## 2-Minute Prep Before Your Meeting Starts

Open these **3 browser tabs** ahead of time so your demo is effortless:

1. **Tab 1 (The Big Picture Diagram):** Open [`docs/ntt-kg-demo-architecture.html`](./ntt-kg-demo-architecture.html) in your browser.
2. **Tab 2 (Knowledge Catalog):** Go to **Google Cloud Console $\rightarrow$ Dataplex $\rightarrow$ Search**
   `https://console.cloud.google.com/dataplex/search?project=<YOUR_GCP_PROJECT_ID>`
   - *Check:* Make sure the **"Natural language search"** toggle switch near the search bar is turned **ON**.
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
> *When someone asks a real-world question—like **'Which cooler handles shutdown cooling, what safety sensor protects it if water flow drops, and do all our blueprints agree?'**—ordinary search tools struggle for three reasons:*
> 1. ***Normal keyword search** is like `Ctrl+F`: it's great if you already know exact part numbers like `FIS-610`, but useless if you type 'prevent pump overheating' and the manual used different words.*
> 2. ***AI vector search** understands meaning and concepts, but often mixes up similar-looking part numbers and codes.*
> 3. ***Neither one shows how things connect**—like which tank feeds which pump and which cooler.*
>
> *In the next 5 minutes, right inside the standard Google Cloud screen with zero custom apps, I'll show you two tools working together:*
> - *First, **Knowledge Catalog**—which works like Google Search for non-technical users to find equipment and spot safety warnings in plain English.*
> - *Second, **Cloud Spanner**—which combines exact part-number search, AI meaning search, and a clickable visual equipment map all in one place."*

---

## Part 2: Knowledge Catalog — Plain-English Discovery (`~3 Minutes`)

Switch to **Tab 2 (Dataplex Knowledge Catalog $\rightarrow$ Search)**.

### Step 2A: Ask a Question in Everyday English (`~1.5 mins`)
1. **[Click & Paste]** into the top search bar and press **Enter**:
   ```text
   heat exchangers that cool reactor coolant during shutdown or post-accident sump recirculation
   ```
2. **[What You'll See]:** Right at the top, you'll see **`RH-E-9B`** and **`RH-E-9A — RHR Loop A Heat Exchanger`**.
3. **[Say This]:**
   > *"Notice I didn't type any part numbers or technical codes—just a plain-English question. Knowledge Catalog understood what I meant and immediately found the exact cooling equipment (`RH-E-9A` and `RH-E-9B`), right alongside the database tables where they live."*
4. **[Click]** on **`RH-E-9A — RHR Loop A Heat Exchanger`** in the results list and scroll slightly down to the **Aspects (`OKF Plant Engineering Asset Aspect`)** box:
   - **[Point Out 3 Simple Fields]:**
     - **`safety_classification`:** Shows its safety rating (`Safety Class 2 and 3`).
     - **`has_discrepancy_warning: true`:** *"Look right here—Knowledge Catalog flags `true` for discrepancy warning! That immediately alerts our team that two engineering drawings disagree on this cooler before anyone makes a costly mistake."*
     - **`gcs_markdown_uri`:** Direct link back to the original source document.

### Step 2B: Combine Plain English + a One-Line Filter (`~1.5 mins`)
1. **[Click Back]** to the Knowledge Catalog search bar, paste this, and press **Enter**:
   ```text
   flow switches that prevent charging pump deadheading or cavitation
   ```
   *(Instant plain-English match: surfaces the safety flow switches `FIS-7325` and `FIS-610` even though we described the problem—"pump overheating/cavitation"—instead of typing their part codes!)*
2. **[Optional 20-Second Bonus Filter]:** Show that you can also filter specifically for items with active safety warnings:
   ```text
   safety interlock AND okf-plant-asset-aspect.has_discrepancy_warning:true
   ```
3. **[Transition to Spanner — Say This]:**
   > *"So Knowledge Catalog makes it effortless for anyone in the business to find trusted assets and spot flagged items like `RH-E-9A` and `FIS-610`. Now, what if an engineer or AI assistant needs to dig deeper into the manuals AND trace every pipe connected to that equipment? Let's switch to **Cloud Spanner**."*

---

## Part 3: Cloud Spanner — Hybrid Search & Visual Equipment Map (`~3 Minutes`)

Switch to **Tab 3 (Spanner Studio)**.

### Step 3A: Spanner Hybrid Search — Exact Codes + AI Meaning Together (`~1.5 mins`)
1. **[Click]** your pre-pasted **Editor Tab 1** and click the blue **Run** button:
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
2. **[Point to the Results Table & Say This]:**
   > *"Don't worry about the SQL—just look at what Spanner did in under a second, and look at these three columns (`exact_keyword_rank`, `ai_meaning_rank`, and `combined_hybrid_score`):*
   > - *First, Spanner called Google's AI model directly inside the database to understand the meaning of our question—no extra app or middleman needed.*
   > - *Second, it ran **both** an **exact code search** (`Interlock G`, `Safety Class 2`) AND an **AI meaning search** (`low suction flow cavitation`) at the same time, then blended both rankings together.*
   > - *Look at rows 1 and 2: our cooler **`RH-E-9A`** (ranked #5 by keywords, #1 by AI meaning) and safety switch **`FIS-610`** (ranked #4 by keywords, #7 by AI meaning) rise straight to the top! Even if a document only matched by meaning or only matched by part number, Hybrid Search catches it."*

### Step 3B: Spanner Graph — Clickable Visual Equipment Map (`~1.5 mins`)
1. **[Click]** your pre-pasted **Editor Tab 2** and click the blue **Run** button:
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
2. **[IMPORTANT CLICK]:** In the bottom **Results** area, switch from `Table` to the **`Graph`** tab! *(Optional: click **`Schema View`** for 3 seconds to show the 5 color-coded categories: Units, Equipment, Instruments, Boundaries, and Documents, then switch back to the graph).*
3. **[Click Nodes on the Map & Say This]:**
   > *"Instead of reading through 10 separate piping manuals, Spanner turns our data into a live interactive map. Watch how easy it is to follow the water path:*
   > - *Here is the emergency water tank (`CBS-TK-10A`), passing through its protective chamber (`CBS-TK-101A`) and flexible joint (`CBS-EP-36A`), straight into the cooling pump (`RH-P-8A`), and into our heat exchanger (`RH-E-9A`).*
   > - *And branching right off them are the exact safety sensors watching over each step—including flow switch `FIS-610`!"*

### Wrap-Up Sentence (`15 Seconds`)
> *"To sum up: normally, companies have to buy and stitch together four separate systems—a keyword search tool, an AI vector database, a graph database, and a data catalog—and keep copying data between them. With Google Cloud, **Knowledge Catalog** gives everyone plain-English search across the business, and **Cloud Spanner** handles **exact keywords, AI meaning search, and visual relationship maps** all inside one trusted database."*

---

## Optional Backup Query (Only If Someone Asks in Q&A!)

**"Can Spanner run Hybrid Search AND walk the Equipment Graph in a single step?"**
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
