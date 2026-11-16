---
type: Risk Assessment Protocol
title: Qualitative Risk Assessment Matrix (RAM) for HAZOP and PHA
description: Application of qualitative Risk Assessment Matrix (RAM) and Risk Assessment
  Codes (RAC 1-4) to HAZOP, PHA, and process safety hazard mitigation.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/hazop/risk-assessment-matrix.md
tags:
- hazop
- pha
- process-safety
- rac
- ram
- risk-assessment
sources:
- id: src-1
  resource: reference/raw/standards/Risk_Assessment_Matrix.pdf
  title: Risk_Assessment_Matrix.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:07:36Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:07:36Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:07:36Z'
status: stable
entity_metadata:
  rac_scale:
  - 1
  - 2
  - 3
  - 4
  framework: RAM
---

> ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
> All HAZOP action items and hazard scenarios must be prioritized in accordance with the Risk Assessment Matrix (RAM). Any node deviation or consequence yielding a **Risk Assessment Code of RAC 1 (Extremely High)** requires an immediate shutdown or suspension of affected operations until independent physical protection layers are installed. RAC 2 requires urgent corrective safeguards.

# Qualitative Risk Assessment Matrix (RAM) Methodology for HAZOP and Process Safety

## Application to Process Hazard Analysis (PHA/HAZOP)
In chemical process facilities, PHA and HAZOP teams apply the **Risk Assessment Matrix (RAM)** to score qualitative risk ranking for identified deviation scenarios (e.g., High Pressure, High Temperature, Loss of Cooling, Reverse Flow).

### Severity Classification in Process Facilities
* **Severity I (Catastrophic)**: Fatalities, total loss of major processing unit/asset, large-scale toxic atmospheric release, extensive off-site environmental devastation.
* **Severity II (Critical)**: Permanent severe personnel injury, extensive equipment damage requiring long outage, significant toxic release within site boundaries.
* **Severity III (Moderate)**: Lost-time injuries (non-permanent), localized equipment damage, minor contained process release without off-site impact.
* **Severity IV (Negligible)**: First-aid injuries, negligible asset impact, transient process upset without containment breach.

### Probability Classification (Exposure-Adjusted)
* **A (Almost Certain)**: Continuous occurrence or multiple times per operational campaign.
* **B (Likely)**: Frequent occurrence over facility operational lifetime (annual frequency).
* **C (Possible)**: Expected to occur several times across facility design life (~10-25 years).
* **D (Unlikely)**: Low probability; remote but credible failure mode.
* **E (Rare)**: Highly improbable; historical industry precedent exists but exceptionally rare.

### Risk Ranking and Action Priorities

| Initial RAC | Risk Category | Color | Action Protocol in HAZOP / PHA |
| :---: | :--- | :---: | :--- |
| **1** | **Extremely High** | Red | **Stop, Immediate Correction**: Operation cannot proceed; mandatory redundant Safety Instrumented Function (SIF / SIL) or passive relief required. |
| **2** | **High** | Orange | **Consider Stopping, Urgent Correction**: High-priority engineering action required prior to startup/commissioning. |
| **3** | **Moderate** | Yellow | **Corrective Attention Needed**: Standard operational or maintenance safeguards to be implemented. |
| **4** | **Low** | Green | **Possible Acceptance**: Risk broadly acceptable within ALARP / operational discipline criteria. |

---

## References
* `reference/raw/standards/Risk_Assessment_Matrix.pdf` [^src-1]

[^src-1]: Technical Standard Document: Risk Assessment Matrix (RAM), Pages 1–5.
