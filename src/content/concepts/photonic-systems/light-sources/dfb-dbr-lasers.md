---
type: concept
slug: dfb-dbr-lasers
canonical_name: DFB / DBR Lasers
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- light-sources
related_concepts: []
companies_using:
- accelink-technologies
- bright-photonics
- broadcom-avago-photonics
- brolis-semiconductors
- denselight-semiconductors
- eagleyard-photonics
- eblana-photonics
- frankfurt-laser-company-flc
- furukawa-electric
- ii-vi-incorporated-coherent
- innolume
- inphenix
- lumentum
- macom-technology-solutions
- mitsubishi-electric-optical-devices
- nanoplus-nanosystems-and-technologies
- photodigm
- raycan
- sivers-photonics
- source-photonics
- sumitomo-electric-industries
- thorlabs
- toptica-photonics
- vixar-acquired-by-osram
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

# DFB / DBR Lasers

*Kind: technology*

## Physics / mechanism

Distributed Feedback (DFB) and Distributed Bragg Reflector (DBR) lasers are single-longitudinal-mode semiconductor lasers that use periodic refractive-index or gain gratings to provide wavelength-selective optical feedback, replacing the broadband mirrors of Fabry-Pérot cavities. In DFB designs the grating runs the full cavity length; in DBR designs discrete grating sections flank the gain region, enabling independent current tuning of wavelength and power. Both operate on the Bragg condition: λ_B = 2nΛ, where Λ is grating pitch and n is effective index. State-of-the-art telecom DFBs achieve side-mode suppression ratios >50 dB, linewidths <1 MHz, and output powers of 10–40 mW CW at 1310/1550 nm. Tunable DBR variants cover >40 nm tuning range. Integration into InP or GaAs PICs is mature; heterogeneous bonding onto silicon photonics is the current scaling frontier.

## Competitive landscape

Key competition comes from Fabry-Pérot lasers (cheap, multimode, adequate for short-reach), VCSELs (lower cost, wafer-testable, dominate datacom ≤10 km), and external-cavity lasers (narrower linewidth, <100 Hz, but bulky/expensive). Emerging coherent thin-film lithium niobate and silicon-nitride-integrated laser sources challenge DBR in linewidth-sensitive sensing.

## Cloudberry relevance

| Type | Linewidth | Tuning | Integration |
|------|-----------|--------|-------------|
| DFB | ~1 MHz | Fixed / slight thermal | InP, GaAs, Si-hybrid |
| VCSEL | ~100 MHz | Limited | GaAs, wafer-scale |
| ECL | <1 kHz | Wide | Discrete / hybrid |


DFB/DBR lasers sit at the core of coherent optical interconnects, LiDAR, and sensing—all high-conviction Cloudberry themes. Deal-flow relevance: fabless photonics startups designing tunable DBR sources for co-packaged optics or FMCW LiDAR; process IP around grating definition that could land at a GlobalFoundries-LP-adjacent foundry expanding into InP or silicon-photonics-on-insulator MPW. Lunar Ventures' seed-stage European photonics bets often need a downstream manufacturing pathway—this is a concrete hook.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
