---
type: concept
slug: photonic-wire-bonding
canonical_name: Photonic Wire Bonding
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- packaging
related_concepts: []
companies_using:
- ayar-labs
- blickfeld
- bright-photonics
- celestial-ai
- globalfoundries
- hyperlight
- ii-vi-coherent
- imec
- leti-cea-leti-spin-out-activity
- ligentec
- marvell-technology
- nanoscribe
- nippon-telegraph-and-telephone-ntt
- optoscribe
- phix-photonics-assembly
- photondelta
- poet-technologies
- rockley-photonics
- scintil-photonics
- sichuan-yichen-photonics
- sicoya
- teramount
- vanguard-photonics
- viasat-photonics-formerly-part-of-karlsruhe-institute-spin-o
- vpiphotonics
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

# Photonic Wire Bonding

*Kind: technology*

## Physics / mechanism

Photonic wire bonding (PWB) uses two-photon polymerization (2PP) direct-laser-write lithography to print freeform polymer waveguides in situ between optical components—chips, fibers, lenses—with sub-micron positional accuracy. The printed structures are typically acrylate or SZ2080 photoresist, with refractive index ~1.53–1.56 and insertion loss of 0.5–2 dB per bond depending on mode-field mismatch. Coupling efficiency >90% chip-to-fiber is demonstrated in research; commercial tools from Vanguard Automation (spun out of KIT) target <1 dB. Writing speeds are 10–100 µm/s; a single bond takes seconds. Key constraint is throughput at wafer scale and long-term thermal/humidity stability of the polymer.

## Competitive landscape

The primary competitor is edge coupling via lensed or cleaved fiber, which is cheaper but alignment-sensitive and not reworkable at scale. V-groove fiber arrays and silicon photonics grating couplers handle multi-channel I/O but require tight fabrication tolerances and degrade at non-standard wavelengths. Flip-chip bonding with spot-size converters offers high throughput but demands co-design across foundry and packaging. Evanescent coupling and adiabatic tapers are on-chip only. PWB's differentiation is alignment tolerance (±5 µm still works), 3D routing freedom, and heterogeneous integration across dissimilar platforms—GaAs, InP, SiPh, LiNbO₃.

## Cloudberry relevance

| Approach | Alignment tolerance | 3D routing | Heterogeneous integration |
|---|---|---|---|
| Lensed fiber | <1 µm | No | Limited |
| Grating coupler | ~5 µm | No | SiPh-native |
| Photonic wire bond | ~5 µm | Yes | Yes |


Direct relevance to Cloudberry's GlobalFoundries-LP mandate: GF's SiPh platform (45RFSOI, 300mm) needs scalable packaging; PWB is a credible last-meter solution for co-packaged optics in AI/HPC. Deal-flow angle: equipment makers (Vanguard-adjacent), photoresist/materials suppliers optimizing 2PP polymers, and fabless SiPh companies whose yield is packaging-limited. Lunar Ventures' hardware-layer interest maps to the instrumentation and process-control stack. PWB is also a potential enabler for quantum photonics packaging—a developing thesis area.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
