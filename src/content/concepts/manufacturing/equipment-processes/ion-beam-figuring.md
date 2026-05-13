---
type: concept
slug: ion-beam-figuring
canonical_name: Ion-Beam Figuring
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
- asml
- asphericon
- brd-optical-beijing
- canon-inc
- changchun-institute-of-optics-fine-mechanics-and-physics-cio
- fraunhofer-iof
- ii-vi-incorporated-coherent-corp
- korea-institute-of-science-and-technology-kist-korea-astrono
- lightpath-technologies
- nikon-corporation
- nu-tek-precision-optical
- optical-surfaces-ltd
- optimax-systems
- raytheon-technologies-rtx
- rigtol-optics
- sagem-safran-electronics-defense
- satisloh
- sifco-industries-precision-optical
- tinsley-laboratories-l3harris
- vista-optics-aperture-optical-sciences
- winlight-optique
- zeeko-ltd
- zeiss-carl-zeiss-ag
- zygo-corporation-ametek
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


# Ion-Beam Figuring

*Kind: technology*

## Physics / mechanism

Ion-beam figuring (IBF) uses a low-energy, broad noble-gas ion beam (typically Ar or Xe, 300–1500 eV) directed at an optical surface to remove material atom-by-atom via momentum-transfer sputtering. The removal function is deterministic and Gaussian-shaped; iterative dwell-time algorithms (derived from deconvolution of the tool influence function) converge surface figure error toward sub-nm RMS. No tool contact means no subsurface damage and no mid-spatial-frequency polishing artifacts introduced. State-of-the-art IBF systems (Zeiss, Optically Driven Figuring/Tinsley, SORL) achieve λ/50 figure accuracy at 632 nm, surface roughness <0.1 nm RMS, and are production-qualified for EUV lithography optics, space telescope mirrors, and X-ray synchrotron optics.

## Competitive landscape

Adjacent finishing techniques compete across different error-spatial-frequency regimes. Magnetorheological finishing (MRF) handles mid-spatial frequencies faster but introduces residual iron contamination and struggles below 1 nm RMS. Reactive-ion etching (RIE) planarizes at wafer scale but lacks freeform figure control. Subaperture lap polishing remains cheaper for loose tolerances. IBF has no peers for combining freeform geometry, angstrom-level figure, and zero mechanical stress delivery.

## Cloudberry relevance

| Technique | Figure accuracy | Surface damage | Freeform capable |
|---|---|---|---|
| IBF | <λ/50 | None | Yes |
| MRF | ~λ/20 | Low | Yes |
| CNC polishing | ~λ/10 | Moderate | Partial |


IBF sits at the intersection of photonics, semiconductor fab tooling, and defence/space optics — all active Cloudberry themes. EUV mask blank and projection optic supply chains depend on IBF; any fabless photonics or advanced-node supplier faces IBF as a bottleneck or enabler. Deal-flow angles: capital equipment startups reducing IBF cycle time, AI-driven dwell-time optimisation software, and materials companies supplying low-defect substrates requiring IBF qualification. GlobalFoundries-adjacent fabs sourcing EUV optics make this directly relevant to LP portfolio context.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
