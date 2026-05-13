---
type: concept
slug: avalanche-photodiodes
canonical_name: Avalanche Photodiodes
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- modulators-detectors
related_concepts: []
companies_using:
- albis-optoelectronics
- argo-photonics
- broadcom
- excelitas-technologies
- first-sensor-te-connectivity
- fraunhofer-heinrich-hertz-institute-hhi-spin-outs
- hamamatsu-photonics
- idq-id-quantique
- ii-vi-incorporated-coherent
- kyosemi-corporation
- laser-components-gmbh
- leica-geosystems-hexagon
- liquidcool-solutions-argo-navis-photonics
- lumentum
- micro-photon-devices-mpd
- onsemi-on-semiconductor
- ouster-colonnade-acquisition-lidar-co
- philips-photonics-now-part-of-ii-vicoherent
- photon-force
- rpmc-lasers-boston-electronics
- sense-photonics
- sifotonics-technologies
- titan-photonics
- trimble
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

# Avalanche Photodiodes

*Kind: technology*

## Physics / mechanism

Avalanche photodiodes (APDs) exploit impact ionization: an absorbed photon generates a primary electron-hole pair, which is accelerated by a strong reverse-bias field (typically 20–200 V depending on structure) until it collides with the lattice and generates secondary carriers, producing internal gain (M = 10–100×). Key figures of merit are gain-bandwidth product (GBP), excess noise factor F(M) tied to the ionization coefficient ratio k, and dark current. InGaAs/InP APDs dominate telecom (1310/1550 nm), with GBP ~160 GHz commercially. Silicon APDs cover visible/NIR; Geiger-mode (SPAD) variants achieve single-photon sensitivity with sub-100 ps timing jitter. Separate absorption, charge, and multiplication (SACM) structures decouple the absorption and gain regions, now standard practice.

## Competitive landscape

Si APDs are cheap but band-limited to ~1 µm. InGaAs/InP APDs cover telecom wavelengths but are expensive, III-V fab-constrained, and LIDAR-hostile at high temperature. Ge-on-Si APDs are the primary challenger—CMOS-compatible, wafer-scale, lower cost—but k-ratio is less favorable (higher noise). HgCdTe APDs reach MWIR/LWIR with near-unity k (near-noiseless gain) but remain cryogenic and defense-niche. AlInAsSb and Al₀.₈Ga₀.₂As are research-stage low-noise candidates. SPADs in SiPh platforms are displacing linear APDs in quantum and ranging applications.

## Cloudberry relevance

| Detector | Wavelength | Noise (k) | CMOS-compatible |
|---|---|---|---|
| Si APD | 400–900 nm | Low (k~0.02) | Yes |
| InGaAs/InP APD | 900–1650 nm | Medium (k~0.4) | No |
| Ge-on-Si APD | 800–1600 nm | Medium-high (k~0.3) | Yes |


Cloudberry's GlobalFoundries-LP relationship is directly relevant: GF's 45CLO SiPh platform and 22FDX enable monolithic Ge APD and SPAD integration—a key process differentiation over fabless III-V plays. Deal-flow angles include LIDAR chipsets for automotive/industrial, co-packaged optics for datacenter (800G/1.6T), and quantum photonics (single-photon counting). Watch for startups designing around SiPh-native SPADs rather than buying discrete InGaAs APDs—this is a displacement trade with a clear foundry hook and defensible IP in quench circuitry and pixel architecture.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
