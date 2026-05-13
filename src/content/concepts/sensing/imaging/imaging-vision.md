---
type: concept
slug: imaging-vision
canonical_name: Imaging & Vision
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- sensing
- imaging
related_concepts: []
companies_using:
- aeye
- algolux
- basler-ag
- beehive-ai-now-part-of-cerence
- himax-technologies
- imec
- inuitive
- irida-labs
- luxonis
- mobileye
- nvidia
- outsight
- photon-vision-systems
- prophesee
- raytrix
- recogni
- seeing-machines
- sievert-larson-lynx
- smartmore
- sony-semiconductor-solutions
- syntiant
- teledyne-technologies
- trieye
- visionary-machines
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 70
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
---

# Imaging & Vision

*Kind: technology · Attio deal count: 70*

## Physics / mechanism

Imaging & vision encompasses the capture, transmission, and processing of spatial light information into actionable data. Core physics spans photodetection (silicon CMOS, InGaAs, HgCdTe), optics (refractive, diffractive, metalens), and signal chain (ADC, ISP, inference). Key parameters: pixel pitch (currently sub-1µm in mobile CMOS), quantum efficiency (>90% achievable in BSI CMOS), dynamic range (120+ dB in stacked HDR sensors), and frame rate (>1000fps in high-speed industrial). State of the art is stacked CMOS with in-sensor compute (Sony IMX, Samsung Isocell), SWIR InGaAs arrays for industrial/defence, and single-photon avalanche diode (SPAD) arrays for LiDAR and low-light. Thermal (LWIR microbolometer) remains uncooled and cost-sensitive.

## Competitive landscape


Competing sensing modalities: RF (radar, mmWave) offers all-weather capability but lower spatial resolution; LiDAR provides depth directly but is cost/complexity-heavy; ultrasound dominates medical near-field. Within imaging, CCD is largely displaced by CMOS except in scientific/space. Emerging competition from neuromorphic event sensors (Prophesee, iniVation) challenging frame-based paradigms in high-speed, low-power applications. Computational imaging (structured light, ptychography, compressed sensing) reduces hardware burden by shifting to algorithm. Metalens arrays threaten conventional refractive optics at wafer scale.

| Approach | Strength | Weakness |
|---|---|---|
| CMOS imaging | Cost, integration, volume | SWIR/LWIR blind |
| InGaAs/HgCdTe | Broad spectrum | Cost, fab complexity |
| Event/neuromorphic | Latency, dynamic range | Ecosystem immaturity |

## Cloudberry relevance
Photonics-native imaging is a direct Cloudberry deal-flow vector. Wafer-scale photonic integration (relevant to GlobalFoundries' silicon photonics PDK) enables LiDAR-on-chip, optical coherence tomography, and hyperspectral sensing as fundable fabless or fab-lite plays. SPAD arrays and single-photon counting overlap with Lunar Ventures' deep-tech software-hardware stack theses. Metalens and computational imaging startups need advanced materials and process nodes — squarely Cloudberry's competence. Defence and automotive pull-through provides near-term revenue anchoring pre-scale valuations.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
