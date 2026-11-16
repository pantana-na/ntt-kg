---
type: Source Document
title: 'P&ID Package: ML101620329 Part 3 (Seabrook Station LR P&IDs)'
description: Seabrook Station License Renewal P&ID Package ML101620329 Part 3 covering
  Service Water (SW), SW Pumphouse & Cooling Tower Air Handling (SWA), and Steam Generator
  Sample Panel 166B (SS) across 5 drawing sheets.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/sources/seabrook-lr-pids-ml101620329-part-3.md
tags:
- license-renewal
- p-and-id
- sample-system
- seabrook-station
- service-water
- ventilation
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-3.pdf
  title: ML101620329-part-3.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-11-05T14:27:45Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:27:45Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:27:45Z'
status: stable
entity_metadata:
  page_count: 5
  drawing_numbers:
  - PID-1-SS-LR20521
  - PID-1-SWA-LR20372
  - PID-1-SW-LR20794
  - PID-1-SW-LR20795
  - PID-1-SW-LR20796
  facility: Seabrook Station
---

# Source Document: Seabrook Station License Renewal P&ID Package (ML101620329 Part 3)

## Document Metadata

| Attribute | Specification |
| :--- | :--- |
| **Document Number** | ML101620329 Part 3 |
| **Facility / Plant** | Seabrook Station (NextEra Energy Seabrook, LLC) |
| **File Location** | `reference/raw/pid/ML101620329-part-3.pdf` |
| **Total Sheets / Pages** | 5 Drawing Sheets |
| **Primary System Classifications** | Nuclear Safety Related (SW, SWA) & Safety Class NNS (SS, SWA non-safety, SF isolated) |
| **Scoping Standard** | 10 CFR 54 License Renewal Scoping / Aging Management Review (AMR) |

## Drawing Index & Scope Summary

### Sheet 1: Drawing PID-1-SS-LR20521 (Rev. 15 / Ref. B20521 Rev. 15)
* **Title:** Sample System Steam Generator Sample Panel 166B P&ID (License Renewal P&ID)
* **Reference Drawing:** PID-1-SS-820521 / PID-1-SS-B20521
* **Associated Drawings:** 20516, 20518, 20519, 20520, 20522, 20626, 20206, 20222, 20350
* **System Prefix:** `SS` (General Note 2: "ALL LINES, EQUIPMENT, COMPONENTS AND INSTRUMENTS HAVE SYSTEM PREFIX SS, UNLESS NOTED OTHERWISE.")
* **Key Equipment & Packages:**
  * Steam Generator Primary Sample Heat Exchangers `1-SS-E-14A`, `1-SS-E-14B`, `1-SS-E-14C`, `1-SS-E-14D` (cooled by CCW Loop A).
  * S/G Sample Constant Temperature Coolers `1-SS-E-173`, `1-SS-E-174`, `1-SS-E-175`, `1-SS-E-176` (inside Panel CP-166B).
  * Refrigeration Skid & Chilled Circulator Package `SKD-128` (located outside PAB in non-safety area; includes Compressor `C-12`, Condenser `E-182` with dual fans `FN-214`/`FN-215`, Receiver `TK-262`, Filter Drier `F-201`, Hot Gas Bypass `PCV-9631`, Thermal Expansion Valve `TCV-9635`, Evaporator `E-183`, Suction Accumulator `TK-299`, Coolant Reservoir `TK-244`, Mixer `MM-948`, Recirc Pump `P-376`, and Strainer `F-311`).
  * Radiation Monitoring Skids `RM-SKD-83` (S/G A), `RM-SKD-84` (S/G B), `RM-SKD-85` (S/G C), `RM-SKD-86` (S/G D) equipped with detectors `RE-6510`, `RE-6511`, `RE-6512`, `RE-6513`.
  * S/G Sample Sink `MM-741` draining to Waste Liquid Drains (`WLD DR 256`).
  * Strong Acid Cation Conductivity (SACC) Column & Heater `H-376` (Note 6: only one S/G lined up at a time).
  * Optional Chemistry Filter elements `1-SS-F-177`, `1-SS-F-178`, `1-SS-F-179`, `1-SS-F-180` (Note 12).
  * High-point grab filter banks `F-203A/B`, `F-204A/B`, `F-205A/B`, `F-206A/B`.

### Sheet 2: Drawing PID-1-SWA-LR20372 (Rev. 0 / Ref. B20372 Rev. 7)
* **Title:** Air Handling System for Service Water Pumphouse and Service Water Cooling Tower License Renewal P&ID
* **Reference Drawing:** PID-1-SWA-B20372 (Rev. 7)
* **Nuclear Classification:** Portions of drawing are Nuclear Safety Related
* **System Prefix:** `SWA` (General Note 1: "ALL EQUIPMENT, COMPONENTS, & INSTRUMENTS HAVE SYSTEM PREFIX SWA UNLESS OTHERWISE NOTED.")
* **Key Equipment & Ductwork:**
  * Service Water Pumphouse Supply Fans `FN-40A` and `FN-40B` (3,400 CFM each, Red AMR scope) with Suction Roll Filters `F-57` and `F-58`.
  * Service Water Pumphouse Exhaust Fans `FN-38A` and `FN-38B` (Red AMR scope).
  * Electric Unit Heaters `UH-116`, `UH-117`, `UH-118`, `UH-119` in Switchgear Rooms (Black scope).
  * Tornado Dampers `DP-367`, `DP-369`, `DP-370` and Air Intake Dampers `DP-39A`, `DP-39B` (and Unit 2 dampers `2-DP-39A`, `2-DP-39B` needed for Unit 1 per Note 6).
  * Cooling Tower Mechanical Equipment Room Supply Fans `FN63` (0–4,300 CFM) and `FN64` (0–3,400 CFM), Roof Vent Fans `FN70` and `FN71` (0–10,500 CFM), and Intake Filter `F-192` with DP indicator `PDI-5731`.
  * Cooling Tower Switchgear Room Heaters `UH-112`, `UH-113`, `UH-114`, `UH-115`.

### Sheet 3: Drawing PID-1-SW-LR20794 (Rev. 33 / Ref. B20794 Rev. 33)
* **Title:** Service Water System Nuclear Detail License Renewal P&ID
* **Reference Drawing:** PID-1-SW-B20794 (Rev. 33)
* **Associated Drawings:** 20792 thru 20796
* **System Prefix:** `SW`, and `1` for Unit-1 (General Note 2)
* **Key Equipment & Infrastructure:**
  * Ocean Intake Service Water Pumps `P-41A` and `P-41C` (Train A, 20" suction / 24" discharge) and `P-41B` and `P-41D` (Train B).
  * Service Water Cooling Tower Pumps `P-110A` (Train A) and `P-110B` (Train B) located at Cooling Tower Basin (Basin floor Elev. 46'-0", Max water level Elev. 36'-0").
  * Cooling Tower Fans `FN-51A` and `FN-51B` (Unit 1, active) and `2-SW-FN-51B` (Unit 2, controlled from Unit 1 MCB and required for Unit 1 operation per LR Note 6; `2-SW-FN-51A` is abandoned and non-functional).
  * Intake & Discharge Transition Structures (42"/38" ocean tunnel expansion joints `2-EP-30`, `EP-31`, `EP-32`, `EP-33`, `2-EP-33`).
  * Cooling Tower Spray Header Nozzle Arrays (`SW-SPARYNOZZLE-CS-SR` commodity per LR Note 4) fed by preset flow balancing butterfly valves `1-SW-V56` (Train A) and `1-SW-V27` (Train B) (General Note 3).
  * Submerged cooling tower drop lines `1-SW-1810-18`, `1810-20`, `1810-21` (LR Note 5).

### Sheet 4: Drawing PID-1-SW-LR20795 (Rev. 37 / Ref. B20795 Rev. 37)
* **Title:** Service Water System Nuclear Detail License Renewal P&ID
* **Reference Drawing:** PID-1-SW-B20795 (Rev. 37)
* **Associated Drawings:** 20792, 20794
* **System Prefix:** `SW` (General Note 2)
* **Key Equipment & Safety Boundaries:**
  * Primary Component Cooling Water Heat Exchangers `CC-E-17A` (Train A) and `CC-E-17B` (Train B) featuring Titanium tube metallurgy (`XX` denoted per Note 8), with 24" SW supply MOVs `V4`/`V5` (interlocked to close on Loss of Offsite Power per Note 7) and 24" discharge MOVs `V15`/`V17` (controlled by TA Logic).
  * Diesel Generator Water Jacket Heat Exchangers `DG-E-42A` (Emergency Diesel Generator 1A, discharge control valve `FO 8291` opening on DG-1A start command) and `DG-E-42B` (EDG 1B, discharge control valve `FO 8292` opening on DG-1B start command).
  * Service Water Automatic Strainers `S-11` (Train A, 24") and `S-10` (Train B, 24") equipped with differential pressure switches `PDIS 8259` and `PDIS 8258`.
  * Secondary Component Cooling Water Heat Exchangers `SCC-E-29A` and `SCC-E-29B` (Turbine Building, 16" SW supply/return, DP switches `PDIS 6157` and `PDIS 6146`).
  * Auxiliary Secondary CCW Heat Exchangers `SCC-E-185A` and `SCC-E-185B` (6" lines, safety relief valves `V199` and `V200` set at 75 PSIG).
  * Condenser Water Box Priming Pump Heat Exchangers `AR-E-72A` and `AR-E-72B` (2" lines, balancing valves `V59` and `V60` per Note 4).
  * Fire Protection Standpipe Tie-In valve `1-SW-V120` (6" connection, LR Note 1).

### Sheet 5: Drawing PID-1-SW-LR20796 (Rev. 0 / Ref. B20794 Rev. 5)
* **Title:** Service Water System Nuclear Detail License Renewal P&ID
* **Reference Drawing:** PID-1-SW-B20794 (Rev. 5)
* **Associated Drawings:** 20792 thru 20795, 20482, 20220
* **System Prefix:** `SW`, and `1` for Unit-1 (General Note 2)
* **Key Equipment & Modifications:**
  * Spent Fuel Pool Heat Exchanger `SF-E-15C` (Safety Class 3, located in Fuel Storage Building).
  * Status per LR Note 1: `SF-E-15C` is isolated and drained. Fixed and spooled SW piping in the Spent Fuel Building has been removed as Alternate Spent Fuel Pool Cooling (ASFPC) is no longer required.
  * Status per LR Notes 2–5: Underground piping (lines `1845` and `1846`) is drained and isolated with blind flanges on both ends; cooling tower flanges are blanked; components are controlled under the Equipment to be Abandoned Program and are out of scope for License Renewal (internal air/gas environment).
  * Detail A: Recirculation Spool replacing lines `1764` and `1765-01-151-8"` (Note 4).

## Comprehensive Piping Line Schedule & Boundary Interfaces

| Line Designation / Identifier | Nominal Size | Drawing Sheet | Grid Location | Source / Origin | Target / Destination | Governing Boundary Valves & In-Line Elements |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `1-SW-24"-TRAIN-A-P41A` | 20" to 24" | Sheet 3 | 11-H..8-H | SW Pumphouse Suction Well | Train A 24" Common Discharge | Reducer 20"x24", Check `V1`, Isolation `V2`, Orifice `RO-6104`, Expansion Joint `EP-42` |
| `1-SW-24"-TRAIN-A-P41C` | 20" to 24" | Sheet 3 | 11-G..8-G | SW Pumphouse Suction Well | Train A 24" Common Discharge | Reducer 20"x24", Check `V21`, Isolation `V22`, Orifice `RO-6106`, Expansion Joint `EP-44` |
| `1-SW-24"-TRAIN-B-P41B` | 20" to 24" | Sheet 3 | 11-G..8-G | SW Pumphouse Suction Well | Train B 24" Common Discharge | Reducer 20"x24", Check `V28`, Isolation `V29`, Orifice `RO-6107`, Expansion Joint `EP-43` |
| `1-SW-24"-TRAIN-B-P41D` | 20" to 24" | Sheet 3 | 11-F..8-F | SW Pumphouse Suction Well | Train B 24" Common Discharge | Reducer 20"x24", Check `V30`, Isolation `V31`, Orifice `RO-6108`, Expansion Joint `EP-45` |
| `1-SW-24"-TRAIN-A-SUP` | 24" | Sheet 3 / 4 | [A-5] F / 12-C | SW Pumphouse Header Train A | PAB Strainer `S-11` Inlet | Pipe Anchor, Gate `V65` (LO), Bypass Gate `V67`, `PDIS 8259` taps |
| `1-SW-24"-TRAIN-B-SUP` | 24" | Sheet 3 / 4 | [A-5] B / 12-B | SW Pumphouse Header Train B | PAB Strainer `S-10` Inlet | Pipe Anchor, Gate `V68` (LO), Bypass Gate `V70`, `PDIS 8258` taps |
| `1-SW-24"-P110A-DISCH` | 24" | Sheet 3 | 9-D..7-C | Cooling Tower Pump `P-110A` | Train A Cross-tie / Tower Header | Check `V53`, Expansion Joint `EP-40`, Butterfly `V54`, `FE-6163`, `FT-6163` |
| `1-SW-24"-P110B-DISCH` | 24" | Sheet 3 | 9-C..7-C | Cooling Tower Pump `P-110B` | Train B Cross-tie / Tower Header | Check `V24`, Expansion Joint `EP-41`, Butterfly `V25`, `FE-6173`, `FT-6173` |
| `1-SW-24"-RET-TOWER-A` | 24" | Sheet 3 / 4 | 7-C / 6-D | CC-E-17A Discharge / Aux Bldg | Cooling Tower Spray Header A | MOV `V23` (TA Logic), Preset MOV `V19` / `V56`, Flow Orifice `FO-8293` |
| `1-SW-24"-RET-TOWER-B` | 24" | Sheet 3 / 4 | 6-C / 6-E | CC-E-17B Discharge / Aux Bldg | Cooling Tower Spray Header B | MOV `V34` (TA Logic), Preset MOV `V20` / `V27`, Flow Orifice `FO-8294` |
| `1-SW-24"-SUP-CC-17A` | 12" to 24" | Sheet 4 | 11-E..9-D | Train A 24" Main SW Header | Primary CCW HX `CC-E-17A` | MOV `V4` (Closes on LOOP), Header Isol `V11` (LO), Cross-tie `V14` (LO) |
| `1-SW-24"-DISCH-CC-17A`| 24" | Sheet 4 | 8-E..7-E | Primary CCW HX `CC-E-17A` | SW Return Header | MOV `V15` (TA Logic), `TE 6105`, `PSL 6103`, Relief `V32` (150 PSIG) |
| `1-SW-24"-SUP-CC-17B` | 12" to 24" | Sheet 4 | 11-E..9-C | Train B 24" Main SW Header | Primary CCW HX `CC-E-17B` | MOV `V5` (Closes on LOOP), Header Isol `V12` (LO) |
| `1-SW-24"-DISCH-CC-17B`| 24" | Sheet 4 | 8-D..7-D | Primary CCW HX `CC-E-17B` | SW Return Header | MOV `V17` (TA Logic), `TE 6115`, `PSL 6113`, Relief `V37` (150 PSIG) |
| `1-SW-16"-SUP-DG-42A` | 10" to 16" | Sheet 4 | 10-B..8-B | Train B 24" Main SW Header | Diesel Generator HX `DG-E-42A` | Isolation `V13` (LO), Relief `V514A` (145 PSIG) |
| `1-SW-16"-DISCH-DG-42A`| 16" | Sheet 4 | 8-B..7-B | Diesel Generator HX `DG-E-42A` | Train B SW Return Header | Check `V16`, Control Valve `FO 8291` (Open on DG-1A), `FE 6181`, `TI 6180` |
| `1-SW-16"-SUP-DG-42B` | 10" to 16" | Sheet 4 | 10-C..8-C | Train A 24" Main SW Header | Diesel Generator HX `DG-E-42B` | Relief `V514B` (145 PSIG) |
| `1-SW-16"-DISCH-DG-42B`| 16" | Sheet 4 | 8-C..7-C | Diesel Generator HX `DG-E-42B` | Train A SW Return Header | Check `V18`, Control Valve `FO 8292` (Open on DG-1B), `FE 6191`, `TI 6190` |
| `1-SW-20"-SUP-TB-A` | 20" | Sheet 4 | 10-F..9-F | Train A in SW Vault | Secondary CCW HXs (Turbine Bldg)| MOV `V76`, Check `V534`, Gate `V532` |
| `1-SW-20"-SUP-TB-B` | 20" | Sheet 4 | 10-F..9-G | Train B in SW Vault | Secondary CCW HXs (Turbine Bldg)| MOV `V74`, Check `V533`, Gate `V531` |
| `1-SW-16"-SCC-29A` | 16" | Sheet 4 | 9-F..8-G | Turbine Bldg 20" SW Header | Secondary CCW HX `SCC-E-29A` | Gate `V7`, Check `V9`, Gate `V508`, `PDIS 6157`, Reliefs `V509`/`V510` |
| `1-SW-16"-SCC-29B` | 16" | Sheet 4 | 9-G..8-H | Turbine Bldg 20" SW Header | Secondary CCW HX `SCC-E-29B` | Gate `V6`, Check `V8`, Gate `V501`, `PDIS 6146`, Reliefs `V502`/`V503` |
| `1-SW-6"-FP-TIE` | 6" | Sheet 4 | 10-A | Train B SW Supply Header | Fire Protection Standpipe | Isolation Valve `V120` (Ref Drawing 20268 [F-12]) |
| `1-SW-12"-SF-E-15C-SUP`| 12" | Sheet 5 | 9-G..6-E | Cooling Tower SW Supply Header | HX `SF-E-15C` Tube Inlet | Isolation `V207`, `V208`, Thermowell `TW 8296` (Drained/Blind Flanged) |
| `1-SW-12"-SF-E-15C-RET`| 12" | Sheet 5 | 6-D..9-D | HX `SF-E-15C` Tube Outlet | Cooling Tower SW Return Header | Isolation `V205`, `V206`, `TW 8297`, `FISL 8298`, Relief `V214` (150 PSIG) |
| `SF-8"-SF-E-15C-IN` | 8" | Sheet 5 | 4-F..5-E | SFP Cooling System (20482) | HX `SF-E-15C` Shell Inlet | Gate `SF-V181`, Thermal Relief `SF-V183` (150 PSIG to DR) |
| `SF-8"-SF-E-15C-OUT` | 8" | Sheet 5 | 5-E..4-E | HX `SF-E-15C` Shell Outlet | Spent Fuel Pool Return (20482) | Gate `SF-V180`, Drains to `WLD DR 132` |
| `SS-3/8"T-SG1-BLOWDOWN`| 3/8"T | Sheet 1 | 12-G..10-G | S/G 1 Blowdown (Dwg 20626 [F-12]) | Sample Cooler `1-SS-E-14A` | CCW Loop A supply (`CC-1"`), `TI-2785`, Relief `PCV-2826` |
| `SS-3/8"T-SG2-BLOWDOWN`| 3/8"T | Sheet 1 | 12-E..10-E | S/G 2 Blowdown (Dwg 20626 [F-12]) | Sample Cooler `1-SS-E-14B` | CCW Loop A supply (`CC-1"`), `TI-2786`, Relief `PCV-2827` |
| `SS-3/8"T-SG3-BLOWDOWN`| 3/8"T | Sheet 1 | 12-D..10-D | S/G 3 Blowdown (Dwg 20626 [E-12]) | Sample Cooler `1-SS-E-14C` | CCW Loop A supply (`CC-1"`), `TI-2787`, Relief `PCV-2828` |
| `SS-3/8"T-SG4-BLOWDOWN`| 3/8"T | Sheet 1 | 12-B..10-B | S/G 4 Blowdown (Dwg 20626 [E-12]) | Sample Cooler `1-SS-E-14D` | CCW Loop A supply (`CC-1"`), `TI-2788`, Relief `PCV-2829` |

## Comprehensive Instrumentation & Control Loops Inventory

| Instrument Tag | Service / Function | Measured Variable | Location / Connected Equipment | Output / Interlock Details |
| :--- | :--- | :--- | :--- | :--- |
| **LT-8260** | SW Pumphouse Basin Level | Level | Pumphouse Intake Well Forebay [6-H] | Remote level monitoring |
| **PT-8274** | SW Train A Discharge Header Pressure | Pressure | Pumphouse Header Train A [8-H] | Capillary transmitter per LR Note 2 |
| **PT-8273** | SW Train A Discharge Header Pressure | Pressure | Pumphouse Header Train A [7-H] | Capillary transmitter per LR Note 2 |
| **PT-8284** | SW Train A Discharge Header Pressure | Pressure | Pumphouse Header Train A [8-G] | Capillary transmitter per LR Note 2 |
| **PT-8272** | SW Train A Discharge Header Pressure | Pressure | Pumphouse Header Train A [7-G] | Capillary transmitter per LR Note 2 |
| **PT-8283** | SW Train A Discharge Header Pressure | Pressure | Pumphouse Header Train A [7-G] | Capillary transmitter per LR Note 2 |
| **PT-8282** | SW Train B Discharge Header Pressure | Pressure | Pumphouse Header Train B [7-F] | Capillary transmitter per LR Note 2 |
| **FE-6163 / FT-6163** | Cooling Tower Pump P-110A Flow | Flow | Pump P-110A 24" Discharge [8-C / 7-D] | Safety-related flow transmitter |
| **FE-6173 / FT-6173** | Cooling Tower Pump P-110B Flow | Flow | Pump P-110B 24" Discharge [7-C / 7-D] | Safety-related flow transmitter |
| **FO-8293** | Train A Cooling Tower Return Orifice | Flow Restriction | 24" Return Header to Cooling Tower [7-C] | Preset flow restriction orifice |
| **FO-8294** | Train B Cooling Tower Return Orifice | Flow Restriction | 24" Return Header to Cooling Tower [6-C] | Preset flow restriction orifice |
| **TE-6184 / PT-6183** | Cooling Tower Pump P-110A Discharge Temp & Press | Temp / Press | Pump P-110A Discharge Line [8-C] | Linked to TA Logic |
| **TE-6194 / PT-6193** | Cooling Tower Pump P-110B Discharge Temp & Press | Temp / Press | Pump P-110B Discharge Line [6-C] | Linked to TA Logic |
| **TE-6152A/B/C** | Cooling Tower Cold Basin Temp | Temperature | Cooling Tower Cold Water Basin [11-B / 10-B] | Ultimate Heat Sink water temp |
| **TE-8286 (x2)** | Cooling Tower Fan Drive Temp | Temperature | Fan Gearbox FN-51A / 2-FN-51A [11-D / 8-D] | Bearing/oil temperature |
| **PSL-8287 (x2)** | Fan Gearbox Oil Pressure Low | Pressure Switch | Fan Drive Units FN-51A / 2-FN-51A [11-D / 8-D] | Low lube oil pressure alarm |
| **PSL-8288 (x2)** | Fan Gearbox Oil Pressure Low | Pressure Switch | Fan Drive Units FN-51B / 2-FN-51B [10-D / 9-D] | Low lube oil pressure alarm |
| **LT-6139 (x2)** | Fan Gearbox Oil Level Transmitter | Level | Fan Drive Sump FN-51A / FN-51B [9-D / 8-D] | Oil level indication |
| **LG-6116A / B** | Fan Gearbox Sight Glass | Level Gauge | Fan Gearbox FN-51A / FN-51B Details B & C | Local oil level sight glass |
| **RO-6104..6108** | SW Pump Recirc Orifices | Minimum Flow | Pumps P-41A, P-41C, P-41B, P-41D [7-H..7-F] | Continuous minimum flow / air release |
| **PDIS 8259** | Train A SW Strainer Differential Pressure | Differential Press | Across Strainer S-11 [11-C] | High DP alarm / backwash initiation |
| **PDIS 8258** | Train B SW Strainer Differential Pressure | Differential Press | Across Strainer S-10 [11-B] | High DP alarm / backwash initiation |
| **TE 6105 / PSL 6103** | CCW HX A SW Discharge Temp & Press | Temp / Press | CC-E-17A SW Outlet Line [8-E / 8-D] | Low pressure alarm / temp monitor |
| **TE 6115 / PSL 6113** | CCW HX B SW Discharge Temp & Press | Temp / Press | CC-E-17B SW Outlet Line [8-D] | Low pressure alarm / temp monitor |
| **TI 6180 / FI 6181 / FE 6181** | DG-E-42A Cooling Water Temp & Flow | Temp / Flow | DG-E-42A SW Discharge Line [7-B] | Local temp / flow indication |
| **TI 6190 / FI 6191 / FE 6191** | DG-E-42B Cooling Water Temp & Flow | Temp / Flow | DG-E-42B SW Discharge Line [7-C] | Local temp / flow indication |
| **FE 6150 / FI 6150** | Train B Main SW Header Flow | Flow | Train B Main 24" SW Header [10-A] | Primary Train B SW supply flow |
| **FE 6151 / FI 6151** | Train B SW Header Flow | Flow | Train B Main SW Header [8-A] | SW flow indication |
| **LSH 8268** | SW Return Overflow Level Switch | Level Switch | SW Return Overflow Line [6-E] | High level alarm |
| **PDIS 6157** | Secondary CCW HX A Differential Pressure | Differential Press | Across SCC-E-29A [8-F] | High DP fouling alarm |
| **PDIS 6146** | Secondary CCW HX B Differential Pressure | Differential Press | Across SCC-E-29B [8-G] | High DP fouling alarm |
| **PDI-5731** | Cooling Tower Air Intake Filter DP | Differential Press | Across Filter SWA-F-192 [4-E] | Filter loading indication |
| **FISL 8298** | SF-E-15C SW Return Flow Indicating Switch | Flow Switch Low | SF-E-15C SW Outlet Line [5-D] | Low cooling flow interlock / alarm |
| **TW 8296 / TW 8297** | SF-E-15C SW Supply & Return Thermowells | Temperature | SF-E-15C SW Supply & Return Lines [6-F / 5-D] | Local temperature measurement |
| **RE-6510..RE-6513** | S/G A..D Sample Stream Radiation Detectors | Gross Gamma Rad | Skid RM-SKD-83..86 [4-H..4-E] | In-line detector for SG tube leak detection |
| **FS-6510..FS-6513** | S/G A..D Radiation Monitor Flow Switches | Sample Flow | Skid RM-SKD-83..86 Discharges [4-H..4-E] | Confirms adequate sample flow through detector |
| **pH AE-2864..2867**| S/G A..D pH Sensor Elements | Chemical (pH) | Panel CP-166B Sample Branches [8-G..8-B] | Continuous S/G blowdown pH monitoring |
| **CE-2806-1..2809-2**| S/G A..D Cation Conductivity Cells | Conductivity | Panel CP-166B Sample Branches [8-G..8-B] | Dual cation conductivity measurement |
| **CE-2784 / FISL-2784**| SACC Column Conductivity & Flow Switch | Conductivity / Flow| SACC Analysis Loop [6-A] | Strong acid cation conductivity monitoring |
| **TI-2784 / TSH-2784**| SACC Column Temp Indicator & High Switch | Temperature | Effluent of Heater H-376 [6-A] | High temp cutout for resin protection |

## Extracted Entities & Cross-References

* **Grounded Equipment Concepts:**
  * `equipment/P-41A` — Service Water Pump 41A (Train A, Ocean Intake)
  * `equipment/P-41B` — Service Water Pump 41B (Train B, Ocean Intake)
  * `equipment/P-41C` — Service Water Pump 41C (Train A, Ocean Intake)
  * `equipment/P-41D` — Service Water Pump 41D (Train B, Ocean Intake)
  * `equipment/P-110A` — Cooling Tower Service Water Pump 110A
  * `equipment/P-110B` — Cooling Tower Service Water Pump 110B
  * `equipment/FN-51A` — Cooling Tower Fan 51A (Unit 1)
  * `equipment/FN-51B` — Cooling Tower Fan 51B (Unit 1)
  * `equipment/S-10` — Service Water Strainer B
  * `equipment/S-11` — Service Water Strainer A
  * `equipment/CC-E-17A` — Primary Component Cooling Water Heat Exchanger A
  * `equipment/CC-E-17B` — Primary Component Cooling Water Heat Exchanger B
  * `equipment/DG-E-42A` — Emergency Diesel Generator 1A Water Jacket Heat Exchanger
  * `equipment/DG-E-42B` — Emergency Diesel Generator 1B Water Jacket Heat Exchanger
  * `equipment/SCC-E-29A` — Secondary Component Cooling Water Heat Exchanger A
  * `equipment/SCC-E-29B` — Secondary Component Cooling Water Heat Exchanger B
  * `equipment/SF-E-15C` — Spent Fuel Pool Heat Exchanger C (Safety Class 3, Abandoned / Isolated)
  * `equipment/1-SS-E-14A` — Steam Generator 1 Primary Sample Heat Exchanger
  * `equipment/1-SS-E-14B` — Steam Generator 2 Primary Sample Heat Exchanger
  * `equipment/1-SS-E-14C` — Steam Generator 3 Primary Sample Heat Exchanger
  * `equipment/1-SS-E-14D` — Steam Generator 4 Primary Sample Heat Exchanger
  * `equipment/SWA-FN-40A` — Service Water Pumphouse Supply Fan 40A
  * `equipment/SWA-FN-40B` — Service Water Pumphouse Supply Fan 40B

## References & Sources
[^src-1]: ML101620329-part-3.pdf (reference/raw/pid/ML101620329-part-3.pdf)
