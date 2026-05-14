---
type: concept
slug: dram
canonical_name: DRAM
aliases: []
kind: technology
parent_concepts:
- memory
- mainstream-memory
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

DRAM stores each bit as charge on a capacitor paired with an access transistor (1T1C cell). Read is destructive—sense amplifiers detect sub-100 fV charge differentials and rewrite. Refresh cycles every ~64 ms prevent leakage-induced data loss, consuming ~10–15% of active power. DRAM scales via process node and cell capacitance engineering (MIM, MIS, stacked trench). Current SOTA: SK Hynix HBM3E at 1.2 TB/s bandwidth, Samsung DDR5 at 7200 MT/s per pin, 10 nm-class (1β/1γ) nodes. Cell capacitance must hold ~10 fF minimum despite shrinking geometry—the central materials and integration challenge as nodes compress below 10 nm.

## Competitive landscape

DRAM competes directly with SRAM (faster, 6T, no refresh, 50–100× area penalty) and emerging non-volatile alternatives for specific tiers. HBM is DRAM repackaged for AI compute bandwidth. Key competitive pressures come from MRAM (persistent, radiation-hard, latency-competitive but density-limited), FeRAM (low power, niche embedded), and CXL-attached DRAM pools blurring memory-storage boundaries.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
