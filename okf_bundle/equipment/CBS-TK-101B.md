---
type: Equipment Concept
title: CBS-TK-101B — Protective Chamber B (Sump B Guard Pipe Enclosure)
description: Safety Class 2 sealed protective chamber enclosing the containment recirculation
  sump B suction line, expansion bellows CBS-EP-36B, and motor-operated sump isolation
  valve CBS-V14, providing containment isolation barrier redundancy and leak detection
  via level switch LS-2357 outside containment penetration X-60.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/CBS-TK-101B.md
tags:
- equipment
- si / cbs
- vessel
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-1.pdf
  title: ML101620329-part-1.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-11T01:58:06Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-11T01:58:06Z'
- by: process:okf-validation-suite
  at: '2026-10-11T01:58:06Z'
status: stable
entity_metadata:
  tag: CBS-TK-101B
  name: Protective Chamber B (Sump B Guard Pipe Enclosure)
  equipment_class: Vessel
  unit: SI / CBS
  instruments:
  - tag: LS-2357
    service: Protective Chamber Leak Detection Level Switch
    type: Level Switch
    location: Chamber Body (Grid D-10)
    setpoint_or_range: Liquid level detection
    interlock_or_alarm: High liquid level alarm in Main Control Room signaling guard
      pipe or valve seal leakage
    source: PID-1-SI-LR20448
  connections:
  - stream_id: STR-CBS-TK101B-SUCT-IN
    direction: INLET
    source_tag: CBS-TK-10B
    target_tag: CBS-TK-101B
    line_size: 16"
    inline_components:
    - Guard pipe 1-CBS-S-611-B
    - Penetration X-60
    temperature: Ambient to post-LOCA
    pressure: Post-LOCA static head
    flow_rate: —
    description: 16" Sump B suction header entering protective chamber through Penetration
      X-60
    source: PID-1-SI-LR20448
  - stream_id: STR-CBS-TK101B-SUCT-OUT
    direction: OUTLET
    source_tag: CBS-TK-101B
    target_tag: RH-P-8B / CBS-P-9B Suction
    line_size: 16"
    inline_components:
    - CBS-V14 (MOV)
    - CBS-EP-36B (Expansion Joint)
    - CBS-V116
    temperature: Ambient to post-LOCA
    pressure: Post-LOCA static head
    flow_rate: —
    description: 16" Sump B suction line exiting chamber to RHR and Containment Spray
      pumps
    source: PID-1-SI-LR20448
  - stream_id: STR-CBS-TK101B-DRN
    direction: DRAIN
    source_tag: CBS-TK-101B
    target_tag: WLD DR 152
    line_size: 1/2"x3/4"
    inline_components:
    - CBS-V90
    - CBS-V91
    - CBS-V92 (LC)
    - CBS-V128 (LC)
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Air test and drainage line to radioactive waste drain DR 152
    source: PID-1-SI-LR20448
---

# CBS-TK-101B — Protective Chamber B (Sump B Guard Pipe Enclosure)

## Function

Safety Class 2 sealed protective chamber enclosing the containment recirculation sump B suction line, expansion bellows CBS-EP-36B, and motor-operated sump isolation valve CBS-V14, providing containment isolation barrier redundancy and leak detection via level switch LS-2357 outside containment penetration X-60.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20448 (Rev. 11, Ref. B20448) | — | PID-1-SI-LR20448 |
| Safety Classification | Safety Class 2 (Nuclear Safety Related) | — | PID-1-SI-LR20448 |
| Physical Location | Penetration Area / Outside Containment (Grid D-10) | — | PID-1-SI-LR20448 |
| AMR Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20448 |
| Enclosed Concentric Guard Pipe | 1-CBS-S-611-B | — | PID-1-SI-LR20448 |
| Containment Penetration | Penetration X-60 | — | PID-1-SI-LR20448 |
| Enclosed Isolation Valve | CBS-V14 (16" Motor-Operated Valve, Interlock A) | — | PID-1-SI-LR20448 |
| Internal Expansion Joint | CBS-EP-36B | — | PID-1-SI-LR20448 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Internal Environment (Normal) | Air / Inert Gas (normally sealed and drained) | — | PID-1-SI-LR20448 |
| Post-Accident Service Fluid | Borated Recirculation Water (retained upon suction pipe leakage) | — | PID-1-SI-LR20448 |
| Drain Destination | Waste Liquid Drains DR 152 via CBS-V128 | — | PID-1-SI-LR20448 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LS-2357](/instruments/LS-2357.md) | Protective Chamber Leak Detection Level Switch | Level Switch | Chamber Body (Grid D-10) | Liquid level detection | High liquid level alarm in Main Control Room signaling guard pipe or valve seal leakage | PID-1-SI-LR20448 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-CBS-TK101B-SUCT-IN | INLET | CBS-TK-10B | CBS-TK-101B | 16" | Guard pipe 1-CBS-S-611-B, Penetration X-60 | Ambient to post-LOCA | Post-LOCA static head | — | 16" Sump B suction header entering protective chamber through Penetration X-60 |
| STR-CBS-TK101B-SUCT-OUT | OUTLET | CBS-TK-101B | RH-P-8B / CBS-P-9B Suction | 16" | CBS-V14 (MOV), CBS-EP-36B (Expansion Joint), CBS-V116 | Ambient to post-LOCA | Post-LOCA static head | — | 16" Sump B suction line exiting chamber to RHR and Containment Spray pumps |
| STR-CBS-TK101B-DRN | DRAIN | CBS-TK-101B | WLD DR 152 | 1/2"x3/4" | CBS-V90, CBS-V91, CBS-V92 (LC), CBS-V128 (LC) | Ambient | Atmospheric | — | Air test and drainage line to radioactive waste drain DR 152 |

## Hazards & Safeguards

- Post-accident radioactive effluent containment: Guard pipe and protective chamber form an extension of containment boundary outside penetration X-60; any leakage from valve CBS-V14 or bellows CBS-EP-36B is contained within chamber and detected by LS-2357.
- Sump MOV inadvertent operation: MOV CBS-V14 is interlocked (Interlock A per Note 6) with containment water levels CBS-LT-930..933 (drawing 20233) to prevent opening prior to reaching adequate flood level in containment.
- Drain valve lineup: Drain valves CBS-V92 and CBS-V128 are maintained Locked Closed (LC) to prevent unmonitored release during plant operation and accident recirculation.

## References & Sources

[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
