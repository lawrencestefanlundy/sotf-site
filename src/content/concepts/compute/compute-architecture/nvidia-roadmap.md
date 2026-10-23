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
- '[[2026-05-14-compute-is-defence-now]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2026-07-10-the-next-vc-meme-is]]'
- '[[2026-06-23-semidoped-daily-update]]'
- '[[2026-06-01-hbm-state-of-play]]'
- '[[2026-03-17-compute-specialisation-equilibrium-aws-rises-to-the-agentic]]'
- '[[2026-03-11-ai-power-thermal-binding-direct-to-chip-liquid-cooling]]'
- '[[2026-07-10-workload-phase-silicon-sweep]]'
- '[[2026-07-05-semianalysis-kyber-nvl144-delayed-2028]]'
- '[[2026-04-15-jensen-huang-tpu-competition-why-we-should-sell-chips-to-chi]]'
- '[[2026-03-16-nvidia-vera-rubin-platform]]'
- '[[2026-06-30-compute-specialisation-equilibrium-deepseek-s-dspark-just]]'
- '[[2026-03-03-ai-power-thermal-binding-nvidia-vera-rubin-and-feynman]]'
- '[[2026-openai-titan-custom-chip]]'
- '[[2026-07-13-sk-hynix-record-fall-hbm4-three-supplier]]'
- '[[2026-03-19-compute-specialisation-equilibrium-how-nvidia-s-20-billion]]'
- '[[2026-stargate-expansion-7gw]]'
- '[[2026-06-08-how-coreweave-sees-the-market-for-compute-right-now]]'
scorecard:
  viability: 4
  drivers: 4
  novelty: 3
  diffusion: 4
  impact: 5
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 51
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
- slug: 2026-07-10-the-next-vc-meme-is
  title: The Next VC Meme Is...
  date: '2026-07-10'
  kind: substack
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
- slug: 2026-06-08-how-coreweave-sees-the-market-for-compute-right-now
  title: How CoreWeave Sees the Market for Compute Right Now
  date: '2026-06-08'
  kind: web
- slug: 2026-06-01-hbm-state-of-play
  title: HBM state of play (mid-2026) — technology, supercycle, three-supplier standing
  date: '2026-06-01'
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
## Summary

## Viability (4/5)

The near-term part is demonstrated rather than promised. The Vera Rubin platform was formally launched on 16 March 2026, ships H2 2026, is fully liquid-cooled, and the first LPX rack is live at Microsoft Azure with no CUDA code changes required <sup class="ref"><a href="https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/" title="Inside the NVIDIA Rubin Platform: Six New Chips, One AI Supercomputer" rel="noopener">ref</a></sup>. Deployment against a named customer programme is also dated: Vera Rubin rolls out across Stargate sites in H2 2026 **2026 Openai Titan Custom Chip**. That is a high bar of evidence for a compute-architecture page.

**TLDR: Rubin is a shipped, racked, customer-live product; everything past it is a schedule that has already slipped once.**

## Drivers (4/5)

Supply: this is the constrained side. NVIDIA booked roughly 55% of 2026 CoWoS capacity with 50-104 week lead times, and packaging rather than the logic die is widely argued to be the gating constraint. NVIDIA has responded by deliberately widening HBM4 to three suppliers, cutting SK Hynix from about two-thirds to mid-50% and lifting Samsung and Micron, which reduces single-vendor risk but introduces qualification variance across a TSMC-fabbed versus Samsung SF4-fabbed logic base die <sup class="ref"><a href="https://finance.yahoo.com/markets/stocks/articles/sk-hynix-shares-fall-much-003035107.html" title="SK Hynix record one-day fall as HBM4 goes three-supplier" rel="noopener">ref</a></sup>. Power and cooling are a further gate: Rubin Ultra NVL576 racks are projected above 600 kW by 2027 <sup class="ref"><a href="https://www.datacenterdynamics.com/en/opinions/unlocking-the-potential-of-direct-to-chip-liquid-cooling/" title="Direct-to-chip liquid cooling moving from niche to mainstream production" rel="noopener">ref</a></sup>, and one analyst report frames the wider $600B+/yr AI infrastructure build as colliding with a grid that cannot deliver.

**TLDR: Demand is committed at hundreds of billions; supply of packaging and HBM4 is the thing throttling delivery.**

## Novelty (3/5)

The sources contain no per-generation performance comparison for Rubin against Blackwell, so any claim of a quantified uplift would be invented. What the sources do support is an architectural change of kind: NVIDIA moved from selling a GPU generation to selling a six-chip rack platform, and it responded to the prefill/decode specialisation threat by licensing a competitor's decode engine rather than building its own. Rubin CPX, its in-house prefill-only part with 30 PF NVFP4 and GDDR7 instead of HBM, was cancelled in March 2026 and replaced by the ~$20B Groq deal signed 24 December 2025, yielding the Groq 3 LPX SRAM decode co-processor on Samsung 4nm <sup class="ref"><a href="https://www.tomshardware.com/tech-industry/semiconductors/nvidias-20-billion-groq-deal-produces-its-first-chip" title="How Nvidia's $20 billion Groq 3 LPU deal reshapes the Nvidia Vera Rubin Platform" rel="noopener">ref</a></sup>. The LPX rack sits alongside Vera Rubin over Spectrum-X and runs with no CUDA code changes <sup class="ref"><a href="https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/" title="Inside the NVIDIA Rubin Platform: Six New Chips, One AI Supercomputer" rel="noopener">ref</a></sup>.

What it is better than: the alternative disaggregated approach, exemplified by the AWS-Cerebras collaboration announced March 2026 pairing Trainium 3 for prefill with Cerebras CS-3 for decode on Bedrock in H2 2026 <sup class="ref"><a href="https://futurumgroup.com/insights/aws-rises-to-the-agentic-ai-moment-with-cerebras-integration-for-fast-inference/" title="AWS Rises to the Agentic AI Moment with Cerebras Integration for Fast Inference" rel="noopener">ref</a></sup>, and by Google's TPU line, where TPU v9 "Triggerfish" is reported to carry roughly three times the baseline memory using MediaTek 336G SerDes <sup class="ref"><a href="https://www.semidoped.com/p/daily-update-june-23rd-2026" title="Semi Doped — Daily Update, June 23rd 2026" rel="noopener">ref</a></sup>. NVIDIA's differentiator is not raw specialisation but that the specialised part arrives inside a CUDA-compatible rack with no software migration. Against that, the Kyber slip means the one dimension where NVIDIA's rack architecture was supposed to pull decisively ahead, scale-up world size, is where it now stands still, which SemiAnalysis explicitly calls a rare technical opening for AMD and Google <sup class="ref"><a href="https://x.com/SemiAnalysis_/status/2073874671498387899" title="SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled" rel="noopener">ref</a></sup>.

**TLDR: The genuine novelty is absorbing specialised silicon into the incumbent rack, not a quantified generational leap the sources can evidence.**

## Diffusion (4/5)

**TLDR: CUDA continuity and pre-committed hyperscaler capex remove the usual adoption friction; the barriers are physical, not commercial.**

## Impact (5/5)

The slip case shows the same leverage in reverse. Because Rubin Ultra now has no proven path to a larger scale-up domain, one packaging problem on a PCB midplane translates directly into a competitive opening for AMD and Google TPU at the high end <sup class="ref"><a href="https://x.com/SemiAnalysis_/status/2073874671498387899" title="SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled" rel="noopener">ref</a></sup>. Second-order impact runs through customer strategy too: OpenAI's own Titan chip enters mass production on TSMC N3 with Broadcom in H2 2026, in parallel with Vera Rubin deployment on the same sites **2026 Openai Titan Custom Chip**, so the largest buyers are hedging even while adopting.

## Timing Now (0-2yr)

The current part is live. Vera Rubin launched 16 March 2026, ships H2 2026, with the first LPX rack already running at Azure and rollout across Stargate in the same window <sup class="ref"><a href="https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/" title="Inside the NVIDIA Rubin Platform: Six New Chips, One AI Supercomputer" rel="noopener">ref</a></sup> **2026 Openai Titan Custom Chip**. The Groq 3 LPX decode co-processor targets Q3 2026. So there is nothing speculative about the 0-2 year band.

## Overrated or underrated? Fairly rated

The product is real and the demand behind it is committed capital, not sentiment. Treating Vera Rubin as anything other than the default frontier training and inference architecture for 2026-27 would be wrong: it is launched, racked, liquid-cooled, live at Azure, deploying across Stargate, and it absorbs the phase-specialisation threat via the Groq licence without asking anyone to leave CUDA <sup class="ref"><a href="https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/" title="Inside the NVIDIA Rubin Platform: Six New Chips, One AI Supercomputer" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.tomshardware.com/tech-industry/semiconductors/nvidias-20-billion-groq-deal-produces-its-first-chip" title="How Nvidia's $20 billion Groq 3 LPU deal reshapes the Nvidia Vera Rubin Platform" rel="noopener">ref</a></sup>.

Where the market rating deserves a discount is the metronome narrative. In roughly nine months NVIDIA cancelled an announced prefill GPU, cancelled a rack stopgap after customer pushback, and lost more than a year on its next-generation rack to a PCB manufacturability problem <sup class="ref"><a href="https://x.com/SemiAnalysis_/status/2073874671498387899" title="SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled" rel="noopener">ref</a></sup>. The binding constraints have moved off the die and onto packaging, midplanes, HBM4 qualification and 600 kW-class thermals <sup class="ref"><a href="https://www.datacenterdynamics.com/en/opinions/unlocking-the-potential-of-direct-to-chip-liquid-cooling/" title="Direct-to-chip liquid cooling moving from niche to mainstream production" rel="noopener">ref</a></sup>. Roadmap dates beyond 2027, Feynman included, should be read as intentions with a demonstrated slip rate, not commitments. Net: correctly rated on the shipping generation, over-rated on cadence beyond it.

## Prediction

## Evidence base

## Open questions

- Is the Kyber PCB midplane a solvable manufacturability problem on a known schedule, or does it force a redesign of the rack interconnect that also affects Feynman?
- Does Feynman hold its 2028 date now that Kyber has been pushed into the same year, and what is its rated TDP given nothing has been disclosed?
- Does the three-way HBM4 split reach volume, given that shipments expected to scale from Q2 2026 had not materialised at scale by July 2026, and does Samsung's in-house SF4 logic base die qualify on NVIDIA parts?
- What is the actual attach rate of the Groq 3 LPX decode rack beyond the first Azure deployment, versus customers choosing disaggregated alternatives such as the AWS-Cerebras Trainium 3 / CS-3 pairing?

---
*Assessment drafted 2026-08-31 from up to 15 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
