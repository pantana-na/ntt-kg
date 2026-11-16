---
type: Equipment Concept
title: SS-TK-228A — Post Accident Sample Cask A
description: Heavily shielded Post Accident Sample Cask designed to safely obtain,
  contain, and transport highly radioactive grab samples of post-LOCA reactor coolant
  liquid for radiochemical and isotopic laboratory analysis under 10 CFR 50.34(f)(2)(viii)
  PASS criteria.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SS-TK-228A.md
tags:
- equipment
- ss
- vessel
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-2.pdf
  title: ML101620329-part-2.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:22:18Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:22:18Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:22:18Z'
status: stable
entity_metadata:
  tag: SS-TK-228A
  name: Post Accident Sample Cask A
  equipment_class: Vessel
  unit: SS
  connections:
  - stream_id: STR-SS-CASK-A-IN
    direction: INLET
    source_tag: SS-E-106
    target_tag: SS-TK-228A
    line_size: 3/8"T
    inline_components:
    - SS-V324 (3-Way)
    - SS-V867
    - SS-MM-687 (Quick Disconnect)
    - SS-V897A
    temperature: Ambient grab temp
    pressure: Grab sample pressure
    flow_rate: Grab sample volume
    description: Cooled post-accident sample inlet from PASS HX E-106 via 3-way valve
      V324 and disconnect MM-687
    source: PID-1-SS-LR20520
  - stream_id: STR-SS-CASK-A-OUT
    direction: OUTLET
    source_tag: SS-TK-228A
    target_tag: SS-TK-197 Drain Line
    line_size: 3/8"T
    inline_components:
    - SS-V898A
    - SS-V303
    temperature: Ambient
    pressure: Gravity head
    flow_rate: Drain/flush rate
    description: Sample cask outlet/flush drainage to Flush Tank TK-197 drain line
    source: PID-1-SS-LR20520
---

# SS-TK-228A — Post Accident Sample Cask A

## Function

Heavily shielded Post Accident Sample Cask designed to safely obtain, contain, and transport highly radioactive grab samples of post-LOCA reactor coolant liquid for radiochemical and isotopic laboratory analysis under 10 CFR 50.34(f)(2)(viii) PASS criteria.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SS-LR20520 (Rev. 13) | — | PID-1-SS-LR20520 |
| Safety Classification | Safety Class NNS (General Note 6) | — | PID-1-SS-LR20520 |
| AMR Scoping Status | In Scope 10 CFR 54.4(a)(2) [Green] | — | PID-1-SS-LR20520 |
| Physical Location | PASS Panel Cubicle (Grid B-7) | — | PID-1-SS-LR20520 |
| Inlet Disconnect Coupling | MM-687 Quick Disconnect (General Note 7) | — | PID-1-SS-LR20520 |
| Cask Isolation Valves | V897A (Inlet) & V898A (Outlet) | — | PID-1-SS-LR20520 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Sample Medium | Post-Accident Primary Coolant Liquid | — | PID-1-SS-LR20520 |
| Operating Pressure | Atmospheric to Low Pressure | PSIG | PID-1-SS-LR20520 |
| Operating Temperature | Ambient (~70–100) | °F | PID-1-SS-LR20520 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-SS-CASK-A-IN | INLET | SS-E-106 | SS-TK-228A | 3/8"T | SS-V324 (3-Way), SS-V867, SS-MM-687 (Quick Disconnect), SS-V897A | Ambient grab temp | Grab sample pressure | Grab sample volume | Cooled post-accident sample inlet from PASS HX E-106 via 3-way valve V324 and disconnect MM-687 |
| STR-SS-CASK-A-OUT | OUTLET | SS-TK-228A | SS-TK-197 Drain Line | 3/8"T | SS-V898A, SS-V303 | Ambient | Gravity head | Drain/flush rate | Sample cask outlet/flush drainage to Flush Tank TK-197 drain line |

## Hazards & Safeguards

- Severe radiological exposure hazard: Fluid contains high-activity fission products; cask provides biological lead/steel shielding to protect chemistry technicians during sampling and transport.
- Disconnect leakage: Quick-disconnect coupling MM-687 must be flushed and leak-checked prior to disconnect.

## References & Sources

[^src-1]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
