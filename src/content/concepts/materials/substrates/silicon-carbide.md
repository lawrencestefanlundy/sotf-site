---
type: concept
slug: silicon-carbide
aliases:
- SiC
- 4H-SiC
- silicon carbide
canonical_name: Silicon Carbide
parent_concepts:
- wide-bandgap-semiconductors
related_concepts:
- wide-bandgap-semiconductors
- gallium-nitride
- silicon-carbide-photonics
- power-electronics
- compound-semiconductors
- mocvd-mbe
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-07-13-department-of-commerce-announces-direct-funding-agreement-wi]]'
- '[[2026-06-12-hku-sic-cryogenic-neuromorphic-chip-10mk]]'
- '[[2024-06-01-stmicroelectronics-to-build-5bn-silicon-carbide-campus-in-it]]'
frontier:
- Can SiC substrate cost reach parity with silicon for 200mm wafers before 2030, or does defect density remain the binding constraint?
- Will SiC MOSFET device performance (channel mobility, gate-oxide reliability) close the remaining gap to theoretical material limits?
- Can power-electronics SiC fabs be repurposed for low-loss photonic waveguides, or are the epi/etch recipes fundamentally incompatible?
last_updated: 2026-06-02
tags:
- concept
mention_count: 44
sources_7d: 6
sources_30d: 13
recent_mentions:
- slug: 2026-07-26-humanoid-duty-cycle-thermal-constraint
  title: 'What actually limits a humanoid to minutes: the thermal cliff, not the battery'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-14-boschs-sic-fab-deal-adds-to-a-resurgence-in-chips-act-fundin
  title: Bosch's SiC fab deal adds to a resurgence in CHIPS Act funding - Electronics360
  date: '2026-07-14'
  kind: web
- slug: 2026-07-13-department-of-commerce-announces-direct-funding-agreement-wi
  title: Department of Commerce Announces Direct Funding Agreement with Bosch for a $225 Million CHIPS Program Award to Support Domestic Production of Silicon Carbide Semiconductors - National Institute of Standards and Technology (.gov)
  date: '2026-07-13'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-06-22-sintered-metal-die-attach-landscape
  title: Sintered-silver / sintered-copper die-attach landscape — physics, incumbents, AI-migration question (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-thermal-stack-layer-landscape
  title: AI datacentre thermal stack, junction-to-ambient — per-layer players, M&A, capture (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-tim-approaches-full-sweep
  title: TIM approaches — exhaustive in-market + R&D sweep (vendors, classes, startups)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-12-hku-sic-cryogenic-neuromorphic-chip-10mk
  title: HKU world-first cryogenic neuromorphic chip at 10 mK (silicon carbide, impact-ionisation spiking)
  date: '2026-06-12'
  kind: web
neighbors:
- slug: wide-bandgap-semiconductors
  name: Wide-Bandgap Semiconductors
  path: /materials/substrates/wide-bandgap-semiconductors/
  macro: materials
- slug: gallium-nitride
  name: Gallium Nitride
  path: /energy-power/power-electronics/gallium-nitride/
  macro: energy-power
- slug: silicon-carbide-photonics
  name: Silicon Carbide Photonics
  path: /materials/substrates/silicon-carbide-photonics/
  macro: materials
- slug: power-electronics
  name: Power Electronics
  path: /energy-power/power-electronics/power-electronics/
  macro: energy-power
- slug: compound-semiconductors
  name: Compound Semiconductors
  path: /materials/substrates/compound-semiconductors/
  macro: materials
- slug: mocvd-mbe
  name: MOCVD / MBE
  path: /manufacturing/equipment-processes/mocvd-mbe/
  macro: manufacturing
---
Silicon carbide (SiC) is a wide-bandgap compound semiconductor with a bandgap of approximately 3.26 eV (4H polytype) versus 1.12 eV for silicon. Its key material advantages over silicon are: breakdown electric field ~10× higher (~3 MV/cm), thermal conductivity ~3× higher (~490 W/m·K), and the ability to operate at junction temperatures up to ~600 °C. These properties make SiC the dominant material for high-voltage power devices — specifically MOSFETs and Schottky diodes operating in the 600–3300 V range.

The primary application is EV traction inverters (800V battery systems) and industrial motor drives, where SiC devices shrink the inverter by enabling higher switching frequencies with lower conduction and switching losses. The thesis **Sic Ev Traction Dominance** tracks the expected displacement of silicon IGBTs by SiC MOSFETs in EV traction by 2030. SiC also matters as a substrate for gallium nitride epitaxy: GaN-on-SiC dominates RF power amplifiers for 5G base stations and defence radar due to superior thermal extraction versus GaN-on-silicon. The material has a secondary frontier as a photonic platform — see [Silicon Carbide Photonics](/materials/substrates/silicon-carbide-photonics/) for quantum and mid-IR waveguide applications.

SiC wafer supply is dominated by Wolfspeed (US), Coherent (formerly II-VI), SICC (China), and SK Siltron CSS (Korea/US). The bottleneck has been crystal growth yield and substrate defect density; the industry is transitioning from 150mm to 200mm wafers.

## Frontier

- Can SiC substrate cost reach parity with silicon for 200mm wafers before 2030, or does defect density remain the binding constraint?
- Will SiC MOSFET device performance (channel mobility, gate-oxide reliability) close the remaining gap to theoretical material limits?
- Can power-electronics SiC fabs be repurposed for low-loss photonic waveguides, or are the epi/etch recipes fundamentally incompatible?
