---
type: concept
slug: hbm
canonical_name: HBM (High-Bandwidth Memory)
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

HBM stacks multiple DRAM dies vertically, connected through silicon via (TSV) arrays, then packages the stack alongside a logic die on a silicon interposer using 2.5D integration. The short TSV interconnects replace long PCB traces, slashing latency and energy per bit. Bandwidth scales with the number of TSV channels × bus width × data rate. HBM3e (current production, SK Hynix / Samsung / Micron) delivers ~1.2 TB/s per stack at 8-Hi configuration; a single H100 carries six stacks for ~3.35 TB/s aggregate. Capacity per stack has reached 36 GB (12-Hi HBM3e). Power efficiency: ~3–4 pJ/bit vs ~15 pJ/bit for GDDR6.

## Competitive landscape

LPDDR5X is the nearest substitute for edge-AI applications where cost dominates over bandwidth. GDDR7 (Micron/Samsung) closes the bandwidth gap at lower packaging cost but loses on capacity density. SRAM remains faster but ~50× larger per bit. CXL-attached DRAM (pooled memory architectures) threatens HBM at datacenter scale if latency tolerance improves. Competitor matrix:

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
