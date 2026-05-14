---
type: concept
slug: photonic-tensor-cores
canonical_name: Photonic Tensor Cores
aliases: []
kind: technology
parent_concepts:
- photonic-systems
- photonic-compute
related_concepts: []
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
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Photonic tensor cores perform matrix-vector multiplication in the optical domain, exploiting interference in Mach-Zehnder interferometer (MZI) meshes or micro-ring resonator (MRR) arrays to execute multiply-accumulate (MAC) operations at the speed of light with near-zero switching energy per operation. The fundamental unit is a tunable beamsplitter implementing a 2×2 unitary; cascaded N×N meshes (Clements or Reck topology) synthesize arbitrary unitary transforms. Matrix encoding is static (weights in phase shifters) or dynamic (EO modulators, ~10 ps switching). State-of-art demonstrations hit ~1–10 TOPS/mm² optical compute density with sub-pJ/MAC in silicon photonics at 1550 nm; Lightmatter's Passage and MIT/Stanford academic tapeouts represent leading integration points. Analog precision remains the constraint: 4–6 effective bits without error correction.

## Competitive landscape

Electronic ASICs (Nvidia H100, Groq LPU, Cerebras) dominate at scale, offering 8–16-bit precision with mature toolchains. Photonic cores trade precision and programmability for energy efficiency at high bandwidth. In-memory compute (SRAM/DRAM MAC, e.g. Mythic, Untether) occupies the mid-ground. Photonic vs. electronic vs. hybrid comparison:

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
