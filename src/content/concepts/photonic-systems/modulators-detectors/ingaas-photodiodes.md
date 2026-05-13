---
type: concept
slug: ingaas-photodiodes
canonical_name: InGaAs Photodiodes
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- modulators-detectors
related_concepts: []
companies_using:
- albis-optoelectronics
- ams-osram
- antaris-formerly-known-as-orbit-fab-unrelated-antaris-labs
- effect-photonics
- epigap-optronic
- flir-teledyne-flir
- fraunhofer-iaf
- guilin-glori-electronics
- hamamatsu-photonics
- ibsen-photonics
- ii-vi-incorporated-coherent-corp
- laser-components-gmbh
- leonardo-drs
- litrax
- lumentum
- oclaro-lumentum-legacy
- osi-systems-perkinelmer-sensors-excelitas
- photon-etc
- rebellion-photonics
- sensors-unlimited-collins-aerospace-rtx
- shengshi-optical-shengtai-photonics
- thorlabs
- voxtel-acquired-by-allegro-microsystems
- xenics
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

# InGaAs Photodiodes

*Kind: technology*

## Physics / mechanism

InGaAs (indium gallium arsenide) photodiodes are III-V compound semiconductor detectors absorbing light from ~900 nm to 1700 nm (extended InGaAs reaches 2.6 µm by tuning In content). Photons excite electron-hole pairs across a narrow bandgap (~0.75 eV for In₀.₅₃Ga₀.₄₇As lattice-matched to InP); reverse-biased p-i-n or avalanche (APD) structures sweep carriers before recombination. Key parameters: responsivity 0.8–1.1 A/W at 1550 nm, dark current 1–10 nA (p-i-n), noise-equivalent power sub-pW/√Hz, bandwidth up to 40+ GHz for high-speed variants. APD variants achieve multiplication gains of 10–30×. State of the art: wafer-scale InP epitaxy, monolithic arrays for LiDAR and optical coherence tomography, with leading suppliers including Lumentum, II-VI/Coherent, Hamamatsu, and GPD Optoelectronics.

## Competitive landscape

Competing detector technologies split by wavelength and application. Ge-on-Si photodiodes are CMOS-compatible and cover 900–1600 nm but carry higher dark current and inferior noise floor. Silicon APDs dominate below 900 nm at lower cost. HgCdTe (MCT) extends to mid-IR but requires cryogenic cooling and is expensive. For LiDAR specifically, SiPM arrays compete on cost and ecosystem maturity at 905 nm.

## Cloudberry relevance

| Technology | Wavelength | Dark Current | CMOS Integration |
|---|---|---|---|
| InGaAs p-i-n | 900–1700 nm | Low (nA) | No (InP substrate) |
| Ge-on-Si | 900–1580 nm | Higher (µA) | Yes |
| HgCdTe | 1–12 µm | Very low (cooled) | No |


InGaAs sits at the intersection of photonics, compound semiconductors, and sensing — core Cloudberry territory. Deal-flow angles: fabless detector startups needing InP foundry access (GlobalFoundries has no InP line, creating supply-chain wedge opportunities), monolithic InGaAs array companies targeting automotive LiDAR or datacom, and materials/epitaxy plays improving defect density or enabling heterogeneous integration onto Si. Lunar Ventures' early-stage mandate fits seed-stage teams attacking InGaAs-on-Si wafer bonding or novel APD architectures.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
