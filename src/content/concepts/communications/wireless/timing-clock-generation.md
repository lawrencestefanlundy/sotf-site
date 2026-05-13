---
type: concept
slug: timing-clock-generation
canonical_name: Timing / Clock Generation
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
- acacia-communications-now-cisco
- analog-devices-adi
- axtal
- bsquare-temex-ocxo-lines
- clockwork-systems
- emergence-photonics-formerly-ameritech
- epson-seiko-epson
- frequency-electronics
- integrated-device-technology-now-renesas
- leonardo-finmeccanica-timing-division
- microchip-technology-microsemi
- murata-manufacturing
- orolia-safran-timing-technologies
- oscilloquartz-advaadtran
- quintessent
- rakon
- renesas-electronics
- silicon-laboratories
- sitime-corporation
- skyworks-solutions
- texas-instruments
- timebeat
- txc-corporation
- wrth-elektronik-vectron-international
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 3
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Timing / Clock Generation

*Kind: technology · Attio deal count: 3*

## Physics / mechanism

Clock generation converts a reference oscillator into the timing signals that synchronise digital, RF, and mixed-signal systems. The core chain: a reference (crystal, MEMS, or atomic resonator) feeds a phase-locked loop (PLL) or delay-locked loop (DLL), which multiplies frequency and reduces jitter. Key parameters are phase noise (dBc/Hz at offset frequencies), RMS jitter (femtoseconds to picoseconds), frequency range, and lock time. State of the art: silicon TCXO references at ±0.5 ppm stability; integrated PLL jitter floors ~50 fs RMS in 7 nm FinFET; photonic-based optical frequency combs pushing sub-femtosecond jitter for defence and metrology applications.

## Competitive landscape


Dominant incumbent approach is quartz crystal + CMOS PLL (SiTime, TXC, Microchip/Vectron). MEMS oscillators (SiTime, Resonant/Murata) displace quartz in harsh environments with better shock/vibration resilience. Photonic frequency combs (Octave Photonics, imec spin-outs) target datacentre co-packaged optics and radar but remain expensive. Atomic clocks (Microsemi, Orolia) address GNSS-denied navigation. The real competitive axis is jitter floor vs. integration level vs. cost.

| Approach | Jitter floor | Integration | Cost band |
|---|---|---|---|
| Quartz + CMOS PLL | ~200 fs | High | $ |
| MEMS oscillator | ~100 fs | High | $$ |
| Photonic comb | <10 fs | Low (today) | $$$$ |

## Cloudberry relevance
For Cloudberry, clock generation is a direct adjacency to photonics and advanced packaging deal flow. Co-packaged optics demand sub-100 fs jitter references integrated at the chiplet level — a whitespace where a fabless startup on a GlobalFoundries photonics PDK (e.g. GF Fotonix) could compete. MEMS-on-CMOS monolithic integration is another angle. Radar / GNSS-denied navigation themes at Lunar Ventures make low-power atomic and MEMS clock startups pipeline-relevant.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
