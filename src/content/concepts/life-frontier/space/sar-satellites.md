---
type: concept
slug: sar-satellites
canonical_name: SAR Satellites (Synthetic Aperture Radar)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- space
related_concepts: []
companies_using:
- airbus-defence-space
- aresys
- aurora-insight
- azimuth-systems-azimuth-space
- capella-space
- e-geos-cosmo-skymed
- iceye-competitor-kleos-space
- iceye
- iqps-institute-for-q-shu-pioneers-of-space
- kompsat-si-imaging-services-siis
- mda-space
- novasar-technologies
- orbital-sidekick
- pixxel
- predasar
- sar-lupe-ohb-system
- sarvision
- sateliot
- satellogic
- satvu
- spacety
- synspective
- thales-alenia-space
- umbra
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

# SAR Satellites (Synthetic Aperture Radar)

*Kind: technology*

## Physics / mechanism

SAR satellites emit microwave pulses (typically 1–12 GHz, X- to L-band) toward Earth and record backscattered returns. By coherently combining returns across the satellite's flight path, an aperture synthetically far larger than the physical antenna is formed — enabling sub-meter resolution from LEO. Key parameters: center frequency (determines penetration depth vs. resolution trade-off), pulse repetition frequency, chirp bandwidth (drives range resolution; ~300 MHz = ~0.5 m), and platform velocity/altitude. Current SoA: Capella Space and ICEYE operate X-band LEO constellations with ~0.5 m resolution and <1 hr revisit; Umbra reaches 25 cm in spotlight mode. Unlike optical systems, SAR is weather- and daylight-independent.

## Competitive landscape

Optical EO satellites (Maxar, Planet) are the primary commercial substitute — lower cost per image, easier interpretation, but cloud-blocked and daylight-constrained. GNSS-R (Spire, HawkEye 360) overlaps in maritime/soil-moisture applications. Hyperspectral adds material-class discrimination optical can't match but SAR can't replicate either.

## Cloudberry relevance

| Modality | All-weather | Resolution (best) | Cost/image (approx) |
|---|---|---|---|
| SAR (X-band LEO) | Yes | 0.25 m | $10–50 |
| Optical (VHR) | No | 0.3 m | $5–30 |
| Hyperspectral | No | 3–10 m | $20–100 |


SAR intersects Cloudberry's stack at the semiconductor layer: custom RF ASICs, GaN-on-SiC T/R modules, and photonics-enabled beamforming (optical true-time-delay for wideband phased arrays) are active design problems. GlobalFoundries' 45RFSOI and 8XP processes are directly relevant to SAR front-end integration. Deal-flow angles: RF ASIC IP, photonic beamforming chiplets, and signal-processing edge silicon for on-board SAR compression — all fundable at seed/Series A in European deep-tech.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
