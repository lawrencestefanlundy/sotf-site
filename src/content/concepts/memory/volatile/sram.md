---
type: concept
slug: sram
canonical_name: SRAM
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- memory
- volatile
related_concepts: []
companies_using:
- alliance-memory
- andes-technology
- arm
- axelera-ai
- brainchip-holdings
- cadence-design-systems
- cypress-semiconductor-infineon
- ememory-technology
- greenwaves-technologies
- gsi-technology
- hailo-technologies
- integrated-silicon-solution-inc-issi
- microchip-technology
- morikatron-morikaai
- movellus
- recogni
- renesas-electronics
- samsung-semiconductor
- silicon-storage-technology-microchipsst
- sk-hynix
- surecore
- synopsys
- syntiant
- tsmc
- weebit-nano
ideas_referencing: []
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

# SRAM

*Kind: technology*

## Physics / mechanism

Six-transistor (6T) SRAM stores one bit in a cross-coupled inverter pair (two PMOS loads, two NMOS drivers) stabilised by two access transistors. No refresh required; data persists as long as power is supplied. Read/write speed is determined by bitline precharge time, wordline drive strength, and sense amplifier offset. At 5nm/3nm nodes, bitcells shrink to ~0.021 µm²; read current ~10–50 µA, access time sub-1ns, standby leakage ~1–10 nA/cell. Density tops out around 10–15 Mb/mm². SRAM dominates on-chip cache (L1/L2/L3) and register files across CPUs, GPUs, and AI accelerators.

## Competitive landscape

DRAM is the primary competitor for larger working memory: higher density, lower cost per bit, but requires refresh and has ~10× higher latency. Embedded DRAM (eDRAM) splits the difference but adds process complexity. Non-volatile alternatives—eMRAM, ePCM, eFlash—offer zero standby power but lose on write endurance or speed. For AI inference specifically, compute-in-memory (CIM) architectures repurpose SRAM arrays as analog MAC units, directly competing with digital SRAM + separate compute.

## Cloudberry relevance

| Memory | Density (relative) | Speed | Volatile |
|--------|-------------------|-------|----------|
| SRAM | 1× | ~1 ns | Yes |
| DRAM | 8–16× | ~10 ns | Yes |
| eMRAM | 4–6× | ~10 ns | No |


SRAM scaling is a known inflection point at sub-5nm: yield and bitcell stability drive wafer costs at GF's 12LP+ and 12nm nodes, which are Cloudberry's manufacturing adjacency. Startups building AI edge accelerators, photonic ASICs requiring embedded memory, or novel CIM architectures all have SRAM density/power as a hard design constraint—making it a recurring technical diligence question and a signal for IP moats in Lunar/Cloudberry deal flow.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
