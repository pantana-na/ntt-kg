---
type: Equipment Concept
title: RH-E-9B — RHR Loop B Heat Exchanger
description: Residual Heat Removal Loop B Heat Exchanger cooling circulating reactor
  coolant during normal plant shutdown / cooldown and cooling emergency post-LOCA
  recirculation water from Containment Recirculation Sump B for low-head safety injection
  into the RCS Cold Legs and SI Accumulators. Cooled by 20" Component Cooling Water
  Loop B. Residual Heat Removal Loop B Heat Exchanger cooling circulating reactor
  coolant during normal plant shutdown/cooldown and cooling emergency post-LOCA recirculation
  water from Containment Recirculation Sump B for low-head safety injection into RCS
  Loops 3 and 4 Cold Legs and SI Accumulators via Penetration X-12. Also provides
  suction supply to Intermediate/High Head SI Pump SI-P-6B via valve RH-V21.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/RH-E-9B.md
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
  at: '2026-10-02T13:18:15Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:18:15Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:18:15Z'
status: stable
entity_metadata:
  tag: RH-E-9B
  name: RHR Loop B Heat Exchanger
  equipment_class: Heat Exchanger
  unit: RH / SI
  instruments:
  - tag: TI-609
    service: RHR Loop B Cooled Effluent Temperature
    type: Temperature Indicator
    location: 12" Outlet Header (Grid D-3)
    setpoint_or_range: Remote readout
    interlock_or_alarm: Heat exchanger outlet process temperature indication
    source: PID-1-SI-LR20448
  - tag: FT-619
    service: Train B Low Head SI Header Flow Transmitter
    type: Flow Transmitter
    location: Outside Shielding Vault 2 / Mechanical Penetration Area
    setpoint_or_range: Differential pressure across FE-619
    interlock_or_alarm: Flow indication to Control Room; signals FCV-619 bypass valve
    source: PID-1-SI-LR20449
  - tag: FE-619
    service: Train B Low Head SI Flow Element
    type: Flow Element
    location: Outside Shielding Vault 2 (8" line)
    setpoint_or_range: 3/4" sensing taps
    interlock_or_alarm: Flow element in 8" RH Train B header
    source: PID-1-SI-LR20449
  - tag: TE-605
    service: Train B Relief Line Temperature Monitoring
    type: Temperature Element
    location: Mechanical Penetration Area (1" inlet to RH-V25)
    setpoint_or_range: Fluid temperature
    interlock_or_alarm: Local/Remote temperature readout on relief line
    source: PID-1-SI-LR20449
  - tag: FE-2559
    service: Loop 4 Cold Leg Injection Flow Element
    type: Flow Element
    location: Inside Containment (6" line)
    setpoint_or_range: 3/4" taps with locked closed valves RH-V126/V127
    interlock_or_alarm: RCS Loop 4 injection flow measurement
    source: PID-1-SI-LR20449
  - tag: FE-2558
    service: Loop 3 Cold Leg Injection Flow Element
    type: Flow Element
    location: Inside Containment (6" line)
    setpoint_or_range: 3/4" taps with locked closed valves RH-V124/V125
    interlock_or_alarm: RCS Loop 3 injection flow measurement
    source: PID-1-SI-LR20449
  - tag: INTERLOCK-A
    service: Safety Interlock Logic on valve RH-V36
    type: Safety Interlock
    location: Shielding Vault 2 (SI-P-6B suction path)
    setpoint_or_range: Interlock logic A
    interlock_or_alarm: 'Safety Interlock A: Interlocked with SI-V89, SI-V90, SI-V93
      (20446), CBS-V14 (20448), RC-V87 & RC-V88 (20441)'
    source: PID-1-SI-LR20449
  connections:
  - stream_id: STR-RH-E9B-TUBE-IN
    direction: INLET
    source_tag: RH-P-8B
    target_tag: RH-E-9B
    line_size: 12"
    inline_components:
    - RH-V154 (Check)
    - RC-V141 (14" LC)
    temperature: Ambient to 350°F
    pressure: Pump discharge head
    flow_rate: —
    description: RHR Pump RH-P-8B discharge entering tube-side inlet nozzle
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-E9B-TUBE-OUT
    direction: OUTLET
    source_tag: RH-E-9B
    target_tag: SI ACCUM / RCS COLD LEGS (20449 [B-12])
    line_size: 12"x8"
    inline_components:
    - TI-609
    temperature: Cooled borated coolant (monitored by TI-609)
    pressure: Low head injection pressure
    flow_rate: —
    description: Cooled reactor coolant leaving tube-side outlet nozzle to low-head
      safety injection header
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-E9B-SHELL-IN
    direction: UTILITY
    source_tag: CCW LOOP B (20213 [D-6])
    target_tag: RH-E-9B Shell
    line_size: 20"
    inline_components:
    - Manual isolation valves
    temperature: Cooling water supply
    pressure: CCW header pressure
    flow_rate: —
    description: Component Cooling Water supply to shell side from CCW Loop B
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-E9B-SHELL-OUT
    direction: UTILITY
    source_tag: RH-E-9B Shell
    target_tag: CCW LOOP B (20213 [D-6])
    line_size: 20"
    inline_components:
    - Manual isolation valves
    temperature: Warmed CCW return
    pressure: CCW return pressure
    flow_rate: —
    description: Component Cooling Water return from shell side to CCW Loop B
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-E9B-DRN
    direction: DRAIN
    source_tag: RH-E-9B Nozzles
    target_tag: WLD DR 155
    line_size: 3/4"
    inline_components:
    - RH-V73
    - RH-V78
    - RH-V74..77
    - RH-V80
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Tube-side vents and drains discharging to liquid waste drainage
    source: PID-1-SI-LR20448
  - stream_id: STR-RH-INJ-TRAIN-B
    direction: OUTLET
    source_tag: RH-E-9B
    target_tag: PENETRATION-X-12
    line_size: 8"
    inline_components:
    - RH-V19
    - HCV-607
    - FCV-619
    - FE-619
    - RH-V26
    temperature: Cooled borated water
    pressure: Low head injection pressure
    flow_rate: —
    description: Train B Low Head SI header from RH-E-9B and RH-P-8B routed through
      HCV-607/FCV-619, FE-619, RH-V26 to Penetration X-12
    source: PID-1-SI-LR20449
  - stream_id: STR-RH-LOOP4-INJ
    direction: OUTLET
    source_tag: PENETRATION-X-12
    target_tag: SI-TK-9D / RCS LOOP 4 COLD LEG
    line_size: 6"
    inline_components:
    - FE-2559
    - RH-V30
    - RH-V65
    temperature: Cooled borated water
    pressure: RCS Operating / Injection Pressure
    flow_rate: —
    description: Train B Low Head SI branch inside containment to RCS Loop 4 Cold
      Leg Injection via Accumulator flow path
    source: PID-1-SI-LR20449
  - stream_id: STR-RH-LOOP3-INJ
    direction: OUTLET
    source_tag: PENETRATION-X-12
    target_tag: SI-TK-9C / RCS LOOP 3 COLD LEG
    line_size: 6"
    inline_components:
    - FE-2558
    - RH-V29
    - RH-V63
    temperature: Cooled borated water
    pressure: RCS Operating / Injection Pressure
    flow_rate: —
    description: Train B Low Head SI branch inside containment to RCS Loop 3 Cold
      Leg Injection via Accumulator flow path
    source: PID-1-SI-LR20449
  - stream_id: STR-RH-TO-SIPB-SUCT
    direction: OUTLET
    source_tag: RH-E-9B
    target_tag: SI-P-6B
    line_size: 8"
    inline_components:
    - RH-V21
    temperature: Ambient to 350°F
    pressure: Pump suction pressure
    flow_rate: —
    description: Train B suction cross-tie from 8" RH header to Intermediate/High
      Head Safety Injection Pump SI-P-6B suction
    source: PID-1-SI-LR20449
  - stream_id: STR-RH-RELIEF-B
    direction: RELIEF
    source_tag: RH-E-9B
    target_tag: WLD DR 152
    line_size: 1"x3/4"
    inline_components:
    - RH-V25
    - TE-605
    - RH-V106
    temperature: Process fluid temp
    pressure: Set @ 600 PSIG
    flow_rate: —
    description: Thermal overpressure relief from Train B RH header to plant drain
      DR 152
    source: PID-1-SI-LR20449
---

# RH-E-9B — RHR Loop B Heat Exchanger

## Function
Residual Heat Removal Loop B Heat Exchanger cooling circulating reactor coolant during normal plant shutdown / cooldown and cooling emergency post-LOCA recirculation water from Containment Recirculation Sump B for low-head safety injection into the RCS Cold Legs and SI Accumulators. Cooled by 20" Component Cooling Water Loop B. Residual Heat Removal Loop B Heat Exchanger cooling circulating reactor coolant during normal plant shutdown/cooldown and cooling emergency post-LOCA recirculation water from Containment Recirculation Sump B for low-head safety injection into RCS Loops 3 and 4 Cold Legs and SI Accumulators via Penetration X-12. Also provides suction supply to Intermediate/High Head SI Pump SI-P-6B via valve RH-V21.

## Design Data
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20449 (Rev. 0, Ref. B20449 Rev. 9) (Rev. 11, Ref. B20448; PID-1-SI-LR20448: PID-1-SI-LR20448) | — | PID-1-SI-LR20448; PID-1-SI-LR20449 |
| System Prefix | SI / RH | — | PID-1-SI-LR20448 (General Note 2) |
| Verbatim Printed Tag | RH-E-9B | — | PID-1-SI-LR20448 |
| Safety Classification | Safety Class 2 (Tube Side) & Safety Class 3 (Shell Side) | — | PID-1-SI-LR20448 |
| AMR Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20448 |
| Physical Location | Primary Auxiliary Building Vault No. 2 - Inside Shielding (Grid D-3 / E-3) | — | PID-1-SI-LR20448 |
| Tube Side Process Inlet Nozzle Size | 12 | in | PID-1-SI-LR20448 |
| Tube Side Process Outlet Nozzle Size | 12 | in | PID-1-SI-LR20448 |
| Shell Side Utility Inlet / Outlet Size | 20 (CCW Loop B) | in | PID-1-SI-LR20448 |
| Containment Penetration B | X-12 (8" RH Line to Loops 3 & 4 Cold Legs) | — | PID-1-SI-LR20449 |
| Relief Valve Setting (RH-V25) | 600 | PSIG | PID-1-SI-LR20449 |

## Operating Conditions
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Tube Side Fluid | Borated Reactor Coolant / Sump Water | — | PID-1-SI-LR20448 |
| Shell Side Cooling Fluid | Component Cooling Water (CCW Loop B, Dwg 20213 [D-6]) | — | PID-1-SI-LR20448 |
| Tube Inlet Source | RHR Pump RH-P-8B 14" discharge header (reduced to 12") | — | PID-1-SI-LR20448 |
| Tube Outlet Destination | Low Head Injection Boric Acid path / SI Accumulator B (20449 [B-12]) | — | PID-1-SI-LR20448 |
| Downstream Injection Destination B1 | RCS Loop 4 Cold Leg Injection (Dwg 20450 [B-7]) | — | PID-1-SI-LR20449 |
| Downstream Injection Destination B2 | RCS Loop 3 Cold Leg Injection (Dwg 20450 [B-9]) | — | PID-1-SI-LR20449 |

## Instrumentation & Control Loops (P&ID)
| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TI-609](/instruments/TI-609.md) | RHR Loop B Cooled Effluent Temperature | Temperature Indicator | 12" Outlet Header (Grid D-3) | Remote readout | Heat exchanger outlet process temperature indication | PID-1-SI-LR20448 |
| [FT-619](/instruments/FT-619.md) | Train B Low Head SI Header Flow Transmitter | Flow Transmitter | Outside Shielding Vault 2 / Mechanical Penetration Area | Differential pressure across FE-619 | Flow indication to Control Room; signals FCV-619 bypass valve | PID-1-SI-LR20449 |
| [FE-619](/instruments/FE-619.md) | Train B Low Head SI Flow Element | Flow Element | Outside Shielding Vault 2 (8" line) | 3/4" sensing taps | Flow element in 8" RH Train B header | PID-1-SI-LR20449 |
| [TE-605](/instruments/TE-605.md) | Train B Relief Line Temperature Monitoring | Temperature Element | Mechanical Penetration Area (1" inlet to RH-V25) | Fluid temperature | Local/Remote temperature readout on relief line | PID-1-SI-LR20449 |
| [FE-2559](/instruments/FE-2559.md) | Loop 4 Cold Leg Injection Flow Element | Flow Element | Inside Containment (6" line) | 3/4" taps with locked closed valves RH-V126/V127 | RCS Loop 4 injection flow measurement | PID-1-SI-LR20449 |
| [FE-2558](/instruments/FE-2558.md) | Loop 3 Cold Leg Injection Flow Element | Flow Element | Inside Containment (6" line) | 3/4" taps with locked closed valves RH-V124/V125 | RCS Loop 3 injection flow measurement | PID-1-SI-LR20449 |
| [INTERLOCK-A](/instruments/INTERLOCK-A.md) | Safety Interlock Logic on valve RH-V36 | Safety Interlock | Shielding Vault 2 (SI-P-6B suction path) | Interlock logic A | Safety Interlock A: Interlocked with SI-V89, SI-V90, SI-V93 (20446), CBS-V14 (20448), RC-V87 & RC-V88 (20441) | PID-1-SI-LR20449 |

## Connections & Stream Summary
| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-RH-E9B-TUBE-IN | INLET | RH-P-8B | RH-E-9B | 12" | RH-V154 (Check), RC-V141 (14" LC) | Ambient to 350°F | Pump discharge head | — | RHR Pump RH-P-8B discharge entering tube-side inlet nozzle |
| STR-RH-E9B-TUBE-OUT | OUTLET | RH-E-9B | SI ACCUM / RCS COLD LEGS (20449 [B-12]) | 12"x8" | TI-609 | Cooled borated coolant (monitored by TI-609) | Low head injection pressure | — | Cooled reactor coolant leaving tube-side outlet nozzle to low-head safety injection header |
| STR-RH-E9B-SHELL-IN | UTILITY | CCW LOOP B (20213 [D-6]) | RH-E-9B Shell | 20" | Manual isolation valves | Cooling water supply | CCW header pressure | — | Component Cooling Water supply to shell side from CCW Loop B |
| STR-RH-E9B-SHELL-OUT | UTILITY | RH-E-9B Shell | CCW LOOP B (20213 [D-6]) | 20" | Manual isolation valves | Warmed CCW return | CCW return pressure | — | Component Cooling Water return from shell side to CCW Loop B |
| STR-RH-E9B-DRN | DRAIN | RH-E-9B Nozzles | WLD DR 155 | 3/4" | RH-V73, RH-V78, RH-V74..77, RH-V80 | Ambient | Atmospheric | — | Tube-side vents and drains discharging to liquid waste drainage |
| STR-RH-INJ-TRAIN-B | OUTLET | RH-E-9B | PENETRATION-X-12 | 8" | RH-V19, HCV-607, FCV-619, FE-619, RH-V26 | Cooled borated water | Low head injection pressure | — | Train B Low Head SI header from RH-E-9B and RH-P-8B routed through HCV-607/FCV-619, FE-619, RH-V26 to Penetration X-12 |
| STR-RH-LOOP4-INJ | OUTLET | PENETRATION-X-12 | SI-TK-9D / RCS LOOP 4 COLD LEG | 6" | FE-2559, RH-V30, RH-V65 | Cooled borated water | RCS Operating / Injection Pressure | — | Train B Low Head SI branch inside containment to RCS Loop 4 Cold Leg Injection via Accumulator flow path |
| STR-RH-LOOP3-INJ | OUTLET | PENETRATION-X-12 | SI-TK-9C / RCS LOOP 3 COLD LEG | 6" | FE-2558, RH-V29, RH-V63 | Cooled borated water | RCS Operating / Injection Pressure | — | Train B Low Head SI branch inside containment to RCS Loop 3 Cold Leg Injection via Accumulator flow path |
| STR-RH-TO-SIPB-SUCT | OUTLET | RH-E-9B | SI-P-6B | 8" | RH-V21 | Ambient to 350°F | Pump suction pressure | — | Train B suction cross-tie from 8" RH header to Intermediate/High Head Safety Injection Pump SI-P-6B suction |
| STR-RH-RELIEF-B | RELIEF | RH-E-9B | WLD DR 152 | 1"x3/4" | RH-V25, TE-605, RH-V106 | Process fluid temp | Set @ 600 PSIG | — | Thermal overpressure relief from Train B RH header to plant drain DR 152 |

## Hazards & Safeguards
- Tube-to-shell barrier integrity: Monitored for radioactive in-leakage from borated primary coolant into Component Cooling Water.
- Drainage radiation safety: Multiple 3/4" vents and drains route to shielded floor drain funnel DR 155 (20221).
- Decay heat removal reliability: Redundant to RH-E-9A to ensure continuous core decay heat removal capacity.
- Thermal overpressure protection provided by relief valve RH-V25 (Set @ 600 PSIG) monitored by TE-605 discharging to drain DR 152.
- Containment isolation barrier integrity via Penetration X-12 sleeve and MOV RH-V26.
- Handjack handwheel on HCV-607 locked open except during midloop operations per Drawing Note 8.
- ⚠️ CONFLICT — Drawing Number: PID-1-SI-LR20448 specifies PID-1-SI-LR20448, whereas PID-1-SI-LR20449 specifies PID-1-SI-LR20449 (Rev. 0, Ref. B20449 Rev. 9) — verify with engineer before HAZOP

## References & Sources
[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
[^src-2]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
