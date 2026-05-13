---
type: concept
slug: photonic-tensor-cores
canonical_name: Photonic Tensor Cores
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- photonic-compute
related_concepts: []
companies_using:
- ascalon-photonics
- baya-systems
- celestial-ai
- ephos
- finle-photonics
- hyperlight
- ibm-research-photonic-ai
- imec
- intel-silicon-photonics-intel-labs
- lightelligence
- lightmatter
- ligthen-formerly-li-photonics
- lumentum
- luminous-computing
- mitsubishi-electric-photonic-ai-labs
- optalysys
- phase-holographic-imaging-phix-photonics-assembly
- photonicare-xanadu-photonic-ai-division
- photonx-huawei-photonics-spinout
- quandela
- rockley-photonics
- salience-labs
- tsmc-silicon-photonics-rd
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

# Photonic Tensor Cores

*Kind: technology*

## Physics / mechanism

Photonic tensor cores perform matrix-vector multiplication in the optical domain, exploiting interference in Mach-Zehnder interferometer (MZI) meshes or micro-ring resonator (MRR) arrays to execute multiply-accumulate (MAC) operations at the speed of light with near-zero switching energy per operation. The fundamental unit is a tunable beamsplitter implementing a 2×2 unitary; cascaded N×N meshes (Clements or Reck topology) synthesize arbitrary unitary transforms. Matrix encoding is static (weights in phase shifters) or dynamic (EO modulators, ~10 ps switching). State-of-art demonstrations hit ~1–10 TOPS/mm² optical compute density with sub-pJ/MAC in silicon photonics at 1550 nm; Lightmatter's Passage and MIT/Stanford academic tapeouts represent leading integration points. Analog precision remains the constraint: 4–6 effective bits without error correction.

## Competitive landscape

Electronic ASICs (Nvidia H100, Groq LPU, Cerebras) dominate at scale, offering 8–16-bit precision with mature toolchains. Photonic cores trade precision and programmability for energy efficiency at high bandwidth. In-memory compute (SRAM/DRAM MAC, e.g. Mythic, Untether) occupies the mid-ground. Photonic vs. electronic vs. hybrid comparison:

## Cloudberry relevance

| Axis | Electronic ASIC | Photonic Core | Hybrid (EO+CMOS) |
|---|---|---|---|
| Precision | 8–16 bit | 4–6 bit | 6–8 bit |
| Energy/MAC | ~1 pJ | ~0.01 pJ | ~0.1 pJ |
| Maturity | Production | Proto/early silicon | Lab–pilot |


GlobalFoundries' 45SPCLO (silicon photonics) PDK is a direct fabrication path for photonic tensor core startups—deal flow lands naturally at Cloudberry. Lightmatter, Luminous, and stealth-mode UK/EU teams (SiPh + III-V hybrid) are live pipeline. The key bet is whether analog precision reaches 6+ bits reliably before electronic efficiency curves close the gap. Package co-integration with CMOS memory (chiplet standards) is the near-term wedge worth underwriting.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
