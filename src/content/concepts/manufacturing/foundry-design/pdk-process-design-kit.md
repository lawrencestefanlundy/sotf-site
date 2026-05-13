---
type: concept
slug: pdk-process-design-kit
canonical_name: PDK / Process Design Kit
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- foundry-design
related_concepts: []
companies_using:
- ansys-formerly-apachelumerical
- bespoke-silicon-group
- cadence-design-systems
- efabless
- europractice-imec-ic-service
- globalfoundries
- ihp-microelectronics
- imec
- intel-foundry-ifs
- luceda-photonics
- phoenix-software-part-of-synopsys
- pragmatic-semiconductor
- pulsic
- samsung-foundry
- semilab
- siemens-eda-mentor
- silvaco
- skywater-technology
- smic
- synopsys
- tower-semiconductor
- tsmc
- unum-semiconductor-formerly-proplus-design-solutions
- weebit-nano
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

# PDK / Process Design Kit

*Kind: technology*

## Physics / mechanism

A PDK is the formal interface between a semiconductor fab's process and a designer's EDA toolchain. It packages design rules (DRC), layer definitions, SPICE models (BSIM, PSP, Verilog-A), parameterised cell libraries (pcells), and extraction decks (LVS/RCX) into a versioned artifact. When a designer draws a gate, the PDK defines minimum poly pitch, gate-oxide capacitance, threshold voltage corners (TT/FF/SS/SF/FS), and parasitic RC budgets. Modern advanced-node PDKs (TSMC N3, Intel 18A, GF 22FDX) contain millions of DRC rules; photonic PDKs (imec iSiPP50G, GF Fotonix, AIM Photonics) add waveguide loss coefficients, coupling gap tolerances, and S-parameter compact models. PDK maturity is a primary proxy for process maturity—tape-out yield tracks PDK revision count closely.

## Competitive landscape

Open-source PDKs (SkyWater SKY130, GF 180MCU, IHP SG13G2) have disrupted the traditional NDA-gated model, lowering university and startup entry costs. Competing abstraction layers include DTCO flows (design-technology co-optimisation, blurs PDK boundaries at 3 nm and below) and chiplet/UCIe interface specs that partially decouple die-level design rules from package integration. Cloud-native EDA (Cadence JedAI, Synopsys.ai) is pushing PDK consumption toward API-based rather than file-based delivery.

## Cloudberry relevance

| Approach | Access model | Typical node | Openness |
|---|---|---|---|
| Foundry PDK (GF, TSMC) | NDA, per-design fee | 5 nm–180 nm | Closed |
| Open PDK (SKY130, GF180) | Apache 2.0 | 130–180 nm | Full |
| Photonic PDK (Fotonix, iSiPP) | MPW shuttle agreement | — | Semi-open |


For Cloudberry, PDK access is a due-diligence signal: a portfolio company with a validated GF Fotonix or 22FDX PDK integration has de-risked a critical path that kills most photonics/RF startups. GF's LP relationship means portfolio companies may negotiate PDK access or co-development terms faster than competitors—a structural moat. Startups building EDA tooling, compact modelling, or photonic component libraries on top of open PDKs represent direct deal-flow; PDK lock-in also determines which fabs a company can realistically exit toward.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
