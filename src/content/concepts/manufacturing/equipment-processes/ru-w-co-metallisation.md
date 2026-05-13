---
type: concept
slug: ru-w-co-metallisation
canonical_name: Ru / W / Co Metallisation
aliases: []
kind: material
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- equipment-processes
related_concepts: []
companies_using:
- adeia-formerly-xperi-technisat-ip
- air-liquide-advanced-materials
- applied-materials
- beneq
- entegris
- forge-nano
- fraunhofer-iisb
- gelest-a-mitsubishi-chemical-group-company
- imec
- intel
- lam-research
- merck-kgaa-electronics
- micron-technology
- nano-x-nanox-imaging
- picosun-an-applied-materials-company
- rasirc
- samsung-foundry
- sk-hynix
- thin-film-electronics-thinfilm
- tokyo-electron-tel
- tower-semiconductor
- tsmc
- umicore
- versum-materials-now-part-of-merck-kgaa
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

# Ru / W / Co Metallisation

*Kind: material*

## Physics / mechanism

Ru, W, and Co are candidate metals replacing Cu/barrier-stack metallisation at advanced nodes (≤7 nm, trending to 2 nm and below). The driver is resistivity scaling: Cu's effective resistivity rises sharply below ~10 nm linewidth due to surface and grain-boundary scattering (bulk ρ Cu ≈ 1.7 µΩ·cm; at 5 nm half-pitch, effective ρ can exceed 10 µΩ·cm). Ru (bulk ρ ≈ 7.6 µΩ·cm) and Co (ρ ≈ 6.2 µΩ·cm) tolerate dimensional scaling better because they permit thinner or eliminated barrier/liner layers, recovering net resistance. W dominates local interconnect and contacts (high electromigration resistance, CVD-compatible). Key parameters: mean free path, liner thickness, electromigration activation energy. TSMC/Intel/Samsung have deployed Co local interconnects at 10–7 nm; Ru is in active integration for M0/M1 at sub-3 nm.

## Competitive landscape

Cu dominates semi-global and global interconnects and will persist where line dimensions stay above ~15 nm. Mo has emerged as a competing refractory metal (bulk ρ ≈ 5.3 µΩ·cm, strong electromigration performance, IBM/TSMC interest). Graphene and CNT interconnects are research-stage with no near-term HVM path.

## Cloudberry relevance

| Metal | Bulk ρ (µΩ·cm) | Barrier needed | Maturity |
|-------|---------------|---------------|---------|
| Cu | 1.7 | Yes (Ta/TaN) | HVM global |
| Ru | 7.6 | Minimal/none | HVM M0–M1 (3 nm) |
| Mo | 5.3 | Minimal | Pilot (IBM, TSMC) |


GF is a trailing-edge/specialty foundry, but metallisation choices affect every node GF licenses or develops (22FDX, 12LP). Portfolio companies building chiplets, MEMS, or photonic ICs on GF processes face interconnect material constraints directly. Deal-flow angle: ALD precursor suppliers, novel barrier/liner startups, and EDA tooling that models resistivity at advanced nodes. Lunar Ventures' focus on deep-tech seed means early materials-IP plays (precursor chemistry, deposition tools) are natural pipeline.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
