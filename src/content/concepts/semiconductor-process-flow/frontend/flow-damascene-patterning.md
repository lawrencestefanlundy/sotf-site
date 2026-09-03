---
type: concept
slug: flow-damascene-patterning
canonical_name: Damascene patterning (via/trench) (process step)
seq: 34
phase: beol
related_concepts:
- lithography
- etch-tools
created: 2026-06-20
last_updated: 2026-06-20
tags:
- concept
- process-flow
- semiconductor
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
mention_count: 9
sources_7d: 1
sources_30d: 2
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
- slug: lithography
  name: Lithography
  path: /manufacturing/lithography/lithography/
  macro: manufacturing
- slug: etch-tools
  name: Etch Tools (ALE, plasma etch)
  path: /manufacturing/equipment-processes/etch-tools/
  macro: manufacturing
---
> Step 34 of 56 in the semiconductor flow (BEOL). Prev: [Low-k dielectric (IMD) deposition (process step)](/semiconductor-process-flow/frontend/flow-low-k-imd-deposition/) · Next: [Barrier / liner / seed deposition (process step)](/semiconductor-process-flow/frontend/flow-barrier-liner-seed/)

## What this step does
Copper cannot be etched the way aluminium was, so the back-end-of-line (BEOL) builds wiring "inside-out": you pattern trenches and via holes into the low-k dielectric laid down in Step 33, then fill them with copper later (Steps 35-37) and polish back. This patterning step is the litho-plus-etch half of that inlaid ("damascene") loop, repeated once per metal level. Sub-processes inside it:
- Via litho: print the vertical contact holes that connect this metal layer to the one below.
- Trench litho: print the horizontal wire troughs.
- Hard-mask / etch-stop open and dielectric reactive-ion etch (RIE) to transfer both patterns into the low-k.
- Resist strip and post-etch clean before the barrier/seed step.

Most BEOL levels use a dual-damascene scheme that forms via and trench in one integrated etch sequence (via-first, trench-first, or self-aligned).

## Where it sits and why it matters
This is the single most-repeated patterning loop in the whole flow. A leading-edge logic wafer carries 10-18 metal levels, and the lower ("Mx") levels are the tightest pitches in the device, so they pull EUV or DUV multi-patterning per layer [1][2]. The economic point: litho and etch cost is multiplied by layer count here. Even if any one BEOL mask is cheaper than a critical FEOL gate mask, you are paying for it 12-plus times. As pitches dropped below ~40nm, the lowest metal layers moved from single-exposure immersion to self-aligned double/quadruple patterning (SADP/SAQP) or EUV, which is why BEOL patterning intensity, not just transistor patterning, now drives a meaningful slice of wafer-fab-equipment (WFE) spend [2][6].

## Equipment market
The two tool buckets this step feeds are lithography and dielectric/conductor etch. These are sized as whole-fab segments (you cannot cleanly carve out "BEOL-only" tools), so read these as the pools this step draws on, not a BEOL-isolated number.

Lithography equipment: roughly $30B in 2025, growing ~9-10% CAGR; ASML is the structural monopoly at the leading edge [3][4]. Etch equipment (all dry + small wet tail): broadly $20-30B in 2025 depending on definition, ~7-8% CAGR; the dielectric-etch sub-segment that does damascene trench/via etch is roughly $1.6-4.5B depending on how narrowly it is drawn [5][7]. Treat the wider report-mill etch TAMs with caution.

| Vendor | HQ | Est. share (segment) | Notable |
|---|---|---|---|
| ASML | Netherlands | ~90%+ litho; 100% EUV | Every sub-40nm BEOL layer needing EUV or immersion multi-patterning routes through ASML [3][4] |
| Applied Materials | US (Santa Clara) | ~32% etch | #1 etch overall; strength in dielectric + atomic-layer etch, the core of damascene RIE [5] |
| Lam Research | US (Fremont, CA) | ~28% etch | Dielectric + conductor etch, high-aspect-ratio via etch; ~50% gross margin [5][8] |
| Tokyo Electron | Japan | ~15% etch; #2 litho-track | Tactras etch + the coat/develop track that wraps every litho exposure [5] |
| Canon / Nikon | Japan | DUV i-line/KrF tail | Older/relaxed BEOL layers and mature nodes, not leading-edge BEOL [3] |

Concentration note: extreme on both axes. ASML alone takes ~90%+ of leading-edge litho; Applied + Lam + TEL take ~75% of etch [3][5]. This step is the most concentrated value-capture surface in the entire process flow.

## Materials & consumables
Per-layer recurring spend this step consumes:
- Photoresist + ancillaries (developers, BARCs, EUV underlayers): part of a ~$5-6B photoresist market (2025), ~11% CAGR for the advanced/EUV slice; TOK ~30% share, then JSR, Shin-Etsu, Fujifilm, Dongjin (top 5 ~50%) [9][10].
- Etch specialty gases (fluorocarbons CxFy, NF3, etch chemistries): the semiconductor etching-gas slice is ~$2.5B (2024) heading to ~$4.1B by 2033, ~6% CAGR, inside a ~$16.5B electronic-specialty-gas market; Linde, Air Liquide, Air Products, Merck KGaA, Kanto Denka [11].
- Hard-mask precursors and post-etch clean chemistries.

This is a textbook razor-and-blades layer: tools are bought once, but every wafer through every BEOL level burns resist and gas. Because the loop runs 12-plus times per wafer, materials spend per finished wafer is heavily weighted to BEOL even though any single dose is cheap.

## Volumes, revenue, profitability
Unit driver: metal-layer-passes. A wafer with ~15 BEOL levels goes through this litho-plus-etch loop ~15 times; at industry volumes north of 200M 300mm-equivalent wafers a year, that is billions of patterned-layer-passes annually, the bulk of recurring litho/etch consumable demand. Revenue pool: the tool spend sits inside the ~$30B litho and ~$20-30B etch markets [3][5]; the BEOL-attributable share is large but not separately reported. Margins: the equipment layer earns it. ASML runs ~52-56% gross margin; Lam ~50% gross, ~34% operating; both at or above the WFE average [4][8]. The materials layer (resist, gas) is lower-margin but stickier and recurring. The fab/foundry that runs the step captures the least per-unit margin on the patterning itself; value concentrates upstream in the tool and chemistry suppliers.

## Competitive landscape & value capture
Moat: this is the deepest moat surface in the flow. EUV is a literal monopoly (ASML), and leading-edge etch is a three-firm oligopoly with decades of process-recipe co-development locked into each foundry's BEOL flow. Switching an etch tool mid-node is near-impossible, which is why incumbents compound. Value accrues to (1) ASML for the exposure, (2) Applied/Lam/TEL for the etch, (3) the Japanese/European chemistry majors for the recurring consumable. There is essentially no seed-stage entry point into mainstream leading-edge BEOL patterning; the only adjacent EU-relevant names are niche/specialty etch (Oxford Instruments, SPTS/KLA in the UK for compound-semi, MEMS, power) and the chemistry primes (Merck KGaA, Air Liquide).

## Market drivers, constraints & trends
Net read: the served pool grows with WFE through 2030, but this specific step faces an architectural inflection that splits its future into two divergent pools rather than one smooth ramp.

- **Drivers**
 - AI/HPC layer-count inflation: leading-edge logic is pushing 15-18+ metal levels and every level re-runs the litho-plus-etch loop, so wafer-fab equipment growth compounds through this step directly [1][2].
 - Advanced packaging is a new copper-damascene demand pool: dual-damascene now builds sub-2um RDL, interposers and hybrid-bonding interfaces, and the packaging market is rising from ~$51.6B (2025) to ~$57.5B (2026), with hybrid bonding ~$165M (2025) to ~$634M (2032), 21.2% CAGR [15][16].
 - High-NA EUV pull-through: Intel installed two EXE:5200 units by late-2025; Samsung/TSMC secured tools for 2026-2028 ramps, expanding the leading-edge litho pool this step feeds [14].

- **Constraints**
 - Copper RC wall: below ~17nm line width, copper resistivity (grain/surface scattering) caps performance, threatening the classic dual-damascene scheme at the tightest BEOL levels [12].
 - High-NA partly deflates litho intensity: it removes 40+ process steps on critical layers vs multi-patterning, so more exposures-per-layer is not guaranteed [14].
 - Capex intensity + cyclicality + extreme supplier concentration leave fabs little patterning-margin to capture (see above).

- **Trends & inflections to watch**
 - Damascene-to-subtractive shift: tight levels move to direct-etched ruthenium/molybdenum (semi-damascene + airgaps, ~25% capacitance cut at <=25nm pitch), shrinking dual-damascene tool/chemistry demand but growing direct-metal-etch demand. Tripwire: TSMC A14 subtractive-Ru in volume production, slated 2028 [12][13].
 - DRAM/3D NAND molybdenum interconnect adoption "moving quickly" diversifies the metal-etch pool. Tripwire: first HVM Mo interconnect node disclosed by a memory maker [12].
 - Panel/2.5D RDL scale-up. Tripwire: a foundry announcing a sub-2um damascene RDL line at panel format [15].

## Connections
[Lithography](/manufacturing/lithography/lithography/) · [Etch Tools (ALE, plasma etch)](/manufacturing/equipment-processes/etch-tools/) · thesis **Lithography Patterning Market**

## Sources
1. imec, "First EUV lithography high-volume manufacturing solution for N5 BEOL" — https://www.imec-int.com/en/imec-magazine/imec-magazine-march-2017/first-euv-lithography-high-volume-manufacturing-solution-for-n5-beol
2. Semiconductor Digest, "Scaling the BEOL: A Toolbox Filled with New Processes" (metal-layer count 3-6 local, up to ~15 total) — https://www.semiconductor-digest.com/scaling-the-beol-a-toolbox-filled-with-new-processes-boosters-and-conductors/
3. Fortune Business Insights, lithography equipment market (~$30B 2025, ~9.7% CAGR; ASML EUV dominance) — https://www.fortunebusinessinsights.com/lithography-equipment-market-110434
4. Yahoo Finance / GM Insights, ASML position + 2025 gross margin 54-56% — https://www.gminsights.com/industry-analysis/lithography-equipment-market
5. Mordor Intelligence / Precedence Research, etch equipment market + Applied 32% / Lam 28% / TEL 15% shares (~75% top 3) — https://www.precedenceresearch.com/semiconductor-etch-equipment-market
6. imec, "EUV lithography: weighing the options" (SADP/SAQP/LELE for tight BEOL pitch) — https://www.imec-int.com/en/imec-magazine/imec-magazine-june-2019/euv-lithography-weighing-the-options-for-future-logic-and-memory-applications
7. Mordor Intelligence, dielectric etchers market (~$1.6B 2025 → ~$2.36B 2030, 8.1% CAGR) — https://www.mordorintelligence.com/industry-reports/dielectric-etchers-market
8. Lam Research FY2025 8-K, gross margin ~50%, operating ~34% — https://www.sec.gov/Archives/edgar/data/0000707549/000070754925000051/lrcx_exhibitx991xq3x2025.htm
9. Grand View Research, photoresist market (~$5.19B 2025) — https://www.grandviewresearch.com/industry-analysis/photoresist-market-report
10. GM Insights, photoresist chemicals for advanced lithography (~$6.1B 2025 → $15.6B 2034, 11% CAGR; TOK ~30%) — https://www.gminsights.com/industry-analysis/photoresist-chemicals-for-advanced-lithography-market
11. Market Research Future + Verified Market Reports, electronic specialty gases (~$16.5B 2025) + semiconductor etching gas (~$2.5B 2024 → $4.1B 2033, 6.1% CAGR; Linde, Air Liquide, Air Products, Merck KGaA) — https://www.marketresearchfuture.com/reports/electronic-specialty-gases-market-39391
12. Semiconductor Engineering, "Interconnects Approach Tipping Point" (Cu RC wall <17nm; hybrid Cu/Ru/Mo; damascene→subtractive shift; Mo in DRAM/3D NAND moving quickly) — https://semiengineering.com/interconnects-approach-tipping-point/
13. Semiconductor Engineering "Ruthenium Interconnects On Tap" + 36Kr/Vik's Newsletter (subtractive-Ru semi-damascene with airgaps, ~25% line-to-line capacitance reduction at ≤25nm pitch; TSMC A14 production 2028; Intel HVM-compatible subtractive Ru demonstrated) — https://semiengineering.com/ruthenium-interconnects-on-tap/
14. FinancialContent, "The High-NA Frontier: ASML Solidifies the Sub-2nm Era" (High-NA removes 40+ process steps on critical layers; Intel two EXE:5200 installed late-2025; Samsung EXE:5200B early-2026; TSMC A14P 2027-2028) — https://www.financialcontent.com/article/tokenring-2025-12-18-the-high-na-frontier-asml-solidifies-the-sub-2nm-era-as-euv-adoption-hits-critical-mass
15. 3D InCites / IMAPS, "Copper Dual Damascene for Wafer-Level Packaging" (dual-damascene now builds sub-2um RDL, interposers, hybrid-bonding interfaces) — https://www.3dincites.com/2025/08/copper-dual-damascene-for-wafer-level-packaging-enabling-reliable-high-density-interconnects/
16. MarketsandMarkets, hybrid bonding (~$164.7M 2025 → $633.9M 2032, 21.2% CAGR) + advanced packaging (~$51.62B 2025 → $57.46B 2026) — https://www.marketsandmarkets.com/Market-Reports/hybrid-bonding-market-2641237.html
