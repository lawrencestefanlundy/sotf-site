---
type: concept
slug: indium-phosphide
canonical_name: Indium Phosphide (InP)
aliases: []
kind: material
domain:
- cloudberry
- sotf
parent_concepts:
- materials
- substrates
related_concepts: []
companies_using:
- accelink-technologies
- broadcom-avago-heritage
- chipworks-quintessent
- effect-photonics
- fraunhofer-hhi
- furukawa-electric
- hrl-laboratories
- ibm-research-zurich
- ii-vi-coherent
- iii-v-lab
- inphenix
- inphi-now-marvell
- landmark-optoelectronics
- ligentec
- lumentum
- macom-technology-solutions
- nokia-bell-labs-nokia-optical-networks
- oclaro-now-lumentum
- opticore-formerly-uphoton
- quix-quantum
- rockley-photonics
- smart-photonics
- sumitomo-electric
- teledyne-technologies
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

# Indium Phosphide (InP)

*Kind: material*

## Physics / mechanism

Indium phosphide is a III-V compound semiconductor with a direct bandgap of ~1.34 eV and electron mobility ~5,400 cm²/V·s — roughly 4× silicon. The direct gap enables efficient photon emission and absorption without phonon assistance, making it the substrate of choice for telecom-band (1,310 nm / 1,550 nm) lasers, modulators, and photodetectors. InP HBTs reach ft/fmax above 500 GHz, dominating mm-wave and sub-THz applications. Epitaxial growth is predominantly MOCVD on 4-inch wafers (6-inch emerging). Wafer cost remains 10–20× GaAs; threading dislocations from lattice mismatch constrain heterogeneous integration. State-of-the-art integrated InP photonic chips achieve >100 Gbaud PAM-4 modulation in datacentre transceiver PICs.

## Competitive landscape

GaAs competes at lower frequencies and shorter wavelengths; cheaper, more mature 6-inch supply chain but no telecom-band advantage. Silicon photonics (SiPh) addresses the same datacentre transceiver market at far lower cost using CMOS fabs, but requires III-V gain elements — often InP — bonded or grown heterogeneously. GaN owns high-power RF. InP's defensible moat is monolithic integration of gain + routing + detection at 1.55 µm.

## Cloudberry relevance

| Material | Bandgap (eV) | Electron mobility | Key application |
|---|---|---|---|
| InP | 1.34 (direct) | ~5,400 cm²/V·s | Telecom PICs, sub-THz HBT |
| GaAs | 1.42 (direct) | ~8,500 cm²/V·s | RF/microwave, 850 nm VCSEL |
| Si (photonics) | 1.12 (indirect) | ~1,400 cm²/V·s | Passive routing, modulators |


InP sits at the intersection of Cloudberry's photonics and advanced materials theses. Deal-flow angles: integrated PIC foundries (tower/SMART Photonics), EPI wafer suppliers, and fabless designers targeting 800G/1.6T datacenter optics or LiDAR. GlobalFoundries has no InP node, creating a white-space opportunity — portfolio companies building heterogeneous integration IP (InP-on-Si bonding) are strategically relevant. Lunar Ventures' early-stage mandate fits InP-native fabless startups before they need a dedicated process partner.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
