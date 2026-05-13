---
type: concept
slug: wafer-level-optics
canonical_name: Wafer-Level Optics
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- metasurfaces
related_concepts: []
companies_using:
- ams-osram
- anteryon
- applied-materials
- atomica-formerly-imt-masken-und-teilungen
- ephemix
- ev-group-evg
- heptagon-acquired-by-ams
- himax-technologies
- holoeye-photonics
- largan-precision
- liqxtal-technology
- litek-lianchuang-electronic
- lumus
- morpho-photonics
- nanoscribe
- photon-dynamics-orbotech-part-of-kla
- polight
- raytrix
- scivax
- sss-microtec
- tessera-xperi
- vario-optics
- viavi-solutions
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


# Wafer-Level Optics

*Kind: technology*

## Physics / mechanism

Wafer-level optics (WLO) fabricates optical elements—microlenses, diffusers, apertures, filters—directly on wafers using semiconductor processes: UV nanoimprint lithography, grayscale lithography, or reactive-ion etching into glass or polymer substrates. Arrays of lenses are replicated simultaneously across a 200 mm or 300 mm wafer, then diced and stacked into modules. Key parameters: sag height (typically 10–200 µm), NA (0.1–0.5 for smartphone modules), surface form error (<λ/10 RMS), and chief ray angle (CRA) matching to the image sensor. Alignment between stacked wafers is held to ±1–2 µm. Current SoA: four- to six-element stacked WLO modules at sub-4 mm total track length, shipping at >1 billion units/year in mobile CMOS image sensor supply chains. AMS-OSRAM, Anteryon, and Himax Imaging are production-scale suppliers.

## Competitive landscape

Traditional precision-machined or injection-moulded discrete lenses dominate longer focal-length and high-NA applications where sag or aberration requirements exceed WLO process limits. Freeform machined optics handle aspheric complexity WLO cannot; diffractive optical elements (DOEs) address wavelength-selective functions but suffer from high diffraction orders. Meta-optics (flat metalenses) threaten WLO at thin-form-factor AR/sensing wavelengths but remain yield-limited and polarisation-sensitive.

## Cloudberry relevance

| Approach | Thickness | CMOS-compatible | Volume cost |
|---|---|---|---|
| WLO (refractive) | ~1–5 mm stack | Yes | Low ($) |
| Machined asphere | 5–50 mm | No | High ($$$) |
| Metalens | <1 mm | Partial | Medium–high |


WLO sits at the semiconductor–photonics interface: manufacturable in foundry-adjacent fabs, scalable on 300 mm lines, and increasingly embedded in LiDAR, ToF, and edge-AI vision modules. For Cloudberry, relevant deal-flow includes companies building WLO process IP for non-mobile verticals (industrial inspection, medical imaging, photonic integrated circuit coupling), startups replacing discrete optics in VCSEL/photodiode packaging—a natural adjacency to GlobalFoundries' photonics PDK—and equipment or materials plays enabling tighter CRA control or IR-transparent polymer stacks.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
