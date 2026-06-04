---
type: concept
slug: probabilistic-computing
canonical_name: Probabilistic Computing
aliases: []
kind: technology
parent_concepts:
- compute
- non-conventional
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-06-03'
tags:
- concept
- technology
mention_count: 2
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Probabilistic computing exploits stochastic behaviour — typically from p-bits (probabilistic bits) — rather than suppressing it. A p-bit is a tuneable random binary unit that fluctuates between 0 and 1 at rates controlled by an input signal; networks of p-bits implement Boltzmann-machine-style sampling natively in hardware. Implementations use low-barrier nanomagnets (stochastic MTJs), modified SRAM bitcells, or purpose-built CMOS circuits. MTJ-based p-bits operate at room temperature, switching at ~1 ns with energy ~1 fJ/operation — orders of magnitude below kT-scale quantum annealing overhead. Current SoA: Tohoku/Purdue academic chips at ~1k p-bit scale; commercial IP still pre-product. Target applications are combinatorial optimisation, Bayesian inference, and generative AI sampling at edge power envelopes (<1 mW).

## Competitive landscape

Competes directly with quantum annealers (D-Wave: ~5000 qubits, but cryogenic, $15M+ capex, limited coherence advantage on real problems) and classical FPGA/ASIC heuristic solvers (Fujitsu DAU, Hitachi CMOS annealer). Adjacent to neuromorphic computing (Intel Loihi, BrainScaleS) and analog in-memory compute. Key differentiator: room-temperature, CMOS-compatible fabrication at standard foundry nodes.

| Approach | Temperature | Foundry-compatible | Maturity |
|---|---|---|---|
| Quantum annealing | ~15 mK | No | Commercial |
| CMOS annealer | 300 K | Yes | Commercial |
| Probabilistic (p-bit) | 300 K | Partial | Research |
| Photonic p-bit | 300 K | Partial | Research (emerging) |

## Photonic p-bits (emerging, 2026)

## Target workloads

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- **Distributed vs central entropy** in photonic p-bit designs (per-p-bit element, or one QRNG feeding a conventional sampler)?
- **Does randomness quality/controllability bind, or is intrinsic noise good enough?** MTJ-defect noise is hard to scale; thermodynamic designs use engineered noise; Gibbs/Boltzmann sampling tolerates imperfect noise — so where does entropy quality change the *answer* rather than just the device engineering?
- **System-level benchmark** — when does anyone publish samples/sec/watt on a real end-to-end workload (not component-level entropy figures)?
- **Higher-order interactions + non-penalty constraint mapping** — is native higher-order + active search-space constraint handling a durable moat vs pairwise-only annealers?
- Does the 1000× (Normal) / 10,000× (Extropic) energy-efficiency claim survive peer review *and* survive to a system-level number?
- Programming model — without a CUDA-equivalent, who writes software at scale? (A compiler + "problem-translator" agent layer is the current answer; does it generalise beyond hand-holding?)
