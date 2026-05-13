---
type: concept
slug: pcm-phase-change-memory
canonical_name: Phase-Change Memory (PCM)
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
- aixtron
- atomera
- cerfe-labs
- enlightra
- entegris
- everspin-technologies
- gyrfalcon-technology
- ibm-research
- intel
- intermolecular
- kioxia
- macronix-international
- microchip-technology
- micron-technology
- nantero
- ovonyx-memory-technology
- phaseshift-technologies
- samsung-electronics
- sk-hynix
- stmicroelectronics
- weebit-nano
- western-digital
- xitore
- yangtze-memory-technologies-ymtc
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

# Phase-Change Memory (PCM)

*Kind: technology*

## Physics / mechanism

Phase-change memory exploits the reversible amorphous↔crystalline transition in chalcogenide alloys—typically Ge₂Sb₂Te₅ (GST) or doped variants. A short high-current pulse (RESET) melts and quench-cools the material into high-resistance amorphous state; a longer lower-current pulse (SET) anneals it into low-resistance crystalline. Resistance contrast runs 10³–10⁴×. Multi-level cell (MLC) operation encodes 2–3 bits per cell by targeting intermediate resistance states. Endurance: 10⁸–10¹² cycles depending on cell architecture. Retention: >10 years at 85 °C for crystalline phase. Leading nodes: Intel/Micron 3D XPoint (now Solidigm), ST Microelectronics automotive PCM, IBM research targeting analogue neuromorphic arrays. Write latency ~100 ns; read ~50 ns—faster than NAND, slower than SRAM/DRAM.

## Competitive landscape

PCM competes directly with NAND Flash (higher endurance, lower density penalty, better random-write), DRAM (lower cost/bit, non-volatile, but slower), and emerging NVM alternatives.

## Cloudberry relevance

| Technology | Endurance | Non-volatile | Density | Key risk |
|---|---|---|---|---|
| PCM | 10⁸–10¹² | Yes | ~F²/4 | RESET current, drift |
| RRAM/OxRAM | 10⁶–10¹⁰ | Yes | ~4F² | Variability |
| MRAM (STT) | >10¹⁵ | Yes | ~20F² | Cost/bit |

Adjacent: optical PCM (same material, photonic switching—Bodle Technologies, Salience Labs), in-memory compute using analogue resistance states, selector device co-integration.


PCM sits at the intersection of advanced materials, fab process integration, and memory architecture—exactly Cloudberry's stack. GlobalFoundries runs embedded NVM programmes where PCM is a qualified option for automotive and edge-AI nodes; deal-flow angle is fabless IP or materials startups targeting GF's 22FDX/12LP+ qualification paths. Optical PCM is a direct photonics adjacency—companies developing PCM-based photonic switching or in-memory inference are credible Cloudberry targets. Watch selector-device and GST-replacement materials (Sb₂Se₃, AIST alloys) as upstream material bets.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
