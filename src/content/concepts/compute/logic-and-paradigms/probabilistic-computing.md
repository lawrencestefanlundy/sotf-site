---
type: concept
slug: probabilistic-computing
canonical_name: Probabilistic Computing
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
- 1qbit
- agnostiq
- brainchip-holdings
- d-wave-systems
- extropic
- fujitsu-digital-annealer-division
- grai-matter-labs
- hitachi-cmos-annealer
- ibm-research-ibm
- innatera-nanosystems
- iprova
- kindred-systems-acquired-by-ocado-but-ip-active
- mindo-mindovation
- multiverse-computing
- normal-computing
- ntt-research-physics-informatics-lab
- probabilistic-computing-lab-intel-labs-intel
- prophesee
- qilimanjaro-quantum-tech
- quera-computing
- rain-neuromorphics
- stochastic-inc
- synsense-aictx
- tunneling-computing-tundra-computing
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 1
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Probabilistic Computing

*Kind: technology · Attio deal count: 1*

## Physics / mechanism

Probabilistic computing exploits stochastic behaviour — typically from p-bits (probabilistic bits) — rather than suppressing it. A p-bit is a tuneable random binary unit that fluctuates between 0 and 1 at rates controlled by an input signal; networks of p-bits implement Boltzmann-machine-style sampling natively in hardware. Implementations use low-barrier nanomagnets (stochastic MTJs), modified SRAM bitcells, or purpose-built CMOS circuits. MTJ-based p-bits operate at room temperature, switching at ~1 ns with energy ~1 fJ/operation — orders of magnitude below kT-scale quantum annealing overhead. Current SoA: Tohoku/Purdue academic chips at ~1k p-bit scale; commercial IP still pre-product. Target applications are combinatorial optimisation, Bayesian inference, and generative AI sampling at edge power envelopes (<1 mW).

## Competitive landscape


Competes directly with quantum annealers (D-Wave: ~5000 qubits, but cryogenic, $15M+ capex, limited coherence advantage on real problems) and classical FPGA/ASIC heuristic solvers (Fujitsu DAU, Hitachi CMOS annealer). Adjacent to neuromorphic computing (Intel Loihi, BrainScaleS) and analog in-memory compute. Key differentiator: room-temperature, CMOS-compatible fabrication at standard foundry nodes.

| Approach | Temperature | Foundry-compatible | Maturity |
|---|---|---|---|
| Quantum annealing | ~15 mK | No | Commercial |
| CMOS annealer | 300 K | Yes | Commercial |
| Probabilistic (p-bit) | 300 K | Partial | Research |

## Cloudberry relevance
GlobalFoundries' 22FDX and 12LP nodes are strong candidates for p-bit SRAM or MTJ integration — direct Cloudberry deal-flow angle. As optimisation demand scales in automotive, logistics, and edge AI, a fabless probabilistic-compute IP or chiplet startup riding GF process IP is a credible seed/Series A target. Lunar Ventures' appetite for physics-layer compute bets makes co-investment natural. Watch for university spinouts from Purdue, Tohoku, or Aalto commercialising MTJ p-bit arrays.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
