---
type: concept
slug: storage-class-memory
canonical_name: Storage-Class Memory
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- memory
- non-volatile-novel
related_concepts: []
companies_using:
- avalanche-technology
- axbit-formerly-axel-technology
- corelink-smart-semiconductor
- crossbar
- enfabrica
- everspin-technologies
- gyrfalcon-technology
- hyperstone
- intel
- kioxia-solid-state-storage-technology-ssstc
- kioxia
- marvell-technology
- memverge
- micron-technology
- montage-technology
- nantero
- numem
- phison-electronics
- piecemakers-technology
- samsung-electronics
- scaleflux
- sk-hynix
- tetramem
- weebit-nano
- western-digital
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Storage-Class Memory

*Kind: technology*

## Physics / mechanism

Storage-class memory (SCM) occupies the latency gap between DRAM (~100 ns, volatile) and NAND flash (~100 µs, persistent). The goal: byte-addressable, non-volatile memory on the CPU memory bus. Intel Optane (3D XPoint, retired 2022) was the canonical implementation — phase-change-like material switching between amorphous/crystalline states, achieving ~300 ns read latency and ~10 GB/s bandwidth at ~3–4× DRAM cost/GB. Current contenders use resistive switching (ReRAM/RRAM), spin-torque transfer (STT-MRAM), or ferroelectric capacitors (FeRAM/FeFET). MRAM is the most commercially mature: Everspin ships DDR4-compatible MRAM at 1–2 Gb density. The field is constrained by the endurance/density/speed trilemma — no single material cleanly wins all three.

## Competitive landscape

The primary competition is DRAM + NVMe SSD tiering managed in software (e.g., CXL memory pooling, Linux tiered memory). CXL 3.0 increasingly renders SCM's architectural argument addressable without new materials. Adjacent approaches include eDRAM (on-package volatile cache), HBM (high bandwidth, still volatile), and compute-in-memory arrays targeting inference workloads rather than storage hierarchy.

## Cloudberry relevance

| Technology | Latency | Non-volatile | Endurance (writes) |
|---|---|---|---|
| STT-MRAM | ~10 ns | Yes | >10¹² |
| ReRAM | ~100 ns | Yes | ~10⁸–10¹⁰ |
| 3D NAND | ~100 µs | Yes | ~10³–10⁵ |


Cloudberry relevance sits at the materials and fab process layer. SCM requires novel thin-film deposition (HfO₂ for FeFET, MTJ stacks for MRAM) — directly in GlobalFoundries' specialty process roadmap. GF offers MRAM on 22FDX; startups differentiating on switching material or selector device are natural deal-flow. Lunar Ventures' software-layer bets on CXL memory disaggregation are the adjacent thesis — SCM hardware and CXL software are complementary positions across the memory hierarchy stack.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
