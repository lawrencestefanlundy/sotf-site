---
type: concept
slug: photonics
canonical_name: Photonics
aliases:
- photonics-optics
- Photonics & Optics
kind: theme
parent_concepts:
- photonic-systems
- pic-platforms
related_concepts: []
sources:
- '[[2025-09-23-the-compute-gradient]]'
- '[[2025-04-23-what-if-ai-can-already-feel]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2022-12-15-im-doing-research-in-venture-capital]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
frontier:
- ''
last_updated: '2026-05-07'
tags:
- concept
- theme
mention_count: 729
descendants:
- diffractive-deep-neural-network
- free-space-photonics
- microwave-photonics
- mid-ir-photonics
- optical-frequency-comb
- optical-frequency-division
- optoelectronic-oscillator
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 11
recent_mentions:
- slug: 2026-06-22-thermal-stack-layer-landscape
  title: AI datacentre thermal stack, junction-to-ambient — per-layer players, M&A, capture (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-18-us-backs-photonics-expansion-for-ai-data-centres-under-chips
  title: US backs photonics expansion for AI data centres under CHIPS Act - Digital Watch Observatory
  date: '2026-06-18'
  kind: web
- slug: 2026-06-17-single-photon-detector-market-spad-snspd
  title: Single-photon detector market aggregation — SPAD, SiPM, SNSPD (2024–2035)
  date: '2026-06-17'
  kind: web
- slug: 2026-06-16-trapped-ion-landscape-2026
  title: Trapped-ion quantum computing landscape 2026 (vendors, scale, integrated photonics)
  date: '2026-06-16'
  kind: web
- slug: 2026-06-15-barry-silverstein-rochester-cxr
  title: University of Rochester hires former Meta exec Barry Silverstein to direct Center for Extended Reality
  date: '2026-06-15'
  kind: web
- slug: 2026-06-15-luminate-ny-accelerator-terms
  title: Luminate NY OPI accelerator — terms and structure
  date: '2026-06-15'
  kind: web
- slug: 2026-06-15-gf-investor-day-2026
  title: GlobalFoundries Investor Day 2026 (presentation)
  date: '2026-06-15'
  kind: web
- slug: 2026-06-13-usgs-mcs-rare-earths-supply-concentration
  title: USGS Mineral Commodity Summaries — Rare Earths (2025 / 2026 editions)
  date: '2026-06-13'
  kind: web
neighbors: []
---
## Physics / mechanism

Photonics is the generation, manipulation, and detection of photons—typically across UV, visible, NIR, and mid-IR spectra. Unlike electronics, signal carriers have zero rest mass, enabling propagation at *c* with negligible resistive loss. Key parameters: wavelength (λ), refractive index (n), group velocity dispersion (GVD), insertion loss (dB), and extinction ratio (dB). Platform state-of-the-art: silicon photonics achieves ~1 dB/cm waveguide loss at 1550 nm, InP lasers hit sub-100 kHz linewidth, LiNbO₃ modulators reach >100 GHz bandwidth. Co-packaged optics in datacenter switching is pushing integration density toward 1.6 Tb/s per package. Quantum photonics and mid-IR sensing are the frontier growth vectors.

## Competitive landscape

Silicon photonics (SiPh) competes with and complements III-V (InP, GaAs), polymer waveguides, and emerging platforms like silicon nitride (SiN) and thin-film LiNbO₃. Each trades off loss, nonlinearity, active gain, and CMOS foundry compatibility differently.

| Platform | Loss (dB/cm) | Active gain | Foundry CMOS-compatible |
|---|---|---|---|
| Silicon (SiPh) | ~1–2 | No (indirect bandgap) | Yes |
| Silicon Nitride | ~0.1 | No | Yes |
| InP / III-V | ~2–5 | Yes | No |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*

## Merged from `photonics-optics` (archived 2026-05-07)

*Hyphenated variant. Photonics is the canonical concept; 'photonics-optics' was an Attio-tag-derived duplicate.*

# Photonics & Optics

*Kind: technology*

## Physics / mechanism

Photonics exploits photons rather than electrons as information or energy carriers. Core physics: Maxwell's equations govern propagation; waveguide confinement via total internal reflection (silicon-on-insulator rib waveguides, ~450 nm × 220 nm cross-sections); modulation via Pockels effect (LiNbO₃, BTO) or plasma dispersion (Si). Key figures of merit: insertion loss (target <1 dB/cm), electro-optic bandwidth (>100 GHz demonstrated in thin-film LiNbO₃), extinction ratio (>20 dB), and V_π·L (sub-1 V·cm now achievable). Silicon photonics dominates datacentre interconnect at 400G–1.6T; III-V (InP, GaAs) leads coherent and sensing; emerging platforms include SiN (ultralow loss, ~0.1 dB/m), lithium niobate on insulator (LNOI), and BTO-on-Si. Photonic integrated circuits (PICs) are manufactured on 200/300 mm CMOS-compatible lines, enabling co-integration with electronics.

## Competitive landscape

Competing carrier: RF/microwave electronics dominate sub-100 GHz comms but hit energy and bandwidth walls above that. Competing photonic platforms pit silicon photonics (low cost, CMOS-native) against InP (monolithic laser integration, higher cost) and polymer waveguides (flexible, lossy). For sensing, MEMs and RF radar compete with LiDAR and optical coherence. Quantum photonics (single-photon sources, entangled pairs) is an adjacent but distinct segment.

| Platform | Loss | EO BW | Laser integration |
|----------|------|--------|-------------------|
| Si photonics | ~2 dB/cm | ~50 GHz | Heterogeneous bonding |
| LNOI | ~0.3 dB/cm | >100 GHz | Hybrid |
| InP | ~1–2 dB/cm | >100 GHz | Monolithic |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
