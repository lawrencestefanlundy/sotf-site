---
type: concept
slug: hybrid-bonding
canonical_name: Hybrid Bonding (Cu-Cu)
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
- amkor-technology
- applied-materials
- ase-group-advanced-semiconductor-engineering
- atomica-formerly-smart-microsystems
- besi-be-semiconductor-industries
- cea-leti
- d-matrix
- eplace-formerly-part-of-disco-corp-ecosystem
- ev-group-evg
- fraunhofer-izm
- huawei-hisilicon-casm
- imec
- intel
- lumileds-formerly-philips-lumileds-now-xperi-see-also-adeia
- micron-technology
- ntopics-spin-out-of-cea-leti
- qubeicon
- samsung-electronics
- sk-hynix
- sony-semiconductor-solutions
- suss-microtec
- tohoku-university-aist-via-tohoku-spin-outs
- tsmc
- unimicron-technology
- yangtze-memory-technologies-ymtc
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

# Hybrid Bonding (Cu-Cu)

*Kind: technology*

## Physics / mechanism

Direct copper-to-copper bonding achieved by planarising dielectric (SiO₂ or SiCN) and Cu pad surfaces to sub-nanometre roughness (Ra < 0.5 nm), then annealing at 200–400 °C. At temperature, Cu atoms interdiffuse across the interface, eliminating the bond line entirely. Electrical resistance across the joint is near-bulk Cu; pitch scalability reaches <1 µm today (TSMC SoIC at ~9 µm pitch in HVM, research demos at 1–3 µm). Bandwidth density scales inversely with pitch squared—orders of magnitude beyond flip-chip bumps. Dielectric fusion bonds simultaneously, providing mechanical integrity and hermetic sealing. Key process parameters: surface activation (plasma or CMP), particle control (sub-10 nm), and anneal ambient.

## Competitive landscape

| Approach | Min pitch | Electrical R | Thermal budget |
|---|---|---|---|
| Hybrid bonding (Cu-Cu) | <1 µm (lab), ~9 µm (HVM) | Near-bulk Cu | 200–400 °C |
| Micro-bump (SnAg) | ~20–40 µm | Higher (intermetallic) | ~260 °C reflow |
| TCB (Cu pillar) | ~10–20 µm | Moderate | ~250–300 °C |

## Cloudberry relevance

Adjacent: glass-core substrates compress interconnect from the package side; monolithic 3D (sequential integration) eliminates bonding entirely but carries process complexity and yield risk. Photonic chiplet integration increasingly requires hybrid bonding to land III-V or SiPh tiles onto CMOS at fine pitch without solder-induced optical misalignment.


Cloudberry angle: hybrid bonding is the enabling integration layer for chiplet ecosystems, advanced photonics co-packaged optics, and GaAs/InP-on-Si photonic integration—all directly in-scope. Equipment and process-materials startups (CMP slurries, activation tooling, metrology for sub-nm roughness) are credible deal targets. GF's mature-node + advanced packaging trajectory creates co-investment context; Lunar portfolio companies building chiplet IP or photonic engines face a make-or-buy decision on bonding capability that informs competitive positioning assessments.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
