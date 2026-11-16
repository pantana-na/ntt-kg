---
type: Equipment Concept
title: DG-E-42A — Diesel Generator 1A Water Jacket Heat Exchanger
description: Nuclear safety-related water jacket heat exchanger for Emergency Diesel
  Generator 1A (Train A), cooled by Service Water Train B, providing engine cooling
  during emergency loss of offsite power or safety injection actuation. Controlled
  by fail-open valve FO 8291 upon DG-1A start command.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/DG-E-42A.md
tags:
- dg
- equipment
- heat exchanger
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-3.pdf
  title: ML101620329-part-3.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-11-05T14:31:10Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:31:10Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:31:10Z'
status: stable
entity_metadata:
  tag: DG-E-42A
  name: Diesel Generator 1A Water Jacket Heat Exchanger
  equipment_class: Heat Exchanger
  unit: DG
  instruments:
  - tag: FO 8291
    service: Emergency Cooling Water Flow Initiation
    type: Flow Control Valve / Solenoid Valve
    location: DG-E-42A SW Discharge Line [7-B]
    setpoint_or_range: Fail Open
    interlock_or_alarm: Fail Open (FO); opens automatically on OPEN CMD FROM DG-1A
      (Reference B)
    source: PID-1-SW-LR20795
  - tag: TI 6180
    service: Diesel Jacket Cooling Water Discharge Temp
    type: Temperature Indicator
    location: DG-E-42A Discharge Line [7-B]
    setpoint_or_range: —
    interlock_or_alarm: Local discharge temperature indication
    source: PID-1-SW-LR20795
  - tag: FE 6181 / FI 6181
    service: Diesel Jacket Cooling Water Flow Rate
    type: Flow Element & Indicator
    location: DG-E-42A Discharge Line [7-B]
    setpoint_or_range: —
    interlock_or_alarm: Local discharge flow measurement
    source: PID-1-SW-LR20795
  - tag: FG 9562
    service: Drain Flow Visual Observation
    type: Sight Flow Glass
    location: DG-E-42A Drain / Cooling Line [7-A/B]
    setpoint_or_range: —
    interlock_or_alarm: Visual cooling / drain flow confirmation
    source: PID-1-SW-LR20795
  connections:
  - stream_id: SW-IN-DG-E-42A
    direction: INLET
    source_tag: SW-PAB-TRAIN-B
    target_tag: DG-E-42A
    line_size: 10" / 16"
    inline_components:
    - V13 (Locked Open Gate Valve)
    - 10"x16" Expander
    - V514A (Thermal Relief Valve)
    temperature: Seawater supply temp
    pressure: —
    flow_rate: —
    description: Train B 24" service water supply via 10" branch and locked open gate
      valve V13
    source: PID-1-SW-LR20795 (Grid 10-B..8-B)
  - stream_id: SW-OUT-DG-E-42A
    direction: OUTLET
    source_tag: DG-E-42A
    target_tag: SW-RET-HDR
    line_size: 16"
    inline_components:
    - V16 (Check Valve)
    - FO 8291 (Fail-Open Control Valve, Open Cmd from DG-1A)
    - FE 6181 (Flow Element)
    - TI 6180 (Temperature Indicator)
    temperature: Monitored by TI 6180
    pressure: —
    flow_rate: Monitored by FE 6181 / FI 6181
    description: 16" Service water discharge through check valve V16 and fail-open
      control valve FO 8291 to Train B SW return header
    source: PID-1-SW-LR20795 (Grid 8-B..7-B)
  - stream_id: SW-REL-DG-E-42A
    direction: RELIEF
    source_tag: DG-E-42A
    target_tag: LOCAL-DRAIN-HUB
    line_size: 3/4"
    inline_components:
    - V514A (Relief Valve, SET @ 145 PSIG)
    temperature: Ambient
    pressure: 145 PSIG setpoint
    flow_rate: —
    description: Cooling water inlet thermal relief valve V514A discharging to local
      drain hub
    source: PID-1-SW-LR20795 (Grid 9-B)
  - stream_id: SW-DR-DG-E-42A
    direction: DRAIN
    source_tag: DG-E-42A
    target_tag: DG-DRAIN-HEADER
    line_size: 2"
    inline_components:
    - V176 (Drain Valve)
    - V188 (Drain Valve)
    - V515 (Drain Valve)
    - V516 (Drain Valve)
    - FG 9562 (Sight Flow Glass)
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Heat exchanger shell/tube drains with sight flow glass FG 9562/9563/9564
    source: PID-1-SW-LR20795 (Grid 8-B / 10-A/B / 7-A/B)
---

# DG-E-42A — Diesel Generator 1A Water Jacket Heat Exchanger

## Function

Nuclear safety-related water jacket heat exchanger for Emergency Diesel Generator 1A (Train A), cooled by Service Water Train B, providing engine cooling during emergency loss of offsite power or safety injection actuation. Controlled by fail-open valve FO 8291 upon DG-1A start command.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Equipment Tag | DG-E-42A (1-DG-E-42A) (General Note 2 & Sheet 4 Grid 7-8, A-B) | — | PID-1-SW-LR20795 |
| Nuclear Safety Classification | Nuclear Safety Related (Category 1) (Drawing Title Block) | — | PID-1-SW-LR20795 |
| License Renewal AMR Status | In Scope (AMR) per 10 CFR 54.4(a)(1) / (a)(3) (Red line color coding per 10 CFR 54.21) | — | PID-1-SW-LR20795 |
| Inlet / Outlet SW Line Size | 10" / 16" (Inlet), 16" (Discharge) (Grid 10-B / 7-B) | inches | PID-1-SW-LR20795 |
| Thermal Relief Valve Setpoint | 145 (Valve V514A, 3/4") (Grid 9-B) | PSIG | PID-1-SW-LR20795 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Cooling Water Medium | Service Water (Train B Seawater) | — | PID-1-SW-LR20795 |
| Engine Side Medium | Treated Diesel Engine Jacket Water | — | PID-1-SW-LR20795 |
| Operating Mode | Standby / Emergency Operation on EDG 1A Start | — | PID-1-SW-LR20795 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [FO 8291](/instruments/le-2384-1.md) | Emergency Cooling Water Flow Initiation | Flow Control Valve / Solenoid Valve | DG-E-42A SW Discharge Line [7-B] | Fail Open | Fail Open (FO); opens automatically on OPEN CMD FROM DG-1A (Reference B) | PID-1-SW-LR20795 |
| [TI 6180](/instruments/le-2384-1.md) | Diesel Jacket Cooling Water Discharge Temp | Temperature Indicator | DG-E-42A Discharge Line [7-B] | — | Local discharge temperature indication | PID-1-SW-LR20795 |
| [FE 6181 / FI 6181](/instruments/le-2384-1.md) | Diesel Jacket Cooling Water Flow Rate | Flow Element & Indicator | DG-E-42A Discharge Line [7-B] | — | Local discharge flow measurement | PID-1-SW-LR20795 |
| [FG 9562](/instruments/le-2384-1.md) | Drain Flow Visual Observation | Sight Flow Glass | DG-E-42A Drain / Cooling Line [7-A/B] | — | Visual cooling / drain flow confirmation | PID-1-SW-LR20795 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SW-IN-DG-E-42A | INLET | SW-PAB-TRAIN-B | DG-E-42A | 10" / 16" | V13 (Locked Open Gate Valve), 10"x16" Expander, V514A (Thermal Relief Valve) | Seawater supply temp | — | — | Train B 24" service water supply via 10" branch and locked open gate valve V13 |
| SW-OUT-DG-E-42A | OUTLET | DG-E-42A | SW-RET-HDR | 16" | V16 (Check Valve), FO 8291 (Fail-Open Control Valve, Open Cmd from DG-1A), FE 6181 (Flow Element), TI 6180 (Temperature Indicator) | Monitored by TI 6180 | — | Monitored by FE 6181 / FI 6181 | 16" Service water discharge through check valve V16 and fail-open control valve FO 8291 to Train B SW return header |
| SW-REL-DG-E-42A | RELIEF | DG-E-42A | LOCAL-DRAIN-HUB | 3/4" | V514A (Relief Valve, SET @ 145 PSIG) | Ambient | 145 PSIG setpoint | — | Cooling water inlet thermal relief valve V514A discharging to local drain hub |
| SW-DR-DG-E-42A | DRAIN | DG-E-42A | DG-DRAIN-HEADER | 2" | V176 (Drain Valve), V188 (Drain Valve), V515 (Drain Valve), V516 (Drain Valve), FG 9562 (Sight Flow Glass) | Ambient | Atmospheric | — | Heat exchanger shell/tube drains with sight flow glass FG 9562/9563/9564 |

## Hazards & Safeguards

- Failure of cooling water flow upon diesel engine start causes rapid overheating; mitigated by fail-open control valve FO 8291 receiving automatic open command from DG-1A start logic (Reference B).
- Thermal expansion overpressurization when isolated mitigated by relief valve V514A set at 145 PSIG.

## References & Sources

[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
