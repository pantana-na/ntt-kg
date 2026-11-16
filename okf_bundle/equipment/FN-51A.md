---
type: Equipment Concept
title: FN-51A — Service Water Cooling Tower Fan 51A
description: Induced-draft nuclear safety-related cooling tower fan for Service Water
  Cooling Tower Cell A, drawing air through the spray nozzle fill pack to reject decay
  heat from the Nuclear Service Water System to the atmosphere during Ultimate Heat
  Sink operation.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/FN-51A.md
tags:
- equipment
- fan
- sw
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-3.pdf
  title: ML101620329-part-3.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-11-05T14:33:31Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:33:31Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:33:31Z'
status: stable
entity_metadata:
  tag: FN-51A
  name: Service Water Cooling Tower Fan 51A
  equipment_class: Fan
  unit: SW
  instruments:
  - tag: PSL-8287
    service: FN-51A Gearbox Oil Pressure Low
    type: Pressure Switch Low
    location: Fan Drive Unit FN-51A [11-D]
    setpoint_or_range: —
    interlock_or_alarm: Low gearbox lube oil pressure alarm
    source: PID-1-SW-LR20794
  - tag: TE-8286
    service: FN-51A Gearbox Oil Temperature
    type: Temperature Element
    location: Fan Drive Unit FN-51A [11-D]
    setpoint_or_range: —
    interlock_or_alarm: High gearbox oil/bearing temperature alarm
    source: PID-1-SW-LR20794
  - tag: LT-6139
    service: FN-51A Gearbox Oil Level
    type: Level Transmitter
    location: Fan Gearbox Sump [8-D]
    setpoint_or_range: —
    interlock_or_alarm: Remote oil level monitoring
    source: PID-1-SW-LR20794
  - tag: LG-6116A
    service: FN-51A Gearbox Oil Level Sight Glass
    type: Level Gauge Glass
    location: Gearbox Assembly Detail C [11-F]
    setpoint_or_range: —
    interlock_or_alarm: Local sight glass level verification
    source: PID-1-SW-LR20794 (Detail C)
  connections:
  - stream_id: SW-AIR-IN-FN51A
    direction: INLET
    source_tag: ATMOSPHERE
    target_tag: FN-51A
    line_size: Tower Cell Intake
    inline_components:
    - Fan Shroud / Intake
    temperature: Ambient wet-bulb temp
    pressure: Atmospheric
    flow_rate: Induced draft cooling airflow
    description: Ambient air inducted across Cooling Tower fill and spray header nozzles
    source: PID-1-SW-LR20794 (Grid 11-D)
  - stream_id: SW-AIR-OUT-FN51A
    direction: OUTLET
    source_tag: FN-51A
    target_tag: ATMOSPHERE
    line_size: Fan Stack Diameter
    inline_components:
    - Fan Stack
    temperature: Plume temperature
    pressure: Atmospheric
    flow_rate: Induced draft exhaust
    description: Moist air discharged vertically out of cooling tower fan stack
    source: PID-1-SW-LR20794 (Grid 11-D)
  - stream_id: SW-DR-FN51A-OIL
    direction: DRAIN
    source_tag: FN-51A
    target_tag: LUBE-OIL-COLLECTION
    line_size: 3/4" / 1-1/4"
    inline_components:
    - V230 (1-SW-V230 Isolation Valve)
    - LG-6116A (Level Sight Glass)
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Fan gearbox lube oil sump drain line
    source: PID-1-SW-LR20794 (Detail C & Grid 11-F)
---

# FN-51A — Service Water Cooling Tower Fan 51A

## Function

Induced-draft nuclear safety-related cooling tower fan for Service Water Cooling Tower Cell A, drawing air through the spray nozzle fill pack to reject decay heat from the Nuclear Service Water System to the atmosphere during Ultimate Heat Sink operation.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Equipment Tag | 1-SW-FN-51A (General Note 2 & Sheet 3 Grid 11-D) | — | PID-1-SW-LR20794 |
| Nuclear Safety Classification | Nuclear Safety Related (Category 1) (Drawing Title Block) | — | PID-1-SW-LR20794 |
| License Renewal AMR Status | In Scope (AMR) per 10 CFR 54.4(a)(1) / (a)(3) (Red line color coding per 10 CFR 54.21) | — | PID-1-SW-LR20794 |
| Gearbox Lubrication Monitoring | Gearbox with 1-1/4" lower isolation valve V230, breather cap, level gauge LG-6116A, 3/4" drain (Sheet 3 Detail C) | — | PID-1-SW-LR20794 |
| Unit 2 Association | Unit 2 counterpart 2-SW-FN-51A is abandoned and non-functional per LR Note 6 (LR Note 6 comparison) | — | PID-1-SW-LR20794 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Fan Service | Induced Draft Cooling Tower Fan | — | PID-1-SW-LR20794 |
| Location | Service Water Cooling Tower Fan Deck [11-D] | — | PID-1-SW-LR20794 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PSL-8287](/instruments/le-2384-1.md) | FN-51A Gearbox Oil Pressure Low | Pressure Switch Low | Fan Drive Unit FN-51A [11-D] | — | Low gearbox lube oil pressure alarm | PID-1-SW-LR20794 |
| [TE-8286](/instruments/le-2384-1.md) | FN-51A Gearbox Oil Temperature | Temperature Element | Fan Drive Unit FN-51A [11-D] | — | High gearbox oil/bearing temperature alarm | PID-1-SW-LR20794 |
| [LT-6139](/instruments/le-2384-1.md) | FN-51A Gearbox Oil Level | Level Transmitter | Fan Gearbox Sump [8-D] | — | Remote oil level monitoring | PID-1-SW-LR20794 |
| [LG-6116A](/instruments/le-2384-1.md) | FN-51A Gearbox Oil Level Sight Glass | Level Gauge Glass | Gearbox Assembly Detail C [11-F] | — | Local sight glass level verification | PID-1-SW-LR20794 (Detail C) |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SW-AIR-IN-FN51A | INLET | ATMOSPHERE | FN-51A | Tower Cell Intake | Fan Shroud / Intake | Ambient wet-bulb temp | Atmospheric | Induced draft cooling airflow | Ambient air inducted across Cooling Tower fill and spray header nozzles |
| SW-AIR-OUT-FN51A | OUTLET | FN-51A | ATMOSPHERE | Fan Stack Diameter | Fan Stack | Plume temperature | Atmospheric | Induced draft exhaust | Moist air discharged vertically out of cooling tower fan stack |
| SW-DR-FN51A-OIL | DRAIN | FN-51A | LUBE-OIL-COLLECTION | 3/4" / 1-1/4" | V230 (1-SW-V230 Isolation Valve), LG-6116A (Level Sight Glass) | Ambient | Atmospheric | — | Fan gearbox lube oil sump drain line |

## Hazards & Safeguards

- Gearbox loss of lubrication or low oil pressure causes bearing seizure; monitored by pressure switch PSL-8287 and level transmitter LT-6139.
- Gearbox high bearing/oil temperature monitored by temperature element TE-8286.

## References & Sources

[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
