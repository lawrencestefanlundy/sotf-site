---
type: concept
slug: state-space-models
canonical_name: State Space Models (SSMs)
aliases:
- SSM
- selective state space models
- Mamba
- linear-time sequence models
parent_concepts: []
related_concepts:
- neuromorphic-computing
- in-memory-computing
- edge-ai
sources:
- '[[2025-cartesia-on-device-ssm]]'
- '[[2026-06-18-sensifai-hybrids-deck]]'
- '[[2026-07-31-etched-research-sprint]]'
- '[[2025-06-wisconsin-mamba-chiplet-gf22]]'
- '[[2025-08-emamba-edge-acceleration]]'
- '[[2026-07-01-sensifai-memo-streaming-physical-ai]]'
- '[[2026-03-mamba-3-iclr]]'
- '[[2026-06-23-on-device-llms-state-of-union-2026]]'
frontier:
- Does the energy advantage of dedicated SSM silicon over optimised kernels on existing NPUs stay large (>5x) and durable, or does software close it to ~2x?
- Does a sub-watt always-on streaming socket (hearing aids, AR perception) reach volume general silicon cannot serve, giving a dedicated SSM ASIC a why-now?
- Does the architecture stabilise (Mamba-3 onwards) enough to tape out fixed-function silicon, or does it keep moving fast enough to favour programmable / kernel approaches?
last_updated: 2026-06-18
tags:
- concept
mention_count: 22
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2026-07-31-etched-research-sprint
  title: Etched research sprint — tape-out speed, HBM supply, customer orders (4-lane web sweep)
  date: '2026-07-31'
  kind: web
- slug: 2026-07-01-sensifai-memo-streaming-physical-ai
  title: SensifAI — Purpose-Built Silicon for Streaming Physical AI (funding memo)
  date: '2026-07-01'
  kind: web
- slug: 2026-06-23-on-device-llms-state-of-union-2026
  title: On-device LLMs, the small-model frontier, and NPU throughput (2025-26 update)
  date: '2026-06-23'
  kind: web
- slug: 2026-06-18-sensifai-hybrids-deck
  title: SensifAI — Funding Round deck (sensifai.vercel.app/hybrids)
  date: '2026-06-18'
  kind: web
- slug: 2026-03-mamba-3-iclr
  title: Mamba-3 (ICLR 2026)
  date: '2026-03-01'
  kind: web
- slug: 2025-08-emamba-edge-acceleration
  title: 'eMamba: Efficient Acceleration Framework for Mamba Models in Edge Computing'
  date: '2025-08-14'
  kind: web
- slug: 2025-cartesia-on-device-ssm
  title: Cartesia — The on-device intelligence update
  date: '2025-08-01'
  kind: web
- slug: 2025-06-wisconsin-mamba-chiplet-gf22
  title: First Mamba Chiplet in GF 22nm — UW–Madison CHIPS
  date: '2025-06-12'
  kind: web
neighbors:
- slug: neuromorphic-computing
  name: Neuromorphic Computing
  path: /compute/non-conventional/neuromorphic-computing/
  macro: compute
- slug: in-memory-computing
  name: In-Memory Computing
  path: /memory/emerging-memory/in-memory-computing/
  macro: memory
- slug: edge-ai
  name: Edge AI
  path: /compute/ai-edge/edge-ai/
  macro: compute
---
## What an SSM is (one paragraph)

A state-space model processes a sequence by carrying a **fixed-size internal "state"** that summarises everything seen so far, updating it token by token, instead of re-attending over the whole history like a transformer. The cost is **linear in sequence length** (O(L)) with **constant memory at inference**, versus the transformer's quadratic O(L²) attention and a KV-cache that grows with context. The modern, practical form is the **selective SSM** (Mamba lineage), where the state-update is input-dependent. Those two properties (linear scaling, constant inference memory) are the entire reason SSMs matter for edge and streaming.

## Model state of the art (2026): hybrids won, not pure SSMs

## Why-now for the edge (the strongest part of the bull case)

- **Streaming without buffering.** An SSM does not need to wait for a full context window: streaming models emit a first token ~120ms after the first audio arrives. For always-on audio, this is a structural fit general transformer inference cannot match on the same power budget.
- **World models / physical AI.** Real-time, causal, on-device world models (NVIDIA Cosmos 3 Edge, Odyssey-2, 6G agentic world-modelling research) increasingly use lightweight recurrent state-space cores for fast look-ahead reasoning at the edge. This is the emerging, datable why-now narrative, though still nascent.
- The honest counter: the why-now has been "forming" for ~2 years (SSM hype peaked around 2024) without yet producing a sub-watt volume socket. That is exactly the open question for Sensifai.

## Hardware-acceleration landscape: where the value is being captured

The decisive question for a chip company is **who serves SSM inference, and on what silicon.** Three layers:

**Read across the layers:** the energy advantage of dedicated SSM silicon is genuine, but the commercial gravity so far sits at layer 1 (software on commodity silicon). A dedicated-ASIC company has to prove its layer-3 energy/cost delta is big and durable enough to beat a fast-moving layer-1 incumbent into a specific socket.

## Comparable set for a dedicated SSM edge play (hand-built; the auto comp query returned none)

| Company | What | Hardware axis | Relevance to Sensifai |
|---|---|---|---|
| **Cartesia** | SSM voice (Sonic), Rene LM, Mamba-3 co-author | **Software** kernels on Apple/commodity | Primary competitor; owns the architecture; phone/laptop, not sub-watt |
| **Applied Brain Research** | LMU state-space edge AI + silicon/IP | Own silicon/IP | Closest commercial dedicated-SSM-hardware analogue |
| **Femtoai** | Sparsity accelerator | Own ASIC, component | Precedent for the realistic exit (hearing-aid component, not IPO) |
| UW-Madison (e-chip-V1) | First Mamba ASIC chiplet | ASIC on ****Globalfoundries** 22nm** | Proves silicon feasibility; academic, GF-lane |
| **Etched** | Transformer-only ASIC (Sohu) | Own ASIC | The "one-architecture ASIC" analogy Lawrence used; different (datacentre, transformer) |

## Is there room for Sensifai?

**Bear (the default gravity)**
- SSMs plateaued into a hybrid niche; the addressable "SSM-specific silicon" TAM is a subset of an already-niche edge-inference market.
- The architecture is still moving (Mamba-2 → Mamba-3 in ~18 months): fixed-function tape-out risks being out of date, the classic edge-AI-silicon trap (cf. Mythic, Blaze, Accelero, which died of moving targets + no market pull).
- Cartesia owns the architecture, moves faster, has no fab risk, and can push down into more devices as Apple/Qualcomm NPUs improve. Customers default to "good enough" ARM Cortex / Qualcomm.
- Realistic exit is a component sale (femtoAI-shaped), capping upside; no startup cohort suggests the market is early or absent.

**Provisional verdict (pre-DD):** Room exists, but it is the **narrow exception**, not the broad case. The architecture-displacement story is over (hybrids won), so the entire thesis rests on a sub-watt streaming niche plus a durable silicon energy advantage. That is investible *if* DD lands a real why-now socket and a >5x energy delta; otherwise it routes to the same component-not-IPO, demand-gated read as the rest of **Low Power Edge Compute**. Worth the diligence; not yet a conviction yes.

## Frontier

- Does the energy advantage of dedicated SSM silicon over optimised kernels on existing NPUs stay large (>5x) and durable, or does software close it to ~2x?
- Does a sub-watt always-on streaming socket (hearing aids, AR perception) reach volume general silicon cannot serve, giving a dedicated SSM ASIC a why-now?
- Does the architecture stabilise (Mamba-3 onwards) enough to justify fixed-function silicon, or keep favouring programmable / kernel approaches?
- Where does value accrue: the model (Cartesia), the kernels (open-source), or the silicon? If the model and kernels are open/commodity, can the chip alone hold durable value?

## Sources

Primary anchors (filed): **2026 03 Mamba 3 Iclr** (tier 1), **2025 08 Emamba Edge Acceleration** (tier 1), **2025 06 Wisconsin Mamba Chiplet Gf22** (tier 5), **2025 Cartesia On Device Ssm** (tier 6). Supporting (web, 18 Jun 2026 sweep): AI21 "rise of hybrid LLMs"; Applied Brain Research "Why SSMs are the future of edge AI"; "Quantizing Small-Scale State-Space Models for Edge AI" (arXiv 2506.12480); NVIDIA Cosmos 3 (physical-AI why-now).
