---
type: concept
slug: optical-neural-networks
canonical_name: Optical Neural Networks
aliases: []
kind: technology
parent_concepts:
- photonic-systems
- photonic-compute
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-07'
tags:
- concept
- technology
mention_count: 0
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---
## Physics / mechanism

Optical neural networks (ONNs) encode matrix-vector multiplications—the dominant compute primitive in inference—into light propagation through programmable photonic circuits. Implementations split into two families: (1) Mach-Zehnder interferometer (MZI) meshes (Clements/Reck topologies) performing unitary transforms in O(N²) phase shifters, and (2) diffractive deep neural networks (D²NNs) using passive diffraction layers. Key parameters: latency sub-ns per layer, energy ~fJ/MAC at device level versus ~pJ/MAC for 7 nm CMOS, bandwidth density limited by modulator speed (currently 50–100 Gb/s per channel). SOA: Lightmatter's Passage achieving 16-TOPS photonic tile; Lightelligence, Luminous Computing, MIT/Soljačić group on MZI mesh accuracy (4–6 bit effective precision remains the hard floor).

## Competitive landscape

MZI mesh ONNs compete directly with GPU/TPU for inference and with in-memory compute (analog SRAM, PCM crossbars, RRAM). Adjacent approaches include free-space spatial light modulators (slower, lab-scale), electro-optic reservoir computing, and neuromorphic ASICs (Intel Loihi, IBM NorthPole). Precision is the shared weak point across all analog inference.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
