---
type: concept
slug: nvidia-roadmap
canonical_name: NVIDIA datacentre roadmap (Rubin to Feynman)
aliases:
- Vera Rubin
- Rubin Ultra
- Feynman GPU
- NVL144
- NVL576
- NVL1152
- Kyber rack
- nvidia accelerator roadmap
parent_concepts:
- compute-architecture
- compute
related_concepts:
- hbm
- optical-interconnect
sources:
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2026-06-23-semidoped-daily-update]]'
- '[[2026-06-01-hbm-state-of-play]]'
- '[[2026-03-17-compute-specialisation-equilibrium-aws-rises-to-the-agentic]]'
- '[[2026-03-11-ai-power-thermal-binding-direct-to-chip-liquid-cooling]]'
- '[[2026-07-10-workload-phase-silicon-sweep]]'
- '[[2026-07-05-semianalysis-kyber-nvl144-delayed-2028]]'
- '[[2026-03-16-nvidia-vera-rubin-platform]]'
- '[[2026-06-30-compute-specialisation-equilibrium-deepseek-s-dspark-just]]'
- '[[2026-03-03-ai-power-thermal-binding-nvidia-vera-rubin-and-feynman]]'
- '[[2026-openai-titan-custom-chip]]'
- '[[2026-07-13-sk-hynix-record-fall-hbm4-three-supplier]]'
- '[[2026-03-19-compute-specialisation-equilibrium-how-nvidia-s-20-billion]]'
- '[[2026-stargate-expansion-7gw]]'
frontier:
- Feynman FLOPS and rack power are unannounced. What is the actual 2028 number?
- Which of NVIDIA's quoted EF figures are dense vs sparse NVFP4?
- VR NVL72 rack power at volume (120-130kW claimed) vs the 2.3kW Max-P per-GPU creep?
- Groq LPX full-system power (LP30 ~600W/chip is an unconfirmed analyst estimate)?
- 'NVL1152 (Kyber, CPO NVLink): 2028 or 2029 in practice?'
last_updated: 2026-07-21
tags:
- concept
- reference
- canonical-benchmark
mention_count: 37
sources_7d: 0
sources_30d: 3
recent_mentions:
- slug: 2026-07-13-sk-hynix-record-fall-hbm4-three-supplier
  title: SK Hynix record one-day fall as HBM4 goes three-supplier
  date: '2026-07-13'
  kind: web
- slug: 2026-07-10-workload-phase-silicon-sweep
  title: 'Workload-phase silicon sweep: pre-training / RL / prefill / decode procurement split'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-05-semianalysis-kyber-nvl144-delayed-2028
  title: 'SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled'
  date: '2026-07-05'
  kind: web
- slug: 2026-06-30-compute-specialisation-equilibrium-deepseek-s-dspark-just
  title: DeepSeek's DSpark Just Made Nvidia's Most Important New Bet Harder to Close
  date: '2026-06-30'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-01-hbm-state-of-play
  title: HBM state of play (mid-2026) — technology, supercycle, three-supplier standing
  date: '2026-06-01'
  kind: web
- slug: 2026-03-19-compute-specialisation-equilibrium-how-nvidia-s-20-billion
  title: How Nvidia's $20 billion Groq 3 LPU deal reshapes the Nvidia Vera Rubin Platform
  date: '2026-03-19'
  kind: web
- slug: 2026-03-17-compute-specialisation-equilibrium-aws-rises-to-the-agentic
  title: AWS Rises to the Agentic AI Moment with Cerebras Integration for Fast Inference
  date: '2026-03-17'
  kind: web
neighbors:
- slug: hbm
  name: HBM (High-Bandwidth Memory)
  path: /memory/mainstream-memory/hbm/
  macro: memory
- slug: optical-interconnect
  name: Optical Interconnect
  path: /communications/optical-interconnect/optical-interconnect/
  macro: communications
---
**Purpose: the canonical comparator for every inference-class chip we diligence.** Any startup claiming an energy, cost, or latency win gets compared against the NVIDIA generation that ships when THEY ship, not against a B200. Built 21 Jul 2026 from GTC 2026 (Mar) + CES 2026 announcements and post-GTC reporting; refresh after each GTC/CES. Figures are NVIDIA-quoted unless marked [derived] or [estimate]; NVIDIA does not always state dense vs sparse, treat quoted EF as best-case marketing until benchmarked.

## The generations

| Platform | Ships | Rack config | FP4 | FP8 | Memory | Rack power | Notes |
|---|---|---|---|---|---|---|---|
| GB300 NVL72 (Blackwell Ultra) | shipping 2026 | 72 pkgs | ~1.1 EF | ~0.36 EF | HBM3e | ~140kW | today's baseline |
| Vera Rubin NVL72 (renamed from NVL144, package-count basis) | 2H 2026 | 72 Rubin pkgs (144 dies) | 3.6 EF | 1.2 EF | 13TB HBM4, 75TB fast | ~120-130kW (Oberon); CPX variant 8 EF NVFP4 @ 370kW | Rubin pkg = 50 PF FP4, 288GB HBM4, 1.8kW Max-Q / 2.3kW Max-P; Vera CPU 88 cores; NVLink6 260TB/s |
| Rubin Ultra NVL576 | 2H 2027 | 144 pkgs x 4 reticle dies (Kyber, vertical trays, liquid) | 15 EF | 5 EF | 1TB HBM4e/pkg, 365TB fast | 600kW | 100 PF FP4/pkg; NVLink7 1.5PB/s |
| Feynman + Rosa CPU | 2028 | Oberon 576 or Kyber up to NVL1152 | not announced | not announced | custom/stacked HBM | not announced | 3D die stacking; FIRST CPO NVLink switches (optical scale-up, pulled in ~5yrs from ~2033); Intel foundry/EMIB in the supply chain |

## The Groq line (low-latency inference lane)

NVIDIA bought Groq's assets for ~$20B (struck 24 Dec 2025) and runs it Mellanox-style, as the low-latency decode accelerator inside the platform:

- **Groq 3 LPU (LP30), ships Q3 2026:** 500MB SRAM/chip, 1.2 PF FP8, Samsung 4nm (LP4X), ~600W/chip [unconfirmed analyst estimate]. LPX rack = 256 LPUs, 128GB total SRAM, 800-1,000 tok/s per user.
- **Claim:** LPX + VR NVL72 = up to 35x tokens/W vs Blackwell NVL72 at extreme-speed inference [NVIDIA marketing, specific operating point, unbenchmarked].
- **LP35** adds NVFP4, aligned to Rubin Ultra (2027). **LP40** aligned to Feynman (2028), TSMC N3P, CoWoS-R, native NVLink.
- Implication for diligence: the "GPUs are bad at low-batch decode" wedge is no longer an open flank. Any latency-first startup pitch now competes with Groq-inside-NVIDIA, with NVFP4 and NVLink attach.

## Derived perf/W benchmarks [derived from the table above]

Chip level, FP8 dense:
- B200: ~4.5 TFLOPS/W (4.5 PF @ ~1kW), the 2025 baseline
- Rubin package: 7.2-9.3 TFLOPS/W (16.7 PF @ 2.3-1.8kW), shipping 2H 2026

Rack level, all-in (compute + CPU + fabric + cooling overhead in rack power):
- GB300 NVL72: ~7.9 TFLOPS/W FP4
- VR NVL72: ~9.2 TFLOPS/W FP8, ~27.7 TFLOPS/W FP4 (at the 130kW figure; scales down if real racks run hotter)
- Rubin Ultra NVL576: ~8.3 TFLOPS/W FP8, ~25 TFLOPS/W FP4

Theoretical token ceiling (70B-class FP8, 140 GFLOP/token, 100% utilisation, no memory/bandwidth bound, so a ceiling not a benchmark):
- VR NVL72: ~66 tok/s/W
- Rubin Ultra NVL576: ~60 tok/s/W

## The bar for a startup taping out 2028, deploying 2029

1. **Rack-level FP4/NVFP4 all-in is the inference currency:** ~25 TFLOPS/W ships 2H 2027 (Rubin Ultra). Feynman-era [estimate, historical cadence of ~1.5-2x perf/W per generation]: ~40-50 TFLOPS/W FP4, ~12-17 TFLOPS/W FP8 by 2028-29. A challenger needs a chip-level number well above this, because it carries no rack ecosystem and pays its own overheads.
2. **Chip-level FP8:** beat ~10 TFLOPS/W to matter, ~15+ to be compelling at 2029 deployment.
3. **Latency lane:** 800-1,000 tok/s/user and a claimed 35x tokens/W regime is the incumbent offer from Q3 2026, NVFP4 from 2027.
4. **Interconnect:** CPO NVLink arrives 2028 (Feynman). Any thesis whose differentiator is "we remove electrical data movement" decays on this schedule; scale-up worlds go to 576-1,152 GPU packages optically.
5. **Memory:** HBM4 (2026), HBM4e 1TB/pkg (2027), custom stacked HBM (2028). SRAM-heavy latency architectures are now in-house via Groq.

## Sources (tier 4-5 press + vendor, GTC/CES 2026 cycle)

- Tom's Hardware: [roadmap w/ Rosa + Feynman + Groq LPU](https://www.tomshardware.com/pc-components/gpus/nvidia-updates-data-center-roadmap-with-rosa-cpu-and-stacked-feynman-gpus-optical-nvlink-groq-lpus-with-nvfp4-and-nvlink-also-on-deck), [Rubin/Rubin Ultra/Feynman announce](https://www.tomshardware.com/pc-components/gpus/nvidia-announces-rubin-gpus-in-2026-rubin-ultra-in-2027-feynam-after), [Groq 3 LPU / $20B deal](https://www.tomshardware.com/tech-industry/semiconductors/nvidias-20-billion-groq-deal-produces-its-first-chip)
- HPCwire: [NVL1152 + scale-up CPO](https://www.hpcwire.com/2026/03/17/huang-shares-nvidia-roadmap-showing-more-chips-nvl1152-scale-up-cpo/), [silicon photonics roadmap](https://www.hpcwire.com/2026/04/20/inside-nvidias-silicon-photonics-roadmap/)
- DCD: [Rubin Ultra NVL576 600kW](https://www.datacenterdynamics.com/en/news/nvidias-rubin-ultra-nvl576-rack-expected-to-be-600kw-coming-second-half-of-2027/)
- More Than Moore: [Groq LP30/LPX specs](https://morethanmoore.substack.com/p/nvidia-introduces-groq-lp30-and-lpx)
- Groq newsroom: [licensing agreement](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale)
- SemiAnalysis: [Vera Rubin extreme co-design](https://newsletter.semianalysis.com/p/vera-rubin-extreme-co-design-an-evolution), [GTC 2026 inference kingdom](https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands)
- Ming-Chi Kuo (X, 6 Jan 2026): NVL144 renamed to NVL72 (package-count basis)
