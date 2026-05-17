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
- '[[2026-05-02-return-of-lithium-niobate-photonics-spectra-jan-2026]]'
- '[[2026-01-24-warning-from-the-photonics-industry-europes-lead-is-at-risk-]]'
- '[[2025-09-26-edmund-optics-acquires-son-x-bioscan-marapr-2025---photonics]]'
- '[[2026-05-02-hybrid-bto-sin-ultra-low-power-tuning-acs-photonics]]'
- '[[2026-01-09-inside-the-gaos-review-of-chips-act-manufacturing-investment]]'
- '[[2025-01-06-radiant-acquires-nilt]]'
- '[[2026-05-02-bto-pockels-modulator-on-silicon-photonics-jlt-2019]]'
frontier:
- ''
last_updated: '2026-05-07'
tags:
- concept
- theme
mention_count: 276
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 18
recent_mentions:
- slug: 2026-05-02-return-of-lithium-niobate-photonics-spectra-jan-2026
  title: Return of Lithium Niobate (Photonics Spectra Jan 2026)
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-hybrid-bto-sin-ultra-low-power-tuning-acs-photonics
  title: Hybrid BTO-SiN ultra-low power tuning (ACS Photonics)
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-bto-pockels-modulator-on-silicon-photonics-jlt-2019
  title: BTO Pockels modulator on silicon photonics (JLT 2019)
  date: '2026-05-02'
  kind: web
- slug: 2026-04-10-doe-to-award-100-million-in-grants-amid-science-funding-cuts
  title: DOE to award $100 million in grants amid science funding cuts - R&D World
  date: '2026-04-10'
  kind: web
- slug: 2026-02-12-how-to-invest-in-ai-sovereignty-sovereign
  title: How to Invest in AI Sovereignty — Sovereign Albion w/ Andrew Bennett
  date: '2026-02-12'
  kind: substack
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
- slug: 2026-01-24-warning-from-the-photonics-industry-europes-lead-is-at-risk-
  title: 'Warning from the photonics industry: Europe’s lead is at risk - ioplus.nl'
  date: '2026-01-24'
  kind: web
- slug: 2026-01-09-inside-the-gaos-review-of-chips-act-manufacturing-investment
  title: Inside the GAO’s Review of CHIPS Act Manufacturing Investments - Optics & Photonics News
  date: '2026-01-09'
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
