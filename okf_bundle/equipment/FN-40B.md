---
type: Equipment Concept
title: FN-40B — Service Water Pumphouse Supply Fan 40B
description: Nuclear safety-related ventilation supply fan for the Service Water Pumphouse
  (Train B), delivering 3,400 CFM of filtered outside air to the Train A and Train
  B electrical switchgear rooms and pump house floor to maintain equipment ambient
  temperatures within qualified design limits during normal and post-accident operations.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/FN-40B.md
tags:
- equipment
- fan
- swa
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-3.pdf
  title: ML101620329-part-3.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-11-05T14:34:23Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:34:23Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:34:23Z'
status: stable
entity_metadata:
  tag: FN-40B
  name: Service Water Pumphouse Supply Fan 40B
  equipment_class: Fan
  unit: SWA
  instruments:
  - tag: TSH-5614-2
    service: FN-40B Fan Control
    type: Temperature Switch High
    location: Fan FN-40B Control [12-G]
    setpoint_or_range: —
    interlock_or_alarm: Local control / Non-functional status
    source: PID-1-SWA-LR20372
  - tag: TSH-5615-1
    service: FN-40B Fan Control
    type: Temperature Switch High
    location: Fan FN-40B Control [11-G]
    setpoint_or_range: —
    interlock_or_alarm: Local control / Non-functional status
    source: PID-1-SWA-LR20372
  - tag: TSHL-5609
    service: Switchgear Room Temp Monitor
    type: Temperature Switch High/Low
    location: Train B Switchgear Room [11-F]
    setpoint_or_range: —
    interlock_or_alarm: Train B Switchgear Room temperature alarm
    source: PID-1-SWA-LR20372
  - tag: TI-8602
    service: Room Temperature Indication
    type: Temperature Indicator
    location: Train B Switchgear Room [11-F]
    setpoint_or_range: —
    interlock_or_alarm: Local temperature gauge
    source: PID-1-SWA-LR20372
  connections:
  - stream_id: SWA-AIR-IN-FN40B
    direction: INLET
    source_tag: F-58
    target_tag: FN-40B
    line_size: HVAC Duct
    inline_components:
    - Birdscreen
    - Roll Filter F-58
    temperature: Ambient outside air
    pressure: Atmospheric / Negative suction
    flow_rate: 3,400 CFM
    description: Outside air intake drawn through birdscreen and roll filter F-58
      into FN-40B suction
    source: PID-1-SWA-LR20372 (Grid 11-H)
  - stream_id: SWA-AIR-OUT-FN40B
    direction: OUTLET
    source_tag: FN-40B
    target_tag: PUMPHOUSE-SWITCHGEAR-RMS
    line_size: Distribution Duct (Red scope)
    inline_components:
    - DP-432B (Backdraft/Balancing Damper)
    - DP-192 (Fire Damper to Train B Switchgear Rm, 600 CFM)
    - DP-191 (Fire Damper to Train A Switchgear Rm, 2,800 CFM)
    temperature: Ventilation supply temp
    pressure: Positive duct pressure
    flow_rate: 3,400 CFM
    description: Supply air discharged through backdraft/balancing damper DP-432B
      into Pumphouse Switchgear Room distribution ductwork
    source: PID-1-SWA-LR20372 (Grid 11-G)
---

# FN-40B — Service Water Pumphouse Supply Fan 40B

## Function

Nuclear safety-related ventilation supply fan for the Service Water Pumphouse (Train B), delivering 3,400 CFM of filtered outside air to the Train A and Train B electrical switchgear rooms and pump house floor to maintain equipment ambient temperatures within qualified design limits during normal and post-accident operations.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Equipment Tag | FN-40B (SWA-FN-40B) (General Note 1 & Sheet 2 Grid 12-11, G-H) | — | PID-1-SWA-LR20372 |
| Nuclear Safety Classification | Nuclear Safety Related (Portions Safety Related) (Drawing Title Block & Section 4) | — | PID-1-SWA-LR20372 |
| License Renewal AMR Status | In Scope (AMR) per 10 CFR 54.4(a)(1) / (a)(3) (Red line color coding per 10 CFR 54.21) | — | PID-1-SWA-LR20372 |
| Rated Design Airflow | 3,400 (Grid 12-11, G-H) | CFM | PID-1-SWA-LR20372 |
| Associated Intake Filter | F-58 (SWA-F-58 Roll Filter) (Grid 11-H) | — | PID-1-SWA-LR20372 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Air Flow Rate | 3,400 | CFM | PID-1-SWA-LR20372 |
| Physical Location | Service Water Pump House (Top-Left, Grid 12-11, Row G/H) | — | PID-1-SWA-LR20372 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TSH-5614-2](/instruments/le-2384-1.md) | FN-40B Fan Control | Temperature Switch High | Fan FN-40B Control [12-G] | — | Local control / Non-functional status | PID-1-SWA-LR20372 |
| [TSH-5615-1](/instruments/le-2384-1.md) | FN-40B Fan Control | Temperature Switch High | Fan FN-40B Control [11-G] | — | Local control / Non-functional status | PID-1-SWA-LR20372 |
| [TSHL-5609](/instruments/le-2384-1.md) | Switchgear Room Temp Monitor | Temperature Switch High/Low | Train B Switchgear Room [11-F] | — | Train B Switchgear Room temperature alarm | PID-1-SWA-LR20372 |
| [TI-8602](/instruments/le-2384-1.md) | Room Temperature Indication | Temperature Indicator | Train B Switchgear Room [11-F] | — | Local temperature gauge | PID-1-SWA-LR20372 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SWA-AIR-IN-FN40B | INLET | F-58 | FN-40B | HVAC Duct | Birdscreen, Roll Filter F-58 | Ambient outside air | Atmospheric / Negative suction | 3,400 CFM | Outside air intake drawn through birdscreen and roll filter F-58 into FN-40B suction |
| SWA-AIR-OUT-FN40B | OUTLET | FN-40B | PUMPHOUSE-SWITCHGEAR-RMS | Distribution Duct (Red scope) | DP-432B (Backdraft/Balancing Damper), DP-192 (Fire Damper to Train B Switchgear Rm, 600 CFM), DP-191 (Fire Damper to Train A Switchgear Rm, 2,800 CFM) | Ventilation supply temp | Positive duct pressure | 3,400 CFM | Supply air discharged through backdraft/balancing damper DP-432B into Pumphouse Switchgear Room distribution ductwork |

## Hazards & Safeguards

- Loss of pumphouse ventilation causing high ambient temperature trips on safety-related switchgear and service water pump motors; room temperatures monitored by TSHL-5608 and TSHL-5609.
- External tornado wind loading and atmospheric pressure transients mitigated by tornado dampers DP-367, DP-369, and DP-370.

## References & Sources

[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
