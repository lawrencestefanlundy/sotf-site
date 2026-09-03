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
- '[[2026-07-03-thats-a-learning-curve-mate-not-rsi]]'
- '[[2026-08-07-the-memory-trade-isnt-over-weights]]'
- '[[2026-04-28-making-ai-inference-cheap-with-analog]]'
- '[[2026-07-16-the-path-to-agi-runs-through-hbm]]'
- '[[2026-07-10-hyperscaler-token-economics-sweep]]'
- '[[2026-07-07-high-bandwidth-flash-the-full-report]]'
- '[[2026-07-31-positron-research-sprint]]'
- '[[2026-06-28-frontier-llm-scaling-chinese-open-weight-models-are-nipping]]'
- '[[2026-05-29-silicon-shock-the-macro-of-tech-inflation]]'
scorecard:
  viability: 4
  drivers: 4
  novelty: 3
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 26
descendants:
- token-cost-stack
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-08-14-chip-tail-verification-sweep
  title: 'Chip-comparison tail verification sweep: 37 companies re-verified, consolidation wave confirmed'
  date: '2026-08-14'
  kind: web
- slug: 2026-08-07-the-memory-trade-isnt-over-weights
  title: 'The Memory Trade Isn''t Over: Weights and KV Cache'
  date: '2026-08-07'
  kind: substack
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
- slug: 2026-07-16-the-path-to-agi-runs-through-hbm
  title: The Path To AGI Runs Through HBM
  date: '2026-07-16'
  kind: substack
- slug: 2026-07-10-workload-phase-silicon-sweep
  title: 'Workload-phase silicon sweep: pre-training / RL / prefill / decode procurement split'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-10-inference-silicon-deep-research
  title: 'Deep research: measured vs claimed inference-silicon economics (adversarially verified, 23/25 claims confirmed)'
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
**Inference silicon is bought against two different customer KPIs depending on where it sits: cost per million tokens (spoken as tokens per watt per dollar under a power cap) in the datacentre, and energy per inference inside a fixed power and thermal envelope at the edge, and confusing the two is the most common analytical error in the sector.**

## Summary

"Inference economics" is shorthand for the fact that buyers of inference compute do not evaluate chips on peak throughput. They evaluate them on a delivered unit-economic figure, and there are two such figures, not one, split cleanly by segment.

In the datacentre the operative KPI is cost per million tokens. Nvidia has published the identity explicitly: $/Mtok = [$/GPU-hr ÷ (tok/s × 3600)] × 1M, under the headline "Cost per Token Is the Only Metric That Matters" (15 April 2026). Because the binding constraint is electrical rather than financial, the same KPI is usually spoken with power in the denominator: Satya Nadella's "tokens per watt per dollar" (January 2025), used on Microsoft's Q2 FY26 call on 28 January 2026 to claim Maia 200 is more than 30% better on tokens per dollar; Jensen Huang's "tokens per second per watt", and his GTC 2026 formulation on 16 March 2026 that Revenue = Tokens/Watt × Available GW. The levers inside the identity are therefore box cost per hour, achieved (not peak) tokens per second, and the power cap that decides how many boxes can be energised at all. Achieved throughput is dominated by memory: reasoning workloads with long output sequences have low arithmetic intensity and tight latency constraints, so utilisation collapses on compute-optimised GPUs, and challengers pitch straight at the KPI terms, as Positron does with claims of 5x tokens per dollar and 5x tokens per watt versus Nvidia Rubin on the back of over 90% memory-bandwidth utilisation against under 30% claimed for GPUs <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>.

At the edge the KPI is different in kind. Silicon is bought against a fixed power and thermal envelope, and the metric is energy per unit of work: cost per token is absent from procurement, which runs on per-unit BOM (typically $15-45) and 12-18 month RFQ cycles. The envelopes are hard physical facts rather than budget choices: smart glasses at hundreds of milliwatts sustained and 1-2W peak with 150-500mAh batteries and a skin-temperature cap around 48C; hearing aids at 1-3mW steady state; Meta's Ray-Ban Live AI rated at roughly 30 minutes and thermally gated. Vendors answer in energy or efficiency, not throughput: Syntiant quotes 140µW keyword spotting, ST leads the STM32N6 with 3 TOPS/W rather than its 600 GOPS, and Qualcomm argues publicly that TOPS is insufficient. Third-party energy anchors exist but are thin: Syntiant's MLPerf Tiny submissions measure 31.5-43.8 µJ per keyword-spotting inference and 71.7-97.2 µJ for visual wake, and are the only verified edge energy figures in the corpus.

The parameters that decide whether the framing is useful are: the gap between claimed and measured delivered economics; whether price and latency move together (they do not); and the rate at which the incumbent baseline improves, since any challenger's advantage must exceed it. Measured provider data for Llama 3.3 70B shows Groq fastest at 311 tok/s and $0.61 per million blended against mainstream GPU providers at 71-163 tok/s and $0.71-0.88, but a cheapest-GPU floor of $0.12-0.17 per million at FP8, putting Groq 3.5-5x above the price floor: the demonstrated advantage is speed, not cost. And the baseline moves fast: 8x B200 delivers 3.0x 8x H200 on MLPerf Llama-2-70B Server (about 2x iso-precision), software alone lifted H100 by up to 1.5x in a year, and the defensible floor for decline in GPU delivered cost per token is put at roughly 2.5-3x per year.

## Viability (4/5)

The limits are real. Vendor claims frequently do not survive verification: Cerebras had no measured 70B figure in the Artificial Analysis provider pages, so its delivered economics are unverified; Positron's 5x tokens-per-dollar and tokens-per-watt claims are company spec-sheet numbers for silicon that had not taped out at the time of reporting, with tape-out reported for October 2026 and production early 2027 <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>. MLPerf headline gains also mix numerics changes with silicon changes (FP4 versus FP8 inflating a 2x silicon step to 3.0x). So the KPI is sound; the integration level at which a number was obtained is what has to be stated, and usually is not.

**TLDR: Both KPIs are well defined, computable and in places third-party measured; the weakness is auditability of delivered figures, not the metrics themselves.**

## Drivers (4/5)

On the demand side, the constraint that forces the KPI is electricity, not capital. Huang described a "power-limited industry" whose "revenues are power limited" at GTC in March 2025, and Nadella said in November 2025 that he has "chips sitting in inventory that I can't plug in... not a compute glut, it's power". Margin pressure supplies the second push: Minack's 21 July 2026 note argues the evidence now says AI provision is a competitive, mediocre-return industry, partly because of cheap Chinese competition, and Chinese open-weight models are reported at coding parity with 5-30x lower cost per token <sup class="ref"><a href="https://quasa.io/media/chinese-open-weight-models-are-nipping-at-the-heels-of-western-sota" title="Chinese Open-Weight Models Are Nipping at the Heels of Western SOTA" rel="noopener">ref</a></sup>. When gross margin is the battleground, serving cost per token stops being an engineering statistic and becomes the P&L. Google reported Gemini serving unit costs down 78% over 2025 on the 4 February 2026 call, and at the application layer Cursor reached slight gross-margin profitability in April 2026 partly through cheaper model routing <sup class="ref"><a href="https://valueaddvc.com/blog/what-series-a-investors-are-looking-for-in-ai-startups-in-2026" title="AI-native application retention and gross margin benchmarks, mid-2026" rel="noopener">ref</a></sup>.

On the supply side, the workload has moved against general-purpose GPUs: reasoning models produce long output sequences at low arithmetic intensity under tight latency, so system utilisation drops and the memory wall binds. That is why decode is being pushed onto different hardware (Splitwise noted decode "can run on lower-cost and lower-power hardware"; DistServe measured up to 7.4x more requests from prefill/decode disaggregation) and why the roadmap now contains phase-specific parts, including the Nvidia-Groq licensing deal of around $20B on 24 December 2025 leading to an SRAM decode co-processor targeted at Q3 2026. Memory cost is the counter-driver: a 73% annualised spike in the software and accessories price index in late 2025, attributed in part to flash-memory prices, shows the input side of the KPI can move against buyers <sup class="ref"><a href="https://www.geninnov.ai/blog/silicon-shock-the-macro-of-tech-inflation" title="Silicon Shock: The Macro of Tech Inflation" rel="noopener">ref</a></sup>.

**TLDR: Demand side: power-capped datacentres and competitive compression of AI service margins. Supply side: memory-bound decode workloads that peak-FLOPS silicon serves badly.**

## Novelty (3/5)

What the two KPIs are better than is datasheet throughput. Nvidia itself now asserts cost per token is the only metric that matters, and on the edge side Qualcomm argues publicly that TOPS is insufficient while ST leads the STM32N6 with 3 TOPS/W ahead of its 600 GOPS. The improvement is not marginal: peak-throughput specs cannot see the utilisation collapse that decode imposes (over 90% memory-bandwidth utilisation versus under 30% claimed for GPUs is the entire Positron pitch) <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>, nor the numerics inflation in headline speedups.

The reason this is not scored higher is that the metrics themselves are old and widely adopted. Energy per inference under a fixed envelope has been how embedded silicon is bought for years, and Ambiq listed in July 2025 on precisely that thesis. Tokens per watt per dollar entered CEO vocabulary in January 2025. The genuinely underused part is the discipline around it: separating price from latency (Groq's measured edge is 2-4.4x speed while sitting 3.5-5x above the price floor, and one GPU provider at 295 tok/s for $0.20 questions how durable even that is), and labelling the integration level of every quoted figure.

**TLDR: Better than TOPS and peak FLOPS as a procurement metric, and by a wide margin; but as a framing it is now industry consensus rather than a new insight.**

## Diffusion (4/5)

Adoption of the framing is close to complete in its respective segments. The datacentre KPI appears in Microsoft, Nvidia and Alphabet public disclosure (Maia 200 claimed more than 30% better tokens per dollar, 28 January 2026; Revenue = Tokens/Watt × Available GW, 16 March 2026; Gemini serving unit costs down 78%, 4 February 2026) and in a vendor pricing frame of $1/M to $150/M token tiers. Challenger silicon markets itself in the same units <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>. Edge datasheets and RFQs run on envelopes and energy per inference.

The barriers are downstream of acceptance. First, measurement: outside Artificial Analysis's provider panel and MLPerf there is no audited source for delivered cost per token, and multiple vendor claims failed verification. Second, the two KPIs resist unification: cost per token is absent from edge procurement, which is BOM-and-envelope driven on 12-18 month RFQ cycles, with tokens entering the edge as a speed metric (tok/s, TTFT) and tokens/sec/W only emerging at the on-device-LLM tier. Third, the KPI is fragmenting by workload phase: prefill and decode pools are already the production default and phase-specific silicon is on committed roadmaps but not yet volume procurement, with Rubin CPX cancelled in March 2026 as one casualty of that transition. A single blended number per chip is becoming less meaningful, not more.

**TLDR: Already the operative language of hyperscaler earnings calls, vendor spec sheets and edge datasheets; the barrier is measurement standardisation, not acceptance.**

## Impact (4/5)

The KPI's power comes from the baseline drift it implies. If GPU delivered cost per token falls at roughly 2.5-3x per year on infrastructure alone (with Epoch putting fixed-capability price declines at a median 50x per year), then a challenger with a claimed 5x advantage against an unshipped Nvidia part <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup> has roughly a year of headroom, and any advantage that is not compounding is not an advantage. That arithmetic is visible in outcomes: the chip tail consolidated hard in one month of mid-2026, with Hailo sold to Microchip at a fraction of its $1.2B peak, Taalas to AMD, Esperanto wound down and Blaize on distress watch.

The same metric propagates up the stack into equity returns. Minack's case that AI provision is a competitive, mediocre-return industry rests on contestability, which is exactly what a falling cost per token enforces. At the application layer the split between 50-60% gross margins for thin frontier-model wrappers and 70%-plus for owners of their own models is a direct read-through from serving cost <sup class="ref"><a href="https://valueaddvc.com/blog/what-series-a-investors-are-looking-for-in-ai-startups-in-2026" title="AI-native application retention and gross margin benchmarks, mid-2026" rel="noopener">ref</a></sup>. And the memory roadmap is being redirected by it: High Bandwidth Flash offers HBM4-class read bandwidth at roughly 10x capacity in cheap NAND, with memory samples expected in the second half of 2026 and inference devices in early 2027, aimed squarely at decode economics <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.

**TLDR: It is the metric that allocates tens of billions of procurement and sets the survival bar for every non-Nvidia inference chip.**

## Timing Now (0-2yr)

This is not a forward-dated technology. The datacentre KPI was in earnings-call language by January 2026 and in Nvidia's own marketing by April 2026; the edge KPI has been procurement practice for longer. What lands in the next 0-2 years is the resolution of the specific bets priced against the KPI: HBF memory samples in the second half of 2026 and inference devices in early 2027 <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>, the Groq-derived SRAM decode co-processor targeted at Q3 2026, and Positron's Asimov at production in early 2027 <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>.

The corollary is that anyone using the KPI needs to re-baseline continuously. With a defensible 2.5-3x annual decline in delivered GPU cost per token, comparisons more than a couple of quarters old are not comparisons.

**TLDR: Both KPIs are already the operative purchase criteria; the open question is measurement rigour, not arrival.**

## Overrated or underrated? Fairly rated

The two-KPI framing is correct and correctly prominent. Cost per million tokens under a power cap really is how datacentre buyers decide, and energy per inference under a fixed envelope really is how edge buyers decide; the sources show both in the buyers' own words, not just analysts'. Nothing here is speculative.

Where the market is loose is in how the KPI is used. Three disciplines are routinely skipped. First, price and latency are different products: the only measured challenger advantage in the corpus is speed (2-4.4x), while price sits 3.5-5x above the cheapest GPU floor, so "cheaper tokens" and "faster tokens" should never be conflated. Second, integration level: spec-sheet tokens per watt from an untaped-out chip and a 72-hour measured P50 from a live provider are not the same class of evidence, and adversarial checking has already killed vendor claims <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>. Third, the single number is decomposing into per-phase numbers as prefill and decode separate. Use the KPI, but insist on the qualifiers, and assume the incumbent baseline improves 2.5-3x while you deliberate.

## Prediction

By 31 December 2027 no third-party measured source (Artificial Analysis provider panel or MLPerf Inference) will show a non-Nvidia inference part delivering both the lowest cost per million tokens and the highest tokens per second on a common frontier-scale model, leaving speed and price advantages held by different vendors.

## Evidence base

- 15 April 2026: Nvidia publishes "Cost per Token Is the Only Metric That Matters" with the identity $/Mtok = [$/GPU-hr ÷ (tok/s × 3600)] × 1M; Huang's GTC 2026 keynote on 16 March 2026 frames Revenue = Tokens/Watt × Available GW with token tiers of $1/M to $150/M.
- 28 January 2026: Microsoft's Q2 FY26 call uses tokens per dollar per watt and claims Maia 200 is over 30% better on tokens per dollar; Alphabet's 4 February 2026 call reports Gemini serving unit costs down 78% over 2025.
- 10 July 2026: measured Llama 3.3 70B provider data shows Groq fastest at 311 tok/s and $0.61/M blended versus mainstream GPU at 71-163 tok/s and $0.71-0.88/M, with a cheapest-GPU FP8 floor of $0.12-0.17/M; the advantage is speed (2-4.4x), not price. Defensible GPU delivered $/token decline floor: 2.5-3x per year.
- 10 July 2026: edge silicon is bought against a fixed power/thermal envelope with cost per token absent from procurement (per-unit BOM $15-45, 12-18 month RFQs); anchors include 1-3mW hearing-aid budgets, Syntiant's 140µW keyword spotting and ST leading the STM32N6 with 3 TOPS/W.
- 31 July 2026: Positron markets Asimov on 5x tokens per dollar and 5x tokens per watt versus Nvidia Rubin, based on over 90% memory-bandwidth utilisation against under 30% claimed for GPUs, with LPDDR5x instead of HBM; tape-out reported October 2026, production early 2027 <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>.
- 21 July 2026: Minack argues the contestability case has firmed up and that AI provision is a competitive, mediocre-return industry, partly due to cheap Chinese competition; Chinese open-weight models are reported at coding parity with 5-30x lower cost per token (28 June 2026) <sup class="ref"><a href="https://quasa.io/media/chinese-open-weight-models-are-nipping-at-the-heels-of-western-sota" title="Chinese Open-Weight Models Are Nipping at the Heels of Western SOTA" rel="noopener">ref</a></sup>.

## Open questions

- Does the speed premium survive? One GPU provider already hit 295 tok/s at $0.20 per million against Groq's 311 tok/s at $0.61; if FP8 GPU serving closes the latency gap, the speed-versus-price split collapses into a single price KPI.
- Will an audited benchmark for delivered cost per token emerge beyond Artificial Analysis's 72-hour P50 panel, so that vendor tokens-per-dollar claims such as Maia 200's 30% or Positron's 5x can be independently checked?
- Does the datacentre KPI split permanently into per-phase figures (prefill $/Mtok and decode $/Mtok) as disaggregation and phase-specific silicon reach volume procurement, and does that change which chip wins?
- Does tokens/sec/W become an actual line item in edge RFQs at the on-device-LLM tier, or does edge procurement stay on BOM plus envelope plus energy per inference indefinitely?

---
*Assessment drafted 2026-08-31 from up to 16 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
