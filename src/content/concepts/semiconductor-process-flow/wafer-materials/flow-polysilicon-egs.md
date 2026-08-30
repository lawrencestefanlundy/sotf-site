---
type: concept
slug: flow-polysilicon-egs
canonical_name: Polysilicon (electronic-grade silicon) (process step)
seq: 15
phase: wafer
related_concepts:
- materials-process
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
- slug: materials-process
  name: Materials & Process
  path: /materials/advanced-materials/materials-process/
  macro: materials
---
> Step 15 of 56 in the semiconductor flow (Wafer). Prev: [Photomask manufacturing (process step)](/semiconductor-process-flow/frontend/flow-photomask-manufacturing/) · Next: [Crystal growth & ingot (Czochralski/Float-Zone) (process step)](/semiconductor-process-flow/wafer-materials/flow-crystal-growth-ingot/)

## What this step does
This is the raw feedstock step: turn metallurgical-grade silicon (about 98-99% pure, made by carbothermic reduction of quartz) into ultra-pure electronic-grade silicon (EGS) at 11N (99.999999999%) or better, the starting material from which single-crystal ingots are pulled. Without 11N feedstock there is no usable wafer. The sub-processes inside this step:
- Convert metallurgical silicon to a volatile precursor, usually trichlorosilane (TCS, SiHCl3) or silane (SiH4).
- Fractionally distil the precursor to strip boron, phosphorus and metal impurities down to parts-per-trillion.
- Deposit pure silicon back out by chemical vapour deposition: the Siemens process (TCS-CVD onto hot silicon rods) or fluidized-bed reactor (FBR, silane onto seed beads).
- Break, sort, etch and pack into the chunk or granule form the crystal pullers consume.

## Where it sits and why it matters
It is the very front of the wafer chain. Solar and semiconductor polysilicon share chemistry, but the purity gap is enormous: solar cells tolerate 6N-9N, while leading-edge logic and memory need 11N with sub-5-ppta net dopant levels (real "12N" is a marketing fiction per Bernreuter [6]). That gap is the entire investment story. EGS is a tiny, slow, hard-to-qualify niche bolted onto a giant, cyclical, China-dominated solar commodity.

## Equipment market
There is no large independent EGS tool market: the value-capturing producers build and operate proprietary CVD reactors in-house, so capex is captive, not a third-party equipment pool. Estimated merchant reactor/engineering revenue is low hundreds of millions of dollars a year, lumpy with capacity cycles. Siemens TCS-CVD held ~66% of polysilicon output in 2025; FBR/silane is growing ~14% CAGR but is mostly a solar cost play [2]. Shares below are rough estimates of the merchant reactor-and-engineering layer.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Captive (Wacker, Hemlock, Tokuyama in-house) | DE / US / JP | majority | EGS reactors are proprietary, not bought |
| AMS / Poly Plant Project | US | ~20-30% merchant | many CVD reactor generations deployed [5] |
| SST / GTAT-lineage | US | ~10-20% merchant | TCS-CVD and FBR/silane reactor lines [5] |
| Dynatec | NO | small | centrifuge-CVD start-up [5] |

Concentration note: the binding constraint is decades of customer qualification, not tool access. A new entrant cannot buy its way to 11N.

## Materials & consumables
This step consumes metallurgical silicon, hydrogen, chlorine/HCl, and electricity (very energy-intensive), and produces the precursors it then re-deposits. The recurring-revenue layers around it:
- TCS and silane gas: the trichlorosilane market was put at ~$7B in 2025 with polysilicon ~43% of it; major EGS producers (Wacker, OCI, Hemlock) make their own precursor, so merchant TCS skews solar/specialty [4].
- Graphite and graphite-felt reactor internals (hot zones, electrodes, insulation), supplied by SGL Carbon and peers, replaced on a maintenance cycle [4].
- Silica crucibles, quartz, and high-purity HCl.
These consumables and the energy bill are the genuinely recurring spend; the reactor is a one-off.

## Volumes, revenue, profitability
- Volume: semiconductor-grade demand is roughly 33,500 MT in 2025, only ~2.4% of all polysilicon, against ~1.4M+ MT of solar output; solar is 95%+ of the market by volume [1][9]. Total polysilicon capacity hit ~2.26M MT by end-2023 with China at ~93% [3].
- Revenue pool: this is where report-mills mislead. Several put "electronic-grade polysilicon" at $8-10.5B [marketreportsworld, verifiedmarketreports], but 33,500 MT even at a premium $50-150/kg implies a true EGS revenue pool closer to ~$2-5B; treat the $10B figures as conflating broader silicon-materials scope. Rough estimate, flagged.
- Pricing: solar polysilicon collapsed to ~$5/kg (Chinese selling price, ~$1 below cost) vs a ~$24/kg "fair" estimate [7]; EGS commands a large multiple of that, several tens to over a hundred dollars per kg, because of purity and qualification.
- Margins: solar producers are loss-making at the trough; EGS producers earn the margin precisely because they sit out the solar price war. Gross margins on qualified EGS are healthy (estimated 30-50%+ in a normal year) for the few who can make it; the margin is earned by the deposition-and-purification know-how, not the chemistry.

## Competitive landscape & value capture
Tight non-Chinese oligopoly at 11N: Wacker (Germany, largest EGS producer, ~22,000 MT semiconductor output) and Hemlock (US, second largest) anchor supply, with OCI/Tokuyama Malaysia, Tokuyama Japan (~12,500 MT) and Mitsubishi covering the rest [4][6]. These four-to-five firms hold essentially the entire 11N market. China owns ~93% of all polysilicon capacity but, per ITIF and SIA, is "not yet" able to dominate semiconductor grade; closing that gap is an explicit Beijing goal and the key strategic risk [1][8]. Moat: qualification cycles measured in years, energy-cost geography, and process IP. EU/seed-relevant: Wacker (Burghausen) is the European champion and a strategic asset; there is little seed-stage opportunity in making EGS itself (capital-brutal, qualification-gated), the more fundable adjacencies are FBR/silane cost innovation and precursor/graphite consumables.

## Market drivers, constraints & trends
Net read: the EGS served pool grows steadily on AI-driven wafer demand, but the trajectory is hostage to the solar cycle that funds the scale, and any re-rate is policy- and shortage-driven rather than volume-driven.

- **Drivers**
  - Wafer demand is the pull: SEMI reports Q1 2026 silicon-wafer shipments up 13% year-on-year, with AI data centres taking the lion's share and a new shipment record expected by 2028 [10]. Every extra leading-edge wafer needs 11N feedstock, and report-mills already put 2026 semiconductor polysilicon uptake up ~10% [11].
  - Sovereignty/reshoring is opening captive demand: Hemlock secured a ~$325M CHIPS grant for new Michigan EGS capacity (~2026) and the Jan 2026 US-Taiwan reshoring deal pulls more leading-edge fab build onshore, lengthening the qualified-feedstock queue [12][13].
  - Pricing resilience at the top: Wacker reports its hyperpure semiconductor-grade business performing very well with rising volumes into 2026 even as solar prices stay crushed, confirming EGS sits out the price war [14].

- **Constraints**
  - The scale trap: domestic EGS economics depend on high-volume solar-grade output to hit the utilisation that makes 11N affordable; the solar glut and China's ~93% capacity share threaten that base [13][8].
  - Capex and qualification gate growth: new EGS lines cost billions and qualification runs years, so supply cannot flex to a demand spike, risking price volatility not volume [11].
  - Cyclicality overshoot: Bernreuter warns the solar shakeout could overcorrect into a polysilicon shortage by 2028, repeating 2018-20, which would whipsaw feedstock cost for EGS makers [15].

- **Trends & inflections to watch**
  - Capacity-step from the West: Wacker commissioned its >€300M Etching Line Next at Burghausen, lifting top-grade EGS capacity by >50% [16]. Tripwire: a second Western +50%-class EGS line announced (Wacker, Hemlock, OCI) by end-2027 confirms the demand pull is structural.
  - Section 232 re-rate: the US polysilicon Section 232 probe opened 1 July 2025 with a determination due by ~March 2026 [8][17]. Tripwire: a tariff or tariff-rate-quota on imported polysilicon issued in 2026 would re-rate non-Chinese EGS supply security overnight.
  - Shortage flip: Tripwire: Chinese polysilicon spot rising back above ~$10/kg (from ~$4.50/kg end-2024) signals the 2028 shortage thesis arriving early and pricing power returning to qualified producers [15].

## Connections
[Materials & Process](/materials/advanced-materials/materials-process/)

- Owning idea: **Sovereign Electronics Manufacturing** (China-dependence / sovereignty lens).

## Sources
1. EnergyTrend / industry demand, semiconductor-grade ~33,500 MT, 2.4% of demand (2025) — https://www.energytrend.com/news/20241009-48523.html
2. Mordor Intelligence, Polysilicon Market, Siemens ~66% share, FBR CAGR — https://www.mordorintelligence.com/industry-reports/polysilicon-market
3. TaiyangNews / capacity ~2.26M MT, China ~93% (2023) — https://taiyangnews.info/business/china-dominates-2024-global-polysilicon-production
4. GMInsights, Trichlorosilane Market (~$7B 2025, polysilicon ~43%); SGL Carbon graphite — https://www.gminsights.com/industry-analysis/trichlorosilane-market
5. TaiyangNews Polysilicon CVD Reactors market survey (AMS, SST, Dynatec) — https://images.assettype.com/taiyangnews/2024-08-21/30tnntp6/TaiyangNews_Market_Survey_Polysilicon_CVD_Reactors_2017.pdf
6. Bernreuter Research, polysilicon manufacturers ranking + 11N/12N purity — https://www.bernreuter.com/polysilicon/manufacturers/
7. ITIF, China Plans to Dominate a Key Semiconductor Material (prices $24/kg fair, ~$5/kg China; solar 95%+) — https://itif.org/publications/2025/09/08/china-plans-to-dominate-a-key-semiconductor-material/
8. SIA, Polysilicon Section 232 Investigation comments (Aug 2025) — https://www.semiconductors.org/wp-content/uploads/2025/08/Semiconductor-Industry-Association-SIA-Comments-Polysilicon-Section-232-Investigation.pdf
9. Verified Market / report-mill EGS value range $10.5B (flagged as overstated) — https://www.verifiedmarketreports.com/product/electronic-grade-polysilicon-market-size-and-forecast/
10. SEMI, Q1 2026 silicon-wafer shipments +13% YoY, AI data centres lead, record by 2028 — https://www.semi.org/en/semi-press-release/semi-reports-worldwide-silicon-wafer-shipments-increase-13-percent-year-on-year-in-q1-2026
11. Verified Market / intel report-mill, 2026 semiconductor polysilicon uptake ~10%, capex/qualification barriers — https://www.intelmarketresearch.com/semiconductor-grade-silicon-market-9591
12. Hemlock Semiconductor, ~$325M CHIPS grant, Michigan EGS expansion ~2026 — https://www.hscpoly.com/biden-harris-administration-announces-preliminary-terms-with-hemlock-semiconductor-to-significantly-expand-u-s-production-capacity-of-semiconductor-grade-polysilicon-2/
13. Global Policy Watch, Jan 2026 US-Taiwan reshoring deal + semiconductor policy push — https://www.globalpolicywatch.com/2026/02/a-month-in-semiconductor-policy-section-232-measures-bis-rule-and-taiwan-deal-signal-strategic-push/
14. Wacker Chemie FY2025 / 2026 outlook, semiconductor-grade business strong, rising volumes — https://www.wacker.com/cms/media/en/documents/pressrelease-pdf/pm2026/wacker_fy2025.pdf
15. pv magazine / Bernreuter Research, polysilicon glut may reverse into shortage by 2028 — https://www.pv-magazine.com/2025/06/24/polysilicon-glut-may-reverse-into-shortage-by-2028-says-bernreuter-research/
16. Evertiq, Wacker commissions >€300M Etching Line Next, +50% top-grade EGS capacity (Jul 2025) — https://evertiq.com/news/2025-07-22-wacker-commissions-300m-production-line-for-chip-grade-polysilicon
17. Sandler Travis & Rosenberg, Section 232 polysilicon investigation timeline (opened 1 Jul 2025) — https://www.strtrade.com/trade-news-resources/tariff-actions-resources/section-232-investigation-polysilicon
