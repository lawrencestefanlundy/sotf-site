---
type: concept
slug: nand-flash
canonical_name: NAND Flash
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

NAND flash stores data as charge in floating-gate or charge-trap transistors stacked in 3D arrays (3D NAND). Each cell holds 1–4 bits (SLC/MLC/TLC/QLC) by controlling discrete threshold-voltage states. Tunneling oxide thickness (~7–10 nm) governs endurance (P/E cycles: SLC ~100k, QLC ~1k) and retention (10-year spec at 40°C). Leading-edge nodes stack 200–300+ layers (Samsung V-NAND, SK Hynix, Micron). Raw bit density exceeds 10 Tb/in². Controllers manage ECC, wear-leveling, and FTL. Interface: NVMe/PCIe Gen5 for enterprise SSDs, pushing sequential read >14 GB/s at sub-20 µs latency.

## Competitive landscape

NAND competes directly with NOR flash (lower density, byte-addressable, dominates code storage / MCU boot), DRAM (volatile, 10× faster, 10× costlier/bit), and emerging non-volatile memories targeting the gap between them.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
