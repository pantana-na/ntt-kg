---
type: Equipment Concept
title: SS-E-13A — RC Loop 1 & 3 Liquid Sample Heat Exchanger A
description: Primary Nuclear Sample System heat exchanger cooling high-pressure, high-temperature
  borated liquid drawn from Reactor Coolant System Loop 1 or Loop 3 hot legs. Upstream
  flow throttled to 0.8 gpm via reach-rod valve RC-V345. Arranged in series with cooler
  SS-E-13B and cooled by Component Cooling Water Loop A.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SS-E-13A.md
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
  at: '2026-10-02T13:20:39Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:20:39Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:20:39Z'
status: stable
entity_metadata:
  tag: SS-E-13A
  name: RC Loop 1 & 3 Liquid Sample Heat Exchanger A
  equipment_class: Heat Exchanger
  unit: SS
  instruments:
  - tag: PI-2838
    service: RCS Loop 1 & 3 Sample Inlet Pressure Indicator
    type: Pressure Indicator
    location: PAB Sample HX Room (line RC-3/8"-T, Grid F-8)
    setpoint_or_range: 0–3000 PSIG
    interlock_or_alarm: Local pressure indicator upstream of E-13A
    source: PID-1-SS-LR20518
  connections:
  - stream_id: STR-SS-E13A-TUBE-IN
    direction: INLET
    source_tag: RCS LOOP 1 / 3 (DWG 20841 / 20843)
    target_tag: SS-E-13A
    line_size: 3/8"T (1/2" line)
    inline_components:
    - RC-V290 / RC-V291 (LO)
    - RC-FY-2832 / RC-FY-2833 (FC)
    - Penetration X-35
    - RC-FY-2874 / RC-FY-2876 (FC)
    - RC-FY-2894 / RC-FY-2896 (FC)
    - RC-V345 (0.8 gpm)
    - PI-2838
    temperature: ~590°F (Hot Leg Temp)
    pressure: RCS Operating Pressure (~2235 psig)
    flow_rate: 0.8 gpm (calibrated per Note 5)
    description: Reactor Coolant Loop 1 / Loop 3 liquid sample header entering E-13A
      tube side via reach-rod valve RC-V345
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E13A-TUBE-OUT
    direction: OUTLET
    source_tag: SS-E-13A
    target_tag: SS-E-13B
    line_size: 3/8"T
    inline_components:
    - 1-SS-FLEX HOSE NO. 2
    temperature: Intermediate sample temp
    pressure: Sample header pressure
    flow_rate: 0.8 gpm
    description: Partially cooled RCS liquid sample exiting E-13A to in-series cooler
      E-13B via flexible hose
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E13-BYPASS
    direction: BYPASS
    source_tag: Upstream of E-13A
    target_tag: Downstream of E-13B
    line_size: 3/8"T
    inline_components:
    - RC-V201
    temperature: Process fluid temp
    pressure: Sample header pressure
    flow_rate: —
    description: Manual cooler bypass around E-13A and E-13B
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E13A-CCW-IN
    direction: UTILITY
    source_tag: CCW LOOP A (20206 [D-1])
    target_tag: SS-E-13A Shell
    line_size: 1" (CC)
    inline_components: []
    temperature: Cooling water supply temp
    pressure: CCW operating pressure
    flow_rate: —
    description: Component Cooling Water supply to shell side from CCW Loop A
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E13A-CCW-OUT
    direction: UTILITY
    source_tag: SS-E-13A Shell
    target_tag: CCW LOOP A (20206 [D-1])
    line_size: 1" (CC)
    inline_components: []
    temperature: Warmed CCW return temp
    pressure: CCW return pressure
    flow_rate: —
    description: Component Cooling Water return from shell side to CCW Loop A
    source: PID-1-SS-LR20518
---

# SS-E-13A — RC Loop 1 & 3 Liquid Sample Heat Exchanger A

## Function

Primary Nuclear Sample System heat exchanger cooling high-pressure, high-temperature borated liquid drawn from Reactor Coolant System Loop 1 or Loop 3 hot legs. Upstream flow throttled to 0.8 gpm via reach-rod valve RC-V345. Arranged in series with cooler SS-E-13B and cooled by Component Cooling Water Loop A.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SS-LR20518 (Rev. 0, Ref. B20518 Rev. 12) | — | PID-1-SS-LR20518 |
| Safety Classification | Safety Class NNS (Non-Nuclear Safety) | — | PID-1-SS-LR20518 |
| AMR Scoping Status | In Scope 10 CFR 54.4(a)(2) [Green] | — | PID-1-SS-LR20518 |
| Physical Location | Primary Auxiliary Building (PAB) Sample HX Room (Grid F-7) | — | PID-1-SS-LR20518 |
| Tube Side Material | 3/8" Tubing (Mat'l 2500 per Note 3) | — | PID-1-SS-LR20518 |
| Shell Side Cooling Fluid | Component Cooling Water Loop A (1" CC Line) | — | PID-1-SS-LR20518 |
| Upstream Flow Throttling Requirement | 0.8 (RC-V345 Reach-Rod Throttled per Note 5) | gpm | PID-1-SS-LR20518 |
| Upstream Safety Relief Valve Setpoints | 2485 (RC-V337 for Loop 1 & RC-V378 for Loop 3) | PSIG | PID-1-SS-LR20518 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Tube Side Operating Fluid | Borated Reactor Coolant Liquid (Loops 1 & 3 Hot Legs) | — | PID-1-SS-LR20518 |
| Shell Side Operating Fluid | Component Cooling Water (CCW Loop A) | — | PID-1-SS-LR20518 |
| Sample Flow Rate | 0.8 (set by RC-V345 per General Note 5) | gpm | PID-1-SS-LR20518 |
| Inlet Operating Pressure | ~2235 | PSIG | PID-1-SS-LR20518 |
| Inlet Operating Temperature | ~590 (RCS Hot Leg) | °F | PID-1-SS-LR20518 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PI-2838](/instruments/PI-2838.md) | RCS Loop 1 & 3 Sample Inlet Pressure Indicator | Pressure Indicator | PAB Sample HX Room (line RC-3/8"-T, Grid F-8) | 0–3000 PSIG | Local pressure indicator upstream of E-13A | PID-1-SS-LR20518 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-SS-E13A-TUBE-IN | INLET | RCS LOOP 1 / 3 (DWG 20841 / 20843) | SS-E-13A | 3/8"T (1/2" line) | RC-V290 / RC-V291 (LO), RC-FY-2832 / RC-FY-2833 (FC), Penetration X-35, RC-FY-2874 / RC-FY-2876 (FC), RC-FY-2894 / RC-FY-2896 (FC), RC-V345 (0.8 gpm), PI-2838 | ~590°F (Hot Leg Temp) | RCS Operating Pressure (~2235 psig) | 0.8 gpm (calibrated per Note 5) | Reactor Coolant Loop 1 / Loop 3 liquid sample header entering E-13A tube side via reach-rod valve RC-V345 |
| STR-SS-E13A-TUBE-OUT | OUTLET | SS-E-13A | SS-E-13B | 3/8"T | 1-SS-FLEX HOSE NO. 2 | Intermediate sample temp | Sample header pressure | 0.8 gpm | Partially cooled RCS liquid sample exiting E-13A to in-series cooler E-13B via flexible hose |
| STR-SS-E13-BYPASS | BYPASS | Upstream of E-13A | Downstream of E-13B | 3/8"T | RC-V201 | Process fluid temp | Sample header pressure | — | Manual cooler bypass around E-13A and E-13B |
| STR-SS-E13A-CCW-IN | UTILITY | CCW LOOP A (20206 [D-1]) | SS-E-13A Shell | 1" (CC) | — | Cooling water supply temp | CCW operating pressure | — | Component Cooling Water supply to shell side from CCW Loop A |
| STR-SS-E13A-CCW-OUT | UTILITY | SS-E-13A Shell | CCW LOOP A (20206 [D-1]) | 1" (CC) | — | Warmed CCW return temp | CCW return pressure | — | Component Cooling Water return from shell side to CCW Loop A |

## Hazards & Safeguards

- High pressure and radiation hazard from primary coolant: Upstream lines protected against overpressure by relief valves RC-V337 and RC-V378 set at 2485 PSIG.
- Containment isolation: Redundant solenoid valves RC-FY-2832, RC-FY-2874, RC-FY-2894 (Loop 1) and RC-FY-2833, RC-FY-2876, RC-FY-2896 (Loop 3) fail closed on containment isolation signal. Breakers 84T and 84U in MCC-522 locked open per Note 11.
- CCW radioactive in-leakage hazard: Monitored for radioactive contamination in CCW Loop A.

## References & Sources

[^src-1]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
