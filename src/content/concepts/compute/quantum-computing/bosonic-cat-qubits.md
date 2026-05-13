---
type: concept
slug: bosonic-cat-qubits
canonical_name: Bosonic / Cat Qubits
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- quantum-computing
related_concepts: []
companies_using:
- alice-bob
- amazon-web-services-aws-center-for-quantum-computing
- anyon-systems
- bleximo
- chalmers-university-spinouts-wacqt
- delft-circuits
- diraq
- equal1-laboratories
- google-quantum-ai
- ibm-quantum
- iqm-quantum-computers
- neel-institute-quobly-adjacent-bosonic-work
- nord-quantique
- pritzker-molecular-engineering-eeroq
- qilimanjaro-quantum-tech
- qnami
- qruise
- quantum-circuits-inc-qci
- quix-quantum
- riken-quantum-functional-system-research-group
- xanadu
- yale-quantum-institute-qulab-spinout-pipeline
- zurich-instruments
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

# Bosonic / Cat Qubits

*Kind: technology*

## Physics / mechanism

Bosonic qubits encode quantum information in the continuous degrees of freedom of a harmonic oscillator—typically a superconducting microwave cavity—rather than a two-level spin. Cat qubits specifically exploit superpositions of coherent states (|α⟩ ± |−α⟩), where the code space lives in a degenerate subspace protected against single-photon-loss errors by design. The key mechanism is parametric two-photon driving (Kerr-cat or dissipative stabilisation), which suppresses bit-flip errors exponentially in |α|² while phase-flip errors grow only linearly—enabling biased-noise qubits. Current state of the art: Alice & Bob report bit-flip suppression >10⁵× at moderate mean photon number (~4–6), with T₂ phase-flip times ~1–10 µs. AWS/CQC (Quantinuum collaboration) and Yale groups are pursuing similar architectures. Fabrication relies on high-Q 3D or planar aluminium/niobium cavities at millikelvin temperatures.

## Competitive landscape

The primary competition is transmon-based superconducting qubits (IBM, Google), which are mature but require full active error correction on both error axes. Trapped-ion qubits offer high gate fidelity (>99.9%) but slow clock speeds. Photonic qubits (PsiQuantum, QuiX) exploit low decoherence but face deterministic gate challenges. Neutral atoms (Atom Computing, QuEra) offer scalable connectivity. Cat qubits sit between: hardware-level noise bias reduces classical control overhead substantially versus transmons, but require specialised cavity hardware not yet in foundry-ready processes.

## Cloudberry relevance

| Approach | Bit-flip suppression | Fab maturity | Gate speed |
|---|---|---|---|
| Cat qubit | Exponential (engineered) | R&D / custom | ~100 ns–1 µs |
| Transmon | None (active QEC) | Semi-foundry (IBM) | ~10–100 ns |
| Trapped ion | High (physical) | Custom fab | ~1–100 µs |


Cloudberry relevance centres on the fabrication supply chain: cat qubits require precision niobium/aluminium deposition, deep sub-micron Josephson junction patterning, and high-Q cavity machining—processes adjacent to compound semiconductor and photonic foundry capabilities. GlobalFoundries has explored superconducting process nodes; as that scales, cat qubit IP becomes a credible licensing target. Alice & Bob (Paris) is a direct deal-flow candidate. Lunar Ventures' early-stage mandate fits the component and control-electronics layer—cryo-CMOS, parametric amplifiers—where deep-tech semiconductor expertise creates genuine sourcing edge.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
