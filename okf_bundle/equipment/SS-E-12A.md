---
type: Equipment Concept
title: SS-E-12A — Pressurizer Liquid & Steam Sample Heat Exchanger A
description: Primary Nuclear Sample System heat exchanger cooling high-temperature,
  high-pressure borated reactor coolant from the Pressurizer steam or liquid space
  prior to grab sampling at Primary Sample Panel CP-166A. Arranged in series with
  cooler SS-E-12B and cooled by Component Cooling Water Loop A.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SS-E-12A.md
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
  at: '2026-10-02T13:20:10Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:20:10Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:20:10Z'
status: stable
entity_metadata:
  tag: SS-E-12A
  name: Pressurizer Liquid & Steam Sample Heat Exchanger A
  equipment_class: Heat Exchanger
  unit: SS
  instruments:
  - tag: PI-2804
    service: Pressurizer Sample Inlet Pressure Indicator
    type: Pressure Indicator
    location: PAB Sample HX Room (on RC-3/8"-T line, Grid H-8)
    setpoint_or_range: 0–3000 PSIG
    interlock_or_alarm: Local pressure readout upstream of sample cooler E-12A
    source: PID-1-SS-LR20518
  connections:
  - stream_id: STR-SS-E12A-TUBE-IN
    direction: INLET
    source_tag: RC-E-10 (PRZR, Dwg 20846)
    target_tag: SS-E-12A
    line_size: 3/8"T (1/2" line)
    inline_components:
    - RC-V311 / RC-V313 (LO)
    - RC-FY-2830 / RC-FY-2831 (FC)
    - Penetration X-35
    - RC-FY-2840 (FC)
    - PI-2804
    - RC-V300
    temperature: ~650°F
    pressure: RCS operating pressure (~2235 psig)
    flow_rate: Sample flow rate
    description: Pressurizer steam/liquid sample line entering E-12A tube side via
      Penetration X-35 and CIVs
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E12A-TUBE-OUT
    direction: OUTLET
    source_tag: SS-E-12A
    target_tag: SS-E-12B
    line_size: 3/8"T
    inline_components:
    - 1-SS-FLEX HOSE NO. 1
    temperature: Intermediate sample temp
    pressure: Sample header pressure
    flow_rate: Sample flow rate
    description: Partially cooled sample fluid exiting E-12A to in-series cooler E-12B
      via flexible hose
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E12-BYPASS
    direction: BYPASS
    source_tag: Upstream of RC-V300
    target_tag: Downstream of E-12B
    line_size: 3/8"T
    inline_components:
    - RC-V199
    temperature: Process fluid temp
    pressure: Sample header pressure
    flow_rate: —
    description: Manual cooler bypass around E-12A and E-12B
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E12A-CCW-IN
    direction: UTILITY
    source_tag: CCW LOOP A (20206 [E-1])
    target_tag: SS-E-12A Shell
    line_size: 1" (CC)
    inline_components: []
    temperature: Cooling water supply temp
    pressure: CCW operating pressure
    flow_rate: —
    description: Component Cooling Water supply to shell side from CCW Loop A
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-E12A-CCW-OUT
    direction: UTILITY
    source_tag: SS-E-12A Shell
    target_tag: CCW LOOP A (20206 [E-1])
    line_size: 1" (CC)
    inline_components: []
    temperature: Warmed CCW return temp
    pressure: CCW return pressure
    flow_rate: —
    description: Component Cooling Water return from shell side to CCW Loop A
    source: PID-1-SS-LR20518
---

# SS-E-12A — Pressurizer Liquid & Steam Sample Heat Exchanger A

## Function

Primary Nuclear Sample System heat exchanger cooling high-temperature, high-pressure borated reactor coolant from the Pressurizer steam or liquid space prior to grab sampling at Primary Sample Panel CP-166A. Arranged in series with cooler SS-E-12B and cooled by Component Cooling Water Loop A.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SS-LR20518 (Rev. 0, Ref. B20518 Rev. 12) | — | PID-1-SS-LR20518 |
| Safety Classification | Safety Class NNS (Non-Nuclear Safety) | — | PID-1-SS-LR20518 |
| AMR Scoping Status | In Scope 10 CFR 54.4(a)(2) [Green] | — | PID-1-SS-LR20518 |
| Physical Location | Primary Auxiliary Building (PAB) Sample HX Room (Grid H-7) | — | PID-1-SS-LR20518 |
| Tube Side Material & Schedule | 3/8" Tubing (Mat'l 2500 per Note 3) | — | PID-1-SS-LR20518 |
| Shell Side Cooling Fluid | Component Cooling Water Loop A (1" CC Line) | — | PID-1-SS-LR20518 |
| Upstream Relief Valve Setting | 2485 (RC-V312 & RC-V314 to DR 141) | PSIG | PID-1-SS-LR20518 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Tube Side Operating Fluid | Pressurizer Steam / Liquid Reactor Coolant | — | PID-1-SS-LR20518 |
| Shell Side Operating Fluid | Component Cooling Water (CCW Loop A) | — | PID-1-SS-LR20518 |
| Operating Pressure | ~2235 | PSIG | PID-1-SS-LR20518 |
| Operating Temperature | ~650 (Steam) / ~650 (Liquid) | °F | PID-1-SS-LR20518 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PI-2804](/instruments/PI-2804.md) | Pressurizer Sample Inlet Pressure Indicator | Pressure Indicator | PAB Sample HX Room (on RC-3/8"-T line, Grid H-8) | 0–3000 PSIG | Local pressure readout upstream of sample cooler E-12A | PID-1-SS-LR20518 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-SS-E12A-TUBE-IN | INLET | RC-E-10 (PRZR, Dwg 20846) | SS-E-12A | 3/8"T (1/2" line) | RC-V311 / RC-V313 (LO), RC-FY-2830 / RC-FY-2831 (FC), Penetration X-35, RC-FY-2840 (FC), PI-2804, RC-V300 | ~650°F | RCS operating pressure (~2235 psig) | Sample flow rate | Pressurizer steam/liquid sample line entering E-12A tube side via Penetration X-35 and CIVs |
| STR-SS-E12A-TUBE-OUT | OUTLET | SS-E-12A | SS-E-12B | 3/8"T | 1-SS-FLEX HOSE NO. 1 | Intermediate sample temp | Sample header pressure | Sample flow rate | Partially cooled sample fluid exiting E-12A to in-series cooler E-12B via flexible hose |
| STR-SS-E12-BYPASS | BYPASS | Upstream of RC-V300 | Downstream of E-12B | 3/8"T | RC-V199 | Process fluid temp | Sample header pressure | — | Manual cooler bypass around E-12A and E-12B |
| STR-SS-E12A-CCW-IN | UTILITY | CCW LOOP A (20206 [E-1]) | SS-E-12A Shell | 1" (CC) | — | Cooling water supply temp | CCW operating pressure | — | Component Cooling Water supply to shell side from CCW Loop A |
| STR-SS-E12A-CCW-OUT | UTILITY | SS-E-12A Shell | CCW LOOP A (20206 [E-1]) | 1" (CC) | — | Warmed CCW return temp | CCW return pressure | — | Component Cooling Water return from shell side to CCW Loop A |

## Hazards & Safeguards

- High temperature and pressure steam/liquid sample (up to 2235 psig, 650°F): Upstream overpressure protected by safety relief valves RC-V312 and RC-V314 set at 2485 PSIG discharging to containment trench DR 141.
- Containment isolation integrity: Dual solenoid containment isolation valves RC-FY-2830 / RC-FY-2831 (inside) and RC-FY-2840 (outside) fail closed upon containment isolation signal.
- CCW radioactive contamination hazard: Tube-to-shell leak could contaminate Component Cooling Water; monitored for radiation in CCW Loop A.

## References & Sources

[^src-1]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
