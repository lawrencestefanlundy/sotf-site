---
type: concept
slug: silicon-nitride
canonical_name: Silicon Nitride
aliases:
- sin
- silicon-nitride
kind: material
parent_concepts:
- materials
- substrates
related_concepts: []
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-05-24-mose2-exciton-polariton-all-optical-switch]]'
- '[[2026-06-04-q-memory-site]]'
- '[[2023-09-04-sinq-csa-catapult]]'
- '[[2026-06-16-trapped-ion-landscape-2026]]'
- '[[2026-05-02-hybrid-bto-sin-ultra-low-power-tuning-acs-photonics]]'
frontier:
- Does the SiN dual-use AI-accelerator / optical-matmul mode give full-stack photonic-QC players a fundable near-term wedge, or is it quantum-washing? (Q-Memory test.)
last_updated: '2026-06-04'
tags:
- concept
- material
mention_count: 81
last_reorg_date: '2026-05-13'
sources_7d: 8
sources_30d: 32
recent_mentions:
- slug: 2026-06-16-trapped-ion-landscape-2026
  title: Trapped-ion quantum computing landscape 2026 (vendors, scale, integrated photonics)
  date: '2026-06-16'
  kind: web
- slug: 2026-06-04-q-memory-site
  title: Q-Memory — company website (q-memory.tech)
  date: '2026-06-04'
  kind: web
- slug: 2026-05-24-mose2-exciton-polariton-all-optical-switch
  title: New light-based switch could cut chip energy use and speed future AI photonics
  date: '2026-05-24'
  kind: web
- slug: 2026-05-02-hybrid-bto-sin-ultra-low-power-tuning-acs-photonics
  title: Hybrid BTO-SiN ultra-low power tuning (ACS Photonics)
  date: '2026-05-02'
  kind: web
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2024-12-16-willow-and-the-race-to-quantum-advantage
  title: Willow and The Race to Quantum Advantage (Feat. Kris Kaczmarek)
  date: '2024-12-16'
  kind: substack
- slug: 2023-09-04-sinq-csa-catapult
  title: SiNQ — Silicon Nitride for Quantum Computing (CSA Catapult live project)
  date: '2023-09-04'
  kind: web
neighbors: []
---
## Physics / mechanism

Silicon nitride (Si₃N₄) is a wide-bandgap ceramic dielectric (bandgap ~5 eV) with exceptional mechanical hardness (~30 GPa), thermal stability (>1400°C), and low optical absorption in the visible through mid-IR. In photonics, stoichiometric Si₃N₄ waveguides exhibit propagation losses <0.1 dB/m at 1550 nm, negligible two-photon absorption at telecom wavelengths, and a moderate Kerr nonlinearity (n₂ ≈ 2.4 × 10⁻¹⁹ m²/W) — enabling frequency combs, LiDAR PICs, and low-noise microwave photonics. In semiconductors, LPCVD Si₃N₄ films serve as hard masks, etch stops, and stress-engineering layers (tensile ~1 GPa). Damascene-process Si₃N₄ photonics (EPFL/Ligentec lineage) is the current state of the art for ultra-low-loss PICs.

## Competitive landscape

Silicon nitride competes with silicon-on-insulator (SOI) for photonic integration — SOI wins on CMOS compatibility and high-index contrast but loses on two-photon absorption and loss at visible wavelengths. Lithium niobate (TFLN) competes for electro-optic modulation (Pockels effect) where Si₃N₄ has no native EO response. Aluminium nitride (AlN) offers EO capability plus UV transparency. Silica (SiO₂) planar waveguides offer lower loss but massive footprint. For structural/ceramic applications, SiC and Al₂O₃ are the principal substitutes.

| Platform | Propagation loss | EO modulation | CMOS compatible |
|---|---|---|---|
| Si₃N₄ | <0.1 dB/m | No | Partial |
| SOI | ~1–2 dB/cm | No | Yes |
| TFLN | ~0.3 dB/cm | Yes | No |

## Quantum computing on SiN

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
