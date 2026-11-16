---
type: Standard Operating Procedure
title: Hazard Assessment and Mitigation Workflow Procedure
description: Step-by-step procedural workflow for conducting hazard assessments, scoring
  Risk Assessment Codes (RAC), and completing mitigation worksheets using the RAM
  framework.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/procedures/hazard-assessment-and-mitigation.md
tags:
- hazard-assessment
- mitigation
- procedures
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
  at: '2026-10-02T13:08:22Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:08:22Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:08:22Z'
status: stable
entity_metadata:
  procedure_type: Risk Assessment and Hazard Mitigation
  document_class: standards
  governing_standard: RAM
---

> ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
> Mandatory Stop-Work Authority applies whenever an operational hazard evaluates to **RAC 1 (Extremely High)** ("Stop, Immediate Correction"). No personnel may proceed with the task until verified physical or procedural barriers downgrade the residual risk code to acceptable thresholds (RAC 3 or 4, subject to unit command authorization). Controls that only mitigate likelihood (Probability) must not be assumed to eliminate severe consequence severity.

# Procedure: Hazard Assessment and Mitigation Workflow

## Purpose and Scope
This procedure defines the operational execution steps for conducting qualitative hazard evaluations using the **Risk Assessment Matrix (RAM)** and recording controls on the **Hazard Assessment and Mitigation Worksheet**. It applies to all plant activities, maintenance interventions, and operational maneuvers.

---

## Procedural Workflow Steps

### Step 1: Task Framing and Hazard Decomposition
1. Define the specific operational task or mission to be performed.
2. Formulate the primary failure question: *"What can go wrong?"* (Identify potential loss-of-containment, personal injury, or asset fouling events).
3. Decompose root causal factors by asking: *"Why?"* (Identify initiating conditions, operational upsets, or environmental factors).

### Step 2: Baseline Risk Ranking
1. **Assign Consequence Severity ($S$)**:
   - Evaluate the worst credible consequence if the mishap occurs.
   - Categorize as **I (Catastrophic)**, **II (Critical)**, **III (Moderate)**, or **IV (Negligible)**.
2. **Assign Mishap Probability ($P$)**:
   - Assess likelihood under current exposure conditions (accounting for personnel density and task frequency).
   - Categorize as **A (Almost Certain)**, **B (Likely)**, **C (Possible)**, **D (Unlikely)**, or **E (Rare)**.
3. **Determine Initial Risk Assessment Code ($RAC_{init}$)**:
   - Intersect the Severity row and Probability column on the standard 4×5 RAM.
   - Record initial RAC ($1$, $2$, $3$, or $4$).

### Step 3: Safeguard Identification and Mitigation Analysis
1. Propose practical engineering, physical, or administrative risk-reduction measures.
2. Evaluate individual and combined mitigation effectiveness:
   - **Severity Reduction Test**: Determine whether the safeguard reduces the consequence magnitude if the mishap occurs (e.g., impact attenuation, passive relief, secondary containment). *Note: Most operational mitigations do not reduce intrinsic severity.*
   - **Probability Reduction Test**: Determine whether the safeguard decreases the likelihood or frequency of initiation (e.g., speed control, interlocks, continuous tension monitoring).
3. Calculate residual Severity ($S_{res}$) and residual Probability ($P_{res}$).
4. Intersect $S_{res}$ and $P_{res}$ to determine residual Risk Assessment Code ($RAC_{res}$).

### Step 4: Decision-Making and Escalation Protocol
* **If $RAC_{res} = 1$ (Extremely High)**: **STOP**. Operation prohibited. Immediate physical/procedural redesign required. Command escalation mandatory.
* **If $RAC_{res} = 2$ (High)**: **CONSIDER STOPPING**. Urgent mitigation mandatory before proceeding. Requires supervisory escalation and sign-off.
* **If $RAC_{res} = 3$ (Moderate)**: **CORRECTIVE ATTENTION NEEDED**. Implement planned safeguards. Operational monitoring required.
* **If $RAC_{res} = 4$ (Low)**: **ACCEPTABLE**. Proceed with standard operating discipline.

---

## Standardized Hazard Assessment and Mitigation Worksheet

The structured worksheet below captures the assessment and mitigation results:

| Task / Mission | Identified Failure Mode ("What can go wrong?") | Root Cause Hazard ("Why?") | Baseline S | Baseline P | Baseline RAC | Proposed Mitigations | Residual S | Residual P | Residual RAC |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- | :---: | :---: | :---: |
| **Marine Tow Operation (47MLB)** | Tow line fouling in screws / propellers | **Too much slack in line** | **III** | **C** | **3** | Monitor line tension; Maintain speed and heading | III | D | **4** |
| **Marine Tow Operation (47MLB)** | Tow line fouling in screws / propellers | **Displacement of MLB stern** | **III** | **C** | **3** | Limit tows to less than specified sea conditions; Monitor line orientation | III | D | **3** |
| **Marine Tow Operation (47MLB)** | Tow line fouling in screws / propellers | **Line parted or snapped** | **III** | **D** | **4** | Inspect tow line for physical wear, chafing, and deterioration prior to deployment | III | D | **4** |

---

## Operational Cautions Against Scoring Biases
Assessors must maintain rigorous objectivity and avoid common cognitive pitfalls:
1. **Over-optimism**: Unjustifiably assuming ideal operational performance or ignoring latent failure modes.
2. **Misrepresentation**: Skewing risk variables to achieve a predetermined low-risk score.
3. **Alarmism**: Inflating consequence ratings beyond credible worst-case scenarios without evaluating probability.
4. **Prejudice**: Disregarding empirical operating data in favor of subjective preferences.
5. **Indiscrimination**: Treating minor procedural lapses with equal weighting as severe physical containment failures.
6. **Inaccuracy**: Operating with incomplete, unverified, or outdated technical parameters.

---

## References
* `reference/raw/standards/Risk_Assessment_Matrix.pdf` [^src-1]

[^src-1]: Source Document: Risk Assessment Matrix (RAM), Pages 1–5.
