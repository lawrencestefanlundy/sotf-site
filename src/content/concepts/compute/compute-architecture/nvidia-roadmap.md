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
scorecard:
  viability: 4
  drivers: 4
  novelty: 3
  diffusion: 4
  impact: 5
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 38
sources_7d: 0
sources_30d: 4
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
**NVIDIA's datacentre roadmap runs from the Vera Rubin platform shipping in H2 2026 to Feynman in 2028, and the July 2026 slip of the Kyber NVL144 rack to 2028 is the first hard evidence that the annual-cadence promise is bounded by packaging and rack engineering rather than by silicon design.**

## Summary

NVIDIA no longer sells chips on a roadmap; it sells rack-scale platforms on a roadmap. The Vera Rubin platform, launched at GTC 2026 on 16 March, was presented as six new chips forming one AI supercomputer: a Rubin GPU generation paired with the Vera CPU, Spectrum-X networking, and an adjacent LPX rack built around a licensed Groq 3 LPU, fully liquid-cooled, shipping in the second half of 2026 with the first rack live at Microsoft Azure and no CUDA code changes required <sup class="ref"><a href="https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/" title="Inside the NVIDIA Rubin Platform: Six New Chips, One AI Supercomputer" rel="noopener">ref</a></sup>. Rubin uses HBM4, and Feynman was confirmed on the public roadmap for 2028 as far back as GTC 2025, though no TDP figures have been disclosed for either <sup class="ref"><a href="https://intuitionlabs.ai/articles/nvidia-data-center-gpu-specs" title="NVIDIA Vera Rubin and Feynman roadmap confirmed at GTC 2025 with HBM4 support" rel="noopener">ref</a></sup>.

The roadmap has already been rewritten twice in a year, in both directions. Rubin CPX, announced September 2025 as a prefill-only GPU with 30 PF of NVFP4 and 128 GB of GDDR7 and no HBM, was cancelled in March 2026 and replaced by the ~$20B Groq licensing deal signed 24 December 2025, which produced the Groq 3 LPX SRAM decode co-processor on Samsung 4nm targeted at Q3 2026 <sup class="ref"><a href="https://www.tomshardware.com/tech-industry/semiconductors/nvidias-20-billion-groq-deal-produces-its-first-chip" title="How Nvidia's $20 billion Groq 3 LPU deal reshapes the Nvidia Vera Rubin Platform" rel="noopener">ref</a></sup>. In the other direction, SemiAnalysis reported on 5 July 2026 that the Kyber NVL144 rack had slipped more than twelve months to 2028, three months after Jensen Huang demoed it, because the multi-layer PCB midplane connecting compute modules "remains challenging from a manufacturability standpoint"; the NVL72x2 back-to-back double-rack stopgap was cancelled after pushback from cloud service providers over its operational burden <sup class="ref"><a href="https://x.com/SemiAnalysis_/status/2073874671498387899" title="SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled" rel="noopener">ref</a></sup>.

The parameters that decide this roadmap are mostly not logic design. They are: CoWoS advanced packaging supply, where NVIDIA booked roughly 55% of 2026 capacity against lead times of 50 to 104 weeks and where packaging rather than the die is widely argued to be the gating constraint; HBM4 ramp, where NVIDIA has deliberately split allocation to roughly mid-50% SK Hynix, mid-20% Samsung and ~20% Micron, down from about two-thirds SK Hynix in January 2026, and where analysts flagged in July 2026 that HBM4 shipments expected to scale from Q2 "do not appear to have materialised at scale" <sup class="ref"><a href="https://finance.yahoo.com/markets/stocks/articles/sk-hynix-shares-fall-much-003035107.html" title="SK Hynix record one-day fall as HBM4 goes three-supplier" rel="noopener">ref</a></sup>; rack power and thermals, with Rubin Ultra NVL576 racks projected to exceed 600 kW by 2027 and direct-to-chip liquid cooling already mandatory from GB200 NVL72 onward <sup class="ref"><a href="https://www.datacenterdynamics.com/en/opinions/unlocking-the-potential-of-direct-to-chip-liquid-cooling/" title="Direct-to-chip liquid cooling moving from niche to mainstream production" rel="noopener">ref</a></sup>; and the manufacturability of the rack itself, which is what killed Kyber's schedule.

Demand-side, the roadmap is the reference architecture for the largest committed capital programme in the industry: Vera Rubin is rolling out across the Stargate sites in H2 2026 **2026 Openai Titan Custom Chip**, a build with five new sites, roughly $400B committed over three years and ~7 GW planned on the path to a headline 10 GW and ~$500B **2026 Stargate Expansion 7Gw**.

## Viability (4/5)

The near-term leg is demonstrated rather than promised. The Vera Rubin platform was formally launched on 16 March 2026, ships H2 2026, is fully liquid-cooled, and the first LPX rack is live at Microsoft Azure with no CUDA code changes required <sup class="ref"><a href="https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/" title="Inside the NVIDIA Rubin Platform: Six New Chips, One AI Supercomputer" rel="noopener">ref</a></sup>. Deployment against a named customer programme is also dated: Vera Rubin rolls out across Stargate sites in H2 2026 **2026 Openai Titan Custom Chip**. That is a high bar of evidence for a compute-architecture page.

The out-years are where the score is capped. Kyber NVL144 slipped more than twelve months to 2028 for PCB midplane manufacturability reasons, and the NVL72x2 fallback was cancelled, leaving NVIDIA with no proven path to expand the scale-up world size for Rubin Ultra, which stays at an NVL72-class domain far longer than roadmapped <sup class="ref"><a href="https://x.com/SemiAnalysis_/status/2073874671498387899" title="SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled" rel="noopener">ref</a></sup>. Rubin CPX was announced then cancelled inside six months. Feynman is on the roadmap for 2028 with no disclosed TDP or configuration <sup class="ref"><a href="https://intuitionlabs.ai/articles/nvidia-data-center-gpu-specs" title="NVIDIA Vera Rubin and Feynman roadmap confirmed at GTC 2025 with HBM4 support" rel="noopener">ref</a></sup>, and the sources give no independent basis for treating that date as firm. Component supply adds a second constraint: HBM4 volumes had not materialised at scale as of July 2026 <sup class="ref"><a href="https://finance.yahoo.com/markets/stocks/articles/sk-hynix-shares-fall-much-003035107.html" title="SK Hynix record one-day fall as HBM4 goes three-supplier" rel="noopener">ref</a></sup>.

**TLDR: Rubin is a shipped, racked, customer-live product; everything past it is a schedule that has already slipped once.**

## Drivers (4/5)

Demand: the Stargate programme alone accounts for five new sites, ~$400B committed over three years and ~7 GW planned toward a 10 GW / ~$500B headline, with Vera Rubin as the deployed architecture **2026 Stargate Expansion 7Gw** **2026 Openai Titan Custom Chip**. AI's share of TSMC's leading node is reported at 60% of N3 in 2026 rising to 90% in 2027, which is the clearest available signal that this roadmap is absorbing the frontier of foundry capacity rather than competing for a slice of it **2026 Openai Titan Custom Chip**. HBM demand growth of ~+70-77% in 2026 and +68% in 2027, with SK Hynix's 2026 capacity booked out as of October 2025, corroborates from the memory side.

Supply: this is the constrained side. NVIDIA booked roughly 55% of 2026 CoWoS capacity with 50-104 week lead times, and packaging rather than the logic die is widely argued to be the gating constraint. NVIDIA has responded by deliberately widening HBM4 to three suppliers, cutting SK Hynix from about two-thirds to mid-50% and lifting Samsung and Micron, which reduces single-vendor risk but introduces qualification variance across a TSMC-fabbed versus Samsung SF4-fabbed logic base die <sup class="ref"><a href="https://finance.yahoo.com/markets/stocks/articles/sk-hynix-shares-fall-much-003035107.html" title="SK Hynix record one-day fall as HBM4 goes three-supplier" rel="noopener">ref</a></sup>. Power and cooling are a further gate: Rubin Ultra NVL576 racks are projected above 600 kW by 2027 <sup class="ref"><a href="https://www.datacenterdynamics.com/en/opinions/unlocking-the-potential-of-direct-to-chip-liquid-cooling/" title="Direct-to-chip liquid cooling moving from niche to mainstream production" rel="noopener">ref</a></sup>, and one analyst report frames the wider $600B+/yr AI infrastructure build as colliding with a grid that cannot deliver.

**TLDR: Demand is committed at hundreds of billions; supply of packaging and HBM4 is the thing throttling delivery.**

## Novelty (3/5)

The sources contain no per-generation performance comparison for Rubin against Blackwell, so any claim of a quantified uplift would be invented. What the sources do support is an architectural change of kind: NVIDIA moved from selling a GPU generation to selling a six-chip rack platform, and it responded to the prefill/decode specialisation threat by licensing a competitor's decode engine rather than building its own. Rubin CPX, its in-house prefill-only part with 30 PF NVFP4 and GDDR7 instead of HBM, was cancelled in March 2026 and replaced by the ~$20B Groq deal signed 24 December 2025, yielding the Groq 3 LPX SRAM decode co-processor on Samsung 4nm <sup class="ref"><a href="https://www.tomshardware.com/tech-industry/semiconductors/nvidias-20-billion-groq-deal-produces-its-first-chip" title="How Nvidia's $20 billion Groq 3 LPU deal reshapes the Nvidia Vera Rubin Platform" rel="noopener">ref</a></sup>. The LPX rack sits alongside Vera Rubin over Spectrum-X and runs with no CUDA code changes <sup class="ref"><a href="https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/" title="Inside the NVIDIA Rubin Platform: Six New Chips, One AI Supercomputer" rel="noopener">ref</a></sup>.

What it is better than: the alternative disaggregated approach, exemplified by the AWS-Cerebras collaboration announced March 2026 pairing Trainium 3 for prefill with Cerebras CS-3 for decode on Bedrock in H2 2026 <sup class="ref"><a href="https://futurumgroup.com/insights/aws-rises-to-the-agentic-ai-moment-with-cerebras-integration-for-fast-inference/" title="AWS Rises to the Agentic AI Moment with Cerebras Integration for Fast Inference" rel="noopener">ref</a></sup>, and by Google's TPU line, where TPU v9 "Triggerfish" is reported to carry roughly three times the baseline memory using MediaTek 336G SerDes <sup class="ref"><a href="https://www.semidoped.com/p/daily-update-june-23rd-2026" title="Semi Doped — Daily Update, June 23rd 2026" rel="noopener">ref</a></sup>. NVIDIA's differentiator is not raw specialisation but that the specialised part arrives inside a CUDA-compatible rack with no software migration. Against that, the Kyber slip means the one dimension where NVIDIA's rack architecture was supposed to pull decisively ahead, scale-up world size, is where it now stands still, which SemiAnalysis explicitly calls a rare technical opening for AMD and Google <sup class="ref"><a href="https://x.com/SemiAnalysis_/status/2073874671498387899" title="SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled" rel="noopener">ref</a></sup>.

**TLDR: The genuine novelty is absorbing specialised silicon into the incumbent rack, not a quantified generational leap the sources can evidence.**

## Diffusion (4/5)

The barriers are physical and procurement-side. Direct-to-chip liquid cooling is already required from GB200 NVL72 and Rubin Ultra NVL576 may exceed 600 kW per rack by 2027, which constrains diffusion to sites designed for it <sup class="ref"><a href="https://www.datacenterdynamics.com/en/opinions/unlocking-the-potential-of-direct-to-chip-liquid-cooling/" title="Direct-to-chip liquid cooling moving from niche to mainstream production" rel="noopener">ref</a></sup>. CoWoS lead times of 50-104 weeks mean rack availability is set by bookings made up to two years earlier. And customer preference is now a live veto: NVL72x2 was cancelled specifically because of heavy pushback from CSPs and hyperscalers over its odd design and operational burden <sup class="ref"><a href="https://x.com/SemiAnalysis_/status/2073874671498387899" title="SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled" rel="noopener">ref</a></sup>, which shows buyers of this scale will refuse a roadmap step they do not want to operate.

**TLDR: CUDA continuity and pre-committed hyperscaler capex remove the usual adoption friction; the barriers are physical, not commercial.**

## Impact (5/5)

The roadmap is the denominator for the sector. It is the deployed architecture for a ~$400B, ~7 GW programme heading to 10 GW **2026 Stargate Expansion 7Gw** **2026 Openai Titan Custom Chip**, it consumes roughly 55% of 2026 CoWoS capacity, and NVIDIA's allocation decisions set the revenue split across the three HBM suppliers, with a single reallocation from two-thirds to mid-50% SK Hynix contributing to a 15.4% one-day fall in SK Hynix on 13 July 2026, the biggest in about two decades <sup class="ref"><a href="https://finance.yahoo.com/markets/stocks/articles/sk-hynix-shares-fall-much-003035107.html" title="SK Hynix record one-day fall as HBM4 goes three-supplier" rel="noopener">ref</a></sup>. Few technologies on this knowledge base have that direct a transmission channel into public markets and foundry allocation.

The slip case shows the same leverage in reverse. Because Rubin Ultra now has no proven path to a larger scale-up domain, one packaging problem on a PCB midplane translates directly into a competitive opening for AMD and Google TPU at the high end <sup class="ref"><a href="https://x.com/SemiAnalysis_/status/2073874671498387899" title="SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled" rel="noopener">ref</a></sup>. Second-order impact runs through customer strategy too: OpenAI's own Titan chip enters mass production on TSMC N3 with Broadcom in H2 2026, in parallel with Vera Rubin deployment on the same sites **2026 Openai Titan Custom Chip**, so the largest buyers are hedging even while adopting.

**TLDR: This roadmap sets the unit economics and the schedule of the entire frontier AI build-out.**

## Timing Now (0-2yr)

The current leg is live. Vera Rubin launched 16 March 2026, ships H2 2026, with the first LPX rack already running at Azure and rollout across Stargate in the same window <sup class="ref"><a href="https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/" title="Inside the NVIDIA Rubin Platform: Six New Chips, One AI Supercomputer" rel="noopener">ref</a></sup> **2026 Openai Titan Custom Chip**. The Groq 3 LPX decode co-processor targets Q3 2026. So there is nothing speculative about the 0-2 year band.

The interesting timing question is 2028, where two roadmap items now converge: Feynman, confirmed for 2028 with no disclosed specifications <sup class="ref"><a href="https://intuitionlabs.ai/articles/nvidia-data-center-gpu-specs" title="NVIDIA Vera Rubin and Feynman roadmap confirmed at GTC 2025 with HBM4 support" rel="noopener">ref</a></sup>, and Kyber NVL144, pushed to 2028 by the midplane slip <sup class="ref"><a href="https://x.com/SemiAnalysis_/status/2073874671498387899" title="SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled" rel="noopener">ref</a></sup>. A generation and a rack architecture arriving in the same year, after one of them has already lost twelve months to manufacturability, is a compression risk the sources do not resolve. Also unresolved in the sources: whether HBM4E at 3+ TB/s, timed for 2027, arrives in step with the parts meant to use it.

**TLDR: Rubin ships and is racked in H2 2026; the contested part of the roadmap lands in 2028.**

## Overrated or underrated? Fairly rated

The product is real and the demand behind it is committed capital, not sentiment. Treating Vera Rubin as anything other than the default frontier training and inference architecture for 2026-27 would be wrong: it is launched, racked, liquid-cooled, live at Azure, deploying across Stargate, and it absorbs the phase-specialisation threat via the Groq licence without asking anyone to leave CUDA <sup class="ref"><a href="https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/" title="Inside the NVIDIA Rubin Platform: Six New Chips, One AI Supercomputer" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.tomshardware.com/tech-industry/semiconductors/nvidias-20-billion-groq-deal-produces-its-first-chip" title="How Nvidia's $20 billion Groq 3 LPU deal reshapes the Nvidia Vera Rubin Platform" rel="noopener">ref</a></sup>.

Where the market rating deserves a discount is the metronome narrative. In roughly nine months NVIDIA cancelled an announced prefill GPU, cancelled a rack stopgap after customer pushback, and lost more than a year on its next-generation rack to a PCB manufacturability problem <sup class="ref"><a href="https://x.com/SemiAnalysis_/status/2073874671498387899" title="SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled" rel="noopener">ref</a></sup>. The binding constraints have moved off the die and onto packaging, midplanes, HBM4 qualification and 600 kW-class thermals <sup class="ref"><a href="https://www.datacenterdynamics.com/en/opinions/unlocking-the-potential-of-direct-to-chip-liquid-cooling/" title="Direct-to-chip liquid cooling moving from niche to mainstream production" rel="noopener">ref</a></sup>. Roadmap dates beyond 2027, Feynman included, should be read as intentions with a demonstrated slip rate, not commitments. Net: correctly rated on the shipping generation, over-rated on cadence beyond it.

## Prediction

By 31 December 2027, NVIDIA will not have shipped in volume a rack-scale system with a scale-up domain larger than NVL72-class, leaving Rubin Ultra's world size unexpanded relative to the 2026 roadmap.

## Evidence base

- GTC 2026, 16 March 2026: Vera Rubin platform launched as six chips forming one system, LPX rack with Groq 3 LPU over Spectrum-X, fully liquid-cooled, ships H2 2026, first rack live at Microsoft Azure, no CUDA code changes <sup class="ref"><a href="https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/" title="Inside the NVIDIA Rubin Platform: Six New Chips, One AI Supercomputer" rel="noopener">ref</a></sup>
- 5 July 2026: Kyber NVL144 delayed more than 12 months to 2028 on PCB midplane manufacturability; NVL72x2 cancelled after CSP pushback; no proven path to expand Rubin Ultra's scale-up domain, framed as an opening for AMD and Google TPU <sup class="ref"><a href="https://x.com/SemiAnalysis_/status/2073874671498387899" title="SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled" rel="noopener">ref</a></sup>
- Rubin CPX announced September 2025 as a prefill-only GPU (30 PF NVFP4, 128 GB GDDR7, no HBM) and cancelled March 2026, replaced by the ~$20B Nvidia-Groq licence of 24 December 2025 producing the Groq 3 LPX SRAM decode co-processor on Samsung 4nm, Q3 2026 target 
- Vera Rubin (H2 2026) and Feynman (2028) confirmed on the NVIDIA roadmap with HBM4 support, but no TDP specifications disclosed as of March 2026 <sup class="ref"><a href="https://intuitionlabs.ai/articles/nvidia-data-center-gpu-specs" title="NVIDIA Vera Rubin and Feynman roadmap confirmed at GTC 2025 with HBM4 support" rel="noopener">ref</a></sup>
- 13 July 2026: NVIDIA HBM4 allocation reported at ~mid-50% SK Hynix / mid-20% Samsung / ~20% Micron, down from about two-thirds SK Hynix in January 2026; SK Hynix fell 15.4% in Seoul, its biggest one-day drop in ~two decades, with analysts noting HBM4 shipments had not scaled <sup class="ref"><a href="https://finance.yahoo.com/markets/stocks/articles/sk-hynix-shares-fall-much-003035107.html" title="SK Hynix record one-day fall as HBM4 goes three-supplier" rel="noopener">ref</a></sup>
- Mid-2026: NVIDIA booked ~55% of 2026 TSMC CoWoS capacity against 50-104 week lead times, with packaging rather than the die argued to be the gating constraint 
- Rubin Ultra NVL576 racks may exceed 600 kW per rack by 2027, following NVIDIA's assertion that direct-to-chip liquid cooling is required from GB200 NVL72 <sup class="ref"><a href="https://www.datacenterdynamics.com/en/opinions/unlocking-the-potential-of-direct-to-chip-liquid-cooling/" title="Direct-to-chip liquid cooling moving from niche to mainstream production" rel="noopener">ref</a></sup>
- Vera Rubin rolling out across Stargate sites in H2 2026, a programme with five new sites, ~$400B committed over three years and ~7 GW planned toward 10 GW / ~$500B; AI reported at 60% of TSMC N3 in 2026 and 90% in 2027 **2026 Openai Titan Custom Chip** **2026 Stargate Expansion 7Gw**

## Open questions

- Is the Kyber PCB midplane a solvable manufacturability problem on a known schedule, or does it force a redesign of the rack interconnect that also affects Feynman?
- Does Feynman hold its 2028 date now that Kyber has been pushed into the same year, and what is its rated TDP given nothing has been disclosed?
- Does the three-way HBM4 split reach volume, given that shipments expected to scale from Q2 2026 had not materialised at scale by July 2026, and does Samsung's in-house SF4 logic base die qualify on NVIDIA parts?
- What is the actual attach rate of the Groq 3 LPX decode rack beyond the first Azure deployment, versus customers choosing disaggregated alternatives such as the AWS-Cerebras Trainium 3 / CS-3 pairing?

---
*Assessment drafted 2026-08-31 from up to 15 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
