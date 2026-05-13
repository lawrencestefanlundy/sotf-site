---
type: concept
slug: optical-coatings
canonical_name: Optical Coatings (dielectric mirrors, filters)
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
- alluxa
- ams-osram
- chroma-technology
- coherent-corp-ii-vi-coherent
- crystran
- edmund-optics
- evaporated-coatings-inc-eci
- hangzhou-shalom-eo
- iridian-spectral-technologies
- jenoptik
- laser-components-gmbh
- layertec
- materion-precision-optics
- nidec-copal-electronics
- oceanoptics-ocean-insight
- omega-optical
- optics-balzers
- optiwave-photonics
- optoman
- photon-dynamics-abrisa-technologies
- photon-dynamics-korea-pdk-optics
- qoptics
- semrock-idex-health-science
- spectrogon
- viavi-solutions
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


# Optical Coatings (dielectric mirrors, filters)

*Kind: material*

## Physics / mechanism

Thin-film stacks of alternating high- and low-refractive-index dielectrics (e.g. TiO₂/SiO₂, Ta₂O₅/SiO₂, Nb₂O₅/SiO₂) deposited by IBS, PECVD, or magnetron sputtering. Reflectance is governed by constructive/destructive interference; layer thickness tuned to λ/4 optical path length. Dielectric mirrors routinely achieve R > 99.999% (5-nines) at target wavelength with scatter losses < 1 ppm—critical for laser cavities and ring-resonator Q-factors. Key parameters: laser damage threshold (LIDT, J/cm²), group delay dispersion (GDD, fs²), spectral bandwidth, and environmental stability (humidity, thermal cycling). State of the art: chirped-mirror designs compress few-fs pulses; ion-beam-sputtered coatings dominate precision metrology and gravitational-wave interferometers (LIGO mirror losses ~1 ppm).

## Competitive landscape

Competing approaches split by use case. Metallic mirrors (Ag, Au, Al) offer broad bandwidth but absorb ~1–5% and degrade. Photonic crystal reflectors (etched semiconductor slabs) integrate monolithically on-chip but require fab-node lithography and are narrowband. Grating-based reflectors suit specific polarization tasks. For integrated photonics, Bragg reflectors grown epitaxially (GaAs/AlGaAs DBRs) compete directly with deposited dielectrics on III-V platforms.

## Cloudberry relevance

| Approach | Loss floor | Integration | Bandwidth |
|---|---|---|---|
| Dielectric thin-film | < 10 ppm | Discrete/hybrid | Narrow–broad |
| Epitaxial DBR | ~100 ppm | Monolithic III-V | Narrow |
| Metallic mirror | ~1% | Any substrate | Broadband |


Optical coatings sit at the yield-limiting, IP-dense layer of photonic hardware: LiDAR transmitters, silicon-photonics co-packaged optics, quantum photonic chips, and advanced EUV optics (Mo/Si multilayers at 13.5 nm). Deal-flow angles: coating-process startups enabling heterogeneous integration on SiPh wafers, LIDT-optimised coatings for high-power laser diode stacks, and metrology-grade coatings for atomic clocks or quantum networking nodes—all adjacent to GlobalFoundries' SiPh and RF-photonics roadmap.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
