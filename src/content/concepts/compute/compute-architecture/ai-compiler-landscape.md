---
type: concept
slug: ai-compiler-landscape
canonical_name: AI Compiler & Heterogeneous Programming-Model Landscape
aliases:
- ML compiler landscape
- heterogeneous compute software stack
- the CUDA-alternative stack
- programming models for heterogeneous compute
kind: landscape
parent_concepts:
- compiler-as-bottleneck-for-novel-hardware
- cuda-moat
- compute-architecture
related_concepts:
- mlir
- xla
- tvm
- iree
- triton
sources: []
frontier:
- Does the winning layer for heterogeneous compute end up being the IR substrate (MLIR), the graph compiler (XLA), the kernel language (Triton/Mojo), or a runtime workload-placement layer above all of them (the Callosum shape)?
- Every independent attempt at 'the cross-hardware compiler company' so far either pivots (OctoML) or stays GPU-family-only (Modular). Does a standalone heterogeneous-compute software company ever reach durable independence, or is the exit always absorption by a silicon vendor?
- Where does the abstraction stop working? GPU-family portability (NVIDIA+AMD+Apple) is now demonstrably tractable; portability across categorically different execution models (wafer-scale dataflow, in-memory/analog, optical) is unsolved by anyone. Is that white space or a wall?
last_updated: '2026-06-22'
tags:
- concept
- landscape
- compiler
- compute
- reference
- callosum-competitive-set
descendants:
- iree
- mlc-llm
- mlir
- triton
- tvm
- xla
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
- slug: iree
  name: IREE (Intermediate Representation Execution Environment)
  path: /sotf-site/compute/compute-architecture/iree/
  macro: compute
- slug: triton
  name: Triton (OpenAI Triton)
  path: /sotf-site/compute/compute-architecture/triton/
  macro: compute
---
> The competitive map for "the software layer that lets one workload run across genuinely different silicon." Built 22 Jun 2026 to ground the **Callosum** diligence question: when a founder says CUDA-like single-source languages structurally fail for heterogeneous hardware (SYCL as the cautionary tale) and "we have a new programming model," **who are they actually competing with?** The answer is not CUDA. It is this stack. Companion to **Cuda Moat** (the incumbent moat) and [Compiler as Bottleneck for Novel Hardware](/sotf-site/compute/compute-architecture/compiler-as-bottleneck-for-novel-hardware/) (why novel silicon dies without a compiler).

## The one framing that matters

The naive read is "CUDA vs the challengers." The correct read has **four distinct layers**, and most analytical errors come from comparing things at different layers:

| Layer | What it is | The players | Heterogeneity it delivers |
|---|---|---|---|
| **IR / substrate** | Reusable compiler plumbing everything else is built on | [MLIR (Multi-Level Intermediate Representation)](/sotf-site/compute/compute-architecture/mlir/) | None by itself — it's the *toolkit* for building per-target paths |
| **Graph compiler** | Compile a whole model graph, fuse ops, emit device code | [XLA / OpenXLA](/sotf-site/compute/compute-architecture/xla/) (OpenXLA), [Apache TVM](/sotf-site/compute/compute-architecture/tvm/) | Closest to "one graph, many silicon" — **already in frontier production** |
| **Kernel language** | Write a kernel once at tile/block level, above raw CUDA | [Triton (OpenAI Triton)](/sotf-site/compute/compute-architecture/triton/), Mojo (**Modular**) | One kernel across GPU *family* (NVIDIA+AMD), not beyond SIMT |
| **End-to-end + runtime** | Compiler + runtime that deploys & executes the artefact | [IREE (Intermediate Representation Execution Environment)](/sotf-site/compute/compute-architecture/iree/), MAX (**Modular**), [MLC-LLM (Machine Learning Compilation for LLMs)](/sotf-site/compute/compute-architecture/mlc-llm/), **Zml** (🇫🇷 EU, Zig/MLIR) | Functional cross-backend portability; uneven performance |

****Callosum** is claiming a fifth layer above all of these**: a runtime that *decomposes a workload and places each sub-task on the chip whose execution model fits it*, rather than trying to make one kernel/graph run everywhere. If that is the real bet, its competitive set is less this stack and more orchestration/scheduling (NVIDIA Dynamo, the clouds). If the "new programming model" is actually a new IR or kernel language, it collides head-on with the mature, well-funded, vendor-backed players below. **That ambiguity is the diligence crux.**

## The players (one line each, detail on the linked pages)

- **[MLIR (Multi-Level Intermediate Representation)](/sotf-site/compute/compute-architecture/mlir/)** (Lattner, 2018-19, Google→LLVM) — the **substrate**. Dialects = composable IR levels designed for heterogeneity. Everyone serious builds on it: XLA, IREE, Triton, Mojo, plus vendor stacks (AMD AIE, Tenstorrent tt-mlir, SOPHGO). A new programming model would almost certainly *build on* MLIR, not compete with it. Framing MLIR as a rival is a founder red flag.
- **[XLA / OpenXLA](/sotf-site/compute/compute-architecture/xla/) / OpenXLA** (Google, ~2017; OpenXLA 2023) — the **graph compiler** and the real incumbent for "one graph, many silicon." Compiles JAX/TF/PyTorch to TPU, NVIDIA, AMD, Apple, Trainium. **XLA:TPU is what lets Google and Anthropic train frontier models without NVIDIA** (Anthropic's ~1M-TPU / multi-GW bet runs through it). The asterisks: performance portability is uneven (TPU excellent, GPU good, rest patchy) and the best backend (TPU) is closed and Google-owned. **Largely already "the CUDA of heterogeneous compute" at the graph layer** — its only hard limit is exotic non-matmul silicon.
- **[Apache TVM](/sotf-site/compute/compute-architecture/tvm/)** (Tianqi Chen, UW, 2017; Apache) — the **breadth/edge compiler**. Distinctive for **search-based auto-tuning** (AutoTVM/Ansor — "ML to optimise ML compilation") and uniquely deep **edge/MCU** reach (microTVM) plus **BYOC** ("Bring Your Own Codegen"), the standard on-ramp for novel silicon (Tenstorrent `tt-tvm`, Qualcomm Hexagon). Still maintained (v0.25, Jun 2025) but mindshare for *new* compilers has moved to MLIR-based stacks. [MLC-LLM (Machine Learning Compilation for LLMs)](/sotf-site/compute/compute-architecture/mlc-llm/) is its on-device-LLM flagship.
- **[IREE (Intermediate Representation Execution Environment)](/sotf-site/compute/compute-architecture/iree/)** (Google, ~2019; LF AI & Data) — the **MLIR-native end-to-end compiler+runtime**, the most direct realisation of "compile one model → run on CPU/GPU via Vulkan/CUDA/ROCm/Metal/WebGPU." Now effectively **AMD-backed** (via the Nod.ai/SHARK acquisition; AMD ran an IREE-based SDXL MLPerf submission Apr 2025). The closest open, vendor-backed competitor on the literal portability claim.
- **[Triton (OpenAI Triton)](/sotf-site/compute/compute-architecture/triton/)** (Philippe Tillet, 2019; OpenAI) — the **kernel language**. Tile-over-SIMT, the default kernel backend in PyTorch 2.x (`torch.compile`→TorchInductor emits Triton). Runs on NVIDIA + AMD + experimental Intel/CPU. **NVIDIA shipped a CUDA Tile-IR backend for Triton (30 Jan 2026)** — the incumbent endorsing the higher-level model and pulling it into its orbit. Partially *refutes* the "single-source fails across hardware" claim, but only *within* the GPU/SIMT family.
- **Mojo / MAX (**Modular**)** — the **best-funded direct attempt** at a new programming model for AI hardware. Chris Lattner (created LLVM + MLIR) + Tim Davis. **$380M total raised, last round $250M at $1.6B (Sept 2025)**. Mojo (MLIR-based Python-superset) + MAX (inference platform) now run unmodified kernels across **NVIDIA + AMD + Apple GPUs** — delivered, not vapour. But: nothing beyond the GPU family, compiler still closed (open-source promised end-2026), 1.0 not yet shipped, no independent revenue, CUDA's moat intact.

## What the precedents teach (the investor lesson)

Two hard datapoints bound any "new programming model for heterogeneous compute" bet:

1. **OctoML is the cautionary tale on the business.** The TVM creators' venture-backed "cross-hardware compiler company" (~$132M raised) could not sell compiler tooling as a standalone market, **pivoted to inference-serving (OctoAI), and was absorbed by NVIDIA (~Sept 2024)** — which promptly **sunset the cross-hardware product**. The category's strongest independent attempt ended up *inside the dominant silicon vendor*, and the portability product died there. See **Octoml**. **Exit gravity in this category points toward acqui-hire by a chip champion, not standalone IPO.**

2. **Modular is the cautionary tale on difficulty + timeline.** Four years, ~$380M, the literal inventor of MLIR/LLVM, and the deliverable is **GPU-family portability with a still-closed compiler and no shipped 1.0.** If that is what world-class pedigree and a third of a billion dollars buys, a sub-$10M seed company claiming a "fundamentally new programming model" spanning *exotic* silicon is a 7-10 year, capital-hungry infrastructure bet where **adoption (unseating CUDA mindshare) is harder than the technology.**

**The corollary for the white space:** GPU-family portability (NVIDIA↔AMD↔Apple) is now demonstrably tractable — Triton, Mojo and IREE all do it. So the strongest form of the "single-source structurally fails" claim is **partly false at the GPU layer**. The genuinely open frontier — where CUDA, SYCL, *and* Mojo all stop — is portability across **categorically different execution models**: wafer-scale dataflow (Cerebras), in-memory/analog, optical. A smaller player's only defensible wedge is **narrow architectural depth** (own one genuinely-different silicon class end-to-end) or a layer *above* the compiler (runtime workload decomposition + placement), not head-on competition for the GPU-portability layer the incumbents already occupy.

## How this maps onto Callosum

**Callosum**'s "new programming model upcoming" is the [crux artifact](../../../answers/2026-06-22-compute-as-racks-routing-callosum.md) on its angel position. This landscape sharpens the questions:

- **Not "why is CUDA wrong" (settled) but "why you over MLIR/XLA/Mojo/IREE"** — the camp that agreed CUDA was wrong years ago and has deep ecosystems + vendor backing.
- **XLA is the hardest comparison**, not CUDA: it already compiles one graph to TPU+GPU+AMD+Trainium at frontier scale. Callosum has to beat it where it's weak (vendor-neutrality; exotic non-matmul silicon), not where it's strong.
- **"Programming model" (CUDA/Mojo-scale moat, brutal and slow) vs "workload decomposition + placement" (a runtime/scheduler, more achievable but more contestable, edges toward the NVIDIA-Dynamo-replicable risk).** These are different bets with different moats; the ~$400m-post seed needs the former. Callosum's own framing blends them — resolving which is the single highest-value thing the next call can extract.

## Connections

- Incumbent moat being attacked: **Cuda Moat**
- Why novel silicon needs this layer at all: [Compiler as Bottleneck for Novel Hardware](/sotf-site/compute/compute-architecture/compiler-as-bottleneck-for-novel-hardware/)
- The live deal this map serves: **Callosum** · its competitive thread: **2026 06 22 Compute As Racks Routing Callosum**
- The distinct/more-fundamental adjacent bet: **Ai Kernel Synthesis** (auto-generating the fast kernels — the layer that makes any of the above actually fast; complement to Callosum)
- Theses it touches: **Compute Specialisation Equilibrium** (the porting/software tax is the historical brake) · **Agents Need New Silicon** · **Ai Compute Toll Booths**
- Detail pages: [MLIR (Multi-Level Intermediate Representation)](/sotf-site/compute/compute-architecture/mlir/) · [XLA / OpenXLA](/sotf-site/compute/compute-architecture/xla/) · [Apache TVM](/sotf-site/compute/compute-architecture/tvm/) · [IREE (Intermediate Representation Execution Environment)](/sotf-site/compute/compute-architecture/iree/) · [Triton (OpenAI Triton)](/sotf-site/compute/compute-architecture/triton/) · **Modular** · **Octoml**

## Confidence flags

Mojo cross-GPU benchmarks and MAX "beats vLLM" numbers are first-party (Modular), not independently reproduced at scale. OctoML acquisition price (~$165M base / >$250M with earnouts) is trade-press only; NVIDIA did not disclose terms. XLA's exact original year (~2017) and OpenXLA's current formal governance are not pinned to a primary source.
