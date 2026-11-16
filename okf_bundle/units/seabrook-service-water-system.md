---
type: Unit Overview
title: 'Unit Overview: Seabrook Station Service Water System (SW & SWA)'
description: Nuclear safety-related Service Water System (SW) and Air Handling System
  (SWA) for Seabrook Station, providing ultimate heat sink cooling via ocean intake
  and mechanical draft cooling tower.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/units/seabrook-service-water-system.md
tags:
- cooling-tower
- nuclear-safety
- p-and-id
- seabrook-station
- service-water
- unit-overview
- ventilation
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-3.pdf
  title: ML101620329-part-3.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-11-05T14:36:06Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:36:06Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:36:06Z'
status: stable
entity_metadata:
  system_prefix: SW
  pids:
  - PID-1-SWA-LR20372
  - PID-1-SW-LR20794
  - PID-1-SW-LR20795
  - PID-1-SW-LR20796
  unit: Seabrook Station Unit 1
  primary_fluids:
  - Raw Seawater
  - Treated Basin Water
  pumps:
  - P-41A
  - P-41B
  - P-41C
  - P-41D
  - P-110A
  - P-110B
---

# Unit Overview: Seabrook Station Service Water System (SW & SWA)

> ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
> The Service Water System (SW) is the ultimate safety-related cooling medium for Seabrook Station, rejecting heat from the Primary Component Cooling Water System (CC), Emergency Diesel Generators (DG), and secondary loads to the Atlantic Ocean or the Ultimate Heat Sink (UHS) Service Water Cooling Tower. On a complete Loss of Offsite Power (LOOP), motor-operated valves 1-SW-V4 and 1-SW-V5 close automatically per General Note 7. Transition between ocean discharge and cooling tower recirculation is governed by safety-related TA Logic (A) modulating valves 1-SW-V15, V17, V19, V20, V23, and V34.

## System Mission & Operational Topology
The Service Water System consists of two 100% redundant, safety-related cooling trains (Train A and Train B):
1. **Normal Ocean Cooling Mode:**
   * Four ocean intake service water pumps (`P-41A` & `P-41C` for Train A; `P-41B` & `P-41D` for Train B) draw raw seawater from the offshore Atlantic Ocean intake tunnel through the Service Water Pumphouse forebay well.
   * Seawater flows through 24" supply headers into the Primary Auxiliary Building (PAB), passing through automatic backwashing strainers `S-11` (Train A) and `S-10` (Train B) monitored by differential pressure switches `PDIS 8259` and `PDIS 8258`.
   * Filtered seawater cools Primary Component Cooling Water Heat Exchangers `CC-E-17A` (Train A) and `CC-E-17B` (Train B) (featuring titanium tube metallurgy `XX`), Emergency Diesel Generator Jacket Coolers `DG-E-42A` and `DG-E-42B`, and Turbine Building secondary coolers `SCC-E-29A` and `SCC-E-29B`.
   * Heated effluent discharges through the ocean discharge transition structure back to the ocean outfall.
2. **Emergency Ultimate Heat Sink (UHS) Cooling Tower Mode:**
   * Upon loss of ocean intake or emergency transition (actuated by TA Logic), discharge flow is realigned to the Service Water Cooling Tower spray header nozzle arrays via preset balancing valves `1-SW-V56` and `1-SW-V27`.
   * Two safety-related cooling tower pumps (`P-110A` for Train A; `P-110B` for Train B) take suction from the cooling tower cold water basin (Basin floor Elev. 46'-0") and recirculate cooling water through the safety trains.
   * Mechanical draft cooling tower fans (`FN-51A`, `FN-51B`, and Unit 2 fan `2-SW-FN-51B` required for Unit 1 per LR Note 6) induce airflow across the cooling tower fill to reject decay heat.
3. **Pumphouse & Cooling Tower Ventilation (SWA):**
   * Safety-related ventilation supply fans `FN-40A` and `FN-40B` (3,400 CFM each) with roll filters `F-57` and `F-58` deliver outdoor air to pumphouse switchgear rooms.
   * Exhaust fans `FN-38A` and `FN-38B` discharge air through tornado dampers `DP-367`, `DP-369`, and `DP-370`.

## Primary Equipment Inventory
| Tag | Description | Train / Safety Class | Function |
| :--- | :--- | :--- | :--- |
| **P-41A / P-41C** | Ocean Intake Service Water Pumps A & C | Train A / Nuclear Safety Related | Ocean intake supply to Train A |
| **P-41B / P-41D** | Ocean Intake Service Water Pumps B & D | Train B / Nuclear Safety Related | Ocean intake supply to Train B |
| **P-110A** | Cooling Tower Service Water Pump 110A | Train A / Nuclear Safety Related | UHS basin recirculation to Train A |
| **P-110B** | Cooling Tower Service Water Pump 110B | Train B / Nuclear Safety Related | UHS basin recirculation to Train B |
| **S-11** | Service Water Automatic Strainer A | Train A / Nuclear Safety Related | In-line 24" seawater debris removal |
| **S-10** | Service Water Automatic Strainer B | Train B / Nuclear Safety Related | In-line 24" seawater debris removal |
| **CC-E-17A** | Primary Component Cooling Water HX A | Train A / Nuclear Safety Related | Closed-loop CCW heat removal (Titanium tubes) |
| **CC-E-17B** | Primary Component Cooling Water HX B | Train B / Nuclear Safety Related | Closed-loop CCW heat removal (Titanium tubes) |
| **DG-E-42A** | Diesel Generator 1A Jacket Water HX | Train A (EDG 1A) / Safety Related | Engine cooling on EDG start (Valve FO 8291) |
| **DG-E-42B** | Diesel Generator 1B Jacket Water HX | Train B (EDG 1B) / Safety Related | Engine cooling on EDG start (Valve FO 8292) |
| **SCC-E-29A / B** | Secondary Component Cooling Water HXs | Non-Nuclear Safety (AMR (a)(2)) | Turbine building conventional cooling |
| **FN-51A / B** | Cooling Tower Induced Draft Fans | Unit 1 / Nuclear Safety Related | Air induction across cooling tower fill |
| **2-SW-FN-51B** | Unit 2 Cooling Tower Fan 51B | Required for Unit 1 per LR Note 6 | Unit 1 MCB controlled UHS fan |
| **FN-40A / B** | Pumphouse Ventilation Supply Fans | SWA / Nuclear Safety Related | 3,400 CFM filtered airflow to switchgear rms |
| **SF-E-15C** | Spent Fuel Pool Heat Exchanger C | Safety Class 3 (Retired / Abandoned) | Isolated and blanked per LR Notes 1–5 |

## Key Instrumentation & Interlock Summary
* **TA Logic Realignment (Reference A):** Automatic command controlling motor-operated butterfly valves `1-SW-V15`, `V17`, `V19`, `V20`, `V23`, and `V34` to redirect SW discharge from ocean outfall to cooling tower spray headers during accident conditions.
* **Loss of Offsite Power (LOOP) Isolation:** Fast closure of MOVs `1-SW-V4` and `1-SW-V5` on LOOP (General Note 7) to shed non-essential CCW loads.
* **Emergency Diesel Generator Start (References B & C):** Open commands sent to fail-open control valves `FO 8291` (DG-1A) and `FO 8292` (DG-1B) to establish immediate cooling water flow.
* **Strainer DP Monitoring:** Switches `PDIS 8259` and `PDIS 8258` continuously monitor strainer loading and initiate automated backwashing.
* **Cooling Tower Return Flow:** Flow elements `FE-6163`/`FT-6163` and `FE-6173`/`FT-6173` verify safety-related cooling tower return flow.

## License Renewal Boundary Notes & Scoping Summary
* **Safety Related (Red Scope):** All ocean intake pumps, strainers, CCW heat exchangers, diesel coolers, cooling tower pumps, cooling tower fans, and pumphouse ventilation fans are within scope per 10 CFR 54.4(a)(1) and subject to AMR per 10 CFR 54.21.
* **Fire Protection Tie-In (LR Note 1):** 6" line from SW Train B to Fire Protection standpipe through valve `1-SW-V120` is included in scope per 10 CFR 54.4(a)(3).
* **Retired / Abandoned Equipment (LR Note 5):** Spent Fuel Pool Heat Exchanger `SF-E-15C` and Unit 2 fan `2-SW-FN-51A` are isolated, drained, and blanked under the Equipment to be Abandoned Program and are out of scope.

## References & Grounding Sources
[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
