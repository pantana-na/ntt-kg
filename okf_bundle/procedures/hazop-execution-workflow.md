---
type: Workflow Procedure
title: HAZOP Study Execution and Documentation Lifecycle Procedure
description: 'Four-phase operational procedure for conducting HAZOP studies: Definition,
  Preparation, Examination, and Documentation & Follow-up with long-term Risk Review
  and Risk Communication.'
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/procedures/hazop-execution-workflow.md
tags:
- hazop
- iec-61882
- procedures
- process-safety
- risk-management
- workflow
sources:
- id: src-1
  resource: reference/raw/standards/HAZOP_Training_Guide.pdf
  title: HAZOP_Training_Guide.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:11:47Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:11:47Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:11:47Z'
status: stable
entity_metadata:
  four_phases:
  - Definition
  - Preparation
  - Examination
  - Documentation and Follow-up
  post_study_requirements:
  - Action Tracking and Closure Verification
  - Long-Term Risk Review
  - Risk Communication in SOPs
  governing_standards:
  - IEC 61882
  - ICH Q9
---

> ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
> All action items generated during a HAZOP study MUST be tracked through a formal action closure management system prior to process startup. Long-term operational feedback must continually challenge initial baseline assumptions: if operating conditions change, or if installed risk-control measures introduce new or unmasked secondary hazards, the affected system parts MUST be re-studied under an updated HAZOP review.

# HAZOP Study Execution and Documentation Lifecycle Procedure

## 1. Procedure Overview
This procedure defines the rigorous four-phase workflow required to plan, execute, document, and maintain a Hazard and Operability (HAZOP) study in accordance with **IEC Standard 61882** and **ICH Q9 Quality Risk Management** standards [^src-1].

```
┌──────────────────────────────────────┐          ┌──────────────────────────────────────┐
│         PHASE 1: DEFINITION          │          │         PHASE 2: PREPARATION         │
│  • Define scope and objectives       ├─────────►│  • Plan the study and schedule       │
│  • Define responsibilities           │          │  • Collect P&IDs, PFDs, data sheets  │
│  • Select cross-functional SME team  │          │  • Agree on recording format         │
│  • Set boundaries and assumptions    │          │  • Consensus on guide words          │
└──────────────────────────────────────┘          └──────────────────┬───────────────────┘
                                                                     │
                                                                     ▼
┌──────────────────────────────────────┐          ┌──────────────────────────────────────┐
│   PHASE 4: DOCUMENTATION & CLOSURE   │          │         PHASE 3: EXAMINATION         │
│  • Record findings in standard sheet │◄─────────┤  • Divide system into nodes/parts    │
│  • Sign off study documentation      │          │  • Agree design intent per element   │
│  • Produce formal study report       │          │  • Apply guide words systematically  │
│  • Track actions to closure          │          │  • Screen for credible deviations    │
│  • Trigger re-study if modified      │          │  • Identify causes, effects, guards  │
└──────────────────────────────────────┘          │  • Agree on action assignments       │
                                                  └──────────────────────────────────────┘
```

---

## 2. Phase 1: Definition Phase
The Definition Phase establishes the boundaries, objectives, and personnel structure for the analysis [^src-1]:
1. **Define Scope and Objectives**: Articulate the exact processing units, utility loops, or procedural sequences under investigation [^src-1].
2. **Establish Physical and Logical Boundaries**: Delineate battery limits, electrical tie-ins, and shared utility interfaces to prevent analytical overlap or gaps [^src-1].
3. **Document Baseline Assumptions**: Record operating assumptions regarding feed stream compositions, ambient conditions, and utility availability [^src-1].
4. **Assemble Cross-Functional SME Team**:
   - The team must include subject matter experts (SMEs) with diverse technical backgrounds (Process Engineering, Operations, Mechanical Integrity, Instrumentation & Controls, and Process Safety) [^src-1].
   - Participants must display strong technical intuition, recent operational knowledge of system deviations, and conduct reviews in an environment of positive thinking and frank discussion [^src-1].

---

## 3. Phase 2: Preparation Phase
The Preparation Phase organizes the engineering inputs and logistics prior to team sessions [^src-1]:
1. **Locate Supporting Engineering Data**:
   - Up-to-date As-Built P&IDs, Process Flow Diagrams (PFDs), Heat & Material Balances (H&MB), equipment data sheets, and operating procedures [^src-1].
2. **Stakeholder Identification**: Identify the end-users, plant operators, regulators, and management stakeholders who will consume study outputs [^src-1].
3. **Project Management Logistics**: Schedule working sessions, reserve technical scribes, and arrange real-time transcription systems [^src-1].
4. **Recording Format Agreement**: Establish consensus on the worksheet recording format (IEC 61882 standard table) and software tooling [^src-1].
5. **Consensus on Guide Word Matrix**: Pre-select core primary and secondary guide words customized to the specific system type (e.g., continuous chemical reaction, batch transfer, or automated cleaning-in-place) [^src-1].

---

## 4. Phase 3: Examination Phase Workflow
The Examination Phase follows an iterative, systematic questioning process applied element-by-element across every node [^src-1]:

```
[Start Node Examination]
   │
   ▼
[Select System Part / Node & Explain Overall Design]
   │
   ▼
[Examine and Formulate Design Intent]
   │
   ▼
[Identify Relevant Elements and Physical Characteristics]
   │
   ▼
[Select Guide Word] ◄────────────────────────────────────────────────────┐
   │                                                                     │
   ▼                                                                     │
[Apply Guide Word to Element/Characteristic -> Generate Deviation]       │
   │                                                                     │
   ▼                                                                     │
<Is Deviation Credible under Reasonable Use / Misuse?>                   │
   │                                                                     │
  (No) ──► [Discard deviation; do not record non-credible combinations]  │
   │                                                                     │
  (Yes)                                                                  │
   │                                                                     │
   ▼                                                                     │
[Investigate Causes, Consequences, Safeguards (Protection/Indication)]   │
   │                                                                     │
   ▼                                                                     │
[Evaluate Significance of Hazard & Formulate Mitigation Actions]         │
   │                                                                     │
   ▼                                                                     │
<Have all interpretations & combinations been applied?> ──(No)───────────┤
   │                                                                     │
  (Yes)                                                                  │
   │                                                                     │
   ▼                                                                     │
<Have all guide words been applied to this element?> ─────(No)───────────┘
   │
  (Yes)
   │
   ▼
<Have all elements in this part been examined?> ──────────(No)──► [Select Next Element]
   │
  (Yes)
   │
   ▼
<Have all parts / nodes in the system been examined?> ───(No)──► [Select Next Part]
   │
  (Yes)
   │
   ▼
[Proceed to Documentation & Follow-up Phase]
```

### 4.1 Credibility Screening Protocol
* Teams must evaluate all reasonable operating conditions and credible misuse scenarios expected by users [^src-1].
* Combinations that do not yield physically credible failure modes are dropped without mandatory documentation, keeping the focus on genuine operational risks [^src-1].

---

## 5. Phase 4: Documentation and Follow-Up Phase
1. **Worksheet Compilation**: Document each credible deviation on the 10-column IEC 61882 template, capturing tracking numbers, guide words, causes, consequences, safeguards, comments, required actions, and designated owners [^src-1].
2. **Formal Documentation Sign-Off**: Secure cross-functional signatures from team leads, operations managers, and safety authorities [^src-1].
3. **Formal Study Report**: Compile the final output report summarizing methodology, high-risk scenarios, and action register [^src-1].
4. **Action Tracking & Closure Verification**: Implement an auditable action-tracking mechanism. Every assigned engineering mitigation must be tracked until physically verified as implemented and effective [^src-1].
5. **System Re-Study Trigger**: If design changes occur during implementation or if action items alter process parameters, the affected nodes must be formally re-examined [^src-1].

---

## 6. Long-Term Risk Review and Continuous Feedback
* **Operational Feedback Loops**: Facilities must monitor field performance and maintenance logs over multi-year operating campaigns to verify that assumptions regarding residual risks remain valid [^src-1].
* **Secondary Risk Introduction**: HAZOP teams must scrutinize new risk-control measures to ensure they do not create secondary hazards or unmask previously filtered aggravating factors (e.g., adding a bypass line may create deadlegs or bypass hazards) [^src-1].

---

## 7. Risk Communication and Regulatory Compliance
* **Stakeholder Calibration**: Study summaries must be structured at appropriate technical depths for executive sponsors, regulatory auditors, and plant operators [^src-1].
* **Standard Operating Procedure (SOP) Requirements**: When HAZOP serves as the basis for GxP decisions, pharmaceutical validation, or high-hazard regulatory authorizations (e.g., OSHA PSM / EPA RMP), the HAZOP procedure itself must be codified in a controlled SOP [^src-1].
* **Controlled Reporting**: Scoring algorithms, risk ranking criteria, and portfolio updates must be maintained under strict document configuration control [^src-1].

---

## References
* `reference/raw/standards/HAZOP_Training_Guide.pdf` [^src-1]
* IEC International Standard 61882: *Hazard and operability studies (HAZOP studies) - Application guide* [^src-1]

[^src-1]: PQRI Manufacturing Technology Committee, *Risk Management Training Guides: Hazard & Operability Analysis (HAZOP)*, pp. 3–9.
