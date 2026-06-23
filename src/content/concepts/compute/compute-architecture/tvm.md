---
type: concept
slug: tvm
canonical_name: Apache TVM
aliases:
- TVM
- Apache TVM
- Relax
- Relay
- AutoTVM
- Ansor
- microTVM
- BYOC
kind: compiler
parent_concepts:
- ai-compiler-landscape
- compiler-as-bottleneck-for-novel-hardware
related_concepts:
- mlir
- xla
- iree
- mlc-llm
- cuda-moat
sources: []
frontier:
- BYOC is the standard on-ramp for novel silicon — is it the mechanism a Cloudberry novel-hardware deal should plan to use, vs building a compiler from scratch?
- Has the MLIR-based stack permanently eclipsed TVM for NEW silicon, or does TVM's auto-tuning + edge/MCU reach keep it the default in its niche?
last_updated: '2026-06-22'
tags:
- concept
- compiler
- compute
- edge
- reference
descendants:
- mlc-llm
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: mlir
  name: MLIR (Multi-Level Intermediate Representation)
  path: /sotf-site/compute/compute-architecture/mlir/
  macro: compute
- slug: xla
  name: XLA / OpenXLA
  path: /sotf-site/compute/compute-architecture/xla/
  macro: compute
- slug: iree
  name: IREE (Intermediate Representation Execution Environment)
  path: /sotf-site/compute/compute-architecture/iree/
  macro: compute
- slug: mlc-llm
  name: MLC-LLM (Machine Learning Compilation for LLMs)
  path: /sotf-site/compute/compute-architecture/mlc-llm/
  macro: compute
---
> The **breadth / edge** compiler of the [AI Compiler & Heterogeneous Programming-Model Landscape](/sotf-site/compute/compute-architecture/ai-compiler-landscape/), and the closest historical precedent for "the cross-hardware compiler company" — a precedent that ended in absorption by NVIDIA (see **Octoml**). Two distinctive things matter for diligence: its **search-based auto-tuning** (a real differentiator vs [XLA / OpenXLA](/sotf-site/compute/compute-architecture/xla/)) and **BYOC**, the mechanism novel-silicon companies actually use to plug in.

## Origin

Started **2017** in the SAMPL group at the University of Washington (the DMLC ecosystem, also home to XGBoost/MXNet) by **Tianqi Chen** (PhD student, creator of XGBoost) and Prof. **Luis Ceze**, with Thierry Moreau and Jared Roesch. Paper: *"TVM: An Automated End-to-End Optimizing Compiler for Deep Learning"* (OSDI 2018, [arXiv 1802.04799](https://arxiv.org/abs/1802.04799), tier 1). Motivation: the N-frameworks × M-backends explosion, especially the long tail of **mobile/embedded/non-NVIDIA** targets. Apache Incubator Mar 2019; Top-Level Project Nov 2020.

## What it is (plain English)

An **open-source ML compiler stack**: model in (PyTorch/TF/ONNX) → optimised machine code out for a chosen target. Three distinctive pieces:

- **Two-level IR.** Graph IR (originally **Relay**, now **Relax** in the "TVM Unity" redesign — built for dynamic/symbolic LLM shapes, Python-first) sits above **TensorIR (TIR)**, the loop/tensor level where kernels are scheduled.
- **Auto-tuning (the differentiator vs XLA).** TVM treats kernel optimisation as a **search problem guided by ML** — "ML to optimise ML compilation." **AutoTVM** searches schedule templates by benchmarking candidates on real hardware; **Ansor/AutoScheduler** generates the search space automatically. It finds non-obvious hardware-specialised schedules, at the cost of **long compile/tuning times** (the recurring criticism). XLA, by contrast, leans on hand-written fusion rules + vendor libraries.
- **BYOC ("Bring Your Own Codegen").** The plug-in for custom hardware: register the op/graph patterns your chip handles, TVM partitions the graph, offloads matched subgraphs to your codegen+runtime, runs the rest on defaults.

## Heterogeneous-hardware angle (the key part)

The broadest backend claim in the field, and the only one that reaches deep into the edge:

- **Delivered backends:** CPU (x86/ARM), GPU via **CUDA, ROCm, Metal, Vulkan, OpenCL**, WebGPU/WASM, and crucially **microTVM** (microcontrollers / bare-metal MCUs) — a tier [XLA / OpenXLA](/sotf-site/compute/compute-architecture/xla/) and most MLIR stacks ignore.
- **Novel silicon plugs in via BYOC.** Real examples: ****Tenstorrent**** (`tt-tvm`), **Qualcomm Hexagon**. For an investor: when a wafer-scale / analog / optical / edge-NPU startup needs a software stack fast, **TVM+BYOC has been the default on-ramp** rather than writing a compiler from scratch — directly relevant to [Compiler as Bottleneck for Novel Hardware](/sotf-site/compute/compute-architecture/compiler-as-bottleneck-for-novel-hardware/) diligence.
- **Honest weaknesses (Modular's critique, broadly credible):** never delivered peak performance on modern Tensor-Core NVIDIA GPUs; **vendor fragmentation** (vendors forked it and drifted — the structural failure of "one compiler for all hardware" when commercial interests diverge); caught flat-footed by GenAI (FlashAttention-class kernels). Relax/Unity and **[MLC-LLM (Machine Learning Compilation for LLMs)](/sotf-site/compute/compute-architecture/mlc-llm/)** (on-device LLMs: browser via WebGPU, iOS, Android) are the answer.

## Status / momentum (2025-26)

Still actively maintained, Apache-governed (v0.25.0, 19 Jun 2025 — genuine engineering, not just patches), community-owned, **not** dependent on any single company. But the centre of gravity shifted: the original brain trust went to OctoML→NVIDIA, and momentum among *new* infrastructure projects favours **[MLIR (Multi-Level Intermediate Representation)](/sotf-site/compute/compute-architecture/mlir/)-based stacks** (OpenXLA, IREE, Mojo, Triton-adjacent). TVM has its own stack and was historically **not** MLIR-based; that remains true. Fair read: **mature, alive, uniquely strong at edge/LLM-on-device, but no longer the default substrate new silicon vendors reach for first.**

## Competitive read (vs a "new programming model" startup)

**The closest-ever precedent, and a sobering one.** TVM proved the technical thesis (one compiler spanning NVIDIA/AMD/Apple/edge/MCU/custom, with BYOC for novel silicon) but exposed two traps: (1) **the business doesn't hold its shape** — "sell a cross-hardware compiler" was too narrow a market (**Octoml** had to pivot to inference-serving), and vendor self-interest fragments any neutral standard; (2) **exit gravity points to the dominant silicon vendor** — the strongest independent attempt was absorbed by NVIDIA, which shut the cross-hardware product down. Underwrite a new entrant as "become the indispensable software layer one class of non-NVIDIA silicon must adopt, then get bought by that silicon's champion," not as "the independent Switzerland of AI compute" — TVM tried to be Switzerland and got annexed.

## Sources

- [TVM (OSDI 2018 / arXiv 1802.04799)](https://arxiv.org/abs/1802.04799) — origin, motivation, AutoTVM. *Tier 1.*
- [apache/tvm releases](https://github.com/apache/tvm/releases) — v0.25.0 (Jun 2025), active maintenance. *Tier 7.*
- [TVM docs — Bring Your Own Codegen](https://tvm.apache.org/docs/how_to/tutorials/bring_your_own_codegen.html) — how novel silicon plugs in. *Tier 7.*
- [MLC-LLM](https://llm.mlc.ai/) — TVM-lineage on-device LLM stack. *Tier 7.*
- [Modular — "What about TVM, XLA, and AI compilers?"](https://www.modular.com/blog/democratizing-ai-compute-part-6-what-about-ai-compilers) — fragmentation / GPU-perf-gap critique (competitor source, note bias). *Tier 6.*

**Flags:** intermediate release dates approximate (load-bearing fact — active releases through Jun 2025 — is solid).
