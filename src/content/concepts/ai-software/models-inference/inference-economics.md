---
type: concept
slug: inference-economics
canonical_name: 'Inference economics: the two customer KPIs'
aliases:
- cost per token
- tokens per watt
- tokens per watt per dollar
- TCO per million tokens
- power envelope
- energy per inference
kind: framework
parent_concepts:
- memory-wall
related_concepts:
- token-cost-stack
- prefill-vs-decode
- analog-in-memory-compute
- processing-in-memory
- adc-bottleneck
- hbm
- nand-flash
- photonic-compute
sources:
- '[[2026-07-10-hyperscaler-token-economics-sweep]]'
- '[[2026-07-07-high-bandwidth-flash-the-full-report]]'
- '[[2026-07-31-positron-research-sprint]]'
- '[[2026-06-28-frontier-llm-scaling-chinese-open-weight-models-are-nipping]]'
- '[[2026-05-29-silicon-shock-the-macro-of-tech-inflation]]'
frontier:
- Does heterogeneous prefill/decode silicon reach VOLUME procurement (Groq 3 LPX inside Vera Rubin ships Q3 2026 — does a hyperscaler deploy it at fleet scale by 2027)?
- Does tokens/sec/W become a standardised edge benchmark (an MLPerf-style edge-LLM metric), or stay vendor marketing?
- Does price-per-task (Epoch's capability-adjusted metric) displace price-per-token as reasoning models inflate token counts?
- Where does the RL-rollout workload settle — on inference silicon (the Maia 200 bet) or unified training platforms (the Trainium bet)?
last_updated: '2026-07-27'
tags:
- concept
- framework
- inference
- economics
- map
descendants:
- token-cost-stack
mention_count: 22
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-14-chip-tail-verification-sweep
  title: 'Chip-comparison tail verification sweep: 37 companies re-verified, consolidation wave confirmed'
  date: '2026-08-14'
  kind: web
- slug: 2026-07-31-positron-research-sprint
  title: 'Positron AI research sprint: architecture, funding, customers, manufacturing'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-26-ai-native-app-retention-margins
  title: AI-native application retention and gross margin benchmarks, mid-2026
  date: '2026-07-26'
  kind: web
- slug: 2026-07-20-ai-inference-economics-column
  title: Money Stuff-style column on AI model pricing, open weights and datacentre monetisation
  date: '2026-07-20'
  kind: web
- slug: 2026-07-10-workload-phase-silicon-sweep
  title: 'Workload-phase silicon sweep: pre-training / RL / prefill / decode procurement split'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-10-inference-silicon-deep-research
  title: 'Deep research: measured vs claimed inference-silicon economics (adversarially verified, 23/25 claims confirmed)'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-10-hyperscaler-token-economics-sweep
  title: 'Hyperscaler inference-economics language sweep: cost per token as the datacentre KPI'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-10-edge-buyer-kpi-sweep
  title: 'Edge-AI buyer KPI sweep: power envelope + energy per work; cost per token absent'
  date: '2026-07-10'
  kind: web
neighbors:
- slug: prefill-vs-decode
  name: Prefill vs Decode (LLM inference phases)
  path: /compute/ai-edge/prefill-vs-decode/
  macro: compute
- slug: analog-in-memory-compute
  name: Analog In-Memory Compute
  path: /memory/emerging-memory/analog-in-memory-compute/
  macro: memory
- slug: processing-in-memory
  name: Processing-in-Memory (PIM)
  path: /memory/emerging-memory/processing-in-memory/
  macro: memory
- slug: adc-bottleneck
  name: ADC Bottleneck (analog in-memory compute)
  path: /compute/compute-architecture/adc-bottleneck/
  macro: compute
- slug: hbm
  name: HBM (High-Bandwidth Memory)
  path: /memory/mainstream-memory/hbm/
  macro: memory
- slug: nand-flash
  name: NAND Flash
  path: /memory/mainstream-memory/nand-flash/
  macro: memory
- slug: photonic-compute
  name: Photonic Compute
  path: /photonic-systems/photonic-compute/photonic-compute/
  macro: photonic-systems
---
The buyer-side frame for comparing every AI-compute approach in the KB. All the device taxonomies (analog vs digital CIM, resistive vs capacitive, PIM vs CIM) answer "how does it work"; this page answers **"which customer metric does it move"**. There are exactly 2, and they are different businesses. Web-verified 10 Jul 2026; the 3 source sweeps carry the full quote list.

## KPI 1 — Datacentre: cost per million tokens (spoken as tokens per watt)

The unit-economics KPI at every layer of the datacentre stack is **cost per million tokens**, computed as (TCO per hour) ÷ (tokens per second). Because every datacentre is power-capped, the buying decision collapses into **tokens per watt**: with power fixed, minimising $/token and maximising tokens/watt are the same optimisation. The dollar term rides on the watt term.

Canonical phrasings (dated, primary):
- **Nadella:** "tokens per watt per dollar" (LinkedIn, Jan 2025; restated Davos Jan 2026; used on the Q2 FY26 earnings call, 28 Jan 2026, where Maia 200 was claimed at >30% better tokens per dollar).
- **Huang:** "tokens per second per watt" (Q3 FY26 earnings call, Nov 2025); GTC 2026 keynote formula **Revenue = (Tokens per Watt) × (Available Gigawatts)**, with token price tiers ~$1/M (batch) to ~$150/M (real-time interactive).
- **Nvidia corporate** (blog, 15 Apr 2026): "Cost per token is the only metric that matters."
- **SemiAnalysis InferenceMAX** (Oct 2025): "TCO per million tokens" as the "true north" benchmark metric.
- **Google** reports it to Wall Street: Gemini serving unit costs down 78% over 2025 (Pichai, Q4 2025 earnings call, 4 Feb 2026).
- **AWS** denominates chip generations in **tokens per megawatt** (Trainium3 claimed ~5x Trainium2, re:Invent Dec 2025).

Power as the binding constraint, on the record: Huang "we are now a power-limited industry... your revenues are power limited" (GTC Mar 2025); Nadella "you may actually have a bunch of chips sitting in inventory that I can't plug in" (Nov 2025); Zuckerberg "we would probably build out bigger clusters than we currently can if we could get the energy" (Apr 2024).

**Nuances that stop naive $/token comparisons:**
- Cost per token is undefined without an interactivity SLA (tokens/sec/user). Nvidia's $1-vs-$150/M tiers and the InferenceMAX Pareto curves make the point; "goodput" (tokens meeting the SLA) is the correction term.
- **Price-per-task ≠ price-per-token.** Epoch AI: price to hit a fixed capability falls 9-900x/year depending on the task (GPT-4-level science Q&A: ~$20/M late 2022 → ~$0.40/M). Reasoning models inflate token counts, so token volume can overstate value delivered.
- First-party silicon owners often stay one level up in public (Google leads Ironwood with perf/watt, Meta MTIA with perf/TCO); the token framing is loudest from Nvidia and Microsoft.

## KPI 2 — Edge: work inside a fixed power/thermal envelope

Edge silicon is bought against a **fixed envelope** set by the product: battery capacity, skin-contact temperature (standards cap ~48°C, product teams target 41-42°C), form factor. Within the envelope the metric is **energy per unit of work** (TOPS/W, mJ per inference, µW at task), and the co-stated purchase drivers are latency and privacy. **Cost per token is absent from edge procurement**: chips are bought per-unit ($15-45 standard tier, RFQs with 12-18 month price commitments), and the token-cost saving of on-device inference accrues to the platform (Apple, Google, Qualcomm avoiding cloud opex), reaching the buyer as battery life, not dollars.

The 4 tiers buyers architect separately (evidence: Qualcomm sensing island, Syntiant wake-tier line, MediaTek's separate "Super Efficient NPU"):

| Tier | Power budget | Workload | Lead metric |
|---|---|---|---|
| Always-on wake/sense | ~10µW-1mW | keyword spotting, VAD, IMU/context | µW at task, mJ/inference (Ambiq KWS <1mJ, Syntiant 140µW) |
| Continuous perception | ~1-100mW | hearing-aid denoise (1-3mW budget), always-on vision, health | mW fit in battery-hours, TOPS/W (ST 3 TOPS/W) |
| Burst AI | ~0.1-2W | photo/video CV, translation, short LLM calls | sustained perf/W, thermal throttle behaviour |
| On-device LLM | ~2-8W | 1-8B local models (Gemini Nano, Apple FM) | tokens/sec + TTFT; **tokens/sec/W emerging** (Qwen 2.5 3B at 110 tok/s @ 4W, Dimensity 9500) |

Anchor datapoint for the always-on constraint: Meta rates Ray-Ban Live AI at ~30 minutes, explicitly thermally gated.

**The bridge between the KPIs:** both reduce to energy per token of work. The datacentre prices the energy in dollars (power-capped revenue), the edge prices it in joules (battery and skin). Tokens/sec/W is the same quantity appearing at both ends, which is why Chipstrat proposed it as THE edge-LLM metric (Nov 2024) and Huang put it in the revenue formula (Mar 2026).

## The workload split (what the datacentre customer actually buys for)

| Phase | Binding constraint | Metric | Silicon it favours |
|---|---|---|---|
| Pre-training | sustained FLOPS at 10k-100k-chip scale + all-reduce interconnect | FP8 FLOPS, collective bandwidth | full-fat GPU/TPU pods (GB300 NVL72, Ironwood superpods, Trainium3 UltraServers) |
| Post-training / RL | rollout generation = decode inside the training loop (largest wall-clock share in recent RL systems) | decode throughput + training interconnect | mixed fleets; Microsoft points Maia 200 (inference chip) at RL/synthetic data |
| Prefill | compute-bound, all prompt tokens in parallel, TTFT | TFLOPS per dollar (HBM lightly used) | high-FLOPS cheap-memory parts (the Rubin CPX concept: 30PF + GDDR7, no HBM) |
| Decode | memory-bandwidth-bound, sequential, KV cache reload per token; <5% tensor utilisation on H100, ~90% of request lifetime | GB/s per dollar, capacity for KV, cost per OUTPUT token (priced ~4x input) | bandwidth-first or SRAM parts (Groq LPU, Cerebras, SK Hynix AiMX, big-HBM GPUs) |

Procurement reality check (10 Jul 2026): **training-vs-inference silicon is real, committed capex** (Maia 200 Jan 2026, OpenAI-Broadcom "Jalapeño" inference ASIC Jun 2026, Meta MTIA 450/500, Google Ironwood). **Prefill/decode as separate pools of the same chip is production default** (DeepSeek published its EP32-prefill/EP144-decode configs Feb 2025; Nvidia Dynamo 1.0 GA; Google's Gemini stack). **Prefill/decode as different silicon is a committed roadmap, not yet volume procurement**: Nvidia announced the prefill-only Rubin CPX (Sep 2025), cancelled it (Mar 2026), then paid **~$20B to license Groq's SRAM LPU as a decode co-processor inside Vera Rubin** (Dec 2025, "Groq 3 LPX", Samsung 4nm, Q3 2026 target). The monopolist redesigning its flagship rack around a decode part is the strongest validation the decode socket will ever get, and the CPX cancellation is the equally honest caution. AWS ran the other way (killed Inferentia, unified Trainium) — resolving the picture: **the durable split is compute-optimised vs bandwidth-optimised, and that line cuts through the middle of inference.** Prefill sits with training; decode is the odd one out.

Demand-side accelerant: KV cache. Agentic/reasoning workloads emit 10-50x more tokens per request than 2024-era chat, contexts run to 1M tokens, and Llama-3.1-70B at batch 128 already needs ~40GB of KV — decode's share of cost rises structurally. Inference overall: ~one-third of AI compute in 2023 → ~half 2025 → ~two-thirds 2026 (Deloitte).

## The technology-agnostic corollary: photonics collapses into the same test

If buyers only pay for the KPI, every technical approach, however exotic, collapses into "what does it do to tokens/watt (datacentre) or joules-per-work-in-envelope (edge)". Photonics is the cleanest demonstration, because the market has already run the test:

## How to use this page

Compare any approach by asking, in order: (1) which KPI, cost-per-token or envelope? (2) if datacentre, which phase, and almost always the honest answer should be decode? (3) what does it do to the metric — tokens/watt for a datacentre part, energy-per-work-in-envelope for an edge part? (4) against whose roadmap — the Groq-inside-Rubin decode part is now the datacentre benchmark; the MCU-vendor eNVM shelf is the edge one. The company-by-company mapping lives in two kpi approach map; the variable decomposition (what produces the metric, and how to discount vendor claims by integration level) is **Token Cost Stack**.
