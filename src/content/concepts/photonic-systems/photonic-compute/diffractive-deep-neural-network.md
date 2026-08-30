---
type: concept
slug: diffractive-deep-neural-network
canonical_name: Diffractive Deep Neural Network
aliases:
- D2NN
- diffractive deep neural network
- programmable diffractive optical element stack
- diffractive optical computing
- multi-layer DOE
parent_concepts:
- free-space-photonics
- photonic-compute
related_concepts:
- spatial-light-modulators
- diffractive-optical-element
- optical-circuit-switching
- multicast-routing
- moe-all-to-all-collectives
sources: []
frontier:
- Can a D2NN stack hit ns-class switching by combining fast SLM tech (LCOS, DMD) with phase-only modulation?
- Does multicast-without-splitters scale beyond 16×2 ports demonstrated, and is the simulated 64×4 achievable in practice?
- Is the alignment + thermal stability of stacked free-space DOE elements production-grade for hyperscaler rack form factors?
- Where is the foundry-vs-no-foundry trade-off — is the absence of a foundry queue a real moat, or a manufacturability liability?
- Does the architecture compete with Microsoft/Kippenberg's soliton-microcomb OCS (sub-ns potential) or only with mechanical OCS (Lumentum/Coherent at ms-class)?
last_updated: 2026-05-27
tags:
- concept
- photonics
- optical-computing
- free-space-photonics
public_expressions:
- AVGO
- COHR
- GOOGL
- LITE
- MSFT
- NVDA
mention_count: 7
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: spatial-light-modulators
  name: Spatial Light Modulators (SLMs)
  path: /photonic-systems/modulators-detectors/spatial-light-modulators/
  macro: photonic-systems
- slug: diffractive-optical-element
  name: Diffractive Optical Element
  path: /photonic-systems/metasurfaces/diffractive-optical-element/
  macro: photonic-systems
- slug: optical-circuit-switching
  name: Optical Circuit Switching (OCS)
  path: /communications/optical-interconnect/optical-circuit-switching/
  macro: communications
- slug: multicast-routing
  name: Multicast Routing
  path: /compute/compute-architecture/multicast-routing/
  macro: compute
- slug: moe-all-to-all-collectives
  name: Moe All to All Collectives
  path: /life-frontier/ai-infrastructure/moe-all-to-all-collectives/
  macro: life-frontier
---
## What it is

A D2NN is a stack of diffractive optical elements (DOEs) where each layer applies a programmable phase transformation to an incoming light wavefront. The composition of multiple layers computes complex optical transformations, originally for classification (image → class) and more recently for arbitrary information routing.

**Architecture in words:** light passes through DOE1 → DOE2 → DOE3 → ... → output. Each DOE is implemented as a spatial light modulator (SLM): a 2D pixel array where each pixel applies a controllable phase delay. Reprogram the phase pattern, change the optical transformation.

**Trade-off:** SLM-class switching speed (single-µs to ms depending on technology — liquid-crystal SLMs slowest, LCOS/DMD faster) bounds the architecture's applicability. Sub-ns electrical switching is not in reach.

## Lineage

The lineage is genuinely a 6-year research arc with peer-reviewed milestones. The pedigree is real. The commercial productisation question is separate.

## What it could enable in AI infrastructure

The Zigzag application repurposes D2NN as an optical interconnect fabric for MoE all-to-all collectives:

1. **Native optical multicast without splitter losses.** Conventional optical multicast uses a 1×N power splitter (12dB loss minimum for 1×16). D2NN does multicast via constructive interference at multiple output ports directly. No splitter, no fixed pattern, programmable.

2. **Combined wavelength + spatial routing in one device.** Conventional OCS does spatial routing only; wavelength routing requires AWG/WSS in series. D2NN handles both in one stack.

3. **Per-layer fabric reconfig** if SLMs hit single-µs. Today's mechanical OCS (Google Apollo) sets topology once per workload. D2NN could potentially reconfigure mid-batch to match current expert-routing patterns.

4. **No foundry queue.** Free-space optical elements don't need a wafer process. Both a moat (no foundry capacity constraint) and a manufacturability risk (alignment + thermal stability + scaling).

## Competitive landscape

D2NN-based OCS is one of four credible architectures competing for the MoE all-to-all interconnect prize:

## Reading list

- **Lin & Ozcan 2018 (Science)** — original D2NN architecture paper
- **Yildirim et al. 2024 (Nat. Photonics)** — nonlinear D2NN
- **Dinç et al. 2024 (arXiv)** — D2NN as multicast OCS
