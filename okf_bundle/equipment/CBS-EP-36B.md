---
type: Equipment Concept
title: CBS-EP-36B — Expansion Bellows / Piece B
description: Safety Class 2 16" flexible expansion bellows installed on the Containment
  Recirculation Sump B suction line inside Protective Chamber CBS-TK-101B downstream
  of penetration X-60, providing seismic and thermal expansion accommodation while
  maintaining post-LOCA containment and ECCS suction boundary integrity.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/CBS-EP-36B.md
tags:
- equipment
- expansion joint
- si / cbs
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-1.pdf
  title: ML101620329-part-1.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-23T02:52:55Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-23T02:52:55Z'
- by: process:okf-validation-suite
  at: '2026-10-23T02:52:55Z'
status: stable
entity_metadata:
  tag: CBS-EP-36B
  name: Expansion Bellows / Piece B
  equipment_class: Expansion Joint
  unit: SI / CBS
  instruments:
  - tag: LS-2357
    service: Protective Chamber Leak Detection Level Switch
    type: Process Instrument
    location: Protective Chamber CBS-TK-101B Body (Grid D-10)
    setpoint_or_range: High Level Trip / Alarm
    interlock_or_alarm: High liquid level alarm in Main Control Room signaling chamber
      leakage
    source: PID-1-SI-LR20448
  connections:
  - stream_id: STR-CBS-EP36B-IN
    direction: INLET
    source_tag: CBS-TK-10B
    target_tag: CBS-EP-36B
    line_size: 16"
    inline_components:
    - Concentric Guard Pipe 1-CBS-S-611-B
    - Penetration X-60
    - CBS-V14 (16" MOV)
    temperature: Ambient to 250 °F (post-LOCA)
    pressure: Post-LOCA Containment Flood Static Head
    flow_rate: Full ECCS Recirculation Flow
    description: Inlet connection from Containment Sump B suction line passing through
      Penetration X-60 inside protective chamber CBS-TK-101B
    source: PID-1-SI-LR20448
  - stream_id: STR-CBS-EP36B-OUT
    direction: OUTLET
    source_tag: CBS-EP-36B
    target_tag: RH-P-8B / CBS-P-9B Suction
    line_size: 16"
    inline_components:
    - CBS-V116 (16" Test Conn)
    temperature: Ambient to 250 °F (post-LOCA)
    pressure: Post-LOCA Containment Flood Static Head
    flow_rate: Full ECCS Recirculation Flow
    description: Outlet connection delivering borated recirculating water to RHR and
      Containment Spray suction headers
    source: PID-1-SI-LR20448
---

# CBS-EP-36B — Expansion Bellows / Piece B

## Function

Safety Class 2 16" flexible expansion bellows installed on the Containment Recirculation Sump B suction line inside Protective Chamber CBS-TK-101B downstream of penetration X-60, providing seismic and thermal expansion accommodation while maintaining post-LOCA containment and ECCS suction boundary integrity.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20448 (Rev. 11, Ref. Dwg: PID-1-SI-B20448) | — | PID-1-SI-LR20448 |
| System Prefix | CBS / SI | — | PID-1-SI-LR20448 |
| Verbatim Printed Tag | CBS-EP-36B | — | PID-1-SI-LR20448 |
| Component Type | Flexible Expansion Bellows / Expansion Piece | — | PID-1-SI-LR20448 |
| Safety Classification | Safety Class 2 (Nuclear Safety Related) | — | PID-1-SI-LR20448 |
| License Renewal AMR Scope | In Scope 10 CFR 54.4(a)(1) and/or (a)(3) [Red] | — | PID-1-SI-LR20448 |
| Nominal Diameter | 16 | in | PID-1-SI-LR20448 |
| Physical Enclosure | Installed inside Protective Chamber CBS-TK-101B (Grid D-10) | — | PID-1-SI-LR20448 |
| Associated Guard Pipe | 1-CBS-S-611-B (Penetration X-60) | — | PID-1-SI-LR20448 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Service Fluid (Post-LOCA) | Borated Containment Recirculation Sump Water | — | PID-1-SI-LR20448 |
| Operating Temperature | Ambient to 250 (post-LOCA transient) | °F | PID-1-SI-LR20448 |
| External Environment | Sealed, dry atmospheric inside protective chamber CBS-TK-101B | — | PID-1-SI-LR20448 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LS-2357](/instruments/ls-2357.md) | Protective Chamber Leak Detection Level Switch | Process Instrument | Protective Chamber CBS-TK-101B Body (Grid D-10) | High Level Trip / Alarm | High liquid level alarm in Main Control Room signaling chamber leakage | PID-1-SI-LR20448 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-CBS-EP36B-IN | INLET | CBS-TK-10B | CBS-EP-36B | 16" | Concentric Guard Pipe 1-CBS-S-611-B, Penetration X-60, CBS-V14 (16" MOV) | Ambient to 250 °F (post-LOCA) | Post-LOCA Containment Flood Static Head | Full ECCS Recirculation Flow | Inlet connection from Containment Sump B suction line passing through Penetration X-60 inside protective chamber CBS-TK-101B |
| STR-CBS-EP36B-OUT | OUTLET | CBS-EP-36B | RH-P-8B / CBS-P-9B Suction | 16" | CBS-V116 (16" Test Conn) | Ambient to 250 °F (post-LOCA) | Post-LOCA Containment Flood Static Head | Full ECCS Recirculation Flow | Outlet connection delivering borated recirculating water to RHR and Containment Spray suction headers |

## Hazards & Safeguards

- Expansion bellows boundary failure during post-LOCA recirculation could result in radioactive sump water leakage; leak integrity is continuously monitored within sealed chamber CBS-TK-101B by level switch LS-2357.
- Bellows must withstand seismic displacements and thermal expansion cycles between the containment wall penetration sleeve and the external auxiliary building piping.

## References & Sources

[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
