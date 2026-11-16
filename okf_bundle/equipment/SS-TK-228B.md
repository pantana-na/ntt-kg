---
type: Equipment Concept
title: SS-TK-228B — Post Accident Sample Cask B
description: Redundant heavily shielded Post Accident Sample Cask designed to obtain,
  contain, and transport highly radioactive grab samples of post-LOCA reactor coolant
  liquid for radiochemical and isotopic laboratory analysis under 10 CFR 50.34(f)(2)(viii)
  PASS criteria.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SS-TK-228B.md
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
  at: '2026-10-02T13:22:27Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:22:27Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:22:27Z'
status: stable
entity_metadata:
  tag: SS-TK-228B
  name: Post Accident Sample Cask B
  equipment_class: Vessel
  unit: SS
  connections:
  - stream_id: STR-SS-CASK-B-IN
    direction: INLET
    source_tag: SS-E-106
    target_tag: SS-TK-228B
    line_size: 3/8"T
    inline_components:
    - SS-V324 (3-Way)
    - SS-V866
    - SS-MM-685 (Quick Disconnect)
    - SS-V897B
    temperature: Ambient grab temp
    pressure: Grab sample pressure
    flow_rate: Grab sample volume
    description: Cooled post-accident sample inlet from PASS HX E-106 via 3-way valve
      V324 and disconnect MM-685
    source: PID-1-SS-LR20520
  - stream_id: STR-SS-CASK-B-OUT
    direction: OUTLET
    source_tag: SS-TK-228B
    target_tag: SS-TK-197 Drain Line
    line_size: 3/8"T
    inline_components:
    - SS-V898B
    - SS-V303
    temperature: Ambient
    pressure: Gravity head
    flow_rate: Drain/flush rate
    description: Sample cask outlet/flush drainage to Flush Tank TK-197 drain line
    source: PID-1-SS-LR20520
---

# SS-TK-228B — Post Accident Sample Cask B

## Function

Redundant heavily shielded Post Accident Sample Cask designed to obtain, contain, and transport highly radioactive grab samples of post-LOCA reactor coolant liquid for radiochemical and isotopic laboratory analysis under 10 CFR 50.34(f)(2)(viii) PASS criteria.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SS-LR20520 (Rev. 13) | — | PID-1-SS-LR20520 |
| Safety Classification | Safety Class NNS (General Note 6) | — | PID-1-SS-LR20520 |
| AMR Scoping Status | In Scope 10 CFR 54.4(a)(2) [Green] | — | PID-1-SS-LR20520 |
| Physical Location | PASS Panel Cubicle (Grid B-8) | — | PID-1-SS-LR20520 |
| Inlet Disconnect Coupling | MM-685 Quick Disconnect (General Note 7) | — | PID-1-SS-LR20520 |
| Cask Isolation Valves | V897B (Inlet) & V898B (Outlet) | — | PID-1-SS-LR20520 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Sample Medium | Post-Accident Primary Coolant Liquid | — | PID-1-SS-LR20520 |
| Operating Pressure | Atmospheric to Low Pressure | PSIG | PID-1-SS-LR20520 |
| Operating Temperature | Ambient (~70–100) | °F | PID-1-SS-LR20520 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-SS-CASK-B-IN | INLET | SS-E-106 | SS-TK-228B | 3/8"T | SS-V324 (3-Way), SS-V866, SS-MM-685 (Quick Disconnect), SS-V897B | Ambient grab temp | Grab sample pressure | Grab sample volume | Cooled post-accident sample inlet from PASS HX E-106 via 3-way valve V324 and disconnect MM-685 |
| STR-SS-CASK-B-OUT | OUTLET | SS-TK-228B | SS-TK-197 Drain Line | 3/8"T | SS-V898B, SS-V303 | Ambient | Gravity head | Drain/flush rate | Sample cask outlet/flush drainage to Flush Tank TK-197 drain line |

## Hazards & Safeguards

- Severe radiological exposure hazard: Fluid contains high-activity fission products; cask provides biological shielding to protect chemistry technicians during sampling and transport.
- Disconnect leakage: Quick-disconnect coupling MM-685 must be flushed and leak-checked prior to disconnect.

## References & Sources

[^src-1]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
