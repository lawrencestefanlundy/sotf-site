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
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
descendants:
- ucie-standard
sources_7d: 0
sources_30d: 0
recent_mentions: []
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
