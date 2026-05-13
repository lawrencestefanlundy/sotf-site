---
type: concept
slug: atmospheric-sensing
canonical_name: Atmospheric Sensing
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
- aclima
- aeroqual
- bright-carbon-brightcarbon-carbon-mapper
- everimpact
- ghgsat
- harp-technologies-sciaps
- kuva-space
- losphere-windcube-vaisala
- lufft-ott-hydromet
- meteogroup-dtn
- nanoquest-aerosense-sony
- opsis
- orion-analytics-spire-global
- picarro
- plair-sa
- quanta3-formerly-quantitative-imaging
- satlantis
- sensirion
- sensonomic
- soofos-quantared-technologies
- sutron-xylem
- tomorrowio
- vaisala
- windborne-systems
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

# Atmospheric Sensing

*Kind: technology*

## Physics / mechanism

Atmospheric sensing detects and quantifies gas-phase species, aerosols, and meteorological parameters in the open atmosphere. Core modalities: differential absorption lidar (DIAL) using tunable laser pulses to exploit species-specific absorption cross-sections at paired wavelengths; Fourier-transform infrared spectrometry (FTIR) for broadband fingerprinting; cavity-enhanced techniques (CRDS, CEAS) reaching sub-ppb detection limits via effective path lengths >10 km in a compact cell; and photoacoustic spectroscopy for portable mid-IR sensing. Key parameters: sensitivity (NEA ~10⁻¹⁰ cm⁻¹ Hz⁻½ for CRDS), selectivity (spectral resolution <0.001 cm⁻¹), range (lidar to 30+ km), and SWaP. Mid-IR quantum cascade lasers (QCLs, 3–12 µm) are the dominant photon source for molecular fingerprinting; interband cascade lasers (ICLs) cover lower power budgets. GHG monitoring, air quality, industrial leak detection, and defence CBRN drive deployment.

## Competitive landscape

Competing and adjacent approaches split by range, cost, and analyte class. Electrochemical and metal-oxide sensors dominate low-cost point detection but lack selectivity and drift. Satellite remote sensing (Sentinel-5P, GHGSat) provides global coverage at coarse resolution (>1 km). Passive FTIR competes with active lidar for standoff. Raman lidar resolves aerosol backscatter independent of absorption. Miniaturised photonic integrated circuit (PIC) spectrometers on Si or SiN wafer platforms are the near-term disruptive vector.

## Cloudberry relevance

| Modality | Range | Selectivity | SWaP |
|---|---|---|---|
| QCL-CRDS | <1 m (cell) | Sub-ppb | Medium |
| DIAL lidar | 1–30 km | ppm–ppb | High |
| PIC spectrometer | <1 m | ppb–ppm | Low |


Photonic sensing hardware is a direct Cloudberry thesis hit: QCL/ICL epitaxy, mid-IR waveguide PICs, and MEMS-tunable filters all sit at the semiconductor-photonics intersection where GlobalFoundries' advanced packaging and Radiant's PIC-on-CMOS capabilities create moat. Deal-flow angles include fabless mid-IR PIC startups needing foundry access, GHG monitoring companies requiring chip-scale spectrometers, and defence-adjacent standoff detection. Lunar Ventures' deep-tech seed exposure surfaces early-stage spin-outs from Fraunhofer or national labs in this space before Series A.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
