---
type: Unit Overview
title: 'Unit Overview: Seabrook Station Safety Injection System (SI)'
description: Emergency Core Cooling System architecture, multi-tier injection regimes
  (High, Intermediate, and Low Head), equipment roster, and containment penetrations
  at Seabrook Station.
resource: gs://cs-poc-y03r7kmfyov4kilzg50fd7s-okf-demo/okf-bundles/acme-plant/units/seabrook-safety-injection-system.md
tags:
- emergency-core-cooling
- high-head-injection
- intermediate-head-injection
- low-head-injection
- residual-heat-removal
- safety-injection
- seabrook-station
- unit-overview
sources:
- id: src-1
  resource: reference/raw/pid/ML101620329-part-1.pdf
  title: ML101620329-part-1.pdf
generated:
  by: extracter_agent/gemini-3.8-flash
  at: '2026-10-22T03:46:37Z'
verified:
- by: human:expert-chemical-engineer
  at: '2026-10-22T03:46:37Z'
- by: process:okf-validation-suite
  at: '2026-10-22T03:46:37Z'
status: stable
entity_metadata:
  unit_code: SI
  key_equipment:
  - CS-P-2A
  - CS-P-2B
  - SI-P-6A
  - SI-P-6B
  - RH-P-8A
  - RH-P-8B
  - RH-E-9A
  - RH-E-9B
  - CBS-TK-10A
  - CBS-TK-10B
  - CBS-TK-101A
  - CBS-TK-101B
  facility: Seabrook Station
  safety_classification: Safety Class 2 (Nuclear Safety Related)
  associated_drawings:
  - PID-1-SI-LR20446
  - PID-1-SI-LR20447
  - PID-1-SI-LR20448
---

# Unit Overview: Seabrook Station Safety Injection System (SI)

> ⚠️ **CRITICAL PROCESS SAFETY / DISCREPANCY WARNING:**
> The Safety Injection System (SI) is a multi-tier Emergency Core Cooling System (ECCS) designed to deliver high-, intermediate-, and low-pressure borated water to the Reactor Coolant System (RCS) cold and hot legs during Loss of Coolant Accidents (LOCAs). Redundant trains and diversity of pumping heads ensure core coverage and decay heat removal across the full spectrum of pipe break sizes. Transfer from RWST suction to post-LOCA containment sump recirculation must be carefully coordinated to prevent pump loss of NPSH or sump screen bypass.

## 1. System Function & Injection Tiers

The Safety Injection System encompasses three synchronized hydraulic injection tiers grounded in drawings PID-1-SI-LR20446, PID-1-SI-LR20447, and PID-1-SI-LR20448:
1. **High Head Injection (HHI) / CVCS Charging (Sheet 4):** Powered by centrifugal Charging Pumps `CS-P-2A` and `CS-P-2B` taking suction from the Refueling Water Storage Tank (RWST) `CBS-TK-8` (or normal VCT) and discharging via 4" header through Containment Penetration `X-24` to RCS Cold Legs 1, 2, 3, and 4.
2. **Intermediate Head Injection (IHI) (Sheet 3):** Powered by multi-stage Safety Injection Pumps `SI-P-6A` (Vault 1) and `SI-P-6B` (Vault 2) taking suction from the RWST via 8" CBS headers and discharging via 4" headers through Containment Penetrations `X-25`, `X-26`, and `X-27` to both RCS Hot Legs (1–4) and Cold Legs (A–D).
3. **Low Head Injection (LHI) / Residual Heat Removal (Sheet 5):** Powered by RHR Pumps `RH-P-8A` and `RH-P-8B` through RHR Heat Exchangers `RH-E-9A` and `RH-E-9B`, drawing from RCS Hot Legs during normal cooldown or from Containment Recirculation Sumps `CBS-TK-10A` and `CBS-TK-10B` (via penetrations `X-61` and `X-60`) during post-accident recirculation.

## 2. Process Flow Architecture & Major Equipment Roster

```
           [RWST CBS-TK-8]
                  │
      ┌───────────┼───────────┐
      │ (8" CBS)  │ (8" CBS)  │ (8" CBS)
      ▼           ▼           ▼
  [CS-P-2A/B] [SI-P-6A/B] [RH-P-8A/B] ◄── [Sump A/B via MOVs CBS-V8/14]
   (High Head) (Inter Head) (Low Head)
      │           │           │
      │ 4"        │ 4"        │ 14"/12"
      ▼           ▼           ▼
  [Pen X-24]  [Pen X-25..27] [RH-E-9A/B]
      │           │           │
      ▼           ▼           ▼
 [RCS Cold]  [RCS Hot/Cold] [RHR / Accumulator Hdr]
```

### Major Equipment Roster

| Verbatim Tag | Full Tag | Equipment Description | Safety Class | Drawing Sheet / Location |
| :--- | :--- | :--- | :--- | :--- |
| **CS-P-2A** | `CS-P-2A` | Charging Pump (High Head Safety Injection) | Safety Class 2 | Sheet 4 (Grid B-5/6) |
| **CS-P-2B** | `CS-P-2B` | Charging Pump (High Head Safety Injection) | Safety Class 2 | Sheet 4 (Grid B-9/10) |
| **CS-P-243A** | `CS-P-243A` | Charging Pump 2A Auxiliary Lube Oil Pump | Safety Class A* | Sheet 4 (Grid B-6) |
| **CS-P-243B** | `CS-P-243B` | Charging Pump 2B Auxiliary Lube Oil Pump | Safety Class A* | Sheet 4 (Grid B-9) |
| **SI-P-6A** | `SI-P-6A` | Safety Injection Pump A (Intermediate Head) | Safety Class 2 | Sheet 3 (Grid B-7, Vault 1) |
| **SI-P-6B** | `SI-P-6B` | Safety Injection Pump B (Intermediate Head) | Safety Class 2 | Sheet 3 (Grid B-11, Vault 2) |
| **RH-P-8A** | `SI-RH-P-8A` | Residual Heat Removal Pump A | Safety Class 2 | Sheet 5 (Grid G-4, Vault 1) |
| **RH-P-8B** | `SI-RH-P-8B` | Residual Heat Removal Pump B | Safety Class 2 | Sheet 5 (Grid C-4, Vault 2) |
| **RH-E-9A** | `SI-RH-E-9A` | RHR Loop A Heat Exchanger | Safety Class 2 & 3 | Sheet 5 (Grid H-3/4, Vault 1) |
| **RH-E-9B** | `SI-RH-E-9B` | RHR Loop B Heat Exchanger | Safety Class 2 & 3 | Sheet 5 (Grid D-3/4, Vault 2) |
| **CBS-TK-10A** | `SI-CBS-TK-10A` | Containment Recirculation Sump A | Safety Class 2 | Sheet 5 (Grid E-12) |
| **CBS-TK-10B** | `SI-CBS-TK-10B` | Containment Recirculation Sump B | Safety Class 2 | Sheet 5 (Grid D-12) |
| **CBS-TK-101A** | `SI-CBS-TK-101A` | Protective Chamber A (Sump A Enclosure) | Safety Class 2 | Sheet 5 (Grid E-10) |
| **CBS-TK-101B** | `SI-CBS-TK-101B` | Protective Chamber B (Sump B Enclosure) | Safety Class 2 | Sheet 5 (Grid D-10) |
| **CBS-EP-36A** | `SI-CBS-EP-36A` | Expansion Bellows Piece A | Safety Class 2 | Sheet 5 (Grid E-10) |
| **CBS-EP-36B** | `SI-CBS-EP-36B` | Expansion Bellows Piece B | Safety Class 2 | Sheet 5 (Grid D-10) |

## 3. Containment Penetrations & Boundary Interfaces

* **Containment Penetration X-24:** 4" High Head Safety Injection line from charging pumps into RCS Cold Legs.
* **Containment Penetrations X-25, X-26, X-27:** 4" Intermediate Head Safety Injection lines from SI pumps to RCS Hot and Cold Legs.
* **Containment Penetrations X-9 & X-10:** 12"/16" RHR suction lines from RCS Loop 1 & 4 Hot Legs.
* **Containment Penetrations X-60 & X-61:** 16" Containment Recirculation Sump suction guard pipes enclosed by Protective Chambers `CBS-TK-101A` and `CBS-TK-101B`.

## 4. Key Instrumentation & Interlock Philosophy

* **Pump Miniflow Recirculation:** Charging pumps `CS-P-2A` and `CS-P-2B` are equipped with flow switches `FIS-7325` and `FIS-7326` that automatically cycle motor-operated miniflow valves `CS-V196` and `CS-V197` to prevent deadheading overheating.
* **Intermediate Head Injection Monitoring:** Flow transmitters `FT-918` and `FT-922` provide Main Control Room indication of forward delivery from SI pumps A and B; pressure transmitters `PT-919` and `PT-923` monitor discharge header pressure.
* **RHR Flow Regulation & Interlocks G & H:** Flow switches `FIS-610` and `FIS-611` coordinate with bypass control valves `RH-FCV-610` and `RH-FCV-611` to modulate flow through and around heat exchangers `RH-E-9A` and `RH-E-9B`.
* **Sump Chamber Leak Detection:** Level switches `LS-2356` and `LS-2357` monitor the dry annular space inside Protective Chambers `CBS-TK-101A` and `CBS-TK-101B` to provide immediate alarm if MOV packing or expansion joint leakage occurs during post-LOCA recirculation.

## 5. References & Sources

[^src-1]: ML101620329-part-1.pdf (Drawings PID-1-SI-LR20446 Rev. 17, PID-1-SI-LR20447 Rev. 15, PID-1-SI-LR20448 Rev. 11)
