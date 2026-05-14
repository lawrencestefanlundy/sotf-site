---
type: concept
slug: cfet
canonical_name: CFET (Complementary FET)
aliases: []
kind: technology
parent_concepts:
- compute
- compute-architecture
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

CFET stacks nMOS and pMOS transistors vertically on the same footprint — n-type device on bottom, p-type on top (or inverted), sharing a common gate stack with separate source/drain contacts routed independently via backside power delivery. The key gain is cell area: a 2× standard-cell height reduction versus FinFET at equivalent logic density, enabling ~50% footprint shrink on inverters and NAND gates. Gate-all-around nanosheets (GAA/RibbonFET) are a prerequisite — CFETs are the next integration step beyond them. IMEC demonstrated functional CFET SRAM at 48nm contacted poly pitch in 2023; TSMC and Samsung are targeting sub-2nm-node insertion around 2027–2029.

## Competitive landscape

The primary alternative is conventional co-planar CMOS scaling with GAA nanosheets (Intel 20A/18A, TSMC N2, Samsung SF2), which avoids CFET complexity at the cost of retaining separate n/p diffusion tracks. Forksheet FET is a direct competitor — it separates n/p by a dielectric wall on the same plane, simpler process than CFET but less area-efficient. Backside power delivery networks (BSPDN) are complementary infrastructure, not a substitute.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
