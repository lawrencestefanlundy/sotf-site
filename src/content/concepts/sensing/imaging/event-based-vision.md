---
type: concept
slug: event-based-vision
canonical_name: Event-Based Vision
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
- airy3d
- akida-brainchip-holdings
- alpsentek
- celex-technologies
- clika
- eventide-imaging
- fastree3d
- imec
- inivation
- insightness
- movidius-intel
- neuromorphicio
- omnivision-technologies
- pictor-labs
- prophesee
- qualcomm
- robosense
- samsung-semiconductor
- silkyevcam-hillhouse-technology
- sony-semiconductor-solutions
- speck-formerly-neural-semiconductor
- synsense
- zurich-eye
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

# Event-Based Vision

*Kind: technology*

## Physics / mechanism

Event-based vision sensors (dynamic vision sensors, DVS) mimic retinal ganglion cells: each pixel fires asynchronously when local log-luminance change exceeds a threshold (~10–50 mV typically), rather than integrating full frames. Output is a sparse stream of (x, y, t, polarity) events at sub-microsecond temporal resolution. Latency is ~1 µs vs ~33 ms for 30 fps CMOS. Dynamic range reaches 120–140 dB (vs ~60 dB for conventional imagers). Leading silicon: Prophesee Metavision IMX636 (1280×720, ~4.86 M px), Samsung DVS, Sony IMX636-based derivatives, iniVation DAVIS346. Fabricated on standard CMOS nodes (180 nm–65 nm); pixel pitch typically 4.86–9 µm.

## Competitive landscape

Event-based sensors compete directly with high-speed global-shutter CMOS (Sony Pregius, ON Semi Python) and neuromorphic frame-free alternatives. Adjacent approaches include SPAD arrays (single-photon, time-resolved but frame-based), LiDAR for depth tasks, and optical flow ASICs. Processing back-ends compete with conventional CNN inference pipelines vs spiking neural network (SNN) accelerators.

## Cloudberry relevance

| Approach | Latency | Power | Dynamic Range |
|---|---|---|---|
| Event-based DVS | ~1 µs | ~5–20 mW | 120–140 dB |
| Global-shutter CMOS | ~1–33 ms | 50–300 mW | 55–70 dB |
| SPAD array | ~ns (ToF) | 100–500 mW | limited |


Deal-flow angles: fabless sensor startups (Prophesee, iniVation) fabbing on 65–180 nm nodes at fabs including GF, needing process-design-kit partnerships or minority stakes. Adjacent SNN inference chip startups are natural Lunar Ventures targets. Automotive ADAS, industrial inspection, and space robotics are near-term revenue wedges. GF's 22FDX platform suits ultra-low-power DVS pixel array variants—direct process conversation opportunity for a Cloudberry portfolio company.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
