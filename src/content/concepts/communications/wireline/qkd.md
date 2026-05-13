---
type: concept
slug: qkd
canonical_name: QKD (Quantum Key Distribution)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- communications
- wireline
related_concepts: []
companies_using:
- aliro-quantum
- arqit-quantum
- bt-group-quantum-networking
- crypta-labs
- euqci-speqtral
- evolutionq
- id-quantique
- kets-quantum-security
- luxquanta
- magiq-technologies
- ntt-quantum-cryptography-rd
- quandela
- quantinuum
- quantum-dice
- quantum-opus
- quantum-xchange
- quantumctek
- qubitekk
- qunu-labs
- sk-telecom-quantum-crypto-unit
- terra-quantum
- thinkquantum
- toshiba-europe-quantum-technology-division
- toshiba-japan-quantum-division
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

# QKD (Quantum Key Distribution)

*Kind: technology*

## Physics / mechanism

QKD encodes cryptographic keys onto individual photons using quantum states—typically polarisation or phase. Measurement by an eavesdropper collapses the quantum state, introducing detectable bit-error anomalies (QBER threshold typically <11% for BB84). Key protocols: BB84 (polarisation), E91 (entanglement), CV-QKD (continuous-variable quadratures). Current SOTA: trusted-node fibre networks at ~400 km (TOSHIBA, ID Quantique), satellite QKD demonstrated by China's Micius at >1,000 km. Practical key rates: ~10 kbps at 100 km over SMF. Twin-field QKD pushing repeater-less range toward 600 km. No quantum memory yet; metropolitan deployments are the commercial reality today.

## Competitive landscape

Post-quantum cryptography (PQC)—NIST-standardised lattice algorithms (CRYSTALS-Kyber, Dilithium)—is the primary competitor. PQC is software-only, zero infrastructure cost, deployable now. QKD wins on information-theoretic security (no computational assumption) but loses on cost and scalability.

## Cloudberry relevance

| Dimension | QKD | PQC | Classical TLS |
|---|---|---|---|
| Security basis | Physics | Computational hardness | Computational hardness |
| Infrastructure cost | High (photonic hardware) | Near-zero | Near-zero |
| Key rate at 100 km | ~10 kbps | Unlimited | Unlimited |


QKD is a photonics hardware problem at its core: single-photon detectors (SNSPD, InGaAs APD), laser sources, integrated photonic chips for miniaturisation. GF's silicon-photonics PDK (GF Fotonix) is a direct process adjacency—QKD transceivers migrating to SiPho PICs is the cost-reduction vector that makes volume deployments viable. Deal-flow angle: fabless QKD startups needing a manufacturable SiPho tapeout, or SNSPD detector companies intersecting with Lunar's deep-tech portfolio. Government procurement (defence, banking) de-risks early revenue.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
