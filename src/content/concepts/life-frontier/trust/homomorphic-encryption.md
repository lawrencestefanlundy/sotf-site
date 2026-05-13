---
type: concept
slug: homomorphic-encryption
canonical_name: Homomorphic Encryption
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
- arcium-formerly-elusiv
- chain-reaction
- cingulata-bullatos-spinout
- cloudflare-research
- cornami
- cosmian
- cryptoexperts
- cryptolab
- desilo
- duality-technologies
- encrypt-ai-formerly-he-arc-spinout
- enveil
- fujitsu-research
- galois
- google-fhe-team-transpiler
- heaan-cryptolab
- heliax
- huawei-pangu-privacy-computing-lab
- ibm-research-helib-fhe-toolkit
- ibm-research
- ingenii-fka-fheorg-spin-out-track
- inpher
- intel-hexl-library
- intel-hexl-team
- ixup
- microsoft-research-seal-ckks
- microsoft-seal-microsoft-research
- niobium-microsystems
- openfhe-duality-spin-community-openfhe-org
- optalysys
- prism-privasea
- sandboxaq
- secretflow-ant-group-alibaba
- sharemind-cybernetica
- shieldio
- sievert-larsen-associates-propeller-industries-na-correct-en
- sunscreen-tech
- zama
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

# Homomorphic Encryption

*Kind: technology*

## Physics / mechanism

Homomorphic encryption (HE) allows computation on ciphertext such that decrypting the result equals applying the same function to plaintext. Fully homomorphic encryption (FHE) supports arbitrary operations via lattice-based constructions (CKKS, BFV, TFHE schemes). The core mechanism relies on learning-with-errors (LWE) hardness; noise accumulates with each operation and must be managed via bootstrapping. Current SOTA: TFHE bootstrapping ~1–10 ms per gate on CPU; GPU-accelerated libraries (OpenFHE, HEIR) cut this 10–100×. Practical deployments remain 3–6 orders of magnitude slower than plaintext compute. Key parameters: polynomial modulus degree (n = 2¹⁴–2¹⁶), noise budget, and multiplicative depth.

## Competitive landscape

The primary competitive tension is between FHE, secure multi-party computation (MPC), and trusted execution environments (TEEs like Intel TDX, AMD SEV). Each occupies a different point on the trust-vs-performance curve.

## Cloudberry relevance

| Approach | Threat model | Relative perf overhead | HW dependency |
|---|---|---|---|
| FHE | Full software isolation | 10⁴–10⁶× | None (but HW accelerators emerging) |
| MPC | Distributed semi-honest | 10²–10³× | Low |
| TEE | HW-rooted trust | ~1–5× | High (Intel/AMD) |

Adjacent: differential privacy (statistical, not cryptographic), federated learning (gradient exposure risk). FHE and MPC are increasingly composed.


HE acceleration is a semiconductor play. Dedicated silicon (Cornami, Intel HERACLES, SiPearl interest) targets the bootstrapping bottleneck with custom NTT engines and high-bandwidth memory. GlobalFoundries' process nodes (12LP+, 22FDX) are candidate fabs for power-constrained FHE ASICs. Deal-flow: fabless startups needing advanced-node tapeouts for cryptographic accelerators; EDA tooling for HE-specific dataflow architectures. Lunar Ventures' enterprise software lens intersects where FHE middleware sits above the silicon stack.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
