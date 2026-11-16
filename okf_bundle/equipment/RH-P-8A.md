---
type: Equipment Concept
title: RH-P-8A — Residual Heat Removal Pump A
description: 'Residual Heat Removal (RHR) Pump A providing dual-function service:
  normal shutdown decay heat removal by drawing reactor coolant from RCS Loop 1 Hot
  Leg through Penetration X-9 and circulating through RHR Heat Exchanger RH-E-9A,
  and emergency Low Head Safety Injection (LHSI) / post-LOCA sump recirculation by
  drawing from Containment Recirculation Sump A (CBS-TK-10A) and delivering cooled
  water to RCS Cold Legs and SI Accumulators. Residual Heat Removal (RHR) Pump A providing
  dual-function service: normal shutdown decay heat removal by drawing reactor coolant
  from RCS Loop 1 Hot Leg through Penetration X-9 and circulating through RHR Heat
  Exchanger RH-E-9A, and emergency Low Head Safety Injection (LHSI) / post-LOCA sump
  recirculation by drawing from Containment Recirculation Sump A (CBS-TK-10A) and
  delivering cooled water to RCS Cold Legs and SI Accumulators via MOV RH-V18 and
  Penetration X-11.'
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/RH-P-8A.md
tags:
- emergency-core-cooling
- equipment
- low-head-injection
- nuclear-safety
- pump
- rh / si
- rhr
- shutdown-cooling
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-1.pdf
  title: ML101620329-part-1.pdf
- id: src-2
  resource: reference/raw/pid/ML101620329-part-2.pdf
  title: ML101620329-part-2.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:23:11Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:23:11Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:23:11Z'
status: stable
entity_metadata:
  tag: RH-P-8A
  name: Residual Heat Removal Pump A
  equipment_class: Pump
  unit: RH / SI
  instruments:
  - tag: TE-612
    service: Pump A Suction Temperature
    type: Temperature Element
    location: 8" Suction Header (Grid G-7)
    setpoint_or_range: Remote readout
    interlock_or_alarm: Monitor suction temperature during cooldown
    source: PID-1-SI-LR20448
  - tag: FE-610
    service: Suction Flow Sensing Element
    type: Flow Element (Orifice)
    location: 8" Suction Line (Grid G-7)
    setpoint_or_range: Differential pressure
    interlock_or_alarm: Flow sensing for FIS-610
    source: PID-1-SI-LR20448
  - tag: FIS-610
    service: Flow Indicating Switch
    type: Flow Switch
    location: Across FE-610
    setpoint_or_range: Flow setpoint
    interlock_or_alarm: Controls bypass FCV-610 (Interlock G)
    source: PID-1-SI-LR20448
  - tag: PI-2425A
    service: Suction Pressure Gauge
    type: Pressure Indicator
    location: 8" Suction Line (Grid F-7)
    setpoint_or_range: Local gauge
    interlock_or_alarm: Local suction pressure verification
    source: PID-1-SI-LR20448
  - tag: PT-614
    service: Suction Pressure Transmitter
    type: Pressure Transmitter
    location: 8" Suction Line (Grid F-7)
    setpoint_or_range: Remote signal
    interlock_or_alarm: Control room suction pressure indication
    source: PID-1-SI-LR20448
  - tag: FISL-2470
    service: Low Suction Flow Alarm
    type: Flow Indicating Switch Low
    location: 8" Suction Line (Grid F-7)
    setpoint_or_range: Low flow setpoint
    interlock_or_alarm: Low suction flow alarm
    source: PID-1-SI-LR20448
  - tag: PI-601
    service: Discharge Pressure Gauge
    type: Pressure Indicator
    location: 14" Discharge Line (Grid F-5)
    setpoint_or_range: Local gauge
    interlock_or_alarm: Local discharge head verification
    source: PID-1-SI-LR20448
  - tag: PT-2585
    service: Discharge Pressure Transmitter
    type: Pressure Transmitter
    location: 14" Discharge Line (Grid F-5)
    setpoint_or_range: Remote signal
    interlock_or_alarm: Control room discharge pressure indication
    source: PID-1-SI-LR20448
  - tag: TE-2564 / TE-2565
    service: Motor Bearing Temperatures
    type: Temperature Elements
    location: Motor Upper/Lower Bearings (Grid G-4)
    setpoint_or_range: RTD / Thermocouple
    interlock_or_alarm: Motor bearing temperature monitoring & high alarm
    source: PID-1-SI-LR20448
  - tag: TE-2566
    service: Pump Seal/Lower Bearing Temp
    type: Temperature Element
    location: Pump Seal Housing (Grid F-4)
    setpoint_or_range: RTD
    interlock_or_alarm: Mechanical seal temperature protection
    source: PID-1-SI-LR20448
  - tag: FE-2473
    service: Miniflow Element
    type: Flow Element (Orifice)
    location: 3" Miniflow Line (Grid F-5)
    setpoint_or_range: Differential pressure
    interlock_or_alarm: Minimum flow measurement across restriction orifice RO
    source: PID-1-SI-LR20448
  connections:
  - stream_id: STR-RH-P8A-SUCT-RCS
    direction: INLET
    source_tag: RCS LOOP 1 HOT LEG
    target_tag: RH-P-8A
    line_size: 12"x16"x8"
    inline_components:
    - Penetration X-9
    - CBS-V26 (16")
    - FE-610
    - RH-V4 (8")
    temperature: Operating RCS cooldown
    pressure: RCS pressure / Static head
    flow_rate: —
    description: Reactor Coolant System Loop 1 hot leg shutdown suction header
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-P8A-SUCT-SUMP
    direction: INLET
    source_tag: CBS-TK-10A (Sump A)
    target_tag: RH-P-8A
    line_size: 16"
    inline_components:
    - Guard Pipe
    - CBS-V8 (MOV)
    - Expansion Joint CBS-EP-36A
    temperature: Post-accident containment water
    pressure: Sump static head
    flow_rate: —
    description: Emergency containment recirculation sump suction line
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-P8A-DISCH
    direction: OUTLET
    source_tag: RH-P-8A
    target_tag: RH-E-9A
    line_size: 14"x16"x12"
    inline_components:
    - RH-V153 (Check)
    - RC-V140 (14" LC)
    - Pipe Anchor RH-S-T-1
    temperature: Ambient to 350°F
    pressure: Pump discharge head
    flow_rate: —
    description: Main 14" discharge header delivering coolant to RHR Heat Exchanger
      RH-E-9A
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-P8A-MINIFLOW
    direction: RECIRC
    source_tag: RH-P-8A
    target_tag: RH-E-9A Bypass Header
    line_size: 3"
    inline_components:
    - FE-2473
    - RO
    - RH-V166 (3")
    temperature: Cooldown fluid
    pressure: Recirculation head
    flow_rate: —
    description: Minimum recirculation flow line with breakdown restriction orifice
      RO
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-P8A-CCW
    direction: UTILITY
    source_tag: CCW LOOP A
    target_tag: RH-P-8A Seal
    line_size: 3/4"
    inline_components:
    - Manual isolation valves
    temperature: Cooling water
    pressure: Component cooling water
    flow_rate: —
    description: CCW supply and return to pump mechanical seal and bearing coolers
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-P8A-DRN
    direction: DRAIN
    source_tag: RH-P-8A Casing
    target_tag: WLD DR 157 / DR 154
    line_size: 3/4"
    inline_components:
    - RH-V121
    - RH-V82/83/84
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Casing and vent drain lines to liquid waste collection
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-P8A-LHSI-CROSSTIE
    direction: OUTLET
    source_tag: RH-P-8A
    target_tag: LOW HEAD SI TRAIN A HEADER (20449 [G-8])
    line_size: 8"
    inline_components:
    - RH-V18 (MOV, Note 8)
    temperature: Borated water
    pressure: LHSI discharge pressure
    flow_rate: LHSI flow rate
    description: Train A 8" discharge cross-tie to Low Head Safety Injection header
      via MOV RH-V18
    source: PID-1-SI-LR20449
---

# RH-P-8A — Residual Heat Removal Pump A

## Function
Residual Heat Removal (RHR) Pump A providing dual-function service: normal shutdown decay heat removal by drawing reactor coolant from RCS Loop 1 Hot Leg through Penetration X-9 and circulating through RHR Heat Exchanger RH-E-9A, and emergency Low Head Safety Injection (LHSI) / post-LOCA sump recirculation by drawing from Containment Recirculation Sump A (CBS-TK-10A) and delivering cooled water to RCS Cold Legs and SI Accumulators. Residual Heat Removal (RHR) Pump A providing dual-function service: normal shutdown decay heat removal by drawing reactor coolant from RCS Loop 1 Hot Leg through Penetration X-9 and circulating through RHR Heat Exchanger RH-E-9A, and emergency Low Head Safety Injection (LHSI) / post-LOCA sump recirculation by drawing from Containment Recirculation Sump A (CBS-TK-10A) and delivering cooled water to RCS Cold Legs and SI Accumulators via MOV RH-V18 and Penetration X-11.

## Design Data
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20448 (Rev. 11, Ref. B20448) | — | PID-1-SI-LR20448 |
| System Prefix | SI / RH | — | PID-1-SI-LR20448 (General Note 2) |
| Verbatim Printed Tag | RH-P-8A | — | PID-1-SI-LR20448 |
| Safety Classification | Safety Class 2 (Nuclear Safety Related) | — | PID-1-SI-LR20448 |
| AMR Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20448 |
| Physical Location | Primary Auxiliary Building Vault No. 1 - Inside Shielding (Grid G-4 / F-4) | — | PID-1-SI-LR20448 |
| Suction Nozzle Size | 8 | in | PID-1-SI-LR20448 |
| Suction Header Size | 12" to 16" to 14" to 8" | in | PID-1-SI-LR20448 (RC-12", CBS-16") |
| Discharge Nozzle Size | 14 | in | PID-1-SI-LR20448 |
| Miniflow Bypass Line Size | 3 | in | PID-1-SI-LR20448 (with FE-2473 & RO) |
| Discharge Check Valve | 14" Check Valve RH-V153 | — | PID-1-SI-LR20448 |
| Drawing Reference | PID-1-SI-LR20449 (Rev. 0, Ref. B20449 Rev. 9) | — | PID-1-SI-LR20449 |
| LHSI Cross-Tie Isolation Valve | RH-V18 (8" MOV, handjack locked open except midloop per Note 8) | — | PID-1-SI-LR20449 |

## Operating Conditions
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Normal RHR Suction Source | RCS Loop 1 Hot Leg (Dwg 20841 [A-12]) via Penetration X-9 | — | PID-1-SI-LR20448 |
| Emergency Post-LOCA Suction | Containment Recirculation Sump A (CBS-TK-10A) via MOV CBS-V8 | — | PID-1-SI-LR20448 |
| Normal / Emergency Discharge | RHR Loop A Heat Exchanger RH-E-9A Tube Inlet (12" line) | — | PID-1-SI-LR20448 |
| Miniflow Bypass Destination | Heat Exchanger RH-E-9A Bypass Header via RH-FCV-610 | — | PID-1-SI-LR20448 |
| Seal Cooling Utility Supply | Component Cooling Water CCW Loop A (20207 [E-11]) via 3/4" line | — | PID-1-SI-LR20448 |
| LHSI Delivery Mode | Direct Low Head SI to RCS Loops 1 & 2 Cold Legs | — | PID-1-SI-LR20449 |

## Instrumentation & Control Loops (P&ID)
| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TE-612](/instruments/TE-612.md) | Pump A Suction Temperature | Temperature Element | 8" Suction Header (Grid G-7) | Remote readout | Monitor suction temperature during cooldown | PID-1-SI-LR20448 |
| [FE-610](/instruments/FE-610.md) | Suction Flow Sensing Element | Flow Element (Orifice) | 8" Suction Line (Grid G-7) | Differential pressure | Flow sensing for FIS-610 | PID-1-SI-LR20448 |
| [FIS-610](/instruments/FIS-610.md) | Flow Indicating Switch | Flow Switch | Across FE-610 | Flow setpoint | Controls bypass FCV-610 (Interlock G) | PID-1-SI-LR20448 |
| [PI-2425A](/instruments/PI-2425A.md) | Suction Pressure Gauge | Pressure Indicator | 8" Suction Line (Grid F-7) | Local gauge | Local suction pressure verification | PID-1-SI-LR20448 |
| [PT-614](/instruments/PT-614.md) | Suction Pressure Transmitter | Pressure Transmitter | 8" Suction Line (Grid F-7) | Remote signal | Control room suction pressure indication | PID-1-SI-LR20448 |
| [FISL-2470](/instruments/FISL-2470.md) | Low Suction Flow Alarm | Flow Indicating Switch Low | 8" Suction Line (Grid F-7) | Low flow setpoint | Low suction flow alarm | PID-1-SI-LR20448 |
| [PI-601](/instruments/PI-601.md) | Discharge Pressure Gauge | Pressure Indicator | 14" Discharge Line (Grid F-5) | Local gauge | Local discharge head verification | PID-1-SI-LR20448 |
| [PT-2585](/instruments/PT-2585.md) | Discharge Pressure Transmitter | Pressure Transmitter | 14" Discharge Line (Grid F-5) | Remote signal | Control room discharge pressure indication | PID-1-SI-LR20448 |
| [TE-2564 / TE-2565](/instruments/TE-2564_TE-2565.md) | Motor Bearing Temperatures | Temperature Elements | Motor Upper/Lower Bearings (Grid G-4) | RTD / Thermocouple | Motor bearing temperature monitoring & high alarm | PID-1-SI-LR20448 |
| [TE-2566](/instruments/TE-2566.md) | Pump Seal/Lower Bearing Temp | Temperature Element | Pump Seal Housing (Grid F-4) | RTD | Mechanical seal temperature protection | PID-1-SI-LR20448 |
| [FE-2473](/instruments/FE-2473.md) | Miniflow Element | Flow Element (Orifice) | 3" Miniflow Line (Grid F-5) | Differential pressure | Minimum flow measurement across restriction orifice RO | PID-1-SI-LR20448 |

## Connections & Stream Summary
| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-RH-P8A-SUCT-RCS | INLET | RCS LOOP 1 HOT LEG | RH-P-8A | 12"x16"x8" | Penetration X-9, CBS-V26 (16"), FE-610, RH-V4 (8") | Operating RCS cooldown | RCS pressure / Static head | — | Reactor Coolant System Loop 1 hot leg shutdown suction header |
| STR-RH-P8A-SUCT-SUMP | INLET | CBS-TK-10A (Sump A) | RH-P-8A | 16" | Guard Pipe, CBS-V8 (MOV), Expansion Joint CBS-EP-36A | Post-accident containment water | Sump static head | — | Emergency containment recirculation sump suction line |
| STR-RH-P8A-DISCH | OUTLET | RH-P-8A | RH-E-9A | 14"x16"x12" | RH-V153 (Check), RC-V140 (14" LC), Pipe Anchor RH-S-T-1 | Ambient to 350°F | Pump discharge head | — | Main 14" discharge header delivering coolant to RHR Heat Exchanger RH-E-9A |
| STR-RH-P8A-MINIFLOW | RECIRC | RH-P-8A | RH-E-9A Bypass Header | 3" | FE-2473, RO, RH-V166 (3") | Cooldown fluid | Recirculation head | — | Minimum recirculation flow line with breakdown restriction orifice RO |
| STR-RH-P8A-CCW | UTILITY | CCW LOOP A | RH-P-8A Seal | 3/4" | Manual isolation valves | Cooling water | Component cooling water | — | CCW supply and return to pump mechanical seal and bearing coolers |
| STR-RH-P8A-DRN | DRAIN | RH-P-8A Casing | WLD DR 157 / DR 154 | 3/4" | RH-V121, RH-V82/83/84 | Ambient | Atmospheric | — | Casing and vent drain lines to liquid waste collection |
| STR-RH-P8A-LHSI-CROSSTIE | OUTLET | RH-P-8A | LOW HEAD SI TRAIN A HEADER (20449 [G-8]) | 8" | RH-V18 (MOV, Note 8) | Borated water | LHSI discharge pressure | LHSI flow rate | Train A 8" discharge cross-tie to Low Head Safety Injection header via MOV RH-V18 |

## Hazards & Safeguards
- Minimum recirculation flow interlock: Flow indicating switch FIS-610 and flow control valve RH-FCV-610 (Interlock G per Note 6) ensure minimum flow protection to prevent deadheading.
- Sump suction isolation: Sump MOV CBS-V8 is located inside sealed protective chamber CBS-TK-101A and interlocked to containment water levels CBS-LT-930..933 (Interlock A).
- Inadvertent RCS overpressure during shutdown: Positive isolation provided by locked-closed 14" gate valve RC-V140 and check valve RH-V153.
- Midloop alignment precaution: Handjack handwheel on RH-V18 must remain locked open except during midloop operations per Drawing Note 8.

## References & Sources
[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
[^src-2]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
