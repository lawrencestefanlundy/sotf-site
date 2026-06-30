---
type: concept
slug: photonic-quantum
canonical_name: Photonic Quantum
aliases: []
kind: technology
parent_concepts:
- compute
- quantum-computing
related_concepts: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2025-11-26-orca-computing-37m-series-b]]'
- '[[2026-06-04-q-memory-site]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 47
last_reorg_date: '2026-05-13'
sources_7d: 5
sources_30d: 26
recent_mentions:
- slug: 2026-06-04-q-memory-site
  title: Q-Memory — company website (q-memory.tech)
  date: '2026-06-04'
  kind: web
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2025-11-26-orca-computing-37m-series-b
  title: ORCA Computing $37M Series B (Temasek, Baillie Gifford, NVIDIA/NVentures, QIA, Morgan Stanley)
  date: '2025-11-26'
  kind: web
- slug: 2024-12-16-willow-and-the-race-to-quantum-advantage
  title: Willow and The Race to Quantum Advantage (Feat. Kris Kaczmarek)
  date: '2024-12-16'
  kind: substack
- slug: 2024-12-04-cubits-in-a-fridge-why-is-nobody
  title: Silicon Spin Quantum Computing (Feat. Himadri Majumdar, SemiQon)
  date: '2024-12-04'
  kind: substack
- slug: 2023-07-14-e08-optical-computing
  title: '🔮E08: Optical Computing'
  date: '2023-07-14'
  kind: substack
neighbors: []
---
## Physics / mechanism

Photonic quantum computing encodes qubits in photons—typically via polarisation, path, or time-bin degrees of freedom. Linear optical quantum computing (LOQC) uses beam splitters, phase shifters, and single-photon detectors to perform gate operations; measurement-based variants (MBQC) pre-entangle photons into cluster states then consume them through adaptive measurements. Key parameters: photon indistinguishability (>99% demonstrated in InGaAs QDs), two-photon interference visibility, detector efficiency (SNSPDs >98%), and loss per component (<0.1 dB on-chip is target). PsiQuantum targets silicon photonics fabs at scale; Quix Quantum ships 20+ mode processors; Xanadu's Borealis demonstrated 216-mode Gaussian boson sampling. Error correction overhead remains the critical bottleneck—photon loss is the dominant error channel.

## Competitive landscape

Competing modalities: superconducting qubits (IBM, Google) lead on gate fidelity and speed but require dilution refrigeration; trapped ions (IonQ, Quantinuum) offer best coherence but low clock rates; neutral atoms (Atom Computing, QuEra) scale spatially but face control complexity. Photonic competes primarily on room-temperature operation, telecom-wavelength networking, and fabrication in standard CMOS/silicon-photonics fabs.

| Approach | Operating temp | Integration path | Key weakness |
|---|---|---|---|
| Photonic | Room temp (detectors ~4K) | Si-photonics foundry | Photon loss, non-determinism |
| Superconducting | ~15 mK | Custom fab | Cryogenic infrastructure |
| Trapped ion | Room temp | Hybrid MEMS | Clock rate, shuttling overhead |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
