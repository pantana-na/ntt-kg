---
type: Engineering Standard
title: Hazard and Operability Analysis (HAZOP) Methodology Standard
description: Standard technical specification, principles, governing standards (IEC
  61882, ICH Q9), scoping perspectives, advantages, and limitations of Hazard and
  Operability (HAZOP) studies.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/standards/hazop-methodology.md
tags:
- hazop
- ich-q9
- iec-61882
- process-safety
- risk-assessment
- standards
sources:
- id: src-1
  resource: reference/raw/standards/HAZOP_Training_Guide.pdf
  title: HAZOP_Training_Guide.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:11:26Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:11:26Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:11:26Z'
status: stable
entity_metadata:
  application_perspectives:
  - Design
  - Physical and Operational Environments
  - Operational and Procedural Controls
  governing_standards:
  - IEC 61882
  - ICH Q9
  - HACCP
  operational_modes:
  - Start-up
  - Standby
  - Normal operation
  - Steady and unsteady states
  - Normal shutdown
  - Emergency shutdown
  methodology_type: Inductive Qualitative Risk Assessment
---

> ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
> HAZOP is an inductive qualitative technique that assumes deviations from design or operational intent cause risk events. However, HAZOP possesses three critical intrinsic limitations: (1) it provides no inherent mechanism to assess hazards arising from complex cross-system interactions between different processing units; (2) it has no native risk ranking or severity/probability scoring mechanism (requiring integration with a Risk Assessment Matrix / RAM); and (3) it cannot evaluate the quantitative reliability or effectiveness of proposed/existing safeguards (requiring coupling with HACCP, LOPA, or SIL verification). Always verify safeguards independently before commissioning.

# Hazard and Operability Analysis (HAZOP) Methodology Standard

## 1. Overview and Core Principles
Hazard and Operability Analysis (HAZOP) is a structured, systematic, and inductive qualitative risk assessment technique designed to examine systems, identify potential hazards, and uncover operability problems likely to compromise personnel safety, facility integrity, environmental compliance, or product quality [^src-1].

The foundational theory of HAZOP postulates that **risk events are caused by deviations from design or operating intentions** [^src-1]. Identification of deviations is systematically driven by pairing process parameters or operational activities with standardized **guide words** that stimulate the technical imagination of subject matter experts (SMEs) [^src-1].

### 1.1 Classification within Quality Risk Management
HAZOP is classified under international risk frameworks (including **ICH Q9** and **IEC 61882**) as:
* **A Brainstorming Technique**: Promotes open, cross-functional exploration of unexpected failure modes [^src-1].
* **A Qualitative Risk Assessment Tool**: Operates without requiring rigid probabilistic failure rate modeling [^src-1].
* **An Inductive ("Bottom-Up") Tool**: Systematically builds risk scenarios starting from low-level operational deviations up to macro-level process consequences, relying on SME experience and intuition [^src-1].

---

## 2. Terminology and Formal Definitions

| Term | Standard Definition (per IEC 61882 / PQRI) |
| :--- | :--- |
| **SYSTEM** | The subject of a risk assessment; generally encompasses a process, product, activity, facility, or logical control system [^src-1]. |
| **Hazard** | A potential source of harm. Deviations from design or operational intent constitute or produce a hazard. A single hazard can lead to multiple distinct forms of harm [^src-1]. |
| **Harm** | Physical injury or damage to the health of people, or damage to property or the environment. Harm represents the ultimate consequence of a hazard and spans patient/user safety, employee safety, business interruption, and regulatory or environmental liability [^src-1]. |
| **Risk** | The combination of the probability of occurrence of harm and the severity of that harm. Core HAZOP does not mandate explicit probability or severity rating, but assessment teams may optionally integrate risk matrices to prioritize mitigations [^src-1]. |

---

## 3. Scoping Perspectives and Operational Modes
HAZOP is optimal for assessing equipment, facilities, utilities, and continuous or batch processes across three primary perspectives [^src-1]:

### 3.1 Design Perspective
* Evaluates system design capability against user requirements, engineering specifications, and safety codes [^src-1].
* Identifies systemic engineering vulnerabilities, sizing deficiencies, and layout bottlenecks [^src-1].

### 3.2 Physical and Operational Environments
* Verifies that physical equipment is properly situated, structurally supported, serviced by utilities, contained, ventilated, and accessible for maintenance [^src-1].

### 3.3 Operational and Procedural Controls
* Assesses engineered controls (distributed control systems [DCS], programmable logic controllers [PLC], interlocks, alarms) and manual human operating procedures [^src-1].
* Scrutinizes all lifecycle operating regimes, including:
  1. Initial Commissioning and Start-up
  2. Standby / Recirculation
  3. Normal Steady-State Operation
  4. Transient and Unsteady-State Dynamics
  5. Normal Controlled Shutdown
  6. Emergency Shutdown (ESD) and Rapid Depressurization [^src-1].

---

## 4. Methodological Strengths and Critical Limitations

| Advantages (+) | Disadvantages and Limitations (-) | Compensating Engineering Practices |
| :--- | :--- | :--- |
| **Confronts Unquantifiable Hazards**: Effectively isolates risks rooted in human behavior, execution errors, and complex transient states where statistical failure rates are unavailable [^src-1]. | **No Cross-System Interaction Analysis**: Ineffective at evaluating complex domino effects or multi-node inter-system dependencies [^src-1]. | Interface with Fault Tree Analysis (FTA) or Global Process Safety Reviews [^src-1]. |
| **Built-In Brainstorming Engine**: Standardized guide words break cognitive bias and groupthink during review sessions [^src-1]. | **No Native Risk Ranking / Prioritization**: Standard HAZOP does not rank deviations by severity or frequency [^src-1]. | Couple HAZOP findings directly with a **Risk Assessment Matrix (RAM)** to calculate Risk Assessment Codes (RAC 1–4) [^src-1]. |
| **Systematic and Comprehensive**: Exhaustive element-by-element interrogation ensures no process line or step is omitted [^src-1]. | **Cannot Quantify Safeguard Reliability**: Does not determine whether existing protections (check valves, alarms, vents) provide sufficient risk reduction [^src-1]. | Integrate with **HACCP**, **Layer of Protection Analysis (LOPA)**, or Safety Integrity Level (SIL) allocation [^src-1]. |
| **Intuitive and Accessible**: Simpler to deploy across cross-functional plant teams than complex quantitative models [^src-1]. | **Resource Intensive**: Dependent on high SME time commitments and active session facilitation [^src-1]. | Strict scoping, preparation, and node boundary definition prior to sessions [^src-1]. |

---

## 5. References
* `reference/raw/standards/HAZOP_Training_Guide.pdf` [^src-1]
* IEC International Standard 61882: *Hazard and operability studies (HAZOP studies) - Application guide* [^src-1]
* ICH Q9 Guideline: *Quality Risk Management* [^src-1]

[^src-1]: PQRI Manufacturing Technology Committee, *Risk Management Training Guides: Hazard & Operability Analysis (HAZOP)*, pp. 1–3.
