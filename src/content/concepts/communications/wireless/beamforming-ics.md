---
type: concept
slug: beamforming-ics
canonical_name: Beamforming ICs
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
- analog-devices-adi
- arralis
- cellium-technologies
- ericsson-silicon-internal
- eurecom-ercom-sige-semiconductor-ip-bluwave-ai
- gigsky-gapwaves
- hisilicon-huawei
- intel-mobileye-network-edge
- lyra-systems
- mediatek
- mixed-mode-technology-mmtc
- mixtela-metawave
- movella-formerly-mcube-kinduct
- nxp-semiconductors
- pharrowtech
- qualcomm
- renesas-electronics
- samsung-semiconductor
- sivers-semiconductors
- soitec
- stmicroelectronics
- syntiant
- uhnder
- wupatki-anokiwave
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

# Beamforming ICs

*Kind: technology*

## Physics / mechanism

Beamforming ICs steer antenna arrays by controlling the phase and amplitude of RF signals across individual elements, producing constructive interference in target directions and destructive interference elsewhere — without mechanical movement. Core architecture: phase shifters (4–6 bit resolution typical), variable gain amplifiers, T/R switches, and a combining network, all integrated per-channel. Monolithic designs in SiGe BiCMOS or bulk CMOS handle mmWave bands (28 GHz, 39 GHz, 77 GHz automotive radar, E-band backhaul). State-of-the-art 5G phased-array front-ends achieve <5 dB noise figure, >15 dBm saturated output per element, scanning ±60°. Channel counts range from 8 to 256+ in production silicon; latency for beam switching is sub-microsecond.

## Competitive landscape

Key competing approaches: optical beamforming (true time delay, avoids beam squint, still largely pre-commercial), digital beamforming (full flexibility, massive DSP/ADC power cost, dominates massive MIMO baseband), and hybrid beamforming (splits analog/digital, dominant in sub-6 GHz and early mmWave). Adjacent ICs: LNAs, PAs, and RF switches increasingly co-packaged or co-integrated. Main suppliers: Sivers Semiconductors, Movella/Anokiwave, Renesas (IDT lineage), Qualcomm, Intel (E-band), Analog Devices, and RFMD/Qorvo for GaAs alternatives.

## Cloudberry relevance

| Approach | Bandwidth | Power | Integration |
|---|---|---|---|
| Analog beamforming IC | Moderate | Low | High |
| Digital beamforming | High | High | Moderate |
| Optical true-time-delay | Very high | Medium | Low (today) |


Cloudberry relevance is direct: GF's 45RFSOI and 22FDX nodes are competitive process choices for beamforming IC design, creating potential portfolio co-investment with GF-LP alignment. Deal-flow angles include mmWave satcom (LEO terminal phased arrays), automotive radar scaling, and fixed wireless access chipsets — all capital-efficient fabless teams needing a process-aware investor who can facilitate GF shuttle access and derisk tape-out decisions.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
