---
type: concept
slug: ferroelectric-hfo2
canonical_name: Ferroelectric HfO2
aliases: []
kind: material
domain:
- cloudberry
- sotf
parent_concepts:
- materials
- functional-layers
related_concepts: []
companies_using:
- applied-materials
- cerfe-labs
- dielectric-labs-dli
- emergence-memory
- entegris
- ferroelectric-memory-company-fmc
- forge-nano
- fraunhofer-ipms
- globalfoundries
- infineon-technologies
- insight-monolithics
- intel
- lam-research
- micron-technology
- namlab
- renesas-electronics
- samsung-electronics
- sk-hynix
- symetrix-corporation
- texas-instruments
- tsmc
- weebit-nano
- winbond-electronics
- ymtc-yangtze-memory-technologies
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

# Ferroelectric HfO2

*Kind: material*

## Physics / mechanism

Hafnium oxide (HfO₂) becomes ferroelectric when doped (Si, Al, Y, Zr) and deposited as thin films (<10 nm), stabilising the orthorhombic phase (Pca2₁) rather than the paraelectric monoclinic ground state. Spontaneous polarisation (Ps) runs 10–30 µC/cm², coercive field ~1–2 MV/cm, endurance 10⁹–10¹² cycles depending on stack engineering. Critical advantage: full CMOS compatibility at standard gate-stack temperatures (400–500 °C) and sub-10 nm thickness scalability — properties legacy ferroelectrics (PZT, SBT) cannot match. Wake-up and imprint remain reliability challenges. State of art: GlobalFoundries, TSMC, and Samsung have integrated Hf₀.₅Zr₀.₅O₂ (HZO) into embedded FRAM and FeFET nodes at 22–28 nm.

## Competitive landscape

HfO₂ ferroelectrics compete directly with SRAM, eFlash, and MRAM for embedded NVM. Charge-trap flash (CTF) occupies overlapping density/cost space but lacks sub-ns write speed. FeRAM using PZT offers higher Ps but fails CMOS integration rules. MRAM (STT, SOT) competes on endurance and speed but carries higher process complexity and cost. FTJ (ferroelectric tunnel junction) devices using the same HZO stack represent an adjacent neuromorphic angle.

## Cloudberry relevance

| Technology | CMOS compatible | Thickness | Endurance |
|---|---|---|---|
| HfO₂ FeFET/FeRAM | Yes | <10 nm | 10¹⁰–10¹² |
| PZT FeRAM | No | >50 nm | 10¹² |
| STT-MRAM | Yes | ~5 nm | >10¹² |

GlobalFoundries' 22FDX platform already ships embedded HZO-based NVM, making this directly relevant to GF-LP fund deal flow. Portfolio targets: IP licensors building FeFET compiler IP, materials suppliers optimising HZO ALD precursors, and fabless teams designing edge-AI inference chips exploiting in-memory compute on FeFET arrays. Lunar Ventures' early-stage mandate fits seed-stage FeTJ neuromorphic or CIM startups before GF process design kits formalise the integration path.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
