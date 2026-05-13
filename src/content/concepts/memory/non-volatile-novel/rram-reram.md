---
type: concept
slug: rram-reram
canonical_name: RRAM / ReRAM
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
- 4ds-memory
- adesto-technologies-now-dialogrenesas
- applied-brain-research
- avalanche-technology
- cerfe-labs
- corelink-wuhan-xinxin-xmc
- crossbar-inc
- ememory-technology
- gigpeak-now-integrated-device-technologyrenesas
- gyrfalcon-technology
- imec
- intel
- macronix-international
- micron-technology
- nantero
- panasonic-semiconductor-solutions
- rain-neuromorphics
- samsung-electronics
- silicon-storage-technology-sst-microchip
- sk-hynix
- syntiant
- tsmc
- weebit-nano
- winbond-electronics
- ynvisible-interactive
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

# RRAM / ReRAM

*Kind: technology*

## Physics / mechanism

Resistive RAM stores data by switching a thin dielectric (typically HfO₂, TaO_x, or Al₂O₃) between high-resistance (HRS) and low-resistance (LRS) states via controlled filament formation and rupture. An applied voltage drives oxygen vacancy migration, forming or dissolving a conductive filament—SET operation ~1 V, RESET ~1–2 V, switching <10 ns, endurance 10⁶–10¹² cycles depending on material stack. Retention >10 years at 85 °C for mature nodes. Cell area as small as 4F². Multi-level cell (MLC) operation enables 2–3 bits/cell. Leading process nodes: TSMC 28 nm embedded RRAM in production; GlobalFoundries exploring integration at 22FDX. Key players: Weebit Nano, Crossbar, CXMT, Ememory, Panasonic.

## Competitive landscape

RRAM competes primarily with embedded Flash (eFlash), MRAM, and PCM for NVM applications.

## Cloudberry relevance

| Technology | Write energy | Endurance | CMOS compatibility |
|---|---|---|---|
| RRAM | ~10 fJ/bit | 10⁶–10¹² | High (BEOL) |
| eFlash | ~10 pJ/bit | 10⁵–10⁶ | Moderate (specialized implants) |
| MRAM (STT) | ~100 fJ/bit | >10¹² | High (BEOL) |

PCM offers better MLC but higher write current. RRAM's BEOL integration is its structural advantage over eFlash below 28 nm. Adjacent use cases: compute-in-memory (CIM) arrays, neuromorphic weight storage, PUF security primitives.


GF's 22FDX platform is a direct hook—embedded RRAM at FD-SOI is a differentiated offering for IoT, automotive, and edge-AI chips where eFlash scaling has stalled. Deal-flow angles: fabless startups building CIM or neuromorphic silicon that need a non-volatile weight store, materials companies developing alternative oxide stacks, and EDA/IP vendors targeting RRAM bitcell compilers. Weebit Nano's licensing model is the archetype to track.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
