---
type: concept
slug: qkd
canonical_name: QKD (Quantum Key Distribution)
aliases: []
kind: technology
parent_concepts:
- communications
- quantum-comms
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

QKD encodes cryptographic keys onto individual photons using quantum states—typically polarisation or phase. Measurement by an eavesdropper collapses the quantum state, introducing detectable bit-error anomalies (QBER threshold typically <11% for BB84). Key protocols: BB84 (polarisation), E91 (entanglement), CV-QKD (continuous-variable quadratures). Current SOTA: trusted-node fibre networks at ~400 km (TOSHIBA, ID Quantique), satellite QKD demonstrated by China's Micius at >1,000 km. Practical key rates: ~10 kbps at 100 km over SMF. Twin-field QKD pushing repeater-less range toward 600 km. No quantum memory yet; metropolitan deployments are the commercial reality today.

## Competitive landscape

Post-quantum cryptography (PQC)—NIST-standardised lattice algorithms (CRYSTALS-Kyber, Dilithium)—is the primary competitor. PQC is software-only, zero infrastructure cost, deployable now. QKD wins on information-theoretic security (no computational assumption) but loses on cost and scalability.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
