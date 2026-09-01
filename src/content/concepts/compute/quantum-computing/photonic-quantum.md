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
scorecard:
  viability: null
  drivers: null
  novelty: null
  diffusion: null
  impact: null
  timing_band: Unclear
  verdict: ''
scorecard_status: draft
mention_count: 89
sources_7d: 4
sources_30d: 13
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
**Photonic quantum computing encodes quantum information in light and processes it with waveguide circuits, squeezers and photon detectors; the 2026 literature shows the individual components improving measurably but no integrated machine, and loss remains the deciding parameter.**

## Summary

Photonic quantum computing uses optical modes rather than superconducting circuits or trapped ions as the carrier of quantum information. Two encodings dominate. The discrete-variable route builds small entangled states of single photons and stitches them into large resource states using probabilistic "fusion" measurements; without ancillary resources, the success probability of a fusion gate is capped at 1/2. The continuous-variable route uses squeezed light from optical parametric oscillators, homodyne detection, and non-Gaussian resources such as Gottesman-Kitaev-Preskill (GKP) states to encode logical qubits with intrinsic error robustness. Both routes are measurement-based: the computation is driven by detection outcomes fed forward into subsequent optics in real time.

The appeal is manufacturability and telecom compatibility. Photon pair sources, filters, modulators and pulse shapers can be patterned on silicon, silicon nitride or thin-film ferroelectrics using processes borrowed from classical integrated photonics. A single silicon chip has now been shown to host a biphoton frequency comb source, pump rejection, high-speed phase modulators and a four-channel pulse shaper together, delivering frequency beamsplitters with success probabilities above 94% and fidelities above 99.9%, and on-chip Bell-state tomography at 95.7(3)% fidelity. New material platforms are entering the same way: thin-film lithium tantalate microrings have produced correlated photon pairs across 1510 to 1570 nm at 24 MHz/mW^2, with heralded antibunching of g2_H(0) = 0.071 +- 0.004.

The parameters that decide the technology are loss, source brightness and indistinguishability, feedforward latency, and reproducibility. Loss is not merely a performance tax: in Gaussian Boson Sampling it destroys entanglement to the point where the output becomes classically simulable, which is why proposals now add optical parametric amplifier networks inside the interferometer to sustain quantum correlations under realistic loss. Latency decides whether measurement-based protocols run at all rather than in post-processing; an FPGA feedforward system with a fibre homodyne detector at greater than 95% quantum efficiency has demonstrated 196 ns total system latency. Reproducibility is a quieter problem: nominally identical squeezers show large threshold variations traced to crystal-edge termination and coating phases.

A fourth parameter is the interface to matter. Modular scaling and quantum memories require spin-photon interfaces, pursued via colour centres in diamond integrated as chiplets onto other photonic platforms, erbium dopants addressed individually in silicon photonic crystal waveguides, and single emitters in two-dimensional materials, which still fight blinking, spectral wandering and charge-noise broadening.

## Viability (unscored)

## Drivers (unscored)

## Novelty (unscored)

## Diffusion (unscored)

## Impact (unscored)

## Timing Unclear

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
