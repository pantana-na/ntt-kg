---
type: Equipment Concept
title: 1-SS-E-14A — Steam Generator 1 Primary Sample Heat Exchanger
description: Primary sample cooler for Steam Generator 1 blowdown sample stream, cooling
  high-temperature, high-pressure blowdown water against Component Cooling Water Loop
  A prior to secondary constant temperature cooling in E-173 and chemical/radiological
  analysis.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/1-SS-E-14A.md
tags:
- equipment
- heat exchanger
- ss
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-3.pdf
  title: ML101620329-part-3.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-11-05T14:32:18Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:32:18Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:32:18Z'
status: stable
entity_metadata:
  tag: 1-SS-E-14A
  name: Steam Generator 1 Primary Sample Heat Exchanger
  equipment_class: Heat Exchanger
  unit: SS
  instruments:
  - tag: TI-2785
    service: S/G 1 Cooled Sample Temperature
    type: Temperature Indicator
    location: E-14A Tube Outlet Line [10-G]
    setpoint_or_range: —
    interlock_or_alarm: Local temperature indication
    source: PID-1-SS-LR20521
  - tag: PCV-2826
    service: S/G 1 Sample Pressure Regulation
    type: Pressure Control / Relief Valve
    location: E-14A Tube Outlet Line [10-G]
    setpoint_or_range: Variable Pressure Regulating Element
    interlock_or_alarm: Variable pressure regulation / overpressure relief
    source: PID-1-SS-LR20521
  connections:
  - stream_id: SS-IN-1-SS-E-14A
    direction: INLET
    source_tag: SB-SG1-BLOWDOWN
    target_tag: 1-SS-E-14A
    line_size: 3/8" Tubing
    inline_components:
    - Root Isolation
    temperature: S/G operating temp
    pressure: Steam generator blowdown operating pressure
    flow_rate: —
    description: S/G 1 Blowdown sample supply line from Dwg 20626 [F-12] into E-14A
      tube inlet
    source: PID-1-SS-LR20521 (Grid 12-G) / Dwg 20626
  - stream_id: SS-OUT-1-SS-E-14A
    direction: OUTLET
    source_tag: 1-SS-E-14A
    target_tag: 1-SS-E-173
    line_size: 3/8" Tubing
    inline_components:
    - V5 (Tube Outlet Isolation Valve)
    - TI-2785 (Temperature Indicator)
    - PCV-2826 (Variable Pressure Regulating Element / Relief)
    temperature: Monitored by TI-2785
    pressure: Regulated by PCV-2826
    flow_rate: —
    description: Cooled sample tube outlet through isolation valve V5 to local indicator
      TI-2785 and PCV-2826
    source: PID-1-SS-LR20521 (Grid 10-G)
  - stream_id: CC-SUP-E14A
    direction: UTILITY
    source_tag: CCW-LOOP-A-SUP
    target_tag: 1-SS-E-14A
    line_size: CC-1"
    inline_components:
    - V762 (CCW Supply Isolation)
    temperature: CCW supply temp
    pressure: CCW operating pressure
    flow_rate: —
    description: Component Cooling Water Loop A supply through isolation valve V762
      to E-14A shell side
    source: PID-1-SS-LR20521 (Grid 11-G) / Dwg 20206 [G-11]
  - stream_id: CC-RET-E14A
    direction: UTILITY
    source_tag: 1-SS-E-14A
    target_tag: CCW-LOOP-A-RET
    line_size: CC-1"
    inline_components:
    - V766 (CCW Return Isolation)
    - V767 (CCW Return Throttling)
    temperature: CCW return temp
    pressure: —
    flow_rate: —
    description: Component Cooling Water Loop A return from E-14A shell side through
      V766 and throttling valve V767
    source: PID-1-SS-LR20521 (Grid 10-G) / Dwg 20206 [G-11]
  - stream_id: SS-VENT-E14A
    direction: VENT
    source_tag: 1-SS-E-14A
    target_tag: ATMOSPHERE
    line_size: 3/8"
    inline_components:
    - V841 (Shell Vent Valve)
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Shell side vent line through valve V841
    source: PID-1-SS-LR20521 (Grid 11-G)
---

# 1-SS-E-14A — Steam Generator 1 Primary Sample Heat Exchanger

## Function

Primary sample cooler for Steam Generator 1 blowdown sample stream, cooling high-temperature, high-pressure blowdown water against Component Cooling Water Loop A prior to secondary constant temperature cooling in E-173 and chemical/radiological analysis.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Equipment Tag | 1-SS-E-14A (Section 4.1 & Sheet 1 Grid 10-G) | — | PID-1-SS-LR20521 |
| Nuclear Safety Classification | Safety Class NNS (Non-Nuclear Safety) (General Note 10) | — | PID-1-SS-LR20521 |
| License Renewal AMR Status | In Scope (AMR) per 10 CFR 54.4(a)(2) (Green line color coding per 10 CFR 54.21) | — | PID-1-SS-LR20521 |
| Sample Tubing Specification | 3/8" Tubing, Material Class 2508 (General Note 3) | — | PID-1-SS-LR20521 |
| Shell Cooling Medium | Component Cooling Water (CCW) Loop A (1" line) (Section 4.1) | — | PID-1-SS-LR20521 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Tube Side Medium | Steam Generator 1 Blowdown Water | — | PID-1-SS-LR20521 |
| Shell Side Medium | Component Cooling Water Loop A | — | PID-1-SS-LR20521 |
| Panel Location | Sample Panel CP-166B Area | — | PID-1-SS-LR20521 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TI-2785](/instruments/le-2384-1.md) | S/G 1 Cooled Sample Temperature | Temperature Indicator | E-14A Tube Outlet Line [10-G] | — | Local temperature indication | PID-1-SS-LR20521 |
| [PCV-2826](/instruments/le-2384-1.md) | S/G 1 Sample Pressure Regulation | Pressure Control / Relief Valve | E-14A Tube Outlet Line [10-G] | Variable Pressure Regulating Element | Variable pressure regulation / overpressure relief | PID-1-SS-LR20521 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SS-IN-1-SS-E-14A | INLET | SB-SG1-BLOWDOWN | 1-SS-E-14A | 3/8" Tubing | Root Isolation | S/G operating temp | Steam generator blowdown operating pressure | — | S/G 1 Blowdown sample supply line from Dwg 20626 [F-12] into E-14A tube inlet |
| SS-OUT-1-SS-E-14A | OUTLET | 1-SS-E-14A | 1-SS-E-173 | 3/8" Tubing | V5 (Tube Outlet Isolation Valve), TI-2785 (Temperature Indicator), PCV-2826 (Variable Pressure Regulating Element / Relief) | Monitored by TI-2785 | Regulated by PCV-2826 | — | Cooled sample tube outlet through isolation valve V5 to local indicator TI-2785 and PCV-2826 |
| CC-SUP-E14A | UTILITY | CCW-LOOP-A-SUP | 1-SS-E-14A | CC-1" | V762 (CCW Supply Isolation) | CCW supply temp | CCW operating pressure | — | Component Cooling Water Loop A supply through isolation valve V762 to E-14A shell side |
| CC-RET-E14A | UTILITY | 1-SS-E-14A | CCW-LOOP-A-RET | CC-1" | V766 (CCW Return Isolation), V767 (CCW Return Throttling) | CCW return temp | — | — | Component Cooling Water Loop A return from E-14A shell side through V766 and throttling valve V767 |
| SS-VENT-E14A | VENT | 1-SS-E-14A | ATMOSPHERE | 3/8" | V841 (Shell Vent Valve) | Ambient | Atmospheric | — | Shell side vent line through valve V841 |

## Hazards & Safeguards

- High pressure and high temperature blowdown steam/water hazard mitigated by upstream isolation and downstream variable pressure regulating element PCV-2826.
- Thermal stress or tube leak from radioactive primary-to-secondary steam generator leakage monitored downstream by radiation detector RE-6510 on RM-SKD-83.

## References & Sources

[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
