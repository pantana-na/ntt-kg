---
type: HAZOP Protocol
title: HAZOP Guide Words, Deviation Analysis, and Recording Template
description: Technical standard for HAZOP guide words, parameter deviation combinations,
  IEC 61882 10-column worksheet template, and application examples.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/hazop/guide-words-and-deviations.md
tags:
- deviations
- guide-words
- hazop
- iec-61882
- pha
- process-safety
sources:
- id: src-1
  resource: reference/raw/standards/HAZOP_Training_Guide.pdf
  title: HAZOP_Training_Guide.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:12:08Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:12:08Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:12:08Z'
status: stable
entity_metadata:
  template_column_count: 10
  case_study: Cleaning Agent Control
  governing_standards:
  - IEC 61882
  time_order_guide_words:
  - Early
  - Late
  - Before
  - After
  classical_guide_words:
  - No or not
  - More
  - Less
  - As well as
  - Part of
  - Reverse
  - Other than
---

> ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
> Guide words must be applied systematically to all elements and physical characteristics of each process node. Teams must not prematurely dismiss deviations without documenting technical rationale if credible hazard mechanisms exist. Every identified safeguard must be scrutinized for human reliability assumptions (e.g., visual inspection limitations or labeling ambiguities) and backed by engineered interlocks or alarms where severe safety, environmental, or product quality harm is possible.

# HAZOP Guide Words, Deviation Analysis, and Recording Template

## 1. Role and Function of HAZOP Guide Words
In accordance with **IEC Standard 61882**, deviations from the design or operational intent are generated through a structured questioning process using standardized **guide words** [^src-1]. The primary role of the guide word is to stimulate imaginative thinking, sharpen the focus of the multidisciplinary team, and provoke rigorous technical dialogue regarding latent vulnerabilities [^src-1].

Guide words provide a systematic and consistent mechanism for brainstorming potential operational abnormalities across both batch and continuous processing systems [^src-1].

---

## 2. Standard Guide Word Classifications

### 2.1 Classical and Process Guide Words
These classical guide words apply to continuous process parameters (such as flow, temperature, pressure, level, composition, and reaction kinetics) and material additions [^src-1]:

| Guide Word | Core Deviation Meaning | Process Context Example |
| :--- | :--- | :--- |
| **No or not** | Complete negation of the design intent [^src-1] | No flow; no cooling water; no reagent added [^src-1] |
| **More** | Quantitative increase above design value [^src-1] | Higher flow rate; higher pressure; excess reagent concentration [^src-1] |
| **Less** | Quantitative decrease below design value [^src-1] | Insufficient flow; low temperature; low chemical concentration [^src-1] |
| **As well as** | Qualitative addition / extraneous material or activity [^src-1] | Contaminant present; entrained gas in liquid line; extraneous byproduct [^src-1] |
| **Part of** | Qualitative omission / partial composition [^src-1] | Critical formulation component omitted; incomplete phase separation [^src-1] |
| **Reverse (of intent)** | Logical or physical opposite of design intent [^src-1] | Backflow from downstream reactor; reverse pump rotation; reverse heat flux [^src-1] |
| **Other than** | Complete substitution of substance or action [^src-1] | Wrong chemical charged; wrong operational line opened; wrong phase [^src-1] |

### 2.2 Time, Order, and Sequence Guide Words
These guide words are primarily deployed for batch processes, sequential logic, operating procedures, and cleaning-in-place (CIP) cycles [^src-1]:

| Guide Word | Sequence Meaning | Operational Context Example |
| :--- | :--- | :--- |
| **Early** | Action occurs before the scheduled time window [^src-1] | Reagent injected before bulk pre-rinse or before target temperature reached [^src-1] |
| **Late** | Action occurs after the scheduled time window [^src-1] | Quench added too late; cycle stopped after excessive residence time [^src-1] |
| **Before** | Sequence reversal (step happens prior to prerequisite) [^src-1] | Agitation engaged before vessel filled, or heating before venting [^src-1] |
| **After** | Step occurs following an unauthorized sequence [^src-1] | Valve closure occurs after pump starts (dead-heading) [^src-1] |
| **Custom** | Tailored guide words crafted for specialized unit operations [^src-1] | E.g., Corrosive, Foaming, Polymerization, Static accumulation [^src-1] |

---

## 3. Practical Case Study: Cleaning Agent Deviation Matrix
The standard demonstrates the application of guide words to a pharmaceutical/chemical cleaning process element (**Detergent Control**) [^src-1]:

| Guide Word | Applied Deviation Scenario (Cleaning Agent) | Engineering Consequence / Hazard Mechanism |
| :--- | :--- | :--- |
| **No or not** | No detergent added during cleaning cycle [^src-1] | Residues not effectively removed; system left in unclean / contaminated state [^src-1] |
| **More** | Too much detergent volume added [^src-1] | Excessive foaming; difficult to rinse; potential chemical residue carryover [^src-1] |
| **More** | Supplied detergent solution concentration is too high [^src-1] | Material corrosion; increased rinse water requirements; effluent non-compliance [^src-1] |
| **Less** | Too little detergent volume added [^src-1] | Cleaning failure; target soils and bioburden not effectively removed [^src-1] |
| **Less** | Supplied detergent solution concentration is too low [^src-1] | Inadequate soil emulsification and sanitization failure [^src-1] |
| **Part of** | Critical detergent component omitted (e.g., surfactant) [^src-1] | Detergent formulation ineffective; surface tension reduction lost [^src-1] |
| **Reverse** | Detergent supply is contaminated with a harmful agent [^src-1] | Gross contamination of product contact surfaces with foreign toxin [^src-1] |
| **Other than** | Wrong detergent used [^src-1] | Material incompatibility, elastomeric seal attack, or ineffective residue removal [^src-1] |
| **Early** | Detergent added too early [^src-1] | Detergent wasted prior to draining bulk soil pre-rinse to sewer [^src-1] |
| **Late** | Detergent added too late in cleaning cycle [^src-1] | Insufficient contact time; wash sequence finishes before soil dissolution [^src-1] |

---

## 4. Standard IEC 61882 HAZOP Recording Template
The documentation of HAZOP analyses is standardized using a 10-column worksheet [^src-1]. Assessment teams may modify or expand columns to integrate specific regulatory, audit, or risk matrix requirements [^src-1]:

### 4.1 Column Specifications and Instructions

| Col No. | Column Title | Technical Field Instruction |
| :---: | :--- | :--- |
| **1** | `No.` | Assign each entry a unique sequential tracking number [^src-1] |
| **2** | `Guide Word` | Insert the specific deviation guide word utilized [^src-1] |
| **3** | `Element` | Describe the element, parameter, material, or process step analyzed [^src-1] |
| **4** | `Deviation` | Formulate the specific operational deviation from design intent [^src-1] |
| **5** | `Possible Causes` | Describe the credible physical, mechanical, or human causes of the deviation [^src-1] |
| **6** | `Consequences` | Detail the potential harmful effects (safety, asset, environment, quality) [^src-1] |
| **7** | `Safeguards` | Enumerate existing preventive or reactive protection and detection controls [^src-1] |
| **8** | `Comments` | Record underlying engineering assumptions, operating data, and rationales [^src-1] |
| **9** | `Actions Required` | Specify necessary risk mitigation, design change, or procedural actions [^src-1] |
| **10** | `Actions Assigned to` | Designate the responsible individual, discipline, or engineering owner [^src-1] |

---

### 4.2 Verbatim Case Records (Cleaning Agent Case Study)

The following records illustrate complete worksheet documentation per the standard [^src-1]:

| No. | Guide Word | Element | Deviation | Possible Causes | Consequences | Safeguards | Comments | Actions Required | Actions Assigned to |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **No** | Cleaning Agent | No detergent added during cleaning cycle [^src-1] | Detergent supply reservoir empty [^src-1] | Residues not effectively removed, leaving system in an unclean state [^src-1] | Technicians check detergent reservoir before every cycle [^src-1] | Assumes technicians can reliably estimate volume visually [^src-1] | Consider alarm for low detergent reservoir level [^src-1] | Engineer [^src-1] |
| **2** | **Other than** | Cleaning Agent | Wrong detergent used [^src-1] | Technician retrieves wrong detergent from warehouse [^src-1] | Incorrect detergent may be ineffective at removing residues, leaving system in an unclean state [^src-1] | Cleaning log requires verification of proper detergent use. Detergent is labeled. [^src-1] | Many different detergent containers look alike [^src-1] | Ensure technician training addresses detergent selection [^src-1] | Trainer [^src-1] |

---

## 5. Integration with Risk Matrices (RAM / RAC)
While standard HAZOP does not mandate quantitative scoring, the standard highlights that teams may optionally incorporate severity and probability ratings into the worksheet [^src-1]. In chemical process plants, this is executed by interfacing the HAZOP worksheet with the plant **Risk Assessment Matrix (RAM)** (see [`hazop/risk-assessment-matrix`](/hazop/risk-assessment-matrix.md)) to prioritize high-risk items (RAC 1 and RAC 2) for immediate engineering mitigation [^src-1].

---

## References
* `reference/raw/standards/HAZOP_Training_Guide.pdf` [^src-1]
* IEC International Standard 61882: *Hazard and operability studies (HAZOP studies) - Application guide* [^src-1]

[^src-1]: PQRI Manufacturing Technology Committee, *Risk Management Training Guides: Hazard & Operability Analysis (HAZOP)*, pp. 4–8.
