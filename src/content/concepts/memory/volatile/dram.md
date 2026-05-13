---
type: concept
slug: dram
canonical_name: DRAM
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
- astera-labs
- blaize
- corelink-acquired-by-arm-formerly-known-as-independent-ip
- cxmt-changxin-memory-technologies
- elpis-semiconductor
- gigaio
- liqid
- marvell-technology
- memverge
- micron-technology
- montage-technology
- nanya-technology
- peraso-technologies
- rambus
- renesas-electronics
- samsung-electronics
- sk-hynix
- tetragon-fraunhofer-ipms-spin-off
- tetramer-technologies
- weebit-nano
- winbond-electronics
- xitore
- ymtc-yangtze-memory-technologies
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

# DRAM

*Kind: technology*

## Physics / mechanism

DRAM stores each bit as charge on a capacitor paired with an access transistor (1T1C cell). Read is destructive—sense amplifiers detect sub-100 fV charge differentials and rewrite. Refresh cycles every ~64 ms prevent leakage-induced data loss, consuming ~10–15% of active power. DRAM scales via process node and cell capacitance engineering (MIM, MIS, stacked trench). Current SOTA: SK Hynix HBM3E at 1.2 TB/s bandwidth, Samsung DDR5 at 7200 MT/s per pin, 10 nm-class (1β/1γ) nodes. Cell capacitance must hold ~10 fF minimum despite shrinking geometry—the central materials and integration challenge as nodes compress below 10 nm.

## Competitive landscape

DRAM competes directly with SRAM (faster, 6T, no refresh, 50–100× area penalty) and emerging non-volatile alternatives for specific tiers. HBM is DRAM repackaged for AI compute bandwidth. Key competitive pressures come from MRAM (persistent, radiation-hard, latency-competitive but density-limited), FeRAM (low power, niche embedded), and CXL-attached DRAM pools blurring memory-storage boundaries.

## Cloudberry relevance

| Technology | Density | Latency | Non-volatile |
|---|---|---|---|
| DRAM | High | ~50–100 ns | No |
| SRAM | Low | <1 ns | No |
| MRAM | Medium | ~3–10 ns | Yes |


DRAM's scaling wall—capacitor dielectric, access transistor leakage, refresh power—generates deal flow in novel dielectrics (high-k, ferroelectric), 3D integration schemes, and CIM (compute-in-memory) architectures. GlobalFoundries doesn't chase leading-edge DRAM but embedded DRAM IP (eDRAM) in specialty nodes is relevant. Cloudberry-relevant angles: materials enablers (ALD dielectrics, novel capacitor stacks), DRAM-adjacent CXL memory controllers, and photonic interconnects resolving HBM bandwidth bottlenecks in AI accelerator stacks.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
