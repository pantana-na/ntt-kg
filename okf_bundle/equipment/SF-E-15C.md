---
type: Equipment Concept
title: SF-E-15C — Spent Fuel Pool Heat Exchanger C (Safety Class 3, Abandoned / Isolated)
description: Third Spent Fuel Pool cooling heat exchanger (Safety Class 3) originally
  installed for Alternate Spent Fuel Pool Cooling (ASFPC). Under License Renewal scope,
  SF-E-15C is isolated and drained, with SW service water supply/return lines permanently
  blind flanged and disconnected under the Equipment to be Abandoned Program.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SF-E-15C.md
tags:
- equipment
- heat exchanger
- sf
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-3.pdf
  title: ML101620329-part-3.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-11-05T14:33:16Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:33:16Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:33:16Z'
status: stable
entity_metadata:
  tag: SF-E-15C
  name: Spent Fuel Pool Heat Exchanger C (Safety Class 3, Abandoned / Isolated)
  equipment_class: Heat Exchanger
  unit: SF
  instruments:
  - tag: FISL 8298
    service: ASFPC Service Water Low Flow Interlock
    type: Flow Indicating Switch Low
    location: 12" SW Return Line [5-D]
    setpoint_or_range: —
    interlock_or_alarm: Non-functional / isolated with piping spool
    source: PID-1-SW-LR20796
  - tag: TW 8296
    service: SW Supply Temperature Measurement
    type: Temperature Well
    location: 12" SW Supply Line [6-F]
    setpoint_or_range: —
    interlock_or_alarm: Local thermowell
    source: PID-1-SW-LR20796
  - tag: TW 8297
    service: SW Return Temperature Measurement
    type: Temperature Well
    location: 12" SW Return Line [5-D]
    setpoint_or_range: —
    interlock_or_alarm: Local thermowell
    source: PID-1-SW-LR20796
  connections:
  - stream_id: SW-SUP-SF-E-15C
    direction: INLET
    source_tag: SW-COOLING-TOWER-SUP
    target_tag: SF-E-15C
    line_size: 12"
    inline_components:
    - V207 (12" Blind Flange / Manual Gate)
    - V208 (12" Blind Flange / Manual Gate)
    - TW 8296 (Thermowell)
    - V212 (High Point Vent)
    temperature: Ambient
    pressure: Drained (Air/Gas internal environment)
    flow_rate: 0 gpm (Isolated/Drained)
    description: 12" Service water supply line from Cooling Tower (isolated and blanked
      per LR Note 1 & Note 3)
    source: PID-1-SW-LR20796 (Grid 6-G/F)
  - stream_id: SW-RET-SF-E-15C
    direction: OUTLET
    source_tag: SF-E-15C
    target_tag: SW-COOLING-TOWER-RET
    line_size: 12"
    inline_components:
    - V206 (12" Blind Flange / Manual Gate)
    - V205 (12" Blind Flange / Manual Gate)
    - TW 8297 (Thermowell)
    - FISL 8298 (Flow Switch Low)
    - V214 (Thermal Relief Valve)
    temperature: Ambient
    pressure: Drained (Air/Gas internal environment)
    flow_rate: 0 gpm (Isolated/Drained)
    description: 12" Service water return line to Cooling Tower (isolated and blanked
      per LR Note 1 & Note 3)
    source: PID-1-SW-LR20796 (Grid 6-D..5-D)
  - stream_id: SW-REL-SF-E-15C
    direction: RELIEF
    source_tag: SF-E-15C
    target_tag: DRAIN-HUB
    line_size: 2"
    inline_components:
    - V214 (Thermal Relief Valve, SET @ 150 PSIG)
    temperature: Ambient
    pressure: 150 PSIG setpoint
    flow_rate: —
    description: Tube side thermal relief valve V214 discharging to open drain DR
    source: PID-1-SW-LR20796 (Grid 6-D)
  - stream_id: SF-IN-SF-E-15C
    direction: INLET
    source_tag: SF-V179-SFP-SYS
    target_tag: SF-E-15C
    line_size: 8" (10" Reducer at nozzle)
    inline_components:
    - SF-V181 (8" Gate Valve)
    - SF-V183 (Thermal Relief Valve, SET @ 150 PSIG)
    temperature: Ambient
    pressure: Drained
    flow_rate: 0 gpm (Isolated/Drained)
    description: Shell side process inlet from Spent Fuel Pool cooling system (Dwg
      20482 [D-5])
    source: PID-1-SW-LR20796 (Grid 4-F) / Dwg 20482
  - stream_id: SF-OUT-SF-E-15C
    direction: OUTLET
    source_tag: SF-E-15C
    target_tag: SPENT-FUEL-POOL
    line_size: 8" (10" to 8" Reducer)
    inline_components:
    - SF-V180 (8" Gate Valve)
    - Drains to WLD DR 132 (SF-V184, SF-V185, SF-V186)
    temperature: Ambient
    pressure: Drained
    flow_rate: 0 gpm (Isolated/Drained)
    description: Shell side process outlet to Spent Fuel Pool return (Dwg 20482 [C-9])
    source: PID-1-SW-LR20796 (Grid 4-E) / Dwg 20482
---

# SF-E-15C — Spent Fuel Pool Heat Exchanger C (Safety Class 3, Abandoned / Isolated)

## Function

Third Spent Fuel Pool cooling heat exchanger (Safety Class 3) originally installed for Alternate Spent Fuel Pool Cooling (ASFPC). Under License Renewal scope, SF-E-15C is isolated and drained, with SW service water supply/return lines permanently blind flanged and disconnected under the Equipment to be Abandoned Program.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Equipment Tag | SF-E-15C (Sheet 5 Grid 6-E) | — | PID-1-SW-LR20796 |
| Nuclear Safety Classification | Safety Class 3 (Nuclear Safety Related) (Sheet 5 Grid 6-E) | — | PID-1-SW-LR20796 |
| License Renewal AMR Status | Not in Scope for License Renewal (Out of Scope / Abandoned) (LR Note 1 & Note 5 (Black line color coding)) | — | PID-1-SW-LR20796 |
| Operational Status | Isolated and drained; SW piping removed as ASFPC is no longer required (LR Note 1) | — | PID-1-SW-LR20796 |
| Isolation & Flange Status | Blind flanges installed on both ends of underground lines; cooling tower flanges blanked (LR Note 2 & Note 3) | — | PID-1-SW-LR20796 |
| Thermal Relief Valve Setpoints | 150 PSIG (Valve V214, 2") & 150 PSIG (Valve SF-V183, 1") (Grid 6-D & 5-F) | PSIG | PID-1-SW-LR20796 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Operating Status | Drained and Isolated (Internal environment Air/Gas per LR Note 5) | — | PID-1-SW-LR20796 |
| Physical Location | Fuel Storage Building (Grid 6-E) | — | PID-1-SW-LR20796 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [FISL 8298](/instruments/le-2384-1.md) | ASFPC Service Water Low Flow Interlock | Flow Indicating Switch Low | 12" SW Return Line [5-D] | — | Non-functional / isolated with piping spool | PID-1-SW-LR20796 |
| [TW 8296](/instruments/le-2384-1.md) | SW Supply Temperature Measurement | Temperature Well | 12" SW Supply Line [6-F] | — | Local thermowell | PID-1-SW-LR20796 |
| [TW 8297](/instruments/le-2384-1.md) | SW Return Temperature Measurement | Temperature Well | 12" SW Return Line [5-D] | — | Local thermowell | PID-1-SW-LR20796 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SW-SUP-SF-E-15C | INLET | SW-COOLING-TOWER-SUP | SF-E-15C | 12" | V207 (12" Blind Flange / Manual Gate), V208 (12" Blind Flange / Manual Gate), TW 8296 (Thermowell), V212 (High Point Vent) | Ambient | Drained (Air/Gas internal environment) | 0 gpm (Isolated/Drained) | 12" Service water supply line from Cooling Tower (isolated and blanked per LR Note 1 & Note 3) |
| SW-RET-SF-E-15C | OUTLET | SF-E-15C | SW-COOLING-TOWER-RET | 12" | V206 (12" Blind Flange / Manual Gate), V205 (12" Blind Flange / Manual Gate), TW 8297 (Thermowell), FISL 8298 (Flow Switch Low), V214 (Thermal Relief Valve) | Ambient | Drained (Air/Gas internal environment) | 0 gpm (Isolated/Drained) | 12" Service water return line to Cooling Tower (isolated and blanked per LR Note 1 & Note 3) |
| SW-REL-SF-E-15C | RELIEF | SF-E-15C | DRAIN-HUB | 2" | V214 (Thermal Relief Valve, SET @ 150 PSIG) | Ambient | 150 PSIG setpoint | — | Tube side thermal relief valve V214 discharging to open drain DR |
| SF-IN-SF-E-15C | INLET | SF-V179-SFP-SYS | SF-E-15C | 8" (10" Reducer at nozzle) | SF-V181 (8" Gate Valve), SF-V183 (Thermal Relief Valve, SET @ 150 PSIG) | Ambient | Drained | 0 gpm (Isolated/Drained) | Shell side process inlet from Spent Fuel Pool cooling system (Dwg 20482 [D-5]) |
| SF-OUT-SF-E-15C | OUTLET | SF-E-15C | SPENT-FUEL-POOL | 8" (10" to 8" Reducer) | SF-V180 (8" Gate Valve), Drains to WLD DR 132 (SF-V184, SF-V185, SF-V186) | Ambient | Drained | 0 gpm (Isolated/Drained) | Shell side process outlet to Spent Fuel Pool return (Dwg 20482 [C-9]) |

## Hazards & Safeguards

- Equipment is retired in place / abandoned under plant administrative controls; must remain drained with blind flanges installed per LR Notes 1–5.
- Thermal expansion relief valves V214 (SW side) and SF-V183 (SF side) both set at 150 PSIG prevent overpressurization if trapped fluid expands.

## References & Sources

[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
