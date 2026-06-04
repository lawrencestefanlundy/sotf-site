---
type: concept
slug: quantum-communications
canonical_name: Quantum Communications
aliases: []
kind: technology
parent_concepts:
- communications
- quantum-comms
related_concepts: []
sources:
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 13
last_reorg_date: '2026-05-14'
sources_7d: 1
sources_30d: 1
recent_mentions:
- slug: 2024-12-16-willow-and-the-race-to-quantum-advantage
  title: Willow and The Race to Quantum Advantage (Feat. Kris Kaczmarek)
  date: '2024-12-16'
  kind: substack
neighbors: []
---
## Physics / mechanism

Quantum communications exploits quantum mechanical properties—superposition, entanglement, no-cloning theorem—to transmit information with information-theoretic security. The dominant near-term protocol is QKD (Quantum Key Distribution), specifically BB84 (polarisation-encoded photons) and its variants. Key parameters: QBER (quantum bit error rate, must stay <11% for BB84), secret key rate (SKR, currently ~Mbps over ~100 km fibre, dropping sharply beyond), and transmission distance (record ~1,000 km via satellite relay, Micius). Repeater-based long-haul requires quantum memory with coherence times >ms—still pre-commercial. Hardware stack: single-photon sources (InGaAs SPADs, SNSPDs), entanglement sources (SPDC crystals), and classical post-processing ASICs. CV-QKD (continuous variable) is an alternative gaining ground for telecom-compatible integration.

## Competitive landscape

Classical encryption (AES-256, RSA) is the incumbent—cheap, fast, widely deployed, but theoretically vulnerable to cryptanalytically relevant quantum computers (CRQC). Post-quantum cryptography (PQC, NIST-standardised: ML-KEM, ML-DSA) is the direct competing approach—software-only, backward-compatible, deployable today, and structurally cheaper. QKD's differentiation is forward secrecy against both classical and quantum adversaries and physics-based rather than computational security guarantees.

| Approach | Deployment cost | CRQC resistance | Infrastructure change |
|---|---|---|---|
| QKD | High | Yes | Major (dedicated fibre/satellite) |
| PQC | Low | Assumed | Minimal |
| Hybrid QKD+PQC | High | Strong | Major |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
