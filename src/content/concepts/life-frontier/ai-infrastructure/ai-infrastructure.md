---
type: concept
slug: ai-infrastructure
canonical_name: AI Infrastructure
aliases: []
parent_concepts:
- life-frontier
related_concepts: []
sources:
- '[[2024-11-05-confidential-ai-the-dog-that-didnt]]'
- '[[2023-06-15-e04-no10-downing-street-and-vector]]'
- '[[2025-09-23-the-compute-gradient]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2024-11-12-atomic-energy-can-nuclear-power-our]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-06-23-semidoped-daily-update]]'
- '[[2026-05-26-techtimes-custom-asic-growth]]'
- '[[2025-11-09-openai-urges-trump-administration-to-expand-chips-act-incent]]'
- '[[2026-06-14-frontier-ai-value-capture]]'
- '[[2025-09-16-talent-as-constraint-csis-analysis-apprenticeship-programs]]'
- '[[2026-05-27-semianalysis-aws-bedrock-margins]]'
- '[[2026-06-02-frontier-llm-scaling-big-tech-ai-capex-2026-microsoft]]'
- '[[2026-07-08-why-ai-infrastructure-must-evolve-for-agent-experience-aksha]]'
- '[[2026-05-27-atlas-data-room]]'
- '[[2026-04-22-optical-displaces-copper-copper-vs-optical-in-the-ai]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-01-08-datacentre-thermal-power-market-data-center-liquid-cooling]]'
- '[[2026-03-16-ai-capex-financeable-financing-the-ai-infrastructure-boom]]'
- '[[2026-03-12-optical-displaces-copper-optical-scale-up-consortium]]'
- '[[2025-10-21-frontier-forum-the-new-power-map-for-ai-infrastructure---lat]]'
- '[[2026-04-09-model-commoditises-value-moves-up-the-foundation-model]]'
- '[[2026-02-12-ai-demand-outruns-expectations-ai-capex-2026-the-690b]]'
- '[[2026-06-17-tech-inflation-silicon-shock-federal-reserve-flags-ai]]'
- '[[2026-06-13-sovereign-electronics-manufacturing-reshoring-digest]]'
- '[[2026-03-12-photonics-material-class-war-hyperlight-umc-and-wavetek]]'
- '[[2026-idc-ai-infrastructure-tracker]]'
- '[[2026-07-01-the-next-ai-infrastructure-opportunity-is-unlocking-what-we-]]'
- '[[2026-04-01-ark-ai-infrastructure]]'
- '[[2026-05-22-ai-power-thermal-binding-goldman-sachs-ai-infrastructure]]'
- '[[2026-06-23-google-project-suncatcher]]'
- '[[2026-02-15-ai-power-thermal-binding-oracle-announces-direct-to-chip]]'
scorecard:
  viability: 4
  drivers: 5
  novelty: 3
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 103
descendants:
- ai-grade-datacentre-real-estate
- ai-infrastructure-scaling
- ai-machine-learning
- datacentre-cloud-infrastructure
- digital-twin
- gpu-virtualization
- moe-all-to-all-collectives
- prefill-vs-decode
- sovereign-ai
sources_7d: 0
sources_30d: 8
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-08-why-ai-infrastructure-must-evolve-for-agent-experience-aksha
  title: Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO
  date: '2026-07-08'
  kind: web
- slug: 2026-07-01-the-next-ai-infrastructure-opportunity-is-unlocking-what-we-
  title: The next AI infrastructure opportunity is unlocking what we already have
  date: '2026-07-01'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-23-google-project-suncatcher
  title: Exploring a space-based, scalable AI infrastructure system design
  date: '2026-06-23'
  kind: web
- slug: 2026-06-17-tech-inflation-silicon-shock-federal-reserve-flags-ai
  title: Federal Reserve flags AI demand as inflation risk in latest minutes
  date: '2026-06-17'
  kind: web
- slug: 2026-06-14-frontier-ai-value-capture
  title: 'Frontier AI value capture: where the $4T accrues (research synthesis)'
  date: '2026-06-14'
  kind: web
- slug: 2026-06-13-sovereign-electronics-manufacturing-reshoring-digest
  title: 'Western/European electronics manufacturing reshoring (PCB/PCBA): market + why-now digest'
  date: '2026-06-13'
  kind: web
neighbors: []
---
**AI infrastructure is the physical and software stack that turns capital into usable model compute (accelerators, power, liquid cooling, interconnect, serving software and the operational machinery that keeps it alive), and it is now absorbing roughly $487B of dedicated spend in 2026 on a path past $1T by 2029 **2026 Idc Ai Infrastructure Tracker**.**

## Summary

"AI infrastructure" is the layer between money and tokens. It spans accelerators (merchant GPUs plus custom silicon such as Amazon's Trainium), the power and thermal systems that let those parts run at density, the interconnect fabric inside and between racks, the inference serving software (vLLM, SGLang and their scheduling architectures), and the operational systems for fault detection, repair and security. It is not one technology but a stack in which each layer has become a distinct engineering and commercial market.

How it works, layer by layer, is where the interesting variables sit. On the silicon side, ARK projects custom accelerators reaching roughly 15-25% of total datacentre AI compute by 2030, with inference already around two-thirds of AI compute <sup class="ref"><a href="https://www.ark-invest.com/articles/analyst-research/the-state-of-ai-infrastructure-demand-costs-custom-silicon" title="The State of AI Infrastructure: Demand, Costs, Custom Silicon" rel="noopener">ref</a></sup>. On thermals, rising accelerator TDP and rack density are pushing air cooling past practical limits: Goldman Sachs forecasts 76% of AI servers requiring liquid cooling by end-2026, with direct-to-chip described as non-discretionary for GPU clusters <sup class="ref"><a href="https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html" title="Goldman Sachs AI Infrastructure Analysis: Liquid Cooling as Non-Discretionary" rel="noopener">ref</a></sup>, while Dell'Oro sizes the liquid cooling market at close to $7B by 2029 <sup class="ref"><a href="https://www.delloro.com/news/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate/" title="Data Center Liquid Cooling Market to Approach $7 Billion by 2029 as AI Deployments Accelerate" rel="noopener">ref</a></sup>. On interconnect, the copper-to-optical transition is slower than the optical thesis assumes: short-reach copper (DACs and AECs) is expected to hold intra-rack connectivity with a TAM above $10B by 2029 <sup class="ref"><a href="https://hightoweradvisors.com/blogs/well-th-blog/copper-vs-optical-in-the-ai-infrastructure-buildout" title="Copper vs Optical in the AI Infrastructure Buildout" rel="noopener">ref</a></sup>.

On the software side, serving architecture has progressively disaggregated: chunked-prefill aggregation, then prefill/decode disaggregation, and most recently operator-level attention-FFN disaggregation, which places memory-bound attention and compute-heavy expert FFNs on separate GPU groups for mixture-of-experts models. Each level widens the scheduling design space across sequence lengths, prefix-KV reuse, latency targets and topology, so the payoff is workload-dependent rather than universal. Underneath, the tooling to reason about this is itself immature: academic cycle-accurate simulators lag current GPU features such as the Tensor Memory Accelerator, and analytical models can misestimate DRAM traffic.

The parameters that decide the category are therefore: how long demand-side capex holds (four hyperscalers at roughly $725B in 2026, up 77% from about $410B in 2025, with analysts projecting above $1T in 2027 <sup class="ref"><a href="https://valueaddvc.com/blog/big-tech-ai-capex-in-2025-microsoft-google-meta-amazon-and-the-spending-race" title="Big Tech AI Capex 2026: Microsoft, Google, Meta, Amazon at $725 Billion" rel="noopener">ref</a></sup>); whether the physical constraints (power, cooling, skilled trades) can be relieved on schedule; and where in the stack margin actually lands, since evidence suggests it accrues upstream in silicon and downstream in distribution rather than in the model layer.

## Viability (4/5)

There is no question that AI infrastructure functions: it is generating revenue at scale and the economics are observable at the segment level. AWS EBIT margins rose roughly 213bp quarter-on-quarter while Azure and GCP were flat to declining, with Bedrock reaching about 37% of AWS AI revenue from around 9% a year earlier, and Trainium reportedly powering a majority of Bedrock token usage <sup class="ref"><a href="https://newsletter.semianalysis.com/p/anthropic-growth-and-bedrock-mix" title="Anthropic Growth and Bedrock Mix Drive AWS Margins Higher While Peers Lag" rel="noopener">ref</a></sup>. That is a working, margin-accretive infrastructure business, not a demonstration.

The deduction is operational. A production hyperscale platform accumulated 72,550 repair tickets over four years, of which 49% involved faults propagating across hardware, firmware, management software and orchestration boundaries, and existing static fault-injection campaigns exercise only 20-25% of modelled cross-layer propagation edges. Self-healing pipelines are therefore being deployed faster than they are being validated. The same pattern appears in tooling (simulators that lag current accelerator features) and in security, where pre-trained models shared through open repositories are treated as essential infrastructure with no established tamper-verification path, which is why NSF is funding supply-chain verification work across three institutions at roughly $400-410k each.

**TLDR: The stack demonstrably works at hyperscale; the reliability and operations layer is measurably incomplete.**

## Drivers (5/5)

Demand: IDC puts dedicated AI infrastructure spend at $487B in 2026, eclipsing $1T by 2029, triangulating with independent estimates of hyperscaler capex around $600B for 2026 and a multi-trillion buildout across 2026-31 **2026 Idc Ai Infrastructure Tracker**. The four largest hyperscalers alone are cited at roughly $725B in 2026, up 77% year on year, with 2027 projected above $1T <sup class="ref"><a href="https://valueaddvc.com/blog/big-tech-ai-capex-in-2025-microsoft-google-meta-amazon-and-the-spending-race" title="Big Tech AI Capex 2026: Microsoft, Google, Meta, Amazon at $725 Billion" rel="noopener">ref</a></sup>. Inference, at around two-thirds of AI compute, is the growing share <sup class="ref"><a href="https://www.ark-invest.com/articles/analyst-research/the-state-of-ai-infrastructure-demand-costs-custom-silicon" title="The State of AI Infrastructure: Demand, Costs, Custom Silicon" rel="noopener">ref</a></sup>, which matters because inference demand is tied to product usage rather than to research budgets and is therefore harder to cut abruptly.

Supply: the binding constraints in these sources are people and physics. CSIS argues the United States must expand apprenticeship programmes by at least 50% by 2030 to meet AI infrastructure demand, with instructor shortage as the primary constraint and near-term immigration required to avoid falling behind <sup class="ref"><a href="https://www.csis.org/analysis/genais-human-infrastructure-challenge-can-united-states-meet-skilled-trade-labor-demand" title="CSIS Analysis—Apprenticeship Programs Must Expand 50% by 2030 to Meet AI Infrastructure Demand" rel="noopener">ref</a></sup>. Thermal capacity is the other gate: liquid cooling is described as moving from niche to a foundational requirement for next-generation deployments <sup class="ref"><a href="https://www.delloro.com/news/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate/" title="Data Center Liquid Cooling Market to Approach $7 Billion by 2029 as AI Deployments Accelerate" rel="noopener">ref</a></sup>. Energy is the long-run driver behind speculative designs such as orbital compute.

**TLDR: Demand is the strongest documented capital signal in the sources; supply constraints are physical and human, not technological.**

## Novelty (3/5)

The genuine novelty claims are architectural rather than component-level. Attention-FFN disaggregation is a new level beyond prefill/decode splitting, exposing the heterogeneity of MoE workloads by placing attention and expert FFNs on separate GPU groups; the paper's own framing is that the central open question is when each level of disaggregation actually pays off, which is an admission that the improvement is conditional on workload and topology. Adaptive fault injection is a clearer delta: it reaches full modelled edge coverage within 10 iterations against 20-25% for static campaigns.

What it is better than, at the commercial layer, is generic IaaS. Bedrock earns both infrastructure fees and a distribution cut on third-party model sales, structurally richer than the IaaS that dominates over 80% of rivals' AI revenue <sup class="ref"><a href="https://newsletter.semianalysis.com/p/anthropic-growth-and-bedrock-mix" title="Anthropic Growth and Bedrock Mix Drive AWS Margins Higher While Peers Lag" rel="noopener">ref</a></sup>. Custom silicon is better than merchant GPUs on inference price-performance, though the sources give only a share projection (15-25% by 2030) rather than a per-token cost delta <sup class="ref"><a href="https://www.ark-invest.com/articles/analyst-research/the-state-of-ai-infrastructure-demand-costs-custom-silicon" title="The State of AI Infrastructure: Demand, Costs, Custom Silicon" rel="noopener">ref</a></sup>. Against that, one widely assumed step change is not happening: copper is expected to remain preferred for intra-rack links with a TAM above $10B by 2029 <sup class="ref"><a href="https://hightoweradvisors.com/blogs/well-th-blog/copper-vs-optical-in-the-ai-infrastructure-buildout" title="Copper vs Optical in the AI Infrastructure Buildout" rel="noopener">ref</a></sup>. Space-based compute is the most novel item and the least proven: Trillium TPUs survive a radiation dose equivalent to a five-year mission without permanent failures and an 81-satellite, 1 km-radius formation is described, but this is a design study, not a system.

**TLDR: Real architectural change (disaggregated serving, custom silicon, liquid cooling), but the sources rarely quantify the gain over the incumbent.**

## Diffusion (4/5)

Diffusion of AI infrastructure is not a persuasion problem. Liquid cooling adoption is described as non-discretionary for AI GPU clusters, with 76% of AI servers forecast to require it by end-2026 <sup class="ref"><a href="https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html" title="Goldman Sachs AI Infrastructure Analysis: Liquid Cooling as Non-Discretionary" rel="noopener">ref</a></sup>; when the alternative is not running the accelerators, deployment follows. The serving software layer diffuses through open source at high velocity: vLLM merged 18,290 PRs between February 2023 and June 2026 and SGLang 14,938 between January 2024 and June 2026, with both projects showing substantial increases in development velocity across the agentic-coding eras. That is fast, broad, low-friction distribution of best-practice inference architecture.

The barriers are downstream of the decision to build. Skilled-trades capacity is the clearest: a required 50% expansion of apprenticeship programmes by 2030 with instructor supply as the bottleneck implies multi-year training lags that capex cannot compress <sup class="ref"><a href="https://www.csis.org/analysis/genais-human-infrastructure-challenge-can-united-states-meet-skilled-trade-labor-demand" title="CSIS Analysis—Apprenticeship Programs Must Expand 50% by 2030 to Meet AI Infrastructure Demand" rel="noopener">ref</a></sup>. Cross-layer fault propagation is the second: roughly three-quarters of the modelled cross-layer attack surface goes unexercised by conventional testing, which becomes an availability risk as fleets scale. Model supply-chain trust is a third, currently at the research-funding stage rather than the deployed-control stage.

**TLDR: Adoption is already forced by physics and product demand; the barriers are trades labour, power and unvalidated operations.**

## Impact (4/5)

In pure magnitude the impact case is settled: dedicated AI infrastructure spend passing $1T by 2029 **2026 Idc Ai Infrastructure Tracker** and hyperscaler capex plausibly above $1T in 2027 <sup class="ref"><a href="https://valueaddvc.com/blog/big-tech-ai-capex-in-2025-microsoft-google-meta-amazon-and-the-spending-race" title="Big Tech AI Capex 2026: Microsoft, Google, Meta, Amazon at $725 Billion" rel="noopener">ref</a></sup> make this one of the largest capital formations in the technology economy. Value capture research places the durable rents upstream in foundry, accelerators, memory, litho and packaging, protected by multi-year contracts new entrants cannot replicate, with AI accelerators taking 60% of N3 output in 2026 and 90% in 2027. That is infrastructure capturing surplus, not merely enabling it.

The reason this is not a 5 is that the same analysis shows value flowing away from the frontier-model layer, with open-weight pricing (DeepSeek V3.2 at $0.28/M against GPT-5.2 at roughly $10/M) imposing a ceiling, and structural unprofitability at high revenue. If model-layer economics compress, the demand curve for the most expensive infrastructure legs is less secure than the aggregate spend figures suggest. The counterweight is that inference is already about two-thirds of compute <sup class="ref"><a href="https://www.ark-invest.com/articles/analyst-research/the-state-of-ai-infrastructure-demand-costs-custom-silicon" title="The State of AI Infrastructure: Demand, Costs, Custom Silicon" rel="noopener">ref</a></sup> and that distribution platforms can convert token volume into margin <sup class="ref"><a href="https://newsletter.semianalysis.com/p/anthropic-growth-and-bedrock-mix" title="Anthropic Growth and Bedrock Mix Drive AWS Margins Higher While Peers Lag" rel="noopener">ref</a></sup>, which makes utilisation-linked infrastructure more resilient than training-linked infrastructure.

**TLDR: Trillion-dollar-scale spend with durable rents, but the sources show the value concentrating in specific layers rather than the category as a whole.**

## Timing Now (0-2yr)

Every commercially material element is in the present tense. Spend is booked for 2026 at $487B dedicated **2026 Idc Ai Infrastructure Tracker** and roughly $725B across four hyperscalers <sup class="ref"><a href="https://valueaddvc.com/blog/big-tech-ai-capex-in-2025-microsoft-google-meta-amazon-and-the-spending-race" title="Big Tech AI Capex 2026: Microsoft, Google, Meta, Amazon at $725 Billion" rel="noopener">ref</a></sup>. The cooling architecture change resolves within the band, with 76% of AI servers forecast liquid-cooled by end-2026 <sup class="ref"><a href="https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html" title="Goldman Sachs AI Infrastructure Analysis: Liquid Cooling as Non-Discretionary" rel="noopener">ref</a></sup>. Disaggregated MoE serving is being characterised and deployed now, and the open-source serving stacks are iterating weekly.

Two items sit later. Labour capacity resolves around 2030, since the apprenticeship expansion CSIS calls for carries a multi-year training lag <sup class="ref"><a href="https://www.csis.org/analysis/genais-human-infrastructure-challenge-can-united-states-meet-skilled-trade-labor-demand" title="CSIS Analysis—Apprenticeship Programs Must Expand 50% by 2030 to Meet AI Infrastructure Demand" rel="noopener">ref</a></sup>, and custom silicon share targets are set for 2030 <sup class="ref"><a href="https://www.ark-invest.com/articles/analyst-research/the-state-of-ai-infrastructure-demand-costs-custom-silicon" title="The State of AI Infrastructure: Demand, Costs, Custom Silicon" rel="noopener">ref</a></sup>. Space-based AI compute is a design-space exploration with component radiation testing only and should be treated as distant.

**TLDR: The buildout, the thermal transition and the serving-architecture shift are all live in 2026; only orbital compute sits beyond a decade.**

## Overrated or underrated? Fairly rated

As a category, AI infrastructure is priced roughly for what it is: an enormous, physically constrained buildout with genuine upstream rents. Three independent estimates converge on the same demand roof of about $600B in 2026 rising to $1T by 2029 **2026 Idc Ai Infrastructure Tracker**, and the margin evidence shows infrastructure owners actually capturing value rather than subsidising the model layer <sup class="ref"><a href="https://newsletter.semianalysis.com/p/anthropic-growth-and-bedrock-mix" title="Anthropic Growth and Bedrock Mix Drive AWS Margins Higher While Peers Lag" rel="noopener">ref</a></sup>. There is no serious case that the category is a lab curiosity or a mirage.

The mispricing is inside the stack, not at the top level. The layers the sources treat as unglamorous are the ones with the most unresolved engineering and the least attention: cross-layer fault propagation, where 49% of 72,550 repair tickets crossed layer boundaries and three-quarters of the modelled propagation surface is untested; model supply-chain integrity, still at NSF grant scale; and skilled-trades capacity, which no amount of capex converts into commissioned megawatts inside the training lag <sup class="ref"><a href="https://www.csis.org/analysis/genais-human-infrastructure-challenge-can-united-states-meet-skilled-trade-labor-demand" title="CSIS Analysis—Apprenticeship Programs Must Expand 50% by 2030 to Meet AI Infrastructure Demand" rel="noopener">ref</a></sup>. Conversely, at least one consensus transition looks overrated: copper is expected to retain intra-rack connectivity through 2029 <sup class="ref"><a href="https://hightoweradvisors.com/blogs/well-th-blog/copper-vs-optical-in-the-ai-infrastructure-buildout" title="Copper vs Optical in the AI Infrastructure Buildout" rel="noopener">ref</a></sup>. Own the constraint, not the headline.

## Prediction

By 31 December 2027, combined reported 2027 AI infrastructure capex for Microsoft, Alphabet, Meta and Amazon will exceed $1 trillion, consistent with the projection made in mid-2026 <sup class="ref"><a href="https://valueaddvc.com/blog/big-tech-ai-capex-in-2025-microsoft-google-meta-amazon-and-the-spending-race" title="Big Tech AI Capex 2026: Microsoft, Google, Meta, Amazon at $725 Billion" rel="noopener">ref</a></sup>.

## Evidence base

- IDC put dedicated AI infrastructure spend at $487B in 2026, eclipsing $1T by 2029, triangulating with independent hyperscaler capex and multi-year buildout estimates **2026 Idc Ai Infrastructure Tracker**.
- Four hyperscalers were reported to be spending roughly $725B on AI infrastructure in 2026, up 77% from about $410B in 2025, with 2027 projected above $1T (2026-06-02) <sup class="ref"><a href="https://valueaddvc.com/blog/big-tech-ai-capex-in-2025-microsoft-google-meta-amazon-and-the-spending-race" title="Big Tech AI Capex 2026: Microsoft, Google, Meta, Amazon at $725 Billion" rel="noopener">ref</a></sup>.
- Goldman Sachs forecast 76% of AI servers requiring liquid cooling by end-2026, with direct-to-chip described as non-discretionary for GPU clusters (2026-05-22) <sup class="ref"><a href="https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html" title="Goldman Sachs AI Infrastructure Analysis: Liquid Cooling as Non-Discretionary" rel="noopener">ref</a></sup>.
- A hyperscale production platform logged 72,550 repair tickets over four years, 49% involving cross-layer fault propagation, while static test campaigns covered only 20-25% of modelled propagation edges (2026-07-20).
- Bedrock reached about 37% of AWS AI revenue from roughly 9% a year earlier, with AWS EBIT margins up around 213bp QoQ and Trainium reportedly powering a majority of Bedrock tokens (2026-05-27) <sup class="ref"><a href="https://newsletter.semianalysis.com/p/anthropic-growth-and-bedrock-mix" title="Anthropic Growth and Bedrock Mix Drive AWS Margins Higher While Peers Lag" rel="noopener">ref</a></sup>.
- Copper DACs and AECs are expected to remain preferred for intra-rack connectivity, with short-reach copper TAM above $10B by 2029 (2026-04-22) <sup class="ref"><a href="https://hightoweradvisors.com/blogs/well-th-blog/copper-vs-optical-in-the-ai-infrastructure-buildout" title="Copper vs Optical in the AI Infrastructure Buildout" rel="noopener">ref</a></sup>.
- Trillium TPUs survived a total ionising dose equivalent to a five-year mission without permanent failures in a study of an 81-satellite, 1 km-radius orbital compute cluster (2026-06-18).

## Open questions

- Does the 76% liquid-cooled AI server share forecast for end-2026 actually verify in shipment data, or does air cooling retain a larger share of new capacity than Goldman assumes <sup class="ref"><a href="https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html" title="Goldman Sachs AI Infrastructure Analysis: Liquid Cooling as Non-Discretionary" rel="noopener">ref</a></sup>?
- If open-weight models continue to price 15-35x below frontier APIs, does inference infrastructure demand still scale with token volume, or does revenue per deployed watt collapse?
- Do adaptive fault-injection methods such as ADA-ST reduce real incident rates in production fleets, or only modelled edge coverage?
- Does attention-FFN disaggregation deliver measurable throughput or latency gains at production scale over prefill/decode disaggregation, and for which sequence-length and KV-reuse regimes?
- Can US apprenticeship capacity expand 50% by 2030 given the instructor bottleneck, and if not, which announced sites slip or cancel <sup class="ref"><a href="https://www.csis.org/analysis/genais-human-infrastructure-challenge-can-united-states-meet-skilled-trade-labor-demand" title="CSIS Analysis—Apprenticeship Programs Must Expand 50% by 2030 to Meet AI Infrastructure Demand" rel="noopener">ref</a></sup>?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
