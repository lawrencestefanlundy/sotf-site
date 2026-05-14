---
type: concept
slug: mach-zehnder-modulators
canonical_name: Mach-Zehnder Modulators
aliases: []
kind: technology
parent_concepts:
- photonic-systems
- modulators-detectors
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
recent_mentions: []
neighbors: []
---
## Physics / mechanism

A Mach-Zehnder Modulator (MZM) splits an optical carrier into two arms, applies a phase shift in one or both arms via an electro-optic effect, then recombines them—constructive or destructive interference encodes data onto the light. In silicon photonics, phase shift is achieved by carrier depletion in a PN junction (plasma dispersion effect); in lithium niobate (LN) or indium phosphide (InP), via the Pockels effect. Key parameters: Vπ·L (drive voltage-length product, target <1 V·cm in thin-film LN), extinction ratio (>30 dB desirable), insertion loss, and electro-optic bandwidth. State of the art: thin-film LN (TFLN) MZMs demonstrate >100 GHz EO bandwidth, Vπ <2 V; silicon PIC MZMs run 50–70 GHz with higher Vπ (~5 V), dominant in data-centre transceivers at 400G/800G.

## Competitive landscape

| Modulator type | EO bandwidth | Vπ (typ.) | CMOS integration |
|---|---|---|---|
| Silicon PN-junction MZM | 50–70 GHz | ~5 V | Monolithic |
| Thin-film LiNbO₃ MZM | >100 GHz | 1–2 V | Heterogeneous bonding |
| InP MZM | 80–100 GHz | ~2 V | III-V foundry only |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
