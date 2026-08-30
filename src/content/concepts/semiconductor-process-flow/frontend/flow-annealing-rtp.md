---
type: concept
slug: flow-annealing-rtp
canonical_name: Annealing / rapid thermal processing (process step)
seq: 26
phase: feol
related_concepts:
- semiconductor-materials-equipment
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
- slug: semiconductor-materials-equipment
  name: Semiconductor Materials & Equipment
  path: /manufacturing/equipment-processes/semiconductor-materials-equipment/
  macro: manufacturing
---
> Step 26 of 56 in the semiconductor flow (FEOL). Prev: [Ion implantation (doping) (process step)](/semiconductor-process-flow/frontend/flow-ion-implantation/) · Next: [CVD / PECVD deposition (process step)](/semiconductor-process-flow/frontend/flow-cvd-pecvd/)

## What this step does
After ions are driven into the silicon (Step 25), the lattice is left damaged and the dopants sit in the wrong places, electrically inert. Annealing heats the wafer to repair the crystal and "activate" the dopants by moving them onto lattice sites where they conduct. The hard constraint at advanced nodes is the thermal budget: you must heat enough to activate but not so long that dopants diffuse and blur the tiny junctions. That tension is the entire reason this step has fragmented into ever-shorter heating regimes. Sub-processes inside the step:
- Spike anneal (rapid thermal anneal, RTA): lamp-based, ramp to ~1000-1200 degC and cool in seconds. The workhorse for dopant activation and general thermal treatment.
- Millisecond anneal (laser spike / dynamic surface anneal): a scanned laser or flash heats only the near-surface for milliseconds, giving high activation with almost no diffusion.
- Nanosecond / melt laser anneal: ultra-short pulses for the most diffusion-sensitive leading-edge junctions and some memory layers.
- Furnace / batch anneal: slower, many wafers at once, for less budget-sensitive steps (oxide densification, contact alloying).

## Where it sits and why it matters
Annealing is the payoff step for implant: without it the implanted dopants do nothing. As nodes shrink from FinFET to gate-all-around (2nm-class) and as DRAM/HBM stacks tighten, the allowable thermal budget keeps falling, which pushes the mix from furnaces toward spike and then toward laser/millisecond tools. The newest anneals (laser, nanosecond) are where the unit economics and the growth sit, because they are the only way to activate dopants without wrecking the geometry the lithography just printed.

## Equipment market
RTP / thermal-anneal equipment was roughly USD 0.83bn in 2024 and is cited at USD 1.3-1.77bn for 2025 across reports, growing ~7-8% CAGR to ~USD 3.9bn by 2035 [1][2][6]. Treat the absolute level as a wide range; report-mill TAMs disagree because some bundle RTCVD and furnace anneal in and others do not. RTA is ~42% of the RTP category and annealing ~56% of applications [2]. The faster, more interesting slice is laser annealing, sized at ~USD 0.9-1.5bn for 2025-2026 at ~10% CAGR [7].

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Applied Materials | USA | ~28% RTP overall; ~21% of front-end laser-anneal tools (~265 units) | Vantage Vulcan spike RTP + dynamic surface anneal (DSA) laser; broadest line [3][7] |
| Kokusai Electric | Japan | top-3 (with AMAT + TEL ~77% of RTP combined) | Lamp-based RTA + batch furnaces, strong in memory; KKR-owned [1] |
| Tokyo Electron (TEL) | Japan | top-3; ~40-50% of Japan diffusion procurement | Single-wafer RTP + batch furnaces + oxidation [1] |
| Veeco | USA | leader in laser spike anneal (LSA) at leading-edge logic | LSA-101, NSA nanosecond; Tool of Record at 2nm GAA nodes; entering DRAM/HBM [4][5] |
| SCREEN Semiconductor | Japan | >25% of front-end IC laser-anneal tools (>310 units) | Largest installed laser-anneal base by unit count [7] |
| Mattson / Beijing E-Town | China/USA | minority | Lamp RTP; part of the ~77% concentration figure [1] |

Concentration is high: three names (AMAT, TEL, Kokusai) take ~77% of broad RTP [1], and laser anneal is effectively a three-way race (AMAT, Veeco, SCREEN ~45% combined, plus Asian regional tools) [7].

## Materials & consumables
Anneal is light on materials versus deposition or etch, which is why the value sits in the tool, not the consumable. Recurring spend is: tungsten-halogen / arc lamps and laser source modules (finite-life, periodic replacement), quartz chambers and showerheads, susceptors/edge rings, plus process gases (N2, O2, H2, NH3, and forming-gas blends). There is a genuine recurring-revenue tail in lamps, laser optics refurbishment, and service contracts on the installed base, but it is a fraction of tool revenue rather than a separate large pool. No single dominant consumables vendor defines this step; the OEMs and general industrial-gas suppliers (Air Liquide, Linde) capture most of it.

## Volumes, revenue, profitability
The revenue pool is the ~USD 1-1.8bn equipment market plus a modest service/parts tail; this is one of the smaller front-end equipment steps, perhaps 2-3% of total wafer-fab equipment (WFE, ~USD 110bn). Units are low and high-value: a leading-edge laser-anneal tool runs into the high single-digit millions of dollars, so a handful of wins (Veeco's 2nm GAA Tool-of-Record placements, DRAM/HBM evaluations) move a vendor's quarter [4][5]. Margins are characteristic of concentrated semicap: gross margins in the ~40-45% range and operating margins in the ~20-25% range for the specialist anneal players (Veeco group-level FY2024 revenue USD 717m, semi segment USD 467m) [5]. The margin is earned by the equipment OEM, not by any materials layer.

## Market drivers, constraints & trends
Net read: the broad RTP base grows with WFE (low-to-mid single digits, cyclical), but the laser/millisecond slice re-rates faster as thermal budget collapses, so the served market accelerates around the leading-edge tools while the furnace tail flattens.

- **Drivers**
  - 2nm GAA ramp is the core pull: dopant activation at gate-all-around mandates sub-millisecond cycling, and TSMC/Samsung are expanding excimer/laser-anneal capacity for it; leading-edge foundry/logic capex is forecast +5.5% in 2026 [8][10]. Veeco's LSA is Tool-of-Record at 2nm GAA, which compounds into volume reorders as the node ramps [4].
  - Memory is the new adjacency: a tier-1 memory maker selected Veeco LSA for advanced DRAM/HBM evaluation (Dec 2025), with follow-on orders flagged for 2027+; HBM is growing ~30% CAGR to ~USD 100bn by 2030, opening a second laser-anneal demand pool beyond logic [6][9].
  - SiC power for EVs adds a separate served market: thin-wafer (<=80um) SiC backside ohmic contacts can no longer use furnace anneal, forcing pulsed laser anneal; SiC power devices grow >30% CAGR toward ~USD 9bn by 2028 [11].

- **Constraints**
  - Cyclicality and capex concentration: this is ~2-3% of WFE (USD ~135bn in 2026, +9%), so a downcycle or a few delayed fab decisions swing the small unit count hard [8].
  - China exposure unwinds: China falls to ~31% of WFE in 2026 from 36% in 2024 as export controls bite and domestic tools substitute; the lamp-RTP installed base most exposed to mature-node China is the softest part of the pool [8].
  - Incumbent + qualification lock-in caps new entrants: recipes are co-developed and node-certified, so value stays with AMAT/Veeco/SCREEN/TEL and there is no commoditisation upside for a challenger [4].

- **Trends & inflections to watch**
  - Implant-anneal consolidation: the Axcelis-Veeco merger (stockholders approved Feb 2026) is expected to close H2 2026 pending China SAMR clearance. Tripwire: a confirmed close announcement in 2026 forms the 4th-largest US WFE supplier and bundles implant+anneal pricing [12].
  - Memory crossover from eval to HVM. Tripwire: a Veeco DRAM/HBM follow-on production order booked in 2027 would confirm the second demand pool is real, not just an R&D placement [9].
  - Furnace-to-laser mix shift as budgets fall. Tripwire: laser-anneal sustaining ~10% CAGR vs ~7-8% for broad RTP through 2027 would confirm the leading-edge slice is doing the work [7][8].

## Connections
[Semiconductor Materials & Equipment](/manufacturing/equipment-processes/semiconductor-materials-equipment/)

- Owning idea: **Deposition Materials Process Market** (materials/process tool layer).

## Sources
1. Business Research Insights / market reports — RTP equipment ~USD 830m (2024), ~7.2% CAGR; AMAT ~28% share, AMAT+TEL+Kokusai ~77%. https://www.businessresearchinsights.com/market-reports/rapid-thermal-processing-equipment-market-105663
2. SNS Insider — RTP equipment USD 1.77bn (2025) to USD 3.90bn (2035), 8.27% CAGR; RTA 42% of type, annealing 56% of application. https://www.globenewswire.com/news-release/2026/03/13/3255288/0/en/Rapid-Thermal-Processing-RTP-Equipment-Market-Size-to-Hit-USD-3-90-Billion-by-2035-SNS-Insider.html
3. Applied Materials — Vantage Vulcan RTP advanced spike anneal (up to ~1200 degC in seconds). https://pradeepchakraborty.wordpress.com/2011/07/02/applied-vantage-vulcan-rtp-better-side-of-anneal/
4. Veeco — Laser Annealing Platform named Production Tool of Record at leading-edge / gate-all-around logic. https://www.veeco.com/company/news/veecos-laser-annealing-platform-named-production-tool-of-record-for-new-applications-at-leading-edge-logic-manufacturers/
5. Semiconductor Today — Veeco FY2024 revenue USD 717.3m, semi segment USD 467m, record laser-annealing revenue. https://www.semiconductor-today.com/news_items/2025/mar/veeco-240325.shtml
6. Veeco — LSA selected by a memory company for advanced DRAM/HBM evaluation (Dec 2025). https://www.globenewswire.com/news-release/2025/12/01/3197107/0/en/Veeco-s-Laser-Spike-Annealing-LSA-System-Selected-by-Leading-Semiconductor-Memory-Company-for-Advanced-DRAM-Evaluation.html
7. Market Report Analytics / MarkWide — laser-annealing equipment ~USD 1.5bn (2025), ~10% CAGR; SCREEN >25% (>310 units) and AMAT ~21% (~265 units) of front-end laser-anneal tools. https://www.marketreportanalytics.com/reports/laser-annealing-equipment-369696
8. SEMI — global WFE +9.0% to USD 135.2bn in 2026; foundry/logic leading-edge capex +5.5% toward 2nm GAA HVM; China share falling to ~31% of WFE (2026) from 36% (2024) on export controls. https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-projected-to-reach-a-record-of-156-billion-dollars-in-2027-semi-reports
9. Veeco / StockTitan — LSA selected by a tier-1 memory company for advanced DRAM/HBM evaluation (Dec 2025); ~1yr eval, follow-on orders flagged 2027+; HBM ~30% CAGR to ~USD 100bn by 2030 (Yole). https://www.stocktitan.net/news/VECO/veeco-s-laser-spike-annealing-lsa-system-selected-by-leading-bfvtc38md13f.html
10. MarkWide Research — TSMC/Samsung expanding excimer laser-anneal capacity for gate-all-around; dopant activation at GAA mandates sub-millisecond thermal cycling; SCREEN LA-3500 dual-beam for 2nm ultra-shallow junctions. https://markwideresearch.com/laser-annealing-system-market
11. Electro Optics / Credence Research — thin-wafer (<=80um) SiC backside ohmic contacts require pulsed laser anneal (furnace no longer feasible); SiC power devices >30% CAGR to ~USD 9bn by 2028 on EV demand. https://www.electrooptics.com/article/sic-power-devices-how-achieve-optimal-ohmic-contact-formation-laser-annealing
12. Semiconductor Today / SEC — Axcelis-Veeco merger; stockholders approved 6 Feb 2026, expected close H2 2026 pending China SAMR approval; forms 4th-largest US WFE supplier bundling implant + anneal. https://www.semiconductor-today.com/news_items/2025/oct/veeco-axcelis-021025.shtml
