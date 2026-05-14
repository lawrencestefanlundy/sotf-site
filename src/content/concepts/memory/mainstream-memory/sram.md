---
type: concept
slug: sram
canonical_name: SRAM
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

Six-transistor (6T) SRAM stores one bit in a cross-coupled inverter pair (two PMOS loads, two NMOS drivers) stabilised by two access transistors. No refresh required; data persists as long as power is supplied. Read/write speed is determined by bitline precharge time, wordline drive strength, and sense amplifier offset. At 5nm/3nm nodes, bitcells shrink to ~0.021 µm²; read current ~10–50 µA, access time sub-1ns, standby leakage ~1–10 nA/cell. Density tops out around 10–15 Mb/mm². SRAM dominates on-chip cache (L1/L2/L3) and register files across CPUs, GPUs, and AI accelerators.

## Competitive landscape

DRAM is the primary competitor for larger working memory: higher density, lower cost per bit, but requires refresh and has ~10× higher latency. Embedded DRAM (eDRAM) splits the difference but adds process complexity. Non-volatile alternatives—eMRAM, ePCM, eFlash—offer zero standby power but lose on write endurance or speed. For AI inference specifically, compute-in-memory (CIM) architectures repurpose SRAM arrays as analog MAC units, directly competing with digital SRAM + separate compute.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
