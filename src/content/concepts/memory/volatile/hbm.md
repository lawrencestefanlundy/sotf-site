---
type: concept
slug: hbm
canonical_name: HBM (High-Bandwidth Memory)
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
- alphawave-semi
- amd
- astera-labs
- axelera-ai
- broadcom
- cadence-design-systems
- cxmt-changxin-memory-technologies
- eliyan
- enfabrica
- groq
- intel
- kandou-bus
- marvell-technology
- micron-technology
- montage-technology
- nvidia
- rain-ai
- rambus
- rebellions
- samsung-semiconductor
- sk-hynix
- synopsys
- tenstorrent
- tetramer-technologies
- tsmc
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

# HBM (High-Bandwidth Memory)

*Kind: technology*

## Physics / mechanism

HBM stacks multiple DRAM dies vertically, connected through silicon via (TSV) arrays, then packages the stack alongside a logic die on a silicon interposer using 2.5D integration. The short TSV interconnects replace long PCB traces, slashing latency and energy per bit. Bandwidth scales with the number of TSV channels × bus width × data rate. HBM3e (current production, SK Hynix / Samsung / Micron) delivers ~1.2 TB/s per stack at 8-Hi configuration; a single H100 carries six stacks for ~3.35 TB/s aggregate. Capacity per stack has reached 36 GB (12-Hi HBM3e). Power efficiency: ~3–4 pJ/bit vs ~15 pJ/bit for GDDR6.

## Competitive landscape

LPDDR5X is the nearest substitute for edge-AI applications where cost dominates over bandwidth. GDDR7 (Micron/Samsung) closes the bandwidth gap at lower packaging cost but loses on capacity density. SRAM remains faster but ~50× larger per bit. CXL-attached DRAM (pooled memory architectures) threatens HBM at datacenter scale if latency tolerance improves. Competitor matrix:

## Cloudberry relevance

| Technology | Bandwidth (per device) | Capacity | $/GB |
|---|---|---|---|
| HBM3e | ~1.2 TB/s | up to 36 GB | ~$10–15 |
| GDDR7 | ~1.5 TB/s (aggregate) | 32 GB | ~$3–5 |
| LPDDR5X | ~68 GB/s | 64 GB | ~$2–4 |


HBM is the primary bottleneck and margin pool in AI accelerator BoM — whoever controls interposer real estate and advanced packaging controls system economics. GF is not in leading-edge DRAM, but the interposer, embedded silicon bridge, and advanced packaging layers are relevant process bets. Deal-flow angles: interposer IP, photonic integration replacing copper TSV signalling, and chiplet substrate materials where Cloudberry's materials thesis intersects directly.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
