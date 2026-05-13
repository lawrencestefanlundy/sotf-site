---
type: concept
slug: atomic-clocks
canonical_name: Atomic Clocks
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- sensing
- quantum-sensing
related_concepts: []
companies_using:
- accubeat
- atomic-time-aosense
- cerca-magnetics
- chengdu-spaceon-electronics
- duration-technologies
- excelitas-technologies
- infleqtion-formerly-coldquanta
- leonardo-finmeccanica
- microsemi-frequency-electronics-inc-fei
- microsemi-microchip-technology
- muquans-part-of-ixblue-exail
- ntsc-national-time-service-center
- nu-quantum
- oscilloquartz-adva-adtran
- quartzlock
- safran-timing-technologies
- spectratime-orolia
- stable-laser-systems
- stanford-research-systems-srs
- symmetricom-part-of-microsemimicrochip
- syrlinks
- temex-time-now-part-of-oroliasafran
- timetech-a-wrth-group-company
- weel-formerly-time-and-frequency-solutions
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

# Atomic Clocks

*Kind: technology*

## Physics / mechanism

Atomic clocks exploit the quantised transition frequency of an atom as a reference oscillator. A local oscillator (typically a quartz TCXO or VCXO) is locked to an atomic resonance via feedback: the interrogation signal is swept, the transition signal is detected (optically or via microwave absorption), and any frequency error corrects the oscillator. Caesium beam clocks define the SI second at ~9.192 GHz; commercial Cs standards reach 1×10⁻¹³ fractional frequency accuracy. Rubidium cell oscillators (10⁻¹¹–10⁻¹² accuracy) dominate size/cost-constrained applications. Optical lattice clocks push to 10⁻¹⁸ instability but remain lab-bound. Chip-scale atomic clocks (CSACs) using coherent population trapping (CPT) in Rb vapour cells achieve ~10⁻¹¹/day in <17 cm³ at ~120 mW—driven by Microsemi/Microchip, Safran, and SiTime's MEMS-enhanced variants.

## Competitive landscape

Rubidium VCXOs and oven-controlled XOs (OCXOs) compete below the CSAC tier on cost but lose badly on holdover under GPS-denied conditions. MEMS oscillators (SiTime, Resonant) close the gap in phase noise but not in absolute accuracy. Hydrogen masers outperform Cs in short-term stability (10⁻¹⁵ at 1 s) but are rack-sized. Optical atomic clocks (Sr, Yb, Al⁺) are the long-run successor technology.

## Cloudberry relevance

| Technology | Accuracy | SWaP | Cost |
|---|---|---|---|
| CSAC (Rb CPT) | ~10⁻¹¹ | <17 cm³, ~120 mW | ~$1,500–3,000 |
| OCXO | ~10⁻⁸ | Moderate | ~$50–500 |
| Cs beam standard | ~10⁻¹³ | Large | ~$30,000+ |


Miniaturised atomic timing is a direct enabler for GPS-denied navigation, 5G/6G synchronisation, and secure comms—all defence-heavy segments where Cloudberry's deep-tech positioning is relevant. Photonic integration of vapour cells (VCSEL interrogation, integrated optics) is an active fabless opportunity; GF's photonics PDK could support on-chip interrogation modules. CSAC companies seeking foundry partners or photonic co-integration are credible deal-flow. Lunar Ventures' seed exposure to timing IP could feed later-stage syndication.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
