---
type: concept
slug: feram
canonical_name: FeRAM (Ferroelectric)
aliases: []
kind: technology
parent_concepts:
- memory
- mainstream-memory
related_concepts: []
sources:
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
frontier:
- Can HfO2 FeRAM / FeCAP endurance and retention reach DRAM-replacement bars (FMC DRAM+)?
- Does FeCAP-based compute become a credible memcapacitor competitor?
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 126
last_reorg_date: '2026-05-14'
descendants:
- fefet
sources_7d: 8
sources_30d: 28
recent_mentions:
- slug: 2025-26-lapedus-next-gen-ferroelectric-memory
  title: Next-Gen Ferroelectric Memory Still A Work In Progress
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
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
neighbors: []
---
## Physics / mechanism

Ferroelectric RAM exploits bistable spontaneous polarization in a ferroelectric capacitor—typically PZT (lead zirconate titanate) or HZO (hafnium zirconium oxide)—integrated with a select transistor (1T1C or 1T). Applying a voltage above the coercive field (~1–3 V for HZO) switches polarization state; remnant polarization (Pr ~10–25 µC/cm²) is retained with zero standby power. Read is destructive, requiring a write-back cycle. Key figures: sub-100 ns write, endurance 10⁹–10¹⁴ cycles (HZO-based), data retention >10 years at 85 °C. HZO's CMOS-compatibility (ALD deposition, sub-10 nm films) has re-energized the field after decades of PZT's integration complexity limiting it to niche MCU/IoT (TI, Cypress/Infineon, Fujitsu).

## Competitive landscape

FeRAM competes directly with MRAM, RRAM/ReRAM, and Flash in the embedded NVM segment, plus SRAM for cache-adjacent ultra-low-power applications.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Can HfO2 FeRAM / FeCAP endurance and retention reach DRAM-replacement bars (FMC DRAM+)?
- Does FeCAP-based compute become a credible memcapacitor competitor?
