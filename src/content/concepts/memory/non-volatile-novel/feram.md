---
type: concept
slug: feram
canonical_name: FeRAM (Ferroelectric)
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
- atomica-formerly-mems-exchange
- cerabyte
- ferroelectric-memory-gmbh-fmc
- fraunhofer-ipms
- fujitsu-semiconductor-memory-solution-fsms
- globalfoundries
- imec
- infineon-technologies
- integrated-silicon-solution-inc-issi
- leti-cea-leti
- microchip-technology
- namlab-ggmbh
- piezoceramics-pi-ceramic
- purdue-quantum-science-and-engineering-institute-pqsei-purdu
- radiant-technologies
- renesas-electronics
- samsung-electronics
- sk-hynix
- stmicroelectronics
- symetrix-corporation
- texas-instruments
- tsmc
- weebit-nano
- xmem-technologies
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

# FeRAM (Ferroelectric)

*Kind: technology*

## Physics / mechanism

Ferroelectric RAM exploits bistable spontaneous polarization in a ferroelectric capacitor—typically PZT (lead zirconate titanate) or HZO (hafnium zirconium oxide)—integrated with a select transistor (1T1C or 1T). Applying a voltage above the coercive field (~1–3 V for HZO) switches polarization state; remnant polarization (Pr ~10–25 µC/cm²) is retained with zero standby power. Read is destructive, requiring a write-back cycle. Key figures: sub-100 ns write, endurance 10⁹–10¹⁴ cycles (HZO-based), data retention >10 years at 85 °C. HZO's CMOS-compatibility (ALD deposition, sub-10 nm films) has re-energized the field after decades of PZT's integration complexity limiting it to niche MCU/IoT (TI, Cypress/Infineon, Fujitsu).

## Competitive landscape

FeRAM competes directly with MRAM, RRAM/ReRAM, and Flash in the embedded NVM segment, plus SRAM for cache-adjacent ultra-low-power applications.

## Cloudberry relevance

| Memory | Write energy | Endurance | CMOS integration |
|---|---|---|---|
| FeRAM (HZO) | ~0.1 pJ/bit | 10¹⁰–10¹⁴ | High (ALD, back-end compatible) |
| MRAM (STT) | ~1–10 pJ/bit | >10¹² | Moderate (dedicated module) |
| RRAM | ~0.1–1 pJ/bit | 10⁶–10⁸ | High but variability risk |

FeFET (gate-stack variant) removes destructive read, compressing cell area further. Adjacent: antiferroelectric (AFE) for energy storage, ferroelectric tunnel junctions for neuromorphic weights.


HZO-based FeRAM sits at the intersection of Cloudberry's three theses: advanced materials (fluorite-structure oxides), semiconductor process integration, and edge AI inference hardware. GlobalFoundries has an active 22FDX eMRAM platform but lacks production FeRAM—a whitespace. Deal-flow angles: HZO materials suppliers, FeFET IP startups, and embedded NVM fabless teams targeting always-on IoT or CIM (compute-in-memory) architectures where MRAM's write energy is prohibitive.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
