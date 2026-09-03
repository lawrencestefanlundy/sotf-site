---
type: concept
slug: edge-inference
canonical_name: Edge Inference
aliases: []
parent_concepts:
- ai-edge
- compute
related_concepts: []
sources:
- '[[2024-11-05-confidential-ai-the-dog-that-didnt]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2026-06-17-femtoai-company-profile]]'
- '[[2025-06-slm-future-agentic-ai-nvidia]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 27
frontier:
- Does the NVIDIA estimate that 40-70% of agentic LLM queries can be served by specialised small models survive independent replication on production agent traces, or is it an upper bound derived from narrow benchmarks?
- Can the ReRAM/MRAM hybrid memory approach in QMC be manufactured at edge BOM prices, or does it remain a simulation-and-calibrated-model result?
- Does the H1+H2 structural argument for INT8 dispatch-invariance hold on transformer and SLM graphs, not just CNNs, and would certification bodies accept it as a determinism guarantee?
- Is there any measured path to sustained multi-hour generative inference inside a 41-42C skin-temperature design target, or does the category stay burst-only regardless of silicon efficiency?
- Does the NVIDIA 40-70% substitution estimate hold in measured production agentic traffic, and what fraction of those invocations fit within a hundreds-of-mW sustained envelope rather than a plugged-in edge box?
- Can outlier-aware quantisation plus emerging non-volatile memory (QMC-style) deliver measured tokens/sec/W on silicon, and how much device-noise-induced accuracy loss survives at 1-3mW hearing-aid-class budgets?
- Do EMC-point tabulation and tail-aware latency models generalise beyond Jetson Orin Nano to ARM SoCs and NPUs, and what deadline-miss rate do they achieve under bursty 100k-cycle workloads?
- Does analogue RF computing over MU-MIMO reach useful MVM accuracy at claimed energy levels in a hardware demonstration, and what is the base station cost per served client?
- Do INT8 dispatch-invariance guarantees (H1+H2) extend to transformer/attention graphs and to non-ONNX-Runtime edge stacks, or is bit-exactness limited to Conv-dominated CNNs?
scorecard:
  viability: 4
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
sources_7d: 1
sources_30d: 1
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-10-edge-buyer-kpi-sweep
  title: 'Edge-AI buyer KPI sweep: power envelope + energy per work; cost per token absent'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-07-high-bandwidth-flash-the-full-report
  title: 'High Bandwidth Flash: The Full Report'
  date: '2026-07-07'
  kind: web
- slug: 2026-06-17-femtoai-company-profile
  title: femtoAI (formerly Femtosense) — company profile, funding, leadership
  date: '2026-06-17'
  kind: web
- slug: 2025-06-slm-future-agentic-ai-nvidia
  title: Small Language Models are the Future of Agentic AI (NVIDIA Research)
  date: '2025-06-01'
  kind: web
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2024-11-05-confidential-ai-the-dog-that-didnt
  title: Confidential AI
  date: '2024-11-05'
  kind: substack
neighbors: []
---
**Edge inference is running trained neural networks on the device that captured the data rather than in a datacentre, and it has moved from lab demos to shipping silicon in a market that buys against a fixed power envelope rather than a cost per token.**

## Summary

Edge inference means executing the forward pass of a trained model locally: on a microcontroller, a hearing-aid SoC, a phone NPU, a Raspberry Pi, a Jetson module or an FPGA, instead of sending data to a cloud GPU. The span of workloads is enormous. At one end sits keyword spotting drawing 140 microwatts on a dedicated neural decision processor; at the other, small language models of a few billion parameters generating tokens on consumer hardware **2025 06 Slm Future Agentic Ai Nvidia**. Treating these as one technology is a mistake, and most disagreement about whether edge inference "works" comes from conflating them.

There are three engineering levers. First, shrink the model: post-training INT8 quantisation, and more radically the substitution of task-specialised small models for general-purpose large ones. NVIDIA Research argues existing agentic systems could serve 40-70% of their LLM queries with specialised SLMs, and that paying 10-30x for unneeded capability is unsustainable at scale **2025 06 Slm Future Agentic Ai Nvidia**. Second, specialise the silicon: sparsity-aware digital accelerators, spiking-neural-network accelerators on low-cost FPGAs, and analogue in-memory or in-materia computing that performs multiply-accumulate in the physical device rather than in logic gates. Third, re-plumb memory, which is increasingly the binding constraint: SRAM is fast but low density, DRAM must hold both static weights and a growing KV cache and so suffers bandwidth contention, and Flash is dense but sits idle during inference. Proposals such as QMC split weights across multi-level ReRAM for inliers and on-chip MRAM for precision-critical outliers to work around this. In practice most deployment work is unglamorous runtime engineering against ONNX Runtime, ExecuTorch and TensorFlow Lite with XNNPACK.

The deciding parameters are not the ones used in datacentre AI. Edge silicon is procured against a fixed power and thermal envelope, with energy per unit of work as the figure of merit; cost per token is absent from procurement, per-unit BOM sits in the $15-45 range for standard parts, and RFQ cycles run 12-18 months. Thermal caps are hard physics: roughly a 48C skin-temperature standard with a 41-42C design target, which is why Meta's Ray-Ban Live AI is rated at about 30 minutes and thermally gated. Latency determinism is a second under-modelled parameter: on a Jetson Orin Nano, sweeping the memory clock across its realistic range shifts median latency by +11% to +48%, an estimator profiled under one power profile can underestimate latency by up to 32% under another, and deadline misses cluster rather than arrive independently, with a 74% chance the next cycle also misses at a 0.1% aggregate miss rate.

## Viability (4/5)

The evidence for working systems is direct rather than promissory. Sub-milliwatt keyword spotting is a commercial product class, with one vendor quoting 30 GOPS "in a microwatt envelope" and 140 microwatts for KWS, and another quoting under 1 millijoule per KWS inference in its IPO filing. A sparsity-focused edge accelerator startup had shipped more than 100,000 units as of December 2025, including into a retail OTC hearing aid, although the headline efficiency figures around 100x lower power are vendor claims <sup class="ref"><a href="https://femto.ai/about-us/" title="femtoAI (formerly Femtosense) — company profile, funding, leadership" rel="noopener">ref</a></sup>. General-purpose microcontrollers now quote 600 GOPS with 3 TOPS/W as the lead metric. Non-trivial classical workloads have also been moved down: hyperspectral-multispectral image fusion, previously too slow on a Raspberry Pi, achieved significant reductions in compute time after migration to ONNX Runtime and ExecuTorch with XNNPACK on a Pi 5.

Two things are not solved. Deadline-aware deployment remains fragile: latency models that ignore the memory clock mispredict badly, and miss events are strongly autocorrelated, so Gaussian mu+3sigma margins overshoot a 0.1% miss target by 13x to 29x while still being the wrong shape. And the generative tier is thermally gated rather than compute-gated, evidenced by a flagship smart-glasses live-AI feature rated at roughly 30 minutes. A useful reproducibility result cuts the other way: INT8 QDQ quantisation on ARM collapses output variation across microarchitectures and execution providers into a single bit-exact equivalence class, verified on MobileNetV2 and ResNet50V2 under TFLite with XNNPACK, whereas FP32 outputs disagreed on every CIFAR-10 image tested with a mean remaining precision of 14.97 of 23 mantissa bits. Quantisation is therefore not only an efficiency measure but a route to deterministic, certifiable edge behaviour.

**TLDR: The perception and small-model tier demonstrably works and ships; hard real-time guarantees and on-device generative workloads do not yet.**

## Drivers (4/5)

On the demand side, the strongest argument is economic rather than technical. NVIDIA Research's position is that agentic systems need narrow task competence rather than broad conversation, that small models run locally on consumer hardware enabling real-time offline inference without network dependency, and that 40-70% of current LLM queries could be served by specialised SLMs at 10-30x less unneeded capability **2025 06 Slm Future Agentic Ai Nvidia**. Energy is the second driver: on-device execution is framed as cutting inference energy by 95% versus cloud, and vendors argue TOPS alone is insufficient and perf/W is the real metric. Privacy is a third, with data access for training and inference identified as the contested frontier <sup class="ref"><a href="https://stateofthefuture.substack.com/p/confidential-ai-the-dog-that-didnt" title="Confidential AI" rel="noopener">ref</a></sup>. Whole product categories, notably hearing aids at 1-3 milliwatt steady-state budgets, simply cannot use the cloud.

On the supply side, capital has rotated back. In Q2 2026, 80 semiconductor startups raised over $6.0B, down from $8.4B in Q1, and the roundup explicitly records edge silicon re-emerging on physical-AI and real-time on-device demand alongside the datacentre wave <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>. There is a public-market datapoint too: an energy-efficiency-thesis edge silicon vendor IPO'd on 30 July 2025. The counterweight is procurement friction: 12-18 month RFQ cycles and a $15-45 per-unit BOM standard mean supply-side enthusiasm converts to revenue slowly and at low unit price.

**TLDR: Demand comes from privacy, offline operation, latency and the economics of over-provisioned models; supply from a re-energised edge silicon funding cycle.**

## Novelty (3/5)

The comparison that matters most is edge versus cloud, and there the claimed margin is wide: a 95% reduction in inference energy for on-device execution, plus removal of network dependency and the ability to run offline **2025 06 Slm Future Agentic Ai Nvidia**. Against alternative edge implementations the deltas are more modest and more contested. A sparsity-aware accelerator claims roughly 100x lower power, 10x smaller footprint and 10x faster integration than conventional edge inference, but these are company figures rather than independent measurements <sup class="ref"><a href="https://femto.ai/about-us/" title="femtoAI (formerly Femtosense) — company profile, funding, leadership" rel="noopener">ref</a></sup>. Microarchitectural engineering on commodity parts also yields large numbers cheaply: pipelining the readout stage of an FPGA SNN accelerator raised Fmax from 13.3 MHz to 167 MHz on an entry-level Artix-7.

**TLDR: Large gains against cloud inference on energy, latency and privacy; the genuinely novel physical substrates are still lab-stage.**

## Diffusion (3/5)

The barriers are documented and specific. Procurement is a per-unit BOM negotiation at $15-45 for standard parts with 12-18 month RFQ cycles, and cost per token, the metric the datacentre world optimises, is absent from edge buying decisions entirely. Power envelopes are fixed by form factor rather than negotiable: hundreds of milliwatts sustained with 1-2W peak for smart glasses, 3-8mW for a wake DSP, 1-3mW steady state for hearing aids, against batteries of 150-500mAh. Skin temperature limits of roughly 48C with a 41-42C design target cap sustained work irrespective of silicon efficiency, which is what produces a 30-minute rating on a shipping glasses product.

Software fragmentation is the second barrier and is being partly resolved. Achieving usable performance on a Raspberry Pi 5 required migrating the heaviest operations across PyTorch, ONNX Runtime and ExecuTorch with XNNPACK, which is skilled per-target work. Output non-determinism across execution providers is a real obstacle for any regulated deployment, and INT8 quantisation appears to remove it structurally on ARM, which materially lowers the qualification barrier. Against that, deadline-aware scheduling remains hard to get right, with clock-configuration changes alone producing up to 32% latency underestimation. The sources do not give market-share or unit-volume figures beyond one vendor's 100,000-plus shipped accelerators, so the score reflects demonstrated but narrow diffusion <sup class="ref"><a href="https://femto.ai/about-us/" title="femtoAI (formerly Femtosense) — company profile, funding, leadership" rel="noopener">ref</a></sup>.

**TLDR: Adoption is already real at the low-power tier but gated by thermal caps, long design-in cycles, thin BOM and fragmented toolchains.**

## Impact (4/5)

The qualification is on value capture, not on utility. Standard edge parts sell into a $15-45 BOM, and the sources contain no market sizing, no revenue figures and no attach-rate data for edge inference silicon. That is a volume business with thin per-unit economics, in contrast to the datacentre side where memory innovation such as High Bandwidth Flash, offering HBM4-class read bandwidth at roughly 10x the capacity, is being aimed at inference devices sampling in early 2027 <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>. High societal impact, uncertain concentration of profit.

**TLDR: If the SLM thesis holds, edge inference removes a large fraction of cloud inference load and enables device classes the cloud cannot serve; value capture per device is thin.**

## Timing Now (0-2yr)

Edge inference is not a future technology in its low-power form. Keyword spotting at 140 microwatts, hearing-aid accelerators with 100,000-plus units shipped by December 2025, and 600 GOPS microcontrollers quoting 3 TOPS/W are current products <sup class="ref"><a href="https://femto.ai/about-us/" title="femtoAI (formerly Femtosense) — company profile, funding, leadership" rel="noopener">ref</a></sup>. Applied deployment engineering on commodity boards is happening now in the literature.

The generative tier is later. The SLM demand thesis was published in June 2025 and rests on a 2025-26 model lineup including Phi-4, Llama 3.2 1B/3B, Ministral 3B/8B, Gemma 2 2B/9B and Qwen 2.5 0.5-3B, so the models exist; what does not exist is a thermal budget for sustained use in the smallest form factors, evidenced by a 30-minute rating on a shipping product **2025 06 Slm Future Agentic Ai Nvidia**. Memory co-design for on-device SLMs, analogue RF computing over MU-MIMO and in-materia KAN processors are all 2026 research papers with no deployment path stated in the sources, which places them beyond the five-year horizon on any conservative reading.

**TLDR: The perception and quantised-CNN tier is deployed today; sustained on-device generative inference is 2-5 years and the analogue substrates longer.**

## Overrated or underrated? Underrated

Two distinct stories are being scored as one, and the market gets both wrong. The sub-watt tier is underrated: it ships in volume, its figures of merit are measured in millijoules per inference rather than benchmark leaderboards, capital has rotated back into edge silicon on physical-AI and real-time on-device demand, and one recent result suggests INT8 quantisation delivers bit-exact cross-hardware determinism as a free side-effect, which is exactly what regulated deployment needs <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>. Meanwhile the demand-side argument that most agentic invocations are over-served by frontier models is now made by NVIDIA's own research group, not just by startups pitching against it **2025 06 Slm Future Agentic Ai Nvidia**.

The consumer-facing half is overrated in the short term. Nothing in these sources indicates a route past a 41-42C design target and a 150-500mAh battery, and the honest reading of a 30-minute thermally gated live-AI rating is that generative assistants in glasses remain a demonstration rather than a sustained capability. The investable insight is that the constraint is thermal and memory-bound, not compute-bound, which is why the interesting research is on memory hierarchies and analogue substrates rather than TOPS. Note that the strongest efficiency multipliers cited for specialised silicon are vendor-stated and unverified in these sources, so the case rests on shipped-unit evidence rather than headline ratios <sup class="ref"><a href="https://femto.ai/about-us/" title="femtoAI (formerly Femtosense) — company profile, funding, leadership" rel="noopener">ref</a></sup>.

## Prediction

By 31 December 2027, flagship AI smart glasses will still advertise continuous on-device live-AI runtime in tens of minutes rather than hours, with thermal gating rather than model size or silicon TOPS cited as the binding constraint.

## Evidence base

- June 2025: NVIDIA Research argues small language models are sufficient for most agentic invocations, estimates 40-70% of LLM queries could be handled by specialised SLMs, and notes paying 10-30x for unneeded capability is unsustainable at scale **2025 06 Slm Future Agentic Ai Nvidia**.
- 10 July 2026: edge silicon is bought against a fixed power/thermal envelope with energy per unit work as the metric and cost per token absent from procurement; per-unit BOM $15-45, 12-18 month RFQs; KWS at 140 microwatts; on-device claimed to cut inference energy 95% versus cloud; Ray-Ban Live AI rated ~30 minutes and thermally gated.
- 16 June 2026: on a Jetson Orin Nano, memory clock across 2133-3199 MHz shifts median latency +11% to +48%; a GPU-frequency estimator profiled under a different power profile underestimates latency by up to 32%; at a 0.1% aggregate deadline-miss rate the next cycle also misses with probability up to 74%.
- 28 July 2026: across four Raspberry Pi devices, FP32 outputs disagreed on every CIFAR-10 image when only the execution provider changed (mean remaining precision 14.97 of 23 mantissa bits), while INT8 QDQ quantisation collapsed all variation to a single bit-exact equivalence class, verified on MobileNetV2 and ResNet50V2.
- December 2025: an edge-AI accelerator vendor had shipped over 100,000 sparse processing units, including into a retail OTC hearing aid, with vendor-claimed ~100x lower power and ~10x smaller footprint versus conventional edge inference <sup class="ref"><a href="https://femto.ai/about-us/" title="femtoAI (formerly Femtosense) — company profile, funding, leadership" rel="noopener">ref</a></sup>.
- Q2 2026: 80 semiconductor startups raised over $6.0B (down from $8.4B in Q1 2026), with edge silicon explicitly re-emerging on physical-AI and real-time on-device demand <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>.

## Open questions

- Does the NVIDIA estimate that 40-70% of agentic LLM queries can be served by specialised small models survive independent replication on production agent traces, or is it an upper bound derived from narrow benchmarks?
- Can the ReRAM/MRAM hybrid memory approach in QMC be manufactured at edge BOM prices, or does it remain a simulation-and-calibrated-model result?
- Does the H1+H2 structural argument for INT8 dispatch-invariance hold on transformer and SLM graphs, not just CNNs, and would certification bodies accept it as a determinism guarantee?
- Is there any measured path to sustained multi-hour generative inference inside a 41-42C skin-temperature design target, or does the category stay burst-only regardless of silicon efficiency?

---
*Assessment drafted 2026-08-31 from up to 14 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
