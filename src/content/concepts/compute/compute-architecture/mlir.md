---
type: concept
slug: mlir
canonical_name: MLIR (Multi-Level Intermediate Representation)
aliases:
- MLIR
- Multi-Level IR
- LLVM MLIR
kind: compiler-infrastructure
parent_concepts:
- ai-compiler-landscape
- compiler-as-bottleneck-for-novel-hardware
related_concepts:
- xla
- iree
- triton
- cuda-moat
sources: []
frontier:
- Does MLIR stay the neutral substrate, or does dialect fragmentation (each vendor's incompatible dialects) recreate the very fragmentation it was built to end?
- Does any heterogeneous-compute company build a durable moat ABOVE MLIR, or does MLIR commoditise the compiler layer such that the value moves entirely to silicon + libraries?
last_updated: '2026-06-22'
tags:
- concept
- compiler
- compute
- substrate
- reference
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: xla
  name: XLA / OpenXLA
  path: /sotf-site/compute/compute-architecture/xla/
  macro: compute
- slug: iree
  name: IREE (Intermediate Representation Execution Environment)
  path: /sotf-site/compute/compute-architecture/iree/
  macro: compute
- slug: triton
  name: Triton (OpenAI Triton)
  path: /sotf-site/compute/compute-architecture/triton/
  macro: compute
---
> The **substrate** layer of the [AI Compiler & Heterogeneous Programming-Model Landscape](/sotf-site/compute/compute-architecture/ai-compiler-landscape/). Not a programming language, not a portability solution — the reusable compiler-construction toolkit that almost every modern ML compiler is now built on. The single most important fact for diligence: **a credible "new programming model for heterogeneous compute" builds ON MLIR; it does not compete WITH it.** A founder who frames MLIR as a rival has misread the stack.

## Origin

Started **2018** by **Chris Lattner** (creator of LLVM, Clang, Swift) at **Google**, with Mehdi Amini, River Riddle and others, out of the TensorFlow infrastructure team. Introduced at the 2019 LLVM Developer Meeting, open-sourced into the LLVM monorepo that year, now a permanent LLVM subproject. Canonical paper: *"MLIR: A Compiler Infrastructure for the End of Moore's Law"* ([arXiv 2002.11054](https://arxiv.org/abs/2002.11054), tier 1). (Lattner went on to co-found **Modular** — the same person is behind the substrate AND the best-funded company building on it.)

Motivation: ML frameworks were each spawning incompatible one-off compiler IRs (TF's XLA HLO, etc.) with no shared, reusable substrate from high-level tensor ops down to hardware instructions.

## What it is (plain English)

A **compiler-construction toolkit**, not a single fixed IR. Its defining idea is **dialects**: each dialect is a self-contained namespace of operations/types/attributes at a chosen abstraction level (a `tensor` dialect, a `gpu` dialect, a vendor's accelerator dialect). You mix dialects in one program and write "lowering" passes that progressively rewrite high-level dialects into lower-level ones until you reach something a backend can emit. **You add a new hardware target by adding a dialect and lowering passes, without forking the framework** — that is the whole point, and it is explicitly a heterogeneity mechanism.

## Heterogeneous-hardware angle (the key part)

MLIR is **plumbing, not portability.** It was *designed for* heterogeneous compilation but does **not** by itself give cross-silicon performance-portability. It standardises *how* you build the path from program to a given chip; **each backend (NVIDIA, AMD, TPU, wafer-scale, analog, optical) still implements its own dialects and lowerings**, and getting good performance on each remains the hard, hand-done engineering. MLIR removes the duplicated scaffolding; it does not remove the per-target work. Anyone claiming "MLIR solves heterogeneity" is overclaiming — it solves the *infrastructure-fragmentation* half, not the *automatic good code on every chip* half.

## Governance + adoption (2025-26)

Governed by the LLVM project (open community, LLVM release cadence). Adoption is the headline: the de-facto substrate under **[XLA / OpenXLA](/sotf-site/compute/compute-architecture/xla/)/OpenXLA, [IREE (Intermediate Representation Execution Environment)](/sotf-site/compute/compute-architecture/iree/), [Triton (OpenAI Triton)](/sotf-site/compute/compute-architecture/triton/) (Triton-IR/Triton-GPU are MLIR dialects), Mojo/**Modular**, Torch-MLIR, ONNX-MLIR**, plus vendor stacks — **AMD/Xilinx (MLIR-AIE), **Tenstorrent** (tt-mlir), SOPHGO (TPU-MLIR)**. 2025 work: governance to curb dialect fragmentation (curated core dialects), the Transform dialect (CGO 2025) for tunable optimisation, expansion beyond ML (proposed WebAssembly dialect, Clang CIR). Entrenched and still growing.

## Competitive read (vs a "new programming model" startup)

**Substrate, not competitor.** A credible new heterogeneous programming model lowers to MLIR dialects; doing otherwise means re-inventing a decade of LLVM/MLIR infrastructure and losing interop with every vendor backend already expressed in MLIR. The startup's real moat must live *above* MLIR — the programming abstraction and the cross-target optimisation/auto-tuning intelligence — with MLIR as its IR layer. This is also the live risk to such a company: if MLIR commoditises the compiler layer, value can drain to silicon + libraries (the **Cuda Moat** lesson that the moat is libraries, not syntax).

## Sources

- [MLIR: A Compiler Infrastructure for the End of Moore's Law — Lattner et al., arXiv 2002.11054](https://arxiv.org/abs/2002.11054) — canonical paper; dialect design for heterogeneity. *Tier 1.*
- [Users of MLIR — mlir.llvm.org/users](https://mlir.llvm.org/users/) — official adopter list (XLA, IREE, Triton, Mojo, AMD AIE, TPU-MLIR, tt-mlir). *Tier 7.*
- [MLIR (software) — Wikipedia](https://en.wikipedia.org/wiki/MLIR_(software)) — origin, governance, dialect mechanism. *Tier 6.*

**Flags:** "April 2018" start month appears in secondary sources only (year solid). The claim that Cerebras/SambaNova/Groq/Apple/Qualcomm use named MLIR projects is plausible but unverified beyond AMD/Xilinx, SOPHGO, Tenstorrent on the official list.
