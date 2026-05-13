---
type: concept
slug: federated-learning
canonical_name: Federated Learning
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
- ant-group-fate-privacy-preserving-ai
- apheris
- apple
- bitfount
- clustar-technology
- datafleets-acquired-by-liveramp
- featureform
- fedml
- fedn-scaleout-systems
- flower-labs
- fusion-ai-tripleblind
- google-deepmind-google-research
- google-google-research-tensorflow-federated
- ibm-ibm-federated-learning
- ibm
- inpher
- intellegens
- leapfrog-ai-leapfrog-data
- lifebit
- lynxmd
- meta-ai-pytorch-flower-integration
- meta-ai
- mindtech-global
- nvidia-flare
- nvidia
- oblivious-antigranular
- openmined
- owkin
- primihub
- rhino-health
- secure-ai-labs-sail
- sherpaai
- substra-foundation-substra-owkin-spin-off
- tongdun-technology
- unifyid-now-prove-ai
- vaidyam-formerly-behaveai-clarity-ai-health
- vaidyam-rhino-health
- webank-ai-fate-framework
- xayn
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

# Federated Learning

*Kind: technology*

## Physics / mechanism

Federated learning (FL) trains a shared model across distributed data sources without moving raw data to a central server. Each node runs local SGD on its own dataset, then transmits only gradient updates or model weight deltas to an aggregator (commonly FedAvg). The aggregator averages updates—optionally weighted by local dataset size—and pushes the revised global model back. Key parameters: communication rounds (typically 50–1000), client participation fraction, local epochs per round, and differential privacy noise budget (ε, δ). State of the art: Google's production FL on Gboard handles ~500M devices; academic benchmarks show <2% accuracy gap vs. centralized training on IID data, larger gaps on non-IID distributions. Secure aggregation adds cryptographic overhead of ~10–30% latency.

## Competitive landscape

Central server training with strict data-sharing contracts is the direct alternative—lower complexity, higher accuracy, but legally untenable under GDPR/HIPAA in many verticals. Split learning partitions the model itself rather than data. Swarm learning removes the central aggregator via blockchain coordination. On-device inference (TinyML) is adjacent but orthogonal—inference, not training.

## Cloudberry relevance

| Approach | Data centralization | Communication cost | Accuracy vs. centralized |
|---|---|---|---|
| Federated Learning | None | Medium–High | 1–5% gap |
| Split Learning | Partial | Low | ~2–3% gap |
| Central Training | Full | Minimal | Baseline |


Relevance is indirect but real. FL is becoming a hard IP requirement for edge-AI silicon—inference chips (neuromorphic, photonic compute accelerators) need FL-compatible training pipelines to win healthcare and automotive design-ins. For Cloudberry/GlobalFoundries-LP deal flow: fabless startups building secure-enclave chiplets or photonic AI accelerators increasingly need FL as a system-level differentiator to access regulated-data markets. Worth tracking as a procurement dependency rather than a primary investment thesis.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
