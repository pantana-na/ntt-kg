---
type: Equipment Concept
title: CS-P-2B — Charging Pump (High Head Safety Injection)
description: High Head Safety Injection / Charging Pump B supplying redundant normal
  CVCS reactor coolant makeup, pressurizer level control, reactor coolant pump (RCP)
  seal water injection, and delivering high-pressure emergency borated water from
  the RWST to RCS Cold Legs (Loops 1–4) through Penetration X-24 during emergency
  safety injection (LOCA / Steam Line Break).
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/CS-P-2B.md
tags:
- charging-pump
- cvcs
- emergency-core-cooling
- equipment
- high-head-injection
- nuclear-safety
- pump
- safety-injection
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-1.pdf
  title: ML101620329-part-1.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T12:43:17Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T12:43:17Z'
- by: process:okf-validation-suite
  at: '2026-10-02T12:43:17Z'
status: stable
entity_metadata:
  tag: CS-P-2B
  instruments:
  - type: Pressure Indicator
    location: 3/4" Tap off 6" Suction Line (Grid C-10)
    tag: PI-188
    interlock_or_alarm: Local suction pressure verification
    setpoint_or_range: Local gauge
    source: PID-1-SI-LR20447
    service: Pump Suction Pressure
  - setpoint_or_range: Local gauge
    source: PID-1-SI-LR20447
    interlock_or_alarm: Local discharge pressure indication
    service: Pump Discharge Pressure
    type: Pressure Indicator
    tag: PI-119
    location: Discharge Header (Grid D-11)
  - service: Pump 2B Discharge Flow Element
    type: Flow Element
    tag: FE-7326
    interlock_or_alarm: Flow sensing for charging pump 2B
    setpoint_or_range: Differential pressure
    location: 4" Discharge Line downstream of CS-V869
    source: PID-1-SI-LR20447
  - tag: FT-7326
    type: Flow Transmitter
    source: PID-1-SI-LR20447
    service: Pump 2B Discharge Flow Rate
    interlock_or_alarm: Control room flow indication
    setpoint_or_range: 4–20 mA
    location: Across FE-7326
  - service: Pump 2B Miniflow Interlock
    setpoint_or_range: Flow setpoint
    interlock_or_alarm: Miniflow valve CS-V197 interlock
    location: Across FE-7326
    source: PID-1-SI-LR20447
    type: Flow Indicating Switch
    tag: FIS-7326
  - source: PID-1-SI-LR20447
    location: Skid Mounted Lube Oil Header
    setpoint_or_range: Local gauge
    tag: PI-7468-1 / -2
    type: Pressure Indicator
    service: Lube Oil Pressure
    interlock_or_alarm: Local lube oil header pressure
  - location: Skid Mounted Lube Oil Header
    service: Lube Oil Low Pressure Trip
    setpoint_or_range: Low trip setpoint
    interlock_or_alarm: Pump trip / control room alarm on loss of oil
    tag: PS-7468
    source: PID-1-SI-LR20447
    type: Pressure Switch
  - source: PID-1-SI-LR20447
    interlock_or_alarm: Bearing / oil temperature monitoring
    tag: TI-2588-1 / -2
    location: Skid Oil Reservoir / Cooler
    setpoint_or_range: Local gauge
    type: Temperature Indicator
    service: Lube Oil Temperature
  connections:
  - flow_rate: —
    stream_id: STR-CS-P2B-SUCT
    source_tag: RWST / RHR / VCT
    inline_components:
    - CBS-V58
    - CS-V217 (LO)
    temperature: Borated ambient
    description: Suction header from RWST, RHR low-head, or VCT
    source: PID-1-SI-LR20447
    direction: INLET
    target_tag: CS-P-2B
    pressure: Static suction head
    line_size: 8"x6"
  - pressure: 2500+ PSIG injection head
    source: PID-1-SI-LR20447
    line_size: 4"
    target_tag: CS-4" HHI Header
    description: Main 4" high-pressure charging / safety injection discharge line
    temperature: Ambient to warmed
    direction: OUTLET
    source_tag: CS-P-2B
    stream_id: STR-CS-P2B-DISCH
    flow_rate: —
    inline_components:
    - CS-V871 (Check)
    - CS-V869
    - FE-7326
    - CS-V220 (LO)
  - description: Minimum recirculation flow line through orifice FO-7482
    temperature: Ambient
    target_tag: CVCS SEAL WTR HX
    inline_components:
    - CS-V199 (Check)
    - FO-7482
    - CS-V197 (MOV)
    flow_rate: —
    pressure: Recirculation head
    stream_id: STR-CS-P2B-MINIFLOW
    source_tag: CS-P-2B
    line_size: 2"
    direction: RECIRC
    source: PID-1-SI-LR20447
  - direction: UTILITY
    line_size: 1-1/2"
    target_tag: CS-P-2B Oil Cooler
    description: Component Cooling Water supply/return for lube oil heat exchanger
    temperature: Cooling water
    stream_id: STR-CS-P2B-LO-CCW
    inline_components:
    - Isolation valves
    flow_rate: —
    source: PID-1-SI-LR20447
    source_tag: CCW LOOP B
    pressure: Component cooling
  - source_tag: CS-P-2B Skid
    line_size: 1/2"x1"
    direction: DRAIN
    temperature: Ambient
    description: Lube oil and casing drains to waste liquid drains (20223 [A, IF-9])
    source: PID-1-SI-LR20447
    target_tag: WLD DR 190 / DR 191
    flow_rate: —
    pressure: Atmospheric
    inline_components:
    - CS-V1217
    - CS-V609
    stream_id: STR-CS-P2B-DRN
  equipment_class: Pump
  name: Charging Pump (High Head Safety Injection)
  unit: CS / SI
---

# CS-P-2B — Charging Pump (High Head Safety Injection)

## Function

High Head Safety Injection / Charging Pump B supplying redundant normal CVCS reactor coolant makeup, pressurizer level control, reactor coolant pump (RCP) seal water injection, and delivering high-pressure emergency borated water from the RWST to RCS Cold Legs (Loops 1–4) through Penetration X-24 during emergency safety injection (LOCA / Steam Line Break).

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20447 (Rev. 15, Ref. B20447) | — | PID-1-SI-LR20447 |
| System Prefix | SI / CS | — | PID-1-SI-LR20447 (General Note 2) |
| Verbatim Printed Tag | CS-P-2B | — | PID-1-SI-LR20447 |
| Safety Classification | Safety Class 2 (Nuclear Safety Related) | — | PID-1-SI-LR20447 |
| AMR Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20447 |
| Physical Location | Primary Auxiliary Building (Grid B-9 / B-10) | — | PID-1-SI-LR20447 |
| Suction Nozzle Size | 6 | in | PID-1-SI-LR20447 |
| Suction Header Size | 8 | in | PID-1-SI-LR20447 (CBS 8" / CS 8") |
| Discharge Nozzle Size | 4 | in | PID-1-SI-LR20447 |
| Miniflow Bypass Line Size | 2 | in | PID-1-SI-LR20447 (with FO-7482) |
| Driver & Auxiliary Skid | Gear Drive, Lube Oil Pump CS-P-243B, Oil Reservoir, Oil Cooler | — | PID-1-SI-LR20447 |
| Lube Oil System Class | A* (Safety Class / Seismic per Note 10) | — | PID-1-SI-LR20447 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Emergency Suction Source | RWST (Drawing 20233 [P, H-6]) via CBS-V58 / CS-V217 (LO) | — | PID-1-SI-LR20447 |
| Alternate Low Head Suction | RHR Low Head Safety Injection Loop A (20449 [A, H-9]) | — | PID-1-SI-LR20447 |
| Normal Suction Source | CVCS Volume Control Tank (20725 [C-8, CS-P-128]) | — | PID-1-SI-LR20447 |
| Main Discharge Destination | High Head Injection Header / Containment Penetration X-24 | — | PID-1-SI-LR20447 |
| Normal Seal Injection Destination | RCP Seal Water Injection Header (20726 [D, D-4]) | — | PID-1-SI-LR20447 |
| Miniflow Return Destination | CVCS Seal Water Heat Exchanger (20726 [D, D-4]) | — | PID-1-SI-LR20447 |
| Lube Oil Cooler Utility | CCW Loop B (20211 [B-5]) via 1-1/2" line | — | PID-1-SI-LR20447 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PI-188](/instruments/PI-188.md) | Pump Suction Pressure | Pressure Indicator | 3/4" Tap off 6" Suction Line (Grid C-10) | Local gauge | Local suction pressure verification | PID-1-SI-LR20447 |
| [PI-119](/instruments/PI-119.md) | Pump Discharge Pressure | Pressure Indicator | Discharge Header (Grid D-11) | Local gauge | Local discharge pressure indication | PID-1-SI-LR20447 |
| [FE-7326](/instruments/FE-7326.md) | Pump 2B Discharge Flow Element | Flow Element | 4" Discharge Line downstream of CS-V869 | Differential pressure | Flow sensing for charging pump 2B | PID-1-SI-LR20447 |
| [FT-7326](/instruments/FT-7326.md) | Pump 2B Discharge Flow Rate | Flow Transmitter | Across FE-7326 | 4–20 mA | Control room flow indication | PID-1-SI-LR20447 |
| [FIS-7326](/instruments/FIS-7326.md) | Pump 2B Miniflow Interlock | Flow Indicating Switch | Across FE-7326 | Flow setpoint | Miniflow valve CS-V197 interlock | PID-1-SI-LR20447 |
| [PI-7468-1 / -2](/instruments/PI-7468.md) | Lube Oil Pressure | Pressure Indicator | Skid Mounted Lube Oil Header | Local gauge | Local lube oil header pressure | PID-1-SI-LR20447 |
| [PS-7468](/instruments/PS-7468.md) | Lube Oil Low Pressure Trip | Pressure Switch | Skid Mounted Lube Oil Header | Low trip setpoint | Pump trip / control room alarm on loss of oil | PID-1-SI-LR20447 |
| [TI-2588-1 / -2](/instruments/TI-2588.md) | Lube Oil Temperature | Temperature Indicator | Skid Oil Reservoir / Cooler | Local gauge | Bearing / oil temperature monitoring | PID-1-SI-LR20447 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-CS-P2B-SUCT | INLET | RWST / RHR / VCT | CS-P-2B | 8"x6" | CBS-V58, CS-V217 (LO) | Borated ambient | Static suction head | — | Suction header from RWST, RHR low-head, or VCT |
| STR-CS-P2B-DISCH | OUTLET | CS-P-2B | CS-4" HHI Header | 4" | CS-V871 (Check), CS-V869, FE-7326, CS-V220 (LO) | Ambient to warmed | 2500+ PSIG injection head | — | Main 4" high-pressure charging / safety injection discharge line |
| STR-CS-P2B-MINIFLOW | RECIRC | CS-P-2B | CVCS SEAL WTR HX | 2" | CS-V199 (Check), FO-7482, CS-V197 (MOV) | Ambient | Recirculation head | — | Minimum recirculation flow line through orifice FO-7482 |
| STR-CS-P2B-LO-CCW | UTILITY | CCW LOOP B | CS-P-2B Oil Cooler | 1-1/2" | Isolation valves | Cooling water | Component cooling | — | Component Cooling Water supply/return for lube oil heat exchanger |
| STR-CS-P2B-DRN | DRAIN | CS-P-2B Skid | WLD DR 190 / DR 191 | 1/2"x1" | CS-V1217, CS-V609 | Ambient | Atmospheric | — | Lube oil and casing drains to waste liquid drains (20223 [A, IF-9]) |

## Hazards & Safeguards

- Minimum flow cavitation protection: Recirculation line with restricting orifice FO-7482 and motor-operated valve CS-V197 (interlocked with FIS-7326) protects pump against deadheading.
- Loss of lube oil protection: Pressure switch PS-7468 trips pump on loss of lubrication oil pressure.
- Penetration isolation: Containment isolation valves V138 and V139 provide dual-barrier motor-operated containment isolation at penetration X-24. Check valve SI-V297 has internals removed per General Note 9.

## References & Sources

[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
