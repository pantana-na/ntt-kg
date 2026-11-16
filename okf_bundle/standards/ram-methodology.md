---
type: Engineering Standard
title: Risk Assessment Matrix (RAM) and Risk Assessment Code (RAC) Standard
description: Qualitative risk evaluation standard consolidating severity, probability,
  and exposure into 4-tier Risk Assessment Codes (RAC 1 to 4) with mandatory mitigation
  action protocols.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/standards/ram-methodology.md
tags:
- hazop
- process-safety
- rac
- ram
- risk-assessment
- safety-standard
- standards
sources:
- id: src-1
  resource: reference/raw/standards/Risk_Assessment_Matrix.pdf
  title: Risk_Assessment_Matrix.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:07:59Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:07:59Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:07:59Z'
status: stable
entity_metadata:
  document_class: standards
  rac_levels:
  - 1
  - 2
  - 3
  - 4
  severity_levels:
  - I
  - II
  - III
  - IV
  matrix_dimensions: 4x5
  probability_levels:
  - A
  - B
  - C
  - D
  - E
  standard_code: RAM
---

> ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
> Risk Assessment Codes (RAC) quantify qualitative mishap potential to prioritize immediate corrective interventions. Any activity or condition evaluated as **RAC 1 (Extremely High)** requires a mandatory **"Stop, Immediate Correction"** order. Any condition evaluated as **RAC 2 (High)** requires **"Consider Stopping, Urgent Correction"**. Risk assessments must not trade off critical safety limits against operational convenience using over-optimistic or biased scoring. If qualitative risk exposure is determined to be extreme or complex, formal quantitative risk assessment (QRA) tools must be deployed.

# Risk Assessment Matrix (RAM) Technical Standard

## Overview and Purpose
The **Risk Assessment Matrix (RAM)** standard establishes a qualitative evaluation methodology to determine the risk level that operational and process hazards pose. It governs whether an activity or mission should proceed and defines mandatory mitigation requirements.

To assess risk, the method evaluates three core hazard attributes:
1. **Severity ($S$)**: Potential consequences if a mishap occurs (e.g., personnel injury, asset loss, mission failure).
2. **Probability ($P$)**: Likelihood that the hazard will result in a mishap (ranging from rare to almost certain).
3. **Exposure ($E$)**: Frequency and duration of contact, or number of personnel exposed to the hazard.

The RAM consolidates the exposure characteristic directly into the probability evaluation. As personnel exposure or frequency of contact increases, the probability of a mishap correspondingly increases. While not mathematically rigorous, this consolidation provides an efficient, standardized qualitative assessment.

---

## Severity Categories ($S$)

Severity is evaluated along four standardized qualitative tiers based on the worst credible outcome:

| Severity Level | Category | Consequence & Impact Definition |
| :---: | :--- | :--- |
| **I** | **Catastrophic** | Death, total loss of asset, loss of mission capability, or complete loss of unit readiness. |
| **II** | **Critical** | Permanent disabling injury or severe damage, significantly degraded mission capability, or significantly degraded unit readiness. |
| **III** | **Moderate** | Non-permanent disabling injury or moderate damage, degraded mission capability, or degraded unit readiness. |
| **IV** | **Negligible** | Minimal injury or damage, little or no impact to mission capability or unit readiness. |

---

## Probability Categories ($P$)

Probability defines the likelihood that a hazard will materialize into a mishap under active exposure:

| Probability Level | Category | Likelihood & Experience Criteria |
| :---: | :--- | :--- |
| **A** | **Almost Certain** | Continuously experienced; extremely high likelihood of occurrence. |
| **B** | **Likely** | Will occur frequently during operations or system lifespan. |
| **C** | **Possible** | Will occur several times; realistic operational potential. |
| **D** | **Unlikely** | Remotely possible but not probable; exceptional circumstances required. |
| **E** | **Rare** | Improbable; has occurred in historical industry/fleet records but rare. |

---

## 4×5 Risk Assessment Matrix Grid

The combination of Severity (Rows I–IV) and Probability (Columns A–E) yields a specific numerical **Risk Assessment Code (RAC)** from 1 to 4:

| Severity Level | Severity Category | Probability A (Almost Certain) | Probability B (Likely) | Probability C (Possible) | Probability D (Unlikely) | Probability E (Rare) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **I** | **Catastrophic** | **1** | **1** | **1** | **2** | **3** |
| **II** | **Critical** | **1** | **1** | **2** | **3** | **3** |
| **III** | **Moderate** | **2** | **2** | **3** | **4** | **4** |
| **IV** | **Negligible** | **3** | **3** | **4** | **4** | **4** |

---

## Risk Assessment Codes (RAC) and Action Protocols

Each RAC level corresponds to a risk tier, color coding, and mandatory procedural action:

| RAC Value | Risk Category | Visual Indicator / Color | Action Required | Escalation & Response Protocol |
| :---: | :--- | :---: | :--- | :--- |
| **1** | **Extremely High** | Red | **Stop, Immediate Correction** | Halt all operations immediately. Implement mandatory physical or procedural controls before resuming. Requires command-level escalation. |
| **2** | **High** | Orange | **Consider Stopping, Urgent Correction** | Evaluate operational stoppage. Expedite urgent mitigation controls. Escalated supervisory review required. |
| **3** | **Moderate** | Yellow | **Corrective Attention Needed** | Proceed with caution under active monitoring. Plan and implement corrective actions during normal workflow. |
| **4** | **Low** | Green | **Possible Acceptance** | Residual risk is acceptable without immediate intervention. Monitor within routine operational discipline. |

---

## Methodological Guidelines, Limitations, and Cognitive Biases

Risk quantification through qualitative scoring requires disciplined oversight to prevent distorted results. The standard highlights several governance requirements and human factor limitations:

### Governance Principles
1. **Command Escalation Thresholds**: Each operational unit must establish specific escalation thresholds governing when risk acceptance decisions must be elevated to higher management.
2. **Avoid Oversimplification**: Numerical scores can mask nuanced operational hazards or dynamic human interactions.
3. **Guard Against False Trade-offs**: Risk cannot be unrealistically traded off against operational convenience or productivity targets solely by manipulating matrix scores.

### Cognitive Biases and Pitfalls to Avoid
* **Over-optimism**: Failing to acknowledge root causes or assuming favorable outcomes without objective evidence.
* **Misrepresentation**: Distorting risk data based on personal bias or isolated experiences.
* **Alarmism**: Projecting worst-case outcomes without evaluating credible probability ("the sky is falling" mindset).
* **Prejudice**: Advancing subjective operational agendas rather than relying on verifiable facts.
* **Indiscrimination**: Assigning equal weight to all data points regardless of credibility or relevance.
* **Inaccuracy**: Utilizing incomplete, outdated, or misunderstood technical data.

---

## Hazard Assessment and Mitigation Workflow

The risk mitigation protocol follows a structured step-by-step procedure captured on the **Hazard Assessment and Mitigation Worksheet**:

1. **Hazard Identification**: Define the operational task, then ask: *"What can go wrong?"* and *"Why?"*
2. **Initial Risk Assignment**: Determine baseline Severity ($S_{init}$) and Probability ($P_{init}$), then intersect them on the RAM to determine initial $RAC_{init}$.
3. **Mitigation Development**: Identify specific engineering, administrative, or operational safeguards.
4. **Residual Risk Calculation**:
   - Assess if the control reduces consequence Severity (engineering controls rarely reduce intrinsic consequence severity, except physical containment/arrestors).
   - Assess if the control reduces mishap Probability (most operational controls reduce likelihood of occurrence).
   - Determine residual Severity ($S_{res}$) and residual Probability ($P_{res}$) to establish the residual $RAC_{res}$.
5. **Implementation & Verification**: If $RAC_{res} \le 4$ (or unit-accepted tolerance), approve operation under specified controls.

### Case Study Example: Marine Towing Operation (47MLB Platform)
* **Task**: Towing sailboat
* **Mishap Event**: Tow line fouling in vessel screws (propellers)

| Hazard Identified ("Why?") | Initial S | Initial P | Initial RAC | Identified Mitigations | Post-Mitigation S | Post-Mitigation P | Residual RAC |
| :--- | :---: | :---: | :---: | :--- | :---: | :---: | :---: |
| **Too much slack in line** | III | C | 3 (Moderate) | Monitor line tension; Maintain speed and heading | III | D | **4 (Low)** |
| **Displacement of MLB stern** | III | C | 3 (Moderate) | Limit tows to less than defined sea states; Monitor line orientation | III | D | **3 (Moderate)** |
| **Line parted or snapped** | III | D | 4 (Low) | Inspect line for wear and deterioration | III | D | **4 (Low)** |

---

## References and Governing Sources
* `reference/raw/standards/Risk_Assessment_Matrix.pdf` [^src-1]

[^src-1]: Technical Standard Document: Risk Assessment Matrix (RAM), Pages 1–5.
