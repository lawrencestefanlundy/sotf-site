---
type: concept
slug: hearing-aid-silicon-beachhead
canonical_name: Hearing aids as an edge-AI silicon beachhead
aliases:
- hearing aid beachhead
- hearing-aid chip market
parent_concepts:
- edge-ai
related_concepts:
- in-memory-computing
- neuromorphic-computing
- state-space-models
sources:
- '[[2026-07-01-hearing-aid-market-structure-edge-ai-beachhead]]'
frontier:
- Does Apple/OTC commoditisation shrink or grow the standalone medical hearing-aid silicon socket by 2028?
- Does any Big Five OEM ever second-source a novel merchant inference chip, or stay in-house / ON-locked?
last_updated: 2026-07-01
tags:
- concept
- edge-ai
- hearing-aids
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: in-memory-computing
  name: In-Memory Computing
  path: /memory/emerging-memory/in-memory-computing/
  macro: memory
- slug: neuromorphic-computing
  name: Neuromorphic Computing
  path: /compute/non-conventional/neuromorphic-computing/
  macro: compute
- slug: state-space-models
  name: State Space Models (SSMs)
  path: /ai-software/models-inference/state-space-models/
  macro: ai-software
---
## Why it looks good
Genuine always-on, sub-watt, latency-bound inference in a wearable form factor. A clean technical fit for neuromorphic / analog-in-memory / SSM-ASIC designs, and a real clinical need driven by **Ageing Population**.

## Why it fails the venture test (small / slow / concentrated / commoditised)
- **Small at the layer that matters.** Device market ~$9.7–10.5B (2025/26), ~22.7M units/yr, but silicon content is a few $/unit → **chip-layer TAM low hundreds of $M**, of which a startup wins a slice. The $10B headline is the wrong denominator.
- **Slow.** ~6–9% device CAGR, and DSPs are specced to last years — a multi-year qualification/design-win cadence per account. Revenue arrives slowly even on a win.
- **Concentrated & partly captive.** Big Five (Sonova, WS Audiology, Demant, GN, Starkey) ≈ **84% US / 90%+ global**, vertically integrated into clinics and benefit managers. Buyers mostly **make their own silicon** (Sonova proprietary DSP/ASIC) or buy the incumbent merchant SoC (**ON Semiconductor Ezairo**, already a heterogeneous CPU+DSP+accelerator part). A new entrant sells into ~5 accounts, several closed.
- **Commoditised from above.** FDA-cleared **AirPods Pro 2 as an OTC hearing aid** (Sept 2024), $250 vs $1,000+, 100M+ units — value migrates to Apple's own silicon in the CE tier you can't sell into.

## Sources
- (size, growth, concentration, Apple/OTC, ONsemi/Sonova silicon)
