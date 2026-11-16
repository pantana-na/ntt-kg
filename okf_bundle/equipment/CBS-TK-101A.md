---
type: Equipment Concept
title: CBS-TK-101A — Protective Chamber A (Sump A Guard Pipe Enclosure)
description: Safety Class 2 sealed protective chamber enclosing the containment recirculation
  sump A suction line, expansion bellows CBS-EP-36A, and motor-operated sump isolation
  valve CBS-V8, providing containment isolation barrier redundancy and leak detection
  via level switch LS-2356 outside containment penetration X-61.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/equipment/CBS-TK-101A.md
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
  at: '2026-10-19T14:03:50Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-19T14:03:50Z'
- by: process:okf-validation-suite
  at: '2026-10-19T14:03:50Z'
status: stable
entity_metadata:
  tag: CBS-TK-101A
  name: Protective Chamber A (Sump A Guard Pipe Enclosure)
  equipment_class: Vessel
  unit: SI / CBS
  instruments:
  - tag: LS-2356
    service: Protective Chamber Leak Detection Level Switch
    type: Process Instrument
    location: Chamber Body (Grid E-10)
    setpoint_or_range: Liquid level detection (High Alarm)
    interlock_or_alarm: High liquid level alarm in Main Control Room signaling guard
      pipe, bellows CBS-EP-36A, or valve CBS-V8 stem leakage
    source: PID-1-SI-LR20448
  connections:
  - stream_id: STR-CBS-TK101A-SUCT-IN
    direction: INLET
    source_tag: CBS-TK-10A
    target_tag: CBS-TK-101A
    line_size: 16"
    inline_components:
    - Guard pipe 1-CBS-S-611-A
    - Penetration X-61
    - Concentric Guard Pipe 1-CBS-S-611-A
    - Containment Penetration X-61
    temperature: Ambient to 250 °F (post-LOCA)
    pressure: Post-LOCA Containment Flood Static Head
    flow_rate: Full ECCS Sump Recirculation Flow
    description: 16" Containment Recirculation Sump A suction line entering protective
      chamber through Penetration X-61
    source: PID-1-SI-LR20448
  - stream_id: STR-CBS-TK101A-SUCT-OUT
    direction: OUTLET
    source_tag: CBS-TK-101A
    target_tag: RH-P-8A / CBS-P-9A Suction
    line_size: 16"
    inline_components:
    - CBS-V8 (MOV)
    - CBS-EP-36A (Expansion Joint)
    - CBS-V115
    - CBS-EP-36A (Expansion Bellows)
    - CBS-V115 (16" Test Conn)
    temperature: Ambient to 250 °F (post-LOCA)
    pressure: Post-LOCA Containment Flood Static Head
    flow_rate: Full ECCS Sump Recirculation Flow
    description: 16" Sump A suction header exiting protective chamber to RHR Pump
      RH-P-8A and Containment Spray Pump CBS-P-9A (via Dwg. 20233)
    source: PID-1-SI-LR20448
  - stream_id: STR-CBS-TK101A-DRN
    direction: DRAIN
    source_tag: CBS-TK-101A
    target_tag: WLD DR 153
    line_size: 1/2"x3/4"
    inline_components:
    - CBS-V88
    - CBS-V89
    - CBS-V92 (LC)
    - CBS-V127 (LC)
    - CBS-V92 (3/4" LC)
    - CBS-V127 (3/4" LC)
    temperature: Ambient
    pressure: Atmospheric
    flow_rate: Intermittent Drainage / Leakage
    description: Chamber floor drainage line routed to radioactive Waste Processing
      Liquid Drains funnel DR 153
    source: PID-1-SI-LR20448
  - stream_id: STR-CBS-TK101A-AIR-TEST
    direction: UTILITY
    source_tag: TEST-AIR-SUPPLY
    target_tag: CBS-TK-101A
    line_size: 1/2"
    inline_components:
    - CBS-V88 (1/2" Globe)
    - CBS-V89 (1/2" Globe)
    temperature: Ambient
    pressure: Pneumatic Test Pressure
    flow_rate: Intermittent Test Flow
    description: Dual-valve pneumatic test / air pressurization connection for chamber
      integrity verification
    source: PID-1-SI-LR20448
---

# CBS-TK-101A — Protective Chamber A (Sump A Guard Pipe Enclosure)

## Function
Safety Class 2 sealed protective chamber enclosing the containment recirculation sump A suction line, expansion bellows CBS-EP-36A, and motor-operated sump isolation valve CBS-V8, providing containment isolation barrier redundancy and leak detection via level switch LS-2356 outside containment penetration X-61.

## Design Data
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Drawing Number | PID-1-SI-LR20448 (Rev. 11, Ref. B20448) (Rev. 11, Ref. B20448) | — | PID-1-SI-LR20448 |
| Safety Classification | Safety Class 2 (Nuclear Safety Related) (Nuclear Safety Related) | — | PID-1-SI-LR20448 |
| Physical Location | Mechanical Penetration Area / Outside Containment (Grid E-10) | — | PID-1-SI-LR20448 |
| AMR Status | In Scope 10 CFR 54.4(a)(1) & (a)(3) [Red] | — | PID-1-SI-LR20448 |
| Enclosed Concentric Guard Pipe | 1-CBS-S-611-A | — | PID-1-SI-LR20448 |
| Containment Penetration | Penetration X-61 (Evaluated under civil-structural system LRSP-CNT) | — | PID-1-SI-LR20448 |
| Enclosed Isolation Valve | CBS-V8 (16" Motor-Operated Gate Valve, Interlock A) (Interlocked with containment flood level transmitters CBS-LT-930..933; 16" Motor-Operated Valve, Interlock A) | — | PID-1-SI-LR20448 |
| Internal Expansion Joint | CBS-EP-36A (Flexible Expansion Bellows) (Accommodates seismic displacement and thermal expansion) | — | PID-1-SI-LR20448 |
| Test and Flush Isolation Valve | CBS-V115 (16" Test Connection) | — | PID-1-SI-LR20448 |
| Air Test Connection Valves | CBS-V88, CBS-V89 (1/2" Globe / Needle Valves) | — | PID-1-SI-LR20448 |
| Drain Isolation Valves | CBS-V92 (3/4" LC), CBS-V127 (3/4" LC to DR 153) (Locked Closed (LC) during plant operation) | — | PID-1-SI-LR20448 |

## Operating Conditions
| Parameter | Value | Unit | Source |
| :--- | :--- | :--- | :--- |
| Internal Environment (Normal) | Air / Inert Gas (normally sealed, atmospheric, dry) (normally sealed and drained) | — | PID-1-SI-LR20448 |
| Post-Accident Service Fluid | Borated Recirculation Water (retained upon suction pipe or bellows leakage) (retained upon suction pipe leakage) | — | PID-1-SI-LR20448 |
| Drain Destination | Waste Liquid Drains DR 153 via CBS-V127 (Primary Auxiliary Building Liquid Drains, Dwg. 20221) | — | PID-1-SI-LR20448 |
| Design Function | Containment Isolation Boundary Extension & Sump Recirculation Guard Pipe Enclosure | — | PID-1-SI-LR20448 |

## Instrumentation & Control Loops (P&ID)
| Tag | Service | Instrument Type | Location / Tap | Range / Setpoint | Alarm / Interlock | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LS-2356](/instruments/LS-2356.md) | Protective Chamber Leak Detection Level Switch | Process Instrument | Chamber Body (Grid E-10) | Liquid level detection (High Alarm) | High liquid level alarm in Main Control Room signaling guard pipe, bellows CBS-EP-36A, or valve CBS-V8 stem leakage | PID-1-SI-LR20448 |

## Connections & Stream Summary
| Stream | Direction | From (Source) | To (Target) | Line Size | Inline Valves / Components | Temp | Pressure | Flow Rate | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STR-CBS-TK101A-SUCT-IN | INLET | CBS-TK-10A | CBS-TK-101A | 16" | Guard pipe 1-CBS-S-611-A, Penetration X-61, Concentric Guard Pipe 1-CBS-S-611-A, Containment Penetration X-61 | Ambient to 250 °F (post-LOCA) | Post-LOCA Containment Flood Static Head | Full ECCS Sump Recirculation Flow | 16" Containment Recirculation Sump A suction line entering protective chamber through Penetration X-61 |
| STR-CBS-TK101A-SUCT-OUT | OUTLET | CBS-TK-101A | RH-P-8A / CBS-P-9A Suction | 16" | CBS-V8 (MOV), CBS-EP-36A (Expansion Joint), CBS-V115, CBS-EP-36A (Expansion Bellows), CBS-V115 (16" Test Conn) | Ambient to 250 °F (post-LOCA) | Post-LOCA Containment Flood Static Head | Full ECCS Sump Recirculation Flow | 16" Sump A suction header exiting protective chamber to RHR Pump RH-P-8A and Containment Spray Pump CBS-P-9A (via Dwg. 20233) |
| STR-CBS-TK101A-DRN | DRAIN | CBS-TK-101A | WLD DR 153 | 1/2"x3/4" | CBS-V88, CBS-V89, CBS-V92 (LC), CBS-V127 (LC), CBS-V92 (3/4" LC), CBS-V127 (3/4" LC) | Ambient | Atmospheric | Intermittent Drainage / Leakage | Chamber floor drainage line routed to radioactive Waste Processing Liquid Drains funnel DR 153 |
| STR-CBS-TK101A-AIR-TEST | UTILITY | TEST-AIR-SUPPLY | CBS-TK-101A | 1/2" | CBS-V88 (1/2" Globe), CBS-V89 (1/2" Globe) | Ambient | Pneumatic Test Pressure | Intermittent Test Flow | Dual-valve pneumatic test / air pressurization connection for chamber integrity verification |

## Hazards & Safeguards
- Post-accident radioactive effluent containment: Guard pipe and protective chamber form an extension of containment boundary outside penetration X-61; any leakage from valve CBS-V8 or bellows CBS-EP-36A is contained within chamber and detected by LS-2356.
- Sump MOV inadvertent operation: MOV CBS-V8 is interlocked (Interlock A per Note 6) with containment water levels CBS-LT-930..933 (drawing 20233) to prevent opening prior to reaching adequate flood level in containment.
- Drain valve lineup: Drain valves CBS-V92 and CBS-V127 are maintained Locked Closed (LC) to prevent unmonitored release during plant operation and accident recirculation.
- Post-Accident Radioactive Effluent Containment: Guard pipe 1-CBS-S-611-A and protective chamber CBS-TK-101A form an extension of the reactor containment boundary outside penetration X-61. Any leakage from motor-operated isolation valve CBS-V8 or expansion bellows CBS-EP-36A is contained within the sealed chamber shell and alarmed by level switch LS-2356.
- Sump MOV Inadvertent Operation & Interlock Philosophy: MOV CBS-V8 is interlocked (Interlock A per Note 6) with containment water level transmitters CBS-LT-930, LT-931, LT-932, and LT-933 (drawing CBS-20233) to prevent inadvertent opening prior to verifying adequate water level in the containment sump, protecting ECCS pumps from air ingestion and vortexing.
- Drain Isolation Lineup Integrity: Manual drain isolation valves CBS-V92 and CBS-V127 are maintained Locked Closed (LC) during plant operation to ensure containment boundary integrity and prevent unmonitored radioactive liquid releases to waste drain DR 153.
- Seismic and Thermal Expansion Protection: Expansion bellows CBS-EP-36A accommodates differential thermal expansion and seismic displacements between the containment penetration sleeve X-61 and the external piping support structure while maintaining leaktight boundary containment.

## References & Sources
[^src-1]: ML101620329-part-1.pdf (reference/raw/pid/ML101620329-part-1.pdf)
