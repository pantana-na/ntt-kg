---
type: Equipment Concept
title: RH-P-8B — Residual Heat Removal Pump B
description: 'Residual Heat Removal (RHR) Pump B providing redundant shutdown decay
  heat removal by drawing reactor coolant from RCS Loop 4 Hot Leg through Penetration
  X-10 and circulating through RHR Heat Exchanger RH-E-9B, and emergency Low Head
  Safety Injection (LHSI) / post-LOCA sump recirculation by drawing from Containment
  Recirculation Sump B (CBS-TK-10B) and delivering cooled water to RCS Cold Legs and
  SI Accumulators. Residual Heat Removal (RHR) Pump B providing dual-function service:
  normal shutdown decay heat removal by drawing reactor coolant from RCS Loop 4 Hot
  Leg through Penetration X-10 and circulating through RHR Heat Exchanger RH-E-9B,
  and emergency Low Head Safety Injection (LHSI) / post-LOCA sump recirculation by
  drawing from Containment Recirculation Sump B (CBS-TK-10B) and delivering cooled
  water to RCS Cold Legs and SI Accumulators via MOV RH-V19 and Penetration X-12.'
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/RH-P-8B.md
tags:
- equipment
- pump
- rh / si
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-1.pdf
  title: ML101620329-part-1.pdf
- id: src-2
  resource: reference/raw/pid/ML101620329-part-2.pdf
  title: ML101620329-part-2.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:23:18Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:23:18Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:23:18Z'
status: stable
entity_metadata:
  tag: RH-P-8B
  name: Residual Heat Removal Pump B
  equipment_class: Pump
  unit: RH / SI
  instruments:
  - tag: TE-613
    service: Pump B Suction Temperature
    type: Temperature Element
    location: 8" Suction Header (Grid C-7)
    setpoint_or_range: Remote readout
    interlock_or_alarm: Monitor suction temperature during cooldown
    source: PID-1-SI-LR20448
  - tag: FE-611
    service: Suction Flow Sensing Element
    type: Flow Element (Orifice)
    location: 8" Suction Line (Grid C-7)
    setpoint_or_range: Differential pressure
    interlock_or_alarm: Flow sensing for FIS-611
    source: PID-1-SI-LR20448
  - tag: FIS-611
    service: Flow Indicating Switch
    type: Flow Switch
    location: Across FE-611
    setpoint_or_range: Flow setpoint
    interlock_or_alarm: Controls bypass FCV-611 (Interlocks G & H)
    source: PID-1-SI-LR20448
  - tag: PI-2425B
    service: Suction Pressure Gauge
    type: Pressure Indicator
    location: 8" Suction Line (Grid D-7)
    setpoint_or_range: Local gauge
    interlock_or_alarm: Local suction pressure verification
    source: PID-1-SI-LR20448
  - tag: PT-615
    service: Suction Pressure Transmitter
    type: Pressure Transmitter
    location: 8" Suction Line (Grid D-7)
    setpoint_or_range: Remote signal
    interlock_or_alarm: Control room suction pressure indication
    source: PID-1-SI-LR20448
  - tag: FISL-2472
    service: Low Suction Flow Alarm
    type: Flow Indicating Switch Low
    location: 8" Suction Line (Grid D-7)
    setpoint_or_range: Low flow setpoint
    interlock_or_alarm: Low suction flow alarm
    source: PID-1-SI-LR20448
  - tag: PI-602
    service: Discharge Pressure Gauge
    type: Pressure Indicator
    location: 14" Discharge Line (Grid C-5)
    setpoint_or_range: Local gauge
    interlock_or_alarm: Local discharge head verification
    source: PID-1-SI-LR20448
  - tag: PT-2586
    service: Discharge Pressure Transmitter
    type: Pressure Transmitter
    location: 14" Discharge Line (Grid C-5)
    setpoint_or_range: Remote signal
    interlock_or_alarm: Control room discharge pressure indication
    source: PID-1-SI-LR20448
  - tag: TE-2567 / TE-2568
    service: Motor Bearing Temperatures
    type: Temperature Elements
    location: Motor Upper/Lower Bearings (Grid D-4)
    setpoint_or_range: RTD / Thermocouple
    interlock_or_alarm: Motor bearing temperature monitoring & high alarm
    source: PID-1-SI-LR20448
  - tag: TE-2569
    service: Pump Seal/Lower Bearing Temp
    type: Temperature Element
    location: Pump Seal Housing (Grid C-4)
    setpoint_or_range: RTD
    interlock_or_alarm: Mechanical seal temperature protection
    source: PID-1-SI-LR20448
  - tag: FE-2474
    service: Miniflow Element
    type: Flow Element (Orifice)
    location: 3" Miniflow Line (Grid B-4)
    setpoint_or_range: Differential pressure
    interlock_or_alarm: Minimum flow measurement across restriction orifice RO
    source: PID-1-SI-LR20448
  connections:
  - stream_id: STR-RH-P8B-SUCT-RCS
    direction: INLET
    source_tag: RCS LOOP 4 HOT LEG (20844 [B-12])
    target_tag: RH-P-8B
    line_size: 12"x16"x8"
    inline_components:
    - Penetration X-10
    - CBS-V25 (16")
    - FE-611
    - RH-V40 (8")
    temperature: Operating RCS cooldown
    pressure: RCS pressure / Static head
    flow_rate: —
    description: Reactor Coolant System Loop 4 hot leg shutdown suction header
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-P8B-SUCT-SUMP
    direction: INLET
    source_tag: CBS-TK-10B (Sump B)
    target_tag: RH-P-8B
    line_size: 16"
    inline_components:
    - Guard Pipe
    - CBS-V14 (MOV)
    - Expansion Joint CBS-EP-36B
    temperature: Post-accident containment water
    pressure: Sump static head
    flow_rate: —
    description: Emergency containment recirculation sump suction line
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-P8B-DISCH
    direction: OUTLET
    source_tag: RH-P-8B
    target_tag: RH-E-9B
    line_size: 14"x16"x12"
    inline_components:
    - RH-V154 (Check)
    - RC-V141 (14" LC)
    - Pipe Anchor RH-S-T-2
    temperature: Ambient to 350°F
    pressure: Pump discharge head
    flow_rate: —
    description: Main 14" discharge header delivering coolant to RHR Heat Exchanger
      RH-E-9B
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-P8B-MINIFLOW
    direction: RECIRC
    source_tag: RH-P-8B
    target_tag: RH-E-9B Bypass Header
    line_size: 3"
    inline_components:
    - FE-2474
    - RO
    - RH-FCV-611
    - RH-V167 (Check)
    temperature: Cooldown fluid
    pressure: Recirculation head
    flow_rate: —
    description: Minimum recirculation flow line with breakdown restriction orifice
      RO and FCV-611
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-P8B-CCW
    direction: UTILITY
    source_tag: CCW LOOP B (20213 [D-4])
    target_tag: RH-P-8B Seal
    line_size: 3/4"
    inline_components:
    - Manual isolation valves
    temperature: Cooling water
    pressure: Component cooling water
    flow_rate: —
    description: CCW supply and return to pump mechanical seal and bearing coolers
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-P8B-DRN
    direction: DRAIN
    source_tag: RH-P-8B Casing
    target_tag: WLD DR 159 / DR 155
    line_size: 3/4"
    inline_components:
    - RH-V120
    - RH-V74/75/76
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Casing and vent drain lines to liquid waste collection
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-P8B-LHSI-CROSSTIE
    direction: OUTLET
    source_tag: RH-P-8B
    target_tag: LOW HEAD SI TRAIN B HEADER (20449 [C-8])
    line_size: 8"
    inline_components:
    - RH-V19 (MOV, Note 8)
    temperature: Borated water
    pressure: LHSI discharge pressure
    flow_rate: LHSI flow rate
    description: Train B 8" discharge cross-tie to Low Head Safety Injection header
      via MOV RH-V19
    source: PID-1-SI-LR20449
---

# RH-P-8B — Residual Heat Removal Pump B

## Function
Residual Heat Removal (RHR) Pump B providing redundant shutdown decay heat removal by drawing reactor coolant from RCS Loop 4 Hot Leg through Penetration X-10 and circulating through RHR Heat Exchanger RH-E-9B, and emergency Low Head Safety Injection (LHSI) / post-LOCA sump recirculation by drawing from Containment Recirculation Sump B (CBS-TK-10B) and delivering cooled water to RCS Cold Legs and SI Accumulators. Residual Heat Removal (RHR) Pump B providing dual-function service: normal shutdown decay heat removal by drawing reactor coolant from RCS Loop 4 Hot Leg through Penetration X-10 and circulating through RHR Heat Exchanger RH-E-9B, and emergency Low Head Safety Injection (LHSI) / post-LOCA sump recirculation by drawing from Containment Recirculation Sump B (CBS-TK-10B) and delivering cooled water to RCS Cold Legs and SI Accumulators via MOV RH-V19 and Penetration X-12.

## Design Data
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20448 (Rev. 11, Ref. B20448) | — | PID-1-SI-LR20448 |
| System Prefix | SI / RH | — | PID-1-SI-LR20448 (General Note 2) |
| Verbatim Printed Tag | RH-P-8B | — | PID-1-SI-LR20448 |
| Safety Classification | Safety Class 2 (Nuclear Safety Related) | — | PID-1-SI-LR20448 |
| AMR Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20448 |
| Physical Location | Primary Auxiliary Building Vault No. 2 - Inside Shielding (Grid C-4 / D-4) | — | PID-1-SI-LR20448 |
| Suction Nozzle Size | 8 | in | PID-1-SI-LR20448 |
| Suction Header Size | 12" to 16" to 14" to 8" (RC-12", CBS-16") | in | PID-1-SI-LR20448 |
| Discharge Nozzle Size | 14 | in | PID-1-SI-LR20448 |
| Miniflow Bypass Line Size | 3 (with FE-2474, RO, & RH-FCV-611) | in | PID-1-SI-LR20448 |
| Discharge Check Valve | 14" Check Valve RH-V154 | — | PID-1-SI-LR20448 |
| Drawing Reference | PID-1-SI-LR20449 (Rev. 0, Ref. B20449 Rev. 9) | — | PID-1-SI-LR20449 |
| LHSI Cross-Tie Isolation Valve | RH-V19 (8" MOV, handjack locked open except midloop per Note 8) | — | PID-1-SI-LR20449 |

## Operating Conditions
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Normal RHR Suction Source | RCS Loop 4 Hot Leg (Dwg 20844 [B-12]) via Penetration X-10 | — | PID-1-SI-LR20448 |
| Emergency Post-LOCA Suction | Containment Recirculation Sump B (CBS-TK-10B) via MOV CBS-V14 | — | PID-1-SI-LR20448 |
| Normal / Emergency Discharge | RHR Loop B Heat Exchanger RH-E-9B Tube Inlet (12" line) | — | PID-1-SI-LR20448 |
| Miniflow Bypass Destination | Heat Exchanger RH-E-9B Bypass Header via RH-FCV-611 | — | PID-1-SI-LR20448 |
| Seal Cooling Utility Supply | Component Cooling Water CCW Loop B (20213 [D-4]) via 3/4" line | — | PID-1-SI-LR20448 |
| LHSI Delivery Mode | Direct Low Head SI to RCS Loops 3 & 4 Cold Legs | — | PID-1-SI-LR20449 |

## Instrumentation & Control Loops (P&ID)
| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TE-613](/instruments/TE-613.md) | Pump B Suction Temperature | Temperature Element | 8" Suction Header (Grid C-7) | Remote readout | Monitor suction temperature during cooldown | PID-1-SI-LR20448 |
| [FE-611](/instruments/FE-611.md) | Suction Flow Sensing Element | Flow Element (Orifice) | 8" Suction Line (Grid C-7) | Differential pressure | Flow sensing for FIS-611 | PID-1-SI-LR20448 |
| [FIS-611](/instruments/FIS-611.md) | Flow Indicating Switch | Flow Switch | Across FE-611 | Flow setpoint | Controls bypass FCV-611 (Interlocks G & H) | PID-1-SI-LR20448 |
| [PI-2425B](/instruments/PI-2425B.md) | Suction Pressure Gauge | Pressure Indicator | 8" Suction Line (Grid D-7) | Local gauge | Local suction pressure verification | PID-1-SI-LR20448 |
| [PT-615](/instruments/PT-615.md) | Suction Pressure Transmitter | Pressure Transmitter | 8" Suction Line (Grid D-7) | Remote signal | Control room suction pressure indication | PID-1-SI-LR20448 |
| [FISL-2472](/instruments/FISL-2472.md) | Low Suction Flow Alarm | Flow Indicating Switch Low | 8" Suction Line (Grid D-7) | Low flow setpoint | Low suction flow alarm | PID-1-SI-LR20448 |
| [PI-602](/instruments/PI-602.md) | Discharge Pressure Gauge | Pressure Indicator | 14" Discharge Line (Grid C-5) | Local gauge | Local discharge head verification | PID-1-SI-LR20448 |
| [PT-2586](/instruments/PT-2586.md) | Discharge Pressure Transmitter | Pressure Transmitter | 14" Discharge Line (Grid C-5) | Remote signal | Control room discharge pressure indication | PID-1-SI-LR20448 |
| [TE-2567 / TE-2568](/instruments/TE-2567_TE-2568.md) | Motor Bearing Temperatures | Temperature Elements | Motor Upper/Lower Bearings (Grid D-4) | RTD / Thermocouple | Motor bearing temperature monitoring & high alarm | PID-1-SI-LR20448 |
| [TE-2569](/instruments/TE-2569.md) | Pump Seal/Lower Bearing Temp | Temperature Element | Pump Seal Housing (Grid C-4) | RTD | Mechanical seal temperature protection | PID-1-SI-LR20448 |
| [FE-2474](/instruments/FE-2474.md) | Miniflow Element | Flow Element (Orifice) | 3" Miniflow Line (Grid B-4) | Differential pressure | Minimum flow measurement across restriction orifice RO | PID-1-SI-LR20448 |

## Connections & Stream Summary
| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-RH-P8B-SUCT-RCS | INLET | RCS LOOP 4 HOT LEG (20844 [B-12]) | RH-P-8B | 12"x16"x8" | Penetration X-10, CBS-V25 (16"), FE-611, RH-V40 (8") | Operating RCS cooldown | RCS pressure / Static head | — | Reactor Coolant System Loop 4 hot leg shutdown suction header |
| STR-RH-P8B-SUCT-SUMP | INLET | CBS-TK-10B (Sump B) | RH-P-8B | 16" | Guard Pipe, CBS-V14 (MOV), Expansion Joint CBS-EP-36B | Post-accident containment water | Sump static head | — | Emergency containment recirculation sump suction line |
| STR-RH-P8B-DISCH | OUTLET | RH-P-8B | RH-E-9B | 14"x16"x12" | RH-V154 (Check), RC-V141 (14" LC), Pipe Anchor RH-S-T-2 | Ambient to 350°F | Pump discharge head | — | Main 14" discharge header delivering coolant to RHR Heat Exchanger RH-E-9B |
| STR-RH-P8B-MINIFLOW | RECIRC | RH-P-8B | RH-E-9B Bypass Header | 3" | FE-2474, RO, RH-FCV-611, RH-V167 (Check) | Cooldown fluid | Recirculation head | — | Minimum recirculation flow line with breakdown restriction orifice RO and FCV-611 |
| STR-RH-P8B-CCW | UTILITY | CCW LOOP B (20213 [D-4]) | RH-P-8B Seal | 3/4" | Manual isolation valves | Cooling water | Component cooling water | — | CCW supply and return to pump mechanical seal and bearing coolers |
| STR-RH-P8B-DRN | DRAIN | RH-P-8B Casing | WLD DR 159 / DR 155 | 3/4" | RH-V120, RH-V74/75/76 | Ambient | Atmospheric | — | Casing and vent drain lines to liquid waste collection |
| STR-RH-P8B-LHSI-CROSSTIE | OUTLET | RH-P-8B | LOW HEAD SI TRAIN B HEADER (20449 [C-8]) | 8" | RH-V19 (MOV, Note 8) | Borated water | LHSI discharge pressure | LHSI flow rate | Train B 8" discharge cross-tie to Low Head Safety Injection header via MOV RH-V19 |

## Hazards & Safeguards
- Minimum recirculation flow interlock: Flow indicating switch FIS-611 controls flow control valve RH-FCV-611 (Interlock H per Note 6) to ensure minimum flow protection against deadheading and cavitation.
- Sump suction isolation: Sump MOV CBS-V14 is located inside sealed protective chamber CBS-TK-101B and interlocked to containment water levels CBS-LT-930..933 (Interlock A).
- Inadvertent RCS overpressurization during shutdown: Positive isolation provided by locked-closed 14" gate valve RC-V141 and check valve RH-V154.
- Midloop alignment precaution: Handjack handwheel on RH-V19 must remain locked open except during midloop operations per Drawing Note 8.

## References & Sources
[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
[^src-2]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
