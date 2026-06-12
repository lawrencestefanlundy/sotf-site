---
type: concept
slug: compiler-as-bottleneck-for-novel-hardware
canonical_name: Compiler as Bottleneck for Novel Hardware
aliases:
- compiler-first hardware
- MLIR gap
- novel-hardware compiler problem
kind: pattern
parent_concepts:
- compute-architecture
- hardware-software-co-design
related_concepts:
- physics-native-compute
- coherent-ising-machine
- memristors
- ai-accelerator
sources: []
frontier:
- Which compiler stack (MLIR, TVM, IREE, MLC) becomes canonical for physics-native compute?
- At what stage in a novel-hardware company does the compiler hire need to be made — pre-seed (Vega) or only after first silicon?
- Does AI-assisted compiler generation (Codex / DeepMind PCA / AlphaEvolve-class) shorten the compiler-build timeline?
last_updated: '2026-05-27'
tags:
- concept
- pattern
- compiler
- novel-hardware
- cautionary-tale
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: physics-native-compute
  name: Physics-Native Compute
  path: /sotf-site/compute/non-conventional/physics-native-compute/
  macro: compute
- slug: coherent-ising-machine
  name: Coherent Ising Machine
  path: /sotf-site/compute/non-conventional/coherent-ising-machine/
  macro: compute
- slug: memristors
  name: Memristors
  path: /sotf-site/compute/non-conventional/memristors/
  macro: compute
- slug: ai-accelerator
  name: AI Accelerator
  path: /sotf-site/compute/conventional-logic/ai-accelerator/
  macro: compute
---
A pattern. **Novel hardware companies die between tape-out and customer deployment because the compiler that maps generic ML graphs to the hardware's native primitives isn't built.** The hardware ships; customers can't use it. The company stalls or pivots.

This is the most reliably recurring failure mode in novel-compute deal flow. Every pre-seed evaluating a hardware play needs the compiler-hire question answered.

## The pattern

1. **Architecture validated.** Simulations show 10x / 100x / 1000x speedup or energy advantage on a target workload.
2. **First silicon arrives.** Hardware works on hand-tuned benchmarks.
3. **Customer pilot starts.** Customer brings their actual model (a transformer with custom layers, an Ising problem with non-standard topology, a specific optimisation graph).
4. **Mapping is manual.** Hand-translation takes weeks per workload. Customer can't iterate. Pilot stalls.
5. **Compiler team starts.** 12–24 months to build something resembling a generic front-end. Cash burns. Customer attention moves to alternatives.

## Notable casualties

| Company | Hardware | What killed it |
|---|---|---|
| **Mythic** | Analog flash matrix-mul | Hand-tuned model mapping; per-customer porting impossible to scale; pivoted, downsized |
| **Lightelligence** | Photonic Ising / matmul | Compiler for arbitrary transformer architectures absent; pivoted to optical interconnect |
| HP Labs memristor | Resistive RAM crossbars | No customer-facing compiler ever shipped; team disbanded after a decade |

## Notable survivors (and how)

| Company | Compiler strategy | Outcome |
|---|---|---|
| **Groq** | Compiler-first development (TSP compiler started years before silicon); LPU shipped with first-customer-ready software | Production AI inference accelerator at chip scale |
| **Cerebras** | CSL (Cerebras Software Language) built in parallel with WSE silicon; PyTorch / TF front-end at GA | Shipping WSE-3 with paying customers |
| Nvidia (historical) | CUDA started ~2006, three years before AI take-off; ecosystem moat | The moat |

## Why physics-native compute is especially exposed

Every [Physics-Native Compute](/sotf-site/compute/non-conventional/physics-native-compute/) substrate (CIM, thermodynamic, p-bit, neuromorphic) requires a compiler that maps a *graph* (transformer, Ising, MAP inference) to a *physical configuration* (J matrix, varactor states, coupling weights). The mapping is mathematically non-trivial because:

- The physical substrate's energy landscape is set by geometry + per-tile tuning, not by software variables
- The realised dynamics differ from idealised by the [FDTD-to-Hardware Calibration Wall](/sotf-site/compute/non-conventional/fdtd-calibration-wall/) gap — compiler has to anticipate or correct for this
- The graph-to-substrate mapping for an arbitrary model is an inverse design problem, not a simple translation

## DD signals

**Strong proceed signals.**
- Compiler engineer named, identified, in pipeline at pre-seed
- Founder maps the compiler problem to MLIR / TVM / IREE specifically (not "we'll build it")
- Customer pilot plan includes manual model mapping for first 1–2 customers; compiler v1 by month 9–12

**Pass / strong concern signals.**
- "Compiler is post-Series A"
- "We'll partner with [Synopsys / Cadence / academic group]" without named partner
- Founder describes hardware in detail but cannot describe how customer input becomes hardware configuration
- Reference customers don't exist because nobody can use the hardware without the founder hand-holding

## Pre-seed-stage compiler hire pattern

For pre-seed deals in this category, the compiler-hire pipeline should be visible at term-sheet:
- Named candidates from MLIR contributor list (LLVM / TensorFlow MLIR)
- Or ex-Synopsys / Cadence compiler engineers
- Or ex-Groq / Cerebras / Tenstorrent compiler team
- Or ML-systems engineers from TVM / IREE / MLC-LLM ecosystem

## Sources

<!-- dataview block stripped for public site -->
