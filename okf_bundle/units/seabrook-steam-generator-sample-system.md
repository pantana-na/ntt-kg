---
type: Unit Overview
title: 'Unit Overview: Seabrook Station Steam Generator Sample System (SS Panel CP-166B)'
description: Overview of the Seabrook Station Steam Generator Sample System (Panel
  CP-166B) covering primary sample coolers E-14A..D, chiller skid SKD-128, and radiation
  monitor skids RM-SKD-83..86.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/units/seabrook-steam-generator-sample-system.md
tags:
- chemical-analysis
- license-renewal
- p-and-id
- radiation-monitoring
- sample-system
- seabrook-station
- steam-generator
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-3.pdf
  title: ML101620329-part-3.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-11-05T14:36:23Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-11-05T14:36:23Z'
- by: process:okf-validation-suite
  at: '2026-11-05T14:36:23Z'
status: stable
entity_metadata:
  pids:
  - PID-1-SS-LR20521
  sample_coolers:
  - 1-SS-E-14A
  - 1-SS-E-14B
  - 1-SS-E-14C
  - 1-SS-E-14D
  unit: Seabrook Station Unit 1
  system_prefix: SS
  primary_fluids:
  - Steam Generator Blowdown
  - Component Cooling Water Loop A
  - Chilled Coolant
---

# Unit Overview: Seabrook Station Steam Generator Sample System (SS Panel CP-166B)

> ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
> Sample Panel CP-166B conditions high-temperature and high-pressure blowdown water directly from Steam Generators 1, 2, 3, and 4. In-line gross gamma radiation detectors RE-6510 through RE-6513 on Skids RM-SKD-83 through RM-SKD-86 provide early warning of Steam Generator Tube Rupture (SGTR) events. SACC resin column operates under strict operational limitation per General Note 6: "ONLY ONE S/G AT A TIME IS LINED UP TO THE SACC ANALYZER."

## System Purpose & Analytical Architecture
The Steam Generator Sample System conditions continuous liquid sample streams from all four steam generator blowdown lines to monitor secondary water chemistry, protect steam generator U-tubes from corrosion/denting, and detect radioactive fission product leakage from the primary reactor coolant system:
1. **Primary Cooling Stage:**
   * High-pressure 3/8" blowdown tubing enters Steam Generator Primary Sample Heat Exchangers `1-SS-E-14A`, `1-SS-E-14B`, `1-SS-E-14C`, and `1-SS-E-14D`.
   * Cooled by Component Cooling Water (CCW) Loop A via 1" supply and return lines (`1-SS-V-762` through `773`).
2. **Secondary Conditioning & Constant Temperature Stage:**
   * Effluent passes local temperature indicators `TI-2785` through `TI-2788` and Variable Pressure Regulating Elements `PCV-2826` through `PCV-2829`.
   * Enters Constant Temperature Coolers `1-SS-E-173`, `1-SS-E-174`, `1-SS-E-175`, and `1-SS-E-176` inside Panel CP-166B.
   * Chilled fluid is supplied from closed-loop Refrigeration Skid `SKD-128` (located outside PAB in a non-safety area; features compressor `C-12`, condenser `E-182`, receiver `TK-262`, evaporator `E-183`, reservoir `TK-244`, and circulating pump `P-376`).
3. **Chemical & Conductivity Analysis Modules:**
   * Continuous pH analysis elements `pH AE-2864` through `pH AE-2867`.
   * Dual cation conductivity cells `CE-2806-1/2` through `CE-2809-1/2`.
   * Pressure regulators `PCV-2816` through `PCV-2819` (set at 20 PSIG) and back-pressure regulators `PCV-2761` through `PCV-2767` (set at 50 PSIG).
   * Strong Acid Cation Conductivity (SACC) analysis loop with electric heater `H-376`, conductivity cell `CE-2784`, and high temperature cutout switch `TSH-2784`.
4. **Radiation Monitoring Skids:**
   * Four dedicated skids (`RM-SKD-83` for S/G A, `RM-SKD-84` for S/G B, `RM-SKD-85` for S/G C, and `RM-SKD-86` for S/G D).
   * Equipped with gross gamma detectors `RE-6510`, `RE-6511`, `RE-6512`, and `RE-6513` protected by upstream relief valves set at 135 PSIG (`PCV-2771`, `PCV-2770`, `PCV-2769`, `PCV-2768`).
   * Effluent discharges to sample sink `MM-741` and Waste Process Liquid Drains (`WLD DR 256`).

## Equipment & Package Summary
| Tag | Description | Location | Service |
| :--- | :--- | :--- | :--- |
| **1-SS-E-14A..D** | Steam Generator Primary Sample HXs | Sample Panel Area | CCW-cooled primary sample coolers |
| **1-SS-E-173..176**| Constant Temperature Coolers | Panel CP-166B | Chilled secondary sample coolers (1/4" tubing) |
| **SKD-128** | Refrigeration & Chiller Skid | Outside PAB | Closed coolant circulator package (P-376, C-12) |
| **RM-SKD-83..86** | Radiation Monitoring Skids | Grids 4-5, Rows E-H | In-line gamma detectors RE-6510..6513 |
| **1-SS-F-177..180**| Optional Chemistry Filters | Upstream of sensors | Particulate filtration per Note 12 |
| **MM-741** | S/G Sample Sink | Panel CP-166B | Drainage collection to WLD DR 256 |
| **H-376** | SACC Electric Heater / Column | SACC Loop [6-A] | Re-boil / conditioning for cation conductivity |

## License Renewal AMR Scoping
* **In Scope (Green Scope):** Sample lines and components containing liquid are in scope per 10 CFR 54.4(a)(2) and subject to AMR per 10 CFR 54.21 to prevent spatial interaction with safety-related equipment.
* **Out of Scope (LR Note 1 & 3):** Chiller Skid SKD-128 is located outside the PAB in a non-safety area and lines containing air/gas have no license renewal intended function.

## References & Grounding Sources
[^src-1]: ML101620329-part-3.pdf — Drawing PID-1-SS-LR20521 (Rev. 15).
