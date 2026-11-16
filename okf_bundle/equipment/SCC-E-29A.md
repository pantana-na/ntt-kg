---
type: Equipment Concept
title: SCC-E-29A — Secondary Component Cooling Water Heat Exchanger A
description: Secondary component cooling water heat exchanger for Train A, located
  in the Turbine Building, cooled by Nuclear Service Water to remove heat from conventional
  turbine-generator auxiliary cooling loops.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SCC-E-29A.md
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
  at: '2026-11-05T14:31:45Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:31:45Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:31:45Z'
status: stable
entity_metadata:
  tag: SCC-E-29A
  name: Secondary Component Cooling Water Heat Exchanger A
  equipment_class: Heat Exchanger
  unit: SCC
  instruments:
  - tag: PDIS 6157
    service: SCC-E-29A Differential Pressure
    type: Differential Pressure Indicating Switch
    location: Across SCC-E-29A Inlet vs Outlet [8-F]
    setpoint_or_range: —
    interlock_or_alarm: High DP fouling alarm across heat exchanger
    source: PID-1-SW-LR20795
  - tag: V507
    service: PDIS 6157 Sensing Isolation
    type: Isolation Valve
    location: SCC-E-29A DP Sensing Line [8-F/G]
    setpoint_or_range: 3/4"
    interlock_or_alarm: DP sensing line isolation
    source: PID-1-SW-LR20795
  connections:
  - stream_id: SW-IN-SCC-E-29A
    direction: INLET
    source_tag: SW-TB-HDR-20
    target_tag: SCC-E-29A
    line_size: 16"
    inline_components:
    - V7 (Manual Gate Valve)
    - DP Sensing Tap
    temperature: Seawater supply temp
    pressure: —
    flow_rate: —
    description: Turbine Building 20" service water supply header branch into SCC-E-29A
      inlet
    source: PID-1-SW-LR20795 (Grid 9-F)
  - stream_id: SW-OUT-SCC-E-29A
    direction: OUTLET
    source_tag: SCC-E-29A
    target_tag: SW-TB-RET-20
    line_size: 16"
    inline_components:
    - V9 (Check Valve)
    - V508 (Manual Gate Valve)
    - DP Sensing Tap
    temperature: Warm seawater return
    pressure: —
    flow_rate: —
    description: 16" Service water discharge from SCC-E-29A to Turbine Building return
      header
    source: PID-1-SW-LR20795 (Grid 8-G)
  - stream_id: SW-REL-SCC-E-29A
    direction: RELIEF
    source_tag: SCC-E-29A
    target_tag: TURBINE-BLDG-DRAIN
    line_size: 2"
    inline_components:
    - V509 (Relief Valve, SET PRESS. @ 150 PSIG)
    - V510 (Relief Valve, SET PRESS. @ 150 PSIG)
    temperature: Ambient
    pressure: 150 PSIG setpoint
    flow_rate: —
    description: Inlet header overpressure thermal relief valves discharging to drainage/sump
    source: PID-1-SW-LR20795 (Grid 8-F/G)
  - stream_id: SW-DR-SCC-E-29A
    direction: DRAIN
    source_tag: SCC-E-29A
    target_tag: TURBINE-BLDG-DRAIN
    line_size: 1" / 3/4"
    inline_components:
    - V511 (Shell Drain Valve)
    - V512 (Shell Drain Valve)
    - V513 (Inlet Drain Valve)
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Shell and channel head drains to floor drain
    source: PID-1-SW-LR20795 (Grid 7-F / 8-F)
---

# SCC-E-29A — Secondary Component Cooling Water Heat Exchanger A

## Function

Secondary component cooling water heat exchanger for Train A, located in the Turbine Building, cooled by Nuclear Service Water to remove heat from conventional turbine-generator auxiliary cooling loops.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Equipment Tag | SCC-E-29A (1-SCC-E-29A) (General Note 2 & Sheet 4 Grid 6-8, F-G) | — | PID-1-SW-LR20795 |
| Nuclear Safety Classification | Safety Class NNS (Non-Nuclear Safety) (Turbine Building service) | — | PID-1-SW-LR20795 |
| License Renewal AMR Status | In Scope (AMR) per 10 CFR 54.4(a)(2) (Green line color coding per 10 CFR 54.21) | — | PID-1-SW-LR20795 |
| Inlet / Outlet SW Line Size | 16" / 16" (Grid 9-F / 8-G) | inches | PID-1-SW-LR20795 |
| Thermal Relief Valve Setpoints | 150 (Valves V509 & V510, 2") (Grid 8-F/G) | PSIG | PID-1-SW-LR20795 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Cooling Medium | Service Water (Raw Seawater) | — | PID-1-SW-LR20795 |
| Process Medium | Secondary Component Cooling Water | — | PID-1-SW-LR20795 |
| Physical Location | Turbine Building [6-8, F-G] | — | PID-1-SW-LR20795 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PDIS 6157](/instruments/le-2384-1.md) | SCC-E-29A Differential Pressure | Differential Pressure Indicating Switch | Across SCC-E-29A Inlet vs Outlet [8-F] | — | High DP fouling alarm across heat exchanger | PID-1-SW-LR20795 |
| [V507](/instruments/le-2384-1.md) | PDIS 6157 Sensing Isolation | Isolation Valve | SCC-E-29A DP Sensing Line [8-F/G] | 3/4" | DP sensing line isolation | PID-1-SW-LR20795 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SW-IN-SCC-E-29A | INLET | SW-TB-HDR-20 | SCC-E-29A | 16" | V7 (Manual Gate Valve), DP Sensing Tap | Seawater supply temp | — | — | Turbine Building 20" service water supply header branch into SCC-E-29A inlet |
| SW-OUT-SCC-E-29A | OUTLET | SCC-E-29A | SW-TB-RET-20 | 16" | V9 (Check Valve), V508 (Manual Gate Valve), DP Sensing Tap | Warm seawater return | — | — | 16" Service water discharge from SCC-E-29A to Turbine Building return header |
| SW-REL-SCC-E-29A | RELIEF | SCC-E-29A | TURBINE-BLDG-DRAIN | 2" | V509 (Relief Valve, SET PRESS. @ 150 PSIG), V510 (Relief Valve, SET PRESS. @ 150 PSIG) | Ambient | 150 PSIG setpoint | — | Inlet header overpressure thermal relief valves discharging to drainage/sump |
| SW-DR-SCC-E-29A | DRAIN | SCC-E-29A | TURBINE-BLDG-DRAIN | 1" / 3/4" | V511 (Shell Drain Valve), V512 (Shell Drain Valve), V513 (Inlet Drain Valve) | Ambient | Atmospheric | — | Shell and channel head drains to floor drain |

## Hazards & Safeguards

- High differential pressure fouling from seawater suspended solids monitored across heat exchanger by PDIS 6157.
- Thermal overpressurization under isolated conditions mitigated by dual 2" relief valves V509 and V510 set at 150 PSIG.

## References & Sources

[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
