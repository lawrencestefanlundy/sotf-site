---
type: concept
slug: multi-party-computation
canonical_name: Multi-Party Computation (MPC)
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

Multi-party computation is a cryptographic protocol family allowing *n* parties to jointly compute a function over private inputs without any party revealing its data to others. Core mechanism: secret sharing (Shamir, additive) splits each input into shares distributed across parties; computation proceeds on shares via arithmetic or Boolean circuits, with results reconstructed only at output. Variants include garbled circuits (Yao, two-party, constant rounds), GMW protocol (multi-party, linear rounds), and SPDZ (preprocessing model, malicious security). Performance benchmarks: AES evaluation ~0.1–1ms in semi-honest LAN settings; malicious-secure protocols add 5–10× overhead. Homomorphic encryption (FHE) handles single-party computation on encrypted data and is often conflated but distinct. MPC maturity is high for specific applications (threshold signatures, private set intersection); general-purpose MPC remains latency-constrained.

## Competitive landscape

| Approach | Security model | Latency | Compute overhead |
|---|---|---|---|
| MPC (SPDZ/GMW) | Multi-party, malicious | Medium–High | 10–100× vs plaintext |
| FHE (CKKS/BFV) | Single-party compute | High | 1000–10000× |
| TEE (SGX/TrustZone) | Hardware attestation | Low | ~1–2× |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
