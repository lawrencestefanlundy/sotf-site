---
type: concept
slug: photonic-compute-memory
canonical_name: Photonic Compute & Memory
aliases: []
kind: category
parent_concepts:
- photonic-systems
- photonic-compute
related_concepts:
- photonic-compute
- photonic-memory
- optical-neural-networks
- photonic-tensor-cores
- diffractive-deep-neural-network
- spatial-light-modulators
- silicon-photonics
- co-packaged-optics
- optical-interconnect
sources: []
frontier:
- Can any photonic memory technology (phase-change, magneto-optical, spin-wave) reach read/write endurance > 10⁸ cycles while maintaining sub-nanosecond latency?
- Which workload class — optimisation/Ising machines, FHE acceleration, FMCW LiDAR signal processing — is the first to demonstrate a sustained TCO advantage over GPU baselines in production?
- Does the energy cost of O/E/O conversion permanently cap the efficiency advantage of analog optical matmul, or does chip-scale WDM + in-situ photodetection change the accounting?
last_updated: 2026-06-02
tags:
- concept
- category
mention_count: 0
last_reorg_date: 2026-05-13
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: photonic-compute
  name: Photonic Compute
  path: /sotf-site/photonic-systems/photonic-compute/photonic-compute/
  macro: photonic-systems
- slug: photonic-memory
  name: Photonic Memory
  path: /sotf-site/memory/emerging-memory/photonic-memory/
  macro: memory
- slug: optical-neural-networks
  name: Optical Neural Networks
  path: /sotf-site/photonic-systems/photonic-compute/optical-neural-networks/
  macro: photonic-systems
- slug: photonic-tensor-cores
  name: Photonic Tensor Cores
  path: /sotf-site/photonic-systems/photonic-compute/photonic-tensor-cores/
  macro: photonic-systems
- slug: spatial-light-modulators
  name: Spatial Light Modulators (SLMs)
  path: /sotf-site/photonic-systems/modulators-detectors/spatial-light-modulators/
  macro: photonic-systems
- slug: silicon-photonics
  name: Silicon Photonics
  path: /sotf-site/photonic-systems/pic-platforms/silicon-photonics/
  macro: photonic-systems
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /sotf-site/manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: optical-interconnect
  name: Optical Interconnect
  path: /sotf-site/communications/optical-interconnect/optical-interconnect/
  macro: communications
---
**Photonic compute and memory** is the category of architectures that process or store information using light rather than — or alongside — electrons. It is the hardware substrate for the investment theses explored in **Photonic Compute Market** and **Optical Memory Market**, and covers two distinct device classes:

**Photonic compute** uses optical interference, diffraction, or nonlinear effects to perform operations — most commonly **matrix–vector multiplication** — at the speed of light and without charge transport. Implementations range from Mach–Zehnder interferometer meshes (integrated silicon-photonic) and [SLM](/sotf-site/photonic-systems/modulators-detectors/spatial-light-modulators/)-based free-space matmul, to **D²NNs** and [Photonic Tensor Cores](/sotf-site/photonic-systems/photonic-compute/photonic-tensor-cores/). The canonical figure of merit is **operations-per-joule at the system boundary**, which must account for optical-to-electrical-to-optical (O/E/O) conversion losses that can erase the in-fabric efficiency gain. [Optical Neural Networks](/sotf-site/photonic-systems/photonic-compute/optical-neural-networks/) are the primary inference target.

## Frontier

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->
