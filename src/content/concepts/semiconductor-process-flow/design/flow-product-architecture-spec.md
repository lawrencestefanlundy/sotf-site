---
type: concept
slug: flow-product-architecture-spec
canonical_name: Product specification & architecture (process step)
seq: 1
phase: design
related_concepts:
- eda-design-tools
created: 2026-06-20
last_updated: 2026-06-20
tags:
- concept
- process-flow
- semiconductor
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
mention_count: 7
parent_concepts:
- flow-rtl-design
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
neighbors:
- slug: eda-design-tools
  name: EDA & Design Tools
  path: /manufacturing/foundry-design/eda-design-tools/
  macro: manufacturing
---
> Step 1 of 56 in the semiconductor flow (Design). Next: [Semiconductor IP licensing (process step)](/semiconductor-process-flow/design/flow-ip-licensing-cores/)

## What this step does
This is the blank-sheet decision about what the chip is: what it must compute, at what power and cost, on which process node, in what package. It produces the product spec and the micro-architecture before any RTL is written. Most of the value here is human, not tooling. The sub-processes:
- Product/market requirements to a frozen spec (performance, power, area, cost, I/O standards).
- Micro-architecture and partitioning (cores, memory hierarchy, interconnect, chiplet vs monolithic).
- Process-node and foundry selection, package and thermal envelope.
- Make-vs-buy on IP blocks, and the build/outsource decision that feeds the design-services market.

## Where it sits and why it matters
This is the highest-leverage step in the entire 56-stage flow. An architecture mistake here cannot be fixed downstream by a better tapeout or a tighter etch. The value-capturing layer is not a tool you buy off the shelf; it is the engineering judgement of an internal architecture team or, increasingly, of a merchant ASIC design house that sells "spec-in to silicon" as a service. The economic story of this step is the rise of the design-services / custom-silicon business, which sits between the chip owner (a hyperscaler, an OEM, a fabless startup) and the foundry.

## Equipment market
There is no fab-style capital equipment at this step. The closest "tool" layer is EDA architecture and verification software (virtual prototyping, high-level synthesis, power/performance estimation), which is a sub-slice of the ~$15-17bn EDA market and is treated on [EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/). The bigger commercial layer at this step is the design-services revenue pool itself. Estimates vary widely and the report-mill TAMs should be distrusted; a defensible range is ~$11-15bn in 2025 growing at roughly 8-12% CAGR for general ASIC design services [1], with the AI-custom-silicon sub-segment growing far faster (below).

| Vendor | HQ | Est. share of merchant ASIC/design-services | Notable |
|---|---|---|---|
| Broadcom (custom silicon) | US | ~60-70% of custom AI ASIC | Google TPU, Meta MTIA; ~70% of custom AI accelerator rev [2] |
| Marvell (custom silicon) | US | ~25% of custom AI ASIC | AWS Trainium 2, >50 sockets, $75bn pipeline [2][3] |
| Alchip | Taiwan | leading pure-play | $1.62bn FY24 rev, ~60% from AWS Trainium 1 [4] |
| GUC (Global Unichip) | Taiwan | leading advanced-node | TSMC-affiliated, HBM/UCIe/3D IP [5] |
| Socionext | Japan | mid-tier | ~Yen221bn (~$1.5bn) FY24 net sales [6] |
| Faraday | Taiwan | mid-tier | NT$11.1bn (~$345m) FY24, 45.7% gross margin [7] |

Concentration note: the headline-grabbing AI slice is a duopoly (Broadcom + Marvell ~80%+ of hyperscaler custom AI silicon per Bloomberg Intelligence [2]), but the broader merchant design-services market is more fragmented across Taiwanese and Japanese houses and dozens of regional shops.

## Materials & consumables
This step consumes no physical materials. Its recurring "consumable" is licensed IP (CPU cores, SerDes, PHYs, memory controllers) bought-in rather than built, which is the subject of the next step [Semiconductor IP licensing (process step)](/semiconductor-process-flow/design/flow-ip-licensing-cores/). The semiconductor-IP market it feeds was ~$5.9-7.5bn in 2024, Arm ~40% share, Synopsys ~13% [8]. The recurring-revenue character of this step comes in two forms: NRE (one-off engineering fees billed during design) and, for turnkey houses, downstream wafer/production margin once the chip ships, which is the stickier annuity.

## Volumes, revenue, profitability
Unit volumes are not the right metric here; design starts and program wins are. The economics split cleanly:
- Custom AI ASIC end-revenue (the production silicon these designs become) was ~$12-13bn in 2024-25 and is forecast toward $50-70bn by 2028 and possibly >$150bn by 2030 (~40-50% CAGR) [2][9]. The design-services fee pool is a fraction of that, but it is the leading indicator.
- Margins separate the asset-light from the turnkey model. Pure design/NRE and IP-rich houses earn high margins: Faraday 45.7% gross [7], GUC ~30% gross (NRE higher, wafer lower) [5]. Turnkey houses that resell foundry wafers earn thin product margins: Alchip ~20% gross in FY24 [4]. Broadcom captures the richest margin because it owns the IP and the customer relationship rather than reselling wafers.
- Who earns the margin: the layer that owns scarce advanced-node design talent and a captive IP library (Broadcom, GUC), not the layer that merely brokers the foundry slot.

## Competitive landscape & value capture
The moat is talent density plus a proven advanced-node track record plus a captive IP portfolio (SerDes, UCIe, HBM, 3D stacking). It is a relationship-and-reputation business: a hyperscaler will not hand a $1bn tapeout to an unproven house. Value accrues to whoever sits closest to the IP and the customer; it leaks away from anyone who is just a foundry sub-contractor (Alchip's AWS dependence and 20% gross margin shows the fragility of the broker position, sharpened when AWS moved Trainium 2 to Marvell [4]). EU / seed-relevant players exist but are small: EnSilica (AIM:ENSI, ~£28-30m FY25 guided, mixed-signal turnkey [10]), the new independent Dolphin Semiconductor and **NanoXplore**'s acquired Dolphin ASIC business (France/aerospace), and Presto Engineering. Alphawave Semi (UK-rooted, now US-acquired; $307.6m FY24, $515.5m bookings [11]) is the clearest example of a Western connectivity-IP-plus-custom-silicon play.

## Market drivers, constraints & trends
Net read on this step's served market (design-services fee pool + the AI-custom-silicon programs it leads): accelerating into 2027-28, then a concentration overhang that decides who keeps the margin.

- **Drivers**
  - Custom ASIC server shipments forecast to grow ~44.6% in 2026, nearly triple merchant-GPU growth (~16.1%), so design-services NRE is the leading indicator of a step-change in production silicon [12]. Broadcom guides to up to ~$100bn AI chip revenue by 2027; Marvell ~$11bn AI ASIC in 2026 [12].
  - New first-party programs widen the design-win pool beyond the original four hyperscalers: OpenAI + Broadcom 10GW of OpenAI-designed accelerators, deployments starting H2 2026 through 2029 [13]; Google now runs four silicon partners plus an in-house team [14].
  - Chiplet disaggregation turns one SoC into many dies and multiplies partitioning, UCIe, and HBM integration work that merchant houses are positioned to sell; ASIC design-service market ~$11.4bn 2025 toward ~$26.8bn 2034 (~10% CAGR) [15].
  - EU Chips Act 2.0 European Design Platform aims to tape out chips from 100 fabless startups (10 unicorns) by 2035, opening a sovereign design-services demand line for the few EU-relevant houses [16].

- **Constraints**
  - Disintermediation: if any hyperscaler internalises the design work now flowing through the Broadcom + Marvell ~95% duopoly, the fee pool erodes; Google's in-house team and MediaTek/Marvell second-sourcing already show the path [14][17].
  - Talent is the hard ceiling: advanced-node physical design, SerDes/mixed-signal, and UVM verification engineers are critically scarce (SIA flags ~115k unfilled US roles by 2030), capping how many parallel tapeouts the merchant houses can staff [18].
  - Concentration and customer captivity: Alchip's ~60% AWS dependence and ~20% gross margin show how fragile the broker position is when a single program moves [4].

- **Trends & inflections to watch**
  - Architecture shift to chiplets + UCIe 2.0 (64 Gbps, optical die-to-die in 2026-27) raises the value of houses with captive UCIe/3D IP [15]. Tripwire: a merchant ASIC house wins a named UCIe-based multi-die hyperscaler socket in 2026.
  - First-party silicon spreading past hyperscalers to AI labs and sovereigns. Tripwire: a second non-hyperscaler (after OpenAI) signs a multi-GW custom-accelerator design deal by end-2026 [13].
  - Hyperscaler insourcing as the bear. Tripwire: a top-four hyperscaler moves a flagship accelerator fully in-house (no merchant design partner) on a 2026-27 tapeout [17].
  - EU sovereign-design route turning real. Tripwire: first European Design Platform tape-out funded through an EU-domiciled design-services house by 2027 [16].

## Connections
- [EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/) (the software layer used at this step)
- **Eda Chip Design** (thesis)
- Next step: [Semiconductor IP licensing (process step)](/semiconductor-process-flow/design/flow-ip-licensing-cores/)

## Sources
1. MarketResearchFuture / Credence / multiple, ASIC Design Services market $11-15bn 2025, ~8-12% CAGR (report-mill range, treat as rough) - https://www.credenceresearch.com/report/asic-design-services-market
2. Tom's Hardware, custom AI ASIC state of play, Broadcom ~60-70% / Marvell ~25%, Bloomberg Intelligence 80%+ duopoly - https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia
3. Yahoo Finance / Marvell, >50 XPU sockets, $75bn pipeline - https://finance.yahoo.com/news/mrvls-custom-silicon-business-scales-135700350.html
4. Alchip / GlobeNewswire, FY24 $1.62bn rev, ~20% gross margin, 60% from AWS; CommonWealth on margin vs Broadcom - https://www.globenewswire.com/news-release/2025/03/28/3051439/0/en/Alchip-Technologies-Sets-2024-Financial-Records.html
5. GUC investor materials, Q1 24 29.7% gross margin, NRE vs wafer split - https://www.guc-asic.com
6. Socionext IR, FY24 net sales ~Yen221bn - https://www.socionext.com/en/ir/pdf/sn_ir20250428_03e.pdf
7. Faraday FY24 results, NT$11.07bn rev, 45.7% gross margin - https://anysilicon.com/faraday-reports-full-year-2024-results/
8. Semiconductor IP market 2024 ~$5.9-7.5bn, Arm ~40%, Synopsys ~13% - https://www.globenewswire.com/news-release/2026/03/02/3247502/0/en/Semiconductor-Intellectual-Property-Research-Report-2026-2035-A-13-54-Billion-Market-by-2030-with-Arm-Synopsys-Cadence-Design-Systems-CEVA-Imagination-Technologies-Leading.html
9. ARK Invest / TrendForce, AI ASIC $13bn 2024 to $150bn 2030, datacenter ASIC $50-70bn by 2028 - https://www.ark-invest.com/articles/analyst-research/the-state-of-ai-infrastructure-demand-costs-custom-silicon
10. EnSilica FY25 guidance £28-30m, EBITDA £3.5-4.5m - https://www.investegate.co.uk/announcement/rns/ensilica--ensi/audited-full-year-results/8529395
11. Alphawave Semi FY24 $307.6m rev, $515.5m bookings - https://awavesemi.com/press-release/alphawave-semi-q4-2024-trading-and-business-update/
12. Tom's Hardware, custom AI ASIC state of play May 2026, ASIC shipments +44.6% 2026 vs GPU +16.1%, Broadcom ~$100bn AI rev by 2027, Marvell ~$11bn AI ASIC 2026 - https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia
13. OpenAI + Broadcom, 10GW OpenAI-designed accelerators, deployments H2 2026 to 2029 - https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/
14. Hashrate Index, AI ASIC design-partner duopoly ~95%, Google four-partner + in-house strategy, disintermediation risk - https://hashrateindex.com/blog/design-partners-ai-asic-market-part-2/
15. ASIC design-service market $11.4bn 2025 to $26.8bn 2034 (~10% CAGR); UCIe 2.0 64 Gbps + optical die-to-die 2026-27 - https://www.patsnap.com/resources/blog/articles/chiplet-interconnect-tech-2026-ucie-hbm4-packaging/
16. EE Times / EU, Chips Act 2.0 European Design Platform, 100 fabless startups + 10 unicorns by 2035 - https://www.eetimes.com/chips-act-2-0-inside-europes-semiconductor-rethink/
17. The Next Web, Google in talks with Marvell for inference chips alongside Broadcom; hyperscaler insourcing/second-sourcing - https://thenextweb.com/news/google-marvell-ai-chips-inference-tpu-broadcom
18. SIA / Synopsys, semiconductor talent shortage, ~115k unfilled US roles by 2030, advanced-node + SerDes + verification scarcity - https://www.synopsys.com/blogs/chip-design/semiconductor-engineering-talent-shortage-solutions.html
