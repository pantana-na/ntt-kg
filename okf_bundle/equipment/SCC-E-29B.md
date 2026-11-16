---
type: Equipment Concept
title: SCC-E-29B — Secondary Component Cooling Water Heat Exchanger B
description: Secondary component cooling water heat exchanger for Train B, located
  in the Turbine Building, cooled by Nuclear Service Water to remove heat from conventional
  turbine-generator auxiliary cooling loops.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SCC-E-29B.md
tags:
- equipment
- heat exchanger
- scc
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-3.pdf
  title: ML101620329-part-3.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-11-05T14:31:57Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:31:57Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:31:57Z'
status: stable
entity_metadata:
  tag: SCC-E-29B
  name: Secondary Component Cooling Water Heat Exchanger B
  equipment_class: Heat Exchanger
  unit: SCC
  instruments:
  - tag: PDIS 6146
    service: SCC-E-29B Differential Pressure
    type: Differential Pressure Indicating Switch
    location: Across SCC-E-29B Inlet vs Outlet [8-G/H]
    setpoint_or_range: —
    interlock_or_alarm: High DP fouling alarm across heat exchanger
    source: PID-1-SW-LR20795
  - tag: V500
    service: PDIS 6146 Sensing Isolation
    type: Isolation Valve
    location: SCC-E-29B DP Sensing Line [8-G/H]
    setpoint_or_range: 3/4"
    interlock_or_alarm: DP sensing line isolation
    source: PID-1-SW-LR20795
  connections:
  - stream_id: SW-IN-SCC-E-29B
    direction: INLET
    source_tag: SW-TB-HDR-20
    target_tag: SCC-E-29B
    line_size: 16"
    inline_components:
    - V6 (Manual Gate Valve)
    - DP Sensing Tap
    temperature: Seawater supply temp
    pressure: —
    flow_rate: —
    description: Turbine Building 20" service water supply header branch into SCC-E-29B
      inlet
    source: PID-1-SW-LR20795 (Grid 9-G)
  - stream_id: SW-OUT-SCC-E-29B
    direction: OUTLET
    source_tag: SCC-E-29B
    target_tag: SW-TB-RET-20
    line_size: 16"
    inline_components:
    - V8 (Check Valve)
    - V501 (Manual Gate Valve)
    - FO 6140 (Fail-Open Flow Valve)
    - FO 6141 (Fail-Open Flow Valve)
    - DP Sensing Tap
    temperature: Warm seawater return
    pressure: —
    flow_rate: —
    description: 16" Service water discharge from SCC-E-29B through check valve V8
      and control valves FO 6140/6141 to return header
    source: PID-1-SW-LR20795 (Grid 8-H..6-G)
  - stream_id: SW-REL-SCC-E-29B
    direction: RELIEF
    source_tag: SCC-E-29B
    target_tag: TURBINE-BLDG-DRAIN
    line_size: 2"
    inline_components:
    - V502 (Relief Valve, SET PRESS. @ 150 PSIG)
    - V503 (Relief Valve, SET PRESS. @ 150 PSIG)
    temperature: Ambient
    pressure: 150 PSIG setpoint
    flow_rate: —
    description: Inlet header overpressure thermal relief valves discharging to drainage/sump
    source: PID-1-SW-LR20795 (Grid 8-H)
  - stream_id: SW-DR-SCC-E-29B
    direction: DRAIN
    source_tag: SCC-E-29B
    target_tag: TURBINE-BLDG-DRAIN
    line_size: 1" / 3/4"
    inline_components:
    - V504 (Shell Drain Valve)
    - V505 (Shell Drain Valve)
    - V506 (Inlet Drain Valve)
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Shell and channel head drains to floor drain
    source: PID-1-SW-LR20795 (Grid 7-G / 8-G)
---

# SCC-E-29B — Secondary Component Cooling Water Heat Exchanger B

## Function

Secondary component cooling water heat exchanger for Train B, located in the Turbine Building, cooled by Nuclear Service Water to remove heat from conventional turbine-generator auxiliary cooling loops.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Equipment Tag | SCC-E-29B (1-SCC-E-29B) (General Note 2 & Sheet 4 Grid 6-8, G-H) | — | PID-1-SW-LR20795 |
| Nuclear Safety Classification | Safety Class NNS (Non-Nuclear Safety) (Turbine Building service) | — | PID-1-SW-LR20795 |
| License Renewal AMR Status | In Scope (AMR) per 10 CFR 54.4(a)(2) (Green line color coding per 10 CFR 54.21) | — | PID-1-SW-LR20795 |
| Inlet / Outlet SW Line Size | 16" / 16" (Grid 9-G / 8-H) | inches | PID-1-SW-LR20795 |
| Thermal Relief Valve Setpoints | 150 (Valves V502 & V503, 2") (Grid 8-H) | PSIG | PID-1-SW-LR20795 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Cooling Medium | Service Water (Raw Seawater) | — | PID-1-SW-LR20795 |
| Process Medium | Secondary Component Cooling Water | — | PID-1-SW-LR20795 |
| Physical Location | Turbine Building [6-8, G-H] | — | PID-1-SW-LR20795 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PDIS 6146](/instruments/le-2384-1.md) | SCC-E-29B Differential Pressure | Differential Pressure Indicating Switch | Across SCC-E-29B Inlet vs Outlet [8-G/H] | — | High DP fouling alarm across heat exchanger | PID-1-SW-LR20795 |
| [V500](/instruments/le-2384-1.md) | PDIS 6146 Sensing Isolation | Isolation Valve | SCC-E-29B DP Sensing Line [8-G/H] | 3/4" | DP sensing line isolation | PID-1-SW-LR20795 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SW-IN-SCC-E-29B | INLET | SW-TB-HDR-20 | SCC-E-29B | 16" | V6 (Manual Gate Valve), DP Sensing Tap | Seawater supply temp | — | — | Turbine Building 20" service water supply header branch into SCC-E-29B inlet |
| SW-OUT-SCC-E-29B | OUTLET | SCC-E-29B | SW-TB-RET-20 | 16" | V8 (Check Valve), V501 (Manual Gate Valve), FO 6140 (Fail-Open Flow Valve), FO 6141 (Fail-Open Flow Valve), DP Sensing Tap | Warm seawater return | — | — | 16" Service water discharge from SCC-E-29B through check valve V8 and control valves FO 6140/6141 to return header |
| SW-REL-SCC-E-29B | RELIEF | SCC-E-29B | TURBINE-BLDG-DRAIN | 2" | V502 (Relief Valve, SET PRESS. @ 150 PSIG), V503 (Relief Valve, SET PRESS. @ 150 PSIG) | Ambient | 150 PSIG setpoint | — | Inlet header overpressure thermal relief valves discharging to drainage/sump |
| SW-DR-SCC-E-29B | DRAIN | SCC-E-29B | TURBINE-BLDG-DRAIN | 1" / 3/4" | V504 (Shell Drain Valve), V505 (Shell Drain Valve), V506 (Inlet Drain Valve) | Ambient | Atmospheric | — | Shell and channel head drains to floor drain |

## Hazards & Safeguards

- High differential pressure fouling from seawater suspended solids monitored across heat exchanger by PDIS 6146.
- Thermal overpressurization under isolated conditions mitigated by dual 2" relief valves V502 and V503 set at 150 PSIG.

## References & Sources

[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
