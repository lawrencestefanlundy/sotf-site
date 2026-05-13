---
type: concept
slug: risc-v
canonical_name: RISC-V
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- logic-and-paradigms
related_concepts: []
companies_using:
- akeana
- allwinner-technology
- andes-technology
- axelera-ai
- calista-semiconductors-now-part-of-rivos
- codasip
- esperanto-technologies
- greenwaves-technologies
- imagination-technologies
- imperas-software
- incore-semiconductors
- micro-magic
- nuclei-system-technology
- quintauris
- risc-v-international
- semidynamics
- sifive
- starfive-technology
- syntacore
- t-head-semiconductor-alibaba
- tenstorrent
- valtrix-systems
- ventana-micro-systems
- vroom-vroomvroom
ideas_referencing: []
sources:
- '[[2023-08-18-e11-in-conversation-with-lux-capital]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2024-eu-chips-act-final-text]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 10
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
---

# RISC-V

*Kind: technology · Attio deal count: 5*

## Physics / mechanism

RISC-V is an open-standard instruction set architecture (ISA) released under royalty-free licenses, originally from UC Berkeley (2010). Unlike proprietary ISAs, any entity can implement RISC-V cores without licensing fees. The base integer ISA is fixed; optional extensions (M, A, F, D, C, V for vector, etc.) are modular. Implementations span 32-bit microcontrollers to 64-bit server-class cores. Current SOTA: SiFive P870 at ~4 GHz on TSMC N3, competitive with Arm Cortex-A series on SPECint. Vector extension (RVV 1.0) enables AI/ML inference acceleration. Embedded cores (e.g., CV32E40P) run at sub-milliwatt budgets, dominant in IoT and secure enclaves.

## Competitive landscape


Arm is the primary incumbent — same application domains, vastly larger software ecosystem, stronger per-core performance at advanced nodes today. x86 competes at server/desktop but is irrelevant in embedded. MIPS and PowerPC are legacy residuals. The real competitive axis is not ISA performance but ecosystem maturity and vendor lock-in tolerance.

| ISA | Licensing | Ecosystem maturity | Edge/IoT traction |
|---|---|---|---|
| Arm | Royalty-bearing | Very high | Dominant |
| RISC-V | Free/open | Growing fast | Strong, accelerating |
| x86 | Proprietary | High (server/PC) | Negligible |

## Cloudberry relevance
Cloudberry's GlobalFoundries-LP mandate makes this directly relevant: GF fabs silicon for multiple RISC-V fabless customers (e.g., secure microcontrollers, automotive). Deal-flow angle is fabless startups designing custom RISC-V SoCs targeting defence, automotive, or edge-AI — sectors where supply-chain sovereignty and open ISA matter. Lunar Ventures' European portfolio has RISC-V-adjacent startups. Watch for opportunities in RISC-V security extensions and domain-specific accelerator companies using RISC-V as a control-plane core.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
