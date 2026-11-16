---
type: Equipment Concept
title: SS-CP-166A — Primary Sample Panel CP-166A & Sink MM-13B
description: Nuclear Primary Sample Panel CP-166A and Sink MM-13B enclosure housing
  sample pressure reduction, analytical instrumentation, dissolved gas analysis (O2
  and H2), grab sample bomb and septum stations, and radioactive drainage collection
  for RCS, CVCS, and RHR process samples.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/SS-CP-166A.md
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
  at: '2026-10-02T13:21:20Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T13:21:20Z'
- by: process:okf-validation-suite
  at: '2026-10-02T13:21:20Z'
status: stable
entity_metadata:
  tag: SS-CP-166A
  name: Primary Sample Panel CP-166A & Sink MM-13B
  equipment_class: Panel / Skid
  unit: SS
  instruments:
  - tag: AE-2658
    service: Dissolved Oxygen Analytical Element
    type: Analytical Element
    location: Primary Sample Sink MM-13B (Grid 11-B)
    setpoint_or_range: ppm / ppb O2
    interlock_or_alarm: Dissolved oxygen measurement in sample stream
    source: PID-1-SS-LR20519
  - tag: AE-2657
    service: Dissolved Hydrogen Analytical Element
    type: Analytical Element
    location: Primary Sample Sink MM-13B (Grid 10-B)
    setpoint_or_range: cc/kg H2
    interlock_or_alarm: Dissolved hydrogen measurement in sample stream
    source: PID-1-SS-LR20519
  - tag: FI-2856
    service: Combined Sample Flow Indicator
    type: Flow Indicator
    location: Panel Header ahead of V55 (Grid 6-E)
    setpoint_or_range: Flow rate readout
    interlock_or_alarm: Combined sample flow measurement returning to VCT
    source: PID-1-SS-LR20519
  - tag: FI-2825
    service: PRT Gas Sample Flow Indicator
    type: Flow Indicator
    location: Panel CP-166A (Grid C-5, Dwg 20518)
    setpoint_or_range: Visual flow indication
    interlock_or_alarm: PRT gas grab sample flow indication (with integral needle
      valve per Note 6)
    source: PID-1-SS-LR20518
  - tag: FI-2824
    service: CVCT / Degasifier Sample Flow Indicator
    type: Flow Indicator
    location: Panel CP-166A (Grid B-5, Dwg 20518)
    setpoint_or_range: Visual flow indication
    interlock_or_alarm: CVCT / Degasifier grab sample flow indication (with integral
      needle valve per Note 6)
    source: PID-1-SS-LR20518
  - tag: FG-2895
    service: CVCT Sample Flow Sight Glass
    type: Sight Glass
    location: Panel CP-166A inlet (Grid B-7, Dwg 20518)
    setpoint_or_range: Visual inspection
    interlock_or_alarm: Visual verification of sample liquid stream flow
    source: PID-1-SS-LR20518
  connections:
  - stream_id: STR-SS-PANEL-PRZR-IN
    direction: INLET
    source_tag: SS-E-12B (20518 [G-3])
    target_tag: SS-CP-166A
    line_size: 3/8"T
    inline_components:
    - SS-V113
    - PCV 2847
    - TI 2850
    - PI 2851
    - SS-V45
    temperature: Ambient grab sample temp
    pressure: Regulated by PCV 2847
    flow_rate: Grab sample flow
    description: Cooled Pressurizer sample line entering Primary Sample Panel via
      PCV 2847
    source: PID-1-SS-LR20519
  - stream_id: STR-SS-PANEL-RCS-IN
    direction: INLET
    source_tag: SS-E-13B (20518 [F-3])
    target_tag: SS-CP-166A
    line_size: 3/8"T
    inline_components:
    - SS-V116
    - PCV 2848
    - TI 2852
    - PI 2853
    - SS-V41
    temperature: Ambient grab sample temp
    pressure: Regulated by PCV 2848
    flow_rate: Grab sample flow
    description: Cooled RCS Loop 1 & 3 sample line entering Primary Sample Panel via
      PCV 2848
    source: PID-1-SS-LR20519
  - stream_id: STR-SS-PANEL-TO-VCT
    direction: OUTLET
    source_tag: SS-CP-166A
    target_tag: CS-TK-1 (20725 [F-4])
    line_size: 3/4"
    inline_components:
    - FI 2856
    - SS-V55
    - SS-V56
    - SS-V57 (Red Class Break)
    - SS-V89
    - SS-V271
    temperature: Ambient
    pressure: VCT operating pressure
    flow_rate: —
    description: Combined sample line return to CVCS Volume Control Tank CS-TK-1
    source: PID-1-SS-LR20519
  - stream_id: STR-SS-SINK-DRAIN
    direction: DRAIN
    source_tag: SS-MM-13B
    target_tag: WLD SUMP A (20222 [F])
    line_size: 1-1/2"
    inline_components:
    - Trap T 344
    - SS-V82
    - SS-V774 (Check)
    temperature: Ambient
    pressure: Atmospheric gravity head
    flow_rate: Gravity drainage
    description: Primary Sample Sink MM-13B drain line through trap T 344 to Sump
      A
    source: PID-1-SS-LR20519
  - stream_id: STR-SS-PRT-OFFGAS
    direction: VENT
    source_tag: SS-CP-166A
    target_tag: EVS-VG (20780 [G-8])
    line_size: 3/8"T / 3/4"
    inline_components:
    - FI-2825
    - V65
    - V75
    temperature: Ambient
    pressure: Waste gas header pressure
    flow_rate: Analytical purge
    description: PRT gas sample off-gas line to Waste Gas Header
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-CVCT-OFFGAS
    direction: VENT
    source_tag: SS-CP-166A
    target_tag: EVS-VG (20780 [G-8])
    line_size: 3/8"T / 3/4"
    inline_components:
    - FI-2824
    - V60
    - V74
    temperature: Ambient
    pressure: Waste gas header pressure
    flow_rate: Analytical purge
    description: CVCT and Letdown Degasifier off-gas to Waste Gas Header
    source: PID-1-SS-LR20518
  - stream_id: STR-SS-DEMIN-FLUSH
    direction: UTILITY
    source_tag: DEMIN WATER PAB (20390 [D-7])
    target_tag: SS-MM-13B
    line_size: 3/4"x3/8"T
    inline_components:
    - DM-V400
    - DM-V399
    - DM-V401
    - DM-V494
    - DM-V16
    - DM-V397
    temperature: Ambient
    pressure: Demin water header pressure
    flow_rate: Flush rate
    description: Demineralized water supply to Primary Sample Sink MM-13B for flushing
    source: PID-1-SS-LR20519
---

# SS-CP-166A — Primary Sample Panel CP-166A & Sink MM-13B

## Function

Nuclear Primary Sample Panel CP-166A and Sink MM-13B enclosure housing sample pressure reduction, analytical instrumentation, dissolved gas analysis (O2 and H2), grab sample bomb and septum stations, and radioactive drainage collection for RCS, CVCS, and RHR process samples.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Numbers | PID-1-SS-LR20518 (Rev. 0) & PID-1-SS-LR20519 (Rev. 10) | — | PID-1-SS-LR20519 |
| Safety Classification | Portions Nuclear Safety Related / Safety Class NNS | — | PID-1-SS-LR20519 |
| AMR Scoping Status | In Scope 10 CFR 54.4(a)(1) & (a)(2) & (a)(3) [Red & Green] | — | PID-1-SS-LR20519 |
| Primary Sample Sink Model | MM-13B with Trap T 344 | — | PID-1-SS-LR20519 |
| Tubing Material & Size | 3/8"-T, Mat'l 2500 (General Note 3) | — | PID-1-SS-LR20519 |
| Sample Pressure Regulators | PCV 2847 (PRZR) & PCV 2848 (RCS Loops), 1/4" connectors | — | PID-1-SS-LR20519 |
| Nitrogen Supply Regulators | PCV 2854 (Set @ 45) & PCV 2855 (Set @ 30) | PSIG | PID-1-SS-LR20519 |
| Skid Relief Valves | V827 (150 PSIG), V760 (90 PSIG), V761 (90 PSIG) | PSIG | PID-1-SS-LR20519 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Operating Fluid | Cooled Borated Reactor Coolant Liquid & Gas Samples | — | PID-1-SS-LR20519 |
| Nitrogen Regulated Pressure Header 1 | 45 (PCV 2854) | PSIG | PID-1-SS-LR20519 |
| Nitrogen Regulated Pressure Header 2 | 30 (PCV 2855) | PSIG | PID-1-SS-LR20519 |
| Operating Environment | PAB Sample Room Atmosphere / Exhaust Ventilated | — | PID-1-SS-LR20519 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [AE-2658](/instruments/AE-2658.md) | Dissolved Oxygen Analytical Element | Analytical Element | Primary Sample Sink MM-13B (Grid 11-B) | ppm / ppb O2 | Dissolved oxygen measurement in sample stream | PID-1-SS-LR20519 |
| [AE-2657](/instruments/AE-2657.md) | Dissolved Hydrogen Analytical Element | Analytical Element | Primary Sample Sink MM-13B (Grid 10-B) | cc/kg H2 | Dissolved hydrogen measurement in sample stream | PID-1-SS-LR20519 |
| [FI-2856](/instruments/FI-2856.md) | Combined Sample Flow Indicator | Flow Indicator | Panel Header ahead of V55 (Grid 6-E) | Flow rate readout | Combined sample flow measurement returning to VCT | PID-1-SS-LR20519 |
| [FI-2825](/instruments/FI-2825.md) | PRT Gas Sample Flow Indicator | Flow Indicator | Panel CP-166A (Grid C-5, Dwg 20518) | Visual flow indication | PRT gas grab sample flow indication (with integral needle valve per Note 6) | PID-1-SS-LR20518 |
| [FI-2824](/instruments/FI-2824.md) | CVCT / Degasifier Sample Flow Indicator | Flow Indicator | Panel CP-166A (Grid B-5, Dwg 20518) | Visual flow indication | CVCT / Degasifier grab sample flow indication (with integral needle valve per Note 6) | PID-1-SS-LR20518 |
| [FG-2895](/instruments/FG-2895.md) | CVCT Sample Flow Sight Glass | Sight Glass | Panel CP-166A inlet (Grid B-7, Dwg 20518) | Visual inspection | Visual verification of sample liquid stream flow | PID-1-SS-LR20518 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-SS-PANEL-PRZR-IN | INLET | SS-E-12B (20518 [G-3]) | SS-CP-166A | 3/8"T | SS-V113, PCV 2847, TI 2850, PI 2851, SS-V45 | Ambient grab sample temp | Regulated by PCV 2847 | Grab sample flow | Cooled Pressurizer sample line entering Primary Sample Panel via PCV 2847 |
| STR-SS-PANEL-RCS-IN | INLET | SS-E-13B (20518 [F-3]) | SS-CP-166A | 3/8"T | SS-V116, PCV 2848, TI 2852, PI 2853, SS-V41 | Ambient grab sample temp | Regulated by PCV 2848 | Grab sample flow | Cooled RCS Loop 1 & 3 sample line entering Primary Sample Panel via PCV 2848 |
| STR-SS-PANEL-TO-VCT | OUTLET | SS-CP-166A | CS-TK-1 (20725 [F-4]) | 3/4" | FI 2856, SS-V55, SS-V56, SS-V57 (Red Class Break), SS-V89, SS-V271 | Ambient | VCT operating pressure | — | Combined sample line return to CVCS Volume Control Tank CS-TK-1 |
| STR-SS-SINK-DRAIN | DRAIN | SS-MM-13B | WLD SUMP A (20222 [F]) | 1-1/2" | Trap T 344, SS-V82, SS-V774 (Check) | Ambient | Atmospheric gravity head | Gravity drainage | Primary Sample Sink MM-13B drain line through trap T 344 to Sump A |
| STR-SS-PRT-OFFGAS | VENT | SS-CP-166A | EVS-VG (20780 [G-8]) | 3/8"T / 3/4" | FI-2825, V65, V75 | Ambient | Waste gas header pressure | Analytical purge | PRT gas sample off-gas line to Waste Gas Header |
| STR-SS-CVCT-OFFGAS | VENT | SS-CP-166A | EVS-VG (20780 [G-8]) | 3/8"T / 3/4" | FI-2824, V60, V74 | Ambient | Waste gas header pressure | Analytical purge | CVCT and Letdown Degasifier off-gas to Waste Gas Header |
| STR-SS-DEMIN-FLUSH | UTILITY | DEMIN WATER PAB (20390 [D-7]) | SS-MM-13B | 3/4"x3/8"T | DM-V400, DM-V399, DM-V401, DM-V494, DM-V16, DM-V397 | Ambient | Demin water header pressure | Flush rate | Demineralized water supply to Primary Sample Sink MM-13B for flushing |

## Hazards & Safeguards

- Radioactive liquid and gas leakage hazard: Grab sampling involves active primary coolant fluids; enclosed sink MM-13B is ventilated and equipped with P-trap T 344 to prevent gas egress into the PAB.
- Overpressure hazard on low-pressure analytical equipment: Regulated by PCV 2847 and PCV 2848, with downstream protection by relief valves V827 (150 psig), V760 (90 psig), and V761 (90 psig).
- Hydrogen gas explosion risk: Dissolved hydrogen analyzer AE 2657 and vent lines routed safely to the Waste Gas System (EVS-VG).

## References & Sources

[^src-1]: ML101620329-part-2.pdf (reference/raw/pid/ML101620329-part-2.pdf)
