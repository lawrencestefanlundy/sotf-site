---
type: concept
slug: imaging-vision
canonical_name: Imaging & Vision
aliases: []
kind: technology
parent_concepts:
- sensing
- imaging
related_concepts: []
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
sources_30d: 0
recent_mentions:
- slug: 2026-06-24-roman-telescope-comes-to-kennedy
  title: Roman Telescope Comes to Kennedy
  date: '2026-06-24'
  kind: web
neighbors: []
---
## Physics / mechanism

Imaging & vision encompasses the capture, transmission, and processing of spatial light information into actionable data. Core physics spans photodetection (silicon CMOS, InGaAs, HgCdTe), optics (refractive, diffractive, metalens), and signal chain (ADC, ISP, inference). Key parameters: pixel pitch (currently sub-1µm in mobile CMOS), quantum efficiency (>90% achievable in BSI CMOS), dynamic range (120+ dB in stacked HDR sensors), and frame rate (>1000fps in high-speed industrial). State of the art is stacked CMOS with in-sensor compute (Sony IMX, Samsung Isocell), SWIR InGaAs arrays for industrial/defence, and single-photon avalanche diode (SPAD) arrays for LiDAR and low-light. Thermal (LWIR microbolometer) remains uncooled and cost-sensitive.

## Competitive landscape

Competing sensing modalities: RF (radar, mmWave) offers all-weather capability but lower spatial resolution; LiDAR provides depth directly but is cost/complexity-heavy; ultrasound dominates medical near-field. Within imaging, CCD is largely displaced by CMOS except in scientific/space. Emerging competition from neuromorphic event sensors (Prophesee, iniVation) challenging frame-based paradigms in high-speed, low-power applications. Computational imaging (structured light, ptychography, compressed sensing) reduces hardware burden by shifting to algorithm. Metalens arrays threaten conventional refractive optics at wafer scale.

| Approach | Strength | Weakness |
|---|---|---|
| CMOS imaging | Cost, integration, volume | SWIR/LWIR blind |
| InGaAs/HgCdTe | Broad spectrum | Cost, fab complexity |
| Event/neuromorphic | Latency, dynamic range | Ecosystem immaturity |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
