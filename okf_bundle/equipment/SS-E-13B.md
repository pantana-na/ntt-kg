---
type: Equipment Concept
title: SS-E-13B — RC Loop 1 & 3 Liquid Sample Heat Exchanger B
description: Second-stage nuclear sample heat exchanger arranged in series with SS-E-13A
  to cool reactor coolant liquid from loops 1 and 3 down to safe grab-sampling temperatures
  prior to discharge to Primary Sample Panel CP-166A. Cooled by CCW Loop A.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SS-E-13B.md
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
  at: '2026-10-02T13:20:53Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:20:53Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:20:53Z'
status: stable
entity_metadata:
  tag: SS-E-13B
  name: RC Loop 1 & 3 Liquid Sample Heat Exchanger B
  equipment_class: Heat Exchanger
  unit: SS
  instruments:
  - tag: TI-467
    service: Loop Sample HX Cooled Effluent Temperature
    type: Temperature Indicator
    location: PAB Sample HX Room (on 3/8"-T line, Grid E-4)
    setpoint_or_range: Ambient to 200°F
    interlock_or_alarm: Local/Panel temperature indicator at heat exchanger discharge
    source: PID-1-SS-LR20518
  connections:
  - stream_id: STR-SS-E13B-TUBE-IN
    direction: INLET
    source_tag: SS-E-13A
    target_tag: SS-E-13B
    line_size: 3/8"T
    inline_components:
    - 1-SS-FLEX HOSE NO. 2
    temperature: Intermediate sample temp
    pressure: Sample header pressure
    flow_rate: 0.8 gpm
    description: Partially cooled RCS liquid sample from E-13A entering E-13B tube
      side via flexible hose
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E13B-TUBE-OUT
    direction: OUTLET
    source_tag: SS-E-13B
    target_tag: SS-CP-166A (20519 [E-12])
    line_size: 3/8"T
    inline_components:
    - 1/2" V44
    - 3/8" V127
    - 3/8" V783
    - 1/2"-V80
    - TI-467
    temperature: Ambient grab sample temp (~70–100°F)
    pressure: Sample header pressure
    flow_rate: 0.8 gpm
    description: Cooled RCS liquid sample exiting E-13B to Primary Sample Panel CP-166A
      via throttle valves and TI-467
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E13B-CCW-IN
    direction: UTILITY
    source_tag: CCW LOOP A (20206 [D-1])
    target_tag: SS-E-13B Shell
    line_size: 1" (CC)
    inline_components: []
    temperature: Cooling water supply temp
    pressure: CCW operating pressure
    flow_rate: —
    description: Component Cooling Water supply to shell side from CCW Loop A
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E13B-CCW-OUT
    direction: UTILITY
    source_tag: SS-E-13B Shell
    target_tag: CCW LOOP A (20206 [D-1])
    line_size: 1" (CC)
    inline_components: []
    temperature: Warmed CCW return temp
    pressure: CCW return pressure
    flow_rate: —
    description: Component Cooling Water return from shell side to CCW Loop A
    source: PID-1-SS-LR20518
---

# SS-E-13B — RC Loop 1 & 3 Liquid Sample Heat Exchanger B

## Function

Second-stage nuclear sample heat exchanger arranged in series with SS-E-13A to cool reactor coolant liquid from loops 1 and 3 down to safe grab-sampling temperatures prior to discharge to Primary Sample Panel CP-166A. Cooled by CCW Loop A.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SS-LR20518 (Rev. 0, Ref. B20518 Rev. 12) | — | PID-1-SS-LR20518 |
| Safety Classification | Safety Class NNS (Non-Nuclear Safety) | — | PID-1-SS-LR20518 |
| AMR Scoping Status | In Scope 10 CFR 54.4(a)(2) [Green] | — | PID-1-SS-LR20518 |
| Physical Location | Primary Auxiliary Building (PAB) Sample HX Room (Grid F-5) | — | PID-1-SS-LR20518 |
| Tube Side Material | 3/8" Tubing (Mat'l 2500 per Note 3) | — | PID-1-SS-LR20518 |
| Shell Side Cooling Fluid | Component Cooling Water Loop A (1" CC Line) | — | PID-1-SS-LR20518 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Tube Side Operating Fluid | Borated Reactor Coolant Liquid (Loops 1 & 3 Hot Legs) | — | PID-1-SS-LR20518 |
| Shell Side Operating Fluid | Component Cooling Water (CCW Loop A) | — | PID-1-SS-LR20518 |
| Cooled Effluent Temperature | < 120 (Monitored by TI-467) | °F | PID-1-SS-LR20518 |
| Design Flow Rate | 0.8 | gpm | PID-1-SS-LR20518 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TI-467](/instruments/TI-467.md) | Loop Sample HX Cooled Effluent Temperature | Temperature Indicator | PAB Sample HX Room (on 3/8"-T line, Grid E-4) | Ambient to 200°F | Local/Panel temperature indicator at heat exchanger discharge | PID-1-SS-LR20518 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-SS-E13B-TUBE-IN | INLET | SS-E-13A | SS-E-13B | 3/8"T | 1-SS-FLEX HOSE NO. 2 | Intermediate sample temp | Sample header pressure | 0.8 gpm | Partially cooled RCS liquid sample from E-13A entering E-13B tube side via flexible hose |
| STR-SS-E13B-TUBE-OUT | OUTLET | SS-E-13B | SS-CP-166A (20519 [E-12]) | 3/8"T | 1/2" V44, 3/8" V127, 3/8" V783, 1/2"-V80, TI-467 | Ambient grab sample temp (~70–100°F) | Sample header pressure | 0.8 gpm | Cooled RCS liquid sample exiting E-13B to Primary Sample Panel CP-166A via throttle valves and TI-467 |
| STR-SS-E13B-CCW-IN | UTILITY | CCW LOOP A (20206 [D-1]) | SS-E-13B Shell | 1" (CC) | — | Cooling water supply temp | CCW operating pressure | — | Component Cooling Water supply to shell side from CCW Loop A |
| STR-SS-E13B-CCW-OUT | UTILITY | SS-E-13B Shell | CCW LOOP A (20206 [D-1]) | 1" (CC) | — | Warmed CCW return temp | CCW return pressure | — | Component Cooling Water return from shell side to CCW Loop A |

## Hazards & Safeguards

- Thermal burn hazard if cooling is degraded: Process temperature is monitored at the outlet by TI-467 before fluid reaches the sample sink.
- Primary coolant activity hazard: Sample lines carry reactor coolant fission and corrosion products; sample fluid is isolated in a ventilated enclosure.

## References & Sources

[^src-1]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
