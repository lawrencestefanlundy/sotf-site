---
type: concept
slug: time-of-flight
canonical_name: Time-of-Flight (iToF, dToF)
aliases: []
kind: technology
parent_concepts:
- sensing
- ranging-detection
related_concepts: []
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
## Physics / mechanism

Time-of-Flight measures distance by timing light (or other EM radiation) round-trips. **iToF (indirect)** modulates a continuous-wave source and measures phase shift between emitted and received signals; depth = (c × Δφ) / (4πf). Typical precision: 1–5 mm at 1–4 m, 30–120 fps, 64×64 to 640×480 resolution. **dToF (direct)** fires discrete pulses and timestamps photon returns via SPAD (single-photon avalanche diode) arrays; resolves sub-mm at longer range, better outdoor performance. Key parameters: modulation frequency (iToF, 10–200 MHz), SPAD fill factor, TDC resolution (dToF, ~10–50 ps), multipath interference, and ambient light rejection. Apple's LiDAR Scanner (iPhone/iPad) is mass-market dToF; Sony and STMicro dominate iToF sensor supply.

## Competitive landscape

iToF competes directly with structured light (cheaper BOM, weaker outdoors), stereo vision (software-heavy, no active illumination cost), and scanning LiDAR (superior range/resolution, far higher cost). dToF competes with FMCW LiDAR (coherent detection, velocity + depth simultaneously, but complex PIC integration). Flash LiDAR is architecturally dToF at array scale.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
