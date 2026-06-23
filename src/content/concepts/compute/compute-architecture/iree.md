---
type: concept
slug: iree
canonical_name: IREE (Intermediate Representation Execution Environment)
aliases:
- IREE
- SHARK
kind: compiler-runtime
parent_concepts:
- ai-compiler-landscape
- compiler-as-bottleneck-for-novel-hardware
related_concepts:
- mlir
- xla
- tvm
- cuda-moat
sources: []
frontier:
- IREE is the open, AMD-backed answer on the literal 'one model, many backends' claim. Does AMD's backing make it the durable open standard, or stay a SHARK-distribution niche?
- Does a layer above IREE (a programming model / workload-placement runtime) capture value IREE itself doesn't, or does IREE's open+free+vendor-backed status commoditise that layer too?
last_updated: '2026-06-22'
tags:
- concept
- compiler
- runtime
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
- slug: xla
  name: XLA / OpenXLA
  path: /sotf-site/compute/compute-architecture/xla/
  macro: compute
- slug: tvm
  name: Apache TVM
  path: /sotf-site/compute/compute-architecture/tvm/
  macro: compute
---
> The **MLIR-native end-to-end compiler + runtime** of the [AI Compiler & Heterogeneous Programming-Model Landscape](/sotf-site/compute/compute-architecture/ai-compiler-landscape/) — the most direct realisation of "compile one model, run on many genuinely different backends." For diligence: of the open stacks, **IREE is the most direct competitor on the literal portability claim**, and it is now effectively **AMD-backed**, so it is free, vendor-funded, and motivated to break NVIDIA lock-in.

## Origin

Built by **Google** (open-sourced ~2019-2020; exact month not pinned — flag), pronounced "eerie." Purpose: an **[MLIR (Multi-Level Intermediate Representation)](/sotf-site/compute/compute-architecture/mlir/)-based, end-to-end compiler *and* runtime** — model → MLIR → deployable artefact → execute. Original emphasis was deployment that "scales up to the datacenter and down to mobile/edge."

## What it is (plain English)

Where MLIR is the toolkit and [XLA / OpenXLA](/sotf-site/compute/compute-architecture/xla/)/[Apache TVM](/sotf-site/compute/compute-architecture/tvm/) are graph compilers, IREE is a *complete product built with the toolkit*: a single flow from common ML frontends (TF, PyTorch via Torch-MLIR/Turbine) to a unified IR, plus a **lightweight runtime** to run the result, supporting both ahead-of-time and just-in-time compilation. It is the "compile once, target many" pitch realised as working open-source code.

## Heterogeneous-hardware angle (the key part)

This is where IREE comes closest to delivering the heterogeneous promise in practice. **Genuinely multi-backend:** CPUs (multiple ISAs), GPUs via **Vulkan, CUDA, ROCm, Metal, WebGPU**, plus a plugin path for custom accelerators. So it ships real cross-silicon *portability* from one model. Honest caveat: portability ≠ peak performance on every target — IREE inherits MLIR's reality that each backend's codegen quality is its own engineering effort, and per-vendor maturity varies (NVIDIA/CPU/AMD relatively mature; long-tail backends less so).

## Governance + adoption (2025-26)

Joined the **LF AI & Data Foundation** as a sandbox project (May 2024); develops under the `iree-org` GitHub org (no longer purely Google). Strongest adoption signal: **AMD is the major backer in practice** — AMD acquired Nod.ai, whose **SHARK** distribution is built on IREE, and **AMD submitted an IREE-based SDXL run to MLPerf (2 Apr 2025)**, i.e. IREE is in AMD's production benchmarking/deployment path as part of its CUDA-alternative ROCm-era stack. (Characterise as "AMD-backed and in AMD's stack," not "AMD's sole official compiler" — AMD has not declared it that.)

## Competitive read (vs a "new programming model" startup)

**The most direct competitor** to a portability-thesis startup: IREE already delivers single-model → multiple genuinely different silicon, open-source/Apache-2.0, MLIR-native, with a deep-pocketed industrial sponsor (AMD) motivated to make heterogeneous portability work. A startup must say *why IREE (free, vendor-backed) is structurally insufficient* — usually "IREE is a model-graph compiler, not a programming model; it doesn't help you write novel custom kernels/algorithms across exotic silicon the way a new language would." That is a defensible wedge, but it has to be argued explicitly, because on the literal "one workload, many chips" claim IREE is a live, credible incumbent. (This is exactly the **Callosum** question: is the bet a new programming model, or a runtime layer *above* compilers like IREE?)

## Sources

- [iree-org/iree — GitHub](https://github.com/iree-org/iree) — what it is, backend list (Vulkan/CUDA/ROCm/Metal/WebGPU), MLIR dependency, LF AI sandbox, AMD MLPerf note. *Tier 7.*
- [nod-ai/AMD-SHARK-Studio — GitHub](https://github.com/nod-ai/AMD-SHARK-Studio) — AMD's SHARK built on IREE (the AMD-adoption proof). *Tier 7.*
- [MLIR users list — mlir.llvm.org/users](https://mlir.llvm.org/users/) — IREE as a flagship MLIR adopter. *Tier 7.*

**Flags:** IREE's exact first open-source year (~2019-2020) not pinned to a primary source.
