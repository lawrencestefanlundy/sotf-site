---
type: concept
slug: quantum-repeaters
canonical_name: Quantum Repeaters
aliases: []
kind: technology
parent_concepts:
- communications
- wireline
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

Quantum repeaters solve the exponential photon-loss problem in long-distance quantum communication. Optical fibre attenuates ~0.2 dB/km at 1550 nm; beyond ~100 km, direct transmission of single photons becomes impractical. Classical amplification destroys quantum states (no-cloning theorem), so repeaters instead use entanglement swapping and quantum memory: entanglement is generated across shorter segments, stored in matter qubits (trapped ions, NV centres, rare-earth-doped crystals), then extended via Bell-state measurements. Key parameters: memory coherence time (target >1 s, current best ~1 s in Eu:Y₂SiO₅), memory-channel coupling efficiency (>90% needed, ~50% demonstrated), and entanglement generation rate. Multiplexed architectures (many parallel modes) are essential for practical throughput. No field-deployed repeater exists; lab demonstrations span <50 km segments.

## Competitive landscape

The primary alternative is trusted-node QKD networks—classical relay points that decrypt and re-encrypt, sacrificing end-to-end security but deployable today (Toshiba, ID Quantique, QuantumCTek). Satellite QKD (Micius-class) bypasses fibre loss for intercontinental links but introduces latency and coverage gaps. All-photonic repeaters (graph states, no matter memory) are an emerging third path, favoured by PsiQuantum and Quix Quantum lineages.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
