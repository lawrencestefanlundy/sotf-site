---
type: concept
slug: polymer-waveguides
canonical_name: Polymer Waveguides
aliases:
- polymer optical waveguides
- SU-8 waveguides
- OrmoCer waveguides
- 2PP-resin waveguides
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- materials
- functional-layers
related_concepts:
- two-photon-polymerization
- xolography
- co-packaged-optics
- material-class-displacement
companies_using:
- light-spring
- opdo
companies_passed:
- '[[light-spring]]'
- '[[opdo]]'
ideas_referencing:
- '[[photonic-packaging-cpo]]'
- '[[photonics-material-class-war]]'
sources: []
frontier:
- Does any polymer waveguide platform reach Telcordia GR-468 qualification for AI-interconnect production by 2028?
- Polymer-as-structural vs polymer-as-overcoat — does the distinction map to qualification risk cleanly?
- Can OrmoCer or specific SU-8 derivatives reach <0.5 dB/cm at 1550 nm with production-grade reliability?
- Does 3D-printed polymer (2PP, xolography) achieve the dimensional accuracy needed for single-mode telecom waveguides at scale?
- What's the moisture-uptake / thermal-cycling failure mode at 25-year telecom-grade reliability targets?
last_updated: 2026-05-08
tags:
- concept
- photonics
- polymer
- 2pp
- cpo
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Polymer Waveguides

*Kind: technology · Cheap, conformal, 3D-printable photonic medium with reliability question*

## Physics / mechanism

Polymer optical waveguides are organic-resin films patterned by photolithography, embossing, or 3D printing (two-photon polymerisation, xolography). Refractive index 1.5-1.6, with cladding ~0.01-0.05 lower than core. Loss best-case ~0.1 dB/cm at 850 nm, worse at 1550 nm (~0.5-2 dB/cm). Common materials: SU-8 epoxy, OrmoCer, PMMA, fluorinated polymers, photopolymer resins for 2PP.

The killer commercial pitch is cost + 3D capability: standard photolithography costs are ~10× lower than silicon photonics, and 3D-printable resins enable arbitrary geometries that wouldn't be lithographically reachable. Light Spring's 2PP and Opdo's xolography are different routes to the same end.

## Competitive landscape

Production today: short-reach datacom (10G/25G optical engines on FR4 PCBs), board-level interconnects, biomedical (waveguide-integrated sensors). Companies: vario-optics, IBM Zurich (research). 3D-printed photonic packaging: Light Spring (2PP), Opdo (xolography), Multiphoton Optics, Nanoscribe.

The binding question for AI-interconnect / CPO is reliability. Telcordia GR-468 qualification — the standard for fibre-optic component reliability under 25-year telecom-grade conditions — has been demonstrated for packaged inorganic photonics but is much harder for polymer-as-structural-element. Cloudberry passed Light Spring and Opdo on exactly this concern (memo-light-spring, memo-opdo).

## Cloudberry relevance

Direct via two pass cases: **Light Spring** (2PP, polymer overcoat) and **Opdo** (xolography, polymer-as-structural). The polymer-fade narrative is part of **Photonics Material Class War**. If polymer reliability lands by 2028, the pass-case logic flips.

## Frontier (open questions)

See frontmatter `frontier:` block.
