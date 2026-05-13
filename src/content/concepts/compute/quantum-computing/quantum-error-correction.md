---
type: concept
slug: quantum-error-correction
canonical_name: Quantum Error Correction
aliases: []
kind: technology
parent_concepts:
- compute
- quantum-computing
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
---
## Physics / mechanism

Quantum error correction (QEC) encodes one logical qubit across many physical qubits, exploiting redundancy to detect and correct errors without measuring qubit state directly — preserving superposition. Stabiliser codes (surface code, colour code, Steane code) measure multi-qubit parity operators (stabilisers); violations flag error syndromes. Surface codes dominate near-term roadmaps: Google's 2024 demonstration showed below-threshold performance at distance-7, achieving logical error rate ~10× lower than physical (~10⁻³ per cycle). Practical fault-tolerant computation likely requires physical error rates <10⁻³ and thousands of physical qubits per logical qubit; current best physical qubits (superconducting, trapped-ion) sit at 10⁻³–10⁻⁴ per gate. The classical decoding bottleneck — real-time syndrome decoding at microsecond latency — is an acute engineering constraint.

## Competitive landscape

The dominant surface code competes with low-density parity-check (LDPC) codes offering better qubit overhead (fewer physicals per logical) but harder hardware connectivity. Bosonic codes (cat qubits, GKP) push error suppression into the hardware layer, reducing software overhead. Trapped-ion platforms favour colour codes; photonic platforms target measurement-based QEC with linear optics.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
