---
type: concept
slug: photonic-memory
canonical_name: Photonic Memory
aliases:
- optical memory
- optical data storage
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- memory
- non-volatile-novel
related_concepts: []
companies_using:
- ayar-labs
- celestial-ai
- elight-formerly-epfl-spin-off-gnie
- hyperlight
- ibm-research-photonic-memory
- imec-photonics-research
- intel-silicon-photonics-group
- lightelligence
- lightmatter
- lionix-international
- lumentum
- luminous-computing
- microsoft-azure-quantum-photonics
- ntt-research-phi-lab
- optalysys
- phase-photonics
- phix-photonics-assembly
- photondelta-ecosystem-smart-photonics
- photonic-inc
- quix-quantum
- rain-neuromorphics
- rockley-photonics
- salience-labs
- tsmc-advanced-photonics
- xanadu
ideas_referencing: []
sources:
- '[[2023-07-14-e08-optical-computing]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2025-02-25-data-driven-vc-is-over]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 8
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Photonic Memory

*Kind: technology · Attio deal count: 0*

## Physics / mechanism

Photonic memory stores and retrieves data using light rather than electrons, exploiting phase-change materials (PCMs) or electro-optic effects in integrated photonic circuits. The dominant mechanism: GST (Ge₂Sb₂Te₅) or GSST thin films erase/write via laser pulses that toggle crystalline ↔ amorphous states, modulating optical transmission. Multi-level cell (MLC) operation demonstrated at 5+ levels per cell. On-chip read speeds reach sub-nanosecond; endurance typically 10⁵–10⁷ cycles before degradation. Retention >10 years projected for crystalline state. Leading academic demonstrations: Oxford, MIT, EPFL. Commercial activity nascent — Bodle Technologies (acquired), Lumenisity adjacent. Integration with silicon photonics waveguides is the active frontier; insertion loss and CMOS back-end compatibility remain unsolved at volume.

## Competitive landscape


Competing approaches: DRAM and SRAM remain dominant for compute-adjacent memory; their latency advantage shrinks as photonic interconnect bandwidth scales. MRAM and ReRAM offer non-volatility but stay electronic. In-memory computing via memristors (Mythic, Analog Devices) is the most direct architectural rival for inference workloads.

| Approach | Non-volatile | Optical I/O native | Maturity |
|---|---|---|---|
| PCM photonic | Yes | Yes | Lab/early proto |
| Electronic PCM (Intel Optane lineage) | Yes | No | EOL |
| ReRAM / memristor | Yes | No | Early commercial |

## Cloudberry relevance
Cloudberry's GF-LP fund positions around silicon photonics process enablement — photonic memory is a logical adjacency. Deal-flow angles: fabless startups needing GF's 90WG or 45CLO process nodes for PCM integration; materials suppliers qualifying GSST deposition. LiDAR and AI-accelerator co-design companies requiring near-memory optical compute are pipeline-relevant. Lunar Ventures' enterprise software lens matters less here, but any portfolio company targeting optical AI inference hardware should be tracked for crossover.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
