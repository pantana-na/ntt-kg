---
type: Equipment Concept
title: RH-E-9A — RHR Loop A Heat Exchanger
description: Residual Heat Removal Loop A Heat Exchanger cooling circulating reactor
  coolant during normal plant shutdown / cooldown and cooling emergency post-LOCA
  recirculation water from Containment Recirculation Sump A for low-head safety injection
  into the RCS Cold Legs and SI Accumulators. Cooled by 20" Component Cooling Water
  Loop A. Residual Heat Removal Loop A Heat Exchanger cooling circulating reactor
  coolant during normal plant shutdown/cooldown and cooling emergency post-LOCA recirculation
  water from Containment Recirculation Sump A for low-head safety injection into RCS
  Loops 1 and 2 Cold Legs and SI Accumulators via Penetration X-11. Also provides
  suction supply to High Head SI Pump SI-P-6A via valve RH-V22.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/RH-E-9A.md
tags:
- equipment
- heat exchanger
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
  at: '2026-10-02T13:18:00Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:18:00Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:18:00Z'
status: stable
entity_metadata:
  tag: RH-E-9A
  name: RHR Loop A Heat Exchanger
  equipment_class: Heat Exchanger
  unit: RH / SI
  instruments:
  - tag: TI-608
    service: RHR Loop A Cooled Effluent Temperature
    type: Temperature Indicator
    location: 12" Outlet Header (Grid H-3)
    setpoint_or_range: Remote readout
    interlock_or_alarm: Heat exchanger outlet process temperature indication
    source: PID-1-SI-LR20448
  - tag: RH-FCV-610
    service: RHR Cooldown Bypass Flow Control
    type: Flow Control Valve
    location: 8" Bypass Header (Grid E-5)
    setpoint_or_range: Throttling control valve
    interlock_or_alarm: Bypass flow regulation interlock (Interlock G)
    source: PID-1-SI-LR20448
  - tag: FT-618
    service: Train A Low Head SI Header Flow Transmitter
    type: Flow Transmitter
    location: Outside Shielding Vault 1 / Mechanical Penetration Area
    setpoint_or_range: Differential pressure across FE-618
    interlock_or_alarm: Flow indication to Control Room; signals FCV-618 bypass valve
    source: PID-1-SI-LR20449
  - tag: FE-618
    service: Train A Low Head SI Flow Element
    type: Flow Element
    location: Outside Shielding Vault 1 (8" line)
    setpoint_or_range: 3/4" sensing taps
    interlock_or_alarm: Flow element in 8" RH Train A header
    source: PID-1-SI-LR20449
  - tag: TE-604
    service: Train A Relief Line Temperature Monitoring
    type: Temperature Element
    location: Mechanical Penetration Area (1" inlet to RH-V13)
    setpoint_or_range: Fluid temperature
    interlock_or_alarm: Local/Remote temperature readout on relief line
    source: PID-1-SI-LR20449
  - tag: FE-2557
    service: Loop 1 Cold Leg Injection Flow Element
    type: Flow Element
    location: Inside Containment (6" line)
    setpoint_or_range: 3/4" taps with locked closed valves RH-V130/V131
    interlock_or_alarm: RCS Loop 1 injection flow measurement
    source: PID-1-SI-LR20449
  - tag: FE-2556
    service: Loop 2 Cold Leg Injection Flow Element
    type: Flow Element
    location: Inside Containment (6" line)
    setpoint_or_range: 3/4" taps with locked closed valves RH-V128/V129
    interlock_or_alarm: RCS Loop 2 injection flow measurement
    source: PID-1-SI-LR20449
  - tag: INTERLOCK-B
    service: Safety Interlock Logic on valve RH-V35
    type: Safety Interlock
    location: Shielding Vault 1 (SI-P-6A suction path)
    setpoint_or_range: Interlock logic B
    interlock_or_alarm: 'Safety Interlock B: Interlocked with SI-V89, SI-V90, SI-V93
      (20446), CBS-V8 (20448), RC-V22 & RC-V23 (20441)'
    source: PID-1-SI-LR20449
  connections:
  - stream_id: STR-RH-E9A-TUBE-IN
    direction: INLET
    source_tag: RH-P-8A
    target_tag: RH-E-9A
    line_size: 12"
    inline_components:
    - RH-V153 (Check)
    - RC-V140 (14" LC)
    temperature: Ambient to 350°F
    pressure: Pump discharge head
    flow_rate: —
    description: RHR Pump RH-P-8A discharge entering tube-side inlet nozzle
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-E9A-TUBE-OUT
    direction: OUTLET
    source_tag: RH-E-9A
    target_tag: SI ACCUM / RCS COLD LEGS (20449 [G-12])
    line_size: 12"x8"
    inline_components:
    - TI-608
    temperature: Cooled borated coolant (monitored by TI-608)
    pressure: Low head injection pressure
    flow_rate: —
    description: Cooled reactor coolant leaving tube-side outlet nozzle to low-head
      safety injection header
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-E9A-BYPASS
    direction: BYPASS
    source_tag: RH-P-8A Discharge
    target_tag: RH-E-9A Discharge Header
    line_size: 8"
    inline_components:
    - RH-FCV-610
    temperature: Uncooled coolant
    pressure: Discharge header pressure
    flow_rate: —
    description: Heat exchanger bypass line around RH-E-9A for temperature control
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-E9A-SHELL-IN
    direction: UTILITY
    source_tag: CCW LOOP A (20207 [D-11])
    target_tag: RH-E-9A Shell
    line_size: 20"
    inline_components:
    - Manual isolation valves
    temperature: Cooling water supply
    pressure: CCW header pressure
    flow_rate: —
    description: Component Cooling Water supply to shell side from CCW Loop A
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-E9A-SHELL-OUT
    direction: UTILITY
    source_tag: RH-E-9A Shell
    target_tag: CCW LOOP A (20207 [D-11])
    line_size: 20"
    inline_components:
    - Manual isolation valves
    temperature: Warmed CCW return
    pressure: CCW return pressure
    flow_rate: —
    description: Component Cooling Water return from shell side to CCW Loop A
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-E9A-DRN
    direction: DRAIN
    source_tag: RH-E-9A Nozzles
    target_tag: WLD DR 154
    line_size: 3/4"
    inline_components:
    - RH-V81
    - RH-V86
    - RH-V82..85
    - RH-V87
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Tube-side vents and drains discharging to liquid waste drainage
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-INJ-TRAIN-A
    direction: OUTLET
    source_tag: RH-E-9A
    target_tag: PENETRATION-X-11
    line_size: 8"
    inline_components:
    - RH-V18
    - HCV-606
    - FCV-618
    - FE-618
    - RH-V14
    temperature: Cooled borated water
    pressure: Low head injection pressure
    flow_rate: —
    description: Train A Low Head SI header from RH-E-9A and RH-P-8A routed through
      HCV-606/FCV-618, FE-618, RH-V14 to Penetration X-11
    source: PID-1-SI-LR20449
  - stream_id: STR-RH-LOOP1-INJ
    direction: OUTLET
    source_tag: PENETRATION-X-11
    target_tag: SI-TK-9A / RCS LOOP 1 COLD LEG
    line_size: 6"
    inline_components:
    - FE-2557
    - RH-V15
    - RH-V59
    temperature: Cooled borated water
    pressure: RCS Operating / Injection Pressure
    flow_rate: —
    description: Train A Low Head SI branch inside containment to RCS Loop 1 Cold
      Leg Injection via Accumulator flow path
    source: PID-1-SI-LR20449
  - stream_id: STR-RH-LOOP2-INJ
    direction: OUTLET
    source_tag: PENETRATION-X-11
    target_tag: SI-TK-9B / RCS LOOP 2 COLD LEG
    line_size: 6"
    inline_components:
    - FE-2556
    - RH-V31
    - RH-V61
    temperature: Cooled borated water
    pressure: RCS Operating / Injection Pressure
    flow_rate: —
    description: Train A Low Head SI branch inside containment to RCS Loop 2 Cold
      Leg Injection via Accumulator flow path
    source: PID-1-SI-LR20449
  - stream_id: STR-RH-TO-SIPA-SUCT
    direction: OUTLET
    source_tag: RH-E-9A
    target_tag: SI-P-6A
    line_size: 8"
    inline_components:
    - RH-V22
    temperature: Ambient to 350°F
    pressure: Pump suction pressure
    flow_rate: —
    description: Train A suction cross-tie from 8" RH header to High Head Safety Injection
      Pump SI-P-6A suction
    source: PID-1-SI-LR20449
  - stream_id: STR-RH-RELIEF-A
    direction: RELIEF
    source_tag: RH-E-9A
    target_tag: WLD DR 153
    line_size: 1"x3/4"
    inline_components:
    - RH-V13
    - TE-604
    - RH-V104
    temperature: Process fluid temp
    pressure: Set @ 600 PSIG
    flow_rate: —
    description: Thermal overpressure relief from Train A RH header to plant drain
      DR 153
    source: PID-1-SI-LR20449
---

# RH-E-9A — RHR Loop A Heat Exchanger

## Function
Residual Heat Removal Loop A Heat Exchanger cooling circulating reactor coolant during normal plant shutdown / cooldown and cooling emergency post-LOCA recirculation water from Containment Recirculation Sump A for low-head safety injection into the RCS Cold Legs and SI Accumulators. Cooled by 20" Component Cooling Water Loop A. Residual Heat Removal Loop A Heat Exchanger cooling circulating reactor coolant during normal plant shutdown/cooldown and cooling emergency post-LOCA recirculation water from Containment Recirculation Sump A for low-head safety injection into RCS Loops 1 and 2 Cold Legs and SI Accumulators via Penetration X-11. Also provides suction supply to High Head SI Pump SI-P-6A via valve RH-V22.

## Design Data
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20449 (Rev. 0, Ref. B20449 Rev. 9) (Rev. 11, Ref. B20448; PID-1-SI-LR20448: PID-1-SI-LR20448) | — | PID-1-SI-LR20448; PID-1-SI-LR20449 |
| System Prefix | SI / RH | — | PID-1-SI-LR20448 (General Note 2) |
| Verbatim Printed Tag | RH-E-9A | — | PID-1-SI-LR20448 |
| Safety Classification | Safety Class 2 (Tube Side) & Safety Class 3 (Shell Side) | — | PID-1-SI-LR20448 |
| AMR Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20448 |
| Physical Location | Primary Auxiliary Building Vault No. 1 - Inside Shielding (Grid H-3 / H-4) | — | PID-1-SI-LR20448 |
| Tube Side Process Inlet Nozzle Size | 12 | in | PID-1-SI-LR20448 |
| Tube Side Process Outlet Nozzle Size | 12 | in | PID-1-SI-LR20448 |
| Shell Side Utility Inlet / Outlet Size | 20 (CCW Loop A) | in | PID-1-SI-LR20448 |
| Bypass Header Size | 8 (with Flow Control Valve RH-FCV-610) | in | PID-1-SI-LR20448 |
| Containment Penetration A | X-11 (8" RH Line to Loops 1 & 2 Cold Legs) | — | PID-1-SI-LR20449 |
| Relief Valve Setting (RH-V13) | 600 | PSIG | PID-1-SI-LR20449 |

## Operating Conditions
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Tube Side Fluid | Borated Reactor Coolant / Sump Water | — | PID-1-SI-LR20448 |
| Shell Side Cooling Fluid | Component Cooling Water (CCW Loop A, Dwg 20207 [D-11]) | — | PID-1-SI-LR20448 |
| Tube Inlet Source | RHR Pump RH-P-8A 14" discharge header (reduced to 12") | — | PID-1-SI-LR20448 |
| Tube Outlet Destination | Low Head Injection Boric Acid path / SI Accumulator A (20449 [G-12]) | — | PID-1-SI-LR20448 |
| Downstream Injection Destination A1 | RCS Loop 1 Cold Leg Injection (Dwg 20450 [A-11]) | — | PID-1-SI-LR20449 |
| Downstream Injection Destination A2 | RCS Loop 2 Cold Leg Injection (Dwg 20450 [B-11]) | — | PID-1-SI-LR20449 |

## Instrumentation & Control Loops (P&ID)
| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TI-608](/instruments/TI-608.md) | RHR Loop A Cooled Effluent Temperature | Temperature Indicator | 12" Outlet Header (Grid H-3) | Remote readout | Heat exchanger outlet process temperature indication | PID-1-SI-LR20448 |
| [RH-FCV-610](/instruments/RH-FCV-610.md) | RHR Cooldown Bypass Flow Control | Flow Control Valve | 8" Bypass Header (Grid E-5) | Throttling control valve | Bypass flow regulation interlock (Interlock G) | PID-1-SI-LR20448 |
| [FT-618](/instruments/FT-618.md) | Train A Low Head SI Header Flow Transmitter | Flow Transmitter | Outside Shielding Vault 1 / Mechanical Penetration Area | Differential pressure across FE-618 | Flow indication to Control Room; signals FCV-618 bypass valve | PID-1-SI-LR20449 |
| [FE-618](/instruments/FE-618.md) | Train A Low Head SI Flow Element | Flow Element | Outside Shielding Vault 1 (8" line) | 3/4" sensing taps | Flow element in 8" RH Train A header | PID-1-SI-LR20449 |
| [TE-604](/instruments/TE-604.md) | Train A Relief Line Temperature Monitoring | Temperature Element | Mechanical Penetration Area (1" inlet to RH-V13) | Fluid temperature | Local/Remote temperature readout on relief line | PID-1-SI-LR20449 |
| [FE-2557](/instruments/FE-2557.md) | Loop 1 Cold Leg Injection Flow Element | Flow Element | Inside Containment (6" line) | 3/4" taps with locked closed valves RH-V130/V131 | RCS Loop 1 injection flow measurement | PID-1-SI-LR20449 |
| [FE-2556](/instruments/FE-2556.md) | Loop 2 Cold Leg Injection Flow Element | Flow Element | Inside Containment (6" line) | 3/4" taps with locked closed valves RH-V128/V129 | RCS Loop 2 injection flow measurement | PID-1-SI-LR20449 |
| [INTERLOCK-B](/instruments/INTERLOCK-B.md) | Safety Interlock Logic on valve RH-V35 | Safety Interlock | Shielding Vault 1 (SI-P-6A suction path) | Interlock logic B | Safety Interlock B: Interlocked with SI-V89, SI-V90, SI-V93 (20446), CBS-V8 (20448), RC-V22 & RC-V23 (20441) | PID-1-SI-LR20449 |

## Connections & Stream Summary
| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-RH-E9A-TUBE-IN | INLET | RH-P-8A | RH-E-9A | 12" | RH-V153 (Check), RC-V140 (14" LC) | Ambient to 350°F | Pump discharge head | — | RHR Pump RH-P-8A discharge entering tube-side inlet nozzle |
| STR-RH-E9A-TUBE-OUT | OUTLET | RH-E-9A | SI ACCUM / RCS COLD LEGS (20449 [G-12]) | 12"x8" | TI-608 | Cooled borated coolant (monitored by TI-608) | Low head injection pressure | — | Cooled reactor coolant leaving tube-side outlet nozzle to low-head safety injection header |
| STR-RH-E9A-BYPASS | BYPASS | RH-P-8A Discharge | RH-E-9A Discharge Header | 8" | RH-FCV-610 | Uncooled coolant | Discharge header pressure | — | Heat exchanger bypass line around RH-E-9A for temperature control |
| STR-RH-E9A-SHELL-IN | UTILITY | CCW LOOP A (20207 [D-11]) | RH-E-9A Shell | 20" | Manual isolation valves | Cooling water supply | CCW header pressure | — | Component Cooling Water supply to shell side from CCW Loop A |
| STR-RH-E9A-SHELL-OUT | UTILITY | RH-E-9A Shell | CCW LOOP A (20207 [D-11]) | 20" | Manual isolation valves | Warmed CCW return | CCW return pressure | — | Component Cooling Water return from shell side to CCW Loop A |
| STR-RH-E9A-DRN | DRAIN | RH-E-9A Nozzles | WLD DR 154 | 3/4" | RH-V81, RH-V86, RH-V82..85, RH-V87 | Ambient | Atmospheric | — | Tube-side vents and drains discharging to liquid waste drainage |
| STR-RH-INJ-TRAIN-A | OUTLET | RH-E-9A | PENETRATION-X-11 | 8" | RH-V18, HCV-606, FCV-618, FE-618, RH-V14 | Cooled borated water | Low head injection pressure | — | Train A Low Head SI header from RH-E-9A and RH-P-8A routed through HCV-606/FCV-618, FE-618, RH-V14 to Penetration X-11 |
| STR-RH-LOOP1-INJ | OUTLET | PENETRATION-X-11 | SI-TK-9A / RCS LOOP 1 COLD LEG | 6" | FE-2557, RH-V15, RH-V59 | Cooled borated water | RCS Operating / Injection Pressure | — | Train A Low Head SI branch inside containment to RCS Loop 1 Cold Leg Injection via Accumulator flow path |
| STR-RH-LOOP2-INJ | OUTLET | PENETRATION-X-11 | SI-TK-9B / RCS LOOP 2 COLD LEG | 6" | FE-2556, RH-V31, RH-V61 | Cooled borated water | RCS Operating / Injection Pressure | — | Train A Low Head SI branch inside containment to RCS Loop 2 Cold Leg Injection via Accumulator flow path |
| STR-RH-TO-SIPA-SUCT | OUTLET | RH-E-9A | SI-P-6A | 8" | RH-V22 | Ambient to 350°F | Pump suction pressure | — | Train A suction cross-tie from 8" RH header to High Head Safety Injection Pump SI-P-6A suction |
| STR-RH-RELIEF-A | RELIEF | RH-E-9A | WLD DR 153 | 1"x3/4" | RH-V13, TE-604, RH-V104 | Process fluid temp | Set @ 600 PSIG | — | Thermal overpressure relief from Train A RH header to plant drain DR 153 |

## Hazards & Safeguards
- Overcooling / thermal stress control: Controlled cooldown rate maintained via 8" bypass line flow control valve RH-FCV-610 interlocked with flow switch FIS-610 (Interlock G).
- Tube-to-shell barrier integrity: Tube side contains high-activity borated reactor coolant; shell side contains Component Cooling Water. Monitored for radioactive in-leakage to CCW.
- Drainage radiation safety: Multiple 3/4" vents and drains route to shielded floor drain funnel DR 154 (20221).
- Thermal overpressure protection provided by relief valve RH-V13 (Set @ 600 PSIG) monitored by TE-604 discharging to drain DR 153.
- Containment isolation barrier integrity via Penetration X-11 sleeve and MOV RH-V14.
- Handjack handwheel on HCV-606 locked open except during midloop operations per Drawing Note 8.
- ⚠️ CONFLICT — Drawing Number: PID-1-SI-LR20448 specifies PID-1-SI-LR20448, whereas PID-1-SI-LR20449 specifies PID-1-SI-LR20449 (Rev. 0, Ref. B20449 Rev. 9) — verify with engineer before HAZOP

## References & Sources
[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
[^src-2]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
