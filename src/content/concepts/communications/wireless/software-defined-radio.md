---
type: concept
slug: software-defined-radio
canonical_name: Software-Defined Radio
aliases: []
kind: technology
parent_concepts:
- communications
- wireless
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

Software-defined radio (SDR) replaces fixed-function analog RF front-ends with programmable digital processing. A wideband ADC/DAC pair digitizes the signal close to the antenna; all filtering, modulation/demodulation, frequency selection, and protocol handling run in software on FPGAs, DSPs, or CPUs. Key parameters: instantaneous bandwidth (commodity SDRs: 10–200 MHz; high-end ADRV9009-class devices: up to 1 GHz), dynamic range (SNR/SFDR typically 60–80 dB), and latency (FPGA-based pipelines push below 1 µs). SoC integration—RF front-end + FPGA fabric on one die (Xilinx RFSoC, AD9361/9371)—is the current centre of gravity. Military/SIGINT-grade platforms extend to 18 GHz+ with 16-bit ADCs.

## Competitive landscape

Fixed-function RF ASICs (cellular modems, Wi-Fi chipsets) dominate volume markets on cost and power; SDR wins where flexibility, multi-band, or rapid protocol iteration matters. Competing approaches include heterodyne architectures with switchable filter banks, direct-conversion radios with firmware-tunable front-ends, and photonic RF processing (electro-optic sampling) for >100 GHz spans. The relevant comparison:

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
