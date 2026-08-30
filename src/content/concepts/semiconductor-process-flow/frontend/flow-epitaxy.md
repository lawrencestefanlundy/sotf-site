---
type: concept
slug: flow-epitaxy
canonical_name: Epitaxial deposition (epi) (process step)
seq: 18
phase: wafer
related_concepts:
- mocvd-mbe
- silicon-germanium
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
- slug: mocvd-mbe
  name: MOCVD / MBE
  path: /manufacturing/equipment-processes/mocvd-mbe/
  macro: manufacturing
- slug: silicon-germanium
  name: Silicon Germanium
  path: /materials/substrates/silicon-germanium/
  macro: materials
---
> Step 18 of 56 in the semiconductor flow (Wafer). Prev: [Wafer slicing, lapping & polishing (process step)](/semiconductor-process-flow/wafer-materials/flow-wafer-slicing-polishing/) · Next: [Wafer foundry / fabrication services (process step)](/semiconductor-process-flow/frontend/flow-foundry-fabrication-services/)

## What this step does
Epitaxy grows a thin, single-crystal layer on top of the polished wafer so its atoms line up with the substrate lattice underneath, giving a near-perfect crystal surface for the active devices. It is the bridge between the bare wafer and the fab: the epi layer (and any strained or compound layer on top) is where the transistors actually live. Sub-processes inside it:
- Silicon epi: a lightly doped Si layer on a Si wafer (the workhorse for power, analog, CMOS image sensors and the channel of advanced logic).
- SiGe / strained-Si: depositing silicon-germanium to strain the channel and lift carrier mobility, central to FinFET and gate-all-around source-drain.
- Selective / source-drain epi: growing material only in defined windows for advanced-logic transistors (Applied's Xtera, ASM's Intrepid).
- Compound epi (MOCVD/MBE): GaN, GaAs, InP, SiC layers grown atom-layer by atom-layer for power, RF and photonics; see [MOCVD / MBE](/manufacturing/equipment-processes/mocvd-mbe/).
- In-situ doping and post-epi metrology (thickness, defect, dopant uniformity).

## Where it sits and why it matters
Epi is the first place crystal quality becomes a device-yield problem rather than a wafer-supplier problem. A single dislocation or thickness error in the epi layer propagates straight into transistor leakage and breakdown. For advanced logic, SiGe source-drain epi is the lever that has kept Moore's law alive across FinFET and into gate-all-around, so the leading-edge epi tool is a node-enabling chokepoint. For power and RF, the epi layer essentially is the product: a GaN-on-Si or SiC epi wafer is sold as a value-added intermediate at a large multiple of the bare substrate.

## Equipment market
Silicon epi equipment is roughly US$1.5B in 2024, forecast to US$2.5-3.2B by 2030 at a 9-13% CAGR, driven by gate-all-around source-drain, DRAM and advanced packaging [3]. Compound epi splits into two pools: SiC epi equipment is ~US$1.25-1.32B in 2024 growing 15-18% CAGR [1], and MOCVD systems (GaN/GaAs/InP) are a few hundred million per year and cyclical with LED and power demand [2]. Treat the report-mill point estimates as directional; the SEMI/Gartner-style splits are firmer on direction than on the decimal.

| Vendor | HQ | est. share | notable |
|---|---|---|---|
| Applied Materials | US | leads Si epi (historically ~50%+; >50% of GAA epi equipment) | Centura / Epi Prime / Xtera selective epi; node-enabling for 2nm GAA [4][5] |
| ASM International | NL | targets >30% Si epi by 2025 | Intrepid ES/ESA single-wafer epi; acquired LPE (Italy) for SiC CVD [3][6] |
| Aixtron | DE | ~70-75% of MOCVD | compound-semi MOCVD (GaN/GaAs/InP); ~1/3 of SiC CVD; €630M FY24 revenue [2][6] |
| Veeco | US | co-leader MOCVD with Aixtron | Propel GaN-on-Si MOCVD, As/P and LED; ~$630M FY24 revenue [2] |
| Tokyo Electron / Nuflare | JP | minority | Si epi and SiC epi tools |
| AMEC / Naura / JSG | CN | rising in China | state-backed local-substitution challengers in MOCVD and SiC epi [6] |

Concentration note: silicon epi is effectively an Applied-plus-ASM duopoly at the leading edge; MOCVD is an Aixtron-Veeco duopoly (>90% pre-2017, now ~60% of MOCVD with the top three including Taiyo Nippon Sanso) being eroded by Chinese entrants [2][6].

## Materials & consumables
Epi consumes high-purity precursor gases and organometallics on every wafer pass, so this is a genuine recurring-revenue layer rather than a one-off tool sale. Silicon epi runs on chlorosilanes and silane (trichlorosilane TCS, dichlorosilane DCS, silane SiH4, plus dopant hydrides) [7]. Compound epi runs on organometallics (trimethylgallium TMGa, trimethylindium TMIn, trimethylaluminium TMAl) and hydride gases (arsine, phosphine, ammonia); merchant-grade TMGa transacts at ~US$2,500-4,500/kg and TMIn ~US$3,000-6,000/kg in 2026 [7]. Other consumables: SiC-coated graphite susceptors, quartzware, showerheads and filters. Supply concentrates in specialty-gas majors (Linde, Air Liquide, Air Products) as blenders/distributors plus producers like Wacker, Shin-Etsu, SK and Nippon Sanso [7]. The materials pool is smaller than the tool pool but stickier, qualified into each process recipe and switched only with painful requalification.

## Volumes, revenue, profitability
Every advanced-logic and most power/RF wafers see at least one epi step, so unit throughput tracks total wafer starts (high tens of millions of wafers/year industry-wide). The revenue pool is the tool sale (silicon epi ~$1.5B, SiC epi ~$1.3B, MOCVD a few hundred million) plus a recurring precursor/parts annuity. Margins: the equipment makers earn the fattest cut. Applied Materials runs ~47-48% gross and ~29-30% operating margin company-wide; ASM ~50%+ gross; Aixtron historically 40-45% gross but highly cyclical (compound-epi demand swings hard with LED and power capex). Specialty-gas precursors are lower gross (commodity-ish chemistry, ~20-35%) but extremely durable. The margin sits with whoever owns the qualified recipe: the tool vendor at install, the gas major across the tool's life.

## Competitive landscape & value capture
Value capture is bimodal. At the leading edge, silicon/SiGe epi is a two-horse race (Applied, ASM) protected by a deep moat: the tool must hit angstrom-scale thickness and defect targets co-developed with the foundry over years, so switching is near-impossible mid-node. In compound epi, Aixtron and Veeco hold a structural MOCVD duopoly, but it is the most contestable of the deposition niches because Chinese local-substitution (AMEC, Naura, JSG) is funded to break it. The other place value accrues is merchant epi wafers: houses like IQE (Wales) sell finished GaN/GaAs/InP epi wafers, capturing the layer's value without owning a fab.

## Market drivers, constraints & trends
Net read is two engines on different clocks: the leading-edge silicon/SiGe epi pool is accelerating, while compound (SiC) epi is in a cyclical trough through ~2027-2028, so the blended served market grows but is lumpy.
- **Drivers** — GAA at 2nm makes epi step-intensive: the shift to gate-all-around at 2nm and below lifts demand for single-wafer Si epi and high-Ge SiGe selective source-drain, the lever keeping leading-edge logic moving [8][9]. HBM is a wafer-intensity multiplier: HBM consumes ~3x the wafer capacity per GB of DDR5 and reached ~23% of DRAM wafers in 2026, with HBM4 (16-die) volume in late 2026/2027, pulling more epi-bearing wafer starts [10]. Data-centre power: the GaN device market is forecast to grow ~35-42% CAGR to ~$2.5-2.9B by 2030 as AI power-supply demand hits the "power wall," all of it MOCVD epi-borne [11].
- **Constraints** — SiC epi is the drag: upstream SiC utilisation fell to ~50% in 2025 (devices ~70%), overcapacity persists to 2027-2028, and SiC equipment is forecast at roughly -7% to -11% CAGR through 2030 [12]. China local-substitution caps Western share: Chinese players held ~40% of SiC wafer/epiwafer capacity by 2024 and back local equipment buys, eroding the Aixtron-ASM-Veeco hold on compound epi [12]. Capex cyclicality: compound-epi (MOCVD) demand still swings hard with LED, EV and power capex.
- **Trends & inflections to watch** — 3D DRAM is the next epi bonanza: it needs 100+ Si/SiGe superlattice bilayers per stack (IMEC has shown up to ~120-300 layers on 300mm), but mass production is ~2032-2035, so the datable tripwire is a memory maker placing its first high-volume superlattice-epi tool order [13]. GaN-on-Si 200mm to 300mm transition (300mm projected >80% of GaN demand by 2030); tripwire = a second Propel300-class 300mm GaN MOCVD order from a power IDM after Veeco's Nov 2025 win [11][14]. SiC recovery tripwire = upstream utilisation back above ~80% plus 8-inch platform ramp signalling the 2027-2028 turn [12].

## Connections
- [MOCVD / MBE](/manufacturing/equipment-processes/mocvd-mbe/) - the compound-epi growth techniques (MOCVD, MBE) that this step uses for GaN/GaAs/InP/SiC.
- [Silicon Germanium](/materials/substrates/silicon-germanium/) - the SiGe / strained-Si epi that enables advanced-logic source-drain.
- **Gan On Si Substrate Epi** - thesis on GaN-on-Si epi wafers as the value-added intermediate for power.
- [Wafer slicing, lapping & polishing (process step)](/semiconductor-process-flow/wafer-materials/flow-wafer-slicing-polishing/) - prior step that delivers the polished substrate epi grows on.
- [Wafer foundry / fabrication services (process step)](/semiconductor-process-flow/frontend/flow-foundry-fabrication-services/) - next step, where the epi wafer enters device fabrication.

## Sources
1. Verified Market Reports / Growth Market Reports, SiC Epitaxy Equipment Market (~$1.25-1.32B 2024, 15-18% CAGR). https://www.verifiedmarketreports.com/product/silicon-carbide-sic-epitaxy-equipment-market/ ; https://growthmarketreports.com/report/sic-epitaxy-equipment-market
2. Market Report Analytics / Intel Market Research, MOCVD equipment market & shares (Aixtron+Veeco; top three ~60%; FY24 revenues ~€630M / ~$630M). https://www.marketreportanalytics.com/reports/mocvd-59003 ; https://www.intelmarketresearch.com/semiconductor-mocvd-equipment-market-32310
3. ASM International Investor Day 2025 / Bits&Chips, Epi market $1.5B (2024) to $2.5-3.2B (2030), 9-13% CAGR; ASM >30% Si epi target. https://www.globenewswire.com/news-release/2025/09/23/3154400/0/en/ASM-hosts-Investor-Day-provides-new-2030-targets-revises-H2-2025-outlook.html ; https://bits-chips.com/article/asm-projects-doubling-revenues-by-2030/
4. Applied Materials, Centura Epi / Xtera epitaxy & GAA leadership. https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-extends-leadership-position-epitaxy ; https://www.appliedmaterials.com/us/en/semiconductor/markets-and-inflections/advanced-logic/gaa.html
5. GMInsights, Gate-All-Around transistor market (AMAT expects >50% of GAA equipment). https://www.gminsights.com/industry-analysis/gate-all-around-gaa-transistor-market
6. Valuates / Jason's Chips / eeNews, SiC epi competitive set (Aixtron, LPE/ASM, Epiluvac, AMEC, Naura); Aixtron ~70-75% MOCVD, ~1/3 SiC CVD; Turin plant. https://reports.valuates.com/market-reports/QYRE-Auto-3A13394/global-silicon-carbide-sic-epitaxy-equipment ; https://www.eenewseurope.com/en/aixtron-selects-turin-for-chip-making-equipment-factory/
7. IndexBox / SkyQuest, epitaxy precursor chemicals (TMGa ~$2.5-4.5k/kg, TMIn ~$3-6k/kg; TCS/DCS/silane; Linde/Air Liquide/Air Products/Wacker/Shin-Etsu). https://www.indexbox.io/store/asia-pacific-epitaxy-precursor-chemicals-market-analysis-forecast-size-trends-and-insights/ ; https://www.skyquestt.com/report/trichlorosilane-market
8. TechInvestments / BALD Engineering, GAA at 2nm+ lifts single-wafer ALD and Si epi demand. https://www.techinvestments.io/p/atomic-layer-deposition-next-gen ; https://www.blog.baldengineering.com/search/label/Semiconductor
9. arXiv 2602.07925, high-Ge-content SiGe selective epitaxy for gate-all-around source/drain. https://arxiv.org/abs/2602.07925
10. Tom's Hardware / Tech-Insider, HBM ~3x wafer capacity/GB vs DDR5; ~23% of DRAM wafers 2026; HBM4 16-die late 2026/2027. https://www.tomshardware.com/pc-components/ram/hbm-is-eating-your-ram ; https://tech-insider.org/memory-chip-shortage-2026-ai-consumer-electronics/
11. Yole Power GaN 2025 / Semiconductor Today / Power Electronics News, GaN device market ~35-42% CAGR to ~$2.5-2.9B by 2030; data-centre "power wall"; 300mm >80% of GaN demand by 2030. https://www.yolegroup.com/product/report/power-gan-2025/ ; https://www.powerelectronicsnews.com/gan-goes-big-how-300-mm-wafers-are-powering-the-next-generation-of-data-centers/
12. Yole / Semiconductor Today, Power SiC overcapacity: upstream ~50% / device ~70% utilisation 2025, downturn to 2027-2028, SiC equipment ~-7% to -11% CAGR through 2030, China ~40% of SiC wafer/epiwafer capacity by 2024, 8-inch ramp drives the turn. https://www.semiconductor-today.com/news_items/2025/dec/yole-181225.shtml
13. SemiEngineering / Tom's Hardware, 3D DRAM needs 100+ Si/SiGe superlattice bilayers (IMEC up to ~120-300 layers on 300mm); mass production ~2032-2035. https://semiengineering.com/epitaxial-growth-of-up-to-120-si-sige-bilayers-in-view-of-3d-dram-applications-imec-ghent-univ/ ; https://www.tomshardware.com/pc-components/dram/sk-hynix-reveals-dram-development-roadmap-through-2031-ddr6-gddr8-lpddr6-and-3d-dram-incoming
14. Semiconductor Today, Veeco Propel300 300mm GaN MOCVD order from GaN-on-Si power IDM (Nov 2025). https://www.semiconductor-today.com/news_items/2025/nov/veeco-051125.shtml
