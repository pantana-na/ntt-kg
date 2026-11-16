---
type: Equipment Concept
title: SI-P-6B — Safety Injection Pump B (Intermediate Head)
description: Intermediate Head Safety Injection Pump B providing redundant high-pressure
  emergency core cooling water from the Refueling Water Storage Tank (RWST) or Cold
  Leg/Hot Leg recirculation headers to the Reactor Coolant System (RCS) Loops during
  loss-of-coolant accidents (LOCA). Intermediate Head Safety Injection Pump B providing
  high-pressure emergency core cooling water from RWST or post-LOCA low-head recirculation
  cross-tie (via MOV RH-V21) delivering to RCS Loops 3 and 4 cold legs.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SI-P-6B.md
tags:
- emergency-core-cooling
- equipment
- nuclear-safety
- pump
- safety-injection
- si
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-1.pdf
  title: ML101620329-part-1.pdf
- id: src-2
  resource: reference/raw/pid/ML101620329-part-2.pdf
  title: ML101620329-part-2.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:23:50Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:23:50Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:23:50Z'
status: stable
entity_metadata:
  tag: SI-P-6B
  name: Safety Injection Pump B (Intermediate Head)
  equipment_class: Pump
  unit: SI
  instruments:
  - tag: PI 978
    service: Pump Suction Pressure
    type: Pressure Indicator (Local)
    location: 6" CBS Suction Line
    setpoint_or_range: Local gauge
    interlock_or_alarm: Local suction pressure indication
    source: PID-1-SI-LR20446
  - tag: PI 2412 B
    service: Casing Suction Pressure
    type: Pressure Indicator
    location: Pump SI-P-6B Casing Tap
    setpoint_or_range: Local gauge
    interlock_or_alarm: Direct pump casing suction pressure
    source: PID-1-SI-LR20446
  - tag: PI 2415 B
    service: Pump Discharge Pressure
    type: Pressure Indicator
    location: 4" Discharge Line upstream of check V72
    setpoint_or_range: Local gauge
    interlock_or_alarm: Pump discharge head verification
    source: PID-1-SI-LR20446
  - tag: PT 923
    service: Discharge Header Pressure
    type: Pressure Transmitter
    location: 4" Discharge Header
    setpoint_or_range: Remote signal
    interlock_or_alarm: Control room pressure indication & safety interlocks
    source: PID-1-SI-LR20446
  - tag: FE 922
    service: Discharge Flow Sensing Element
    type: Flow Element (Orifice)
    location: 4" Discharge Line upstream of V75
    setpoint_or_range: Differential pressure
    interlock_or_alarm: Primary injection flow measurement
    source: PID-1-SI-LR20446
  - tag: FT 922
    service: Discharge Flow Rate
    type: Flow Transmitter
    location: Across FE-922 (via V73/V74)
    setpoint_or_range: 4–20 mA
    interlock_or_alarm: Control room flow indication & ESFAS verification
    source: PID-1-SI-LR20446
  connections:
  - stream_id: STR-SI-P6B-SUCT
    direction: INLET
    source_tag: CBS-TK-8 (RWST)
    target_tag: SI-P-6B
    line_size: 8"x6"
    inline_components:
    - CBS-V51 (MOV)
    - CBS-V52 (Check)
    - CBS-V53 (MOV)
    temperature: Borated ambient
    pressure: Static RWST head
    flow_rate: —
    description: Suction header from Refueling Water Storage Tank
    source: PID-1-SI-LR20446
  - stream_id: STR-SI-P6B-DISCH
    direction: OUTLET
    source_tag: SI-P-6B
    target_tag: SI-X-26 / SI-X-27
    line_size: 4"
    inline_components:
    - SI-V71 (LO)
    - SI-V72 (Check)
    - FE-922
    - SI-V75
    - SI-V272 (MOV)
    - SI-V114 (MOV)
    temperature: Ambient to warmed
    pressure: 2235 PSIG (Relief V76)
    flow_rate: —
    description: Main 4" intermediate head safety injection header
    source: PID-1-SI-LR20446
  - stream_id: STR-SI-P6B-RECIRC
    direction: RECIRC
    source_tag: SI-P-6B
    target_tag: CBS-TK-8 (RWST)
    line_size: 1-1/2"x2"x3"
    inline_components:
    - SI-V88 (MOV)
    - SI-V89 (MOV)
    - SI-V93 (Check)
    temperature: Ambient
    pressure: Recirculation head
    flow_rate: —
    description: Minimum recirculation flow line back to RWST (interlocked valve A
      per Note 3)
    source: PID-1-SI-LR20446
  - stream_id: STR-SI-P6B-XOVER
    direction: INLET
    source_tag: SI-P-6A Discharge
    target_tag: SI-P-6B
    line_size: 3"
    inline_components:
    - SI-V112 (MOV)
    - SI-V111 (MOV)
    temperature: Ambient
    pressure: System pressure
    flow_rate: —
    description: Intermediate Head cross-tie header between Train A and Train B
    source: PID-1-SI-LR20446
  - stream_id: STR-SI-P6B-DRN
    direction: DRAIN
    source_tag: SI-P-6B
    target_tag: WLD DR 161
    line_size: 2"
    inline_components:
    - SI-V279
    - SI-V199
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Pump casing and base drain lines to liquid waste drains (20221 [D-10])
    source: PID-1-SI-LR20446
  - stream_id: STR-SI-P6B-CCW
    direction: UTILITY
    source_tag: CCW LOOP B
    target_tag: SI-P-6B
    line_size: 1"
    inline_components:
    - Isolation valves
    temperature: Cooling water
    pressure: Component cooling
    flow_rate: —
    description: Component Cooling Water supply and return to pump bearings/coolers
    source: PID-1-SI-LR20446
  - stream_id: STR-RH-TO-SIPB-SUCT
    direction: INLET
    source_tag: LOW HEAD SI TRAIN B (20448 [C-8])
    target_tag: SI-P-6B
    line_size: 8"
    inline_components:
    - RH-V21 (MOV)
    temperature: Ambient to 350°F
    pressure: RHR discharge head
    flow_rate: Suction flow rate
    description: Suction cross-tie from Low Head SI / RHR header via MOV RH-V21 to
      SI-P-6B suction
    source: PID-1-SI-LR20449
  - stream_id: STR-SI-P6B-LOOP4-INJ
    direction: OUTLET
    source_tag: SI-P-6B (20446 [E-4])
    target_tag: RCS LOOP 4 COLD LEG (20450 [B-7])
    line_size: 6"
    inline_components:
    - RH-V65 (Check)
    temperature: Borated water
    pressure: Cold leg injection pressure
    flow_rate: Injection flow
    description: Intermediate Head SI-P-6B discharge injection branch to RCS Loop
      4 Cold Leg
    source: PID-1-SI-LR20449
  - stream_id: STR-SI-P6B-LOOP3-INJ
    direction: OUTLET
    source_tag: SI-P-6B (20446 [D-4])
    target_tag: RCS LOOP 3 COLD LEG (20450 [B-9])
    line_size: 6"
    inline_components:
    - RH-V63 (Check)
    temperature: Borated water
    pressure: Cold leg injection pressure
    flow_rate: Injection flow
    description: Intermediate Head SI-P-6B discharge injection branch to RCS Loop
      3 Cold Leg
    source: PID-1-SI-LR20449
---

# SI-P-6B — Safety Injection Pump B (Intermediate Head)

## Function
Intermediate Head Safety Injection Pump B providing redundant high-pressure emergency core cooling water from the Refueling Water Storage Tank (RWST) or Cold Leg/Hot Leg recirculation headers to the Reactor Coolant System (RCS) Loops during loss-of-coolant accidents (LOCA). Intermediate Head Safety Injection Pump B providing high-pressure emergency core cooling water from RWST or post-LOCA low-head recirculation cross-tie (via MOV RH-V21) delivering to RCS Loops 3 and 4 cold legs.

## Design Data
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20446 (Rev. 0, Ref. B20446 Rev. 17) | — | PID-1-SI-LR20446 |
| System Prefix | SI | — | PID-1-SI-LR20446 |
| Verbatim Printed Tag | SI-P-6B | — | PID-1-SI-LR20446 |
| Safety Classification | Safety Class 2 (Nuclear Safety Related) | — | PID-1-SI-LR20446 |
| AMR Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20446 |
| Physical Location | Primary Auxiliary Building Vault 2 (Inside Shielding) | — | PID-1-SI-LR20446 |
| Suction Nozzle Size | 6 | in | PID-1-SI-LR20446 |
| Suction Header Size | 8 | in | PID-1-SI-LR20446 (CBS-8") |
| Discharge Nozzle Size | 4 | in | PID-1-SI-LR20446 |
| Miniflow Line Size | 1.5 to 3 | in | PID-1-SI-LR20446 |
| Suction Relief Valve | CBS-V54 (Set @ 220 psig) | psig | PID-1-SI-LR20446 |
| Discharge Relief Valve | SI-V76 (Set @ 2235 psig) | psig | PID-1-SI-LR20446 |
| Drawing Reference | PID-1-SI-LR20449 (Rev. 0, Ref. B20449 Rev. 9) | — | PID-1-SI-LR20449 |
| Low Head Suction Cross-Tie Valve | RH-V21 (8" MOV) | — | PID-1-SI-LR20449 |

## Operating Conditions
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Primary Suction Source | RWST (Drawing 20233 [D-8]) via CBS-V51/V53 | — | PID-1-SI-LR20446 |
| Alternate Suction Source | RHR System Low Head Injection Header (20663 [H-6]) | — | PID-1-SI-LR20446 |
| Discharge Destination | Containment Penetrations X-26 and X-27 to RCS Loops | — | PID-1-SI-LR20446 |
| Miniflow Return Destination | RWST via common 3" return header (20233 [H-71]) | — | PID-1-SI-LR20446 |
| Cooling Utility Supply | Component Cooling Water CCW Loop B (20213 [E-6]) | — | PID-1-SI-LR20446 |
| Recirculation Suction Supply | RHR Train B discharge via 8" valve RH-V21 (20446 [B-11]) | — | PID-1-SI-LR20449 |

## Instrumentation & Control Loops (P&ID)
| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PI 978](/instruments/PI_978.md) | Pump Suction Pressure | Pressure Indicator (Local) | 6" CBS Suction Line | Local gauge | Local suction pressure indication | PID-1-SI-LR20446 |
| [PI 2412 B](/instruments/PI_2412_B.md) | Casing Suction Pressure | Pressure Indicator | Pump SI-P-6B Casing Tap | Local gauge | Direct pump casing suction pressure | PID-1-SI-LR20446 |
| [PI 2415 B](/instruments/PI_2415_B.md) | Pump Discharge Pressure | Pressure Indicator | 4" Discharge Line upstream of check V72 | Local gauge | Pump discharge head verification | PID-1-SI-LR20446 |
| [PT 923](/instruments/PT_923.md) | Discharge Header Pressure | Pressure Transmitter | 4" Discharge Header | Remote signal | Control room pressure indication & safety interlocks | PID-1-SI-LR20446 |
| [FE 922](/instruments/FE_922.md) | Discharge Flow Sensing Element | Flow Element (Orifice) | 4" Discharge Line upstream of V75 | Differential pressure | Primary injection flow measurement | PID-1-SI-LR20446 |
| [FT 922](/instruments/FT_922.md) | Discharge Flow Rate | Flow Transmitter | Across FE-922 (via V73/V74) | 4–20 mA | Control room flow indication & ESFAS verification | PID-1-SI-LR20446 |

## Connections & Stream Summary
| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-SI-P6B-SUCT | INLET | CBS-TK-8 (RWST) | SI-P-6B | 8"x6" | CBS-V51 (MOV), CBS-V52 (Check), CBS-V53 (MOV) | Borated ambient | Static RWST head | — | Suction header from Refueling Water Storage Tank |
| STR-SI-P6B-DISCH | OUTLET | SI-P-6B | SI-X-26 / SI-X-27 | 4" | SI-V71 (LO), SI-V72 (Check), FE-922, SI-V75, SI-V272 (MOV), SI-V114 (MOV) | Ambient to warmed | 2235 PSIG (Relief V76) | — | Main 4" intermediate head safety injection header |
| STR-SI-P6B-RECIRC | RECIRC | SI-P-6B | CBS-TK-8 (RWST) | 1-1/2"x2"x3" | SI-V88 (MOV), SI-V89 (MOV), SI-V93 (Check) | Ambient | Recirculation head | — | Minimum recirculation flow line back to RWST (interlocked valve A per Note 3) |
| STR-SI-P6B-XOVER | INLET | SI-P-6A Discharge | SI-P-6B | 3" | SI-V112 (MOV), SI-V111 (MOV) | Ambient | System pressure | — | Intermediate Head cross-tie header between Train A and Train B |
| STR-SI-P6B-DRN | DRAIN | SI-P-6B | WLD DR 161 | 2" | SI-V279, SI-V199 | Ambient | Atmospheric | — | Pump casing and base drain lines to liquid waste drains (20221 [D-10]) |
| STR-SI-P6B-CCW | UTILITY | CCW LOOP B | SI-P-6B | 1" | Isolation valves | Cooling water | Component cooling | — | Component Cooling Water supply and return to pump bearings/coolers |
| STR-RH-TO-SIPB-SUCT | INLET | LOW HEAD SI TRAIN B (20448 [C-8]) | SI-P-6B | 8" | RH-V21 (MOV) | Ambient to 350°F | RHR discharge head | Suction flow rate | Suction cross-tie from Low Head SI / RHR header via MOV RH-V21 to SI-P-6B suction |
| STR-SI-P6B-LOOP4-INJ | OUTLET | SI-P-6B (20446 [E-4]) | RCS LOOP 4 COLD LEG (20450 [B-7]) | 6" | RH-V65 (Check) | Borated water | Cold leg injection pressure | Injection flow | Intermediate Head SI-P-6B discharge injection branch to RCS Loop 4 Cold Leg |
| STR-SI-P6B-LOOP3-INJ | OUTLET | SI-P-6B (20446 [D-4]) | RCS LOOP 3 COLD LEG (20450 [B-9]) | 6" | RH-V63 (Check) | Borated water | Cold leg injection pressure | Injection flow | Intermediate Head SI-P-6B discharge injection branch to RCS Loop 3 Cold Leg |

## Hazards & Safeguards
- Pump runout protection: Throttle valve SI-V71 and branch balancing valves SI-V78/V79, SI-V83/V84, SI-V115/V116, SI-V119/V120, SI-V123/V124, SI-V127/V128 are adjusted in field and locked to prevent runout per General Note 7.
- Minimum flow interlock: Miniflow isolation valve SI-V89 carries Interlock A from residual heat removal valves RH-V35/RH-V36 per General Note 3 to prevent improper diversion during shutdown cooling.
- Suction overpressure: Relief valve CBS-V54 set at 220 psig protects the 6" suction line.
- Discharge overpressure: Thermal relief valves SI-V76 and SI-V113 set at 2235 psig protect discharge headers.
- Safety interlock A logic: Controls valve RH-V36 interlocked with SI-V89, SI-V90, SI-V93 (20446), CBS-V14 (20448), RC-V87 and RC-V88 (20441) per Note 3.

## References & Sources
[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
[^src-2]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
