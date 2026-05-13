---
type: concept
slug: tee
canonical_name: TEE
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
- amazon-web-services
- amd
- anjuna-security
- arm
- confidential-cloud-cape-privacy
- confidential-cloud-r3-corda
- cosmian
- cysec
- decentriq
- edgeless-systems
- fortanix
- google
- hailo-tee-integration
- hailo
- huawei-itrustee-trustzone
- huawei-kunpeng-hisilicon
- intel
- keystone-enclave
- kindite-acquired-by-coinbase
- microsoft
- mithril-security
- nuvoton-technology
- opacity
- opaque-systems
- penglai-ant-group-ipads
- profian
- r3-conclave
- samsung-knox-trustzone
- samsung-samsung-research
- scalys
- sievert-larson-cybersecurity-telos
- sievert-larson-sievert
- telecom-italia-tim-telsy
- veracruz
- zama
ideas_referencing: []
sources:
- '[[2023-10-19-e20-the-state-of-privacy-enhancing]]'
- '[[2023-06-30-e06-the-model-t-moment-for-bits-llms]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2023-10-13-e19-trusted-execution-environments]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 6
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
---

# TEE

*Kind: technology · Attio deal count: 1*

## Physics / mechanism

A Trusted Execution Environment is a hardware-isolated compute enclave running alongside the main OS, enforcing confidentiality and integrity of code and data even against a privileged attacker. Implemented via dedicated silicon — ARM TrustZone partitions the CPU into Normal/Secure worlds; Intel TDX and AMD SEV-SNP extend isolation to full VMs using memory encryption. Key parameters: memory encryption latency overhead (~5–15%), attestation round-trip (<100 ms for remote attestation via ECDSA/DCAP), and TCB surface area (smaller = better; measured in lines of verified firmware). Current SoA: CCA (Confidential Compute Architecture) on ARMv9 introduces Realm Management Extensions, enabling dynamic realm creation without OEM key dependency.

## Competitive landscape


Competing approaches: homomorphic encryption (HE) handles computation on encrypted data without hardware trust anchors but carries 1,000–10,000× compute overhead — impractical for inference workloads today. Secure multi-party computation (SMPC) distributes trust across parties but requires coordination overhead. RISC-V enclaves (Keystone, Penglai) offer open-source TCB alternatives. The confidential computing stack is increasingly converging around CCA/TDX/SEV-SNP as the hyperscaler-validated trio.

| Approach | Perf overhead | Trust anchor | Maturity |
|---|---|---|---|
| TEE (TDX/SEV) | Low (5–15%) | Hardware | Production |
| HE | Extreme (>1000×) | Cryptographic | Research/niche |
| SMPC | Medium-high | Protocol | Limited deploy |

## Cloudberry relevance
Cloudberry relevance sits at the intersection of confidential AI inference and semiconductor IP licensing. As GF and other fabs push secure enclave IP into chiplet and edge-AI designs, TEE integration becomes a differentiator in custom silicon. Deal-flow angles: startups building attestation infrastructure, confidential ML serving (relevant to any portfolio company handling regulated data), and RISC-V TEE IP vendors targeting GF process nodes where ARM licensing is cost-prohibitive.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
