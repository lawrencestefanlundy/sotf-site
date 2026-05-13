---
type: concept
slug: software-defined-radio
canonical_name: Software-Defined Radio
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- communications
- wireless
related_concepts: []
companies_using:
- airspy
- analog-devices-adi
- andro-computational-solutions
- bittele-signalyst-sdrplay
- bsquare-atscsdr-practice
- canonical-gnu-radio-project-software-freedom-conservancy
- cohere-technologies
- combitech-saab-group
- deepsig
- epiq-solutions
- ettus-research-national-instruments-ni
- fairwaves
- hiber
- hume-technology-formerly-collins-aerospace-sdr-division-spin
- kratos-defense-srt-spectralnet
- lime-microsystems
- nutaq-innovation
- per-vices
- pronto-networks
- radiomobile-rad-hard
- silvus-technologies
- syrlink
- thales-group-radio-communications-division
- viasat-former-comtech-ef-data-sdr-units
- xilinx-amd
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

# Software-Defined Radio

*Kind: technology*

## Physics / mechanism

Software-defined radio (SDR) replaces fixed-function analog RF front-ends with programmable digital processing. A wideband ADC/DAC pair digitizes the signal close to the antenna; all filtering, modulation/demodulation, frequency selection, and protocol handling run in software on FPGAs, DSPs, or CPUs. Key parameters: instantaneous bandwidth (commodity SDRs: 10–200 MHz; high-end ADRV9009-class devices: up to 1 GHz), dynamic range (SNR/SFDR typically 60–80 dB), and latency (FPGA-based pipelines push below 1 µs). SoC integration—RF front-end + FPGA fabric on one die (Xilinx RFSoC, AD9361/9371)—is the current centre of gravity. Military/SIGINT-grade platforms extend to 18 GHz+ with 16-bit ADCs.

## Competitive landscape

Fixed-function RF ASICs (cellular modems, Wi-Fi chipsets) dominate volume markets on cost and power; SDR wins where flexibility, multi-band, or rapid protocol iteration matters. Competing approaches include heterodyne architectures with switchable filter banks, direct-conversion radios with firmware-tunable front-ends, and photonic RF processing (electro-optic sampling) for >100 GHz spans. The relevant comparison:

## Cloudberry relevance

| Approach | Flexibility | Power / cost | Bandwidth ceiling |
|---|---|---|---|
| SDR (FPGA/RFSoC) | High | Medium | ~8 GHz practical |
| Fixed ASIC | Low | Low | Protocol-locked |
| Photonic RF | Very high | High, early-TRL | >100 GHz |


SDR intersects Cloudberry's portfolio at multiple nodes. GlobalFoundries' 45RFSOI and 22FDX processes are the preferred silicon for RF front-ends and integrated transceivers—direct foundry relevance for fabless SDR startups. Photonic RF (coherent sampling, microwave photonics) is a credible next-generation SDR substrate, bridging the photonics angle. Deal-flow watch: FPGA-less SDR on custom silicon, defence/SIGINT miniaturisation plays, and spectrum-sensing infrastructure for LEO ground stations.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
