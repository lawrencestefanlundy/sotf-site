---
type: concept
slug: quantum-networks
canonical_name: Quantum Networks
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
- aegiq
- airbus-quantum-communications
- aliro-quantum
- amazon-web-services-aws-quantum-networks
- arqit-quantum
- bt-group-quantum-networking
- cisco-quantum-networking-rd
- eleqtron
- id-quantique
- kets-quantum-security
- origin-quantum
- quandela
- quantum-brilliance-network-nodes
- quantum-internet-alliance-qia-delft-spin-outs
- quantum-xchange
- quantumctek
- quantumpath-telefnica-quantum-network-rd
- quix-quantum
- qunnect
- sandboxaq-quantum-security-network
- sparrow-quantum
- thales-quantum-networks
- toshiba-japan-qkd-division
- toshiba-quantum-technology
- welinq
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

# Quantum Networks

*Kind: technology*

## Physics / mechanism

Quantum networks transmit quantum information between nodes using entanglement distribution and quantum state teleportation. The physical layer relies on photonic qubits—typically single photons at telecom wavelengths (1310 nm / 1550 nm)—propagating through optical fiber or free-space links. Key parameters: entanglement generation rate (current state-of-the-art: ~10 kHz over 50 km fiber), fidelity (>90% demonstrated in lab; <85% in deployed systems), and quantum memory coherence time (spin-photon interfaces in NV-diamond or rare-earth-doped crystals: microseconds to low milliseconds). Quantum repeaters remain the unsolved scaling problem—no deployed repeater exists yet. Point-to-point QKD links are commercially live (Toshiba, ID Quantique, QuantumCTek); multi-node entanglement networks are at prototype stage (QuTech Quantum Internet Alliance, AWS/Caltech).

## Competitive landscape

Classical encrypted networks (TLS 1.3, post-quantum cryptography algorithms like CRYSTALS-Kyber/Dilithium) directly compete on the near-term security use case. PQC is software-deployable today at near-zero marginal cost—the primary competitive threat to QKD. Adjacent photonic approaches: continuous-variable QKD (cheaper detectors, lower fidelity), satellite QKD (Micius heritage; SpaceQT, SpeQtral). Quantum memory materials—rare-earth crystals, atomic ensembles, silicon-vacancy diamond—compete on coherence and integration. Integrated photonic chip platforms (SiPh, InP) are the component battlefield.

## Cloudberry relevance

| Approach | Deployment readiness | Key limitation |
|---|---|---|
| QKD (fiber) | Commercial today | Distance-limited, no repeater |
| PQC (software) | Deployed at scale | Not information-theoretic secure |
| Satellite QKD | Early commercial | Cost, weather, latency |


Cloudberry's photonics and advanced materials thesis maps directly onto quantum network infrastructure—specifically photon sources, detectors (SNSPDs), and quantum memory substrates. GlobalFoundries' silicon photonics process (45RFSOI / upcoming SiPh platforms) is a credible integration path for co-packaged QKD transceivers. Deal-flow angle: fabless startups building entanglement sources or integrated photonic quantum chips needing foundry access. Lunar Ventures' European network surfaces early-stage plays in the QuTech/Delft ecosystem. The repeater problem creates a materials-and-packaging wedge where deep-tech capital is differentiated.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
