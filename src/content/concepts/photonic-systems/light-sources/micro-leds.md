---
type: concept
slug: micro-leds
canonical_name: Micro-LEDs
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- light-sources
related_concepts: []
companies_using:
- aledia
- apple
- elux
- epistar
- glo-now-part-of-nanosys-azumo-lineage-via-google
- jade-bird-display-jbd
- kopin-corporation
- lextar-electronics
- lg-electronics-lg-display
- lumileds
- lumiode
- micledi-microdisplays
- mojo-vision
- optovate
- ostendo-technologies
- playnitride
- porotech
- quantum-display-formerly-leyard-subsidiary
- raysolve-optronics
- samsung-display
- saphlux
- sony
- tsmc-auo-au-optronics
- vuereal
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

# Micro-LEDs

*Kind: technology*

## Physics / mechanism

Micro-LEDs are inorganic III-nitride (typically GaN-on-Si or GaN-on-sapphire) or AlInGaP emitters with pixel pitch below ~100 µm, often 1–50 µm for high-density displays. Electroluminescence efficiency peaks at optimal current density; at micro-scale, external quantum efficiency (EQE) degrades due to surface recombination at mesa sidewalls — the "size-effect" problem. State-of-the-art EQE sits ~10–20% at small pitches without passivation; best-in-class (Porotech, Apple internal) pushes toward 40%+ with ALD sidewall passivation. Key fabrication bottleneck: mass transfer of millions of dies at yield >99.9999%. Peak brightness >1M nits; contrast ratio effectively infinite (per-pixel off-state).

## Competitive landscape

OLED is the primary incumbent — flexible, mature supply chain, good EQE, but limited peak brightness, burn-in susceptibility, and lifetime under high-luminance operation. LCD+mini-LED backlight is a near-term bridge. Quantum-dot color conversion (QDCC) layered on blue micro-LED is a leading color-patterning route vs. direct RGB epitaxy. Key competing approaches:

## Cloudberry relevance

| Approach | Peak Brightness | Lifetime | Maturity |
|---|---|---|---|
| OLED | ~1,000 nits | ~50k hrs | HVM |
| Mini-LED LCD | ~5,000 nits | >100k hrs | HVM |
| Micro-LED | >1M nits | >100k hrs (projected) | Pilot/early HVM |


Micro-LED intersects Cloudberry's core theses: GaN-on-Si epitaxy is a GlobalFoundries-adjacent process node question; compound semiconductor fabs (Silex, X-Fab) are potential portfolio adjacencies. Mass transfer tooling, driver IC design (CMOS backplane), and monolithic integration all represent fundable infrastructure gaps. Radiant Technologies' context around specialty display drivers is directly relevant. For Lunar Ventures, software-hardware co-design stacks for AR/XR headsets sit immediately downstream of micro-LED commercialization.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
