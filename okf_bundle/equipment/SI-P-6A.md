---
type: Equipment Concept
title: SI-P-6A — Safety Injection Pump A (Intermediate Head)
description: Intermediate Head Safety Injection Pump A providing high-pressure emergency
  core cooling water from the Refueling Water Storage Tank (RWST) or Cold Leg/Hot
  Leg recirculation headers to the Reactor Coolant System (RCS) Loops during loss-of-coolant
  accidents (LOCA). Intermediate Head Safety Injection Pump A providing high-pressure
  emergency core cooling water from RWST or post-LOCA low-head recirculation cross-tie
  (via MOV RH-V22) delivering to RCS Loops 1 and 2 cold legs.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SI-P-6A.md
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
  at: '2026-10-02T13:23:41Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:23:41Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:23:41Z'
status: stable
entity_metadata:
  tag: SI-P-6A
  name: Safety Injection Pump A (Intermediate Head)
  equipment_class: Pump
  unit: SI
  instruments:
  - tag: PI 977
    service: Pump Suction Pressure
    type: Pressure Indicator (Local)
    location: 6" CBS Suction Line
    setpoint_or_range: Local gauge
    interlock_or_alarm: Local suction pressure indication
    source: PID-1-SI-LR20446
  - tag: PI 2412 A
    service: Casing Suction Pressure
    type: Pressure Indicator
    location: Pump SI-P-6A Casing Tap
    setpoint_or_range: Local gauge
    interlock_or_alarm: Direct pump casing suction pressure
    source: PID-1-SI-LR20446
  - tag: PI 2415 A
    service: Pump Discharge Pressure
    type: Pressure Indicator
    location: 4" Discharge Line upstream of check V97
    setpoint_or_range: Local gauge
    interlock_or_alarm: Pump discharge head verification
    source: PID-1-SI-LR20446
  - tag: PT 919
    service: Discharge Header Pressure
    type: Pressure Transmitter
    location: 4" Discharge Header
    setpoint_or_range: Remote signal
    interlock_or_alarm: Control room pressure indication & safety interlocks
    source: PID-1-SI-LR20446
  - tag: FE 918
    service: Discharge Flow Sensing Element
    type: Flow Element (Orifice)
    location: 4" Discharge Line upstream of V100
    setpoint_or_range: Differential pressure
    interlock_or_alarm: Primary injection flow measurement
    source: PID-1-SI-LR20446
  - tag: FT 918
    service: Discharge Flow Rate
    type: Flow Transmitter
    location: Across FE-918 (via V98/V99)
    setpoint_or_range: 4–20 mA
    interlock_or_alarm: Control room flow indication & ESFAS verification
    source: PID-1-SI-LR20446
  - tag: FE 968
    service: Miniflow Recirculation Element
    type: Flow Element (Orifice)
    location: Common 3" Miniflow Line to RWST
    setpoint_or_range: Differential pressure
    interlock_or_alarm: Measures combined minimum recirculation flow
    source: PID-1-SI-LR20446
  - tag: FI 968
    service: Miniflow Flow Rate
    type: Flow Indicator
    location: Across FE-968
    setpoint_or_range: Local indicator
    interlock_or_alarm: Verification of pump minimum flow protection
    source: PID-1-SI-LR20446
  connections:
  - stream_id: STR-SI-P6A-SUCT
    direction: INLET
    source_tag: CBS-TK-8 (RWST)
    target_tag: SI-P-6A
    line_size: 8"x6"
    inline_components:
    - CBS-V47 (MOV)
    - CBS-V48 (Check)
    - CBS-V49 (MOV)
    temperature: Borated ambient
    pressure: Static RWST head
    flow_rate: —
    description: Suction header from Refueling Water Storage Tank
    source: PID-1-SI-LR20446
  - stream_id: STR-SI-P6A-DISCH
    direction: OUTLET
    source_tag: SI-P-6A
    target_tag: SI-X-25
    line_size: 4"
    inline_components:
    - SI-V96 (LO)
    - SI-V97 (Check)
    - FE-918
    - SI-V100
    - SI-V102 (MOV)
    temperature: Ambient to warmed
    pressure: 2235 PSIG (Relief V107)
    flow_rate: —
    description: Main 4" intermediate head safety injection header
    source: PID-1-SI-LR20446
  - stream_id: STR-SI-P6A-RECIRC
    direction: RECIRC
    source_tag: SI-P-6A
    target_tag: CBS-TK-8 (RWST)
    line_size: 1-1/2"x2"x3"
    inline_components:
    - SI-V90
    - SI-V91
    - SI-V93 (Check)
    - FE-968
    - SI-V259 (LO)
    temperature: Ambient
    pressure: Recirculation head
    flow_rate: —
    description: Minimum recirculation flow line back to RWST
    source: PID-1-SI-LR20446
  - stream_id: STR-SI-P6A-XOVER
    direction: OUTLET
    source_tag: SI-P-6A
    target_tag: SI-P-6B Discharge
    line_size: 3"
    inline_components:
    - SI-V111 (MOV)
    - SI-V112 (MOV)
    temperature: Ambient
    pressure: System pressure
    flow_rate: —
    description: Intermediate Head cross-tie header between Train A and Train B
    source: PID-1-SI-LR20446
  - stream_id: STR-SI-P6A-DRN
    direction: DRAIN
    source_tag: SI-P-6A
    target_tag: WLD DR 160
    line_size: 2"
    inline_components:
    - SI-V163
    - SI-V195
    - SI-V196
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Pump casing and base drain lines to liquid waste drains (20221 [D-6])
    source: PID-1-SI-LR20446
  - stream_id: STR-SI-P6A-CCW
    direction: UTILITY
    source_tag: CCW LOOP A
    target_tag: SI-P-6A
    line_size: 1"
    inline_components:
    - Isolation valves
    temperature: Cooling water
    pressure: Component cooling
    flow_rate: —
    description: Component Cooling Water supply and return to pump bearings/coolers
    source: PID-1-SI-LR20446
  - stream_id: STR-RH-TO-SIPA-SUCT
    direction: INLET
    source_tag: LOW HEAD SI TRAIN A (20448 [G-8])
    target_tag: SI-P-6A
    line_size: 8"
    inline_components:
    - RH-V22 (MOV)
    temperature: Ambient to 350°F
    pressure: RHR discharge head
    flow_rate: Suction flow rate
    description: Suction cross-tie from Low Head SI / RHR header via MOV RH-V22 to
      SI-P-6A suction
    source: PID-1-SI-LR20449
  - stream_id: STR-SI-P6A-LOOP1-INJ
    direction: OUTLET
    source_tag: SI-P-6A (20446 [C-4])
    target_tag: RCS LOOP 1 COLD LEG (20450 [A-11])
    line_size: 6"
    inline_components:
    - RH-V59 (Check)
    temperature: Borated water
    pressure: Cold leg injection pressure
    flow_rate: Injection flow
    description: Intermediate Head SI-P-6A discharge injection branch to RCS Loop
      1 Cold Leg
    source: PID-1-SI-LR20449
  - stream_id: STR-SI-P6A-LOOP2-INJ
    direction: OUTLET
    source_tag: SI-P-6A (20446 [D-4])
    target_tag: RCS LOOP 2 COLD LEG (20450 [B-11])
    line_size: 6"
    inline_components:
    - RH-V61 (Check)
    temperature: Borated water
    pressure: Cold leg injection pressure
    flow_rate: Injection flow
    description: Intermediate Head SI-P-6A discharge injection branch to RCS Loop
      2 Cold Leg
    source: PID-1-SI-LR20449
---

# SI-P-6A — Safety Injection Pump A (Intermediate Head)

## Function
Intermediate Head Safety Injection Pump A providing high-pressure emergency core cooling water from the Refueling Water Storage Tank (RWST) or Cold Leg/Hot Leg recirculation headers to the Reactor Coolant System (RCS) Loops during loss-of-coolant accidents (LOCA). Intermediate Head Safety Injection Pump A providing high-pressure emergency core cooling water from RWST or post-LOCA low-head recirculation cross-tie (via MOV RH-V22) delivering to RCS Loops 1 and 2 cold legs.

## Design Data
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20446 (Rev. 0, Ref. B20446 Rev. 17) | — | PID-1-SI-LR20446 |
| System Prefix | SI | — | PID-1-SI-LR20446 |
| Verbatim Printed Tag | SI-P-6A | — | PID-1-SI-LR20446 |
| Safety Classification | Safety Class 2 (Nuclear Safety Related) | — | PID-1-SI-LR20446 |
| AMR Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20446 |
| Physical Location | Primary Auxiliary Building Vault 1 (Inside Shielding) | — | PID-1-SI-LR20446 |
| Suction Nozzle Size | 6 | in | PID-1-SI-LR20446 |
| Suction Header Size | 8 | in | PID-1-SI-LR20446 (CBS-8") |
| Discharge Nozzle Size | 4 | in | PID-1-SI-LR20446 |
| Miniflow Line Size | 1.5 to 3 | in | PID-1-SI-LR20446 |
| Suction Relief Valve | CBS-V50 (Set @ 220 psig) | psig | PID-1-SI-LR20446 |
| Discharge Relief Valve | SI-V107 (Set @ 2235 psig) | psig | PID-1-SI-LR20446 |
| Drawing Reference | PID-1-SI-LR20449 (Rev. 0, Ref. B20449 Rev. 9) | — | PID-1-SI-LR20449 |
| Low Head Suction Cross-Tie Valve | RH-V22 (8" MOV) | — | PID-1-SI-LR20449 |

## Operating Conditions
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Primary Suction Source | RWST (Drawing 20233 [C-11]) via CBS-V47/V49 | — | PID-1-SI-LR20446 |
| Alternate Suction Source | RHR System Low Head Injection Header (20662 [F-7]) | — | PID-1-SI-LR20446 |
| Discharge Destination | Containment Penetration X-25 to RCS Loops | — | PID-1-SI-LR20446 |
| Miniflow Return Destination | RWST via common 3" return header (20233 [H-71]) | — | PID-1-SI-LR20446 |
| Cooling Utility Supply | Component Cooling Water CCW Loop A (20207 [E-11]) | — | PID-1-SI-LR20446 |
| Recirculation Suction Supply | RHR Train A discharge via 8" valve RH-V22 (20447 [A-7]) | — | PID-1-SI-LR20449 |

## Instrumentation & Control Loops (P&ID)
| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PI 977](/instruments/PI_977.md) | Pump Suction Pressure | Pressure Indicator (Local) | 6" CBS Suction Line | Local gauge | Local suction pressure indication | PID-1-SI-LR20446 |
| [PI 2412 A](/instruments/PI_2412_A.md) | Casing Suction Pressure | Pressure Indicator | Pump SI-P-6A Casing Tap | Local gauge | Direct pump casing suction pressure | PID-1-SI-LR20446 |
| [PI 2415 A](/instruments/PI_2415_A.md) | Pump Discharge Pressure | Pressure Indicator | 4" Discharge Line upstream of check V97 | Local gauge | Pump discharge head verification | PID-1-SI-LR20446 |
| [PT 919](/instruments/PT_919.md) | Discharge Header Pressure | Pressure Transmitter | 4" Discharge Header | Remote signal | Control room pressure indication & safety interlocks | PID-1-SI-LR20446 |
| [FE 918](/instruments/FE_918.md) | Discharge Flow Sensing Element | Flow Element (Orifice) | 4" Discharge Line upstream of V100 | Differential pressure | Primary injection flow measurement | PID-1-SI-LR20446 |
| [FT 918](/instruments/FT_918.md) | Discharge Flow Rate | Flow Transmitter | Across FE-918 (via V98/V99) | 4–20 mA | Control room flow indication & ESFAS verification | PID-1-SI-LR20446 |
| [FE 968](/instruments/FE_968.md) | Miniflow Recirculation Element | Flow Element (Orifice) | Common 3" Miniflow Line to RWST | Differential pressure | Measures combined minimum recirculation flow | PID-1-SI-LR20446 |
| [FI 968](/instruments/FI_968.md) | Miniflow Flow Rate | Flow Indicator | Across FE-968 | Local indicator | Verification of pump minimum flow protection | PID-1-SI-LR20446 |

## Connections & Stream Summary
| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-SI-P6A-SUCT | INLET | CBS-TK-8 (RWST) | SI-P-6A | 8"x6" | CBS-V47 (MOV), CBS-V48 (Check), CBS-V49 (MOV) | Borated ambient | Static RWST head | — | Suction header from Refueling Water Storage Tank |
| STR-SI-P6A-DISCH | OUTLET | SI-P-6A | SI-X-25 | 4" | SI-V96 (LO), SI-V97 (Check), FE-918, SI-V100, SI-V102 (MOV) | Ambient to warmed | 2235 PSIG (Relief V107) | — | Main 4" intermediate head safety injection header |
| STR-SI-P6A-RECIRC | RECIRC | SI-P-6A | CBS-TK-8 (RWST) | 1-1/2"x2"x3" | SI-V90, SI-V91, SI-V93 (Check), FE-968, SI-V259 (LO) | Ambient | Recirculation head | — | Minimum recirculation flow line back to RWST |
| STR-SI-P6A-XOVER | OUTLET | SI-P-6A | SI-P-6B Discharge | 3" | SI-V111 (MOV), SI-V112 (MOV) | Ambient | System pressure | — | Intermediate Head cross-tie header between Train A and Train B |
| STR-SI-P6A-DRN | DRAIN | SI-P-6A | WLD DR 160 | 2" | SI-V163, SI-V195, SI-V196 | Ambient | Atmospheric | — | Pump casing and base drain lines to liquid waste drains (20221 [D-6]) |
| STR-SI-P6A-CCW | UTILITY | CCW LOOP A | SI-P-6A | 1" | Isolation valves | Cooling water | Component cooling | — | Component Cooling Water supply and return to pump bearings/coolers |
| STR-RH-TO-SIPA-SUCT | INLET | LOW HEAD SI TRAIN A (20448 [G-8]) | SI-P-6A | 8" | RH-V22 (MOV) | Ambient to 350°F | RHR discharge head | Suction flow rate | Suction cross-tie from Low Head SI / RHR header via MOV RH-V22 to SI-P-6A suction |
| STR-SI-P6A-LOOP1-INJ | OUTLET | SI-P-6A (20446 [C-4]) | RCS LOOP 1 COLD LEG (20450 [A-11]) | 6" | RH-V59 (Check) | Borated water | Cold leg injection pressure | Injection flow | Intermediate Head SI-P-6A discharge injection branch to RCS Loop 1 Cold Leg |
| STR-SI-P6A-LOOP2-INJ | OUTLET | SI-P-6A (20446 [D-4]) | RCS LOOP 2 COLD LEG (20450 [B-11]) | 6" | RH-V61 (Check) | Borated water | Cold leg injection pressure | Injection flow | Intermediate Head SI-P-6A discharge injection branch to RCS Loop 2 Cold Leg |

## Hazards & Safeguards
- Pump runout protection: Throttle valve SI-V96 and branch flow trim valves SI-V103/SI-V104 are adjusted in the field to limit pump runout under low RCS backpressure conditions and locked per General Note 7.
- Minimum flow protection: Recirculation line with check valve SI-V93 and orifice prevents pump overheating and cavitation during shutoff head or deadheading operation.
- Suction overpressure: Relief valve CBS-V50 set at 220 psig protects the 6" suction line against inadvertent backflow overpressurization from the RCS.
- Discharge overpressure: Thermal/overpressure relief valve SI-V107 set at 2235 psig protects the discharge header.
- Safety interlock B logic: Controls valve RH-V35 interlocked with SI-V89, SI-V90, SI-V93 (20446), CBS-V8 (20448), RC-V22 and RC-V23 (20441) per Note 3.

## References & Sources
[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
[^src-2]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
