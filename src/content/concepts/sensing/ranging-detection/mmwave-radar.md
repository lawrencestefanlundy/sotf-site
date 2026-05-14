---
type: concept
slug: mmwave-radar
canonical_name: mmWave Radar
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
recent_mentions: []
neighbors: []
---
## Physics / mechanism

mmWave radar operates in the 30–300 GHz band (most automotive and industrial deployments use 76–81 GHz). Transmitted FMCW chirps reflect off targets; range is extracted from beat frequency, velocity from Doppler shift, angle from phased-array receive aperture. Key parameters: range resolution ∝ 1/bandwidth (4 GHz BW → ~3.75 cm), velocity resolution ∝ carrier frequency and chirp duration, angular resolution ∝ aperture size. Modern 77 GHz SoCs (TI AWR, NXP S32R, Vayyar) integrate TX/RX chains, ADC, and DSP on a single RFCMOS or SiGe die. MIMO virtual aperture extension pushes angular resolution below 1°. Point-cloud outputs now feed directly into neural inference pipelines on-chip.

## Competitive landscape

LiDAR dominates perception where point-cloud density matters; cameras dominate where texture/color is needed. mmWave wins on weather immunity, through-barrier sensing, and velocity-first use cases. Ultrasonic covers short-range parking (<5 m) at lower cost. Structured-light and ToF depth sensors compete in indoor/industrial but fail outdoors. Key differentiation axes:

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
