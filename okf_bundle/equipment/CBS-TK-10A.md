---
type: Equipment Concept
title: CBS-TK-10A — Containment Recirculation Sump A
description: Containment Recirculation Sump A providing a qualified suction reservoir
  for emergency core cooling and containment spray systems during post-LOCA recirculation
  mode. Features concentric guard pipe 1-CBS-S-611-A, expansion joint CBS-EP-36A,
  sealed protective chamber CBS-TK-101A housing motor-operated isolation valve CBS-V8,
  and level instrumentation.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/CBS-TK-10A.md
tags:
- equipment
- si / cbs
- sump / vessel
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-1.pdf
  title: ML101620329-part-1.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T12:48:22Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T12:48:22Z'
- by: process:okf-validation-suite
  at: '2026-10-02T12:48:22Z'
status: stable
entity_metadata:
  tag: CBS-TK-10A
  name: Containment Recirculation Sump A
  equipment_class: Sump / Vessel
  unit: SI / CBS
  instruments:
  - tag: LE-2384-1
    service: Containment Sump A Water Level Transmitter
    type: Level Element (Transmitter)
    location: CBS-TK-10A Sump (Grid E-12)
    setpoint_or_range: Safety level transmitter
    interlock_or_alarm: Post-accident containment sump water level transmission
    source: PID-1-SI-LR20448
  - tag: LE-2384-2
    service: Containment Sump A Water Level Transmitter
    type: Level Element (Transmitter)
    location: CBS-TK-10A Sump (Grid F-12)
    setpoint_or_range: Safety level transmitter
    interlock_or_alarm: Post-accident containment sump water level transmission (redundant)
    source: PID-1-SI-LR20448
  - tag: LE-2350
    service: Historical Level Sensor
    type: Level Element
    location: CBS-TK-10A / 10B Sump (Grid E-12)
    setpoint_or_range: 'Marked: NON-FUNCTIONAL'
    interlock_or_alarm: Decommissioned / non-functional instrument
    source: PID-1-SI-LR20448
  - tag: LS-2356
    service: Protective Chamber Leak Detection Level Switch
    type: Level Switch
    location: CBS-TK-101A Protective Chamber (Grid E-10)
    setpoint_or_range: Liquid detection switch
    interlock_or_alarm: Leak detection alarm in protective chamber
    source: PID-1-SI-LR20448
  connections:
  - stream_id: STR-CBS-TK10A-IN
    direction: INLET
    source_tag: CONTAINMENT FLOOR
    target_tag: CBS-TK-10A
    line_size: Sump Structure
    inline_components:
    - Sump screening / trash racks
    temperature: Post-accident containment water
    pressure: Containment atmospheric / post-LOCA pressure
    flow_rate: —
    description: Post-LOCA containment flood water collection into sump pit
    source: PID-1-SI-LR20448
  - stream_id: STR-CBS-TK10A-OUT
    direction: OUTLET
    source_tag: CBS-TK-10A
    target_tag: RH-P-8A / CBS-P-9A Suction
    line_size: 16"
    inline_components:
    - CBS-V8 (MOV)
    - CBS-EP-36A (Expansion Joint)
    - CBS-V115
    temperature: Post-accident containment water
    pressure: Sump static suction head
    flow_rate: —
    description: 16" suction effluent through guard pipe 1-CBS-S-611-A and penetration
      X-61 to RHR and Containment Spray pumps
    source: PID-1-SI-LR20448
  - stream_id: STR-CBS-TK10A-CHAMBER-DRN
    direction: DRAIN
    source_tag: CBS-TK-101A
    target_tag: WLD DR 153
    line_size: 1/2"x3/4"
    inline_components:
    - CBS-V88
    - CBS-V89
    - CBS-V92
    - CBS-V127
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Guard pipe / protective chamber air test and drainage
    source: PID-1-SI-LR20448
---

# CBS-TK-10A — Containment Recirculation Sump A

## Function

Containment Recirculation Sump A providing a qualified suction reservoir for emergency core cooling and containment spray systems during post-LOCA recirculation mode. Features concentric guard pipe 1-CBS-S-611-A, expansion joint CBS-EP-36A, sealed protective chamber CBS-TK-101A housing motor-operated isolation valve CBS-V8, and level instrumentation.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20448 (Rev. 11, Ref. B20448) | — | PID-1-SI-LR20448 |
| System Prefix | SI / CBS | — | PID-1-SI-LR20448 (General Note 2) |
| Verbatim Printed Tag | CBS-TK-10A | — | PID-1-SI-LR20448 |
| Safety Classification | Safety Class 2 (Nuclear Safety Related) | — | PID-1-SI-LR20448 |
| AMR Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20448 |
| Physical Location | Containment Building (Grid E-12) | — | PID-1-SI-LR20448 |
| Suction Effluent Header Size | 16 | in | PID-1-SI-LR20448 |
| Concentric Guard Pipe | 1-CBS-S-611-A (passing through Penetration X-61) | — | PID-1-SI-LR20448 |
| Protective Chamber Tag | CBS-TK-101A (Grid E-10) | — | PID-1-SI-LR20448 |
| Expansion Joint Tag | CBS-EP-36A (Grid E-10) | — | PID-1-SI-LR20448 |
| Sump Suction MOV | CBS-V8 (Motor Operated, Interlock A per Note 6) | — | PID-1-SI-LR20448 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Primary Operating Fluid | Post-LOCA Borated Water (RCS + RWST inventory) | — | PID-1-SI-LR20448 |
| Effluent Destination | RHR Pump RH-P-8A and Containment Spray Pump CBS-P-9A (20233 [A-10]) | — | PID-1-SI-LR20448 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LE-2384-1](/instruments/LE-2384-1.md) | Containment Sump A Water Level Transmitter | Level Element (Transmitter) | CBS-TK-10A Sump (Grid E-12) | Safety level transmitter | Post-accident containment sump water level transmission | PID-1-SI-LR20448 |
| [LE-2384-2](/instruments/LE-2384-2.md) | Containment Sump A Water Level Transmitter | Level Element (Transmitter) | CBS-TK-10A Sump (Grid F-12) | Safety level transmitter | Post-accident containment sump water level transmission (redundant) | PID-1-SI-LR20448 |
| [LE-2350](/instruments/LE-2350.md) | Historical Level Sensor | Level Element | CBS-TK-10A / 10B Sump (Grid E-12) | Marked: NON-FUNCTIONAL | Decommissioned / non-functional instrument | PID-1-SI-LR20448 |
| [LS-2356](/instruments/LS-2356.md) | Protective Chamber Leak Detection Level Switch | Level Switch | CBS-TK-101A Protective Chamber (Grid E-10) | Liquid detection switch | Leak detection alarm in protective chamber | PID-1-SI-LR20448 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-CBS-TK10A-IN | INLET | CONTAINMENT FLOOR | CBS-TK-10A | Sump Structure | Sump screening / trash racks | Post-accident containment water | Containment atmospheric / post-LOCA pressure | — | Post-LOCA containment flood water collection into sump pit |
| STR-CBS-TK10A-OUT | OUTLET | CBS-TK-10A | RH-P-8A / CBS-P-9A Suction | 16" | CBS-V8 (MOV), CBS-EP-36A (Expansion Joint), CBS-V115 | Post-accident containment water | Sump static suction head | — | 16" suction effluent through guard pipe 1-CBS-S-611-A and penetration X-61 to RHR and Containment Spray pumps |
| STR-CBS-TK10A-CHAMBER-DRN | DRAIN | CBS-TK-101A | WLD DR 153 | 1/2"x3/4" | CBS-V88, CBS-V89, CBS-V92, CBS-V127 | Ambient | Atmospheric | — | Guard pipe / protective chamber air test and drainage |

## Hazards & Safeguards

- Debris clogging / vortexing: Qualified emergency sump design to ensure continuous NPSH for RHR pump RH-P-8A and Containment Spray pump CBS-P-9A during recirculation.
- Valve interlock and containment integrity: Sump isolation valve CBS-V8 is interlocked to containment water levels CBS-LT-930..933 (Interlock A per Note 6) and enclosed in protective chamber CBS-TK-101A to prevent inadvertent opening before water level is established.
- Leak detection in guard pipe / chamber: Monitored by level switch LS-2356 inside protective chamber CBS-TK-101A.

## References & Sources

[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
