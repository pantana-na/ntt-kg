---
type: Equipment Concept
title: CS-P-243B — Charging Pump CS-P-2B Lube Oil Pump
description: Auxiliary positive displacement lubrication oil pump for Charging / High
  Head Safety Injection Pump CS-P-2B, circulating lube oil from oil reservoir through
  oil cooler and bearings to maintain hydrodynamic bearing lubrication during normal
  and emergency injection service.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/CS-P-243B.md
tags:
- cs
- equipment
- pump
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-1.pdf
  title: ML101620329-part-1.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-11T01:57:28Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-11T01:57:28Z'
- by: process:okf-validation-suite
  at: '2026-10-11T01:57:28Z'
status: stable
entity_metadata:
  tag: CS-P-243B
  name: Charging Pump CS-P-2B Lube Oil Pump
  equipment_class: Pump
  unit: CS
  instruments:
  - tag: PI-7468-1
    service: Lube Oil Discharge Pressure (Local)
    type: Pressure Indicator
    location: Skid Mounted
    setpoint_or_range: Local gauge
    interlock_or_alarm: Local pressure indication
    source: PID-1-SI-LR20447
  - tag: PI-7468-2
    service: Lube Oil Bearing Header Pressure (Local)
    type: Pressure Indicator
    location: Skid Mounted
    setpoint_or_range: Local gauge
    interlock_or_alarm: Local pressure indication
    source: PID-1-SI-LR20447
  - tag: PS-7468
    service: Lube Oil Low Pressure Trip / Alarm
    type: Pressure Switch
    location: Skid Mounted
    setpoint_or_range: Low setpoint
    interlock_or_alarm: Trips pump CS-P-2B on loss of lubrication oil pressure
    source: PID-1-SI-LR20447
  - tag: TI-2588-1
    service: Lube Oil Reservoir Temperature
    type: Temperature Indicator
    location: Skid Mounted
    setpoint_or_range: Local gauge
    interlock_or_alarm: Oil reservoir temperature verification
    source: PID-1-SI-LR20447
  - tag: TI-2588-2
    service: Lube Oil Cooler Discharge Temperature
    type: Temperature Indicator
    location: Skid Mounted
    setpoint_or_range: Local gauge
    interlock_or_alarm: Bearing feed temperature monitoring
    source: PID-1-SI-LR20447
  connections:
  - stream_id: STR-LO-P243B-SUCT
    direction: INLET
    source_tag: OIL RESV'R (CS-P-2B)
    target_tag: CS-P-243B
    line_size: 1"
    inline_components:
    - Suction line
    temperature: Ambient to 140°F
    pressure: Static head
    flow_rate: —
    description: Lube oil pump suction from oil reservoir
    source: PID-1-SI-LR20447
  - stream_id: STR-LO-P243B-DISCH
    direction: OUTLET
    source_tag: CS-P-243B
    target_tag: OIL COOLER (CS-P-2B)
    line_size: 1"
    inline_components:
    - Sight Flow Indicator (LOF)
    temperature: Operating lube temp
    pressure: Lube oil operating pressure
    flow_rate: —
    description: Pump discharge through sight flow indicator LOF to shell/tube oil
      cooler
    source: PID-1-SI-LR20447
  - stream_id: STR-LO-P243B-COOLING
    direction: UTILITY
    source_tag: CCW LOOP B (20211 [B-5])
    target_tag: OIL COOLER (CS-P-2B)
    line_size: 1-1/2"
    inline_components:
    - Isolation valves
    temperature: CCW supply temp
    pressure: CCW operating pressure
    flow_rate: —
    description: CCW Loop B cooling water to lube oil cooler
    source: PID-1-SI-LR20447
  - stream_id: STR-LO-P243B-DRN
    direction: DRAIN
    source_tag: CS-P-243B Skid
    target_tag: WLD DR 191
    line_size: 1/2"x1"
    inline_components:
    - CS-V1217
    - CS-V609
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Skid drain and reservoir drain to waste liquid processing
    source: PID-1-SI-LR20447
---

# CS-P-243B — Charging Pump CS-P-2B Lube Oil Pump

## Function

Auxiliary positive displacement lubrication oil pump for Charging / High Head Safety Injection Pump CS-P-2B, circulating lube oil from oil reservoir through oil cooler and bearings to maintain hydrodynamic bearing lubrication during normal and emergency injection service.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20447 (Rev. 15, Ref. B20447) | — | PID-1-SI-LR20447 |
| Safety Classification | Safety Class 2 / Seismic Class A* (per Note 10) | — | PID-1-SI-LR20447 (Note 10) |
| Parent Equipment | Charging Pump CS-P-2B | — | PID-1-SI-LR20447 |
| Physical Location | Primary Auxiliary Building (Grid B-9 / B-10) | — | PID-1-SI-LR20447 |
| AMR Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20447 |
| Lube Oil Reservoir Drain Valve | CS-V1217 (1/2" line to DR 191) | — | PID-1-SI-LR20447 |
| Lube Oil Skid Drain Header | CS-V609 (1" line to DR 191) | — | PID-1-SI-LR20447 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Working Fluid | Turbine / Machinery Lubricating Oil | — | PID-1-SI-LR20447 |
| Cooling Medium | Component Cooling Water (CCW Loop B via 1-1/2" line) | — | PID-1-SI-LR20447 |
| Suction Source | CS-P-2B Oil Reservoir (OIL RESV'R) | — | PID-1-SI-LR20447 |
| Discharge Destination | CS-P-2B Gear Drive and Bearings via Oil Cooler | — | PID-1-SI-LR20447 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PI-7468-1](/instruments/PI-7468-1.md) | Lube Oil Discharge Pressure (Local) | Pressure Indicator | Skid Mounted | Local gauge | Local pressure indication | PID-1-SI-LR20447 |
| [PI-7468-2](/instruments/PI-7468-2.md) | Lube Oil Bearing Header Pressure (Local) | Pressure Indicator | Skid Mounted | Local gauge | Local pressure indication | PID-1-SI-LR20447 |
| [PS-7468](/instruments/PS-7468.md) | Lube Oil Low Pressure Trip / Alarm | Pressure Switch | Skid Mounted | Low setpoint | Trips pump CS-P-2B on loss of lubrication oil pressure | PID-1-SI-LR20447 |
| [TI-2588-1](/instruments/TI-2588-1.md) | Lube Oil Reservoir Temperature | Temperature Indicator | Skid Mounted | Local gauge | Oil reservoir temperature verification | PID-1-SI-LR20447 |
| [TI-2588-2](/instruments/TI-2588-2.md) | Lube Oil Cooler Discharge Temperature | Temperature Indicator | Skid Mounted | Local gauge | Bearing feed temperature monitoring | PID-1-SI-LR20447 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-LO-P243B-SUCT | INLET | OIL RESV'R (CS-P-2B) | CS-P-243B | 1" | Suction line | Ambient to 140°F | Static head | — | Lube oil pump suction from oil reservoir |
| STR-LO-P243B-DISCH | OUTLET | CS-P-243B | OIL COOLER (CS-P-2B) | 1" | Sight Flow Indicator (LOF) | Operating lube temp | Lube oil operating pressure | — | Pump discharge through sight flow indicator LOF to shell/tube oil cooler |
| STR-LO-P243B-COOLING | UTILITY | CCW LOOP B (20211 [B-5]) | OIL COOLER (CS-P-2B) | 1-1/2" | Isolation valves | CCW supply temp | CCW operating pressure | — | CCW Loop B cooling water to lube oil cooler |
| STR-LO-P243B-DRN | DRAIN | CS-P-243B Skid | WLD DR 191 | 1/2"x1" | CS-V1217, CS-V609 | Ambient | Atmospheric | — | Skid drain and reservoir drain to waste liquid processing |

## Hazards & Safeguards

- Loss of lube oil pressure: Low pressure switch PS-7468 protects main charging pump CS-P-2B bearings and gear drive from wiping on lubrication failure.
- Thermal fouling of oil cooler: Cooled by CCW Loop B; requires monitoring via TI-2588-2 to prevent bearing overheating.
- Drainage segregation: Drains via CS-V1217 and CS-V609 to radioactive waste drains DR 191 per drawing 20223 [A, IF-9].

## References & Sources

[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
