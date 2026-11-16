---
type: Equipment Concept
title: 1-SS-E-14B — Steam Generator 2 Primary Sample Heat Exchanger
description: Primary sample cooler for Steam Generator 2 blowdown sample stream, cooling
  high-temperature blowdown water against CCW Loop A prior to secondary constant temperature
  cooling in E-174 and chemical/radiological analysis.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/1-SS-E-14B.md
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
  at: '2026-11-05T14:32:32Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:32:32Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:32:32Z'
status: stable
entity_metadata:
  tag: 1-SS-E-14B
  name: Steam Generator 2 Primary Sample Heat Exchanger
  equipment_class: Heat Exchanger
  unit: SS
  instruments:
  - tag: TI-2786
    service: S/G 2 Cooled Sample Temperature
    type: Temperature Indicator
    location: E-14B Tube Outlet Line [10-E]
    setpoint_or_range: —
    interlock_or_alarm: Local temperature indication
    source: PID-1-SS-LR20521
  - tag: PCV-2827
    service: S/G 2 Sample Pressure Regulation
    type: Pressure Control / Relief Valve
    location: E-14B Tube Outlet Line [10-E]
    setpoint_or_range: Variable Pressure Regulating Element
    interlock_or_alarm: Variable pressure regulation / overpressure relief
    source: PID-1-SS-LR20521
  connections:
  - stream_id: SS-IN-1-SS-E-14B
    direction: INLET
    source_tag: SB-SG2-BLOWDOWN
    target_tag: 1-SS-E-14B
    line_size: 3/8" Tubing
    inline_components:
    - Root Isolation
    temperature: S/G operating temp
    pressure: Steam generator blowdown operating pressure
    flow_rate: —
    description: S/G 2 Blowdown sample supply line from Dwg 20626 [F-12] into E-14B
      tube inlet
    source: PID-1-SS-LR20521 (Grid 12-E) / Dwg 20626
  - stream_id: SS-OUT-1-SS-E-14B
    direction: OUTLET
    source_tag: 1-SS-E-14B
    target_tag: 1-SS-E-174
    line_size: 3/8" Tubing
    inline_components:
    - V15 (Tube Outlet Isolation Valve)
    - TI-2786 (Temperature Indicator)
    - PCV-2827 (Variable Pressure Regulating Element / Relief)
    temperature: Monitored by TI-2786
    pressure: Regulated by PCV-2827
    flow_rate: —
    description: Cooled sample tube outlet through isolation valve V15 to local indicator
      TI-2786 and PCV-2827
    source: PID-1-SS-LR20521 (Grid 10-E)
  - stream_id: CC-SUP-E14B
    direction: UTILITY
    source_tag: CCW-LOOP-A-SUP
    target_tag: 1-SS-E-14B
    line_size: CC-1"
    inline_components:
    - V763 (CCW Supply Isolation)
    temperature: CCW supply temp
    pressure: CCW operating pressure
    flow_rate: —
    description: Component Cooling Water Loop A supply through isolation valve V763
      to E-14B shell side
    source: PID-1-SS-LR20521 (Grid 11-E) / Dwg 20206 [G-11]
  - stream_id: CC-RET-E14B
    direction: UTILITY
    source_tag: 1-SS-E-14B
    target_tag: CCW-LOOP-A-RET
    line_size: CC-1"
    inline_components:
    - V768 (CCW Return Isolation)
    - V769 (CCW Return Throttling)
    temperature: CCW return temp
    pressure: —
    flow_rate: —
    description: Component Cooling Water Loop A return from E-14B shell side through
      V768 and throttling valve V769
    source: PID-1-SS-LR20521 (Grid 10-E) / Dwg 20206 [G-11]
  - stream_id: SS-VENT-E14B
    direction: VENT
    source_tag: 1-SS-E-14B
    target_tag: ATMOSPHERE
    line_size: 3/8"
    inline_components:
    - V842 (Shell Vent Valve)
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Shell side vent line through valve V842
    source: PID-1-SS-LR20521 (Grid 11-F)
---

# 1-SS-E-14B — Steam Generator 2 Primary Sample Heat Exchanger

## Function

Primary sample cooler for Steam Generator 2 blowdown sample stream, cooling high-temperature blowdown water against CCW Loop A prior to secondary constant temperature cooling in E-174 and chemical/radiological analysis.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Equipment Tag | 1-SS-E-14B (Section 4.1 & Sheet 1 Grid 10-E) | — | PID-1-SS-LR20521 |
| Nuclear Safety Classification | Safety Class NNS (Non-Nuclear Safety) (General Note 10) | — | PID-1-SS-LR20521 |
| License Renewal AMR Status | In Scope (AMR) per 10 CFR 54.4(a)(2) (Green line color coding per 10 CFR 54.21) | — | PID-1-SS-LR20521 |
| Sample Tubing Specification | 3/8" Tubing, Material Class 2508 (General Note 3) | — | PID-1-SS-LR20521 |
| Shell Cooling Medium | Component Cooling Water (CCW) Loop A (1" line) (Section 4.1) | — | PID-1-SS-LR20521 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Tube Side Medium | Steam Generator 2 Blowdown Water | — | PID-1-SS-LR20521 |
| Shell Side Medium | Component Cooling Water Loop A | — | PID-1-SS-LR20521 |
| Panel Location | Sample Panel CP-166B Area | — | PID-1-SS-LR20521 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TI-2786](/instruments/le-2384-1.md) | S/G 2 Cooled Sample Temperature | Temperature Indicator | E-14B Tube Outlet Line [10-E] | — | Local temperature indication | PID-1-SS-LR20521 |
| [PCV-2827](/instruments/le-2384-1.md) | S/G 2 Sample Pressure Regulation | Pressure Control / Relief Valve | E-14B Tube Outlet Line [10-E] | Variable Pressure Regulating Element | Variable pressure regulation / overpressure relief | PID-1-SS-LR20521 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SS-IN-1-SS-E-14B | INLET | SB-SG2-BLOWDOWN | 1-SS-E-14B | 3/8" Tubing | Root Isolation | S/G operating temp | Steam generator blowdown operating pressure | — | S/G 2 Blowdown sample supply line from Dwg 20626 [F-12] into E-14B tube inlet |
| SS-OUT-1-SS-E-14B | OUTLET | 1-SS-E-14B | 1-SS-E-174 | 3/8" Tubing | V15 (Tube Outlet Isolation Valve), TI-2786 (Temperature Indicator), PCV-2827 (Variable Pressure Regulating Element / Relief) | Monitored by TI-2786 | Regulated by PCV-2827 | — | Cooled sample tube outlet through isolation valve V15 to local indicator TI-2786 and PCV-2827 |
| CC-SUP-E14B | UTILITY | CCW-LOOP-A-SUP | 1-SS-E-14B | CC-1" | V763 (CCW Supply Isolation) | CCW supply temp | CCW operating pressure | — | Component Cooling Water Loop A supply through isolation valve V763 to E-14B shell side |
| CC-RET-E14B | UTILITY | 1-SS-E-14B | CCW-LOOP-A-RET | CC-1" | V768 (CCW Return Isolation), V769 (CCW Return Throttling) | CCW return temp | — | — | Component Cooling Water Loop A return from E-14B shell side through V768 and throttling valve V769 |
| SS-VENT-E14B | VENT | 1-SS-E-14B | ATMOSPHERE | 3/8" | V842 (Shell Vent Valve) | Ambient | Atmospheric | — | Shell side vent line through valve V842 |

## Hazards & Safeguards

- High pressure and high temperature blowdown steam/water hazard mitigated by upstream isolation and downstream variable pressure regulating element PCV-2827.
- Thermal stress or tube leak from radioactive primary-to-secondary steam generator leakage monitored downstream by radiation detector RE-6511 on RM-SKD-84.

## References & Sources

[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
