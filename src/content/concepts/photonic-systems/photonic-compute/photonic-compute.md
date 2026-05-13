---
type: concept
slug: photonic-compute
canonical_name: Photonic Compute
aliases:
- photonic processor
- optical computing
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- photonic-compute
related_concepts: []
companies_using:
- ayar-labs
- celestial-ai
- cisco-acacia-silicon-photonics
- compass-photonics
- ephos
- ii-vi-coherent-corp
- imec-spin-outs-photonics-program
- intel-silicon-photonics-division
- leti-cea-leti
- lightelligence
- lightmatter
- liobate-technologies-now-part-of-hyperlight
- luminous-computing
- nano-x-novaphy-photonic-compute-division
- optalysys
- photonics-foundry-smart-photonics
- poet-technologies
- psiquantum
- quix-quantum
- ranovus
- rockley-photonics
- salience-labs
- sicoya-acquired-by-samsung
- silc-technologies
- xanadu
ideas_referencing: []
sources:
- '[[2025-03-12-project-mayhem-ai-inward-collapse]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2023-03-29-oxford-spinout-lumai-secures-11m-grant-to-power-optical-comp]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 15
descendants:
- diffractive-deep-neural-networks
- spatial-light-modulators
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 2
---

# Photonic Compute

*Kind: technology · Attio deal count: 0*

## Physics / mechanism

Photonic compute uses light instead of electrons to perform matrix-vector multiplications—the dominant operation in neural network inference. Photons propagate through Mach-Zehnder interferometer (MZI) meshes or microring resonator arrays; weight encoding happens via phase shifts or amplitude modulation. Core advantage: multiply-accumulate operations execute at the speed of light with near-zero dynamic power. Key figures of merit are TOPS/W (demonstrated >1000× over GPU in optical domain, though O/E/O conversion erodes this), bandwidth density (>10 Tbps/mm² on-chip), and precision (typically 4–8 bit equivalent). State of the art: Lightmatter's Passage interconnect, Luminous's in-memory photonic arrays, MIT/Stanford silicon photonics platforms. Integration with CMOS at 300mm wafers remains the manufacturing bottleneck.

## Competitive landscape


Competing approaches: in-memory SRAM/DRAM compute (Mythic, Analog Devices), analog resistive (Mythic, Syntiant), neuromorphic (Intel Loihi, IBM NorthPole). Adjacent: silicon photonics for interconnect (Ayar Labs, Celestial AI) often overlaps with compute claims. Electro-optic modulators and III-V bonding techniques (InP, GaAs) are enabling adjacent material plays.

| Approach | Latency | Power | Maturity |
|---|---|---|---|
| Photonic MZI mesh | Sub-ns | ~10 fJ/MAC optical | Pre-production |
| Analog SRAM compute | ~10 ns | ~1 pJ/MAC | Production (edge) |
| Digital GPU/TPU | ~100 ns | ~10 pJ/MAC | Mature |

## Cloudberry relevance
GlobalFoundries' silicon photonics PDK (GF Fotonix, 300mm) is a direct manufacturing hook—portfolio companies fabbing on GF get photonic IP access without captive fab risk. Deal-flow priority: companies using GF-compatible photonic processes for inference accelerators or optical interconnect, where Cloudberry can add fab-relationship alpha. Lunar Ventures' enterprise software lens intersects where photonic inference sits behind API abstractions. Watch optical compute startups requiring early GF tape-out commitments as a signal of seriousness.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
