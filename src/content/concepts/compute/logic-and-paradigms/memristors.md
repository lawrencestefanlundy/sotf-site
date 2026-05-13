---
type: concept
slug: memristors
canonical_name: Memristors
aliases: []
kind: material
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- logic-and-paradigms
related_concepts: []
companies_using:
- 4ds-memory
- adesto-technologies-acquired-by-dialog-semiconductor-renesas
- ambiq-micro
- axon-technologies
- cerfe-labs
- corelink-acquired-path-via-arm-ecosystem
- crossbar-inc
- globalfoundries
- imec
- infineon-technologies
- innodata-memory
- intrinsic-semiconductor-technologies
- knowm-inc
- macronix-international
- memryx
- nantero
- neural-semiconductor
- panasonic-holdings
- rain-neuromorphics
- resistive-memory-technologies-rmt
- tetramem
- weebit-nano
- winbond-electronics
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- material
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Memristors

*Kind: material*

## Physics / mechanism

Memristors are two-terminal passive devices whose resistance depends on the history of current or voltage applied — resistance is non-volatile state. The dominant physical mechanisms are filamentary conductive-bridge RAM (CBRAM, ionic metal migration) and valence-change memory (VCM, oxygen vacancy filament modulation), plus phase-change and ferroelectric variants. Key parameters: switching speed (sub-10 ns demonstrated), endurance (10⁶–10⁸ cycles for HfOₓ VCM), retention (>10 years at 85 °C), on/off ratio (10²–10⁴), and multi-level cell (MLC) programmability (3–4 bits/cell demonstrated in research). State of the art: TSMC and GlobalFoundries both offer embedded RRAM (1T1R) in 22–28 nm nodes for MCU/IoT NVM; crossbar arrays at 4 F² density are production-feasible. The fundamental appeal is CMOS back-end integration — no new fab infrastructure required beyond dielectric stack tuning.

## Competitive landscape

The primary NVM competitors are embedded Flash (eFlash) and embedded MRAM (STT-MRAM). eFlash is mature but hits a wall below 28 nm due to tunnel oxide scaling. STT-MRAM offers faster write and better endurance but higher write current density and process complexity. PCM (phase-change) competes for storage-class memory at higher density. Neuromorphic-specific competition comes from SRAM-based analog compute-in-memory and ferroelectric FETs (FeFETs). CBRAM trails VCM on endurance; VCM trails PCM on MLC precision.

## Cloudberry relevance

| Technology | Endurance | Write energy | CMOS integration |
|---|---|---|---|
| RRAM/VCM | 10⁶–10⁸ | ~0.1 pJ | Back-end, straightforward |
| STT-MRAM | >10¹⁰ | ~1–10 pJ | Back-end, high current |
| PCM | ~10⁸ | ~10–100 pJ | Back-end, thermal budget risk |


GF's 22FDX and 12LP+ platforms already support embedded RRAM qualification paths — direct deal-flow relevance for startups building edge-AI inference chips, secure MCUs, or CIM (compute-in-memory) accelerators fabbing at GF. Cloudberry's materials + semiconductor angle makes sense for companies differentiating at the dielectric stack level (HfOₓ doping, bilayer oxides). Watch neuromorphic compute startups and IoT secure-element plays needing NVM density beyond eFlash. Lunar Ventures' software-adjacent portfolio adds context where memristive CIM reduces memory-bandwidth bottleneck in inference hardware.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
