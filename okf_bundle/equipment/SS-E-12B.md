---
type: Equipment Concept
title: SS-E-12B — Pressurizer Liquid & Steam Sample Heat Exchanger B
description: Second-stage nuclear sample heat exchanger arranged in series with SS-E-12A
  to cool pressurizer steam and liquid sample streams down to safe grab-sampling temperatures
  prior to discharge to Primary Sample Panel CP-166A. Cooled by CCW Loop A.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SS-E-12B.md
tags:
- equipment
- heat exchanger
- ss
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-2.pdf
  title: ML101620329-part-2.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:20:23Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:20:23Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:20:23Z'
status: stable
entity_metadata:
  tag: SS-E-12B
  name: Pressurizer Liquid & Steam Sample Heat Exchanger B
  equipment_class: Heat Exchanger
  unit: SS
  connections:
  - stream_id: STR-SS-E12B-TUBE-IN
    direction: INLET
    source_tag: SS-E-12A
    target_tag: SS-E-12B
    line_size: 3/8"T
    inline_components:
    - 1-SS-FLEX HOSE NO. 1
    temperature: Intermediate sample temp
    pressure: Sample header pressure
    flow_rate: Sample flow rate
    description: Partially cooled sample fluid from E-12A entering E-12B tube side
      via flexible hose
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E12B-TUBE-OUT
    direction: OUTLET
    source_tag: SS-E-12B
    target_tag: SS-CP-166A (20519 [F-12])
    line_size: 3/8"T
    inline_components:
    - 1/2" V43
    - 1/2" V79
    temperature: Ambient grab sample temp (~70–100°F)
    pressure: Sample header pressure
    flow_rate: Sample flow rate
    description: Cooled pressurizer sample fluid exiting E-12B to Primary Sample Panel
      CP-166A
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E12B-CCW-IN
    direction: UTILITY
    source_tag: CCW LOOP A (20206 [E-1])
    target_tag: SS-E-12B Shell
    line_size: 1" (CC)
    inline_components: []
    temperature: Cooling water supply temp
    pressure: CCW operating pressure
    flow_rate: —
    description: Component Cooling Water supply to shell side from CCW Loop A
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E12B-CCW-OUT
    direction: UTILITY
    source_tag: SS-E-12B Shell
    target_tag: CCW LOOP A (20206 [E-1])
    line_size: 1" (CC)
    inline_components: []
    temperature: Warmed CCW return temp
    pressure: CCW return pressure
    flow_rate: —
    description: Component Cooling Water return from shell side to CCW Loop A
    source: PID-1-SS-LR20518
---

# SS-E-12B — Pressurizer Liquid & Steam Sample Heat Exchanger B

## Function

Second-stage nuclear sample heat exchanger arranged in series with SS-E-12A to cool pressurizer steam and liquid sample streams down to safe grab-sampling temperatures prior to discharge to Primary Sample Panel CP-166A. Cooled by CCW Loop A.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SS-LR20518 (Rev. 0, Ref. B20518 Rev. 12) | — | PID-1-SS-LR20518 |
| Safety Classification | Safety Class NNS (Non-Nuclear Safety) | — | PID-1-SS-LR20518 |
| AMR Scoping Status | In Scope 10 CFR 54.4(a)(2) [Green] | — | PID-1-SS-LR20518 |
| Physical Location | Primary Auxiliary Building (PAB) Sample HX Room (Grid H-5) | — | PID-1-SS-LR20518 |
| Tube Side Material | 3/8" Tubing (Mat'l 2500 per Note 3) | — | PID-1-SS-LR20518 |
| Shell Side Cooling Fluid | Component Cooling Water Loop A (1" CC Line) | — | PID-1-SS-LR20518 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Tube Side Operating Fluid | Pressurizer Steam / Liquid Reactor Coolant | — | PID-1-SS-LR20518 |
| Shell Side Operating Fluid | Component Cooling Water (CCW Loop A) | — | PID-1-SS-LR20518 |
| Discharge Temperature Target | < 120 (Safe Grab Sampling) | °F | PID-1-SS-LR20518 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-SS-E12B-TUBE-IN | INLET | SS-E-12A | SS-E-12B | 3/8"T | 1-SS-FLEX HOSE NO. 1 | Intermediate sample temp | Sample header pressure | Sample flow rate | Partially cooled sample fluid from E-12A entering E-12B tube side via flexible hose |
| STR-SS-E12B-TUBE-OUT | OUTLET | SS-E-12B | SS-CP-166A (20519 [F-12]) | 3/8"T | 1/2" V43, 1/2" V79 | Ambient grab sample temp (~70–100°F) | Sample header pressure | Sample flow rate | Cooled pressurizer sample fluid exiting E-12B to Primary Sample Panel CP-166A |
| STR-SS-E12B-CCW-IN | UTILITY | CCW LOOP A (20206 [E-1]) | SS-E-12B Shell | 1" (CC) | — | Cooling water supply temp | CCW operating pressure | — | Component Cooling Water supply to shell side from CCW Loop A |
| STR-SS-E12B-CCW-OUT | UTILITY | SS-E-12B Shell | CCW LOOP A (20206 [E-1]) | 1" (CC) | — | Warmed CCW return temp | CCW return pressure | — | Component Cooling Water return from shell side to CCW Loop A |

## Hazards & Safeguards

- Thermal burn hazard from hot sample effluent if CCW cooling is lost. Process sample monitored and throttled via valves V43 and V79.
- Radioactive fluid containment: Secondary containment barrier in PAB Sample HX room with drains routed to liquid waste processing.

## References & Sources

[^src-1]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
