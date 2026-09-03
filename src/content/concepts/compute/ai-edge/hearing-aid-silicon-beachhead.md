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

## Confirmed arithmetically, 15 Jul 2026
A three-part research sprint ([The ear as a sensing site](/sensing/biosensing/ear-as-sensing-site/)) tested this page rather than assuming it, and **confirmed it at ~80%** with better numbers. Quote these rather than re-deriving:
- **23.16M hearing aids sold in 2025, +2.1% YoY** — [EHIMA](https://www.ehima.com/about-ehima/hearing-aid-sales/), the manufacturers' own association, i.e. **actual member sales, not an analyst forecast**. This is the highest-quality number in the cluster. (Prior years: 22.69M/2024, 21.81M/2023.)
- **Top-5 concentration 92.4% (2024)** — tighter than the ~84%/90% previously carried here.
- **Chip-layer TAM ~$115M–$460M/yr** at $5–20 sensing/SoC content. ⚠️ The content figure is an **estimate** — no independent BOM teardown found. Treat as an order-of-magnitude check that the answer is "hundreds of millions, not billions"; that survives a 3× error either way. Unit count and concentration are solid, the BOM is not.
- **The one un-absorbed corner:** **Naox Technologies** took the **first-ever FDA 510(k) for in-ear EEG (Jan 2026)**. Regulated-medical is the only position with a proof point — and it is a medical-device business, not a silicon one. This is the exception that defines the rule, not a counter-example to it.

## Sources
- (size, growth, concentration, Apple/OTC, ONsemi/Sonova silicon)
