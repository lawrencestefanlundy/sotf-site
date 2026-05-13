---
type: concept
slug: diffusion-barriers
canonical_name: Diffusion Barriers (TiN, TaN)
aliases: []
kind: material
domain:
- cloudberry
- sotf
parent_concepts:
- materials
- coatings-interfaces
related_concepts: []
companies_using:
- adeka-corporation
- air-liquide-advanced-materials
- applied-materials
- asm-international
- atomic-fabless-atfl
- beneq
- chemically-speaking-chem-say
- entegris
- eugenus
- forge-nano
- fraunhofer-ipms
- intel
- lam-research
- merck-kgaa-electronics
- micron-technology
- nata-semiconductor-materials
- picosun-ikea-group-okmetic
- resonac-formerly-showa-denko
- samsung-semiconductor
- sige-semiconductor-tower-semiconductor
- sk-hynix
- smic-semiconductor-manufacturing-international
- tokyo-electron-tel
- tsmc
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


# Diffusion Barriers (TiN, TaN)

*Kind: material*

## Physics / mechanism

TiN and TaN are refractory metal nitrides deposited by PVD or ALD as thin films (2–10 nm typical) between copper interconnects and surrounding dielectrics or silicon. Their function is kinetic: they present a thermodynamically unfavorable diffusion path for Cu atoms, which would otherwise migrate into SiO₂ or low-k dielectrics and create trap states or junction leakage. TaN is preferred at the seed-layer interface (better adhesion to Cu); TiN dominates gate and contact applications. Resistivity runs 50–200 µΩ·cm depending on stoichiometry and deposition conditions. ALD enables conformal coverage into high-aspect-ratio vias at sub-3 nm nodes; thickness control below 1 nm is now production-relevant. Key failure mode is pinhole formation at ultrathin regimes, driving research into amorphous alternatives.

## Competitive landscape

TiN/TaN face substitution pressure from three directions. Ruthenium liners (used by Intel at sub-5 nm) offer lower resistivity and direct-plate Cu without a seed layer. Cobalt fill eliminates the barrier/seed stack entirely for narrow lines but has electromigration limits. Manganese self-forming barriers (diffusion from CuMn alloy) are low-volume but eliminate deposition steps entirely.

## Cloudberry relevance

| Approach | Resistivity | Node fit | Process complexity |
|---|---|---|---|
| TaN/TiN (ALD) | 100–200 µΩ·cm | 5 nm–28 nm | Low |
| Ru liner | 7 µΩ·cm | <5 nm | Medium |
| Self-forming MnSiO₃ | N/A | 10–22 nm | Low |


GlobalFoundries remains a major TiN/TaN consumer across its 12LP, 22FDX, and GF45RFSOI platforms—relevant context for any materials supplier Cloudberry evaluates. Deal-flow angles: ALD precursor chemistry startups pushing conformality at aspect ratios >10:1; barrier metrology tools (XRF, in-line TEM) enabling tighter process control; and alternative liner materials targeting GF's photonics and RF nodes where parasitic resistance in contact stacks directly degrades device performance.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
