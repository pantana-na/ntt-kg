---
type: Equipment Concept
title: DM-8 — Fuel Pool Demineralizer
description: Fuel Pool Demineralizer providing deep-bed ion-exchange purification
  of spent fuel pool water and cavity cleanup streams, removing soluble radionuclides,
  fission products, and ionic impurities to maintain pool water clarity and minimize
  radiation fields.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/DM-8.md
tags:
- demineralizer / ion exchanger
- equipment
- sf
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-1.pdf
  title: ML101620329-part-1.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-02T12:46:33Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-02T12:46:33Z'
- by: process:okf-validation-suite
  at: '2026-10-02T12:46:33Z'
status: stable
entity_metadata:
  tag: DM-8
  name: Fuel Pool Demineralizer
  equipment_class: Demineralizer / Ion Exchanger
  unit: SF
  instruments:
  - tag: PDIS-2624
    service: Resin Bed Differential Pressure Monitoring
    type: Differential Pressure Indicator, Switch
    location: Across DM-8 (Inlet top head vs Outlet bottom head, Grid E-6)
    setpoint_or_range: DP High Setpoint
    interlock_or_alarm: Demineralizer resin bed differential pressure indication and
      high alarm
    source: PID-1-SF-LR20483
  - tag: TE-2625
    service: Inlet Temperature Monitoring for Resin Bed Protection
    type: Temperature Element
    location: Demineralizer Inlet Header (Grid Column 6, Row H)
    setpoint_or_range: High Temperature Alarm
    interlock_or_alarm: High inlet fluid temperature alarm / resin thermal protection
    source: PID-1-SF-LR20483
  connections:
  - stream_id: STR-SF-DM8-IN
    direction: INLET
    source_tag: F-33 Manifold
    target_tag: DM-8
    line_size: 3"
    inline_components:
    - 1-SF-V40
    temperature: Pool ambient (monitored by TE-2625)
    pressure: Cleanup loop operating pressure
    flow_rate: —
    description: Main process inlet from prefilter F-33 effluent / purification manifold
    source: PID-1-SF-LR20483
  - stream_id: STR-SF-DM8-OUT
    direction: OUTLET
    source_tag: DM-8
    target_tag: F-34 Manifold
    line_size: 3"x4"
    inline_components:
    - 1-SF-V38
    temperature: Pool ambient
    pressure: Downstream header pressure
    flow_rate: —
    description: Demineralized effluent routing to Postfilter F-34 inlet header
    source: PID-1-SF-LR20483
  - stream_id: STR-SF-DM8-BYPASS
    direction: BYPASS
    source_tag: F-33 Effluent
    target_tag: F-34 Manifold
    line_size: 4"
    inline_components:
    - 1-SF-V76
    temperature: Pool ambient
    pressure: Header pressure
    flow_rate: —
    description: Full demineralizer bypass around DM-8
    source: PID-1-SF-LR20483
  - stream_id: STR-SF-DM8-RESIN-FILL
    direction: INLET
    source_tag: Resin Addition Station
    target_tag: DM-8 Top Head
    line_size: 3"
    inline_components:
    - 1-SF-V36
    temperature: Ambient
    pressure: Resin fill pressure
    flow_rate: —
    description: Fresh resin fill connection to top head
    source: PID-1-SF-LR20483
  - stream_id: STR-SF-DM8-SLUICE
    direction: OUTLET
    source_tag: DM-8 Bottom Head
    target_tag: RS-TK-79A & B (20252 [G-4])
    line_size: 3"
    inline_components:
    - 1-SF-V49
    - 1-SF-V57 (Boundary MOV/Gate)
    temperature: Ambient
    pressure: Sluicing header pressure
    flow_rate: —
    description: Spent resin sluice discharge from bottom head to Spent Resin Sluicing
      System
    source: PID-1-SF-LR20483
  - stream_id: STR-SF-DM8-SLUICE-WTR
    direction: UTILITY
    source_tag: RS Sluice Water Supply (20252 [H-3])
    target_tag: DM-8 Bottom Head
    line_size: 3"
    inline_components:
    - 1-SF-V47
    temperature: Ambient
    pressure: Sluice water supply pressure
    flow_rate: —
    description: Sluice water supply connection to bottom head for resin transfer/fluidization
    source: PID-1-SF-LR20483
---

# DM-8 — Fuel Pool Demineralizer

## Function

Fuel Pool Demineralizer providing deep-bed ion-exchange purification of spent fuel pool water and cavity cleanup streams, removing soluble radionuclides, fission products, and ionic impurities to maintain pool water clarity and minimize radiation fields.

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SF-LR20483 (Rev. 0, Ref. B20482 Rev. 15) | — | PID-1-SF-LR20483 |
| System Prefix | 1-SF | — | PID-1-SF-LR20483 (General Note 2) |
| Verbatim Printed Tag | DM-8 | — | PID-1-SF-LR20483 |
| Safety Classification | Safety Class NNS (Non-Nuclear Safety) | — | PID-1-SF-LR20483 (General Note 3) |
| AMR Scope Status | In Scope 10 CFR 54.4(a)(2) [Green] | — | PID-1-SF-LR20483 (LR Note 1) |
| Physical Location | Primary Auxiliary Building (Grid E/F-6) | — | PID-1-SF-LR20483 |
| Process Inlet Nozzle Size | 3 | in | PID-1-SF-LR20483 |
| Process Outlet Nozzle Size | 3 | in | PID-1-SF-LR20483 |
| Resin Fill Nozzle Size | 3 | in | PID-1-SF-LR20483 |
| Resin Sluice Nozzle Size | 3 | in | PID-1-SF-LR20483 |
| Bypass Line & Valve Size | 4 (Valve 1-SF-V76) | in | PID-1-SF-LR20483 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Primary Operating Fluid | Borated Water (Spent Fuel Pool / Cavity Cleanup) | — | PID-1-SF-LR20483 |
| Inlet Stream Source | Prefilter F-33 effluent via valve 1-SF-V40 (Grid E-6) | — | PID-1-SF-LR20483 |
| Outlet Stream Destination | Postfilter F-34 via valve 1-SF-V38 (Grid E-5) | — | PID-1-SF-LR20483 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PDIS-2624](/instruments/PDIS-2624.md) | Resin Bed Differential Pressure Monitoring | Differential Pressure Indicator, Switch | Across DM-8 (Inlet top head vs Outlet bottom head, Grid E-6) | DP High Setpoint | Demineralizer resin bed differential pressure indication and high alarm | PID-1-SF-LR20483 |
| [TE-2625](/instruments/TE-2625.md) | Inlet Temperature Monitoring for Resin Bed Protection | Temperature Element | Demineralizer Inlet Header (Grid Column 6, Row H) | High Temperature Alarm | High inlet fluid temperature alarm / resin thermal protection | PID-1-SF-LR20483 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-SF-DM8-IN | INLET | F-33 Manifold | DM-8 | 3" | 1-SF-V40 | Pool ambient (monitored by TE-2625) | Cleanup loop operating pressure | — | Main process inlet from prefilter F-33 effluent / purification manifold |
| STR-SF-DM8-OUT | OUTLET | DM-8 | F-34 Manifold | 3"x4" | 1-SF-V38 | Pool ambient | Downstream header pressure | — | Demineralized effluent routing to Postfilter F-34 inlet header |
| STR-SF-DM8-BYPASS | BYPASS | F-33 Effluent | F-34 Manifold | 4" | 1-SF-V76 | Pool ambient | Header pressure | — | Full demineralizer bypass around DM-8 |
| STR-SF-DM8-RESIN-FILL | INLET | Resin Addition Station | DM-8 Top Head | 3" | 1-SF-V36 | Ambient | Resin fill pressure | — | Fresh resin fill connection to top head |
| STR-SF-DM8-SLUICE | OUTLET | DM-8 Bottom Head | RS-TK-79A & B (20252 [G-4]) | 3" | 1-SF-V49, 1-SF-V57 (Boundary MOV/Gate) | Ambient | Sluicing header pressure | — | Spent resin sluice discharge from bottom head to Spent Resin Sluicing System |
| STR-SF-DM8-SLUICE-WTR | UTILITY | RS Sluice Water Supply (20252 [H-3]) | DM-8 Bottom Head | 3" | 1-SF-V47 | Ambient | Sluice water supply pressure | — | Sluice water supply connection to bottom head for resin transfer/fluidization |

## Hazards & Safeguards

- Thermal degradation of ion exchange resin: High temperature above resin operating limit (typically ~140°F / 60°C) causes irreversible breakdown of resin beads and release of sulfonic/amine groups; monitored upstream by temperature element TE-2625 on inlet header.
- Resin bed compaction / channeling / high differential pressure: Monitored across demineralizer shell by PDIS-2624; excessive DP requires resin replacement/sluice.
- Resin migration downstream: Protected by downstream Fuel Pool Postfilter F-34 to capture resin fines or fragments before water returns to Spent Fuel Pool.
- Radiation shielding / radioactive resin transfer: Sluice discharge through 1-SF-V49 and boundary valve 1-SF-V57 to Spent Resin Sluicing Tanks RS-TK-79A/B.

## References & Sources

[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
