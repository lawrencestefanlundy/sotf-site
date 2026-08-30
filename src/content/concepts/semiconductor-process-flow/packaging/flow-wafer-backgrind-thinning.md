---
type: concept
slug: flow-wafer-backgrind-thinning
canonical_name: Wafer backgrinding / thinning (process step)
seq: 41
phase: assembly
related_concepts:
- bonding-dicing-equipment
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
neighbors:
- slug: bonding-dicing-equipment
  name: Bonding & Dicing Equipment
  path: /manufacturing/equipment-processes/bonding-dicing-equipment/
  macro: manufacturing
---
> Step 41 of 56 in the semiconductor flow (Assembly). Prev: [Wafer sort / probe (process step)](/semiconductor-process-flow/test-metrology/flow-wafer-sort-probe/) · Next: [Wafer dicing / singulation (process step)](/semiconductor-process-flow/packaging/flow-wafer-dicing-singulation/)

Value here concentrates harder than almost anywhere else in the flow. One company, DISCO, takes the large majority of the grinder equipment spend and then earns a second, recurring stream from the grinding wheels those machines wear through. The tape layer underneath is a separate, smaller razor-blade business owned by four Japanese chemical firms. The public-markets read is the headline; everything else is a footnote.

## What this step does

After a wafer finishes front-end processing and electrical sort, the active circuits sit on the top ~10 micrometres of a disc that is 775 micrometres thick (300mm). Backgrinding removes most of that bulk silicon from the back so the die can fit thin packages, dissipate heat, and stack vertically. A finished device wafer may be thinned to 50-100 micrometres for standard packages and below 50 micrometres (sometimes 20-30) for 3D and HBM stacks. The unit sub-processes inside this step:

- Lamination of a protective backgrind (BG) tape over the device side to shield circuits and hold the wafer flat.
- Coarse grind, then fine grind, on a diamond-wheel grinder to remove bulk silicon.
- Stress relief: dry polish, CMP, or wet etch to remove the grind-damaged subsurface layer that would otherwise crack thin wafers.
- DAF (die-attach film) or dicing-tape mount on the ground side; BG-tape removal.
- For ultra-thin / 3D: TAIKO grinding (a thick rim ~3mm left at the edge for rigidity) or grind-on-a-temporary-bonded-carrier.

## Where it sits and why it matters

This is the gateway into back-end assembly. It is also the step that makes advanced packaging physically possible: you cannot stack 8-12 HBM DRAM die or build a logic-on-logic 3D part without thinning wafers to tens of micrometres and keeping them flat and crack-free. As packaging moves from a commodity afterthought to the main lever on AI-system performance, thinning shifts from cost centre to enabling technology, which is exactly why DISCO's grinder shipments hit records on generative-AI demand [1].

## Equipment market

The wafer grinding equipment market is roughly $4.0bn in 2026, growing to ~$6.7bn by 2035 at about a 6.5% CAGR [2]. That figure spans grinders plus closely adjacent thin-wafer tooling; treat it as order-of-magnitude, since report-mill numbers for this niche vary widely. Backgrinders specifically are a sub-set of that pool.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| DISCO | Japan | ~65-75% grinders | Dominant in grinders + dicers; TAIKO ultra-thin; near-lock on power-semi and HBM thinning [1][3] |
| Tokyo Seimitsu (Accretech) | Japan | ~15-25% | Main grinder/dicer alternative; CMP and metrology too [3] |
| Okamoto Semiconductor | Japan | single digits | Surface/back grinders, niche positions |
| GigaMat / others | US / Asia | small | Specialty and refurbished tooling [3] |

Concentration note: this is one of the most concentrated equipment niches in the entire flow. DISCO holds roughly 70%+ of both grinders and dicing saws, with Accretech the only serious second source and Okamoto a distant third [1][3]. The barrier is process accuracy, yield, and a global service footprint that buyers will not gamble on for HBM thinning [1].

## Materials & consumables

This step consumes two recurring streams. First, DISCO's own grinding wheels and dicing blades: sintered-diamond wheels wear out and are re-bought continuously, which is the razor-blade attach to the installed grinder base and a large reason DISCO's margins hold up. Second, the tape layer, a separate market: protective BG tape and dicing tape (and DAF) made by chemical firms, not equipment vendors.

Dicing and backgrinding tapes together are roughly a $1.2bn market (2023), heading to ~$2.3bn by 2032 at about 7% CAGR [4]; the BG-tape sub-segment alone is several hundred million dollars [5]. Vendors: Mitsui Chemicals Tohcello, Nitto (Nitto Denko), LINTEC, Furukawa Electric, Denka, plus LG Chem and Maxell [4][6]. Tape is pure recurring revenue, consumed per-wafer, qualified into each customer's process and slow to switch.

## Volumes, revenue, profitability

Volume scales with wafers entering assembly: on the order of tens of millions of 300mm-equivalent wafers a year, plus the larger count of 200mm and below for power and analog, where thinning is heaviest. Revenue pools: grinder equipment ~$1-2bn/yr of the broader grinding-tool spend; grinding-wheel and blade consumables a substantial recurring add on top; tapes ~$1.2bn. DISCO group revenue ran ~¥194.5bn for 1H FY2025 (about $1.3bn at recent rates) with operating margin ~38-43% across the two quarters and net margin in the mid-20s [1][7]. Those are extraordinary numbers for capital equipment and reflect the consumables mix plus monopoly pricing. The margin sits with DISCO (equipment + wheels/blades) and, in tape, with the Japanese chemical majors whose product is qualified-in.

## Competitive landscape & value capture

The moat is process know-how compounded by a service/consumables flywheel: every grinder sold pulls a stream of wheel and blade sales, and HBM/power customers will not risk yield by qualifying a second source. Value accrues overwhelmingly to DISCO, secondarily to Accretech, and then to the tape oligopoly. There is essentially no European or seed-stage presence in the core tooling, and tape is locked up by incumbents; this is a study in what an un-disruptable razor-and-blade position looks like, not a sourcing target. Adjacent white space that a seed/angel could touch is metrology and edge-defect inspection for ultra-thin wafers, and carrier/temporary-bond chemistry for sub-50um 3D flows, where the process is still maturing.

## Market drivers, constraints & trends

Net read: the served market accelerates this decade, with the demand mix rotating hard from power/automotive toward AI memory and logic. The cyclicality fear has eased: DISCO's Q4 FY2026 shipments beat guidance, so the structural story (thinning moving from cost step to yield-critical enabler) is in front of the cycle, not behind it.

- **Drivers** — HBM is the swing factor: 16-Hi HBM4 must thin DRAM die to ~30 micrometres to fit 16 layers under JEDEC's 775 micrometre stack height, with HBM4 in production through 2026 and HBM4E in 2027 [8][9]. AI/GPU demand drove DISCO to a record Q3 FY2026 quarter (shipments ¥113.6bn, operating margin 43.3%), then a Q4 (Jan-Mar 2026) that beat guidance at ¥118.2bn on strong AI logic, recovering HBM and solid China demand [10][14]. SiC power devices add a separate, hardware-intensive thinning pull (SiC power market ~25%+ CAGR; SiC near diamond hardness so it eats grinding wheels faster, lifting the consumables attach) [11].
- **Constraints** — Cyclicality is structural even if currently benign: the demand leg now rests heavily on a single AI capex wave, and the prior EV slowdown that cut power-semiconductor investment showed how fast a second leg can disappear [12]. China strength (no visible geopolitical drag yet) is a tail risk if export controls tighten [14]. The position is also un-disruptable from the outside, which caps any new-entrant upside, and report-mill sizing for this niche is unreliable.
- **Trends & inflections to watch** — Hybrid bonding for HBM is postponed: HBM4 stays on microbumps (SK Hynix on MR-MUF), pushing direct copper bonding to HBM4E/HBM5, which keeps grind-and-thin volume central rather than displacing it near-term [8][15]. Glass-core substrates and panel-level packaging are the second structural pull: they need ultra-flat temporary-bond glass carriers for backside thinning, expanding the served carrier/thinning pool, with SK Absolics and a TSMC mini-line targeting 2026 and mass production 2028-2030 [16]. Tripwire 1: a glass-substrate line reaching qualified mass production (SK Absolics 2026, TSMC 2028-2030) would confirm the panel-level thinning leg [16]. Tripwire 2: DISCO posting two more consecutive up quarters into 2H-CY2026 after the Q4 beat would confirm the AI leg has outrun the power-cycle drag [10][14].

## Connections

- [Bonding & Dicing Equipment](/manufacturing/equipment-processes/bonding-dicing-equipment/)
- [Wafer sort / probe (process step)](/semiconductor-process-flow/test-metrology/flow-wafer-sort-probe/)
- [Wafer dicing / singulation (process step)](/semiconductor-process-flow/packaging/flow-wafer-dicing-singulation/)

- Owning idea: **Back End Wafer Prep Equipment**, **Advanced Packaging Market** (back-end wafer-prep growth story).

## Sources

1. SemiAnalysis, "DISCO Corporation: the world leader" and search summary of DISCO FY2025 results (record AI-driven grinder/dicer shipments; ~70%+ share; operating margin 38-43%). https://newsletter.semianalysis.com/p/disco-corporation-the-world-leader
2. Business Research Insights, Wafer Grinding Equipment Market ($4.02bn 2026 to $6.65bn 2035, 6.5% CAGR). https://www.businessresearchinsights.com/market-reports/wafer-grinding-equipment-market-103888
3. Datahorizzon / Verified Market Research, Wafer Grinder Market (DISCO, Tokyo Seimitsu, GigaMat as leaders; concentration). https://datahorizzonresearch.com/wafer-grinder-market-26505
4. Dataintelo, Dicing and Backgrinding Tapes Market ($1.2bn 2023 to $2.3bn 2032, 7.2% CAGR; Nitto, LINTEC, Furukawa, Mitsui, Denka). https://dataintelo.com/report/dicing-and-backgrinding-tapes-market
5. Global Growth Insights / Future Market Report, Back Grinding Tape Market (BG-tape sub-segment several hundred million USD; estimates vary widely). https://www.globalgrowthinsights.com/market-reports/back-grinding-tapes-market-107561
6. Valuates / OpenPR, Wafer Backgrinding Tape and Dicing Tapes (Mitsui Chemicals Tohcello, Nitto, LINTEC, Furukawa, Denka, LG Chem, Maxell). https://reports.valuates.com/market-reports/QYRE-Auto-27E16972/global-wafer-backgrinding-tape-and-dicing-tapes
7. DISCO Corporation, FY2025 Second Quarter Financial Results (¥194.5bn 1H net sales; operating income ¥44.4B 2Q; margins). https://www.disco.co.jp/eg/ir/library/doc/film/20251029.pdf
8. Semiconductor Engineering, "HBM4 Sticks With Microbumps, Postponing Hybrid Bonding" (HBM4 on microbumps; hybrid bonding pushed to HBM4E/HBM5; sub-30um thinning). https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/
9. PatSnap, HBM Technology Landscape 2026 (16-Hi HBM4 thinned to ~30um under 775um JEDEC height; HBM4 production 2026, HBM4E 2027). https://www.patsnap.com/resources/blog/articles/hbm-technology-landscape-2026-market-and-ai-demand/
10. BigGo Finance / JPX TDnet, DISCO Corp Q3 FY2026 Results (9-mo revenue +11.5% to ¥303.8bn; record Oct-Dec shipment value on GPU/HBM; FY guidance ¥419bn). https://finance.biggo.com/news/jpx_tdnet_140120260120535984
11. UniversityWafer / IntechOpen, SiC wafer thinning and power-electronics demand (SiC power market 25%+ CAGR; SiC hardness near diamond accelerates wheel wear). https://www.universitywafer.com/unlocking-sic-wafer-power-electronics.html
12. Investing.com, "Disco reports strong Q1 results, forecasts Q2 shipment decline" (Q2 FY2026 shipment decline on foundry inventory correction / capex slowdown; power-semi appetite down on EV slowdown). https://www.investing.com/news/earnings/disco-reports-strong-q1-results-forecasts-q2-shipment-decline-93CH-4139841
13. Semiconductor Engineering, "Making Hybrid Bonding Better" / industry reporting (SK Hynix completed 12-high HBM hybrid-bonding validation and placed first mass-production order for an inline hybrid-bonding system, April 2026). https://semiengineering.com/making-hybrid-bonding-better/
14. Investing.com, "Disco preliminary Q4 shipment beats guidance on strong AI and China demand" (6 Apr 2026; consolidated implied shipment ¥118.2bn, beat guidance +1.1%, 1.22x consolidated/parent ratio; AI logic strong, HBM recovered, China solid). https://www.investing.com/news/earnings/disco-preliminary-q4-shipment-beats-guidance-on-strong-ai-and-china-demand-93CH-4597858
15. TrendForce, "SK hynix May Stick With MR-MUF for HBM4 16-High amid Fluxless Bonding Evaluation" (13 Jan 2026; HBM4 16-Hi via MR-MUF with DRAM wafers thinned to ~30um; hybrid bonding deferred). https://www.trendforce.com/news/2026/01/13/news-sk-hynix-may-stick-with-mr-muf-for-hbm4-16-high-despite-asmpt-tc-bonder-orders/
16. TrendForce Insights, "Glass Substrates Are Breaking Through the AI Chip Packaging Bottleneck" (glass-core substrate / panel-level packaging timeline: SK Absolics + TSMC mini-line 2026, mass production 2028-2030; needs ultra-flat temporary-bond glass carriers for backside thinning). https://insights.trendforce.com/p/glass-substrate-development
