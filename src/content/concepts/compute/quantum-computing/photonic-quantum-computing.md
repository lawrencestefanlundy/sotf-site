---
type: concept
slug: photonic-quantum-computing
canonical_name: Photonic Quantum Computing
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
- aegiq
- allegro-microsystems-sige-semiconductor-via-ams-osram
- brightspec-bright-photonics
- hyperlight
- imec
- libreon
- lightmatter
- ntt-quantum-computing-division
- nu-quantum
- orca-computing
- parity-quantum-computing
- photonic-inc
- psiquantum
- qant
- quandela
- quantum-brilliance
- quantum-source
- quix-quantum
- qutech-tu-delft-tno
- single-quantum
- sparrow-quantum
- toshiba-europe-quantum-technology-division
- xanadu
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Photonic Quantum Computing

*Kind: technology*

## Physics / mechanism

Photonic quantum computing encodes qubits in optical modes — typically via photon polarisation, path, time-bin, or squeezed-light (continuous-variable) degrees of freedom. Gates are implemented through linear-optical networks (beam splitters, phase shifters) plus photon-number-resolving (PNR) detectors; non-determinism is the core liability, addressed by measurement-based / fusion-based architectures (PsiQuantum, Xanadu). Key parameters: photon indistinguishability (>99% demonstrated in III-V QDs), two-photon interference visibility, detector efficiency (SNSPDs now >95%), and loss per component (<0.1 dB/cm in Si₃N₄). Room-temperature operation and CMOS-fab compatibility are structural advantages over superconducting and trapped-ion rivals.

## Competitive landscape

Superconducting qubits (IBM, Google) dominate near-term gate fidelity (99.9% two-qubit) but require dilution refrigeration. Trapped ions (IonQ, Quantinuum) offer long coherence but slow gate rates (~kHz). Neutral atoms (QuEra, Atom Computing) scale in 2D arrays but remain early-stage. Photonics competes on interconnect-native architecture and ambient operation; it loses on deterministic entanglement generation.

## Cloudberry relevance

| Platform | Operating temp | Gate speed | Interconnect |
|---|---|---|---|
| Superconducting | ~15 mK | ~100 ns | Microwave, lossy |
| Trapped ion | Room (vacuum) | ~1–10 µs | Photonic (emerging) |
| Photonic | Room | ~ps (passive) | Native optical |


GlobalFoundries has qualified Si photonics PDKs (45SPCLO) directly relevant to integrated photonic quantum chip production — a rare foundry-level moat. Cloudberry's photonics portfolio sits upstream: waveguide platforms, PNR detector materials, low-loss packaging. Deal-flow angles include component suppliers to PsiQuantum/Xanadu, UK/EU fabless photonic quantum startups needing advanced-node tape-out partners, and SNSPD material plays (NbN, WSi) addressable via advanced-materials thesis.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
