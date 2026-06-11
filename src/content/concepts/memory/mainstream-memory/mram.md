---
type: concept
slug: mram
canonical_name: MRAM (STT/SOT-MRAM)
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

Magnetic RAM stores bits via the magnetization orientation of a magnetic tunnel junction (MTJ): a fixed reference layer and a free layer separated by an MgO tunnel barrier. **STT-MRAM** (spin-transfer torque) switches the free layer by passing a spin-polarized current through the MTJ; switching current ~100 µA, write time ~10 ns, endurance >10¹² cycles. **SOT-MRAM** (spin-orbit torque) decouples read/write paths via a heavy-metal (W, Ta, Pt) spin Hall channel, cutting write current ~3× and improving endurance. Retention: ~10 years at 85 °C for embedded nodes. TSMC, GlobalFoundries, Samsung, and Everspin have qualified embedded STT-MRAM at 22–40 nm; SOT remains mostly pre-production.

## Competitive landscape

STT-MRAM competes directly with eFlash (dominant embedded NVM below 28 nm, but scaling-limited), SRAM (as last-level cache replacement), and FeRAM/FRAM (lower endurance, niche). SOT targets SRAM-class latency (<1 ns write claimed in research). PCM (Intel Optane, now discontinued) competed at storage-class tier. Emerging competition includes FeFET (TSMC, Globalfoundries roadmaps) which offers smaller cell size but inferior endurance data at scale.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*

## Merged from root duplicate (mram.md at concepts/ root, 2026-06-10)

# MRAM (Magnetoresistive RAM)

Non-volatile memory that stores bits in the magnetisation of a magnetic tunnel junction. STT-MRAM (spin-transfer torque) and SOT-MRAM (spin-orbit torque) are the leading embedded-NVM candidates to displace eFlash at advanced nodes for MCU and last-level-cache use. One cohort in the **Emerging Nvm** race alongside ferroelectric (FeRAM/FeFET) and ReRAM.
