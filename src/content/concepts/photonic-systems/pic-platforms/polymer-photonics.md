---
type: concept
slug: polymer-photonics
canonical_name: Polymer Photonics
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- pic-platforms
related_concepts: []
companies_using:
- ams-osram
- asahi-glass-agc-photonics-division
- chromis-fiberoptics
- cubicpv-formerly-1366-technologies
- enablence-technologies
- eo-polymers-soluxra
- flexenable
- fraunhofer-hhi-spin-outs-cluster
- hyperlight
- inphotec
- lightwave-logic
- linkra-photonics
- optoscribe
- phio-tx-formerly-rxi-pharmaceuticals
- phoxene
- polariton-technologies
- polymer-photonix-formerly-gigpeak
- polyphotonix
- scrona
- sumitomo-bakelite-photonics-materials
- teem-photonics
- thinfilm-thin-film-electronics
- toptica-photonics
- vanguard-photonics
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

# Polymer Photonics

*Kind: technology*

## Physics / mechanism

Polymer photonics uses organic polymer films as the waveguiding medium instead of silica or III-V semiconductors. Light is confined by refractive index contrast between polymer core (n ≈ 1.4–1.7, tunable via monomer selection) and cladding. Key functional mechanisms: electro-optic (EO) effect in chromophore-doped polymers (e.g., poled PMMA or AJL8-doped systems achieving r₃₃ > 200 pm/V, versus LiNbO₃'s ~30 pm/V), thermo-optic switching, and passive waveguide routing. Fabrication routes include spin-coating, nanoimprint, and direct laser writing—all wafer-scale compatible. Bandwidth potential exceeds 100 GHz in EO modulators; insertion loss remains the gap (2–5 dB/cm vs. <0.1 dB/cm for SiPh).

## Competitive landscape

The primary competition is silicon photonics (mature ecosystem, CMOS fabs, dense integration) and lithium niobate on insulator (LNOI, high r₃₃, low loss, but expensive and hard to integrate). Polymer sits between them on cost/performance.

## Cloudberry relevance

| Platform | EO coefficient | Loss (dB/cm) | CMOS-fab compatible |
|---|---|---|---|
| Silicon photonics | Weak (plasma) | 2–3 | Yes |
| LNOI | ~30 pm/V | <0.1 | No |
| Polymer EO | >150 pm/V | 2–5 | Partial |

Adjacent: polymer optical fiber (POF) for short-reach links; organic LEDs/lasers as potential on-chip sources; sol-gel silica hybrids.


Cloudberry angle: polymer EO modulators are a credible insertion point for datacenter optical interconnects—high-bandwidth, low drive-voltage, potentially chiplet-compatible. GF's platform doesn't natively support polymer back-end integration, but a polymer-on-Si hybrid module company could use GF front-end silicon then post-process. Deal-flow targets: fabless EO modulator startups (Polariton Technologies is the benchmark), tooling for poling/alignment, and materials suppliers with demonstrated r₃₃ > 150 pm/V in production-stable formulations.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
