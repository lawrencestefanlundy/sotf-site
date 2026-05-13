---
type: concept
slug: zero-knowledge-proofs
canonical_name: Zero-Knowledge Proofs
aliases: []
kind: technology
parent_concepts:
- life-frontier
- trust
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---
## Physics / mechanism

Zero-knowledge proofs (ZKPs) let a prover convince a verifier that a statement is true without revealing any information beyond its truth. Formally: a protocol is ZK if it satisfies completeness, soundness, and zero-knowledge. Modern constructions—zk-SNARKs (Groth16, PLONK), zk-STARKs, and Bulletproofs—reduce proof size and verification cost via polynomial commitment schemes and elliptic-curve pairings or hash-based arithmetic. Current benchmarks: zk-SNARKs generate proofs in ~100ms–10s depending on circuit depth; STARKs are slower to prove (~10×) but avoid trusted setup and are post-quantum candidate-compatible. Proof sizes range from ~200 bytes (Groth16) to ~100 KB (STARKs). Prover compute remains the bottleneck—GPU/FPGA acceleration is actively reducing latency toward real-time thresholds.

## Competitive landscape

The primary axis is proof system choice: SNARKs (small proofs, pairing-dependent, trusted setup) vs. STARKs (larger proofs, hash-only, no setup) vs. Bulletproofs (no setup, logarithmic size, slower verification). Adjacent: secure multi-party computation (MPC) and fully homomorphic encryption (FHE) address overlapping confidentiality use cases but differ sharply on latency and composability.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
