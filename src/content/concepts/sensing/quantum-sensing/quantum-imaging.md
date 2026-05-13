---
type: concept
slug: quantum-imaging
canonical_name: Quantum Imaging (ghost, sub-shot-noise)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- sensing
- quantum-sensing
related_concepts: []
companies_using:
- aegiq
- hamamatsu-photonics
- id-quantique
- imec
- lightsolver
- luxtera-cisco-silicon-photonics
- micro-photon-devices-mpd
- optica-formerly-optiqal
- photon-force
- photon-spot
- photonic-sentient
- qlm-technology
- qt-imaging
- quanta-image-sensor-qis-group-gigajot-technology
- quantum-dot-capital-qdot-imaging
- quantum-imaging-lab-spin-out-quibim
- quantum-opus
- quix-quantum
- quside
- raytheon-bbn-technologies
- scontel
- sensiq-photonics
- single-quantum
- sparrow-quantum
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

# Quantum Imaging (ghost, sub-shot-noise)

*Kind: technology*

## Physics / mechanism

Quantum imaging exploits correlations between photon pairs—typically generated via spontaneous parametric down-conversion (SPDC) in nonlinear crystals (BBO, KTP, PPKTP)—to extract image information beyond classical limits. Ghost imaging uses one photon to illuminate the object while its entangled twin, never touching the object, carries the spatial information via coincidence detection; the image emerges from correlation measurements, not direct detection. Sub-shot-noise imaging suppresses photon-number variance below the Poisson limit using squeezed or N00N states, enabling SNR improvements scaling as √N over classical bounds. Current lab benchmarks: ~15 dB squeezing (PTB, 2023), ghost imaging at cm-scale resolution with <1 μW illumination. Key materials chokepoint is low-loss integrated nonlinear waveguides; free-space systems dominate but chip-scale PPLN and AlGaAs platforms are closing in. Entanglement rates in fiber-coupled sources now exceed 10⁸ pairs/sec.

## Competitive landscape

Classical low-light imaging (EMCCD, SPAD arrays, InGaAs APDs) competes directly on sensitivity without the complexity overhead. Structured illumination and computational ghost imaging (single-pixel, classical speckle correlations) replicate some ghost-imaging advantages without entanglement. LIDAR with Geiger-mode APDs addresses range-gated low-flux scenarios.

## Cloudberry relevance

| Approach | SNR advantage | Illumination flux | Complexity |
|---|---|---|---|
| Quantum ghost imaging | Moderate (correlation gain) | Ultra-low | High |
| Sub-shot-noise (squeezed) | Up to 15 dB | Low–medium | Very high |
| SPAD / classical single-pixel | None vs shot noise | Low | Low–medium |

Adjacent: quantum illumination (target detection under noise), QKD-integrated sensing, mid-IR upconversion imaging via sum-frequency in PPLN.


Cloudberry's photonics and advanced materials mandate makes this directly relevant. The critical IP sits in integrated nonlinear sources (PPLN, AlGaAs-on-insulator), low-noise SNSPD or SPAD readout, and correlation processing ASICs—all fundable as semiconductor or photonic component plays rather than full system bets. GlobalFoundries' silicon photonics PDK and Radiant's ferroelectric process nodes are plausible fabrication hooks for on-chip entangled-source startups. Deal-flow watch: companies commercialising chip-scale SPDC sources, squeezed-light modules for medical or defence sensing, or correlation-engine FPGAs.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
