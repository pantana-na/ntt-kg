---
type: Equipment Concept
title: FN-51B — Service Water Cooling Tower Fan 51B
description: Induced-draft nuclear safety-related cooling tower fan for Service Water
  Cooling Tower Cell B, drawing air through the spray nozzle fill pack to reject decay
  heat from the Nuclear Service Water System to the atmosphere during Ultimate Heat
  Sink operation.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/FN-51B.md
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
  at: '2026-11-05T14:33:43Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:33:43Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:33:43Z'
status: stable
entity_metadata:
  tag: FN-51B
  name: Service Water Cooling Tower Fan 51B
  equipment_class: Fan
  unit: SW
  instruments:
  - tag: PSL-8288
    service: FN-51B Gearbox Oil Pressure Low
    type: Pressure Switch Low
    location: Fan Drive Unit FN-51B [10-D]
    setpoint_or_range: —
    interlock_or_alarm: Low gearbox lube oil pressure alarm
    source: PID-1-SW-LR20794
  - tag: LT-6139
    service: FN-51B Gearbox Oil Level
    type: Level Transmitter
    location: Fan Gearbox Sump [9-D]
    setpoint_or_range: —
    interlock_or_alarm: Remote oil level monitoring
    source: PID-1-SW-LR20794
  - tag: LG-6116B
    service: FN-51B Gearbox Oil Level Sight Glass
    type: Level Gauge Glass
    location: Gearbox Assembly Detail B [11-G]
    setpoint_or_range: —
    interlock_or_alarm: Local sight glass level verification
    source: PID-1-SW-LR20794 (Detail B)
  connections:
  - stream_id: SW-AIR-IN-FN51B
    direction: INLET
    source_tag: ATMOSPHERE
    target_tag: FN-51B
    line_size: Tower Cell Intake
    inline_components:
    - Fan Shroud / Intake
    temperature: Ambient wet-bulb temp
    pressure: Atmospheric
    flow_rate: Induced draft cooling airflow
    description: Ambient air inducted across Cooling Tower fill and spray header nozzles
    source: PID-1-SW-LR20794 (Grid 10-D)
  - stream_id: SW-AIR-OUT-FN51B
    direction: OUTLET
    source_tag: FN-51B
    target_tag: ATMOSPHERE
    line_size: Fan Stack Diameter
    inline_components:
    - Fan Stack
    temperature: Plume temperature
    pressure: Atmospheric
    flow_rate: Induced draft exhaust
    description: Moist air discharged vertically out of cooling tower fan stack
    source: PID-1-SW-LR20794 (Grid 10-D)
  - stream_id: SW-DR-FN51B-OIL
    direction: DRAIN
    source_tag: FN-51B
    target_tag: LUBE-OIL-COLLECTION
    line_size: 3/4" / 1-1/4"
    inline_components:
    - V231 (1-SW-V231 Isolation Valve)
    - LG-6116B (Level Sight Glass)
    - V232 (Drain Valve)
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Fan gearbox lube oil sump drain line
    source: PID-1-SW-LR20794 (Detail B & Grid 11-G)
---

# FN-51B — Service Water Cooling Tower Fan 51B

## Function

Induced-draft nuclear safety-related cooling tower fan for Service Water Cooling Tower Cell B, drawing air through the spray nozzle fill pack to reject decay heat from the Nuclear Service Water System to the atmosphere during Ultimate Heat Sink operation.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Equipment Tag | 1-SW-FN-51B (General Note 2 & Sheet 3 Grid 10-D) | — | PID-1-SW-LR20794 |
| Nuclear Safety Classification | Nuclear Safety Related (Category 1) (Drawing Title Block) | — | PID-1-SW-LR20794 |
| License Renewal AMR Status | In Scope (AMR) per 10 CFR 54.4(a)(1) / (a)(3) (Red line color coding per 10 CFR 54.21) | — | PID-1-SW-LR20794 |
| Gearbox Lubrication Monitoring | Gearbox with 1-1/4" isolation V231, breather cap, level gauge LG-6116B, drain V232 (Sheet 3 Detail B) | — | PID-1-SW-LR20794 |
| Unit 2 Cross-Tie Status | Unit 2 counterpart 2-SW-FN-51B is controlled from Unit 1 MCB and required for Unit 1 operation (LR Note 6) | — | PID-1-SW-LR20794 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Fan Service | Induced Draft Cooling Tower Fan | — | PID-1-SW-LR20794 |
| Location | Service Water Cooling Tower Fan Deck [10-D] | — | PID-1-SW-LR20794 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PSL-8288](/instruments/le-2384-1.md) | FN-51B Gearbox Oil Pressure Low | Pressure Switch Low | Fan Drive Unit FN-51B [10-D] | — | Low gearbox lube oil pressure alarm | PID-1-SW-LR20794 |
| [LT-6139](/instruments/le-2384-1.md) | FN-51B Gearbox Oil Level | Level Transmitter | Fan Gearbox Sump [9-D] | — | Remote oil level monitoring | PID-1-SW-LR20794 |
| [LG-6116B](/instruments/le-2384-1.md) | FN-51B Gearbox Oil Level Sight Glass | Level Gauge Glass | Gearbox Assembly Detail B [11-G] | — | Local sight glass level verification | PID-1-SW-LR20794 (Detail B) |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SW-AIR-IN-FN51B | INLET | ATMOSPHERE | FN-51B | Tower Cell Intake | Fan Shroud / Intake | Ambient wet-bulb temp | Atmospheric | Induced draft cooling airflow | Ambient air inducted across Cooling Tower fill and spray header nozzles |
| SW-AIR-OUT-FN51B | OUTLET | FN-51B | ATMOSPHERE | Fan Stack Diameter | Fan Stack | Plume temperature | Atmospheric | Induced draft exhaust | Moist air discharged vertically out of cooling tower fan stack |
| SW-DR-FN51B-OIL | DRAIN | FN-51B | LUBE-OIL-COLLECTION | 3/4" / 1-1/4" | V231 (1-SW-V231 Isolation Valve), LG-6116B (Level Sight Glass), V232 (Drain Valve) | Ambient | Atmospheric | — | Fan gearbox lube oil sump drain line |

## Hazards & Safeguards

- Gearbox loss of lubrication or low oil pressure causes bearing seizure; monitored by pressure switch PSL-8288 and level transmitter LT-6139.
- Gearbox high bearing/oil temperature monitored by local sensing.

## References & Sources

[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
