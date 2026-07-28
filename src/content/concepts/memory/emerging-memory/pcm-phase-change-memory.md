---
type: concept
slug: pcm-phase-change-memory
canonical_name: Phase-Change Memory (PCM)
aliases: []
kind: technology
parent_concepts:
- memory
- emerging-memory
related_concepts: []
sources:
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-06-04-q-memory-site]]'
frontier:
- Can PCM drift and endurance be tamed enough for analog-CIM volume, or does it stay a research device?
- Does PCM hold a role as storage-class memory even if PCM-CIM stalls?
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 8
last_reorg_date: '2026-05-14'
sources_7d: 1
sources_30d: 1
recent_mentions:
- slug: 2026-06-04-q-memory-site
  title: Q-Memory — company website (q-memory.tech)
  date: '2026-06-04'
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

Phase-change memory exploits the reversible amorphous↔crystalline transition in chalcogenide alloys—typically Ge₂Sb₂Te₅ (GST) or doped variants. A short high-current pulse (RESET) melts and quench-cools the material into high-resistance amorphous state; a longer lower-current pulse (SET) anneals it into low-resistance crystalline. Resistance contrast runs 10³–10⁴×. Multi-level cell (MLC) operation encodes 2–3 bits per cell by targeting intermediate resistance states. Endurance: 10⁸–10¹² cycles depending on cell architecture. Retention: >10 years at 85 °C for crystalline phase. Leading nodes: Intel/Micron 3D XPoint (now Solidigm), ST Microelectronics automotive PCM, IBM research targeting analogue neuromorphic arrays. Write latency ~100 ns; read ~50 ns—faster than NAND, slower than SRAM/DRAM.

## Competitive landscape

PCM competes directly with NAND Flash (higher endurance, lower density penalty, better random-write), DRAM (lower cost/bit, non-volatile, but slower), and emerging NVM alternatives.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Can PCM drift and endurance be tamed enough for analog-CIM volume, or does it stay a research device?
- Does PCM hold a role as storage-class memory even if PCM-CIM stalls?
