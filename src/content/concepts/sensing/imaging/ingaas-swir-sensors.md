---
type: concept
slug: ingaas-swir-sensors
canonical_name: InGaAs SWIR Sensors
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- sensing
- imaging
related_concepts: []
companies_using:
- albis-optoelectronics
- caeleste
- episensors-epistar-subsidiary
- flir-systems-teledyne-flir
- hamamatsu-photonics
- ii-vi-incorporated-coherent
- infrared-laboratories-irlabs
- laser-components-gmbh
- leonardo-drs
- leti-cea-leti
- lynred-formerly-sofradir-ulis
- opsens-solutions
- photon-lines-photonicsnov
- princeton-infrared-technologies
- quantum-opus-pixel-photonics-spin-out-context-actualsense
- raptor-photonics
- scd-semiconductor-devices
- sensors-unlimited-collins-aerospace
- shenzhen-hypersen-technologies
- swir-vision-systems
- teledyne-technologies
- voxtel-acquired-by-allegro-microsystems
- wuhan-guide-infrared
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

# InGaAs SWIR Sensors

*Kind: technology*

## Physics / mechanism

Indium gallium arsenide (InGaAs) photodetectors exploit the direct bandgap of In₀.₅₃Ga₀.₄₇As lattice-matched to InP substrates. The bandgap (~0.74 eV) gives absorption from ~900 nm to 1700 nm; extending In content to ~0.82 shifts cutoff to ~2.6 µm (extended SWIR) at the cost of lattice mismatch and dark current. Core figures of merit: quantum efficiency >80%, dark current density <1 nA/cm² at room temperature for standard compositions, noise-equivalent irradiance in the 10⁻¹⁰ W/cm² range. FPAs ship at 640×512 and 1280×1024 formats; pixel pitches have compressed to 5 µm. ROIC integration (InGaAs flip-bonded to Si CMOS) is the dominant packaging architecture. Key producers: Sensors Unlimited (UTC/Collins), Vigo, Leonardo DRS, Hamamatsu, and SWIR Vision Systems.

## Competitive landscape

InGaAs competes primarily on cost and operating temperature against three alternatives:

## Cloudberry relevance

| Detector | Cutoff | Cooling required | Cost (FPA) |
|---|---|---|---|
| InGaAs (standard) | 1.7 µm | None (RT) | $$$ |
| MCT (HgCdTe) | Tunable to 12 µm | Yes (77 K typical) | $$$$ |
| Colloidal QD (PbS/InAs) | 1.4–2.0 µm | None | $ (emerging) |

Germanium-on-Si is a direct fab-compatible challenger in the 0.9–1.6 µm window; SWIR Vision's CMOS-native colloidal QD approach threatens InGaAs's price floor in consumer/industrial segments. InGaAs holds the professional and defense market on sensitivity and reliability grounds.


InGaAs sits at the intersection of III-V epitaxy, ROIC design, and photonics packaging — all Cloudberry-relevant capability nodes. Deal-flow angles: fabless SWIR camera companies dependent on InP epi supply chains, QD-on-CMOS startups trying to displace InGaAs in industrial machine vision, and SWIR LiDAR stacks for automotive or defence. GlobalFoundries has no InP epi capability, so integration plays (III-V-on-Si heterogeneous integration) are the natural tension point to watch for investable wedges.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
