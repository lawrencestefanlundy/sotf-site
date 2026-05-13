---
type: concept
slug: differential-privacy
canonical_name: Differential Privacy
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
- anonos
- apheris
- apple-wwdc-dp-team
- apple
- bitfount
- bitglass-acquired-by-forcepoint
- cape-privacy-acquired-by-themis-ai
- cape-privacy-now-cape
- decentriq
- dpella
- duality-technologies
- google
- gretelai
- habu
- hazy
- incentive-inpher
- iqvia
- leapyear-technologies
- lynx-analytics
- meta
- microsoft
- mostly-ai
- oblivious-ai
- oblivious
- openmined
- privacy-dynamics
- privately
- privitar
- sarus-technologies
- spirent-communications-intellicheck-privacyguard-unit
- statice-acquired-by-anonos
- statice
- tumult-analytics-tumult-labs
- tumult-labs
- vaultree
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

# Differential Privacy

*Kind: technology*

## Physics / mechanism

Differential privacy (DP) adds calibrated statistical noise to query outputs or training gradients so that the presence or absence of any single record changes the output distribution by at most a multiplicative factor e^ε — the privacy budget. Smaller ε means stronger privacy, larger noise, lower utility. The Gaussian and Laplace mechanisms are workhorses; the Rényi DP and zero-concentrated DP variants offer tighter composition accounting. Local DP (noise at source) versus central DP (noise at aggregator) is the key architectural split. Google, Apple, and the US Census Bureau deploy central/local DP at scale; state-of-the-art ML training (DP-SGD via Opacus/TF Privacy) achieves ImageNet-class accuracy at ε ≈ 8–10 with clipping norm ~1.0.

## Competitive landscape

Competing approaches: secure multi-party computation (MPC) and homomorphic encryption (HE) preserve exact outputs but carry 10³–10⁶× compute overhead. Federated learning reduces data exposure but provides no formal privacy guarantee without DP layered on top. Synthetic data generation (e.g., SDV, Gretel) is easier to deploy but lacks composable, auditable guarantees. Trusted execution environments (TEEs — Intel TDX, AMD SEV) protect computation rather than the statistical output. In practice, most enterprise deployments combine DP + federated learning + TEEs.

## Cloudberry relevance

| Approach | Formal guarantee | Compute overhead | Auditability |
|---|---|---|---|
| Differential Privacy | Yes (ε-δ) | Low–moderate | High |
| Homomorphic Encryption | Yes (exact) | Very high | Medium |
| Synthetic Data | No | Low | Low |


Cloudberry relevance is indirect but real. Semiconductor IP for privacy-preserving compute — on-device DP noise injection in NPU silicon, TEE-integrated DP accelerators — is an emerging design-win angle at GlobalFoundries-node fabless players. Lunar portfolio companies building B2B data infrastructure increasingly need DP compliance for EU AI Act and GDPR audit trails. DP-capable edge inference chips targeting healthcare and fintech verticals are a credible deal-flow screen for deep-tech seed rounds.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
