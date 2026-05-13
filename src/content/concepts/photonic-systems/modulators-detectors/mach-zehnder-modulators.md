---
type: concept
slug: mach-zehnder-modulators
canonical_name: Mach-Zehnder Modulators
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- modulators-detectors
related_concepts: []
companies_using:
- acacia-communications-acquired-by-cisco
- bright-photonics
- ceyear-technologies
- ciena-wavelogic
- coherent-corp-formerly-ii-vi-finisar
- colour-formerly-orca-computing-platform-sparrow-quantum-sepa
- effect-photonics
- ephos
- fujitsu-optical-components
- hisilicon-huawei-optical
- hyperlight
- imec
- inphi-acquired-by-marvell
- intel-foundry-services-intel-silicon-photonics
- ligentec
- lumentum
- lumiphase
- photonics-mw-photonicsmultiworks-imec-spin-off-network-repla
- poet-technologies
- poeta-networks
- rockley-photonics
- salience-labs
- sicoya-acquired-by-globalfoundries
- sumitomo-electric-industries-sei-optifrontier
- tersera-photonics-formerly-elenion-technologies-assets-via-n
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

# Mach-Zehnder Modulators

*Kind: technology*

## Physics / mechanism

A Mach-Zehnder Modulator (MZM) splits an optical carrier into two arms, applies a phase shift in one or both arms via an electro-optic effect, then recombines them—constructive or destructive interference encodes data onto the light. In silicon photonics, phase shift is achieved by carrier depletion in a PN junction (plasma dispersion effect); in lithium niobate (LN) or indium phosphide (InP), via the Pockels effect. Key parameters: Vπ·L (drive voltage-length product, target <1 V·cm in thin-film LN), extinction ratio (>30 dB desirable), insertion loss, and electro-optic bandwidth. State of the art: thin-film LN (TFLN) MZMs demonstrate >100 GHz EO bandwidth, Vπ <2 V; silicon PIC MZMs run 50–70 GHz with higher Vπ (~5 V), dominant in data-centre transceivers at 400G/800G.

## Competitive landscape

| Modulator type | EO bandwidth | Vπ (typ.) | CMOS integration |
|---|---|---|---|
| Silicon PN-junction MZM | 50–70 GHz | ~5 V | Monolithic |
| Thin-film LiNbO₃ MZM | >100 GHz | 1–2 V | Heterogeneous bonding |
| InP MZM | 80–100 GHz | ~2 V | III-V foundry only |

## Cloudberry relevance

Electro-absorption modulators (EAMs) offer smaller footprint and lower drive voltage but worse linearity and higher loss—preferred in co-packaged optics where space dominates. Ring modulators compete on footprint and power but are temperature-sensitive and narrowband. For coherent 400ZR/800ZR, MZMs remain the reference architecture. MEMS-based modulators are early-stage but relevant for switching.


MZMs sit at the intersection of Cloudberry's photonics and semiconductor process interests. TFLN is a materials/fab story—wafer bonding, etch process development, foundry qualification—directly relevant to GlobalFoundries' silicon photonics roadmap and potential TFLN platform partnerships. Deal-flow angles: fabless TFLN modulator startups (Enlightra, POET adjacencies), EIC/PIC co-design IP plays, and component suppliers into 800G/1.6T coherent and LiDAR. Vπ reduction and packaging integration are the near-term value inflection points worth tracking.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
