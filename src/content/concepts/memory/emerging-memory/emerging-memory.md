---
type: concept
slug: emerging-memory
canonical_name: Emerging Memory
aliases:
- emerging memories
sources:
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2024-yole-emerging-memories-2024]]'
- '[[2026-06-22-beyond-cmos-device-layer-research]]'
- '[[2026-07-25-thoughts-on-ai-and-power]]'
verified: false
last_updated: '2026-08-31'
tags:
- concept
- stub
descendants:
- adc-bottleneck
- analog-in-memory-compute
- capram
- charge-domain-compute
- computational-storage
- cxl
- digital-in-memory-compute
- in-memory-computing
- memcapacitor
- pcm-phase-change-memory
- photonic-memory
- processing-in-memory
- rram-reram
- sram-cim
- storage-class-memory
mention_count: 12
frontier:
- Does continued scaling of BEOL M3D on-chip memory reduce total LLM serving energy, or does the saving from avoided off-chip HBM traffic saturate below the added array and thermal cost 2026 07 30 llmet enabling cross layer evaluation of emerging m3d memories for energy efficient llm serving?
- Does SOT-MRAM move from pilot to a qualified last-level-cache product at any foundry, and at what node and yield, given it was still R&D as of 2024-26 2026 06 22 beyond cmos device layer research?
- Does the 10% device-to-device variation measured on 300mm SOT-MRAM hold at full array scale, and does the 2-bit quantisation ceiling extend to workloads harder than MNIST 2026 06 05 evaluation of wafer scale sot mram for analog crossbar array?
- Does FeFET/HfO2-FeRAM actually reach ≥5% of embedded NV units by 2030, and which GF 22FDX design wins ship in the 2026-2027 window 2024 yole emerging memories 2024?
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-07-high-bandwidth-flash-the-full-report
  title: 'High Bandwidth Flash: The Full Report'
  date: '2026-07-07'
  kind: web
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2024-yole-emerging-memories-2024
  title: Yole Group — Emerging Non-Volatile Memories 2024
  date: '2024-10-15'
  kind: web
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
neighbors: []
---
## Physics / mechanism

The commercial driver is not raw device physics but the embedded flash scaling wall: 28/22nm is the last node for embedded flash, which needs 6-8 extra masks versus roughly 3 for MRAM, so the switch to eNVM (MRAM/RRAM/FeRAM) is an economic decision rather than a purely physical one beyond cmos device layer research. The second driver is data movement. Because these devices are two-terminal or compact three-terminal elements with a programmable conductance, they can be wired into analog crossbar arrays that perform vector-matrix multiplication in place, removing the fetch of weights across a memory bus evaluation of wafer scale sot mram for analog crossbar array.

Device-level parameters reported for 300mm-compatible SOT-MRAM include a 150% tunnel magnetoresistance ratio, 2 ns switching at under 1 V, 350 fJ energy dissipation, 0.1% write noise and 10% device-to-device variation; with 2-bit quantisation-aware training and noisy training as mitigation, the measured devices reached 95% on MNIST evaluation of wafer scale sot mram for analog crossbar array. The same paper notes that the bi-stable anisotropy and stochastic switching of SOT-MRAM can be used deliberately, for stochastic training of binary neural networks evaluation of wafer scale sot mram for analog crossbar array. Variation and noise are the recurring constraint for in-memory computing: IMC architectures use noisy computation operations that significantly harm training accuracy leveraging ecram for edge continual learning.

A distinct integration path is monolithic 3D (M3D), where emerging cache memories are built in the back-end-of-line above a logic chip, giving larger and denser on-chip memory to displace off-chip HBM traffic. Whether continued on-chip memory scaling with these technologies actually improves system energy efficiency for LLM serving is stated as an open question requiring cross-layer evaluation llmet enabling cross layer evaluation of emerging m3d memories for energy efficient llm serving.

## Competitive landscape

| Technology | Status per sources |
|---|---|
| eFlash | Incumbent; retains >50% of embedded NV at ≥40nm via 3D stacking; 28/22nm is the last node **2024 Yole Emerging Memories 2024** beyond cmos device layer research |
| STT-MRAM | Volume production: TSMC 22nm (16nm qualifying, automotive 2025), Samsung 28nm FD-SOI (mass production since 2019), GlobalFoundries 22FDX (production Feb 2020) beyond cmos device layer research; holds the embedded NV slot where endurance binds **2024 Yole Emerging Memories 2024** |
| SOT-MRAM | R&D/pilot as of 2024-26; imec 300mm perpendicular SOT-MRAM with field-free switching for last-level cache; TSMC/ITRI/NYCU 64kb β-tungsten SOT-MRAM at 1 ns switching beyond cmos device layer research |
| FeFET / HfO2-FeRAM | <0.5% of embedded NV units in 2024, forecast ≥5% by 2030; GF 22FDX FeFET volume customer adoption 2026-2027 **2024 Yole Emerging Memories 2024** |
| ReRAM / PCM | Evaluated as in-memory processing substrates in accelerator surveys cross domain acceleration of open modification search from c |
| ECRAM | Research device for edge continual learning under IMC constraints leveraging ecram for edge continual learning |

Emerging memory is not positioned as a replacement for the AI accelerator main-memory layer: FeFET does not displace HBM through 2030 **2024 Yole Emerging Memories 2024**. The adjacent challenger at that layer is High Bandwidth Flash, a NAND stack built like an HBM stack with TSVs on the package interposer, offering the same read bandwidth as an HBM4 stack with roughly 10x the capacity, with first memory samples expected in the second half of 2026 and first AI inference devices in early 2027 high bandwidth flash the full report. Workload-driven comparisons place ReRAM/PCM in-memory processing and 3D NAND/FeNAND in-storage processing alongside GPUs, near-storage FPGAs and DRAM near-memory processing rather than as a single winner cross domain acceleration of open modification search from c.

## Evidence base

- Wafer-scale 300mm-compatible SOT-MRAM measured at 150% TMR, 2 ns and <1 V operation, 350 fJ dissipation, 0.1% write noise and 10% device-to-device variation, reaching 95% on MNIST after quantisation-aware and noisy training (published 2025-10-29) evaluation of wafer scale sot mram for analog crossbar array.
- Yole's 2024 report projects FeFET and HfO2-FeRAM growing from <0.5% of embedded NV memory units in 2024 to ≥5% by 2030, with GF 22FDX FeFET reaching volume customer adoption in 2026-2027 **2024 Yole Emerging Memories 2024**.
- eMRAM is already in volume production at TSMC 22nm (16nm qualifying, automotive 2025), Samsung 28nm FD-SOI (mass production since 2019, cited at ~1000x faster and ~1/400 the write energy of its eFlash) and GlobalFoundries 22FDX (production February 2020) beyond cmos device layer research.
- SOT-MRAM remained R&D/pilot rather than volume through 2024-26, with imec demonstrating integrated 300mm perpendicular SOT-MRAM with field-free switching and a TSMC/ITRI/NYCU 64kb β-tungsten array switching in 1 ns beyond cmos device layer research.
- A 2026 cross-platform survey of open modification search accelerators compares GPUs, near-storage FPGAs, DRAM near-memory processing, ReRAM/PCM in-memory processing and 3D NAND/FeNAND in-storage processing, finding performance dominated by reference data movement rather than computation cross domain acceleration of open modification search from c.
- A 2026 survey covers volatile and non-volatile memory across room-temperature and cryogenic environments, including SRAM, DRAM, eDRAM, NAND/NOR Flash, RRAM, MRAM and FeFET, motivated by memory latency, energy, scalability and data movement bottlenecks emerging memory technologies at roomcryogenic temperature.

## Frontier (open questions)

- Does continued scaling of BEOL M3D on-chip memory reduce total LLM serving energy, or does the saving from avoided off-chip HBM traffic saturate below the added array and thermal cost llmet enabling cross layer evaluation of emerging m3d memories for energy efficient llm serving?
- Does SOT-MRAM move from pilot to a qualified last-level-cache product at any foundry, and at what node and yield, given it was still R&D as of 2024-26 beyond cmos device layer research?
- Does the 10% device-to-device variation measured on 300mm SOT-MRAM hold at full array scale, and does the 2-bit quantisation ceiling extend to workloads harder than MNIST evaluation of wafer scale sot mram for analog crossbar array?
- Does FeFET/HfO2-FeRAM actually reach ≥5% of embedded NV units by 2030, and which GF 22FDX design wins ship in the 2026-2027 window **2024 Yole Emerging Memories 2024**?

*Synthesised 2026-08-31 from 12 KB sources by the resynth pipeline; citations are KB source slugs.*
