---
type: Equipment Concept
title: CS-P-2A — Charging Pump (High Head Safety Injection)
description: High Head Safety Injection / Charging Pump A supplying normal CVCS reactor
  coolant makeup, pressurizer level control, reactor coolant pump (RCP) seal water
  injection, and delivering high-pressure emergency borated water from the RWST to
  RCS Cold Legs (Loops 1–4) through Penetration X-24 during emergency safety injection
  (LOCA / Steam Line Break).
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/CS-P-2A.md
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
  at: '2026-10-02T12:42:54Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T12:42:54Z'
- by: process:okf-validation-suite
  at: '2026-10-02T12:42:54Z'
status: stable
entity_metadata:
  connections:
  - inline_components:
    - CBS-V60
    - CS-V207 (LO)
    line_size: 8"x6"
    direction: INLET
    source_tag: RWST / RHR / VCT
    description: Suction header from RWST, RHR low-head, or VCT
    flow_rate: —
    temperature: Borated ambient
    source: PID-1-SI-LR20447
    stream_id: STR-CS-P2A-SUCT
    pressure: Static suction head
    target_tag: CS-P-2A
  - line_size: 4"
    direction: OUTLET
    description: Main 4" high-pressure charging / safety injection discharge line
    target_tag: CS-4" HHI Header
    source: PID-1-SI-LR20447
    flow_rate: —
    pressure: 2500+ PSIG injection head
    stream_id: STR-CS-P2A-DISCH
    temperature: Ambient to warmed
    inline_components:
    - CS-V875 (Check)
    - CS-V873
    - FE-7325
    - CS-V220 (LO)
    source_tag: CS-P-2A
  - description: Minimum recirculation flow line through orifice FO-7466
    flow_rate: —
    source_tag: CS-P-2A
    stream_id: STR-CS-P2A-MINIFLOW
    pressure: Recirculation head
    source: PID-1-SI-LR20447
    line_size: 2"
    target_tag: CVCS SEAL WTR HX
    direction: RECIRC
    temperature: Ambient
    inline_components:
    - CS-V211 (Check)
    - FO-7466
    - CS-V196 (MOV)
  - pressure: Component cooling
    temperature: Cooling water
    direction: UTILITY
    source_tag: CCW LOOP A
    line_size: 1-1/2"
    description: Component Cooling Water supply/return for lube oil heat exchanger
    stream_id: STR-CS-P2A-LO-CCW
    inline_components:
    - Isolation valves
    target_tag: CS-P-2A Oil Cooler
    source: PID-1-SI-LR20447
    flow_rate: —
  - flow_rate: —
    inline_components:
    - CS-V1215
    - CS-V602
    source_tag: CS-P-2A Skid
    stream_id: STR-CS-P2A-DRN
    description: Lube oil and casing drains to waste liquid drains (20223 [B, IF-9])
    temperature: Ambient
    line_size: 1/2"x1"
    target_tag: WLD DR 188 / DR 189
    source: PID-1-SI-LR20447
    direction: DRAIN
    pressure: Atmospheric
  unit: CS / SI
  instruments:
  - source: PID-1-SI-LR20447
    service: Pump Suction Pressure
    location: 3/4" Tap off 6" Suction Line (Grid C-7)
    tag: PI-187
    setpoint_or_range: Local gauge
    type: Pressure Indicator
    interlock_or_alarm: Local suction pressure verification
  - location: Discharge Header (Grid C-5)
    type: Pressure Indicator
    service: Pump Discharge Pressure
    source: PID-1-SI-LR20447
    setpoint_or_range: Local gauge
    tag: PI-118
    interlock_or_alarm: Local discharge pressure indication
  - service: Pump 2A Discharge Flow Element
    tag: FE-7325
    setpoint_or_range: Differential pressure
    location: 4" Discharge Line downstream of CS-V873
    type: Flow Element
    source: PID-1-SI-LR20447
    interlock_or_alarm: Flow sensing for charging pump 2A
  - interlock_or_alarm: Control room flow indication
    tag: FT-7325
    setpoint_or_range: 4–20 mA
    type: Flow Transmitter
    location: Across FE-7325
    service: Pump 2A Discharge Flow Rate
    source: PID-1-SI-LR20447
  - tag: FIS-7325
    location: Across FE-7325
    source: PID-1-SI-LR20447
    setpoint_or_range: Flow setpoint
    type: Flow Indicating Switch
    interlock_or_alarm: Miniflow valve CS-V196 interlock
    service: Pump 2A Miniflow Interlock
  - setpoint_or_range: Differential pressure
    interlock_or_alarm: Primary high head injection flow sensing
    location: Main 4" High Head Injection Header
    service: Total HHI Header Flow Element
    type: Flow Element
    source: PID-1-SI-LR20447
    tag: FE-917
  - service: Total HHI Injection Flow Rate
    tag: FT-917
    source: PID-1-SI-LR20447
    type: Flow Transmitter
    setpoint_or_range: 4–20 mA
    location: Across FE-917
    interlock_or_alarm: Control room indication & ESFAS logging
  - service: Lube Oil Pressure
    type: Pressure Indicator
    location: Skid Mounted Lube Oil Header
    source: PID-1-SI-LR20447
    setpoint_or_range: Local gauge
    tag: PI-7467-1 / -2
    interlock_or_alarm: Local lube oil header pressure
  - interlock_or_alarm: Pump trip / control room alarm on loss of oil
    setpoint_or_range: Low trip setpoint
    type: Pressure Switch
    location: Skid Mounted Lube Oil Header
    tag: PS-7467
    source: PID-1-SI-LR20447
    service: Lube Oil Low Pressure Trip
  - tag: TI-2587-1 / -2
    service: Lube Oil Temperature
    setpoint_or_range: Local gauge
    type: Temperature Indicator
    interlock_or_alarm: Bearing / oil temperature monitoring
    location: Skid Oil Reservoir / Cooler
    source: PID-1-SI-LR20447
  name: Charging Pump (High Head Safety Injection)
  tag: CS-P-2A
  equipment_class: Pump
---

# CS-P-2A — Charging Pump (High Head Safety Injection)

## Function

High Head Safety Injection / Charging Pump A supplying normal CVCS reactor coolant makeup, pressurizer level control, reactor coolant pump (RCP) seal water injection, and delivering high-pressure emergency borated water from the RWST to RCS Cold Legs (Loops 1–4) through Penetration X-24 during emergency safety injection (LOCA / Steam Line Break).

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20447 (Rev. 15, Ref. B20447) | — | PID-1-SI-LR20447 |
| System Prefix | SI / CS | — | PID-1-SI-LR20447 (General Note 2) |
| Verbatim Printed Tag | CS-P-2A | — | PID-1-SI-LR20447 |
| Safety Classification | Safety Class 2 (Nuclear Safety Related) | — | PID-1-SI-LR20447 |
| AMR Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20447 |
| Physical Location | Primary Auxiliary Building (Grid B-5 / B-6) | — | PID-1-SI-LR20447 |
| Suction Nozzle Size | 6 | in | PID-1-SI-LR20447 |
| Suction Header Size | 8 | in | PID-1-SI-LR20447 (CBS 8" / CS 8") |
| Discharge Nozzle Size | 4 | in | PID-1-SI-LR20447 |
| Miniflow Bypass Line Size | 2 | in | PID-1-SI-LR20447 (with FO-7466) |
| Driver & Auxiliary Skid | Gear Drive, Lube Oil Pump CS-P-243A, Oil Reservoir, Oil Cooler | — | PID-1-SI-LR20447 |
| Lube Oil System Class | A* (Safety Class / Seismic per Note 10) | — | PID-1-SI-LR20447 |
| Suction Relief Valve | CS-V227 (Set @ 220 psig to BRS) | psig | PID-1-SI-LR20447 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Emergency Suction Source | RWST (Drawing 20233 [N, H-6]) via CBS-V60 / CS-V207 (LO) | — | PID-1-SI-LR20447 |
| Alternate Low Head Suction | RHR Low Head Safety Injection Loop A (20449 [A, H-9]) | — | PID-1-SI-LR20447 |
| Normal Suction Source | CVCS Volume Control Tank (20725 [C-8, CS-P-128]) | — | PID-1-SI-LR20447 |
| Main Discharge Destination | High Head Injection Header / Containment Penetration X-24 | — | PID-1-SI-LR20447 |
| Normal Seal Injection Destination | RCP Seal Water Injection Header (20726 [D, D-4]) | — | PID-1-SI-LR20447 |
| Miniflow Return Destination | CVCS Seal Water Heat Exchanger (20726 [D, D-4]) | — | PID-1-SI-LR20447 |
| Lube Oil Cooler Utility | CCW Loop A (20205 [B-5]) via 1-1/2" line | — | PID-1-SI-LR20447 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PI-187](/instruments/PI-187.md) | Pump Suction Pressure | Pressure Indicator | 3/4" Tap off 6" Suction Line (Grid C-7) | Local gauge | Local suction pressure verification | PID-1-SI-LR20447 |
| [PI-118](/instruments/PI-118.md) | Pump Discharge Pressure | Pressure Indicator | Discharge Header (Grid C-5) | Local gauge | Local discharge pressure indication | PID-1-SI-LR20447 |
| [FE-7325](/instruments/FE-7325.md) | Pump 2A Discharge Flow Element | Flow Element | 4" Discharge Line downstream of CS-V873 | Differential pressure | Flow sensing for charging pump 2A | PID-1-SI-LR20447 |
| [FT-7325](/instruments/FT-7325.md) | Pump 2A Discharge Flow Rate | Flow Transmitter | Across FE-7325 | 4–20 mA | Control room flow indication | PID-1-SI-LR20447 |
| [FIS-7325](/instruments/FIS-7325.md) | Pump 2A Miniflow Interlock | Flow Indicating Switch | Across FE-7325 | Flow setpoint | Miniflow valve CS-V196 interlock | PID-1-SI-LR20447 |
| [FE-917](/instruments/FE-917.md) | Total HHI Header Flow Element | Flow Element | Main 4" High Head Injection Header | Differential pressure | Primary high head injection flow sensing | PID-1-SI-LR20447 |
| [FT-917](/instruments/FT-917.md) | Total HHI Injection Flow Rate | Flow Transmitter | Across FE-917 | 4–20 mA | Control room indication & ESFAS logging | PID-1-SI-LR20447 |
| [PI-7467-1 / -2](/instruments/PI-7467.md) | Lube Oil Pressure | Pressure Indicator | Skid Mounted Lube Oil Header | Local gauge | Local lube oil header pressure | PID-1-SI-LR20447 |
| [PS-7467](/instruments/PS-7467.md) | Lube Oil Low Pressure Trip | Pressure Switch | Skid Mounted Lube Oil Header | Low trip setpoint | Pump trip / control room alarm on loss of oil | PID-1-SI-LR20447 |
| [TI-2587-1 / -2](/instruments/TI-2587.md) | Lube Oil Temperature | Temperature Indicator | Skid Oil Reservoir / Cooler | Local gauge | Bearing / oil temperature monitoring | PID-1-SI-LR20447 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-CS-P2A-SUCT | INLET | RWST / RHR / VCT | CS-P-2A | 8"x6" | CBS-V60, CS-V207 (LO) | Borated ambient | Static suction head | — | Suction header from RWST, RHR low-head, or VCT |
| STR-CS-P2A-DISCH | OUTLET | CS-P-2A | CS-4" HHI Header | 4" | CS-V875 (Check), CS-V873, FE-7325, CS-V220 (LO) | Ambient to warmed | 2500+ PSIG injection head | — | Main 4" high-pressure charging / safety injection discharge line |
| STR-CS-P2A-MINIFLOW | RECIRC | CS-P-2A | CVCS SEAL WTR HX | 2" | CS-V211 (Check), FO-7466, CS-V196 (MOV) | Ambient | Recirculation head | — | Minimum recirculation flow line through orifice FO-7466 |
| STR-CS-P2A-LO-CCW | UTILITY | CCW LOOP A | CS-P-2A Oil Cooler | 1-1/2" | Isolation valves | Cooling water | Component cooling | — | Component Cooling Water supply/return for lube oil heat exchanger |
| STR-CS-P2A-DRN | DRAIN | CS-P-2A Skid | WLD DR 188 / DR 189 | 1/2"x1" | CS-V1215, CS-V602 | Ambient | Atmospheric | — | Lube oil and casing drains to waste liquid drains (20223 [B, IF-9]) |

## Hazards & Safeguards

- Minimum flow cavitation protection: Recirculation line with restricting orifice FO-7466 and motor-operated valve CS-V196 (interlocked with FIS-7325) protects positive-displacement / multi-stage centrifugal pump from deadheading.
- Loss of lube oil protection: Pressure switch PS-7467 trips pump on loss of lubrication oil pressure.
- Suction overpressurization: Thermal relief valve CS-V227 set at 220 psig relieves excess pressure to Boron Recovery Tanks BRS-TK-66A/B.
- RCS Cold Leg backpressure: Restricting orifices RO-2671 through RO-2674 balance injection flows to Loops 1–4, and throttle valves V144, V148, V152, V156 are locked per General Note 4 to limit runout.

## References & Sources

[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
