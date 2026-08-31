---
type: concept
slug: flow-ip-licensing-cores
canonical_name: Semiconductor IP licensing (process step)
seq: 2
phase: design
related_concepts:
- eda-design-tools
- pdk-process-design-kit
created: 2026-06-20
last_updated: 2026-06-20
tags:
- concept
- process-flow
- semiconductor
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
mention_count: 8
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
- slug: pdk-process-design-kit
  name: PDK / Process Design Kit
  path: /manufacturing/foundry-design/pdk-process-design-kit/
  macro: manufacturing
---
> Step 2 of 56 in the semiconductor flow (Design). Prev: [Product specification & architecture (process step)](/semiconductor-process-flow/design/flow-product-architecture-spec/) · Next: [RTL design (HDL) (process step)](/semiconductor-process-flow/design/flow-rtl-design/)

## What this step does
Once the chip's architecture is fixed, the design team buys in pre-built, pre-verified circuit blocks (semiconductor IP, or "cores") rather than designing every function from scratch. A modern system-on-chip is mostly licensed IP stitched together with a thin layer of custom logic. The licensed blocks fall into three groups:
- Processor IP (CPU, GPU, NPU, DSP cores) such as an Arm Cortex or a RISC-V core
- Interface / connectivity IP (PCIe, USB, DDR/HBM memory controllers, SerDes, Ethernet) which Yole calls the "wired interface" category
- Foundation IP (standard-cell libraries, embedded memory compilers, analog PLLs, security and physical IP tied to a specific foundry node)

## Where it sits and why it matters
This is the step where the largest single chunk of design-stage economics is paid out, and it is the most concentrated and highest-margin layer in the entire 56-step flow. A licence is taken once per design; a royalty is then paid on every chip shipped for the life of the product, so IP revenue compounds with end-market volume rather than with design activity. The IP chosen here also locks the design into a software ecosystem (the Arm vs RISC-V instruction-set choice is effectively irreversible after this point) and constrains the foundation IP available downstream at RTL, synthesis and physical design.

## Equipment market
There is no physical equipment in this step. The "tool" market is the design IP licence pool itself plus the [EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/) used to integrate it. The IPnest/Yole design IP market reached roughly $8.5B in 2024, growing ~20% year on year, an all-time-high growth rate [1]. Broader "semiconductor IP" reports put 2025 at ~$7.9B with a mid-single-digit to ~9% CAGR [2][3]; the gap is mostly classification (some reports exclude EDA-bundled IP). Treat the ~$8B and the headline shares as the reliable numbers and the longer forecasts as report-mill estimates.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Arm | UK | ~40% (largest single vendor) | Processor IP; FY25 revenue $4.0B, royalty 54% [4] |
| Synopsys | US | ~20% | Interface + foundation IP; IP revenue ~$1.7B [1] |
| Cadence | US | ~8-9% | Interface IP; IP revenue ~$0.7B+ [1] |
| Alphawave | UK/Canada | ~5-7% | SerDes/connectivity; acquired by Qualcomm Dec 2025, ~$2.4B EV [5] |
| Imagination | UK | low single % | GPU IP (PowerVR), now China-owned (Canyon Bridge) |
| Ceva | US/Israel | low single % | DSP, wireless and edge-AI IP |
| SiFive / Andes / Codasip | US / Taiwan / Germany | RISC-V leaders | RISC-V CPU IP, fast-growing share [6] |

Concentration note: the top four (Arm, Synopsys, Cadence, Alphawave) held ~75% of the design IP market in 2024, up from 72% in 2023, and grew faster than the market (~25%) [1]. Arm and Synopsys alone are ~66%. This is one of the most concentrated layers in semiconductors, now tightening further as Qualcomm absorbs Alphawave and Synopsys absorbs Ansys.

## Materials & consumables
The recurring "consumable" of this step is the royalty stream, not a physical material. Each shipped chip carries a per-unit royalty (often a few cents to low single-digit percent of chip ASP) back to the IP owner, so the installed base of designs behaves like an annuity. Arm books royalties on tens of billions of chips a year, and royalty was ~54% of its $4.0B FY25 revenue [4]. The other "consumable" is renewal: subscription and multi-year licence agreements (Arm Total Access, Synopsys/Cadence IP subscriptions) convert one-off licences into recurring revenue. There are no physical-material vendors here.

## Volumes, revenue, profitability
Unit volumes are measured in chips shipped against licensed cores: Arm-based chips alone run at ~30B units a year, and essentially every smartphone, most microcontrollers and a rising share of data-centre and automotive silicon carry licensed IP. The revenue pool is the ~$8B design IP market [1] plus the royalty tail that compounds on top. This layer carries the best margins in the whole flow: Arm's FY25 gross margin was ~97% with non-GAAP operating margin in the low-50s% [4]; pure-play IP gross margins generally run 90%+ because the marginal cost of granting another licence is near zero. The margin is earned by the IP owner, not the licensee, the foundry or the EDA vendor. This is the structural reason IP licensing is a far better business than fabrication.

## Market drivers, constraints & trends
Net read: accelerating. The IP pool grew ~20% in 2024 [1] and the two fastest sub-pools (chiplet interface IP, RISC-V CPU IP) are compounding well ahead of the blended ~6-9% silicon-IP forecast [2], pulled by AI silicon and dragged by export-control and incumbent-encroachment risk.

- **Drivers** — AI/datacentre custom silicon multiplies the interface IP per design: the die-to-die IP pool runs ~$1.8B in 2025 to ~$3.7B by 2033 (~9.6% CAGR), with UCIe ~53% of it and growing fastest (~9.9%) [7]. HBM4 PHY/controller IP is becoming a per-XPU recurring buy as hyperscalers move to custom HBM base dies [8]. RISC-V CPU IP is the highest-growth processor sub-pool (~$1.3B 2025, 40%+ CAGR forecast, "year of RVA silicon" server launches: SiFive P870D, NextSilicon Arbel) [9][10]. Automotive and edge-AI add royalty-bearing units on top.
- **Constraints** — China export controls hit the licensing channel hard: BIS letters in May 2025 froze EDA/IP sales (Synopsys ~16%, Cadence ~12% of revenue from China) before being rescinded six weeks later [11]; the on/off risk recurs and caps the China royalty tail. Arm moving up the stack (AGI CPU, its first own production chip, full availability H2 2026; CSS/CSA subsystems) creates channel conflict with the licensees it sells to [12]. RISC-V's near-parity with high-end Arm cores by end-2026 [10] threatens the processor-royalty rent that is the pool's best margin.
- **Trends & inflections to watch** — Chiplet disaggregation shifts value from one CPU licence to many interface-IP licences per package; tripwire: UCIe 2.0 (64Gbps, optical D2D option) production design wins in 2026-2027 [13]. Arm's own-silicon model proves out or backfires; tripwire: a top-5 hyperscaler publicly switching from an Arm licence to a RISC-V server core for production inference [9]. Royalty mix re-rates upward as subscription/Total-Access deals convert one-off licences to recurring revenue; tripwire: Qualcomm-Alphawave UCIe/HBM IP showing up in third-party data-centre design wins [11].

## Connections
- Tooling and integration: [EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/)
- Foundry-specific foundation IP comes via the [PDK / Process Design Kit](/manufacturing/foundry-design/pdk-process-design-kit/)
- Thesis on whether open silicon takes share from Arm: **Risc V Open Silicon Share**
- Broader design-software thesis: **Eda Chip Design**

## Sources
1. Design-Reuse / IPnest, "Design IP Market Increased by All-time-high: 20% in 2024" ($8.5B market, top-4 ~75% share, category growth). https://www.design-reuse.com/industryexpertblogs/57690/2024-design-ip-market.html
2. Mordor Intelligence, Semiconductor Silicon IP Market (~$7.9B 2025 to ~$8.39B 2026). https://www.mordorintelligence.com/industry-reports/global-semiconductor-silicon-intellectual-property-market-industry
3. Market.us, Semiconductor IP Market (CAGR ~5.2%). https://market.us/report/semiconductor-intellectual-property-ip-market/
4. Arm Holdings FY2025 results / SEC 6-K (revenue $4.0B, gross margin ~97%, royalty 54%, op margin low-50s%). https://www.sec.gov/Archives/edgar/data/0001973239/000197323925000010/exhibit992fye25q431-marx25.htm
5. Qualcomm, "Qualcomm Completes Acquisition of Alphawave Semi" (~$2.4B EV, Dec 2025). https://investor.qualcomm.com/news-events/press-releases/news-details/2025/Qualcomm-to-Acquire-Alphawave-Semi/default.aspx
6. GMInsights / MarketsandMarkets, RISC-V market (~$1.76B 2024, ~30%+ CAGR; SiFive, Andes, Codasip leaders). https://www.gminsights.com/industry-analysis/risc-v-market
7. SNS Insider via GlobeNewswire, "Die-to-Die IP Market to Surpass USD 3.72 Billion by 2033" (~$1.80B 2025, ~9.57% CAGR; UCIe ~53.4% share, fastest sub-segment ~9.92%). https://www.globenewswire.com/news-release/2026/01/14/3218798/0/en/Die-to-Die-IP-Market-Size-to-Surpass-USD-3-72-Billion-by-2033-Research-by-SNS-Insider.html
8. Semiconductor Engineering, "Redefining XPU Memory For AI Data Centers Through Custom HBM4" + Synopsys HBM4 PHY/controller IP pages (per-XPU custom HBM4 base dies). https://semiengineering.com/redefining-xpu-memory-for-ai-data-centers-through-custom-hbm4-part-3/
9. EE Times / IndexBox, "RISC-V Targets Data Centers, Edge AI, Space" — RISC-V Summit Europe 2026; "year of RVA silicon" server launches (SiFive P870D, NextSilicon Arbel, Akeana). https://www.eetimes.com/risc-v-targets-data-centers-edge-ai-space/
10. Mordor Intelligence / MarketsandMarkets, RISC-V tech market (~$1.34B 2025, ~41% CAGR to 2031; near-parity with high-end Arm cores projected end-2026). https://www.mordorintelligence.com/industry-reports/risc-v-tech-market
11. CNBC / TechCrunch, US EDA-to-China export curbs imposed May 2025 then lifted Jul 2025 (Synopsys ~16%, Cadence ~12% of revenue from China); Qualcomm-Alphawave UCIe/HBM IP. https://www.cnbc.com/2025/07/03/us-lifts-chip-software-curbs-on-china-amid-trade-truce-synopsys-says-.html
12. Omdia / Arm Newsroom, "Arm Steps Deeper into Silicon" + Arm AGI CPU launch (first own production chip, Neoverse V3, TSMC 3nm, full availability H2 2026; CSS/CSA channel conflict). https://omdia.tech.informa.com/blogs/2026/apr/arm-steps-deeper-into-silicon-implications-for-the-semiconductor-value-chain
13. PatSnap, "Chiplet interconnect tech 2026: UCIe, HBM4 & packaging" (UCIe 2.0 expected 2026-2027, 64Gbps, optical die-to-die option). https://www.patsnap.com/resources/blog/articles/chiplet-interconnect-tech-2026-ucie-hbm4-packaging/
