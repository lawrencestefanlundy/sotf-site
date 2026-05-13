---
type: concept
slug: lithography
canonical_name: Lithography
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- lithography
related_concepts: []
companies_using:
- applied-materials
- asml
- canon-semiconductor-equipment
- entegris
- eulitha
- euv-lithography-euvl-foundation-imec
- heidelberg-instruments
- inpria
- intel-foundry
- irresistible-materials
- jsr-corporation
- kla-corporation
- lam-research
- morphotonics
- multibeam-corporation
- mycronic
- nikon-precision
- onto-innovation
- print-rite-jiangfeng-electronics
- samsung-foundry
- shin-etsu-chemical
- smee-shanghai-micro-electronics-equipment
- tsmc
- vistec-electron-beam
- zeiss-smt
ideas_referencing: []
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-05-02-euv-lithography-wikipedia]]'
- '[[2026-05-02-asml-euv-lithography-systems]]'
- '[[2023-12-06-euv-lithography-but-with-a-free-electron-laser]]'
- '[[2025-01-06-radiant-acquires-nilt]]'
- '[[2026-05-02-two-photon-lithography-for-integrated-photonic-packaging-lig]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 32
descendants:
- duv-immersion-lithography
- e-beam-lithography
- euv-light-sources
- high-na-euv-lithography
- lithography-tools
- mask-blank-manufacturing
- maskless-lithography
- nanoimprint-lithography
- photoresists
- two-photon-polymerization
- xolography
last_reorg_date: '2026-05-13'
sources_7d: 3
sources_30d: 7
---


# Lithography

*Kind: technology · Attio deal count: 5*

## Physics / mechanism

Lithography is the patterning process that defines transistor features, interconnects, and devices on semiconductor wafers by projecting light (or particle beams) through a mask onto photoresist-coated substrates. Resolution is governed by the Rayleigh criterion: R = k₁λ/NA, where k₁ is a process-dependent factor, λ is wavelength, and NA is numerical aperture. EUV (13.5 nm wavelength) is current leading-edge, enabling sub-5 nm nodes at ~200 wafers/hour on ASML's NXE/EXE platforms. Deep-UV (193 nm immersion) remains dominant for mature nodes. Overlay accuracy, dose uniformity, and mask defectivity are the binding constraints at leading edge. High-NA EUV (0.55 NA) is entering HVM, pushing single-exposure resolution below 8 nm half-pitch.

## Competitive landscape


| Technique | Wavelength / Method | Node range | Key players |
|---|---|---|---|
| DUV (193i) | 193 nm immersion | 28 nm–65 nm | ASML, Nikon |
| EUV (Low-NA) | 13.5 nm, 0.33 NA | 5 nm–7 nm | ASML only |
| High-NA EUV | 13.5 nm, 0.55 NA | <2 nm | ASML only |
| Nanoimprint (NIL) | Contact mechanical | ~14 nm | Canon, EV Group |
| e-beam direct-write | Electron beam | Mask-making, R&D | IMS, Raith |

## Cloudberry relevance

Nanoimprint is the credible disruptor for cost-sensitive nodes; e-beam matters for mask inspection and advanced packaging. Multi-patterning extends DUV life but inflates process steps and cost. Directed self-assembly (DSA) remains pre-commercial.


GlobalFoundries competes on differentiated nodes (22FDX, 45CLO for photonics) where DUV suffices—lithography cost-per-wafer and overlay at those nodes directly affects LP fund portfolio economics. Cloudberry deal-flow angles: photomask materials, resist chemistry (EUV requires new CAR/MOR formulations), metrology and inspection hardware, and fab-adjacent software for OPC/SMO. Startups improving EUV resist sensitivity or NIL throughput are fundable; photonic IC fabs using deep-UV for waveguide definition are direct pipeline candidates.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
