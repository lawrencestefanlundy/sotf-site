---
type: concept
slug: mmwave-radar
canonical_name: mmWave Radar
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- sensing
- ranging-detection
related_concepts: []
companies_using:
- acconeer
- ainstein-ai
- ancortek
- arbe-robotics
- bitsensing
- calterah-semiconductor
- huawei-hisilicon
- imec
- infineon-technologies
- lunewave
- metawave
- novelda
- nxp-semiconductors
- oculii-ambarella
- provizio
- sensor-kinesis
- smartmicro
- spartan-radar
- stereovision-imaging-acquired-by-renesas
- texas-instruments
- uhnder
- vayyar-imaging
- zadar-labs
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

# mmWave Radar

*Kind: technology*

## Physics / mechanism

mmWave radar operates in the 30–300 GHz band (most automotive and industrial deployments use 76–81 GHz). Transmitted FMCW chirps reflect off targets; range is extracted from beat frequency, velocity from Doppler shift, angle from phased-array receive aperture. Key parameters: range resolution ∝ 1/bandwidth (4 GHz BW → ~3.75 cm), velocity resolution ∝ carrier frequency and chirp duration, angular resolution ∝ aperture size. Modern 77 GHz SoCs (TI AWR, NXP S32R, Vayyar) integrate TX/RX chains, ADC, and DSP on a single RFCMOS or SiGe die. MIMO virtual aperture extension pushes angular resolution below 1°. Point-cloud outputs now feed directly into neural inference pipelines on-chip.

## Competitive landscape

LiDAR dominates perception where point-cloud density matters; cameras dominate where texture/color is needed. mmWave wins on weather immunity, through-barrier sensing, and velocity-first use cases. Ultrasonic covers short-range parking (<5 m) at lower cost. Structured-light and ToF depth sensors compete in indoor/industrial but fail outdoors. Key differentiation axes:

## Cloudberry relevance

| Sensor | Range (typ.) | Weather robustness | Velocity direct |
|---|---|---|---|
| mmWave radar | 0.1–300 m | High | Yes (Doppler) |
| LiDAR | 0.1–200 m | Medium | No (derived) |
| Camera | 0.1–150 m | Low | No (optical flow) |


GF's 22FDX and 12LP nodes are credible process targets for integrated mmWave front-ends; any fabless startup taping out 76–81 GHz silicon is natural deal flow. Cloudberry's semiconductor angle means evaluating RF CMOS process-node lock-in, antenna-in-package co-design IP, and calibration IP moats. Adjacent bets: photonic radar (FMCW LiDAR on-chip) shares architecture intuition. Watch startups commoditising the SoC layer and moving value into radar-native perception software or metamaterial apertures.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
