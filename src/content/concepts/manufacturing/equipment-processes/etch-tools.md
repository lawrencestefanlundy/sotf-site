---
type: concept
slug: etch-tools
canonical_name: Etch Tools (ALE, plasma etch)
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
- advanced-micro-fabrication-equipment-amec
- applied-materials
- atomica-formerly-imec-spin-off
- corial-a-veeco-company
- forge-nano
- hitachi-high-tech
- inx-international-ips-ion-plasma-etch-systems
- jusung-engineering
- lam-research
- mattson-technology
- metryx-formerly-part-of-sifcoalstom-spin-off-lineage
- mist-systems-mistale
- naura-technology-group
- oxford-instruments-plasma-technology
- pegasus-semiconductor-pgase
- plasma-therm
- sentech-instruments
- sio2-medical-products-etch-division
- spts-technologies-orbotechkla
- tignis
- tokyo-electron-tel
- ulvac
- xsem
- yield-engineering-systems-yes
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


# Etch Tools (ALE, plasma etch)

*Kind: technology*

## Physics / mechanism

Etch removes material from a wafer surface with atomic-scale precision. Plasma etch ionises a process gas (Cl₂, HBr, CF₄, SF₆ etc.) into reactive radicals and ions; the former provide chemical selectivity, the latter provide directional energy. Key parameters: selectivity (target:mask:stop-layer removal ratios, ideally >50:1), aspect-ratio-dependent etch (ARDE) uniformity, line-edge roughness (LER, <1 nm 3σ for leading-edge), and damage depth. Atomic Layer Etching (ALE) takes this to the limit—self-limiting half-cycles (adsorption then energetic desorption) give <1 Å/cycle control. ALE is now production-relevant at 3 nm and below; LETI/IMEC roadmaps require it for gate-all-around and backside power rail patterning. Lam Research, Applied Materials, and TEL dominate capital-equipment supply; Hitachi and Oxford Instruments serve compound-semiconductor and photonics niches.

## Competitive landscape

Wet etch (HF, KOH, TMAH) is cheaper but isotropic—unsuitable for sub-10 nm critical dimensions. Laser ablation handles thick-film removal or singulation but lacks selectivity. Ion-beam etch (IBE/CAIBE) offers angstrom control for photonics facets and MEMS but throughput is too low for front-end logic. The key competitive axis is selectivity vs. throughput vs. damage budget.

## Cloudberry relevance

| Technique | Selectivity | Throughput | Damage |
|-----------|-------------|------------|--------|
| Plasma etch | High | High | Moderate |
| ALE | Very high | Low–moderate | Minimal |
| IBE/CAIBE | Low–moderate | Low | Low–moderate |


Cloudberry's photonics and advanced-materials portfolio companies (III-V, SiC, LiNbO₃, GaN) hit etch as an integration bottleneck before every tape-out. ALE tooling gaps for non-silicon materials are a live equipment whitespace. Deal-flow angles: process-equipment startups targeting compound-semiconductor ALE, etch-chemistry IP (novel precursors, selectivity additives), and process-control software layered onto existing Lam/AMAT installed base—all fit the deep-tech, capital-efficient thesis Cloudberry runs alongside the GF-LP fund.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
