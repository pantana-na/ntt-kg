---
type: Source Document
title: Risk Assessment Matrix (RAM) Technical Standard Document
description: Standard technical documentation for qualitative Risk Assessment Matrix
  (RAM), Risk Assessment Codes (RAC), and hazard mitigation protocols.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/sources/risk-assessment-matrix.md
tags:
- hazard-mitigation
- process-safety
- rac
- ram
- risk-assessment
- standards
sources:
- id: src-1
  resource: reference/raw/standards/Risk_Assessment_Matrix.pdf
  title: Risk_Assessment_Matrix.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:08:09Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:08:09Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:08:09Z'
status: stable
entity_metadata:
  subfolder: standards
  document_class: standards
  page_count: 5
  file_name: Risk_Assessment_Matrix.pdf
---

# Source Document: Risk Assessment Matrix (RAM)

## Document Overview
The **Risk Assessment Matrix (RAM)** document is an engineering technical standard establishing a standardized qualitative methodology for evaluating operational and process hazards. The framework consolidates hazard **Severity**, **Probability**, and personnel/activity **Exposure** to calculate a discrete **Risk Assessment Code (RAC)** ranging from 1 (Extremely High) to 4 (Low). It specifies mandatory mitigation responses and escalation thresholds for each RAC level.

## Document Metadata
* **Document Title**: Risk Assessment Matrix (RAM)
* **File Name**: `Risk_Assessment_Matrix.pdf`
* **Storage Location**: `reference/raw/standards/Risk_Assessment_Matrix.pdf`
* **Page Count**: 5 pages
* **Document Class**: Operational Risk Standard / Engineering Safety Procedure
* **Primary Scope**: Hazard Evaluation, Risk Assessment Codes (RAC), Mitigation Governance, and Assessment Worksheet Protocol

## Document Structure & Content Summary

### Page 1: Methodological Foundation & Matrix Axes
* **Core Characteristics**: Severity (consequence magnitude), Probability (likelihood of mishap), and Exposure (personnel count/frequency).
* **Consolidation**: Exposure is integrated into the probability evaluation axis.
* **Probability Scale (Columns A–E)**: A (Almost Certain), B (Likely), C (Possible), D (Unlikely), E (Rare).
* **Severity Scale (Rows I–IV)**: I (Catastrophic), II (Critical), III (Moderate), IV (Negligible).
* **Qualitative Example**: Spilled oil on a shop floor (Critical severity + Likely probability = RAC 1 / Extremely High).

### Page 2: Matrix Grid & Risk Assessment Codes (RAC)
* **Figure 1**: Standard 4×5 RAM Grid.
* **Risk Assessment Codes (RAC)**:
  * **RAC 1 (Extremely High)**: Red — *Action Required: Stop, Immediate Correction*.
  * **RAC 2 (High)**: Orange — *Action Required: Consider Stopping, Urgent Correction*.
  * **RAC 3 (Moderate)**: Yellow — *Action Required: Corrective Attention Needed*.
  * **RAC 4 (Low)**: Green — *Action Required: Possible Acceptance*.
* **Risk Prioritization Principles**: Enables ranking hazards by risk exposure and evaluating effectiveness of controls.

### Page 3: Quantification Cautions & Human Factor Biases
* **Administrative Governance**: Operational units dictate specific command-level escalation thresholds.
* **Limitations of Quantification**: Difficult to numerically model human behavior; danger of trading off safety margins against operational convenience.
* **Subjective Misrepresentations**: Over-optimism, misrepresentation, alarmism, prejudice, indiscrimination, inaccuracy.

### Pages 4–5: Mitigation Workflow & Case Study Worksheet
* **Worksheet Methodology**: Two-step query (*"What can go wrong?"* and *"Why?"*).
* **Mitigation Calculation**: Separately evaluating whether proposed safeguards reduce consequence Severity ($S$) or mishap Probability ($P$).
* **Case Study (47MLB Marine Towing Operation)**:
  * Baseline hazard: Too much slack in tow line ($S=\text{III}, P=\text{C}, RAC=3$).
  * Mitigation: Monitoring line tension reduces probability to $P=\text{D}$, achieving residual $RAC=4$.

## Extracted OKF Concepts
* **Engineering Standard**: [standards/ram-methodology](/standards/ram-methodology.md)
* **HAZOP / PHA Protocol**: [hazop/risk-assessment-matrix](/hazop/risk-assessment-matrix.md)
* **Operating Procedure**: [procedures/hazard-assessment-and-mitigation](/procedures/hazard-assessment-and-mitigation.md)

## Governing References
* `reference/raw/standards/Risk_Assessment_Matrix.pdf` [^src-1]

[^src-1]: Source Document: Risk Assessment Matrix (RAM), Pages 1–5.
