---
type: concept
slug: hearables-silent-speech
canonical_name: Hearables / Silent-Speech Interfaces
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- neural-interfaces
related_concepts: []
companies_using:
- apple
- bragi
- cakewalk-formerly-stages-cycling-cakewalk-audio-ai
- cogito-corp
- cogito-now-part-of-spring-health-ecosystem-removed-replacing
- earable-neuroscience
- essilorluxottica-nuance-audio-ray-ban-meta
- idun-technologies
- innomind-waverly-labs
- jabra-gn-audio
- logitech-zone-true-wireless-logi-bolt
- mediatek
- mimi-hearing-technologies
- nuheara
- olive-union
- ora-oura-adjacent-removed-replacing-with-valencell
- orfeo-soundworks
- oticon-demant
- qualcomm
- samsung-galaxy-buds-mx-division
- sonova-phonak-sennheiser-consumer
- sony
- speechless-sonica-ai
- titan-titan-hst-kokoon-technology
- whisper
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

# Hearables / Silent-Speech Interfaces

*Kind: technology*

## Physics / mechanism

Hearables combine in-ear or on-ear transducers with signal processing to capture biosignals — EMG from facial/jaw muscles, EEG from temporal cortex, ultrasonic Doppler of articulatory movement, or bone-conducted vibration — and decode intended speech without audible vocalisation. Silent-speech interfaces (SSIs) typically chain a sensor array, analog front-end ASIC, edge ML inference (transformer or RNN), and BLE/UWB radio. Key metrics: word-error rate (<10% is competitive; best lab demos hit ~5% on constrained vocabularies), inference latency (<200 ms end-to-end for conversational use), and power budget (<5 mW continuous for all-day wear). Current SoA: Meta/CTRL-Labs wrist EMG, Whisper Chip integration in TWS, Halo Neuroscience ear EEG. Commercialisation bottleneck is electrode-skin contact variability and per-user calibration overhead.

## Competitive landscape

The primary modality competition is laryngeal microphone / sub-vocal capture (simpler, worse in noise), EEG headbands (higher SNR, non-portable form factor), and ultrasound throat patches. Adjacent: GaN/SiC MEMS microphones with beamforming, photoplethysmographic biosensing reusing existing TWS optics, and radar-based lip-reading (60 GHz mmWave). Processing alternatives split between on-device neuromorphic ASICs (Innatera, Syntiant) and offload to companion SoC.

## Cloudberry relevance

| Approach | SNR/accuracy ceiling | Power | Form factor |
|---|---|---|---|
| Surface EMG | Medium (~85% WER floor) | 1–3 mW | Conformable patch |
| Bone conduction mic | High (whisper-dependent) | <1 mW | Standard TWS |
| EEG temporal | High (lab) / Low (field) | 5–15 mW | Dedicated headband |


Cloudberry relevance sits at the ASIC and photonic sensor layer: custom analog-front-end ASICs for low-noise biopotential acquisition are a GlobalFoundries 22FDX sweet spot (mixed-signal, low-power). SSI creates pull for specialised foundry process nodes and novel electrode materials (advanced materials angle). Deal-flow: sensor fusion startups needing tape-out capital, neuromorphic inference chip plays, and photonic biosensing (PPG/LiDAR-in-ear) are all plausible Lunar or Cloudberry co-investment targets as TWS OEMs demand differentiated silicon.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
