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
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
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
