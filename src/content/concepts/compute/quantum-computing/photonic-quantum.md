---
type: concept
slug: photonic-quantum
canonical_name: Photonic Quantum
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
- epiq-ecole-polytechnique-integrated-quantum
- hyperlight
- id-quantique
- imec
- lightmatter
- nu-quantum
- orca-computing
- parity-quantum-computing
- photon-spot
- photonic-inc
- photonics-for-quantum-p4q
- pixel-photonics
- psiquantum
- qant
- quandela
- quantinuum-photonics-division
- quantum-computing-inc-qci
- quantum-photonics-qpx
- quera-computing
- quix-quantum
- sparrow-quantum
- toshiba-quantum-technology
- xanadu
ideas_referencing: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 15
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 4
---

# Photonic Quantum

*Kind: technology · Attio deal count: 7*

## Physics / mechanism

Photonic quantum computing encodes qubits in photons—typically via polarisation, path, or time-bin degrees of freedom. Linear optical quantum computing (LOQC) uses beam splitters, phase shifters, and single-photon detectors to perform gate operations; measurement-based variants (MBQC) pre-entangle photons into cluster states then consume them through adaptive measurements. Key parameters: photon indistinguishability (>99% demonstrated in InGaAs QDs), two-photon interference visibility, detector efficiency (SNSPDs >98%), and loss per component (<0.1 dB on-chip is target). PsiQuantum targets silicon photonics fabs at scale; Quix Quantum ships 20+ mode processors; Xanadu's Borealis demonstrated 216-mode Gaussian boson sampling. Error correction overhead remains the critical bottleneck—photon loss is the dominant error channel.

## Competitive landscape


Competing modalities: superconducting qubits (IBM, Google) lead on gate fidelity and speed but require dilution refrigeration; trapped ions (IonQ, Quantinuum) offer best coherence but low clock rates; neutral atoms (Atom Computing, QuEra) scale spatially but face control complexity. Photonic competes primarily on room-temperature operation, telecom-wavelength networking, and fabrication in standard CMOS/silicon-photonics fabs.

| Approach | Operating temp | Integration path | Key weakness |
|---|---|---|---|
| Photonic | Room temp (detectors ~4K) | Si-photonics foundry | Photon loss, non-determinism |
| Superconducting | ~15 mK | Custom fab | Cryogenic infrastructure |
| Trapped ion | Room temp | Hybrid MEMS | Clock rate, shuttling overhead |

## Cloudberry relevance
Cloudberry's GlobalFoundries-LP mandate makes this directly relevant: GF's 45RFSOI and future silicon-photonics nodes are candidate platforms for photonic quantum chip production. Deal-flow angles include integrated photonics component suppliers (SNSPDs, low-loss waveguide IP), EDA/design-tool startups targeting PIC-for-quantum workflows, and materials plays in low-loss SiN or LiNbO₃. Lunar Ventures' deep-tech network surfaces early European photonic quantum spinouts—Quix, QuiX-adjacent teams—worth tracking for co-investment.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
