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
sources:
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2024-yole-emerging-memories-2024]]'
- '[[2026-06-22-beyond-cmos-device-layer-research]]'
- '[[2026-04-29-optical-dram-everspin-reports-q1-2026-financial-results]]'
- '[[2026-06-04-globalfoundries-emram-22fdx-availability]]'
frontier:
- Does any MRAM-CIM (in-array compute) reach product, or does MRAM stay a cache / eNVM device?
- How far does eMRAM displace eFlash at advanced nodes?
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 46
last_reorg_date: '2026-05-14'
sources_7d: 1
sources_30d: 2
recent_mentions:
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-04-globalfoundries-emram-22fdx-availability
  title: GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform
  date: '2026-06-04'
  kind: web
- slug: 2026-04-29-optical-dram-everspin-reports-q1-2026-financial-results
  title: Everspin Reports Q1 2026 Financial Results
  date: '2026-04-29'
  kind: web
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
- slug: 2024-yole-emerging-memories-2024
  title: Yole Group — Emerging Non-Volatile Memories 2024
  date: '2024-10-15'
  kind: web
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
- slug: 2023-06-23-e05-the-future-of-edge-ai-brain-inspired
  title: '🔮 E05: Neuromorphic Computing & The Future of Edge AI'
  date: '2023-06-23'
  kind: substack
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

- Does any MRAM-CIM (in-array compute) reach product, or does MRAM stay a cache / eNVM device?
- How far does eMRAM displace eFlash at advanced nodes?

## Merged from root duplicate (mram.md at concepts/ root, 2026-06-10)

# MRAM (Magnetoresistive RAM)

Non-volatile memory that stores bits in the magnetisation of a magnetic tunnel junction. STT-MRAM (spin-transfer torque) and SOT-MRAM (spin-orbit torque) are the leading embedded-NVM candidates to displace eFlash at advanced nodes for MCU and last-level-cache use. One cohort in the **Emerging Nvm** race alongside ferroelectric (FeRAM/FeFET) and ReRAM.
