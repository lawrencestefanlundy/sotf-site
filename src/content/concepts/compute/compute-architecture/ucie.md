---
type: concept
slug: ucie
canonical_name: UCIe (Universal Chiplet Interconnect Express)
aliases: []
kind: technology
parent_concepts:
- compute
- compute-architecture
related_concepts: []
sources:
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-03-02-chiplets-architecture-share-rebellions-rebel-100-industry-s]]'
- '[[2026-03-05-chiplets-architecture-share-chiplet-summit-2026-ucie]]'
- '[[2026-07-02-semianalysis-ectc2026-advanced-packaging]]'
- '[[2024-yole-advanced-packaging-2024]]'
- '[[2026-04-15-semianalysis-isscc-2026]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 15
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2026-07-02-semianalysis-ectc2026-advanced-packaging
  title: 'ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More'
  date: '2026-07-02'
  kind: web
- slug: 2026-04-15-semianalysis-isscc-2026
  title: 'ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More'
  date: '2026-04-15'
  kind: web
- slug: 2026-03-05-chiplets-architecture-share-chiplet-summit-2026-ucie
  title: 'Chiplet Summit 2026: UCIe Momentum Across Growing Ecosystem (UCIe Consortium)'
  date: '2026-03-05'
  kind: web
- slug: 2026-03-02-chiplets-architecture-share-rebellions-rebel-100-industry-s
  title: 'Rebellions Rebel 100: Industry''s First Quad-Chiplet AI Solution with UCIe (Tom''s Hardware)'
  date: '2026-03-02'
  kind: web
- slug: 2024-yole-advanced-packaging-2024
  title: Yole Group — Advanced Packaging 2024 Market Analysis
  date: '2024-12-01'
  kind: web
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
neighbors: []
---
## Physics / mechanism

UCIe is a die-to-die interconnect standard ratified in 2022 (v1.0) and updated in 2023 (v1.1), enabling chiplets from different vendors to interoperate on a common substrate. The physical layer runs over a 2D or advanced packaging interface; standard package delivers up to ~16 GB/s/mm of interconnect bandwidth density, while advanced package (using silicon bridge or interposer) pushes ~160 GB/s/mm. Protocol stack sits atop PCIe and CXL, so existing software stacks map cleanly. Die-to-die latency targets sub-2 ns. Consortium members include Intel, TSMC, Samsung, AMD, Qualcomm, Arm, and GF. Spec governs the physical, adaptation, and protocol layers, leaving die implementation to vendors.

## Competitive landscape

The direct alternative is proprietary die-to-die links: Intel's EMIB+AIB, AMD's Infinity Fabric, NVIDIA's NVLink-C2C. These outperform UCIe on bandwidth density today but lock the supply chain. BoW (Bunch of Wires) from OCP is a simpler, lower-level subset. HBM sits adjacent — it solves memory bandwidth, not heterogeneous logic integration. Optical die-to-die (co-packaged optics) threatens UCIe's relevance at rack scale but remains 3–5 years from cost parity.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
