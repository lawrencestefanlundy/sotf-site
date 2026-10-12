---
type: concept
slug: cheri
canonical_name: CHERI (Capability Hardware Enhanced RISC Instructions)
aliases:
- CHERIoT
- CHERI-RISC-V
- capability hardware
parent_concepts:
- compute-architecture
- compute
related_concepts:
- tee
sources: []
frontier:
- Does CHERI / CHERIoT reach a production design-win at scale, or stay a research + eval-board architecture?
- Does Arm revive a capability path (after shelving Morello) or stay on MTE?
last_updated: '2026-06-23'
tags:
- concept
- security
mention_count: 7
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors:
- slug: tee
  name: TEE
  path: /life-frontier/trust/tee/
  macro: life-frontier
---
A hardware architecture for **memory safety**, developed at the University of Cambridge and SRI International (with DARPA funding from ~2010). CHERI makes every pointer a hardware-enforced **capability**: a fat pointer carrying bounds and permissions, validated in silicon on every memory access, with an unforgeable tag bit. The result is deterministic, hardware-enforced **spatial and temporal memory safety** for C/C++ code, plus fine-grained software compartmentalisation, without rewriting the code.

## Why it matters

Roughly 70% of serious security vulnerabilities are memory-safety bugs (Microsoft / Google / US ONCD data). The policy world's primary fix is memory-safe *languages* (Rust); CHERI is the *hardware* path, valuable for the trillions of lines of legacy C/C++ firmware that will never be rewritten. It is a different primitive from confidential computing / TEEs (which protect data *in use* from a privileged host), and the two are sibling hardware-security mechanisms — see **Hardware Memory Safety** and **Confidential Computing**.

## How it differs from the alternatives

- **vs Rust / software:** protects existing C/C++ binaries (recompiled), not only newly written safe code.
- **vs ASLR:** deterministic, not probabilistic.
- **vs Arm MTE (Memory Tagging Extension):** finer-grained and stronger (full bounds + permissions per pointer) vs MTE's coarser, statistical tag-matching.

The adoption tax: it requires *new silicon* and a recompiled toolchain, which is the central reason its commercialisation is slow.

## Ecosystem