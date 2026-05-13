---
type: concept
slug: multi-party-computation
canonical_name: Multi-Party Computation (MPC)
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
- anoma-namada-heliax
- applied-mpc-blockstream-subsidiary
- arcium-formerly-elusiv
- beacon-formerly-known-as-zengos-mpc-team-spin-context
- breeze-formerly-known-as-beacon
- cape-privacy-acquired-by-oblivious-ai
- cape-privacy-acquired-by-wandisco
- cosmian
- crypho-secrify
- curv-acquired-by-paypal
- cybernetica
- duality-technologies
- entropy-now-part-of-axelar-ecosystem
- entropy-now-part-of-ecosystem
- escrypto-tnos-spinout-via-roseman-labs
- fireblocks
- holonym-holonym-foundation
- inpher
- keyless
- ligero-acquired-by-alchemy
- liminal-formerly-wazirx-custody
- nillion
- partisia-blockchain
- portal-formerly-portals
- privy
- pyte
- sepior-acquired-by-blockdaemon
- sharemind-cybernetica-subsidiary
- sharemind-cybernetica
- sievert-cybrid-sepior-lineage-startups
- sievert-keyless
- silence-laboratories
- taurus-group
- tno-applied-cryptography-group
- unbound-security-acquired-by-coinbase
- zama
- zengo
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

# Multi-Party Computation (MPC)

*Kind: technology*

## Physics / mechanism

Multi-party computation is a cryptographic protocol family allowing *n* parties to jointly compute a function over private inputs without any party revealing its data to others. Core mechanism: secret sharing (Shamir, additive) splits each input into shares distributed across parties; computation proceeds on shares via arithmetic or Boolean circuits, with results reconstructed only at output. Variants include garbled circuits (Yao, two-party, constant rounds), GMW protocol (multi-party, linear rounds), and SPDZ (preprocessing model, malicious security). Performance benchmarks: AES evaluation ~0.1–1ms in semi-honest LAN settings; malicious-secure protocols add 5–10× overhead. Homomorphic encryption (FHE) handles single-party computation on encrypted data and is often conflated but distinct. MPC maturity is high for specific applications (threshold signatures, private set intersection); general-purpose MPC remains latency-constrained.

## Competitive landscape

| Approach | Security model | Latency | Compute overhead |
|---|---|---|---|
| MPC (SPDZ/GMW) | Multi-party, malicious | Medium–High | 10–100× vs plaintext |
| FHE (CKKS/BFV) | Single-party compute | High | 1000–10000× |
| TEE (SGX/TrustZone) | Hardware attestation | Low | ~1–2× |

## Cloudberry relevance

TEEs are the dominant competitor for confidential compute: lower latency, simpler deployment, but hardware trust assumptions and side-channel exposure. Differential privacy handles aggregate statistics without interactive protocols. Federated learning addresses distributed model training but leaks gradient information MPC can seal. PSI (private set intersection) is MPC's most commercially deployed subset.


Cloudberry's semiconductor angle: MPC acceleration is an open hardware problem. Custom ASIC or FPGA implementations targeting finite-field arithmetic (NTT, modular multiply) could reduce MPC latency 100×+—a credible deep-tech wedge. GlobalFoundries process nodes (12LP, 22FDX) are viable targets for low-power secure-compute silicon. Lunar Ventures' enterprise SaaS portfolio creates pull-through demand for confidential data collaboration infrastructure. Deal-flow: fabless MPC accelerator startups, threshold-cryptography infrastructure for AI data consortia, privacy-preserving analytics in regulated verticals.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
