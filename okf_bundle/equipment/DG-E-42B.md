---
type: Equipment Concept
title: DG-E-42B — Diesel Generator 1B Water Jacket Heat Exchanger
description: Nuclear safety-related water jacket heat exchanger for Emergency Diesel
  Generator 1B (Train B), cooled by Service Water Train A, providing engine cooling
  during emergency loss of offsite power or safety injection actuation. Controlled
  by fail-open valve FO 8292 upon DG-1B start command.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/DG-E-42B.md
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
  at: '2026-11-05T14:31:28Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:31:28Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:31:28Z'
status: stable
entity_metadata:
  tag: DG-E-42B
  name: Diesel Generator 1B Water Jacket Heat Exchanger
  equipment_class: Heat Exchanger
  unit: DG
  instruments:
  - tag: FO 8292
    service: Emergency Cooling Water Flow Initiation
    type: Flow Control Valve / Solenoid Valve
    location: DG-E-42B SW Discharge Line [7-C]
    setpoint_or_range: Fail Open
    interlock_or_alarm: Fail Open (FO); opens automatically on OPEN CMD FROM DG-1B
      (Reference C)
    source: PID-1-SW-LR20795
  - tag: TI 6190
    service: Diesel Jacket Cooling Water Discharge Temp
    type: Temperature Indicator
    location: DG-E-42B Discharge Line [7-C]
    setpoint_or_range: —
    interlock_or_alarm: Local discharge temperature indication
    source: PID-1-SW-LR20795
  - tag: FE 6191 / FI 6191
    service: Diesel Jacket Cooling Water Flow Rate
    type: Flow Element & Indicator
    location: DG-E-42B Discharge Line [7-C]
    setpoint_or_range: —
    interlock_or_alarm: Local discharge flow measurement
    source: PID-1-SW-LR20795
  connections:
  - stream_id: SW-IN-DG-E-42B
    direction: INLET
    source_tag: SW-PAB-TRAIN-A
    target_tag: DG-E-42B
    line_size: 10" / 16"
    inline_components:
    - 10"x16" Expander
    - V514B (Thermal Relief Valve)
    temperature: Seawater supply temp
    pressure: —
    flow_rate: —
    description: Train A 24" service water supply via 10" branch and locked open valving
    source: PID-1-SW-LR20795 (Grid 10-C..8-C)
  - stream_id: SW-OUT-DG-E-42B
    direction: OUTLET
    source_tag: DG-E-42B
    target_tag: SW-RET-HDR
    line_size: 16"
    inline_components:
    - V18 (Check Valve)
    - FO 8292 (Fail-Open Control Valve, Open Cmd from DG-1B)
    - FE 6191 (Flow Element)
    - TI 6190 (Temperature Indicator)
    temperature: Monitored by TI 6190
    pressure: —
    flow_rate: Monitored by FE 6191 / FI 6191
    description: 16" Service water discharge through check valve V18 and fail-open
      control valve FO 8292 to Train A SW return header
    source: PID-1-SW-LR20795 (Grid 8-C..7-C)
  - stream_id: SW-REL-DG-E-42B
    direction: RELIEF
    source_tag: DG-E-42B
    target_tag: LOCAL-DRAIN-HUB
    line_size: 3/4"
    inline_components:
    - V514B (Relief Valve, SET @ 145 PSIG)
    temperature: Ambient
    pressure: 145 PSIG setpoint
    flow_rate: —
    description: Cooling water inlet thermal relief valve V514B discharging to local
      drain hub
    source: PID-1-SW-LR20795 (Grid 9-C)
  - stream_id: SW-DR-DG-E-42B
    direction: DRAIN
    source_tag: DG-E-42B
    target_tag: DG-DRAIN-HEADER
    line_size: 2"
    inline_components:
    - V176 (Drain Valve)
    - V517 (Drain Valve)
    - V518 (Drain Valve)
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Heat exchanger shell/tube drains with sight flow glass FG 9565
    source: PID-1-SW-LR20795 (Grid 8-B / 9-B/C / 7-C)
---

# DG-E-42B — Diesel Generator 1B Water Jacket Heat Exchanger

## Function

Nuclear safety-related water jacket heat exchanger for Emergency Diesel Generator 1B (Train B), cooled by Service Water Train A, providing engine cooling during emergency loss of offsite power or safety injection actuation. Controlled by fail-open valve FO 8292 upon DG-1B start command.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Equipment Tag | DG-E-42B (1-DG-E-42B) (General Note 2 & Sheet 4 Grid 7-8, B-C) | — | PID-1-SW-LR20795 |
| Nuclear Safety Classification | Nuclear Safety Related (Category 1) (Drawing Title Block) | — | PID-1-SW-LR20795 |
| License Renewal AMR Status | In Scope (AMR) per 10 CFR 54.4(a)(1) / (a)(3) (Red line color coding per 10 CFR 54.21) | — | PID-1-SW-LR20795 |
| Inlet / Outlet SW Line Size | 10" / 16" (Inlet), 16" (Discharge) (Grid 10-C / 7-C) | inches | PID-1-SW-LR20795 |
| Thermal Relief Valve Setpoint | 145 (Valve V514B, 3/4") (Grid 9-C) | PSIG | PID-1-SW-LR20795 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Cooling Water Medium | Service Water (Train A Seawater) | — | PID-1-SW-LR20795 |
| Engine Side Medium | Treated Diesel Engine Jacket Water | — | PID-1-SW-LR20795 |
| Operating Mode | Standby / Emergency Operation on EDG 1B Start | — | PID-1-SW-LR20795 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [FO 8292](/instruments/le-2384-1.md) | Emergency Cooling Water Flow Initiation | Flow Control Valve / Solenoid Valve | DG-E-42B SW Discharge Line [7-C] | Fail Open | Fail Open (FO); opens automatically on OPEN CMD FROM DG-1B (Reference C) | PID-1-SW-LR20795 |
| [TI 6190](/instruments/le-2384-1.md) | Diesel Jacket Cooling Water Discharge Temp | Temperature Indicator | DG-E-42B Discharge Line [7-C] | — | Local discharge temperature indication | PID-1-SW-LR20795 |
| [FE 6191 / FI 6191](/instruments/le-2384-1.md) | Diesel Jacket Cooling Water Flow Rate | Flow Element & Indicator | DG-E-42B Discharge Line [7-C] | — | Local discharge flow measurement | PID-1-SW-LR20795 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SW-IN-DG-E-42B | INLET | SW-PAB-TRAIN-A | DG-E-42B | 10" / 16" | 10"x16" Expander, V514B (Thermal Relief Valve) | Seawater supply temp | — | — | Train A 24" service water supply via 10" branch and locked open valving |
| SW-OUT-DG-E-42B | OUTLET | DG-E-42B | SW-RET-HDR | 16" | V18 (Check Valve), FO 8292 (Fail-Open Control Valve, Open Cmd from DG-1B), FE 6191 (Flow Element), TI 6190 (Temperature Indicator) | Monitored by TI 6190 | — | Monitored by FE 6191 / FI 6191 | 16" Service water discharge through check valve V18 and fail-open control valve FO 8292 to Train A SW return header |
| SW-REL-DG-E-42B | RELIEF | DG-E-42B | LOCAL-DRAIN-HUB | 3/4" | V514B (Relief Valve, SET @ 145 PSIG) | Ambient | 145 PSIG setpoint | — | Cooling water inlet thermal relief valve V514B discharging to local drain hub |
| SW-DR-DG-E-42B | DRAIN | DG-E-42B | DG-DRAIN-HEADER | 2" | V176 (Drain Valve), V517 (Drain Valve), V518 (Drain Valve) | Ambient | Atmospheric | — | Heat exchanger shell/tube drains with sight flow glass FG 9565 |

## Hazards & Safeguards

- Failure of cooling water flow upon diesel engine start causes rapid overheating; mitigated by fail-open control valve FO 8292 receiving automatic open command from DG-1B start logic (Reference C).
- Thermal expansion overpressurization when isolated mitigated by relief valve V514B set at 145 PSIG.

## References & Sources

[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
