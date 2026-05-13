---
type: concept
slug: ald-atomic-layer-deposition
canonical_name: ALD (Atomic Layer Deposition)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- equipment-processes
related_concepts: []
companies_using:
- adnano-technologies
- air-liquide-advanced-materials-voltaix
- applied-materials
- asm-international
- atlant-3d
- beneq
- dnf-co
- encapsulix
- forge-nano-europe-ald-nanosolutions
- forge-nano
- jusung-engineering
- lam-research
- lotus-applied-technology
- merck-kgaa-electronics-division
- nuflare-technology
- oxford-instruments
- picosun-now-part-of-applied-materials
- plasma-therm
- rasirc
- strem-chemicals-ascensus-specialties
- tokyo-electron-tel
- veeco-instruments
- wonik-ips
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

# ALD (Atomic Layer Deposition)

*Kind: technology*

## Physics / mechanism

ALD deposits material one atomic monolayer at a time via sequential, self-limiting surface reactions. A precursor gas chemisorbs onto the substrate; excess is purged; a co-reactant (oxidant, plasma, or reducing agent) reacts with the chemisorbed layer; excess purged again. One cycle = ~0.1–2 Å growth. Self-limiting nature gives exceptional conformality (>99% step coverage in high-aspect-ratio structures) and sub-Ångström thickness control. Typical cycle times 0.5–5 s; throughput is the main industrial constraint. Key materials: Al₂O₃, HfO₂, TiN, ZnO, Ru. State-of-the-art tools (ASM, Lam, Tokyo Electron) run spatial or plasma-enhanced ALD at wafer scales; EUV underlayers and gate dielectrics at <2 nm nodes are ALD-dependent.

## Competitive landscape

CVD is the primary alternative—higher throughput, lower conformality, worse thickness control. PVD (sputtering) is faster still but line-of-sight limited, useless for deep trenches. Wet chemical routes (sol-gel, electrodeposition) are cheaper but lack monolayer precision. Molecular beam epitaxy offers crystalline quality but is vacuum-intensive and slow. Area-selective ALD (AS-ALD) is an emerging adjacent that adds patterning functionality, competing with litho-etch steps. Key vendors: ASM International (dominant), Applied Materials, Lam Research, Picosun (AMAT-acquired), Forge Nano (nanoparticle coating niche).

## Cloudberry relevance

| Technique | Conformality | Thickness control | Throughput |
|-----------|-------------|------------------|------------|
| ALD | >99% | Sub-Å | Low |
| CVD | 70–90% | ~nm | High |
| PVD | Poor | ~nm | Very high |


ALD is infrastructure for every advanced node GlobalFoundries pursues—gate dielectrics, diffusion barriers, optical thin films for photonics PICs, ferroelectric HZO in Radiant's FeRAM. Deal-flow angles: equipment startups attacking throughput bottlenecks (spatial ALD, roll-to-roll), precursor chemistry companies enabling new material sets (Ru, Mo, 2D-material seeds), and AS-ALD firms reducing patterning costs. Advanced packaging and chiplet integration are pulling ALD into new substrate geometries—watch encapsulation and interposer plays.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
