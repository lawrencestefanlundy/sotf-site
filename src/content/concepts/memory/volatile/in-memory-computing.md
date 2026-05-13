---
type: concept
slug: in-memory-computing
canonical_name: In-Memory Computing
aliases:
- in-memory compute
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- memory
- volatile
related_concepts:
- memcapacitor
- analog-computing
companies_using:
- aerospike
- axelera-ai
- exasol
- greenwaves-technologies
- gridgain-systems
- hazelcast
- imply-data
- kognitio
- memkind-memverge
- mevion-nand-x-polymem
- mythic
- panmnesia
- rain-neuromorphics
- redis-ltd
- sap-se
- scylladb
- singlestore
- sk-hynix
- speedata
- syntiant
- tetramem
- untether-ai
- upmem
- voltdb
- weebit-nano
ideas_referencing: []
sources:
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 13
descendants:
- memcapacitor
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 2
---

# In-Memory Computing

*Kind: technology · Attio deal count: 4*

## Physics / mechanism

Conventional compute separates memory and logic, forcing data across the von Neumann bottleneck—dominant cost in AI inference workloads. In-memory computing (IMC) embeds arithmetic directly in the memory array, typically using analog crossbar structures where Ohm's law and Kirchhoff's current summation perform matrix-vector multiplication (MVM) in O(1) time per layer. Key device substrates: SRAM-based digital IMC (Samsung, TSMC N5/N3), and analog non-volatile variants using PCM, RRAM, or OTS-based selectors. SRAM IMC achieves ~10–50 TOPS/W at 28–5nm; analog NVM claims 100+ TOPS/W but suffers weight precision limits (~4–6 bit effective), conductance drift, and write endurance constraints. Closest to productization: Mythic (RRAM), Syntiant (SRAM), Untether AI (SRAM near-memory).

## Competitive landscape


SRAM digital IMC is conservative but foundry-compatible and production-ready. Analog NVM IMC promises highest efficiency but requires custom fab and error-correction overhead. Near-memory compute (HBM + logic die, e.g., SK Hynix AiMX) is a softer alternative—no array-level compute but cuts bandwidth cost. PIM (Processing-in-Memory) from Samsung/SK overlaps significantly. Neuromorphic (Intel Loihi, IBM NorthPole) shares the co-location principle but targets spiking networks.

| Approach | TOPS/W | Precision | Foundry risk |
|---|---|---|---|
| SRAM IMC | 10–50 | 8-bit native | Low |
| Analog NVM IMC | 100+ | 4–6 bit effective | High |
| Near-memory (HBM+PIM) | 5–20 | Full | Low |

## Cloudberry relevance
Cloudberry's GlobalFoundries-LP mandate makes SRAM IMC at GF 22FDX directly relevant—22FDX's FD-SOI back-biasing suits analog-assist IMC at lower leakage than bulk CMOS. Deal-flow angle: fabless startups needing GF process design kits for IMC tapeouts, or IP licensing plays targeting edge-inference ASICs in automotive and industrial. Lunar Ventures' enterprise software angle is weaker here, but hardware-software co-design startups bridging IMC compilers (mapping DNNs onto crossbar topologies) are pipeline-relevant.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
