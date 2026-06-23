---
type: concept
slug: xla
canonical_name: XLA / OpenXLA
aliases:
- XLA
- OpenXLA
- Accelerated Linear Algebra
- StableHLO
kind: compiler
parent_concepts:
- ai-compiler-landscape
- compiler-as-bottleneck-for-novel-hardware
related_concepts:
- mlir
- cuda-moat
- tvm
sources: []
frontier:
- Is XLA already 'the CUDA of heterogeneous compute' at the graph layer? Largely yes — so any new graph compiler must beat it where it is WEAK (vendor-neutrality, exotic non-matmul silicon), not where it is strong.
- The best XLA backend (XLA:TPU) is closed and Google-owned. Does 'OpenXLA' stay open at the layer that matters, or does the value stay locked to Google's silicon?
last_updated: '2026-06-22'
tags:
- concept
- compiler
- compute
- reference
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: mlir
  name: MLIR (Multi-Level Intermediate Representation)
  path: /sotf-site/compute/compute-architecture/mlir/
  macro: compute
- slug: tvm
  name: Apache TVM
  path: /sotf-site/compute/compute-architecture/tvm/
  macro: compute
---
> The **graph-compiler** layer of the [AI Compiler & Heterogeneous Programming-Model Landscape](/sotf-site/compute/compute-architecture/ai-compiler-landscape/) — and the real incumbent for "one graph, many silicon." The most important diligence point for **Callosum**: when a founder claims to be inventing "the CUDA of heterogeneous compute," **XLA already largely is that**, in frontier-scale production. The challenge is not CUDA; it is XLA.

## Origin

**XLA (Accelerated Linear Algebra)** began inside Google as the compiler for TensorFlow, shipped **~2017** (year not re-confirmed against a primary source — flag). Its purpose: fuse and optimise the linear-algebra graph that TensorFlow (later JAX, PyTorch via PyTorch/XLA) emits, and crucially to be the compiler that targets Google's **TPU**, where there is no CUDA. **OpenXLA** (announced late 2022, GA **March 2023**) spun XLA out of the TensorFlow monorepo into an independent, consortium-governed open-source project.

## What it is (plain English)

A **graph compiler**: hand it a whole computation graph and it fuses operations, allocates memory, and emits optimised device code for a target backend. Its signature optimisation is operator **fusion** (collapsing e.g. add→exp→matmul into one kernel). It sits at a *higher* altitude than a kernel language like [Triton (OpenAI Triton)](/sotf-site/compute/compute-architecture/triton/) or CUDA — you describe the math, XLA generates the kernels. **StableHLO** is the portability contract at the front: a versioned, MLIR-serialisable high-level operator set that JAX/TF/PyTorch all emit, decoupling framework from compiler. XLA's internals migrated onto **[MLIR (Multi-Level Intermediate Representation)](/sotf-site/compute/compute-architecture/mlir/)**-based infrastructure (StableHLO; Shardy for sharding).

## Heterogeneous-hardware angle (the key part)

XLA is the closest *existing, production* thing to "one graph, many silicon" — which is exactly why a "we're inventing this" claim needs scrutiny. The same StableHLO graph compiles to **TPU, NVIDIA GPU, AMD GPU, Intel GPU, Apple GPU, CPU, and AWS Trainium/Inferentia.** The catch is **performance parity, not portability**: XLA:TPU is mature, closed-source, and the reason Google can train frontier models without NVIDIA; XLA:GPU is materially weaker (hand-written CUDA/cuDNN/Triton generally beats it on NVIDIA), and AMD/Intel backends reach only partial parity. So XLA delivers genuine *functional* portability (the graph runs everywhere) with **uneven performance portability**, and its deepest moat (TPU) is closed and Google-controlled — the central tension in the word "Open."

**The strategic fact:** XLA:TPU is the software layer that makes TPU a credible NVIDIA alternative. **Anthropic (Oct 2025) committed to up to ~1M TPUs (>1 GW online 2026), expanding to ~3.5 GW from 2027, with Google reportedly investing ~$40bn.** This is the live proof that "compile one model to non-NVIDIA silicon at frontier scale" is *already happening in production* via XLA — not a green field.

## Governance + adoption (2025-26)

Multi-vendor consortium — members include **Google, NVIDIA, AMD, Intel, Apple, Arm, Meta, AWS, Alibaba, Cerebras, Graphcore, Hugging Face.** Compiler under **JAX** (default) and **TensorFlow**, and the only path to TPU for **PyTorch** (via PyTorch/XLA — TPUs do not use the Triton/Inductor stack). **Governance caveat (flag):** no confirmation of a Linux Foundation move or a formal independent steering committee as of 2026 — still "Google-anchored consortium, formalisation incomplete."

## Competitive read (vs a "new programming model" startup)

**Substrate, incumbent, AND partly the very thing being claimed as new.** If the pitch is "single-source kernel languages (CUDA/SYCL) structurally fail for heterogeneous hardware," XLA is the strongest evidence that the *graph-compiler* answer already exists and is in frontier-scale production on non-NVIDIA silicon. The only defensible wedge against it: (a) performance parity across genuinely dissimilar architectures, and/or (b) vendor-neutrality where XLA is Google-centric. **XLA's hard limit — and the real white space — is architecturally exotic silicon (wafer-scale, in-memory/analog, optical), where its dense-matmul-fusion model breaks down.** A startup that genuinely targets post-von-Neumann silicon routes *around* XLA into white space; another GPU+TPU graph compiler collides with an incumbent that has already won (~70% confidence the "new model" overlaps heavily with prior art unless it commits to exotic silicon).

## Sources

- [OpenXLA is ready — Google Open Source blog, Mar 2023](https://opensource.googleblog.com/2023/03/openxla-is-ready-to-accelerate-and-simplify-ml-development.html) — launch, members, StableHLO/MLIR. *Tier 6.*
- [Accelerated Linear Algebra — Wikipedia](https://en.wikipedia.org/wiki/Accelerated_Linear_Algebra) — device/backend roster, StableHLO/Shardy. *Tier 6.*
- [Anthropic — Expanding use of Google Cloud TPUs, Oct 2025](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services) + [CNBC 23 Oct 2025](https://www.cnbc.com/2025/10/23/anthropic-google-cloud-deal-tpu.html) — TPU-at-frontier-scale via XLA. *Tier 6 / Tier 4.*

**Flags:** XLA's original year (~2017) not re-confirmed; OpenXLA formal governance unverified; cross-vendor "70-90% of CUDA perf" is a general ROCm/OpenCL benchmark, not XLA-specific.
