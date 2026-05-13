---
type: concept
slug: cowos
canonical_name: CoWoS (TSMC)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- packaging
related_concepts: []
companies_using:
- alphawave-semi
- amd
- ase-group-advanced-semiconductor-engineering
- besi-be-semiconductor-industries
- broadcom
- celestial-ai
- cerebras-systems
- d-matrix
- eliyan
- groq
- ibiden
- intel
- kandou-bus
- marvell-technology
- micron-technology
- nvidia
- onto-innovation
- rivos
- samsung-semiconductor
- shin-etsu-chemical
- simaai
- sk-hynix
- tsmc
- unimicron
- untether-ai
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

# CoWoS (TSMC)

*Kind: technology*

## Physics / mechanism

CoWoS (Chip-on-Wafer-on-Substrate) is TSMC's mature 2.5D advanced packaging platform. A silicon interposer (passive or active) is fabricated on a standard wafer, then known-good dies—logic, HBM, SerDes chiplets—are flip-chip bonded onto it before dicing and substrate attachment. The interposer provides ultra-fine RDL wiring (≤0.4 µm line/space in CoWoS-S) and microbumps at ~40–55 µm pitch, enabling die-to-die bandwidth densities impossible on organic substrates. HBM3/3E stacks connected via CoWoS deliver ~1.2 TB/s per stack. Interposer sizes have scaled to ~120 mm × 120 mm (reticle-stitched) to accommodate multi-chiplet AI accelerators. CoWoS-R replaces the passive Si interposer with an RDL-only interposer; CoWoS-L embeds a bridge die for heterogeneous integration. TSMC's CoWoS capacity was ~13,000 wspm in 2023, scaling aggressively under AI demand pressure.

## Competitive landscape

| Platform | Interposer type | Bump pitch | Key user |
|---|---|---|---|
| CoWoS-S | Passive Si | ~40 µm | NVIDIA H/B series |
| Intel EMIB | Si bridge embedded in organic | ~55 µm | Intel Ponte Vecchio |
| ASE/Amkor FOCoS | Fan-out RDL | ~100–130 µm | Broader merchant |

## Cloudberry relevance

Samsung SF-FOWLP and Nepes RDL interposers compete at lower cost. OSAT players (ASE, Amkor) close the gap on yield but lag on interconnect density. Intel's EMIB avoids full interposer cost but limits bandwidth scaling.

CoWoS is a forcing function on upstream supply: silicon interposer blanks, high-purity quartz, specialty dielectrics, underfill chemistries, and HBM substrate laminate are all capacity-constrained. Cloudberry's advanced-materials and photonics angles surface deals in photonic interposers (replacing electrical RDL with Si-photonics layers), novel low-k dielectrics, and precision metrology for bump inspection—none of which TSMC verticalises. GF's role as an interposer fab (mature node silicon) is a direct LP-context thread worth tracking.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
