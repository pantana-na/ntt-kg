---
type: Equipment Concept
title: CC-E-17B — Primary Component Cooling Water Heat Exchanger B
description: Primary nuclear safety-related component cooling water heat exchanger
  for Train B, transferring heat from the closed-loop Primary Component Cooling Water
  System (shell side) to the open-loop Nuclear Service Water System (tube side, titanium
  tubes).
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/CC-E-17B.md
tags:
- cc
- equipment
- heat exchanger
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-3.pdf
  title: ML101620329-part-3.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-11-05T14:30:51Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:30:51Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:30:51Z'
status: stable
entity_metadata:
  tag: CC-E-17B
  name: Primary Component Cooling Water Heat Exchanger B
  equipment_class: Heat Exchanger
  unit: CC
  instruments:
  - tag: TE 6115
    service: Service Water Discharge Temperature
    type: Temperature Element
    location: CC-E-17B SW Discharge Line [8-D]
    setpoint_or_range: —
    interlock_or_alarm: Discharge temperature monitoring / thermal performance
    source: PID-1-SW-LR20795
  - tag: PSL 6113
    service: Service Water Discharge Pressure Low
    type: Pressure Switch Low
    location: CC-E-17B SW Discharge Line [8-D]
    setpoint_or_range: —
    interlock_or_alarm: Low service water discharge pressure alarm / trip logic
    source: PID-1-SW-LR20795
  - tag: V17
    service: SW Discharge Isolation / Realignment
    type: Motor-Operated Control Valve
    location: CC-E-17B SW Discharge Line [7-D]
    setpoint_or_range: 24" MOV
    interlock_or_alarm: Controlled by TA Logic (A) for emergency alignment
    source: PID-1-SW-LR20795
  - tag: V5
    service: SW Supply Isolation on LOOP
    type: Motor-Operated Valve
    location: CC-E-17B SW Supply Line [11-E]
    setpoint_or_range: 12" MOV
    interlock_or_alarm: Direct interlock to close on complete Loss of Off-Site Power
      (LOOP) per General Note 7
    source: PID-1-SW-LR20795
  connections:
  - stream_id: SW-IN-CC-E-17B
    direction: INLET
    source_tag: SW-PAB-TRAIN-B
    target_tag: CC-E-17B
    line_size: 24" (from 12" branch)
    inline_components:
    - V5 (Motor-Operated Valve, Closes on LOOP)
    - V12 (Locked Open Gate Valve)
    temperature: Ocean seawater supply temp
    pressure: —
    flow_rate: —
    description: Train B 24" service water supply through MOV V5 and locked open isolation
      V12
    source: PID-1-SW-LR20795 (Grid 11-E..9-C)
  - stream_id: SW-OUT-CC-E-17B
    direction: OUTLET
    source_tag: CC-E-17B
    target_tag: SW-RET-HDR
    line_size: 24"
    inline_components:
    - V17 (Motor-Operated Valve, Controlled by TA Logic A)
    - TE 6115 (Temperature Element)
    - PSL 6113 (Pressure Switch Low)
    temperature: Monitored by TE 6115
    pressure: Monitored by PSL 6113
    flow_rate: —
    description: 24" Service water discharge from CC-E-17B tube side to SW return
      header
    source: PID-1-SW-LR20795 (Grid 8-D..7-D)
  - stream_id: SW-REL-CC-E-17B
    direction: RELIEF
    source_tag: CC-E-17B
    target_tag: FUNNEL-DRAIN
    line_size: 3/4" x 1"
    inline_components:
    - V37 (Thermal Relief Valve, SET PRESS. @ 150 PSIG)
    temperature: Ambient
    pressure: 150 PSIG setpoint
    flow_rate: —
    description: Tube side overpressure thermal relief valve V37 discharging to open
      funnel drain
    source: PID-1-SW-LR20795 (Grid 8-D)
  - stream_id: SW-VENT-CC-E-17B
    direction: VENT
    source_tag: CC-E-17B
    target_tag: ATMOSPHERE
    line_size: 3/4" / 2"
    inline_components:
    - V97 (Vent Valve)
    - V98 (Vent Valve)
    - V172 (Isolation Valve)
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Tube side vent manifold with material class break from Titanium to
      Carbon Steel per LR Note 6
    source: PID-1-SW-LR20795 (Grid 8-D)
  - stream_id: SW-DR-CC-E-17B
    direction: DRAIN
    source_tag: CC-E-17B
    target_tag: PAB-DRAIN-HUB
    line_size: 1"
    inline_components:
    - V99 (Drain Valve)
    - V171 (Drain Valve)
    - V175 (Drain Valve)
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: —
    description: Tube side and channel head drain line
    source: PID-1-SW-LR20795 (Grid 8-C / 9-C)
---

# CC-E-17B — Primary Component Cooling Water Heat Exchanger B

## Function

Primary nuclear safety-related component cooling water heat exchanger for Train B, transferring heat from the closed-loop Primary Component Cooling Water System (shell side) to the open-loop Nuclear Service Water System (tube side, titanium tubes).

## Design Data

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Equipment Tag & Prefix | CC-E-17B (1-CC-E-17B) (General Note 2 & Sheet 4 Grid 8-C/D) | — | PID-1-SW-LR20795 |
| Nuclear Safety Classification | Nuclear Safety Related (Category 1) (Drawing Title Block) | — | PID-1-SW-LR20795 |
| License Renewal AMR Status | In Scope (AMR) per 10 CFR 54.4(a)(1) / (a)(3) (Red line color coding per 10 CFR 54.21) | — | PID-1-SW-LR20795 |
| Tube Material Metallurgy | Titanium (XX denoted) (General Note 8: 'XX - DENOTES TITANIUM MATERIAL') | — | PID-1-SW-LR20795 |
| Piping Class Break at Vents | Material change from Titanium (CC side) to Carbon Steel (SW side) at vent valves V97/V98 (LR Note 6) | — | PID-1-SW-LR20795 |
| Thermal Relief Valve Setpoint | 150 (Valve V37, 3/4" x 1") (Grid 8-D) | PSIG | PID-1-SW-LR20795 |

## Operating Conditions

| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Cooling Medium (Tube Side) | Raw Ocean Seawater (Service Water Train B) | — | PID-1-SW-LR20795 |
| Process Medium (Shell Side) | Inhibited Demineralized Water (Component Cooling Water) | — | PID-1-SW-LR20795 |
| Plant Location | Primary Auxiliary Building (PAB) [8-9, C-D] | — | PID-1-SW-LR20795 |

## Instrumentation & Control Loops (P&ID)

| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TE 6115](/instruments/le-2384-1.md) | Service Water Discharge Temperature | Temperature Element | CC-E-17B SW Discharge Line [8-D] | — | Discharge temperature monitoring / thermal performance | PID-1-SW-LR20795 |
| [PSL 6113](/instruments/le-2384-1.md) | Service Water Discharge Pressure Low | Pressure Switch Low | CC-E-17B SW Discharge Line [8-D] | — | Low service water discharge pressure alarm / trip logic | PID-1-SW-LR20795 |
| V17 | SW Discharge Isolation / Realignment | Motor-Operated Control Valve | CC-E-17B SW Discharge Line [7-D] | 24" MOV | Controlled by TA Logic (A) for emergency alignment | PID-1-SW-LR20795 |
| [V5](/instruments/le-2384-1.md) | SW Supply Isolation on LOOP | Motor-Operated Valve | CC-E-17B SW Supply Line [11-E] | 12" MOV | Direct interlock to close on complete Loss of Off-Site Power (LOOP) per General Note 7 | PID-1-SW-LR20795 |

## Connections & Stream Summary

| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SW-IN-CC-E-17B | INLET | SW-PAB-TRAIN-B | CC-E-17B | 24" (from 12" branch) | V5 (Motor-Operated Valve, Closes on LOOP), V12 (Locked Open Gate Valve) | Ocean seawater supply temp | — | — | Train B 24" service water supply through MOV V5 and locked open isolation V12 |
| SW-OUT-CC-E-17B | OUTLET | CC-E-17B | SW-RET-HDR | 24" | V17 (Motor-Operated Valve, Controlled by TA Logic A), TE 6115 (Temperature Element), PSL 6113 (Pressure Switch Low) | Monitored by TE 6115 | Monitored by PSL 6113 | — | 24" Service water discharge from CC-E-17B tube side to SW return header |
| SW-REL-CC-E-17B | RELIEF | CC-E-17B | FUNNEL-DRAIN | 3/4" x 1" | V37 (Thermal Relief Valve, SET PRESS. @ 150 PSIG) | Ambient | 150 PSIG setpoint | — | Tube side overpressure thermal relief valve V37 discharging to open funnel drain |
| SW-VENT-CC-E-17B | VENT | CC-E-17B | ATMOSPHERE | 3/4" / 2" | V97 (Vent Valve), V98 (Vent Valve), V172 (Isolation Valve) | Ambient | Atmospheric | — | Tube side vent manifold with material class break from Titanium to Carbon Steel per LR Note 6 |
| SW-DR-CC-E-17B | DRAIN | CC-E-17B | PAB-DRAIN-HUB | 1" | V99 (Drain Valve), V171 (Drain Valve), V175 (Drain Valve) | Ambient | Atmospheric | — | Tube side and channel head drain line |

## Hazards & Safeguards

- Loss of Off-Site Power (LOOP) causes direct interlock closure of SW inlet motor-operated valve V5 per General Note 7.
- Seawater tube-side fouling or micro-biologically influenced corrosion mitigated by Titanium tube metallurgy (XX denoted).
- Thermal overpressurization of isolated tube side mitigated by safety relief valve V37 set at 150 PSIG.

## References & Sources

[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
