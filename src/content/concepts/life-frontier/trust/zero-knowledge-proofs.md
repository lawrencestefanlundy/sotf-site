---
type: concept
slug: zero-knowledge-proofs
canonical_name: Zero-Knowledge Proofs
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- trust
related_concepts: []
companies_using:
- aleo
- aligned-layer
- aztec-network
- boundless-fka-risczeros-proving-network
- cysic
- fermah
- gevulot
- ingonyama
- irreducible-formerly-binius
- irreducible-formerly-ulvetanna-spinout
- lurk-lab
- matter-labs
- mina-protocol-o1-labs
- mina-protocol-o1labs
- modulus-labs
- nexus
- nil-foundation
- polygon-zk-division
- polyhedra-network
- proven-formerly-zkonduit
- proven
- rarimo
- reclaim-protocol
- risc-zero
- scroll
- starkware-industries
- succinct-labs
- taceo
- toposware
- ulvetanna
- zama
- zkpass
- zksync-matter-labs
ideas_referencing: []
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

# Zero-Knowledge Proofs

*Kind: technology*

## Physics / mechanism

Zero-knowledge proofs (ZKPs) let a prover convince a verifier that a statement is true without revealing any information beyond its truth. Formally: a protocol is ZK if it satisfies completeness, soundness, and zero-knowledge. Modern constructions—zk-SNARKs (Groth16, PLONK), zk-STARKs, and Bulletproofs—reduce proof size and verification cost via polynomial commitment schemes and elliptic-curve pairings or hash-based arithmetic. Current benchmarks: zk-SNARKs generate proofs in ~100ms–10s depending on circuit depth; STARKs are slower to prove (~10×) but avoid trusted setup and are post-quantum candidate-compatible. Proof sizes range from ~200 bytes (Groth16) to ~100 KB (STARKs). Prover compute remains the bottleneck—GPU/FPGA acceleration is actively reducing latency toward real-time thresholds.

## Competitive landscape

The primary axis is proof system choice: SNARKs (small proofs, pairing-dependent, trusted setup) vs. STARKs (larger proofs, hash-only, no setup) vs. Bulletproofs (no setup, logarithmic size, slower verification). Adjacent: secure multi-party computation (MPC) and fully homomorphic encryption (FHE) address overlapping confidentiality use cases but differ sharply on latency and composability.

## Cloudberry relevance

| Approach | Proof size | Trusted setup | PQ-safe |
|---|---|---|---|
| zk-SNARK (Groth16) | ~200 B | Yes | No |
| zk-STARK | ~100 KB | No | Yes |
| FHE | N/A (ciphertext) | No | Yes |


ZKP prover acceleration is a direct semiconductor opportunity: custom ASICs and FPGA IP cores targeting the MSM (multi-scalar multiplication) and NTT (number-theoretic transform) bottlenecks. This maps cleanly to Cloudberry's compute-silicon thesis and GlobalFoundries' specialty-process positioning. Deal-flow angles: fabless ZKP accelerator startups (cf. Ingonyama, Cysic), EDA tooling for ZK circuits, and photonic interconnect for multi-chip prover disaggregation at data-center scale.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
