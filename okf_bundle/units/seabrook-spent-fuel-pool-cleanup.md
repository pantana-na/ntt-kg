---
type: Unit Overview
title: 'Unit Overview: Seabrook Station Spent Fuel Pool Cooling and Cleanup System
  (SF)'
description: System topology, major equipment roster, process flow, and boundary interfaces
  of the Seabrook Station Spent Fuel Pool Cooling and Cleanup System (SF).
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/units/seabrook-spent-fuel-pool-cleanup.md
tags:
- decay-heat-removal
- filtration
- seabrook-station
- spent-fuel-pool
- unit-overview
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-1.pdf
  title: ML101620329-part-1.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-22T03:46:21Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-22T03:46:21Z'
- by: process:okf-validation-suite
  at: '2026-10-22T03:46:21Z'
status: stable
entity_metadata:
  facility: Seabrook Station
  unit_code: SF
  associated_drawings:
  - PID-1-SF-LR20483
  - PID-1-SF-LR20484
  key_equipment:
  - P-12
  - F-33
  - DM-8
  - F-34
  - P-272
  - F-207
  safety_classification: Safety Class NNS
---

# Unit Overview: Seabrook Station Spent Fuel Pool Cooling and Cleanup System (SF)

> ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
> The Spent Fuel Pool Cooling and Cleanup System (SF) maintains pool water inventory, subcriticality (via dissolved boron), and water clarity while dissipating decay heat from irradiated fuel assemblies. Return piping into the Spent Fuel Pool terminates 11 feet above fuel assemblies (General Note 6) with anti-siphon holes and check valve 1-SF-V34 to physically prevent accidental gravity siphoning of pool inventory below the safe radiation shielding water level.

## 1. System Function & Boundaries

The Spent Fuel Pool Cooling and Clean-up System (SF) at Seabrook Station performs two key process functions:
1. **Surface Skimming and Particulate Filtration:** Collects surface water from Spent Fuel Pool skimmers `S-2A` through `S-2E` and Cask Pool skimmer `1-SF-S-2E`, circulating fluid via Skimmer Pump `1-SF-P-12` through Fuel Pool Prefilter `1-SF-F-33`.
2. **Ionic Purification and Demineralization:** Passes filtered water through Fuel Pool Demineralizer `1-SF-DM-8` and downstream resin-trap Fuel Pool Postfilter `1-SF-F-34` before returning purified water to the Spent Fuel Pool.
3. **Refueling Cavity Cleanup Integration:** Integrates with the reactor cavity purification loop via Containment Penetration `X-39`, Refueling Canal Skimmer Pump `SF-P-272`, and Reactor Cavity Cleanup Filter `SF-F-207` (Dwg PID-1-SF-LR20484).

## 2. Process Flow Architecture & Major Equipment

```
[SFP Skimmers S-2A..E] ──► [4" Suction Hdr] ──► [Pump P-12] ──► (1"x4" Reducer)
                                                                       │
┌──────────────────────────────────────────────────────────────────────┘
▼
[Prefilter F-33] ────► [Demineralizer DM-8] ────► [Postfilter F-34]
   (Bypass V25)            (Bypass V76)              (Bypass V37)
        │                       │                         │
        └───────────────────────┴─────────────────────────┴────────► [4" Return Header]
                                                                             │
                                                                     [1-SF-V33 / V34]
                                                                             │
                                                                             ▼
                                                                     [Spent Fuel Pool]
                                                                  (+11 ft above fuel)
```

### Major Equipment Roster

| Verbatim Tag | Full Tag | Equipment Description | Safety Class | Drawing Location |
| :--- | :--- | :--- | :--- | :--- |
| **P-12** | `1-SF-P-12` | Spent Fuel Pool Skimmer Pump | Safety Class NNS | PID-1-SF-LR20483 (Grid B-7/8) |
| **F-33** | `1-SF-F-33` | Fuel Pool Prefilter | Safety Class NNS | PID-1-SF-LR20483 (Grid E/F-7/8) |
| **DM-8** | `1-SF-DM-8` | Fuel Pool Demineralizer | Safety Class NNS | PID-1-SF-LR20483 (Grid E/F-6) |
| **F-34** | `1-SF-F-34` | Fuel Pool Postfilter | Safety Class NNS | PID-1-SF-LR20483 (Grid E/F-4) |
| **S-2A..E** | `1-SF-S-2A..E` | Spent Fuel Pool Skimmers (5 total) | Safety Class NNS | PID-1-SF-LR20483 (Grid C/D/E-11/12) |
| **P-272** | `SF-P-272` | Refueling Canal Skimmer Pump | Safety Class NNS | PID-1-SF-LR20484 (Grid 8-B) |
| **F-207** | `SF-F-207` | Reactor Cavity Cleanup Filter | Safety Class NNS | PID-1-SF-LR20484 (Grid 10-B) |
| **S-245A..E** | `SF-S-245A..E` | Refueling Pool / Canal Skimmers (5 total) | Safety Class NNS | PID-1-SF-LR20484 (Grid 10-E..H) |

## 3. Boundary Interfaces & Utility Cross-Ties

* **Chemical & Volume Control (CVCS):** Boric acid makeup tie-in via valve `CS-V91` (2" line); purification header tie-ins to valves `CS-V100`, `CS-V267`, `CS-V83`, `CS-V274`, `CS-V255`, `CS-V280`, `CS-V260` (Dwgs 20723, 20728).
* **Reactor Make-Up Water (RMW):** Tie-in downstream of boundary isolation (`RMW-2"`).
* **Resin Sluicing (RS):** Resin transfer lines to `RS-TK-79A & B` via valve `1-SF-V57` and sluice supply via `1-SF-V47`.
* **Waste Liquid Processing Drains (WLD):** Common filter vent manifold with sight glass `FG-2612` draining to `WLD OR 218`; equipment casing drains to `CS DRN HDR` (`WLD OR 183`) and `WLD DR 232`.
* **Containment Boundary:** Transfer line from Refueling Cavity cleanup loop enters auxiliary building via Containment Penetration `X-39` (isolated by inside valve `SF-V86` and locked-closed outside valve `SF-V87`).

## 4. Key Instrumentation & Control Architecture

* **Pump Suction Protection:** `PISL-2621` monitors pump `P-12` suction pressure to trip the pump on low head and prevent cavitation.
* **Filter Loading Diagnostics:** Differential pressure switches `PDIS-2622` (F-33), `PDIS-2624` (DM-8), and `PDIS-2623` (F-34) alert operators to particulate and resin blinding.
* **Resin Bed Protection:** Temperature element `TE-2625` monitors DM-8 inlet water temperature to prevent thermal degradation of anion/cation exchange resin beads.
* **Refueling Cavity Level:** Transmitter `LT-2629` / element `LE-2629-1` provides continuous refueling pool and transfer canal water level indication.

## 5. References & Sources

[^src-1]: ML101620329-part-1.pdf (Drawings PID-1-SF-LR20483 Rev. 0 & PID-1-SF-LR20484 Rev. 0)
