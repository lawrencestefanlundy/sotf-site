---
type: concept
slug: diffractive-deep-neural-networks
canonical_name: Diffractive Deep Neural Networks (D2NN)
aliases:
- D2NN
- diffractive ONN
- diffractive optical neural network
- holographic ONN
kind: technology
parent_concepts:
- photonic-systems
- photonic-compute
related_concepts:
- spatial-light-modulators
- holographic-volumetric-displays
- free-space-photonics
- metasurfaces-flat-optics
sources: []
frontier:
- Reconfigurable D2NN with telecoms-grade SLM — production-ready or still bench? (Coherix claim, 2026-05-06).
- Headline performance numbers for D2NN inference on transformer matmul — cleanly published comparison vs H100/B200 with methodology stated.
- Cascaded SLM count vs single-pass — what depth is achievable before optical loss compounds beyond useful precision?
- Edge form-factor for D2NN — coherent source, optical path, and alignment requirements at sub-watt deployments?
- Patent landscape — Ozcan/UCLA originating IP vs Envisics-lineage holographic IP vs newer entrants (CMU, Stanford, USTC). Where does Coherix sit?
last_updated: 2026-05-07
tags:
- concept
- technology
- photonics
- photonic-compute
- onn
- d2nn
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors:
- slug: spatial-light-modulators
  name: Spatial Light Modulators (SLMs)
  path: /sotf-site/photonic-systems/modulators-detectors/spatial-light-modulators/
  macro: photonic-systems
- slug: holographic-volumetric-displays
  name: Holographic / Volumetric Displays
  path: /sotf-site/photonic-systems/displays/holographic-volumetric-displays/
  macro: photonic-systems
- slug: free-space-photonics
  name: Free-Space Photonics
  path: /sotf-site/communications/fibre-and-free-space/free-space-photonics/
  macro: communications
- slug: metasurfaces-flat-optics
  name: Metasurfaces & Flat Optics
  path: /sotf-site/photonic-systems/metasurfaces/metasurfaces-flat-optics/
  macro: photonic-systems
---
*Architecture class within [ONNs](/sotf-site/photonic-systems/photonic-compute/optical-neural-networks/).*

## Physics / mechanism

| Implementation | Phase-shift element | Reconfigurable? | Status |
|---|---|---|---|
| Printed phase plates | 3D-printed dielectric stack | No (fixed at fab) | Original Ozcan 2018 demonstrations; lab scale |
| Photolithographically-patterned | Etched phase masks | No | Higher precision than 3D-printed |
| Reconfigurable **SLM**-driven | LCOS or metamaterial SLM | Yes | Bench scale; **Coherix** commercial bet 2026 |
| Metasurface-based | Active metasurfaces | Partially | Research |

**Origin:** Lin et al. (Ozcan group, UCLA) demonstrated the first all-optical D2NN classifier in *Science* 2018, with cascaded 3D-printed phase plates performing MNIST-class classification at the speed of light through the stack. The architecture has since spread to USTC, Stanford, CMU, and many others.

**Key parameters:**

- **Latency** sub-ns per layer (light propagation through optical path)
- **Energy** dominated by source laser and detector array (not the diffraction itself, which is "free")
- **Precision** historically the weak point — analog at every layer, error compounds with depth
- **Reconfigurability** is the major variable — fixed phase plates are fastest but task-locked; SLM-driven systems are slower (limited by SLM refresh) but reprogrammable per workload

## Distinguished from sibling architectures

| Architecture | Compute primitive | Where it lives | Key trade-off |
|---|---|---|---|
| **D2NN (this page)** | Diffraction through phase masks | Free space | Massively parallel, but precision compounds; reconfigurability tied to SLM speed |
| **MZI mesh ONN** (**Lightmatter**, **Lightelligence**) | Guided-wave Mach-Zehnder phase shifters | Silicon photonic IC | Foundry-fabable; but O(N²) phase shifters limits scale |
| **Photonic tensor cores** | Wavelength-multiplexed multiply-accumulate | Silicon photonic IC | High throughput; precision still 4-6 bit |
| **Photonic reservoir** | Fixed nonlinear dynamical system | Free-space or fibre | Good for time-series / ODEs; limited generality, no commercial breakout |
| **Analog optical (Salience)** | PCM crossbar with optical readout | Hybrid PCM + photonic | Foundry-adjacent; precision-bound |

## Why this matters now (2026)

The D2NN architecture has been a research curiosity for ~8 years. The bet **Coherix** makes (2026 spinout from **Envisics**) is that **(a) reconfigurable SLM-driven D2NNs with a production-grade [SLM](/sotf-site/photonic-systems/modulators-detectors/spatial-light-modulators/) hardware base are now commercialisable**, and **(b) the energy story (data movement is free in light propagation) wins on energy/inference at deployable form factors**. The "telecoms-grade holographic SLM" claim is the load-bearing IP, inherited from **Envisics**'s holographic-display lineage.

Open question: most demonstrated D2NN benchmarks are CNN-shaped (image classification, denoising). Transformer matmul (where most current AI inference cycles go) maps less obviously. The Coherix deck includes ODE solving and time-series, which suggests they may be pitching a workload-class beachhead away from transformers.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

See frontmatter `frontier:` block.

## Reading list

- *To be added — Ozcan UCLA originating Science 2018 paper + key follow-ups.* Run `/kb-research diffractive-deep-neural-networks` to populate `sources/papers/`.
