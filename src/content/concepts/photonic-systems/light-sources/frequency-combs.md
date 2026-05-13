---
type: concept
slug: frequency-combs
canonical_name: Frequency Combs
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
- attocube-systems
- enlightra
- epiqc-peregrine-semiconductor-now-psemi-murata
- flux-photonics
- fraunhofer-hhi
- freedom-photonics
- hyperlight
- ii-vi-incorporated-coherent-corp
- imec
- imra-america
- laser-zentrum-hannover-lzh-spin-offs-lumentum
- lionix-international
- menlo-systems
- micro-photon-devices-mpd
- norcada
- nuro-photonics-formerly-known-as-fyla-laser
- octave-photonics
- oewaves
- rafeal-advanced-defense-systems-elbit-fibernet
- sifotonicst-sifotonics-technologies
- stable-laser-systems
- toptica-photonics
- vescent-photonics
- wieserlabs
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

# Frequency Combs

*Kind: technology*

## Physics / mechanism

A frequency comb is a laser source whose output spectrum consists of hundreds to thousands of equally spaced, phase-coherent spectral lines — a ruler in frequency space. Generated via mode-locked lasers, microresonator-based Kerr combs (microcombs), or electro-optic modulation, the line spacing equals the cavity repetition rate (typically 10 MHz–100 GHz). Key parameters: repetition rate stability, comb tooth SNR, octave span, and carrier-envelope offset (CEO) control. Microcombs on chip — using silicon nitride or lithium niobate resonators with Q > 10⁷ — now achieve sub-milliwatt threshold pump power. NIST and PTB-grade optical clocks use combs for absolute frequency measurement at 10⁻¹⁸ fractional uncertainty. Commercial units (Menlo Systems, Octave Photonics) ship at $50K–$200K; chip-scale versions are in late R&D.

## Competitive landscape

Competing approaches for precision metrology: optical atomic clocks without comb readout (limited to single transitions), Fourier-transform infrared spectroscopy (lower resolution, no absolute reference), and tunable diode laser absorption spectroscopy (TDLAS). For ranging/LiDAR, time-of-flight and FMCW LiDAR compete on cost.

## Cloudberry relevance

| Approach | Resolution | Chip-integrability | Cost |
|---|---|---|---|
| Microcomb (SiN/LN) | Sub-Hz line | High | Low (roadmap) |
| Mode-locked fiber laser | ~10 Hz | Low | High |
| TDLAS | ~MHz | Medium | Medium |

Adjacent: integrated photonics platforms (SiPh, InP), optical atomic clocks, dual-comb spectroscopy for molecular fingerprinting.


Frequency combs sit at the intersection of integrated photonics and precision instrumentation — both core Cloudberry theses. The chip-scale transition (SiN, LN-on-insulator) maps directly onto GlobalFoundries' 300mm silicon photonics and partner fabs. Deal-flow angles: fabless comb startups needing process-qualified foundry access, sensing companies (methane detection, medical breath analysis) de-risking TDLAS with comb calibration, and optical clock components feeding defense/PNT markets where Lunar Ventures co-investors are active.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
