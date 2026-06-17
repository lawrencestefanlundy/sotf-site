---
type: concept
slug: silicon-carbide
canonical_name: Silicon Carbide
aliases:
- SiC
- 4H-SiC
- silicon carbide
parent_concepts:
- wide-bandgap-semiconductors
related_concepts:
- wide-bandgap-semiconductors
- gallium-nitride
- silicon-carbide-photonics
- power-electronics
- compound-semiconductors
- mocvd-mbe
sources: []
frontier:
- Can SiC substrate cost reach parity with silicon for 200mm wafers before 2030, or does defect density remain the binding constraint?
- Will SiC MOSFET device performance (channel mobility, gate-oxide reliability) close the remaining gap to theoretical material limits?
- Can power-electronics SiC fabs be repurposed for low-loss photonic waveguides, or are the epi/etch recipes fundamentally incompatible?
last_updated: 2026-06-02
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-06-01-nibras-ucl-chipstart
  title: UCL EEE ventures selected for national ChipStart programme (incl. Nibras Communications)
  date: '2026-06-01'
  kind: web
- slug: 2026-05-26-semianalysis-800vdc-revolution
  title: Inside the 800VDC Revolution – Part 1
  date: '2026-05-26'
  kind: web
- slug: 2024-trendforce-foundry-2024
  title: TrendForce — Global Foundry Industry Outlook 2024-2026
  date: '2024-11-15'
  kind: web
- slug: 2024-omdia-power-electronics-forecast
  title: Omdia — Power Semiconductors Long-Term Forecast 2024
  date: '2024-11-01'
  kind: web
- slug: 2024-yole-power-sic-2024
  title: Yole Group — Power SiC 2024 Market Analysis
  date: '2024-09-15'
  kind: web
- slug: 2024-yole-power-gan-2024
  title: Yole Group — Power GaN 2024 Market Analysis
  date: '2024-09-15'
  kind: web
- slug: 2023-07-27-e10-pushing-moores-law-to-the-limit
  title: '🔮E10: Pushing Moore''s Law to the Limit with High-NA EUV (aka Nanoscale Chip Printing)'
  date: '2023-07-27'
  kind: substack
neighbors:
- slug: wide-bandgap-semiconductors
  name: Wide-Bandgap Semiconductors
  path: /sotf-site/materials/substrates/wide-bandgap-semiconductors/
  macro: materials
- slug: gallium-nitride
  name: Gallium Nitride
  path: /sotf-site/energy-power/power-electronics/gallium-nitride/
  macro: energy-power
- slug: silicon-carbide-photonics
  name: Silicon Carbide Photonics
  path: /sotf-site/materials/substrates/silicon-carbide-photonics/
  macro: materials
- slug: power-electronics
  name: Power Electronics
  path: /sotf-site/energy-power/power-electronics/power-electronics/
  macro: energy-power
- slug: compound-semiconductors
  name: Compound Semiconductors
  path: /sotf-site/materials/substrates/compound-semiconductors/
  macro: materials
- slug: mocvd-mbe
  name: MOCVD / MBE
  path: /sotf-site/manufacturing/equipment-processes/mocvd-mbe/
  macro: manufacturing
---
Silicon carbide (SiC) is a wide-bandgap compound semiconductor with a bandgap of approximately 3.26 eV (4H polytype) versus 1.12 eV for silicon. Its key material advantages over silicon are: breakdown electric field ~10× higher (~3 MV/cm), thermal conductivity ~3× higher (~490 W/m·K), and the ability to operate at junction temperatures up to ~600 °C. These properties make SiC the dominant material for high-voltage power devices — specifically MOSFETs and Schottky diodes operating in the 600–3300 V range.

The primary application is EV traction inverters (800V battery systems) and industrial motor drives, where SiC devices shrink the inverter by enabling higher switching frequencies with lower conduction and switching losses. The thesis **Sic Ev Traction Dominance** tracks the expected displacement of silicon IGBTs by SiC MOSFETs in EV traction by 2030. SiC also matters as a substrate for gallium nitride epitaxy: GaN-on-SiC dominates RF power amplifiers for 5G base stations and defence radar due to superior thermal extraction versus GaN-on-silicon. The material has a secondary frontier as a photonic platform — see [Silicon Carbide Photonics](/sotf-site/materials/substrates/silicon-carbide-photonics/) for quantum and mid-IR waveguide applications.

SiC wafer supply is dominated by Wolfspeed (US), Coherent (formerly II-VI), SICC (China), and SK Siltron CSS (Korea/US). The bottleneck has been crystal growth yield and substrate defect density; the industry is transitioning from 150mm to 200mm wafers.

## Frontier

- Can SiC substrate cost reach parity with silicon for 200mm wafers before 2030, or does defect density remain the binding constraint?
- Will SiC MOSFET device performance (channel mobility, gate-oxide reliability) close the remaining gap to theoretical material limits?
- Can power-electronics SiC fabs be repurposed for low-loss photonic waveguides, or are the epi/etch recipes fundamentally incompatible?
