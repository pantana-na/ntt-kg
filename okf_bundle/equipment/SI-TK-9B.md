---
type: Equipment Concept
title: SI-TK-9B — Safety Injection Accumulator Tank B
description: Safety Injection Accumulator Tank B providing rapid, passive injection
  of borated water into Reactor Coolant System (RCS) Loop 2 Cold Leg during large
  or intermediate LOCA events when RCS pressure drops below the accumulator N2 blanket
  pressure (~650 psig).
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SI-TK-9B.md
tags:
- equipment
- si
- vessel
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-2.pdf
  title: ML101620329-part-2.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:19:10Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:19:10Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:19:10Z'
status: stable
entity_metadata:
  tag: SI-TK-9B
  name: Safety Injection Accumulator Tank B
  equipment_class: Vessel
  unit: SI
  instruments:
  - tag: LT-952
    service: Accumulator B Water Level Transmitter
    type: Level Transmitter
    location: On 66" min standpipe (valves V209/V210)
    setpoint_or_range: Taps ±8" around normal scribe mark
    interlock_or_alarm: Dual narrow-range level indication and control room alarm
    source: PID-1-SI-LR20450
  - tag: LT-953
    service: Accumulator B Water Level Transmitter
    type: Level Transmitter
    location: On 66" min standpipe (valves V211/V212)
    setpoint_or_range: Taps ±8" around normal scribe mark
    interlock_or_alarm: Redundant narrow-range level indication and control room alarm
    source: PID-1-SI-LR20450
  - tag: PT-962
    service: Accumulator B Pressure Transmitter
    type: Pressure Transmitter
    location: Tank Top Head (valve V251)
    setpoint_or_range: 600–700 PSIG normal band
    interlock_or_alarm: Dual pressure indication and low/high pressure alarm in MCR
    source: PID-1-SI-LR20450
  - tag: PT-963
    service: Accumulator B Pressure Transmitter
    type: Pressure Transmitter
    location: Tank Top Head (valve V252)
    setpoint_or_range: 600–700 PSIG normal band
    interlock_or_alarm: Redundant pressure indication and alarm in MCR
    source: PID-1-SI-LR20450
  - tag: FV-2482
    service: Accumulator B Vent Solenoid Valve
    type: Control Valve
    location: Vent header to ATM
    setpoint_or_range: Fail Closed (FC)
    interlock_or_alarm: Remote solenoid actuation; Fail Closed
    source: PID-1-SI-LR20450
  - tag: FV-2483
    service: Accumulator B Vent Solenoid Valve
    type: Control Valve
    location: Vent header to ATM
    setpoint_or_range: Fail Closed (FC)
    interlock_or_alarm: Remote solenoid actuation; Fail Closed
    source: PID-1-SI-LR20450
  connections:
  - stream_id: STR-SI-ACCUM-B-DISCH
    direction: OUTLET
    source_tag: SI-TK-9B
    target_tag: RCS LOOP 2 COLD LEG (20842 [D-12])
    line_size: 10" (Sch 140)
    inline_components:
    - 3/8" Flow Restrictor (bullet A)
    - SI-V17 (MOV)
    - SI-V20 (Check)
    temperature: Ambient borated water
    pressure: 600–700 PSIG passive injection pressure
    flow_rate: Safety analysis injection capacity
    description: Passive 10" cold leg injection line into RCS Loop 2 Cold Leg through
      3/8" flow restrictor, MOV SI-V17, and check valve SI-V20
    source: PID-1-SI-LR20450
  - stream_id: STR-SI-ACCUM-B-RHR-TIE
    direction: INLET
    source_tag: RH-E-9B (20449 [B-11])
    target_tag: SI-TK-9B Discharge Line
    line_size: 10"x6"
    inline_components:
    - RH-V61 (LO Check)
    - RH-V31 (Check)
    temperature: Cooled borated water
    pressure: RHR injection pressure
    flow_rate: —
    description: Low Head Safety Injection tie-in from RHR Train B HX RH-E-9B to Accumulator
      B discharge line
    source: PID-1-SI-LR20450
  - stream_id: STR-SI-ACCUM-B-N2
    direction: INLET
    source_tag: NITROGEN GAS (20136)
    target_tag: SI-TK-9B
    line_size: 1"
    inline_components:
    - NG-V251
    temperature: Ambient
    pressure: Approx. 650 PSIG
    flow_rate: —
    description: 1" Nitrogen gas cover blanket supply from Nitrogen Gas System
    source: PID-1-SI-LR20450
  - stream_id: STR-SI-ACCUM-B-VENT
    direction: VENT
    source_tag: SI-TK-9B
    target_tag: ATM
    line_size: 1"
    inline_components:
    - FV-2482 (FC)
    - FV-2483 (FC)
    temperature: Ambient
    pressure: Atmospheric vent
    flow_rate: —
    description: Accumulator N2 vent header to atmosphere via solenoid vent valves
      FV-2482 and FV-2483
    source: PID-1-SI-LR20450
  - stream_id: STR-SI-ACCUM-B-RELIEF
    direction: RELIEF
    source_tag: SI-TK-9B
    target_tag: ATM / DRAIN
    line_size: 1"
    inline_components:
    - SI-V30 (Set @ 700 PSIG)
    temperature: Ambient
    pressure: Set @ 700 PSIG
    flow_rate: —
    description: Safety relief valve SI-V30 overpressure discharge
    source: PID-1-SI-LR20450
  - stream_id: STR-SI-ACCUM-B-FILL
    direction: INLET
    source_tag: PENETRATION-X-35
    target_tag: SI-TK-9B
    line_size: 3/4"
    inline_components:
    - SI-V61 (LC)
    - SI-V62 (Check)
    - SI-V26
    temperature: Ambient
    pressure: Fill pump head
    flow_rate: —
    description: 3/4" borated water fill line from RWST and Boron Recovery through
      Penetration X-35
    source: PID-1-SI-LR20450
  - stream_id: STR-SI-ACCUM-B-DRAIN
    direction: DRAIN
    source_tag: SI-TK-9B
    target_tag: WLD DR 141
    line_size: 3/4"
    inline_components:
    - SI-V286
    - SI-V302
    - Blind Flange
    temperature: Ambient borated water
    pressure: Atmospheric
    flow_rate: —
    description: Accumulator drain line to containment drain DR 141 provided with
      blind flange and spool piece per Note 3
    source: PID-1-SI-LR20450
  - stream_id: STR-SI-ACCUM-B-SAMPLE
    direction: OUTLET
    source_tag: SI-TK-9B
    target_tag: WLD DR 141 / V8001
    line_size: 3/4"
    inline_components:
    - SI-V21
    temperature: Ambient
    pressure: Accumulator pressure
    flow_rate: —
    description: Local sample line to containment drain DR 141 via valve SI-V21 /
      V8001
    source: PID-1-SI-LR20450
---

# SI-TK-9B — Safety Injection Accumulator Tank B

## Function

Safety Injection Accumulator Tank B providing rapid, passive injection of borated water into Reactor Coolant System (RCS) Loop 2 Cold Leg during large or intermediate LOCA events when RCS pressure drops below the accumulator N2 blanket pressure (~650 psig).

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20450 (Rev. 14) | — | PID-1-SI-LR20450 |
| Safety Classification | Safety Class 2 (Nuclear Safety Related) | — | PID-1-SI-LR20450 |
| AMR Scoping Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20450 |
| Discharge Header Nominal Diameter | 10 | in | PID-1-SI-LR20450 |
| Discharge Piping Schedule | Schedule 140 (Mandatory per Note 10) | — | PID-1-SI-LR20450 |
| Flow Restrictor Size | 3/8 (Detail on DWG RC-20848 per Note 8) | in | PID-1-SI-LR20450 |
| Standpipe Minimum Height | 66 (per Note 6) | in | PID-1-SI-LR20450 |
| Level Transmitter Tap Offset | ±8 from scribe mark (per Note 6) | in | PID-1-SI-LR20450 |
| Relief Valve Set Pressure (SI-V30) | 700 | PSIG | PID-1-SI-LR20450 |
| Discharge Isolation Valve (SI-V17) Type | 10" Motor-Operated Gate Valve with Stem Leak-Off to VSL | — | PID-1-SI-LR20450 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Operating Fluid | Borated Water with Nitrogen Gas Blanket | — | PID-1-SI-LR20450 |
| Operating Pressure Band | 600–700 | PSIG | PID-1-SI-LR20450 |
| Normal Operating Temperature | Ambient Containment Temperature (~70–120) | °F | PID-1-SI-LR20450 |
| Injection Flow Destination | Reactor Coolant Loop 2 Cold Leg Injection (DWG 20842 / H [D-12]) | — | PID-1-SI-LR20450 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LT-952](/instruments/LT-952.md) | Accumulator B Water Level Transmitter | Level Transmitter | On 66" min standpipe (valves V209/V210) | Taps ±8" around normal scribe mark | Dual narrow-range level indication and control room alarm | PID-1-SI-LR20450 |
| [LT-953](/instruments/LT-953.md) | Accumulator B Water Level Transmitter | Level Transmitter | On 66" min standpipe (valves V211/V212) | Taps ±8" around normal scribe mark | Redundant narrow-range level indication and control room alarm | PID-1-SI-LR20450 |
| [PT-962](/instruments/PT-962.md) | Accumulator B Pressure Transmitter | Pressure Transmitter | Tank Top Head (valve V251) | 600–700 PSIG normal band | Dual pressure indication and low/high pressure alarm in MCR | PID-1-SI-LR20450 |
| [PT-963](/instruments/PT-963.md) | Accumulator B Pressure Transmitter | Pressure Transmitter | Tank Top Head (valve V252) | 600–700 PSIG normal band | Redundant pressure indication and alarm in MCR | PID-1-SI-LR20450 |
| [FV-2482](/instruments/FV-2482.md) | Accumulator B Vent Solenoid Valve | Control Valve | Vent header to ATM | Fail Closed (FC) | Remote solenoid actuation; Fail Closed | PID-1-SI-LR20450 |
| [FV-2483](/instruments/FV-2483.md) | Accumulator B Vent Solenoid Valve | Control Valve | Vent header to ATM | Fail Closed (FC) | Remote solenoid actuation; Fail Closed | PID-1-SI-LR20450 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-SI-ACCUM-B-DISCH | OUTLET | SI-TK-9B | RCS LOOP 2 COLD LEG (20842 [D-12]) | 10" (Sch 140) | 3/8" Flow Restrictor (bullet A), SI-V17 (MOV), SI-V20 (Check) | Ambient borated water | 600–700 PSIG passive injection pressure | Safety analysis injection capacity | Passive 10" cold leg injection line into RCS Loop 2 Cold Leg through 3/8" flow restrictor, MOV SI-V17, and check valve SI-V20 |
| STR-SI-ACCUM-B-RHR-TIE | INLET | RH-E-9B (20449 [B-11]) | SI-TK-9B Discharge Line | 10"x6" | RH-V61 (LO Check), RH-V31 (Check) | Cooled borated water | RHR injection pressure | — | Low Head Safety Injection tie-in from RHR Train B HX RH-E-9B to Accumulator B discharge line |
| STR-SI-ACCUM-B-N2 | INLET | NITROGEN GAS (20136) | SI-TK-9B | 1" | NG-V251 | Ambient | Approx. 650 PSIG | — | 1" Nitrogen gas cover blanket supply from Nitrogen Gas System |
| STR-SI-ACCUM-B-VENT | VENT | SI-TK-9B | ATM | 1" | FV-2482 (FC), FV-2483 (FC) | Ambient | Atmospheric vent | — | Accumulator N2 vent header to atmosphere via solenoid vent valves FV-2482 and FV-2483 |
| STR-SI-ACCUM-B-RELIEF | RELIEF | SI-TK-9B | ATM / DRAIN | 1" | SI-V30 (Set @ 700 PSIG) | Ambient | Set @ 700 PSIG | — | Safety relief valve SI-V30 overpressure discharge |
| STR-SI-ACCUM-B-FILL | INLET | PENETRATION-X-35 | SI-TK-9B | 3/4" | SI-V61 (LC), SI-V62 (Check), SI-V26 | Ambient | Fill pump head | — | 3/4" borated water fill line from RWST and Boron Recovery through Penetration X-35 |
| STR-SI-ACCUM-B-DRAIN | DRAIN | SI-TK-9B | WLD DR 141 | 3/4" | SI-V286, SI-V302, Blind Flange | Ambient borated water | Atmospheric | — | Accumulator drain line to containment drain DR 141 provided with blind flange and spool piece per Note 3 |
| STR-SI-ACCUM-B-SAMPLE | OUTLET | SI-TK-9B | WLD DR 141 / V8001 | 3/4" | SI-V21 | Ambient | Accumulator pressure | — | Local sample line to containment drain DR 141 via valve SI-V21 / V8001 |

## Hazards & Safeguards

- RCS backpressure protection: Series check valve SI-V20 and downstream RCS check valve prevent high-pressure RCS coolant (2235 psig) from backfeeding into the accumulator.
- Piping wall thickness / hydraulic restriction: Schedule 140 piping must be strictly adhered to due to safety analysis flow requirements per General Note 10.
- Overpressurization protection: Safety relief valve SI-V30 set at 700 PSIG prevents tank overpressure during nitrogen charging.
- Drain isolation safety: Accumulator drain is provided with a blind flange; spool piece to be installed only during draining per General Note 3.

## References & Sources

[^src-1]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
