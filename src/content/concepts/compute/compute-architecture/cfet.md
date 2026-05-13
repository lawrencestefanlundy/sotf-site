---
type: concept
slug: cfet
canonical_name: CFET (Complementary FET)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- compute-architecture
related_concepts: []
companies_using:
- applied-materials
- asml
- atomica-formerly-x-fab-erfurt-spin-out
- atomicalis
- brewer-science
- cadence-design-systems
- cea-leti
- coventor-a-kla-company
- entegris
- fraunhofer-iisb
- imec
- intel
- lam-research
- pdf-solutions
- rapidus
- samsung-foundry
- screen-semiconductor-solutions
- siemens-eda-mentor
- siltronic
- soitec
- synopsys
- tokyo-electron-tel
- tsmc
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

# CFET (Complementary FET)

*Kind: technology*

## Physics / mechanism

CFET stacks nMOS and pMOS transistors vertically on the same footprint — n-type device on bottom, p-type on top (or inverted), sharing a common gate stack with separate source/drain contacts routed independently via backside power delivery. The key gain is cell area: a 2× standard-cell height reduction versus FinFET at equivalent logic density, enabling ~50% footprint shrink on inverters and NAND gates. Gate-all-around nanosheets (GAA/RibbonFET) are a prerequisite — CFETs are the next integration step beyond them. IMEC demonstrated functional CFET SRAM at 48nm contacted poly pitch in 2023; TSMC and Samsung are targeting sub-2nm-node insertion around 2027–2029.

## Competitive landscape

The primary alternative is conventional co-planar CMOS scaling with GAA nanosheets (Intel 20A/18A, TSMC N2, Samsung SF2), which avoids CFET complexity at the cost of retaining separate n/p diffusion tracks. Forksheet FET is a direct competitor — it separates n/p by a dielectric wall on the same plane, simpler process than CFET but less area-efficient. Backside power delivery networks (BSPDN) are complementary infrastructure, not a substitute.

## Cloudberry relevance

| Approach | Area scaling | Process complexity | Maturity |
|---|---|---|---|
| GAA nanosheet (co-planar) | Moderate | High | Production 2025 |
| Forksheet FET | Good | Very high | R&D / pilot |
| CFET | Best | Extreme | Early R&D |


For Cloudberry, CFET matters as a capital-intensive process node forcing increased IP disaggregation — new etch, selective epitaxy, and metrology tools create discrete vendor opportunities. GlobalFoundries won't chase sub-2nm, but portfolio companies supplying CFET-enabling process equipment or EDA (cell library re-architecture, parasitic extraction for 3D stacks) have clear insertion points at TSMC/Samsung capex cycles. Watch thermal budget management and wafer-bonding alignment startups — these are the near-term bottlenecks.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
