---
type: Equipment Concept
title: SS-CP-419 — Post Accident Sample Panel CP-419
description: Post Accident Sample Panel CP-419 enclosure structure located within
  the shielded PASS panel cubicle in the Primary Auxiliary Building. Houses post-accident
  primary coolant manifolding, demineralized water flush connections, inert Argon
  gas purge, sample cask routing, and effluent drainage to containment penetration
  X-19.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SS-CP-419.md
tags:
- equipment
- panel / skid
- ss
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-2.pdf
  title: ML101620329-part-2.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:22:58Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:22:58Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:22:58Z'
status: stable
entity_metadata:
  tag: SS-CP-419
  name: Post Accident Sample Panel CP-419
  equipment_class: Panel / Skid
  unit: SS
  instruments:
  - tag: PI-2879-1
    service: Argon Cylinder Supply Pressure Gauge
    type: Pressure Indicator
    location: Argon package skid (Grid G-11)
    setpoint_or_range: Cylinder pressure (0–3000 PSIG)
    interlock_or_alarm: Argon gas cylinder high-side supply pressure indication
    source: PID-1-SS-LR20520
  - tag: PI-2879-2
    service: Argon Regulated Header Pressure Gauge
    type: Pressure Indicator
    location: Downstream of PCV-2879 (Grid G-11)
    setpoint_or_range: Per Chemistry Procedures
    interlock_or_alarm: Argon gas regulated header pressure indication
    source: PID-1-SS-LR20520
  connections:
  - stream_id: STR-SS-PASS-IN
    direction: INLET
    source_tag: RCS LOOPS 1 & 3 (20518 [E-8])
    target_tag: SS-CP-419
    line_size: 1/4"T (from RC-3/8"T)
    inline_components:
    - SS-V230
    temperature: Post-LOCA coolant temp
    pressure: Post-accident RCS pressure
    flow_rate: Grab sample flow
    description: Post-accident primary coolant sample inlet to PASS manifold from
      RCS Loops 1 & 3
    source: PID-1-SS-LR20520
  - stream_id: STR-SS-ARGON-PURGE
    direction: UTILITY
    source_tag: ARGON SUPPLY PACKAGE
    target_tag: SS-CP-419
    line_size: 1/4" Tubing
    inline_components:
    - SS-PCV-2879
    - SS-V282 (Vent)
    - SS-V212
    temperature: Ambient
    pressure: Per Chemistry Procedures
    flow_rate: Purge gas flow
    description: Inert Argon gas purge supply from package skid to sample manifold
    source: PID-1-SS-LR20520
  - stream_id: STR-SS-PASS-DEMIN
    direction: UTILITY
    source_tag: DEMIN SYSTEM (20350 [D-7])
    target_tag: SS-CP-419
    line_size: 3/8"T x 1/4"T
    inline_components:
    - SS-V322 (Check)
    - SS-V321
    - SS-V236
    temperature: Ambient
    pressure: Demin water header pressure
    flow_rate: Flush flow rate
    description: Demineralized water flush supply to sample manifold
    source: PID-1-SS-LR20520
  - stream_id: STR-SS-FP-TIE
    direction: OUTLET
    source_tag: SS-CP-419
    target_tag: CNT REC SUMP SMPL RH (20519 [C-4])
    line_size: 1/4"T x 3/8"T
    inline_components:
    - SS-V232
    temperature: Ambient
    pressure: System pressure
    flow_rate: —
    description: Fire Protection AMR scope tie-in line from manifold valve V232
    source: PID-1-SS-LR20520
  - stream_id: STR-SS-PASS-DRAIN
    direction: DRAIN
    source_tag: SS-CP-419
    target_tag: PENETRATION-X-19
    line_size: 1/2"T / 1/2"
    inline_components:
    - SS-V208
    - SS-V337
    - SS-FV-2857 (FC)
    - Penetration X-19
    temperature: Ambient
    pressure: Drain header pressure
    flow_rate: Drain flow
    description: PASS panel manifold drain line to containment drainage through Penetration
      X-19
    source: PID-1-SS-LR20520
---

# SS-CP-419 — Post Accident Sample Panel CP-419

## Function

Post Accident Sample Panel CP-419 enclosure structure located within the shielded PASS panel cubicle in the Primary Auxiliary Building. Houses post-accident primary coolant manifolding, demineralized water flush connections, inert Argon gas purge, sample cask routing, and effluent drainage to containment penetration X-19.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SS-LR20520 (Rev. 13) | — | PID-1-SS-LR20520 |
| Safety Classification | Safety Class NNS (portions Nuclear Safety Related) | — | PID-1-SS-LR20520 |
| AMR Scoping Status | In Scope 10 CFR 54.4(a)(2) [Green] & 10 CFR 54.4(a)(3) [Red - Fire Protection] | — | PID-1-SS-LR20520 |
| Physical Location | PASS Panel Cubicle (Grids A-10 / B-10) | — | PID-1-SS-LR20520 |
| Containment Penetration Designation | Penetration X-19 (Evaluated under LRSP-CNT per LR Note 1) | — | PID-1-SS-LR20520 |
| Manifold Tubing Sizes | 1/4" Tubing and 3/8" Tubing | in | PID-1-SS-LR20520 |
| Fire Protection Scope Criteria | Red piping in scope for criterion (a)(3) Fire Protection (LR Note 4) | — | PID-1-SS-LR20520 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Operating Environment | Shielded PASS Panel Cubicle (PAB) | — | PID-1-SS-LR20520 |
| Operating Service | Emergency Post-Accident Reactor Coolant Grab Sampling | — | PID-1-SS-LR20520 |
| Inert Purge Medium | High Purity Argon Gas (Vendor Supplied Skid) | — | PID-1-SS-LR20520 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PI-2879-1](/instruments/PI-2879-1.md) | Argon Cylinder Supply Pressure Gauge | Pressure Indicator | Argon package skid (Grid G-11) | Cylinder pressure (0–3000 PSIG) | Argon gas cylinder high-side supply pressure indication | PID-1-SS-LR20520 |
| [PI-2879-2](/instruments/PI-2879-2.md) | Argon Regulated Header Pressure Gauge | Pressure Indicator | Downstream of PCV-2879 (Grid G-11) | Per Chemistry Procedures | Argon gas regulated header pressure indication | PID-1-SS-LR20520 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-SS-PASS-IN | INLET | RCS LOOPS 1 & 3 (20518 [E-8]) | SS-CP-419 | 1/4"T (from RC-3/8"T) | SS-V230 | Post-LOCA coolant temp | Post-accident RCS pressure | Grab sample flow | Post-accident primary coolant sample inlet to PASS manifold from RCS Loops 1 & 3 |
| STR-SS-ARGON-PURGE | UTILITY | ARGON SUPPLY PACKAGE | SS-CP-419 | 1/4" Tubing | SS-PCV-2879, SS-V282 (Vent), SS-V212 | Ambient | Per Chemistry Procedures | Purge gas flow | Inert Argon gas purge supply from package skid to sample manifold |
| STR-SS-PASS-DEMIN | UTILITY | DEMIN SYSTEM (20350 [D-7]) | SS-CP-419 | 3/8"T x 1/4"T | SS-V322 (Check), SS-V321, SS-V236 | Ambient | Demin water header pressure | Flush flow rate | Demineralized water flush supply to sample manifold |
| STR-SS-FP-TIE | OUTLET | SS-CP-419 | CNT REC SUMP SMPL RH (20519 [C-4]) | 1/4"T x 3/8"T | SS-V232 | Ambient | System pressure | — | Fire Protection AMR scope tie-in line from manifold valve V232 |
| STR-SS-PASS-DRAIN | DRAIN | SS-CP-419 | PENETRATION-X-19 | 1/2"T / 1/2" | SS-V208, SS-V337, SS-FV-2857 (FC), Penetration X-19 | Ambient | Drain header pressure | Drain flow | PASS panel manifold drain line to containment drainage through Penetration X-19 |

## Hazards & Safeguards

- High radiation area: Shielded cubicle designed to minimize occupational radiation dose during post-accident sampling operations per NUREG-0737 / 10 CFR 50.34(f)(2)(viii).
- Containment isolation integrity: Solenoid valve SS-FV-2857 automatically isolates drainage penetration X-19 on containment isolation actuation signal 'T'. Inside containment isolation valve SS-V272 is maintained Locked Closed.

## References & Sources

[^src-1]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
