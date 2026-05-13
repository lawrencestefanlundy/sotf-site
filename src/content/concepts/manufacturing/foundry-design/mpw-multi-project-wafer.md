---
type: concept
slug: mpw-multi-project-wafer
canonical_name: MPW / Multi-Project Wafer
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- foundry-design
related_concepts: []
companies_using:
- ams-osram-formerly-austriamicrosystems
- chipflow
- cmc-microsystems
- cmp-circuits-multi-projets
- efabless
- europractice
- globalfoundries
- ihp-microelectronics
- imec
- leti-cea-leti
- liqtech-formerly-lilas-micro
- mosis-usc-information-sciences-institute
- pragmatic-semiconductor
- quickly-quicklogic-spin-out-concept-silicon-catalyst
- samsung-foundry
- semiwise
- siltectra-fraunhofer-iis
- silterra
- skywater-technology
- tenstorrent
- tower-semiconductor
- tsmc
- x-fab
- zero-asic
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

# MPW / Multi-Project Wafer

*Kind: technology*

## Physics / mechanism

Multi-Project Wafer (MPW) runs multiple chip designs on a single wafer by partitioning the reticle field — typically 26×33 mm for EUV, larger for older nodes — among several customers, each paying a fractional share of mask and fab costs. A full mask set at TSMC N5 runs $5–15M; MPW reduces per-project NRE to $50K–500K depending on process node and die area. Shuttle runs are batched periodically (monthly to quarterly). Key parameters: reticle utilisation, shuttle cadence, PDK access, and test vehicle availability. GF, TSMC, Europractice (imec/IHP), SkyWater, and Tower all run commercial MPW programmes. EDA tool compatibility and DRC sign-off are gating constraints.

## Competitive landscape

Dedicated wafer runs (full production) are the alternative once yield and volume justify it; breakeven typically hits at 5K–50K units depending on die area. ASIC prototyping via PCB + FPGA bridges early feasibility but cannot validate analogue, RF, or photonic performance. SiPh-specific MPW (AIM Photonics, imec, CEA-Leti, Cornerstone) compete with CMOS-node shuttles for photonics teams. Open-source PDKs (SkyWater 130nm, GF 180nm) lower the floor further.

## Cloudberry relevance

| Approach | Cost | Cycle time | Risk |
|---|---|---|---|
| MPW shuttle | $50K–500K | 3–6 months | Medium |
| Full wafer run | $500K–5M+ | 4–9 months | Low (volume) |
| FPGA emulation | $5K–50K | Days–weeks | High (no silicon fidelity) |


MPW is a direct signal filter for portfolio companies: startups that have taped out show hardware conviction and are past simulation-only risk. For GF-LP fund deal-flow, GF's own MPW programme (130nm–45nm CLN, RFSOI, SiPh90) creates a natural pipeline — companies using GF shuttles are already in the ecosystem. Photonics and compound semi startups (relevant to Cloudberry's photonics thesis) depend on AIM and Leti MPW to derisk before Series A. Shuttle history is a useful diligence proxy for execution tempo.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
