---
type: concept
slug: interaction-nets
canonical_name: Interaction Nets
aliases:
- interaction net
- interaction combinators
- interaction-net
parent_concepts:
- compute-paradigms
related_concepts: []
sources:
- '[[2026-06-03-tendrils-compute]]'
frontier:
- Has any interaction-net machine (FPGA / ASIC) beaten a conventional CPU on a real workload, with the advantage GROWING as concurrency rises rather than being swamped by constant factors?
- Can the per-rewrite bookkeeping and memory-traffic overhead be designed away in hardware, when 35 years of software attempts could not?
- Does any production workload express naturally enough as interaction nets that the rewrite model is a net win over von Neumann + scheduler?
last_updated: 2026-06-18
tags:
- concept
mention_count: 15
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-06-03-tendrils-compute
  title: Tendrils Compute — company site (about / background / jobs)
  date: '2026-06-03'
  kind: web
neighbors: []
---
A model of computation introduced by **Yves Lafont (1990)** in which a program is a **graph** that runs by repeatedly applying **local rewrite rules**. Nodes ("agents") are wired together at ports; wherever two agents meet at their principal ports (an "active pair"), a rule rewrites that small local pattern into another. Computation is the repeated firing of active pairs until none remain. There is **no global control flow and no shared program counter** — all the structure lives in the graph.

Two properties are the entire reason the model is interesting, and the git branch/merge intuition fits here: you can reduce different parts of the graph in parallel (branch) and recombine without conflict (merge).

1. **Inherent parallelism.** Every rewrite is purely local — it touches only the two agents in the active pair. So independent active pairs across the graph can fire **simultaneously**, with no central scheduler and no locks. Parallelism is a property of the model, not something the programmer hand-manages with threads.
2. **Strong confluence (no conflicts).** The order in which active pairs fire does not change the final result, and in interaction nets even the *number* of rewrite steps is invariant (the one-step "diamond" property). Parallel rewrites therefore never clash — this is the formal version of "things don't constantly collide."

**Interaction combinators** (Lafont, 1997) are a fixed, universal set of three agents and their rules that is Turing-complete; they are the canonical compilation target, the "interaction-net assembly" that higher-level languages reduce to.

## Why it is pitched for new silicon

The software lineage is real and active, all of it running on existing CPUs/GPUs today: **HVM** (the Higher-order Virtual Machine) and **Bend** from the Higher Order Company (Victor Taelin), the **HVM2** paper, and the independent **Vine → Ivy → IVM** toolchain by the pseudonymous "T6". Vine is a public, working compiler. So the *runtime* is demonstrated; the *hardware* is not.

## The load-bearing caveat (why this is a non-area prior, not a cheerleading page)

This is why, under **Agents Need New Silicon**, a clean-sheet interaction-net CPU sits in the **recorded non-area** (the agent control plane is software-bound by the measured evidence and tends to be CPU-incumbent-captured) and is a founder-led *exception* candidate rather than a thesis bet. Confluence and parallelism are **necessary but not sufficient**; the constant factors are the historical killer.

## Diligence reduction

For any interaction-net hardware claim the question collapses to the benchmark gate (): **does expressing the real workload as interaction-net graph rewriting beat a conventional CPU + scheduler, with the advantage GROWING as concurrency rises** (FPGA or cycle-accurate sim is sufficient)? A concurrency-growing win re-opens the thesis; a flat or shrinking curve is the failure mode the constant factors predict.

## Not to be confused with

## See also