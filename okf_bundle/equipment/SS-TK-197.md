---
type: Equipment Concept
title: SS-TK-197 — Post Accident Flush Tank
description: Post Accident Sample System Flush Tank accumulating radioactive demineralized
  flush water and residual coolant drainage from the PASS sample casks and tubing
  before transferring effluent inside containment through Penetration X-19 to Waste
  Process Liquid Drains.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SS-TK-197.md
tags:
- equipment
- ss
- vessel
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-2.pdf
  title: ML101620329-part-2.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T13:22:06Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:22:06Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:22:06Z'
status: stable
entity_metadata:
  tag: SS-TK-197
  name: Post Accident Flush Tank
  equipment_class: Vessel
  unit: SS
  instruments:
  - tag: LT-9616
    service: Flush Tank Liquid Level Transmitter
    type: Level Transmitter
    location: PASS Panel Cubicle across root valves V317 & V318 (Grid C-6)
    setpoint_or_range: 0–100% tank level (Note 5 reference leg)
    interlock_or_alarm: Differential pressure liquid level transmitter across flush
      tank
    source: PID-1-SS-LR20520
  - tag: FV-2857
    service: PASS Effluent Containment Isolation Valve
    type: Control Valve
    location: Outside Containment ahead of Penetration X-19 (Grid B-5)
    setpoint_or_range: Fail Closed (FC)
    interlock_or_alarm: Solenoid-operated containment isolation valve; fails closed
      on Containment Isolation Signal 'T'
    source: PID-1-SS-LR20520
  connections:
  - stream_id: STR-SS-TK197-IN
    direction: INLET
    source_tag: DEMIN SYSTEM (20350 [D-7])
    target_tag: SS-TK-197
    line_size: 1/4"T / 3/8"T
    inline_components:
    - SS-V321
    - SS-V322 (Check)
    temperature: Ambient
    pressure: Demin header pressure
    flow_rate: Flush flow rate
    description: Demineralized water and sample flush inlet line to Flush Tank TK-197
    source: PID-1-SS-LR20520
  - stream_id: STR-SS-TK197-DRAIN
    direction: DRAIN
    source_tag: SS-TK-197
    target_tag: WLD DR 141 (20219 [F-5])
    line_size: 3/8"T / 1/2"
    inline_components:
    - SS-V303
    - SS-V266
    - SS-FV-2857 (FC)
    - Penetration X-19
    - SS-V273
    temperature: Ambient
    pressure: Drain header pressure
    flow_rate: Gravity drainage
    description: Tank bottom drain line through CIV FV-2857 and Penetration X-19 to
      Liquid Waste Drains DR 141
    source: PID-1-SS-LR20520
  - stream_id: STR-SS-TK197-VENT
    direction: VENT
    source_tag: SS-TK-197
    target_tag: PRIMARY AIR HANDLING PAB VENT (20495 [D-8])
    line_size: 1/2"
    inline_components:
    - SS-V868
    - SS-T-312
    temperature: Ambient
    pressure: Atmospheric vent head
    flow_rate: Vessel vent flow
    description: Tank top off-gas vent line to Liquid Drainer T-312 and PAB Vent System
    source: PID-1-SS-LR20520
---

# SS-TK-197 — Post Accident Flush Tank

## Function

Post Accident Sample System Flush Tank accumulating radioactive demineralized flush water and residual coolant drainage from the PASS sample casks and tubing before transferring effluent inside containment through Penetration X-19 to Waste Process Liquid Drains.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SS-LR20520 (Rev. 13) | — | PID-1-SS-LR20520 |
| Safety Classification | Safety Class NNS (General Note 6) | — | PID-1-SS-LR20520 |
| AMR Scoping Status | In Scope 10 CFR 54.4(a)(2) [Green] | — | PID-1-SS-LR20520 |
| Physical Location | PASS Panel Cubicle (Grid C-6) | — | PID-1-SS-LR20520 |
| Bottom Drain Line Size | 3/8" Tubing into 1/2" Line | in | PID-1-SS-LR20520 |
| Top Vent Line Size | 1/2" | in | PID-1-SS-LR20520 |
| Reference Leg Requirement | Maintain level of demin water in reference leg (General Note 5) | — | PID-1-SS-LR20520 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Operating Fluid | Radioactive Demineralized Flush Water & Coolant Effluent | — | PID-1-SS-LR20520 |
| Operating Pressure | Atmospheric / Gravity head | PSIG | PID-1-SS-LR20520 |
| Operating Temperature | Ambient (~70–120) | °F | PID-1-SS-LR20520 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LT-9616](/instruments/LT-9616.md) | Flush Tank Liquid Level Transmitter | Level Transmitter | PASS Panel Cubicle across root valves V317 & V318 (Grid C-6) | 0–100% tank level (Note 5 reference leg) | Differential pressure liquid level transmitter across flush tank | PID-1-SS-LR20520 |
| [FV-2857](/instruments/FV-2857.md) | PASS Effluent Containment Isolation Valve | Control Valve | Outside Containment ahead of Penetration X-19 (Grid B-5) | Fail Closed (FC) | Solenoid-operated containment isolation valve; fails closed on Containment Isolation Signal 'T' | PID-1-SS-LR20520 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-SS-TK197-IN | INLET | DEMIN SYSTEM (20350 [D-7]) | SS-TK-197 | 1/4"T / 3/8"T | SS-V321, SS-V322 (Check) | Ambient | Demin header pressure | Flush flow rate | Demineralized water and sample flush inlet line to Flush Tank TK-197 |
| STR-SS-TK197-DRAIN | DRAIN | SS-TK-197 | WLD DR 141 (20219 [F-5]) | 3/8"T / 1/2" | SS-V303, SS-V266, SS-FV-2857 (FC), Penetration X-19, SS-V273 | Ambient | Drain header pressure | Gravity drainage | Tank bottom drain line through CIV FV-2857 and Penetration X-19 to Liquid Waste Drains DR 141 |
| STR-SS-TK197-VENT | VENT | SS-TK-197 | PRIMARY AIR HANDLING PAB VENT (20495 [D-8]) | 1/2" | SS-V868, SS-T-312 | Ambient | Atmospheric vent head | Vessel vent flow | Tank top off-gas vent line to Liquid Drainer T-312 and PAB Vent System |

## Hazards & Safeguards

- Post-accident liquid waste transfer: Drainage penetrates containment via Penetration X-19, protected outside containment by solenoid valve SS-FV-2857 (Fail Closed, actuation signal T).
- Liquid carryover into ventilation: Off-gas line protected by in-line liquid drainer SS-T-312 with separate liquid trap discharge to DR 264.

## References & Sources

[^src-1]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
