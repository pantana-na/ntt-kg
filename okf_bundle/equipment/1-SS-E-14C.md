---
type: Equipment Concept
title: 1-SS-E-14C — Steam Generator 3 Primary Sample Heat Exchanger
description: Primary sample cooler for Steam Generator 3 blowdown sample stream, cooling
  high-temperature blowdown water against CCW Loop A prior to secondary constant temperature
  cooling in E-175 and chemical/radiological analysis.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/1-SS-E-14C.md
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
  at: '2026-11-05T14:32:44Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:32:44Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:32:44Z'
status: stable
entity_metadata:
  tag: 1-SS-E-14C
  name: Steam Generator 3 Primary Sample Heat Exchanger
  equipment_class: Heat Exchanger
  unit: SS
  instruments:
  - tag: TI-2787
    service: S/G 3 Cooled Sample Temperature
    type: Temperature Indicator
    location: E-14C Tube Outlet Line [10-D]
    setpoint_or_range: —
    interlock_or_alarm: Local temperature indication
    source: PID-1-SS-LR20521
  - tag: PCV-2828
    service: S/G 3 Sample Pressure Regulation
    type: Pressure Control / Relief Valve
    location: E-14C Tube Outlet Line [10-D]
    setpoint_or_range: Variable Pressure Regulating Element
    interlock_or_alarm: Variable pressure regulation / overpressure relief
    source: PID-1-SS-LR20521
  connections:
  - stream_id: SS-IN-1-SS-E-14C
    direction: INLET
    source_tag: SB-SG3-BLOWDOWN
    target_tag: 1-SS-E-14C
    line_size: 3/8" Tubing
    inline_components:
    - Root Isolation
    temperature: S/G operating temp
    pressure: Steam generator blowdown operating pressure
    flow_rate: —
    description: S/G 3 Blowdown sample supply line from Dwg 20626 [E-12] into E-14C
      tube inlet
    source: PID-1-SS-LR20521 (Grid 12-D) / Dwg 20626
  - stream_id: SS-OUT-1-SS-E-14C
    direction: OUTLET
    source_tag: 1-SS-E-14C
    target_tag: 1-SS-E-175
    line_size: 3/8" Tubing
    inline_components:
    - V20 (Tube Outlet Isolation Valve)
    - TI-2787 (Temperature Indicator)
    - PCV-2828 (Variable Pressure Regulating Element / Relief)
    temperature: Monitored by TI-2787
    pressure: Regulated by PCV-2828
    flow_rate: —
    description: Cooled sample tube outlet through isolation valve V20 to local indicator
      TI-2787 and PCV-2828
    source: PID-1-SS-LR20521 (Grid 10-D)
  - stream_id: CC-SUP-E14C
    direction: UTILITY
    source_tag: CCW-LOOP-A-SUP
    target_tag: 1-SS-E-14C
    line_size: CC-1"
    inline_components:
    - V764 (CCW Supply Isolation)
    temperature: CCW supply temp
    pressure: CCW operating pressure
    flow_rate: —
    description: Component Cooling Water Loop A supply through isolation valve V764
      to E-14C shell side
    source: PID-1-SS-LR20521 (Grid 11-D) / Dwg 20206 [F-11]
  - stream_id: CC-RET-E14C
    direction: UTILITY
    source_tag: 1-SS-E-14C
    target_tag: CCW-LOOP-A-RET
    line_size: CC-1"
    inline_components:
    - V770 (CCW Return Isolation)
    - V771 (CCW Return Throttling)
    temperature: CCW return temp
    pressure: —
    flow_rate: —
    description: Component Cooling Water Loop A return from E-14C shell side through
      V770 and throttling valve V771
    source: PID-1-SS-LR20521 (Grid 10-D) / Dwg 20206 [F-11]
  - stream_id: SS-VENT-E14C
    direction: VENT
    source_tag: 1-SS-E-14C
    target_tag: ATMOSPHERE
    line_size: 3/8"
    inline_components:
    - V843 (Shell Vent Valve)
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Shell side vent line through valve V843
    source: PID-1-SS-LR20521 (Grid 11-D)
---

# 1-SS-E-14C — Steam Generator 3 Primary Sample Heat Exchanger

## Function

Primary sample cooler for Steam Generator 3 blowdown sample stream, cooling high-temperature blowdown water against CCW Loop A prior to secondary constant temperature cooling in E-175 and chemical/radiological analysis.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Equipment Tag | 1-SS-E-14C (Section 4.1 & Sheet 1 Grid 10-D) | — | PID-1-SS-LR20521 |
| Nuclear Safety Classification | Safety Class NNS (Non-Nuclear Safety) (General Note 10) | — | PID-1-SS-LR20521 |
| License Renewal AMR Status | In Scope (AMR) per 10 CFR 54.4(a)(2) (Green line color coding per 10 CFR 54.21) | — | PID-1-SS-LR20521 |
| Sample Tubing Specification | 3/8" Tubing, Material Class 2508 (General Note 3) | — | PID-1-SS-LR20521 |
| Shell Cooling Medium | Component Cooling Water (CCW) Loop A (1" line) (Section 4.1) | — | PID-1-SS-LR20521 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Tube Side Medium | Steam Generator 3 Blowdown Water | — | PID-1-SS-LR20521 |
| Shell Side Medium | Component Cooling Water Loop A | — | PID-1-SS-LR20521 |
| Panel Location | Sample Panel CP-166B Area | — | PID-1-SS-LR20521 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TI-2787](/instruments/le-2384-1.md) | S/G 3 Cooled Sample Temperature | Temperature Indicator | E-14C Tube Outlet Line [10-D] | — | Local temperature indication | PID-1-SS-LR20521 |
| [PCV-2828](/instruments/le-2384-1.md) | S/G 3 Sample Pressure Regulation | Pressure Control / Relief Valve | E-14C Tube Outlet Line [10-D] | Variable Pressure Regulating Element | Variable pressure regulation / overpressure relief | PID-1-SS-LR20521 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SS-IN-1-SS-E-14C | INLET | SB-SG3-BLOWDOWN | 1-SS-E-14C | 3/8" Tubing | Root Isolation | S/G operating temp | Steam generator blowdown operating pressure | — | S/G 3 Blowdown sample supply line from Dwg 20626 [E-12] into E-14C tube inlet |
| SS-OUT-1-SS-E-14C | OUTLET | 1-SS-E-14C | 1-SS-E-175 | 3/8" Tubing | V20 (Tube Outlet Isolation Valve), TI-2787 (Temperature Indicator), PCV-2828 (Variable Pressure Regulating Element / Relief) | Monitored by TI-2787 | Regulated by PCV-2828 | — | Cooled sample tube outlet through isolation valve V20 to local indicator TI-2787 and PCV-2828 |
| CC-SUP-E14C | UTILITY | CCW-LOOP-A-SUP | 1-SS-E-14C | CC-1" | V764 (CCW Supply Isolation) | CCW supply temp | CCW operating pressure | — | Component Cooling Water Loop A supply through isolation valve V764 to E-14C shell side |
| CC-RET-E14C | UTILITY | 1-SS-E-14C | CCW-LOOP-A-RET | CC-1" | V770 (CCW Return Isolation), V771 (CCW Return Throttling) | CCW return temp | — | — | Component Cooling Water Loop A return from E-14C shell side through V770 and throttling valve V771 |
| SS-VENT-E14C | VENT | 1-SS-E-14C | ATMOSPHERE | 3/8" | V843 (Shell Vent Valve) | Ambient | Atmospheric | — | Shell side vent line through valve V843 |

## Hazards & Safeguards

- High pressure and high temperature blowdown steam/water hazard mitigated by upstream isolation and downstream variable pressure regulating element PCV-2828.
- Thermal stress or tube leak from radioactive primary-to-secondary steam generator leakage monitored downstream by radiation detector RE-6512 on RM-SKD-85.

## References & Sources

[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
