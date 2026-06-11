---
type: concept
slug: homomorphic-encryption
canonical_name: Homomorphic Encryption
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
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Homomorphic encryption (HE) allows computation on ciphertext such that decrypting the result equals applying the same function to plaintext. Fully homomorphic encryption (FHE) supports arbitrary operations via lattice-based constructions (CKKS, BFV, TFHE schemes). The core mechanism relies on learning-with-errors (LWE) hardness; noise accumulates with each operation and must be managed via bootstrapping. Current SOTA: TFHE bootstrapping ~1–10 ms per gate on CPU; GPU-accelerated libraries (OpenFHE, HEIR) cut this 10–100×. Practical deployments remain 3–6 orders of magnitude slower than plaintext compute. Key parameters: polynomial modulus degree (n = 2¹⁴–2¹⁶), noise budget, and multiplicative depth.

## Competitive landscape

The primary competitive tension is between FHE, secure multi-party computation (MPC), and trusted execution environments (TEEs like Intel TDX, AMD SEV). Each occupies a different point on the trust-vs-performance curve.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*

## Merged from root duplicate (homomorphic-encryption.md at concepts/ root, 2026-06-10)

# Homomorphic Encryption (FHE)

Encryption that allows computation directly on ciphertext, so data stays encrypted in use. The blocker is compute cost (orders of magnitude over plaintext), which drives the **Fhe Acceleration Silicon** thesis: purpose-built accelerators for the polynomial/NTT bottleneck. A pillar of confidential computing alongside TEEs.
