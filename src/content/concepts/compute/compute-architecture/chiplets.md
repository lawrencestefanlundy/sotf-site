---
type: concept
slug: chiplets
canonical_name: Chiplets
aliases: []
kind: technology
parent_concepts:
- compute
- compute-architecture
related_concepts: []
sources:
- '[[2023-10-06-e18-the-state-of-silent-speech-and]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2026-03-26-sotf-interview-dorian-haci-mintneuro]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2023-05-24-launching-state-of-the-future]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2026-03-02-chiplets-architecture-share-rebellions-rebel-100-industry-s]]'
- '[[2026-06-22-beyond-cmos-device-layer-research]]'
- '[[2026-03-05-chiplets-architecture-share-chiplet-summit-2026-ucie]]'
- '[[2026-07-02-semianalysis-ectc2026-advanced-packaging]]'
- '[[2024-yole-advanced-packaging-2024]]'
- '[[2025-12-31-chiplets-architecture-share-chiplet-market-size-share]]'
- '[[2026-05-30-intel-glass-substrates-program]]'
- '[[2026-05-28-europes-semiconductor-strategy-chiplets-ecosystem-integratio]]'
- '[[2026-04-15-semianalysis-isscc-2026]]'
- '[[2024-tsmc-cowos-roadmap-disclosure]]'
- '[[2026-03-31-semianalysis-nvidia-blackwell-dissection]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 97
last_reorg_date: '2026-05-13'
descendants: []
sources_7d: 0
sources_30d: 3
recent_mentions:
- slug: 2026-07-02-semianalysis-ectc2026-advanced-packaging
  title: 'ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More'
  date: '2026-07-02'
  kind: web
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2026-05-28-europes-semiconductor-strategy-chiplets-ecosystem-integratio
  title: 'Europe’s Semiconductor Strategy: Chiplets, Ecosystem Integration, and Chips Act 2.0 in 2026 - News and Statistics - IndexBox'
  date: '2026-05-28'
  kind: web
- slug: 2026-04-15-semianalysis-isscc-2026
  title: 'ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More'
  date: '2026-04-15'
  kind: web
- slug: 2026-03-31-semianalysis-nvidia-blackwell-dissection
  title: Dissecting Nvidia Blackwell - Tensor Cores, PTX Instructions, SASS, Floorsweep, Yield
  date: '2026-03-31'
  kind: web
- slug: 2026-03-26-sotf-interview-dorian-haci-mintneuro
  title: 'Chips for the Brain: Modular Semiconductors for Neural Interfaces (MintNeuro / Dorian Haci)'
  date: '2026-03-26'
  kind: substack
- slug: 2026-03-05-chiplets-architecture-share-chiplet-summit-2026-ucie
  title: 'Chiplet Summit 2026: UCIe Momentum Across Growing Ecosystem (UCIe Consortium)'
  date: '2026-03-05'
  kind: web
- slug: 2026-03-02-chiplets-architecture-share-rebellions-rebel-100-industry-s
  title: 'Rebellions Rebel 100: Industry''s First Quad-Chiplet AI Solution with UCIe (Tom''s Hardware)'
  date: '2026-03-02'
  kind: web
neighbors: []
---
## Physics / mechanism

Chiplets are discrete, pre-validated silicon (or III-V / glass) dies designed to be integrated into a multi-die package rather than a monolithic SoC. Integration is achieved via advanced packaging: 2.5D (dies side-by-side on an interposer — silicon, organic, or glass), 3D (die-stacked with TSVs), or hybrid bonding (Cu-Cu direct bond, <10 µm pitch). Key parameters: die-to-die bandwidth density (>1 TB/s/mm² with hybrid bonding vs. ~100 GB/s/mm² for organic substrate), interconnect pitch (SoIC at ~9 µm, shrinking toward 1–3 µm), and thermal resistance (W/mm²). UCIe 1.0 standardizes the PHY/protocol layer. State of art: AMD 3D V-Cache (TSMC SoIC), Intel Foveros Direct, NVIDIA GB200 NVL72 disaggregated memory. Disaggregation breaks the monolithic reticle limit (~800 mm²) and enables per-function node optimization — logic on 3 nm, analog/RF on mature nodes.

## Competitive landscape

Monolithic scaling (TSMC N2/A16, Intel 18A) remains the primary competitor where die area fits the reticle and yield is acceptable. Wafer-scale integration (Cerebras) eliminates packaging overhead entirely. SiP (system-in-package) with wire-bond is the low-cost legacy path. Glass substrates (Intel, Corning) threaten silicon interposers on cost and loss at high frequency.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*

## Merged from root duplicate (chiplets.md at concepts/ root, 2026-06-10)

# Chiplets

Decomposing a monolithic SoC into smaller dies integrated in-package over a die-to-die interconnect (UCIe and competitors), trading the reticle limit and yield curve of one big die for the cost/heterogeneity of several small ones. The architectural substrate under AI-accelerator scaling, HBM integration, and the advanced-packaging value shift.
