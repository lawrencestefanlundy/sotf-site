---
type: concept
slug: wireless-power-transfer
canonical_name: Wireless Power Transfer
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- energy-power
- power-electronics
related_concepts: []
companies_using:
- convenientpower-cps
- daihen-corporation
- elix-wireless
- energous-corporation
- fraunhofer-iaf
- guru-rf
- hevo
- indra-renewable-technologies
- inpipe-energy
- ipt-technology
- metacharge
- momentum-dynamics
- murata-manufacturing
- nuvolta-technologies
- ossia
- powercast
- powermat-technologies
- reach-power
- solace-power
- spark-connected
- tdk-corporation
- volterio
- wibotic
- witricity
- wrth-elektronik
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Wireless Power Transfer

*Kind: technology*

## Physics / mechanism

Wireless power transfer (WPT) moves energy without galvanic contact via three dominant mechanisms: inductive coupling (near-field magnetic, <1 m, 85–95% efficiency at 100 W–22 kW in Qi/SAE J2954), magnetic resonance coupling (mid-range, 1–5 m, 70–90% efficiency, tolerant of misalignment via coupled LC resonators at matched frequencies), and far-field RF/microwave or laser-based approaches (rectenna arrays, <30% wall-to-load at useful range, but distance-independent geometry). Key parameters: coupling coefficient k, quality factor Q (kQ product governs range/efficiency tradeoff), operating frequency (6.78 MHz for AirFuel, 85–150 kHz for automotive), and thermal derating under misalignment. State of the art: GaN-based inverters push switching frequencies above 1 MHz with compact form factors; silicon carbide dominates high-power EV charging pads.

## Competitive landscape

Competing and adjacent approaches split by range and power class. Wired charging is the obvious baseline—lower cost, higher efficiency, zero radiation management overhead. For IoT/implantables, energy harvesting (RF ambient, piezo, thermoelectric) competes at sub-milliwatt scales. Capacitive WPT covers short-range, low-EMI niches. Laser/optical WPT (LaserMotive, Wi-Charge) targets line-of-sight, medium-range industrial use.

## Cloudberry relevance

| Approach | Range | Efficiency | Sweet spot |
|---|---|---|---|
| Inductive (Qi) | <5 cm | 85–95% | Consumer, EV |
| Magnetic resonance | 0.1–5 m | 70–90% | Industrial, EV floor |
| RF/Microwave | 1–100 m | 5–30% | IoT, space solar |


Cloudberry relevance sits at the semiconductor layer: GaN-on-Si and SiC power devices are the efficiency-defining components in WPT inverters and rectifiers, directly in GlobalFoundries' wafer fab addressable market. Deal-flow angles include fabless GaN/SiC power IC designers, resonator control ASICs, and coil-integrated passive chiplets. Lunar Ventures' seed exposure to deep-tech hardware startups may surface early-stage WPT companies needing semiconductor design partnerships or foundry access before Series A.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
