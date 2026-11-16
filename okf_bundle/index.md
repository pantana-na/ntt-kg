# Subdirectories

* [equipment](equipment/index.md) - Index of equipment
* [hazop](hazop/index.md) - Index of hazop
* [instruments](instruments/index.md) - Index of instruments
* [procedures](procedures/index.md) - Index of procedures
* [sources](sources/index.md) - Index of sources
* [standards](standards/index.md) - Index of standards
* [units](units/index.md) - Index of units

---

# Master Plant Knowledge Catalog (OKF v0.2)

## 1. Plant Unit Architecture & Scope
- **[Unit Overview: Seabrook Station Safety Injection System (SI)](units/seabrook-safety-injection-system.md)**: Emergency Core Cooling System architecture, multi-tier injection regimes (High, Intermediate, and Low Head), equipment roster, and contai...
- **[Unit Overview: Seabrook Station Service Water System (SW & SWA)](units/seabrook-service-water-system.md)**: Nuclear safety-related Service Water System (SW) and Air Handling System (SWA) for Seabrook Station, providing ultimate heat sink cooling...
- **[Unit Overview: Seabrook Station Spent Fuel Pool Cooling and Cleanup System (SF)](units/seabrook-spent-fuel-pool-cleanup.md)**: System topology, major equipment roster, process flow, and boundary interfaces of the Seabrook Station Spent Fuel Pool Cooling and Cleanu...
- **[Unit Overview: Seabrook Station Steam Generator Sample System (SS Panel CP-166B)](units/seabrook-steam-generator-sample-system.md)**: Overview of the Seabrook Station Steam Generator Sample System (Panel CP-166B) covering primary sample coolers E-14A..D, chiller skid SKD...

## 2. Master Equipment Specifications & P&ID Loop Matrix

| Tag | Equipment Title | Unit | Class | P&ID Loops | Engineering Function Summary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [1-SS-E-14A](equipment/1-SS-E-14A.md) | 1-SS-E-14A — Steam Generator 1 Primary Sample Heat Exchanger | SS | Heat Exchanger | 2 loops | Primary sample cooler for Steam Generator 1 blowdown sample stream, cooling high-temperature, high-pressure blowdown water against Compon... |
| [1-SS-E-14B](equipment/1-SS-E-14B.md) | 1-SS-E-14B — Steam Generator 2 Primary Sample Heat Exchanger | SS | Heat Exchanger | 2 loops | Primary sample cooler for Steam Generator 2 blowdown sample stream, cooling high-temperature blowdown water against CCW Loop A prior to s... |
| [1-SS-E-14C](equipment/1-SS-E-14C.md) | 1-SS-E-14C — Steam Generator 3 Primary Sample Heat Exchanger | SS | Heat Exchanger | 2 loops | Primary sample cooler for Steam Generator 3 blowdown sample stream, cooling high-temperature blowdown water against CCW Loop A prior to s... |
| [1-SS-E-14D](equipment/1-SS-E-14D.md) | 1-SS-E-14D — Steam Generator 4 Primary Sample Heat Exchanger | SS | Heat Exchanger | 2 loops | Primary sample cooler for Steam Generator 4 blowdown sample stream, cooling high-temperature blowdown water against CCW Loop A prior to s... |
| [CBS-EP-36A](equipment/CBS-EP-36A.md) | CBS-EP-36A — Expansion Bellows / Piece A | SI / CBS | Expansion Joint | 1 loops | Safety Class 2 16" flexible expansion bellows installed on the Containment Recirculation Sump A suction line inside Protective Chamber CB... |
| [CBS-EP-36B](equipment/CBS-EP-36B.md) | CBS-EP-36B — Expansion Bellows / Piece B | SI / CBS | Expansion Joint | 1 loops | Safety Class 2 16" flexible expansion bellows installed on the Containment Recirculation Sump B suction line inside Protective Chamber CB... |
| [CBS-TK-101A](equipment/CBS-TK-101A.md) | CBS-TK-101A — Protective Chamber A (Sump A Guard Pipe Enclosure) | SI / CBS | Vessel | 1 loops | Safety Class 2 sealed protective chamber enclosing the containment recirculation sump A suction line, expansion bellows CBS-EP-36A, and m... |
| [CBS-TK-101B](equipment/CBS-TK-101B.md) | CBS-TK-101B — Protective Chamber B (Sump B Guard Pipe Enclosure) | SI / CBS | Vessel | 1 loops | Safety Class 2 sealed protective chamber enclosing the containment recirculation sump B suction line, expansion bellows CBS-EP-36B, and m... |
| [CBS-TK-10A](equipment/CBS-TK-10A.md) | CBS-TK-10A — Containment Recirculation Sump A | SI / CBS | Sump / Vessel | 4 loops | Containment Recirculation Sump A providing a qualified suction reservoir for emergency core cooling and containment spray systems during ... |
| [CBS-TK-10B](equipment/CBS-TK-10B.md) | CBS-TK-10B — Containment Recirculation Sump B | SI / CBS | Sump / Vessel | 3 loops | Containment Recirculation Sump B providing a redundant, qualified suction reservoir for emergency core cooling and containment spray syst... |
| [CC-E-17A](equipment/CC-E-17A.md) | CC-E-17A — Primary Component Cooling Water Heat Exchanger A | CC | Heat Exchanger | 4 loops | Primary nuclear safety-related component cooling water heat exchanger for Train A, transferring heat from the closed-loop Primary Compone... |
| [CC-E-17B](equipment/CC-E-17B.md) | CC-E-17B — Primary Component Cooling Water Heat Exchanger B | CC | Heat Exchanger | 4 loops | Primary nuclear safety-related component cooling water heat exchanger for Train B, transferring heat from the closed-loop Primary Compone... |
| [CS-P-243A](equipment/CS-P-243A.md) | CS-P-243A — Charging Pump CS-P-2A Lube Oil Pump | CS | Pump | 5 loops | Auxiliary positive displacement lubrication oil pump for Charging / High Head Safety Injection Pump CS-P-2A, circulating lube oil from oi... |
| [CS-P-243B](equipment/CS-P-243B.md) | CS-P-243B — Charging Pump CS-P-2B Lube Oil Pump | CS | Pump | 5 loops | Auxiliary positive displacement lubrication oil pump for Charging / High Head Safety Injection Pump CS-P-2B, circulating lube oil from oi... |
| [CS-P-2A](equipment/CS-P-2A.md) | CS-P-2A — Charging Pump (High Head Safety Injection) | CS / SI | Pump | 10 loops | High Head Safety Injection / Charging Pump A supplying normal CVCS reactor coolant makeup, pressurizer level control, reactor coolant pum... |
| [CS-P-2B](equipment/CS-P-2B.md) | CS-P-2B — Charging Pump (High Head Safety Injection) | CS / SI | Pump | 8 loops | High Head Safety Injection / Charging Pump B supplying redundant normal CVCS reactor coolant makeup, pressurizer level control, reactor c... |
| [DG-E-42A](equipment/DG-E-42A.md) | DG-E-42A — Diesel Generator 1A Water Jacket Heat Exchanger | DG | Heat Exchanger | 4 loops | Nuclear safety-related water jacket heat exchanger for Emergency Diesel Generator 1A (Train A), cooled by Service Water Train B, providin... |
| [DG-E-42B](equipment/DG-E-42B.md) | DG-E-42B — Diesel Generator 1B Water Jacket Heat Exchanger | DG | Heat Exchanger | 3 loops | Nuclear safety-related water jacket heat exchanger for Emergency Diesel Generator 1B (Train B), cooled by Service Water Train A, providin... |
| [DM-8](equipment/DM-8.md) | DM-8 — Fuel Pool Demineralizer | SF | Demineralizer / Ion Exchanger | 2 loops | Fuel Pool Demineralizer providing deep-bed ion-exchange purification of spent fuel pool water and cavity cleanup streams, removing solubl... |
| [F-207](equipment/F-207.md) | F-207 — Reactor Cavity Cleanup Filter | SF | Filter | 1 loops | Reactor Cavity Cleanup Filter providing particulate and crud filtration for the Refueling Pool & Canal water inside primary containment d... |
| [F-33](equipment/F-33.md) | F-33 — Fuel Pool Prefilter | SF | Filter | 2 loops | Fuel Pool Prefilter removing particulates and suspended solids from spent fuel pool water and cavity cleanup flows prior to entry into io... |
| [F-34](equipment/F-34.md) | F-34 — Fuel Pool Postfilter | SF | Filter | 2 loops | Fuel Pool Postfilter installed downstream of Demineralizer DM-8 to capture resin fines, particulates, and resin fragments, preventing rad... |
| [FN-40A](equipment/FN-40A.md) | FN-40A — Service Water Pumphouse Supply Fan 40A | SWA | Fan | 4 loops | Nuclear safety-related ventilation supply fan for the Service Water Pumphouse (Train A), delivering 3,400 CFM of filtered outside air to ... |
| [FN-40B](equipment/FN-40B.md) | FN-40B — Service Water Pumphouse Supply Fan 40B | SWA | Fan | 4 loops | Nuclear safety-related ventilation supply fan for the Service Water Pumphouse (Train B), delivering 3,400 CFM of filtered outside air to ... |
| [FN-51A](equipment/FN-51A.md) | FN-51A — Service Water Cooling Tower Fan 51A | SW | Fan | 4 loops | Induced-draft nuclear safety-related cooling tower fan for Service Water Cooling Tower Cell A, drawing air through the spray nozzle fill ... |
| [FN-51B](equipment/FN-51B.md) | FN-51B — Service Water Cooling Tower Fan 51B | SW | Fan | 3 loops | Induced-draft nuclear safety-related cooling tower fan for Service Water Cooling Tower Cell B, drawing air through the spray nozzle fill ... |
| [P-110A](equipment/P-110A.md) | P-110A — Cooling Tower Service Water Pump 110A (Train A) | SW | Pump | 4 loops | Safety-related Ultimate Heat Sink (UHS) cooling tower service water pump for Train A, taking suction from the Service Water Cooling Tower... |
| [P-110B](equipment/P-110B.md) | P-110B — Cooling Tower Service Water Pump 110B (Train B) | SW | Pump | 4 loops | Safety-related Ultimate Heat Sink (UHS) cooling tower service water pump for Train B, taking suction from the Service Water Cooling Tower... |
| [P-12](equipment/P-12.md) | P-12 — Spent Fuel Pool Skimmer Pump | SF | Pump | 1 loops | Spent Fuel Pool Skimmer Pump taking suction from surface skimmers S-2A through S-2E and pool headers, circulating surface pool water thro... |
| [P-272](equipment/P-272.md) | P-272 — Refueling Canal Skimmer Pump | SF | Pump | 1 loops | Refueling Canal Skimmer Pump taking suction from refueling pool surface skimmers S-245A..E and bottom floor drains (via Reactor Cavity Cl... |
| [P-41A](equipment/P-41A.md) | P-41A — Service Water Pump 41A (Ocean Intake Train A) | SW | Pump | 4 loops | Primary nuclear safety-related ocean intake service water pump for Train A, taking suction from the Service Water Pumphouse forebay well ... |
| [P-41B](equipment/P-41B.md) | P-41B — Service Water Pump 41B (Ocean Intake Train B) | SW | Pump | 2 loops | Primary nuclear safety-related ocean intake service water pump for Train B, taking suction from the Service Water Pumphouse forebay well ... |
| [P-41C](equipment/P-41C.md) | P-41C — Service Water Pump 41C (Ocean Intake Train A) | SW | Pump | 3 loops | Primary nuclear safety-related ocean intake service water pump for Train A (parallel with P-41A), taking suction from the Service Water P... |
| [P-41D](equipment/P-41D.md) | P-41D — Service Water Pump 41D (Ocean Intake Train B) | SW | Pump | 1 loops | Primary nuclear safety-related ocean intake service water pump for Train B (parallel with P-41B), taking suction from the Service Water P... |
| [RH-E-9A](equipment/RH-E-9A.md) | RH-E-9A — RHR Loop A Heat Exchanger | RH / SI | Heat Exchanger | 8 loops | Residual Heat Removal Loop A Heat Exchanger cooling circulating reactor coolant during normal plant shutdown / cooldown and cooling emerg... |
| [RH-E-9B](equipment/RH-E-9B.md) | RH-E-9B — RHR Loop B Heat Exchanger | RH / SI | Heat Exchanger | 7 loops | Residual Heat Removal Loop B Heat Exchanger cooling circulating reactor coolant during normal plant shutdown / cooldown and cooling emerg... |
| [RH-P-8A](equipment/RH-P-8A.md) | RH-P-8A — Residual Heat Removal Pump A | RH / SI | Pump | 11 loops | Residual Heat Removal (RHR) Pump A providing dual-function service: normal shutdown decay heat removal by drawing reactor coolant from RC... |
| [RH-P-8B](equipment/RH-P-8B.md) | RH-P-8B — Residual Heat Removal Pump B | RH / SI | Pump | 11 loops | Residual Heat Removal (RHR) Pump B providing redundant shutdown decay heat removal by drawing reactor coolant from RCS Loop 4 Hot Leg thr... |
| [S-10](equipment/S-10.md) | S-10 — Service Water Strainer S-10 (Train B) | SW | Filter | 4 loops | Nuclear safety-related automatic in-line basket strainer for Service Water Train B, located in the Primary Auxiliary Building (PAB), remo... |
| [S-11](equipment/S-11.md) | S-11 — Service Water Strainer S-11 (Train A) | SW | Filter | 3 loops | Nuclear safety-related automatic in-line basket strainer for Service Water Train A, located in the Primary Auxiliary Building (PAB), remo... |
| [SCC-E-29A](equipment/SCC-E-29A.md) | SCC-E-29A — Secondary Component Cooling Water Heat Exchanger A | SCC | Heat Exchanger | 2 loops | Secondary component cooling water heat exchanger for Train A, located in the Turbine Building, cooled by Nuclear Service Water to remove ... |
| [SCC-E-29B](equipment/SCC-E-29B.md) | SCC-E-29B — Secondary Component Cooling Water Heat Exchanger B | SCC | Heat Exchanger | 2 loops | Secondary component cooling water heat exchanger for Train B, located in the Turbine Building, cooled by Nuclear Service Water to remove ... |
| [SF-E-15C](equipment/SF-E-15C.md) | SF-E-15C — Spent Fuel Pool Heat Exchanger C (Safety Class 3, Abandoned / Isolated) | SF | Heat Exchanger | 3 loops | Third Spent Fuel Pool cooling heat exchanger (Safety Class 3) originally installed for Alternate Spent Fuel Pool Cooling (ASFPC). Under L... |
| [SI-P-6A](equipment/SI-P-6A.md) | SI-P-6A — Safety Injection Pump A (Intermediate Head) | SI | Pump | 8 loops | Intermediate Head Safety Injection Pump A providing high-pressure emergency core cooling water from the Refueling Water Storage Tank (RWS... |
| [SI-P-6B](equipment/SI-P-6B.md) | SI-P-6B — Safety Injection Pump B (Intermediate Head) | SI | Pump | 6 loops | Intermediate Head Safety Injection Pump B providing redundant high-pressure emergency core cooling water from the Refueling Water Storage... |
| [SI-TK-9A](equipment/SI-TK-9A.md) | SI-TK-9A — Safety Injection Accumulator Tank A | SI | Vessel | 6 loops | Safety Injection Accumulator Tank A providing rapid, passive injection of borated water into Reactor Coolant System (RCS) Loop 1 Cold Leg... |
| [SI-TK-9B](equipment/SI-TK-9B.md) | SI-TK-9B — Safety Injection Accumulator Tank B | SI | Vessel | 6 loops | Safety Injection Accumulator Tank B providing rapid, passive injection of borated water into Reactor Coolant System (RCS) Loop 2 Cold Leg... |
| [SI-TK-9C](equipment/SI-TK-9C.md) | SI-TK-9C — Safety Injection Accumulator Tank C | SI | Vessel | 6 loops | Safety Injection Accumulator Tank C providing rapid, passive injection of borated water into Reactor Coolant System (RCS) Loop 3 Cold Leg... |
| [SI-TK-9D](equipment/SI-TK-9D.md) | SI-TK-9D — Safety Injection Accumulator Tank D | SI | Vessel | 6 loops | Safety Injection Accumulator Tank D providing rapid, passive injection of borated water into Reactor Coolant System (RCS) Loop 4 Cold Leg... |
| [SS-CP-166A](equipment/SS-CP-166A.md) | SS-CP-166A — Primary Sample Panel CP-166A & Sink MM-13B | SS | Panel / Skid | 6 loops | Nuclear Primary Sample Panel CP-166A and Sink MM-13B enclosure housing sample pressure reduction, analytical instrumentation, dissolved g... |
| [SS-CP-419](equipment/SS-CP-419.md) | SS-CP-419 — Post Accident Sample Panel CP-419 | SS | Panel / Skid | 2 loops | Post Accident Sample Panel CP-419 enclosure structure located within the shielded PASS panel cubicle in the Primary Auxiliary Building. H... |
| [SS-E-106](equipment/SS-E-106.md) | SS-E-106 — Post Accident Sample System Heat Exchanger | SS | Heat Exchanger | 1 loops | Post Accident Sample System (PASS) heat exchanger designed to rapidly cool highly radioactive post-accident reactor coolant fluid drawn f... |
| [SS-E-12A](equipment/SS-E-12A.md) | SS-E-12A — Pressurizer Liquid & Steam Sample Heat Exchanger A | SS | Heat Exchanger | 1 loops | Primary Nuclear Sample System heat exchanger cooling high-temperature, high-pressure borated reactor coolant from the Pressurizer steam o... |
| [SS-E-12B](equipment/SS-E-12B.md) | SS-E-12B — Pressurizer Liquid & Steam Sample Heat Exchanger B | SS | Heat Exchanger | 0 loops | Second-stage nuclear sample heat exchanger arranged in series with SS-E-12A to cool pressurizer steam and liquid sample streams down to s... |
| [SS-E-13A](equipment/SS-E-13A.md) | SS-E-13A — RC Loop 1 & 3 Liquid Sample Heat Exchanger A | SS | Heat Exchanger | 1 loops | Primary Nuclear Sample System heat exchanger cooling high-pressure, high-temperature borated liquid drawn from Reactor Coolant System Loo... |
| [SS-E-13B](equipment/SS-E-13B.md) | SS-E-13B — RC Loop 1 & 3 Liquid Sample Heat Exchanger B | SS | Heat Exchanger | 1 loops | Second-stage nuclear sample heat exchanger arranged in series with SS-E-13A to cool reactor coolant liquid from loops 1 and 3 down to saf... |
| [SS-P-392](equipment/SS-P-392.md) | SS-P-392 — Primary Sample Sink Vacuum Pump | SS | Pump | 3 loops | Auxiliary vacuum pump providing vacuum evacuation for sample containers, flexible hoses, and Primary Sample Sink MM-13B analytical appara... |
| [SS-T-312](equipment/SS-T-312.md) | SS-T-312 — Post Accident Liquid Drainer | SS | Vessel | 0 loops | Post Accident Liquid Drainer T-312 acting as an in-line moisture and liquid knockout separator on the Flush Tank TK-197 off-gas vent line... |
| [SS-TK-197](equipment/SS-TK-197.md) | SS-TK-197 — Post Accident Flush Tank | SS | Vessel | 2 loops | Post Accident Sample System Flush Tank accumulating radioactive demineralized flush water and residual coolant drainage from the PASS sam... |
| [SS-TK-228A](equipment/SS-TK-228A.md) | SS-TK-228A — Post Accident Sample Cask A | SS | Vessel | 0 loops | Heavily shielded Post Accident Sample Cask designed to safely obtain, contain, and transport highly radioactive grab samples of post-LOCA... |
| [SS-TK-228B](equipment/SS-TK-228B.md) | SS-TK-228B — Post Accident Sample Cask B | SS | Vessel | 0 loops | Redundant heavily shielded Post Accident Sample Cask designed to obtain, contain, and transport highly radioactive grab samples of post-L... |

## 4. Instrumentation, Safety Interlocks (SIS) & Overpressure Protection Register

| Subsystem Register | Canonical Path | Scope & Safety Interlock Summary |
| :--- | :--- | :--- |
| [FIS-610 — RHR Loop A Suction Flow Indicating Switch & Bypass Interlock](instruments/fis-610.md) | `instruments/fis-610.md` | Flow Indicating Switch across FE-610 on RHR Loop A suction header providing flow alarm and Interlock G control to Heat Exchanger bypass v... |
| [FIS-611 — RHR Loop B Suction Flow Indicating Switch & Bypass Interlock](instruments/fis-611.md) | `instruments/fis-611.md` | Flow Indicating Switch across FE-611 on RHR Loop B suction header providing flow alarm and Interlock H control to Heat Exchanger bypass v... |
| [FIS-7325 — Charging Pump CS-P-2A Miniflow Interlock Flow Indicating Switch](instruments/fis-7325.md) | `instruments/fis-7325.md` | Flow Indicating Switch across FE-7325 on Charging Pump CS-P-2A discharge controlling automatic opening of miniflow recirculation valve CS... |
| [FIS-7326 — Charging Pump CS-P-2B Miniflow Interlock Flow Indicating Switch](instruments/fis-7326.md) | `instruments/fis-7326.md` | Flow Indicating Switch across FE-7326 on Charging Pump CS-P-2B discharge controlling automatic opening of miniflow recirculation valve CS... |
| [FISL-2626 — Spent Fuel Pool Cleanup Return Header Flow Indicating Switch Low](instruments/fisl-2626.md) | `instruments/fisl-2626.md` | Flow Indicating Switch Low monitoring cleanup recirculation flow downstream of postfilter F-34 returning to the Spent Fuel Pool on P&ID P... |
| [FT-6163 — Cooling Tower Pump P-110A Discharge Flow Transmitter](instruments/ft-6163.md) | `instruments/ft-6163.md` | Nuclear safety-related discharge flow transmitter for Service Water Cooling Tower Pump P-110A (Train A). |
| [FT-917 — High Head Safety Injection / Charging Main Header Flow Transmitter](instruments/ft-917.md) | `instruments/ft-917.md` | Flow Transmitter across FE-917 measuring total High Head Safety Injection flow delivered through 4" header and penetration X-24 to the RC... |
| [FT-918 — Intermediate Head Safety Injection Pump A Discharge Flow Transmitter](instruments/ft-918.md) | `instruments/ft-918.md` | Safety Class 2 flow transmitter and orifice monitoring discharge flow of Intermediate Head Safety Injection Pump SI-P-6A on P&ID PID-1-SI... |
| [FT-922 — Intermediate Head Safety Injection Pump B Discharge Flow Transmitter](instruments/ft-922.md) | `instruments/ft-922.md` | Safety Class 2 flow transmitter and orifice monitoring discharge flow of Intermediate Head Safety Injection Pump SI-P-6B on P&ID PID-1-SI... |
| [LE-2384-1 / LE-2384-2 — Containment Recirculation Sump A Water Level Elements](instruments/le-2384-1.md) | `instruments/le-2384-1.md` | Safety Class 2 redundant level elements monitoring Containment Recirculation Sump A water level and providing recirculation switchover in... |
| [LE-2385-1 / LE-2385-2 — Containment Recirculation Sump B Water Level Elements](instruments/le-2385-1.md) | `instruments/le-2385-1.md` | Safety Class 2 redundant level elements monitoring Containment Recirculation Sump B water level and providing recirculation switchover in... |
| [LS-2356 — Protective Chamber A Leak Detection Level Switch](instruments/ls-2356.md) | `instruments/ls-2356.md` | Nuclear Safety Related Level Switch monitoring liquid accumulation and boundary leakage inside Protective Chamber CBS-TK-101A outside con... |
| [LS-2357 — Protective Chamber B Leak Detection Level Switch](instruments/ls-2357.md) | `instruments/ls-2357.md` | Nuclear Safety Related Level Switch monitoring liquid accumulation and boundary leakage inside Protective Chamber CBS-TK-101B outside con... |
| [LT-2629 — Refueling Cavity Water Level Transmitter](instruments/lt-2629.md) | `instruments/lt-2629.md` | Electronic level transmitter and element monitoring Refueling Pool and Canal water level on P&ID PID-1-SF-LR20484. |
| [PDI-2682 — Reactor Cavity Cleanup Filter Differential Pressure Indicator](instruments/pdi-2682.md) | `instruments/pdi-2682.md` | Differential Pressure Indicator across Reactor Cavity Cleanup Filter F-207 inside containment monitoring filter cartridge loading during ... |
| [PDIS-2622 — Fuel Pool Prefilter Differential Pressure Indicator & Switch](instruments/pdis-2622.md) | `instruments/pdis-2622.md` | Differential Pressure Indicator and High Alarm Switch across Fuel Pool Prefilter F-33 monitoring filter element particulate loading and c... |
| [PDIS-2623 — Fuel Pool Postfilter Differential Pressure Indicator & Switch](instruments/pdis-2623.md) | `instruments/pdis-2623.md` | Differential Pressure Indicator and High Alarm Switch across Fuel Pool Postfilter F-34 monitoring resin fines capture and element loading. |
| [PDIS-2624 — Fuel Pool Demineralizer Differential Pressure Indicator & Switch](instruments/pdis-2624.md) | `instruments/pdis-2624.md` | Differential Pressure Indicator and High Alarm Switch across Fuel Pool Demineralizer DM-8 monitoring resin bed compaction and underdrain ... |
| [PDIS-8258 — Service Water Strainer S-10 Differential Pressure Indicating Switch](instruments/pdis-8258.md) | `instruments/pdis-8258.md` | Nuclear safety-related differential pressure indicating switch across automatic service water strainer S-10 (Train B) providing high DP a... |
| [PDIS-8259 — Service Water Strainer S-11 Differential Pressure Indicating Switch](instruments/pdis-8259.md) | `instruments/pdis-8259.md` | Nuclear safety-related differential pressure indicating switch across automatic service water strainer S-11 (Train A) providing high DP a... |
| [PISL-2621 — Spent Fuel Pool Skimmer Pump Suction Pressure Indicator & Switch Low](instruments/pisl-2621.md) | `instruments/pisl-2621.md` | Pressure Indicator and Low Switch on the 4" suction header of Spent Fuel Pool Skimmer Pump P-12 providing cavitation protection and low-p... |
| [PT-614 — RHR Loop A Suction Header Pressure Transmitter](instruments/pt-614.md) | `instruments/pt-614.md` | Safety Class 2 pressure transmitter monitoring suction header pressure of Residual Heat Removal Pump RH-P-8A on P&ID PID-1-SI-LR20448. |
| [PT-615 — RHR Loop B Suction Header Pressure Transmitter](instruments/pt-615.md) | `instruments/pt-615.md` | Safety Class 2 pressure transmitter monitoring suction header pressure of Residual Heat Removal Pump RH-P-8B on P&ID PID-1-SI-LR20448. |
| [RE-6510 — Steam Generator 1 Blowdown Sample Radiation Monitor](instruments/re-6510.md) | `instruments/re-6510.md` | In-line gross gamma radiation detector on Skid RM-SKD-83 monitoring Steam Generator 1 blowdown sample stream for primary-to-secondary tub... |

## 5. Cross-Document Engineering Discrepancies & Safety Warnings (`⚠️ CONFLICT`)

- **[RH-E-9A — RHR Loop A Heat Exchanger](equipment/RH-E-9A.md)**: - ⚠️ CONFLICT — Drawing Number: PID-1-SI-LR20448 specifies PID-1-SI-LR20448, whereas PID-1-SI-LR20449 specifies PID-1-SI-LR20449 (Rev. 0, Ref. B20449 Rev. 9) — verify with engineer before HAZOP
- **[RH-E-9B — RHR Loop B Heat Exchanger](equipment/RH-E-9B.md)**: - ⚠️ CONFLICT — Drawing Number: PID-1-SI-LR20448 specifies PID-1-SI-LR20448, whereas PID-1-SI-LR20449 specifies PID-1-SI-LR20449 (Rev. 0, Ref. B20449 Rev. 9) — verify with engineer before HAZOP
- **[HAZOP Guide Words, Deviation Analysis, and Recording Template](hazop/guide-words-and-deviations.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[Qualitative Risk Assessment Matrix (RAM) for HAZOP and PHA](hazop/risk-assessment-matrix.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[FIS-610 — RHR Loop A Suction Flow Indicating Switch & Bypass Interlock](instruments/fis-610.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[FIS-611 — RHR Loop B Suction Flow Indicating Switch & Bypass Interlock](instruments/fis-611.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[FIS-7325 — Charging Pump CS-P-2A Miniflow Interlock Flow Indicating Switch](instruments/fis-7325.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[FIS-7326 — Charging Pump CS-P-2B Miniflow Interlock Flow Indicating Switch](instruments/fis-7326.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[FISL-2626 — Spent Fuel Pool Cleanup Return Header Flow Indicating Switch Low](instruments/fisl-2626.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[FT-6163 — Cooling Tower Pump P-110A Discharge Flow Transmitter](instruments/ft-6163.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[FT-917 — High Head Safety Injection / Charging Main Header Flow Transmitter](instruments/ft-917.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[FT-918 — Intermediate Head Safety Injection Pump A Discharge Flow Transmitter](instruments/ft-918.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[FT-922 — Intermediate Head Safety Injection Pump B Discharge Flow Transmitter](instruments/ft-922.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[LE-2384-1 / LE-2384-2 — Containment Recirculation Sump A Water Level Elements](instruments/le-2384-1.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[LE-2385-1 / LE-2385-2 — Containment Recirculation Sump B Water Level Elements](instruments/le-2385-1.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[LS-2356 — Protective Chamber A Leak Detection Level Switch](instruments/ls-2356.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[LS-2357 — Protective Chamber B Leak Detection Level Switch](instruments/ls-2357.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[LT-2629 — Refueling Cavity Water Level Transmitter](instruments/lt-2629.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[PDI-2682 — Reactor Cavity Cleanup Filter Differential Pressure Indicator](instruments/pdi-2682.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[PDIS-2622 — Fuel Pool Prefilter Differential Pressure Indicator & Switch](instruments/pdis-2622.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[PDIS-2623 — Fuel Pool Postfilter Differential Pressure Indicator & Switch](instruments/pdis-2623.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[PDIS-2624 — Fuel Pool Demineralizer Differential Pressure Indicator & Switch](instruments/pdis-2624.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[PDIS-8258 — Service Water Strainer S-10 Differential Pressure Indicating Switch](instruments/pdis-8258.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[PDIS-8259 — Service Water Strainer S-11 Differential Pressure Indicating Switch](instruments/pdis-8259.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[PISL-2621 — Spent Fuel Pool Skimmer Pump Suction Pressure Indicator & Switch Low](instruments/pisl-2621.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[PT-614 — RHR Loop A Suction Header Pressure Transmitter](instruments/pt-614.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[PT-615 — RHR Loop B Suction Header Pressure Transmitter](instruments/pt-615.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[RE-6510 — Steam Generator 1 Blowdown Sample Radiation Monitor](instruments/re-6510.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[Hazard Assessment and Mitigation Workflow Procedure](procedures/hazard-assessment-and-mitigation.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[HAZOP Study Execution and Documentation Lifecycle Procedure](procedures/hazop-execution-workflow.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[Hazard and Operability Analysis (HAZOP) Methodology Standard](standards/hazop-methodology.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[Risk Assessment Matrix (RAM) and Risk Assessment Code (RAC) Standard](standards/ram-methodology.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[Unit Overview: Seabrook Station Safety Injection System (SI)](units/seabrook-safety-injection-system.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[Unit Overview: Seabrook Station Service Water System (SW & SWA)](units/seabrook-service-water-system.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[Unit Overview: Seabrook Station Spent Fuel Pool Cooling and Cleanup System (SF)](units/seabrook-spent-fuel-pool-cleanup.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
- **[Unit Overview: Seabrook Station Steam Generator Sample System (SS Panel CP-166B)](units/seabrook-steam-generator-sample-system.md)**: ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**

