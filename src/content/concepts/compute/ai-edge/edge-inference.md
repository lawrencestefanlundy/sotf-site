---
type: concept
slug: edge-inference
canonical_name: Edge Inference
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2024-11-05-confidential-ai-the-dog-that-didnt]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2026-06-17-femtoai-company-profile]]'
- '[[2025-06-slm-future-agentic-ai-nvidia]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 26
frontier:
- Does the NVIDIA 40-70% substitution estimate hold in measured production agentic traffic, and what fraction of those invocations fit within a hundreds-of-mW sustained envelope rather than a plugged-in edge box?
- Can outlier-aware quantisation plus emerging non-volatile memory (QMC-style) deliver measured tokens/sec/W on silicon, and how much device-noise-induced accuracy loss survives at 1-3mW hearing-aid-class budgets?
- Do EMC-point tabulation and tail-aware latency models generalise beyond Jetson Orin Nano to ARM SoCs and NPUs, and what deadline-miss rate do they achieve under bursty 100k-cycle workloads?
- Does analogue RF computing over MU-MIMO reach useful MVM accuracy at claimed energy levels in a hardware demonstration, and what is the base station cost per served client?
- Do INT8 dispatch-invariance guarantees (H1+H2) extend to transformer/attention graphs and to non-ONNX-Runtime edge stacks, or is bit-exactness limited to Conv-dominated CNNs?
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-10-edge-buyer-kpi-sweep
  title: 'Edge-AI buyer KPI sweep: power envelope + energy per work; cost per token absent'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-07-high-bandwidth-flash-the-full-report
  title: 'High Bandwidth Flash: The Full Report'
  date: '2026-07-07'
  kind: web
- slug: 2026-06-17-femtoai-company-profile
  title: femtoAI (formerly Femtosense) — company profile, funding, leadership
  date: '2026-06-17'
  kind: web
- slug: 2025-06-slm-future-agentic-ai-nvidia
  title: Small Language Models are the Future of Agentic AI (NVIDIA Research)
  date: '2025-06-01'
  kind: web
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2024-11-05-confidential-ai-the-dog-that-didnt
  title: Confidential AI
  date: '2024-11-05'
  kind: substack
neighbors: []
---
## Physics / mechanism

Edge inference is the execution of a trained neural network on the device that generates or consumes the data, rather than in a datacentre. The binding constraint is not throughput but a fixed power and thermal envelope: edge silicon is procured against a per-unit BOM (typically $15-45, on 12-18 month RFQ cycles) and judged on energy per unit of work rather than cost per token edge buyer kpi sweep. Representative envelopes span hundreds of mW sustained with 1-2W peak for smart glasses, wake-word DSPs at 3-8mW, and hearing-aid steady-state budgets of 1-3mW; skin-contact devices are additionally capped by a ~48C surface limit with 41-42C design targets edge buyer kpi sweep. Where tokens do enter edge procurement, they arrive as a speed metric (tok/s, time-to-first-token), with tokens/sec/W emerging at the on-device-LLM tier edge buyer kpi sweep.

The demand-side case rests on model size collapsing rather than growing. NVIDIA Research argues that small language models are sufficiently powerful and more economical for most agentic invocations, that agents need narrow task competence rather than broad conversation, and that SLMs run locally on consumer hardware to give real-time, offline inference without network dependency; the paper estimates 40-70% of LLM queries in existing agentic systems could be served by specialised SLMs, and that paying 10-30x for unneeded capability is unsustainable at scale **2025 06 Slm Future Agentic Ai Nvidia**.

On-device SLM deployment is memory-bound as much as compute-bound. SRAM is fast but low-density; DRAM must hold static weights and dynamic KV caches simultaneously, creating bandwidth contention; Flash is dense but conventionally idle during inference, used only for initialisation qmc efficient slm edge inference via outlier aware quantizat. The QMC work proposes retraining-free outlier-aware quantisation paired with a heterogeneous memory organisation, separating inlier from outlier weights so that inliers occupy compact (and noisier) emerging non-volatile storage qmc efficient slm edge inference via outlier aware quantizat. A related packaging-level response is High Bandwidth Flash: a TSV-stacked NAND stack on the GPU interposer with HBM4-class read bandwidth at roughly 10x the capacity, with first memory samples expected in the second half of 2026 and first inference devices sampling in early 2027 high bandwidth flash the full report.

Latency modelling for deadline-aware deployment is less tractable than CPU/GPU frequency models assume. On an NVIDIA Jetson Orin Nano, sweeping the memory clock across the realistic upper EMC range (2133 to 3199 MHz) shifted median latency by +11% to +48% depending on workload, with a reproducible non-monotonic case (-9%) for a synthetic L2-resident kernel at top GPU clock; a GPU-frequency estimator profiled under one power profile and deployed under another underestimated latency by up to 32%, and tabulating the four lockable EMC points repaired most workloads where a parametric 1/f_emc term did not beyond cpu gpu frequency memory clock and tail effects in ed. Numerical reproducibility is also arithmetic-dependent: across four Raspberry Pi devices spanning Cortex-A53, A72 and A76 under ONNX Runtime CPU, microarchitecture was not observable in a fixed FP32 CNN's outputs, but holding hardware at Cortex-A76 and switching only the execution provider made FP32 outputs disagree on every CIFAR-10 image with a mean remaining precision of 14.97 of 23 mantissa bits, while INT8 QDQ post-training quantisation collapsed both axes to a single equivalence class int8 quantization makes arm edge inference dispatch invarian.

## Competitive landscape

| Approach | Mechanism | Evidence point |
|---|---|---|
| Digital MCU/NPU at fixed envelope | Conventional accelerators sized to mW-W budgets | Syntiant NDP250 claims 30 GOPS "in a microwatt envelope", KWS at 140µW; Ambiq cites KWS <1mJ/inference and IPO'd 30 Jul 2025 (NYSE: AMBQ) edge buyer kpi sweep |
| Sparsity-aware digital accelerator | Neuromorphic-inspired sparse dataflow | femtoAI SPU/SPU-001, claimed ~100x lower power and ~10x smaller footprint vs conventional edge AI; 100,000+ units shipped as of Dec 2025 femtoai company profile |
| Quantisation + heterogeneous memory | Split inlier/outlier weights across SRAM/DRAM/NVM tiers | QMC, retraining-free qmc efficient slm edge inference via outlier aware quantizat |
| Spiking / FPGA neuromorphic | Discrete temporal events, time-multiplexed 1-bit spike feeding, integer LIF neurons | Inference-only SNN accelerator for MNIST on low-cost FPGA a time multiplexed spiking neural network accelerator with p |
| Analogue in-materia compute | Learnable nonlinear edge functions realised in reconfigurable nanoscale silicon devices (RNPUs) forming analogue KANs | System-level aKAN implementation with mixed-signal interfacing physical analogue kolmogorov arnold networks based on reconf |
| Analogue RF computing | Base station broadcasts weight-encoded RF waveforms; client passive mixer performs the MVM | Requires a computing-centric physical layer controlling analogue MVM accuracy and energy analog rf computing a new paradigm for energy efficient edge |
| General-purpose SBC software optimisation | Migrating and restructuring compute on commodity boards | Hyperspectral-multispectral fusion optimised on Raspberry Pi after an initial implementation showed high computational time optimized embedded implementation of hyperspectral multispec |

The funding environment supports the category rather than any single approach: 80 semiconductor startups raised over $6.0B in Q2 2026, with edge silicon re-emerging on physical-AI and real-time on-device demand, and SiFive raising a $400.0M Series G for RISC-V CPU and AI IP semiengineering startup funding q2 2026.

## Evidence base

- NVIDIA Research (arXiv 2506.02153, Jun 2025) estimates 40-70% of LLM queries in existing agentic systems could be handled by specialised SLMs, and lists a 2025-26 lineup including Phi-4/Phi-3.5-mini, Llama 3.2 1B/3B, Ministral 3B/8B, Gemma 2 2B/9B and Qwen 2.5 0.5-3B **2025 06 Slm Future Agentic Ai Nvidia**.
- A 10 Jul 2026 buyer KPI sweep concludes (~85% confidence) that edge silicon is bought against a fixed power/thermal envelope with energy per unit work as the metric, and that cost-per-token is absent from procurement edge buyer kpi sweep.
- Memory-clock sweeps on a Jetson Orin Nano (16 Jun 2026) shift median latency by +11% to +48%, and cross-power-profile deployment of a GPU-frequency estimator underestimates latency by up to 32% beyond cpu gpu frequency memory clock and tail effects in ed.
- INT8 QDQ quantisation collapses ARM edge inference outputs to a single equivalence class across Cortex-A53/A72/A76 and execution providers, where FP32 retains a mean 14.97 of 23 mantissa bits of agreement (28 Jul 2026) int8 quantization makes arm edge inference dispatch invarian.
- High Bandwidth Flash memory samples are expected in H2 2026 with first HBF-based AI inference devices sampling in early 2027, at HBM4 read bandwidth and roughly 10x capacity (7 Jul 2026) high bandwidth flash the full report.
- femtoAI (formerly Femtosense, renamed mid-2025) had shipped 100,000+ SPU units and closed an undisclosed round as of Dec 2025 femtoai company profile.

## Frontier (open questions)

- Does the NVIDIA 40-70% substitution estimate hold in measured production agentic traffic, and what fraction of those invocations fit within a hundreds-of-mW sustained envelope rather than a plugged-in edge box?
- Can outlier-aware quantisation plus emerging non-volatile memory (QMC-style) deliver measured tokens/sec/W on silicon, and how much device-noise-induced accuracy loss survives at 1-3mW hearing-aid-class budgets?
- Do EMC-point tabulation and tail-aware latency models generalise beyond Jetson Orin Nano to ARM SoCs and NPUs, and what deadline-miss rate do they achieve under bursty 100k-cycle workloads?
- Does analogue RF computing over MU-MIMO reach useful MVM accuracy at claimed energy levels in a hardware demonstration, and what is the base station cost per served client?
- Do INT8 dispatch-invariance guarantees (H1+H2) extend to transformer/attention graphs and to non-ONNX-Runtime edge stacks, or is bit-exactness limited to Conv-dominated CNNs?

*Synthesised 2026-08-31 from 12 KB sources by the resynth pipeline; citations are KB source slugs.*
