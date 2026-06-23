---
type: concept
slug: mlc-llm
canonical_name: MLC-LLM (Machine Learning Compilation for LLMs)
aliases:
- MLC-LLM
- MLC LLM
- WebLLM
kind: compiler-application
parent_concepts:
- tvm
- ai-compiler-landscape
related_concepts:
- tvm
- mlir
sources: []
frontier:
- Does on-device LLM inference (browser/phone/edge) stay a real category, or does the cloud-API economics swamp it? MLC-LLM is the canonical proof it is technically possible.
last_updated: '2026-06-22'
tags:
- concept
- compiler
- edge
- on-device-llm
- reference
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: tvm
  name: Apache TVM
  path: /sotf-site/compute/compute-architecture/tvm/
  macro: compute
- slug: mlir
  name: MLIR (Multi-Level Intermediate Representation)
  path: /sotf-site/compute/compute-architecture/mlir/
  macro: compute
---
> The [Apache TVM](/sotf-site/compute/compute-architecture/tvm/)-lineage flagship for running LLMs **natively across consumer/edge devices** — the most visible proof that the TVM stack still does something [XLA / OpenXLA](/sotf-site/compute/compute-architecture/xla/)/PyTorch-native cannot: ship an LLM to a phone or a browser tab. Part of the [AI Compiler & Heterogeneous Programming-Model Landscape](/sotf-site/compute/compute-architecture/ai-compiler-landscape/).

## What it is

An open-source project (`mlc-ai/mlc-llm`) built directly on **TVM Unity** (Relax + TIR) that compiles LLMs to run **on-device**: browser (WebLLM via WebGPU), iOS, Android, and local CPU/GPU. It is the answer to the criticism that TVM's auto-tuning search was caught flat-footed by GenAI — MLC-LLM is where the TVM lineage stayed relevant in the LLM era. Actively developed through 2025.

## Why it matters here

It is the clearest demonstration that "compile one model, deploy to radically different and resource-constrained targets" is a real, shipped capability of the [Apache TVM](/sotf-site/compute/compute-architecture/tvm/) stack — the edge/on-device tier that [XLA / OpenXLA](/sotf-site/compute/compute-architecture/xla/) and most [MLIR (Multi-Level Intermediate Representation)](/sotf-site/compute/compute-architecture/mlir/)-based datacenter stacks ignore. For the **Callosum** competitive read, it is a reminder that the heterogeneous-deployment problem is already partially solved at the *graph-compiler + on-device runtime* layer, not green field.

## Sources

- [MLC-LLM project site](https://llm.mlc.ai/) — what it is, targets, current status. *Tier 7.*
- [mlc-ai/mlc-llm — GitHub](https://github.com/mlc-ai/mlc-llm) — repo, TVM Unity dependency. *Tier 7.*
