---
type: Equipment Concept
title: CBS-TK-10B — Containment Recirculation Sump B
description: Containment Recirculation Sump B providing a redundant, qualified suction
  reservoir for emergency core cooling and containment spray systems during post-LOCA
  recirculation mode. Features concentric guard pipe 1-CBS-S-611-B, expansion joint
  CBS-EP-36B, sealed protective chamber CBS-TK-101B housing motor-operated isolation
  valve CBS-V14, and level instrumentation.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/CBS-TK-10B.md
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
  at: '2026-10-02T12:48:37Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T12:48:37Z'
- by: process:okf-validation-suite
  at: '2026-10-02T12:48:37Z'
status: stable
entity_metadata:
  tag: CBS-TK-10B
  name: Containment Recirculation Sump B
  equipment_class: Sump / Vessel
  unit: SI / CBS
  instruments:
  - tag: LE-2385-1
    service: Containment Sump B Water Level Transmitter
    type: Level Element (Transmitter)
    location: CBS-TK-10B Sump (Grid D-12)
    setpoint_or_range: Safety level transmitter
    interlock_or_alarm: Post-accident containment sump water level transmission
    source: PID-1-SI-LR20448
  - tag: LE-2385-2
    service: Containment Sump B Water Level Transmitter
    type: Level Element (Transmitter)
    location: CBS-TK-10B Sump (Grid D-12)
    setpoint_or_range: Safety level transmitter
    interlock_or_alarm: Post-accident containment sump water level transmission (redundant)
    source: PID-1-SI-LR20448
  - tag: LS-2357
    service: Protective Chamber Leak Detection Level Switch
    type: Level Switch
    location: CBS-TK-101B Protective Chamber (Grid D-10)
    setpoint_or_range: Liquid detection switch
    interlock_or_alarm: Leak detection alarm in protective chamber
    source: PID-1-SI-LR20448
  connections:
  - stream_id: STR-CBS-TK10B-IN
    direction: INLET
    source_tag: CONTAINMENT FLOOR
    target_tag: CBS-TK-10B
    line_size: Sump Structure
    inline_components:
    - Sump screening / trash racks
    temperature: Post-accident containment water
    pressure: Containment atmospheric / post-LOCA pressure
    flow_rate: —
    description: Post-LOCA containment flood water collection into sump pit
    source: PID-1-SI-LR20448
  - stream_id: STR-CBS-TK10B-OUT
    direction: OUTLET
    source_tag: CBS-TK-10B
    target_tag: RH-P-8B / CBS-P-9B Suction
    line_size: 16"
    inline_components:
    - CBS-V14 (MOV)
    - CBS-EP-36B (Expansion Joint)
    - CBS-V116
    temperature: Post-accident containment water
    pressure: Sump static suction head
    flow_rate: —
    description: 16" suction effluent through guard pipe 1-CBS-S-611-B and penetration
      X-60 to RHR and Containment Spray pumps
    source: PID-1-SI-LR20448
  - stream_id: STR-CBS-TK10B-CHAMBER-DRN
    direction: DRAIN
    source_tag: CBS-TK-101B
    target_tag: WLD DR 152
    line_size: 1/2"x3/4"
    inline_components:
    - CBS-V90
    - CBS-V91
    - CBS-V128
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Guard pipe / protective chamber air test and drainage
    source: PID-1-SI-LR20448
---

# CBS-TK-10B — Containment Recirculation Sump B

## Function

Containment Recirculation Sump B providing a redundant, qualified suction reservoir for emergency core cooling and containment spray systems during post-LOCA recirculation mode. Features concentric guard pipe 1-CBS-S-611-B, expansion joint CBS-EP-36B, sealed protective chamber CBS-TK-101B housing motor-operated isolation valve CBS-V14, and level instrumentation.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20448 (Rev. 11, Ref. B20448) | — | PID-1-SI-LR20448 |
| System Prefix | SI / CBS | — | PID-1-SI-LR20448 (General Note 2) |
| Verbatim Printed Tag | CBS-TK-10B | — | PID-1-SI-LR20448 |
| Safety Classification | Safety Class 2 (Nuclear Safety Related) | — | PID-1-SI-LR20448 |
| AMR Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20448 |
| Physical Location | Containment Building (Grid D-12) | — | PID-1-SI-LR20448 |
| Suction Effluent Header Size | 16 | in | PID-1-SI-LR20448 |
| Concentric Guard Pipe | 1-CBS-S-611-B (passing through Penetration X-60) | — | PID-1-SI-LR20448 |
| Protective Chamber Tag | CBS-TK-101B (Grid D-10) | — | PID-1-SI-LR20448 |
| Expansion Joint Tag | CBS-EP-36B (Grid D-10) | — | PID-1-SI-LR20448 |
| Sump Suction MOV | CBS-V14 (Motor Operated, Interlock A per Note 6) | — | PID-1-SI-LR20448 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Primary Operating Fluid | Post-LOCA Borated Water (RCS + RWST inventory) | — | PID-1-SI-LR20448 |
| Effluent Destination | RHR Pump RH-P-8B and Containment Spray Pump CBS-P-9B (20233 [A-10]) | — | PID-1-SI-LR20448 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LE-2385-1](/instruments/LE-2385-1.md) | Containment Sump B Water Level Transmitter | Level Element (Transmitter) | CBS-TK-10B Sump (Grid D-12) | Safety level transmitter | Post-accident containment sump water level transmission | PID-1-SI-LR20448 |
| [LE-2385-2](/instruments/LE-2385-2.md) | Containment Sump B Water Level Transmitter | Level Element (Transmitter) | CBS-TK-10B Sump (Grid D-12) | Safety level transmitter | Post-accident containment sump water level transmission (redundant) | PID-1-SI-LR20448 |
| [LS-2357](/instruments/LS-2357.md) | Protective Chamber Leak Detection Level Switch | Level Switch | CBS-TK-101B Protective Chamber (Grid D-10) | Liquid detection switch | Leak detection alarm in protective chamber | PID-1-SI-LR20448 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-CBS-TK10B-IN | INLET | CONTAINMENT FLOOR | CBS-TK-10B | Sump Structure | Sump screening / trash racks | Post-accident containment water | Containment atmospheric / post-LOCA pressure | — | Post-LOCA containment flood water collection into sump pit |
| STR-CBS-TK10B-OUT | OUTLET | CBS-TK-10B | RH-P-8B / CBS-P-9B Suction | 16" | CBS-V14 (MOV), CBS-EP-36B (Expansion Joint), CBS-V116 | Post-accident containment water | Sump static suction head | — | 16" suction effluent through guard pipe 1-CBS-S-611-B and penetration X-60 to RHR and Containment Spray pumps |
| STR-CBS-TK10B-CHAMBER-DRN | DRAIN | CBS-TK-101B | WLD DR 152 | 1/2"x3/4" | CBS-V90, CBS-V91, CBS-V128 | Ambient | Atmospheric | — | Guard pipe / protective chamber air test and drainage |

## Hazards & Safeguards

- Debris clogging / vortexing: Qualified emergency sump design to ensure continuous NPSH for RHR pump RH-P-8B and Containment Spray pump CBS-P-9B during recirculation.
- Valve interlock and containment integrity: Sump isolation valve CBS-V14 is interlocked to containment water levels CBS-LT-930..933 (Interlock A per Note 6) and enclosed in protective chamber CBS-TK-101B.
- Leak detection in guard pipe / chamber: Monitored by level switch LS-2357 inside protective chamber CBS-TK-101B.

## References & Sources

[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
