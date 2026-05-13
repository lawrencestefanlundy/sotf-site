---
type: concept
slug: germanium-photodiodes
canonical_name: Germanium Photodiodes
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
- broadcom
- effect-photonics
- ephos
- gigpeak-integrated-device-technology-renesas
- globalfoundries
- hamamatsu-photonics
- hyperlight
- ihp-microelectronics
- ii-vi-incorporated-coherent-corp
- imec
- intel-intel-foundry-silicon-photonics
- jdsu-viavi-solutions
- kyosemi-corporation
- ligentec
- lumentum
- osi-systems-optoelectronics-division
- photondelta-portfolio-photon-delta
- poetech-poet-technologies
- quintessent
- rockley-photonics
- scintil-photonics
- sicoya-now-trumpf-photonic-components
- smart-photonics
- teledyne-e2v
- wuhan-hglaser-hg-optronics
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

# Germanium Photodiodes

*Kind: technology*

## Physics / mechanism

Germanium photodiodes exploit Ge's bandgap (~0.66 eV) to absorb photons out to ~1600 nm, covering the full O- through L-band telecom window where silicon is blind. Incident photons generate electron-hole pairs; reverse bias sweeps carriers across a thin intrinsic region (p-i-n architecture) producing photocurrent. Key figures of merit: responsivity 0.6–0.9 A/W at 1310/1550 nm, dark current 1–100 nA (waveguide-integrated devices tighter), bandwidth >50 GHz in advanced implementations, and operating voltage typically −1 to −3 V. State of the art: monolithic Ge-on-Si grown by CVD epitaxy, threading dislocation density reduced to ~10⁷ cm⁻² via graded buffers or cyclic annealing. Leading edge devices (Intel, imec, GlobalFoundries 45RFSOI/45CLO) are fully CMOS-back-end integrated for silicon photonics PICs.

## Competitive landscape

InGaAs p-i-n and APDs are the primary competition—superior dark current and noise floor, but III-V fab incompatible with CMOS, expensive, and harder to integrate monolithically. Si APDs dominate <900 nm. Extended-InGaAs and HgCdTe push to mid-IR but at significant cost and complexity penalties.

## Cloudberry relevance

| Detector | Wavelength range | CMOS integration | Relative cost |
|---|---|---|---|
| Ge p-i-n | 800–1600 nm | Native (SiPh) | Low |
| InGaAs p-i-n | 900–1700 nm | Hybrid/flip-chip | Medium–High |
| Si APD | 400–1000 nm | Native | Low |


Ge photodiodes are the enabling element for silicon photonics transceivers—the segment scaling fastest in AI/HPC interconnect buildout. GF's 45CLO and 45RFSOI platforms both include qualified Ge PD modules, making this directly relevant to Cloudberry portfolio companies fabbing at GF. Deal-flow angles: startups building LiDAR receivers, 800G/1.6T co-packaged optics ASICs, or sensing PICs where CMOS-native Ge detection removes a co-packaging integration risk and cost node.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
