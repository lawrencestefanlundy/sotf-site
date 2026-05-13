---
type: concept
slug: mmwave
canonical_name: mmWave (24-100 GHz)
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
- celeno-communications-acquired-by-renesas
- echodyne
- endresshauser-vega-acquisition-context-endresshauser-radar
- ericsson
- gapwaves
- infineon-technologies
- intel
- keysight-technologies
- metawave
- movella-formerly-mcube
- nokia
- nxp-semiconductors
- octave-biosciences-acconeer
- ori-industries-now-ori
- pivotal-commware
- qualcomm
- robotic-research-ainstein
- samsung-electronics
- siklu-acquired-by-ceragon
- sivers-semiconductors
- spark-microsystems
- tensorcom
- texas-instruments
- vayyar-imaging
- wispry
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

# mmWave (24-100 GHz)

*Kind: technology*

## Physics / mechanism

Millimeter-wave spans 24–100 GHz (wavelengths 3–12 mm), sitting between microwave and sub-THz. Propagation is governed by free-space path loss scaling with f², plus oxygen absorption peaks near 60 GHz (~15 dB/km) and rain fade. Useful upside: high bandwidth (multi-GHz channels vs. tens of MHz at sub-6 GHz), tight beamforming due to short wavelength, and dense spatial reuse. State-of-the-art phased arrays integrate 64–256 antenna elements with beam-steering latency <1 µs. Key parameters: EIRP (typically 40–55 dBm for 5G NR FR2), NF (~5–8 dB at 28 GHz in SiGe/GaN front-ends), and link budget limited to ~100–200 m in NLOS urban environments.

## Competitive landscape

Competing approaches: sub-6 GHz 5G (better coverage, lower capacity), Wi-Fi 6E/7 at 6 GHz (unlicensed, shorter range), and sub-THz/D-band (100–300 GHz, emerging for backhaul). Key tension is coverage-vs-capacity. GaN-on-SiC dominates defence/backhaul power applications; SiGe BiCMOS leads cost-sensitive 5G CPE. RFFE consolidation is pressing chipmakers toward integrated transceiver+antenna modules.

## Cloudberry relevance

| Approach | Bandwidth | Range | Maturity |
|---|---|---|---|
| mmWave 24–100 GHz | 400 MHz–2 GHz | 50–200 m | Commercial (5G NR FR2) |
| Sub-6 GHz 5G | 10–100 MHz | 1–10 km | Mature |
| Sub-THz 100–300 GHz | 2–10 GHz | 10–50 m | Pre-commercial |


GlobalFoundries' RF process nodes (9SW, 8XP SiGe) are direct substrates for mmWave front-end ICs—deal flow here touches RFFE chiplets, beamforming ASICs, and advanced packaging for antenna-in-package (AiP) modules. Fixed wireless access and automotive radar (76–81 GHz FMCW) are capital-efficient entry markets. Lunar-stage companies building mmWave sensing (industrial, imaging, gesture) or low-cost AiP assembly IP are credible bets; the moat is process-antenna co-design, not pure algorithm play.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
