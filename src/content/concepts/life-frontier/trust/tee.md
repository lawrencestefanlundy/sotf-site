---
type: concept
slug: tee
canonical_name: TEE
aliases: []
kind: technology
parent_concepts:
- life-frontier
- trust
related_concepts: []
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
mention_count: 8
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2025-10-09-a-specific-theory-of-sovereign-ai
  title: A Specific Theory of Sovereign AI
  date: '2025-10-09'
  kind: substack
- slug: 2023-10-19-e20-the-state-of-privacy-enhancing
  title: Understanding Privacy Enhancing Technology (Feat. Karim Eldefrawy, Confidencial.io)
  date: '2023-10-19'
  kind: substack
- slug: 2023-10-13-e19-trusted-execution-environments
  title: Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)
  date: '2023-10-13'
  kind: substack
- slug: 2023-06-30-e06-the-model-t-moment-for-bits-llms
  title: '🔮 E06: Large Language Models and the Assembly Line'
  date: '2023-06-30'
  kind: substack
neighbors: []
---
## Physics / mechanism

A Trusted Execution Environment is a hardware-isolated compute enclave running alongside the main OS, enforcing confidentiality and integrity of code and data even against a privileged attacker. Implemented via dedicated silicon — ARM TrustZone partitions the CPU into Normal/Secure worlds; Intel TDX and AMD SEV-SNP extend isolation to full VMs using memory encryption. Key parameters: memory encryption latency overhead (~5–15%), attestation round-trip (<100 ms for remote attestation via ECDSA/DCAP), and TCB surface area (smaller = better; measured in lines of verified firmware). Current SoA: CCA (Confidential Compute Architecture) on ARMv9 introduces Realm Management Extensions, enabling dynamic realm creation without OEM key dependency.

## Competitive landscape

Competing approaches: homomorphic encryption (HE) handles computation on encrypted data without hardware trust anchors but carries 1,000–10,000× compute overhead — impractical for inference workloads today. Secure multi-party computation (SMPC) distributes trust across parties but requires coordination overhead. RISC-V enclaves (Keystone, Penglai) offer open-source TCB alternatives. The confidential computing stack is increasingly converging around CCA/TDX/SEV-SNP as the hyperscaler-validated trio.

| Approach | Perf overhead | Trust anchor | Maturity |
|---|---|---|---|
| TEE (TDX/SEV) | Low (5–15%) | Hardware | Production |
| HE | Extreme (>1000×) | Cryptographic | Research/niche |
| SMPC | Medium-high | Protocol | Limited deploy |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
