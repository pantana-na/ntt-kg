# AI-SDLC, Spec-Driven Development (SDD) & Google Cloud WAF/SAIF Governance Platform

An enterprise AI engineering and DevSecOps framework orchestrated by the **[`ai-sdlc` Master Hub Skill](./_agents/skills/ai_sdlc/SKILL.md)** across the **3-Phase AI-Driven Software Development Lifecycle (AI-SDLC)**, **Spec-Driven Development (SDD)**, **Google Agent Development Kit (`google-adk`)**, **Google Cloud Well-Architected Framework (WAF — 6 Pillars)**, and **Google Secure AI Framework (SAIF / SAIF 2.0)**.

> [!IMPORTANT]
> **Supreme Precedence Mandate:** In case of any conflict between legacy rules, templates, or heuristics and the **[Google Cloud Well-Architected Framework (WAF)](https://docs.cloud.google.com/architecture/framework)** or **[Google Secure AI Framework (SAIF / SAIF 2.0)](https://safety.google/intl/en/safety/saif/)**, **WAF and SAIF take strict precedence** ([`gcp-well-architected-saif`](./_agents/skills/gcp_well_architected_saif/SKILL.md)).

---

## 🏛️ Master Hub-and-Spoke Architecture (`ai-sdlc` $\leftrightarrow$ All Rules & Skills)

The **[`ai-sdlc` skill](./_agents/skills/ai_sdlc/SKILL.md)** acts as the **central orchestrator hub** wired bidirectionally to **3 consolidated governance rule files (Rules 1–13)** in [`_agents/rules/`](./_agents/rules/) and **5 specialized companion skills** in [`_agents/skills/`](./_agents/skills/), routed from [`AGENTS.md`](./AGENTS.md):

```
+===================================================================================================+
|                     MASTER HUB SKILL: ai-sdlc (_agents/skills/ai_sdlc/SKILL.md)                   |
|     Phase 1: Inception (Intent & WAF/SAIF Arch) -> Phase 2: Execution (SDD) -> Phase 3: Operation  |
|   (Workspace Scaffolder --init • Dual-Input Discovery Doc + ask_question • Phase Gate Validators)  |
+===================================================================================================+
         │                                         │                                         │
         ▼                                         ▼                                         ▼
+---------------------------------+   +-----------------------------------+   +---------------------------------+
|   SUPREME PRECEDENCE FRAMEWORK  |   |   3 CONSOLIDATED RULES (1 - 13)   |   |    5 COMPANION SPOKE SKILLS     |
|  gcp-well-architected-saif      |   | • ai_sdlc_and_sdd_standards (R13) |   | • requirements-discovery (Opt.) |
| • WAF 6 Pillars + AI/ML & FSI   |   | • google_adk_and_agent_runtime    |   | • gcp-well-architected-saif     |
| • SAIF 6 Elements & 15 Risks    |   |   (Rules 11 - 12: agent_runtime)  |   | • architecture-diagram          |
| • SAIF 2.0 4-Pt Guardrails/HITL |   | • devops_security_and_quality     |   | • codemender (cm find/verify/fix)|
| • validate_waf_saif.py          |   |   (Rules 1 - 10: cloud_run)       |   | • gcp-cost-estimator (Live API) |
+---------------------------------+   +-----------------------------------+   +---------------------------------+
                                                   │
                                                   ▼
+---------------------------------------------------------------------------------------------------+
|                   Mandatory 4-Step RCA Protocol & WAF Graceful Degradation (Rule 13)              |
|  - Zero Synthetic Mockup Data or Regex Heuristics  - Circuit Breakers + Transparent Degraded Mode |
+---------------------------------------------------------------------------------------------------+
```

### Governance Rules Wiring Matrix (Rules 1–13)

| Consolidated Rule File | Trigger | Owned Rules | Core Enforcement Scope |
| :--- | :--- | :--- | :--- |
| **[`ai_sdlc_and_sdd_standards.md`](./_agents/rules/ai_sdlc_and_sdd_standards.md)** | `always_on` | **Lifecycle, SDD & Rule 13** | 3-Phase AI-SDLC, WAF/SAIF Supreme Precedence, Dual-Input (`specs/discovery/` + `ask_question`) zero-assumption & zero-placeholder SDD completion, interactive phase gates, Two-Track Brownfield Baselines (`specs/baseline/`), Feature SDDs (`specs/features/`), Unit Tests + Property-Based Tests (PBT) per step, living plans (`specs/plan/`), and **Rule 13: 4-Step RCA + WAF Graceful Degradation**. |
| **[`google_adk_and_agent_runtime.md`](./_agents/rules/google_adk_and_agent_runtime.md)** | `model_decision` | **Rules 11–12** | **Rule 11:** Official `google-adk` (`OrchestratorAgent`, Read-Only vs. Action Subagents, `FunctionTool`), cognitive MECE intents (`OTHERS`), pinned models + execution budgets (`DMS`), `User Auth` OAuth2 anti-Confused-Deputy propagation, Externalized Deterministic HITL (`RAC`), and **4-point Model Armor + Cloud DLP callbacks**. **Rule 12:** DLP-safe live `agents-cli eval` ($\ge 95\%$ precision, $1.000$ groundedness). |
| **[`devops_security_and_quality_standards.md`](./_agents/rules/devops_security_and_quality_standards.md)** | `model_decision` | **Rules 1–10** | Multi-branch Git (`main`/`develop` $\rightarrow$ `prod`), static quality, pre-build CodeMender SAST (`cm`), Artifact Analysis + **SLSA L3 / Binary Authorization**, Cloud Build (`cloudbuild.yaml`), Cloud Run (`/healthz` probe, SLO burn-rate alerts, OpenTelemetry Trace), smoke tests, unified `.env` + Secret Manager/CMEK, Terraform Infra Manager + **VPC-SC** + FinOps + Sustainability (`CFE %`), and **WAF Zero-Trust IAM/Ingress** (ALB + Cloud Armor + IAP/OAuth2; zero `allUsers`). |

---

## ⚡ Workload Modes & Runtime Architecture (`Regular App` vs. `AI Agent` / `Hybrid`)

Every specification declares **`Workload Type`** (`Regular App` | `AI Agent` | `Hybrid`) in **Document Control**:
- **`Regular App` (Non-AI Web, API, Microservice, or Data Workload):** Runs on **Google Cloud Run (`cloud_run`)** + managed GCP services inside **VPC-SC + CMEK**; enforces **Google Cloud WAF (6 Pillars)** and **Rules 1–10 & Rule 13** (omits `[AI-Agent Only]` sections and Rules 11–12).
- **`AI Agent` / `Hybrid` Workload:** Strictly decoupled across **Dual Runtimes** (`cloud_run` + `agent_runtime`) inside **VPC-SC + CMEK**; enforces **Google Cloud WAF (6 Pillars)**, **Google SAIF / SAIF 2.0**, and **all Rules 1–13**:

| Dimension | Web Frontend, Backend APIs & Policy Gate *(Universal)* | `[AI-Agent Only]` Conversational AI Agents & Reasoning Engine |
| :--- | :--- | :--- |
| **Target Runtime** | **Google Cloud Run (`cloud_run`)** | **Gemini Enterprise Agent Platform (`agent_runtime`)** |
| **Deployed Artifacts** | Global External ALB + Cloud Armor WAF + IAP/OAuth2, React/Vite web client, REST/gRPC APIs or SSE/WS proxy, `/healthz` probe, and deterministic policy/HITL gates. | ADK Root Coordinator (`OrchestratorAgent`), Read-Only vs. Action Domain Subagents, 4-point Model Armor + Cloud DLP callbacks, and `FunctionTool` registries. |
| **Deployment Mechanism** | Google Cloud Build (`cloudbuild.yaml` + SLSA L3/Binary Auth) + Terraform via Google Cloud Infrastructure Manager | `agents-cli deploy --deployment-target agent_runtime` (VPC-SC + CMEK) |
| **Core Responsibilities** | Zero-Trust HTTPS/WSS ingress, human authentication, business APIs, client UI rendering, health/SLO probes (`/healthz`), and *(if AI Agent/Hybrid)* externalized HITL signing + streaming proxy. | Autonomous multi-turn cognitive reasoning, session persistence (`agentengine://`), `User Auth` row/doc ACL tool execution, and DLP-safe trajectory evaluation (`agents-cli eval`). |
| **Governance Rule** | [`_agents/rules/devops_security_and_quality_standards.md`](./_agents/rules/devops_security_and_quality_standards.md) | [`_agents/rules/google_adk_and_agent_runtime.md`](./_agents/rules/google_adk_and_agent_runtime.md) |

---

## 📁 Repository Structure & Workspace Scaffolding

The template directories for `specs/` and `docs/` are packaged inside [`_agents/skills/ai_sdlc/examples/`](./_agents/skills/ai_sdlc/examples/). When the **`ai-sdlc` master skill** is activated on a project (`python3 _agents/skills/ai_sdlc/scripts/validate_sdlc_gate.py --init`), it automatically scaffolds `specs/` and `docs/` into the project root:

```
├── AGENTS.md                              # Authoritative Agent Operating Manual & Executive Governance Router
├── README.md                              # Project root documentation & Hub-and-Spoke architecture overview
├── _agents/                               # Agent governance rules and specialized skill toolkits
│   ├── README.md                          # Governance framework index
│   ├── rules/                             # 3 Consolidated governance rule files (Rules 1–13)
│   │   ├── README.md                      # Rules catalog & Zero-Trust runtime topology
│   │   ├── ai_sdlc_and_sdd_standards.md   # [always_on] 3-Phase AI-SDLC, SDD, WAF/SAIF Precedence & Rule 13 (4-Step RCA)
│   │   ├── google_adk_and_agent_runtime.md # [model_decision] Rules 11–12: Google ADK, SAIF 2.0 4-Pt Guardrails & Eval
│   │   └── devops_security_and_quality_standards.md # [model_decision] Rules 1–10: WAF DevSecOps, SAST, Cloud Run & IaC
│   └── skills/                            # Hub-and-Spoke operational agent skills (6 total)
│       ├── README.md                      # Skills catalog & operating guidelines
│       ├── ai_sdlc/                       # [MASTER HUB] 3-Phase AI-SDLC orchestrator wired to all rules & skills
│       │   ├── SKILL.md                   # Master workflow, Hub-and-Spoke wiring matrices & phase gates
│       │   ├── ai-sdlc-architecture.html  # Interactive Brownfield vs. Greenfield lifecycle SVG diagram
│       │   ├── scripts/                   # validate_sdlc_gate.py (--init scaffolder & workload-aware gate validator)
│       │   ├── references/                # Brownfield assessment playbook, questionnaires & rules integration matrix
│       │   └── examples/                  # Seed templates for specs/ & docs/ + sample end-to-end walkthrough
│       ├── requirements_discovery/        # [OPTIONAL PRE-INCEPTION] Multi-modal raw inputs -> 15-section Discovery Doc
│       │   ├── SKILL.md                   # 6-Stage multi-modal discovery, conflict & WAF quality attribute workflow
│       │   ├── scripts/                   # validate_discovery.py 15-section & 100% package traceability validator
│       │   └── references/                # Multi-modal locator guide & 1-to-1 Discovery -> SDD mapping
│       ├── gcp_well_architected_saif/     # [SUPREME PRECEDENCE] Google Cloud WAF (6 Pillars) & SAIF / SAIF 2.0
│       │   ├── SKILL.md                   # WAF + SAIF 2.0 architecture & conflict-resolution blueprint
│       │   ├── scripts/                   # validate_waf_saif.py workload-aware WAF/SAIF compliance scanner
│       │   └── references/                # 6 Pillars + AI/ML & FSI guide, SAIF 15-Risk catalog & compliance template
│       ├── architecture_diagram/          # Dark-themed technical/Zero-Trust architecture diagrams & HTML/SVG assets
│       ├── codemender/                    # Pre-build SAST discovery (cm find), PoC triage (verify) & patching (fix)
│       └── gcp_cost_estimator/            # Real-time GCP Billing API cost estimation (zero caching) & FinOps BoM
├── specs/                                 # [Scaffolded on ai-sdlc --init] Single Source of Truth for SDD
│   ├── README.md                          # Specifications index and SDD registry
│   ├── templates/                         # discovery-template.md [15 §§], sdd-template.md [10 §§], baseline-template.md [8 §§]
│   ├── discovery/                         # [Optional Pre-AI-SDLC] Consolidated multi-modal Discovery Documents
│   ├── baseline/                          # Brownfield baseline specifications ("as-is" architecture, logic & FMEA)
│   ├── features/                          # Feature & Solution Design SDDs (Regular App or AI Agent / Hybrid)
│   └── plan/                              # Living execution progress reports and RCA logs
└── docs/                                  # [Scaffolded on ai-sdlc --init] Operational reports, cost models & diagrams
    ├── README.md                          # Documentation index & naming conventions
    ├── waf-saif-review_*.md               # Google Cloud WAF 6-Pillar [& SAIF 2.0] compliance audit reports
    ├── *-architecture.{md,html}           # Architecture designs & standalone HTML/SVG visualizers
    ├── codemender-*.md                    # CodeMender SAST scan, verification, remediation & summary reports
    └── gcp_cost_estimate_*.md             # Live Google Cloud Billing API cost models & itemized BoMs
```

---

## 🗂️ Phase-by-Phase Output Folder Map (`ai-sdlc`)

| AI-SDLC Phase | Deliverable / Activity | Skill / Validator Invoked | Target Output Folder & Naming Pattern |
| :--- | :--- | :--- | :--- |
| **Phase 0: Activation** | Workspace Scaffolding | `ai-sdlc` (`validate_sdlc_gate.py --init`) | `specs/` & `docs/` seeded from `_agents/skills/ai_sdlc/examples/` |
| **Optional Pre-Phase 1** | Multi-Modal Stakeholder Input Consolidation | `requirements-discovery` (`validate_discovery.py`) | `specs/discovery/DISCOVERY-<YYYYMMDD>-<PROJECT>.md` *(15 Sections)* |
| **Phase 1: Inception** | Brownfield "As-Is" Discovery *(if brownfield)* | `ai-sdlc` + `codemender` (`cm find`) | `specs/baseline/system-overview.md` or `<subsystem>-baseline.md` *(Sections 1–8)* |
| **Phase 1: Inception** | Intent, Workload Mode & WAF[/SAIF] Framing | `ai-sdlc` + `gcp-well-architected-saif` | `specs/features/SPEC-<YYYYMMDD>-<FEATURE>.md` *(Doc Control + §§1–2)* & `docs/waf-saif-review_<project>.md` |
| **Phase 1: Inception** | Visual Architecture Diagram | `architecture-diagram` | `docs/<project>-architecture.md` & `docs/<project>-architecture.html` |
| **Phase 1: Inception** | Live Cloud Cost & FinOps BoM | `gcp-cost-estimator` | `docs/gcp_cost_estimate_<project>.md` |
| **Phase 2: Execution** | Full Solution Design SDD & Test Plan | `ai-sdlc` + `gcp-well-architected-saif` | `specs/features/SPEC-<YYYYMMDD>-<FEATURE>.md` *(Document Control + Sections 1–10)* |
| **Phase 2: Execution** | `[AI-Agent Only]` ADK Agents & Guardrails (`agent_runtime`) | `ai-sdlc` (Rules 11–12) | `app/` (`agent.py`, `tools/*.py`, `callbacks/*.py`, `agents-cli-manifest.yaml`) |
| **Phase 2: Execution** | Cloud Run UI, Backend APIs / Proxy & `/healthz` (`cloud_run`) | `ai-sdlc` (Rules 6, 8, 10) | `src/` (React/Vite UI) & `server/` (REST/SSE service + `/healthz`) |
| **Phase 2: Execution** | Unit Tests, Property-Based Tests (PBT) *(+ Agent Evals)* | `ai-sdlc` (Rules 11–13) | `tests/unit/`, `tests/property/` *(+ `evals/` if AI Agent/Hybrid)* |
| **Phase 2: Execution** | Living Plan Progress Report & WAF[/SAIF] Gate | `validate_sdlc_gate.py --phase execution` | `specs/plan/PROGRESS_REPORT_<YYYYMMDD>.md` & `specs/README.md` |
| **Phase 3: Operation** | Pre-Build CodeMender SAST Gate | `codemender` (`cm find/verify/fix`) | `docs/codemender-01-*.md` .. `03-*.md`, `docs/codemender-security-audit-summary.md` |
| **Phase 3: Operation** | CI/CD Pipeline, SLSA L3, IaC & Unified `.env` | `ai-sdlc` (Rules 1–10) | `cloudbuild.yaml`, `.env.example`, `terraform/*.tf` (VPC-SC + CMEK) |
| **Phase 3: Operation** | Post-Deploy `/healthz`, SLOs *(+ Live Agent Eval)* | `validate_sdlc_gate.py --phase operation` | Final telemetry update to `specs/plan/PROGRESS_REPORT_<YYYYMMDD>.md` |

---

## 🔄 3-Phase AI-SDLC & Spec-Driven Development (SDD) Workflow

Every task is orchestrated by [`_agents/skills/ai_sdlc/SKILL.md`](./_agents/skills/ai_sdlc/SKILL.md) through three gated phases (with an optional pre-Inception consolidation step when raw stakeholder packages exist):

```
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
| OPTIONAL PRE-PHASE 1: MULTI-MODAL DISCOVERY (requirements-discovery)          |
|  - Consolidate interview scripts, drawings, emails & manuals into 15 sections |
|  - Output: specs/discovery/DISCOVERY-*.md (validate_discovery.py)             |
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
                                        ┆ (Optional Input — OR Direct ask_question)
                                        ▼
+---------------------------------------------------------------------------------+
| PHASE 1: INCEPTION (Intent Framing, WAF 6-Pillar & SAIF 2.0 Architecture)       |
|  - Scaffold specs/ & docs/ in root (validate_sdlc_gate.py --init)               |
|  - Ingest Discovery Doc + repo context; resolve gaps/blockers via ask_question  |
|  - Assess brownfield vs. greenfield scope (specs/baseline/ vs. Manual Drift)    |
|  - Frame Runtime mode (Regular App vs. Dual-Runtime AI Agent) & Zero-Trust IAM  |
|  - Orchestrate: gcp-well-architected-saif, architecture-diagram, cost-estimator |
+---------------------------------------------------------------------------------+
                                        │
                         [Gate 1: ask_question Sign-Off]
                                        ▼
+---------------------------------------------------------------------------------+
| PHASE 2: EXECUTION (The Spec-Driven Development Cycle — SDD Steps 2.0 to 2.5)   |
|  - SDD Step 2.0: Brownfield Baseline + Characterization & PBT Safety Net        |
|  - SDD Step 2.1: Author 10-Section Feature SDD (Zero Placeholders Allowed)      |
|  - SDD Step 2.2: Granular Step-by-Step Plan + Unit + PBT [+ DLP-Safe Live Eval] |
|  - SDD Step 2.3: Pre-Code Stakeholder Alignment Sub-Gate (ask_question Sign-Off)|
|  - SDD Step 2.4: Step-by-Step Build & Test (Rule 13 4-Step RCA on any failure)  |
|  - SDD Step 2.5: Chained WAF[/SAIF] Gate, Spec Sync & Living Plan (specs/plan/) |
+---------------------------------------------------------------------------------+
                                        │
                         [Gate 2: ask_question Sign-Off]
                                        ▼
+---------------------------------------------------------------------------------+
| PHASE 3: OPERATION (Repository Integration, SAST & Cloud / Agent Deployment)    |
|  - Pre-Merge Gate: Static Analysis + CodeMender SAST + SLSA L3 + Unified .env   |
|  - Git Multi-Branch Integration (main/develop -> reviewed PR to prod)           |
|  - Deploy (VPC-SC + CMEK): Cloud Build & Terraform [+ agents-cli if AI Agent]   |
|  - Post-Deploy Gate: Live /healthz + SLO alerts [+ DLP-safe agents-cli eval]    |
+---------------------------------------------------------------------------------+
```

### Mandatory Testing & Quality Gates at Every Step
- **Deterministic Unit Tests (Universal):** Boundary conditions, malformed payloads, auth rejection, and error handling (`pytest` / `vitest`).
- **Generative Property-Based Tests (PBT — Universal):** Mathematical and structural invariants verified across randomized inputs (`hypothesis` / `fast-check`).
- **`[AI-Agent Only]` DLP-Safe Live Agent Evaluation:** Executed against isolated, de-identified Non-Prod backends via `agents-cli eval run` ($\ge 95\%$ tool selection precision, $1.000$ groundedness, $100\%$ 4-point SAIF adversarial block rate).
- **Mandatory 4-Step RCA Protocol (Rule 13 — Universal):** Zero synthetic mockup fallbacks or regex patches; deep root cause diagnosis + $\ge 2$ sustainable architectural options approved via `ask_question` (harmonized with WAF Graceful Degradation `503 UPSTREAM_UNAVAILABLE_DEGRADED`).

---

## 🛠️ Integrated Skills & Capabilities (Master Hub + 5 Companion Skills)

1. **[`ai-sdlc`](./_agents/skills/ai_sdlc/SKILL.md) *(Main / Master Hub Skill)*:** Orchestrates Phase 1 (Inception), Phase 2 (SDD Execution), and Phase 3 (Operation), wires all 3 governance rules (Rules 1–13) and all 5 companion skills, scaffolds `specs/` & `docs/` (`--init`), supports **Dual-Input ingestion** (`specs/discovery/DISCOVERY-*.md` + `ask_question`), enforces zero-placeholder SDD completion, and validates gates via `validate_sdlc_gate.py`.
2. **[`requirements-discovery`](./_agents/skills/requirements_discovery/SKILL.md) *(Optional Pre-Inception Discovery Spoke)*:** Consolidates multi-modal raw stakeholder inputs (interview scripts, whiteboard/architecture drawings, user emails, manuals/PDFs, spreadsheets) into a citation-grounded **15-Section Discovery Document** (`specs/discovery/DISCOVERY-*.md`), flagging stakeholder tensions, cross-artifact/brownfield-code contradictions, WAF 6-Pillar quality attribute gaps, and the Phase 1 cut line (`validate_discovery.py`).
3. **[`gcp-well-architected-saif`](./_agents/skills/gcp_well_architected_saif/SKILL.md) *(Supreme Precedence Architecture & AI Security Skill)*:** Enforces the Google Cloud Well-Architected Framework (6 Core Principles, 6 Core Pillars including Sustainability `CFE %`, plus AI/ML & FSI Perspectives) and Google Secure AI Framework (SAIF 6 Elements, 15 Risks `DP`–`RAC`, and SAIF 2.0 4-Point Autonomous Agent Guardrails), backed by workload-aware `validate_waf_saif.py`.
4. **[`architecture-diagram`](./_agents/skills/architecture_diagram/SKILL.md):** Generates dark-themed technical system and Zero-Trust cloud diagrams (`docs/*-architecture.md`) paired with standalone interactive SVG/HTML visualizers (`docs/*-architecture.html`).
5. **[`codemender`](./_agents/skills/codemender/SKILL.md):** Orchestrates 3-stage pre-build SAST workflows—vulnerability discovery (`cm find`), sandbox PoC exploit verification (`cm verify`), and automated remediation (`cm fix`)—mapped to OWASP/CWE and SAIF Risk IDs (`docs/codemender-*.md`).
6. **[`gcp-cost-estimator`](./_agents/skills/gcp_cost_estimator/SKILL.md):** Performs zero-assumption Google Cloud running cost estimation querying real-time unit rates strictly from the live Google Cloud Billing API or official live pricing pages (zero local price caching), complete with WAF Pillar 4 FinOps unit economics, Pillar 6 `CFE %`, and CUD/Provisioned Throughput optimization (`docs/gcp_cost_estimate_*.md`).

---

## 📖 Key References
- **Executive Governance Router:** [`AGENTS.md`](./AGENTS.md)
- **Framework Overview:** [`_agents/README.md`](./_agents/README.md)
- **Master AI-SDLC Hub Skill:** [`_agents/skills/ai_sdlc/SKILL.md`](./_agents/skills/ai_sdlc/SKILL.md)
- **Optional Requirements Discovery Skill:** [`_agents/skills/requirements_discovery/SKILL.md`](./_agents/skills/requirements_discovery/SKILL.md)
- **WAF & SAIF 2.0 Skill:** [`_agents/skills/gcp_well_architected_saif/SKILL.md`](./_agents/skills/gcp_well_architected_saif/SKILL.md)
- **Rules Catalog (Rules 1–13):** [`_agents/rules/README.md`](./_agents/rules/README.md)
- **Skills Catalog (6 Skills):** [`_agents/skills/README.md`](./_agents/skills/README.md)
- **SDD & Rules Integration Matrix:** [`_agents/skills/ai_sdlc/references/sdd_and_rules_integration_matrix.md`](./_agents/skills/ai_sdlc/references/sdd_and_rules_integration_matrix.md)
- **Consolidated Discovery Template (15 §§):** [`_agents/skills/ai_sdlc/examples/specs/templates/discovery-template.md`](./_agents/skills/ai_sdlc/examples/specs/templates/discovery-template.md)
- **Master Feature SDD Template (10 §§):** [`_agents/skills/ai_sdlc/examples/specs/templates/sdd-template.md`](./_agents/skills/ai_sdlc/examples/specs/templates/sdd-template.md)
- **Brownfield Baseline Template (8 §§):** [`_agents/skills/ai_sdlc/examples/specs/templates/baseline-template.md`](./_agents/skills/ai_sdlc/examples/specs/templates/baseline-template.md)


