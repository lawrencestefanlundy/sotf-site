---
type: concept
slug: flow-advanced-pkg-fanout
canonical_name: 'Advanced packaging: fan-out (InFO / FOWLP / FOPLP) (process step)'
seq: 51
phase: assembly
related_concepts:
- fowlp
- advanced-packaging
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
- slug: fowlp
  name: FOWLP / Fan-Out WLP
  path: /manufacturing/packaging/fowlp/
  macro: manufacturing
- slug: advanced-packaging
  name: Advanced Packaging
  path: /manufacturing/packaging/advanced-packaging/
  macro: manufacturing
---
> Step 51 of 56 in the semiconductor flow (Assembly). Prev: [Advanced packaging: 2.5D (CoWoS / EMIB / interposer) (process step)](/semiconductor-process-flow/packaging/flow-advanced-pkg-2-5d/) · Next: [Advanced packaging: 3D stacking & hybrid bonding (process step)](/semiconductor-process-flow/packaging/flow-advanced-pkg-3d-hybrid-bonding/)

## What this step does
Fan-out packaging dispenses with the organic substrate that older flip-chip and wire-bond packages depend on, and instead routes the chip's I/O directly into a "reconstituted" wafer or panel of molded dies. Because the routing fans out beyond the die edge into the surrounding mold compound, you get more I/O, a thinner stack, and a shorter electrical path than a chip-scale package can give. The volume archetype is TSMC's InFO (Integrated Fan-Out), which carries Apple's A- and M-series processors. The sub-processes inside the step:
- Die placement and reconstitution: known-good dies are picked and placed (often face-down) onto a temporary carrier, then over-molded with epoxy molding compound (EMC) to form a reconstituted wafer or panel.
- Carrier debond and grind: the temporary carrier is released and the molded panel is thinned to expose the die face.
- Redistribution layer (RDL) build-up: alternating dielectric (photosensitive polyimide / PSPI or Ajinomoto build-up film) and copper layers are patterned, seeded by electroless or sputtered Cu, then electroplated, to redistribute the I/O.
- Bumping and singulation: solder bumps or balls are placed, then the panel is diced into individual packages (handed off to [Wafer dicing / singulation (process step)](/semiconductor-process-flow/packaging/flow-wafer-dicing-singulation/) tooling).

## Where it sits and why it matters
This is the substrate-less branch of advanced assembly. It sits beside [Advanced packaging: 2.5D (CoWoS / EMIB / interposer) (process step)](/semiconductor-process-flow/packaging/flow-advanced-pkg-2-5d/) (silicon-interposer 2.5D for HBM-class bandwidth) and before [Advanced packaging: 3D stacking & hybrid bonding (process step)](/semiconductor-process-flow/packaging/flow-advanced-pkg-3d-hybrid-bonding/) (true 3D stacking). Fan-out matters because it was the first advanced-packaging family to reach true mobile volume: Apple's adoption of InFO-PoP in the iPhone 7's A10 (2016) was the inflection point that made fan-out mainstream [1][6]. It is now the cost-and-thinness workhorse for premium mobile SoCs, RF, PMICs and automotive, and the panel-level (FOPLP) variant is the leading candidate to drag advanced packaging onto large rectangular substrates where the cost-per-good-package falls.

## Equipment market
Equipment-plus-materials for fan-out is a roughly USD 1.5 to 2.0bn annual capex-and-consumables pool inside the wider advanced-packaging equipment market, growing low-to-mid teens; the FOWLP market it serves was about USD 1.77bn in 2024 heading to USD 4.13bn by 2030 at ~15% CAGR [2], with FOPLP a faster ~17% sub-segment off a smaller base [3]. Tooling is the bottleneck: panel-scale lithography and plating capacity, not demand, caps how fast TSMC, ASE and Amkor can add fan-out lines [4].

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| EV Group | Austria | Leader in temp bond/debond | Temporary bonding/debonding for reconstituted wafers; ~EU player |
| SUSS MicroTec | Germany | Leader, coat/develop + bonders | Coat/develop, lithography, bonders; 100% of TSMC CoWoS-L temp bonders, >70% HBM bond/debond [9] |
| ASML / Canon / Nikon | NL / JP / JP | Litho duopoly+ | Steppers/scanners for fine-pitch RDL; Nikon DSP-100 direct-write for 600mm panels [4] |
| Atotech (MKS) / Dow | DE / US | Plating chemistry+tools | Cu RDL electroplating lines and chemistry [10] |
| Applied Materials / TEL / Lam | US / JP / US | Strong in PVD/etch/dep | Seed-layer PVD, etch, deposition for RDL |
| Disco / DISCO + ASMPT | JP / HK | Dicing + assembly | Grinding, dicing, die-attach for reconstituted panels |

Concentration note: no single firm owns the line. Value splits across a litho oligopoly (ASML/Canon/Nikon), two strong EU specialists in bonding and coat/develop (EVG, SUSS), and a deposition/plating tail (AMAT, TEL, Lam, Atotech, Disco). Panel-level litho is the scarcest link.

## Materials & consumables
Per-panel, recurring spend that scales with volume, not a one-time tool sale, so the margin is annuity-like for incumbents. The bill of materials: epoxy molding compound (EMC, including dry-film EMC for panels), dielectric (Ajinomoto build-up film / ABF, photosensitive polyimide / PSPI), photoresist, electroless or sputtered copper seed, plating chemistry, temporary bonding adhesives and laser-debond release layers [3][8]. Suppliers: Ajinomoto (ABF, near-monopoly on the build-up dielectric), Shin-Etsu, Sumitomo Bakelite and Nagase ChemteX (EMC), Brewer Science and 3M (temp-bond adhesives), Fujifilm and Merck (PSPI/resist), Atotech/Dow/Meltex (plating). Recurring-revenue note: ABF and EMC are consumed every panel and are sticky on qualification, which is why the materials layer earns durable gross margins even though it is invisible in headline TAMs.

## Volumes, revenue, profitability
The cleanest revenue datapoint is TSMC's InFO line: revenue grew from ~USD 1.8bn (2018) to >USD 3.5bn (2024), driven almost entirely by Apple A- and M-series chips [1][6]. For scale, TSMC's CoWoS (the 2.5D cousin) hit ~USD 9.6bn in 2025, ~2.5x InFO, on Nvidia/AMD AI demand [1] — fan-out is the mobile-volume play, 2.5D is the AI-bandwidth play. Apple is now migrating its top A-series from InFO toward WMCM (wafer-level multi-chip module), with TSMC WMCM capacity targeted at ~60k wafers/month by end-2026 and >120k/month in 2027 [5]. On profitability, the value-capturing layer is the OSAT/foundry that runs the line. Pure-play OSAT economics are modest: Amkor posted ~14.8% gross margin and high-single-digit operating margin in 2024-25, with advanced packaging the higher-margin mix that lifts the blend [7]. TSMC's captive InFO earns foundry-class margins well above that because it is bundled with leading-edge logic.

## Market drivers, constraints & trends
Net read: the legacy mobile fan-out base grows steadily mid-single-to-low-teens, but the served equipment-and-materials pool is set to re-rate as fan-out moves up into AI-class packaging via panel-level (FOPLP/CoPoS), the single biggest swing factor over the next 2-5 years.

- **Drivers** — AI heterogeneous integration now pulls fan-out upward, not just mobile: ~65% of high-performance AI chips are expected on advanced packaging by 2026 [13]. Apple's InFO-to-WMCM migration is itself a capacity-builder, with TSMC WMCM targeted at ~60k wafers/month by end-2026 and >120k/month in 2027 [5]. With CoWoS sold out through at least mid-2026 [14], panel-level fan-out is the relief valve for large dies once FOWLP is no longer economical above the reticle limit [13][16].
- **Constraints** — Panel yield is the cap: warpage, lithography non-uniformity and die-shift challenges amplify ~5x going from a 300mm wafer to a 600x600mm panel, and high-density packages need die-shift within ±5µm [15][16]. CTE mismatch between silicon (2.6ppm/°C) and mold compound (7ppm/°C) drives warpage and yield loss [15]. Sub-10µm via metallization on panels remains hard [16]. Mobile FOWLP base growth is only ~6.7% CAGR [13], so the re-rate depends entirely on AI/panel adoption.
- **Trends & inflections to watch** — TSMC has standardised CoPoS on a 310x310mm panel and is building a 2026 mini-line, pilot 2027, mass production 2H 2028; glass-core substrate is the post-2030 step [13][16]. Taiwan suppliers' low-temperature (<180°C) dielectrics and a laser-modification-plus-etch two-step via process have already passed IDM qualification [13]. Tripwire: CoPoS mass-production go in 2H 2028, plus any AI accelerator (not just PMIC/RF) qualified on a 310mm panel before then, confirms the re-rate [13][16].

## Connections
- [FOWLP / Fan-Out WLP](/manufacturing/packaging/fowlp/) — the underlying technology cluster page for fan-out wafer-level packaging.
- [Advanced Packaging](/manufacturing/packaging/advanced-packaging/) — parent concept tying fan-out to 2.5D and 3D branches.
- **Advanced Packaging Market** — thesis on the overall advanced-packaging spend pool and where value accrues.
- **Chiplets Architecture Share** — thesis on disaggregation; fan-out and FOPLP are the low-cost integration substrate for multi-die designs.

## Sources
1. SemiAnalysis, "Apple-TSMC: The Partnership That Built Modern Semiconductors" (InFO revenue 2018 $1.8bn to >$3.5bn 2024; CoWoS $9.6bn 2025; InFO-PoP A10 2016 inflection). https://newsletter.semianalysis.com/p/apple-tsmc-the-partnership-that-built
2. Grand View Research / Research and Markets, Fan-Out WLP market USD 1.77bn (2024) to USD 4.13bn (2030), ~15.3% CAGR. https://www.grandviewresearch.com/horizon/statistics/semiconductor-packaging-market/advanced-packaging/fan-out-wafer-level-packaging-fo-wlp/global
3. Reanin / market research, FOPLP market ~USD 2.4bn (2025) to ~USD 7.4bn (2032), ~17.4% CAGR; FOPLP materials (dry-film EMC, ABF, PSPI). https://www.reanin.com/reports/fan-out-panel-level-packaging-market
4. SemiEngineering / Future Market Insights, RDL litho bottleneck; Nikon DSP-100 600mm panel direct-write; capacity capped 8-12%/yr. https://semiengineering.com/litho-options-for-panel-fan-out/
5. TrendForce / techovedas, Apple InFO to WMCM migration; WMCM capacity ~60k wpm end-2026, >120k wpm 2027. https://www.trendforce.com/news/2026/01/20/news-tsmc-reportedly-expands-wmcm-packaging-for-apple-capacity-may-more-than-double-by-2027/
6. SemiconductorX, InFO / integrated fan-out background and Apple adoption. https://semiconductorx.com/packaging-info.html
7. Amkor 8-K / Futurum, 2024 gross margin ~14.8%, operating margin high-single-digit, advanced packaging record. https://futurumgroup.com/insights/amkor-q4-2025-earnings-advanced-packaging-bottleneck-spurs-investment/
8. AllenPress JMEP / Polymer Innovation Blog, FOPLP materials: EMC, ABF dielectric, PSPI, electroless Cu seed, LDI. https://meridian.allenpress.com/jmep/article/15/4/141/36735/Design-Materials-Process-and-Fabrication-of-Fan
9. EV Group / SUSS MicroTec, temp bond/debond for FOWLP; SUSS 100% TSMC CoWoS-L temp bonders, >70% HBM. https://semiengineering.com/inside-panel-level-fan-out-technology/
10. Yole "Equipment and Materials for Fan-Out Packaging" overview; Atotech/Dow plating, panel consortium members. https://www.slideshare.net/slideshow/equipment-and-materials-for-fanout-packaging-2019-report-by-yole-dveloppement/183549385
11. TrendForce, Top 10 OSAT 2024: ASE $18.54bn (~45%), Amkor $6.32bn (~15%), JCET $5bn (~12%). https://www.trendforce.com/presscenter/news/20250513-12577.html
12. SkyWater / Deca, M-Series Gen 2 fan-out + Adaptive Patterning licence (2µm RDL, 20µm pad pitch, LDI). https://www.skywatertechnology.com/skywater-signs-technology-transfer-and-license-agreement-for-decas-gen-2-m-series-fan-out-and-adaptive-patterning-technology/
13. Persistence Market Research / Intel Market Research, FOWLP USD 4.0bn (2026) to USD 6.4bn (2033) ~6.7% CAGR; ~65% of high-performance AI chips on advanced packaging by 2026; AI heterogeneous-integration driver. https://www.persistencemarketresearch.com/market-research/fan-out-wafer-level-packaging-market.asp
14. Silicon Analysts / Fusion Worldwide, CoWoS sold out / oversubscribed through at least mid-2026; advanced packaging the AI bottleneck. https://siliconanalysts.com/analysis/foundry-allocation-status-q1-2026
15. SemiEngineering / Frontiers, FOPLP warpage + die-shift; CTE silicon 2.6ppm/°C vs mold compound 7ppm/°C; die-shift within ±5µm for high-density; challenges amplified ~5x from 300mm wafer to 600x600mm panel. https://semiengineering.com/fan-out-panel-level-packaging-hurdles/
16. TrendForce, "TSMC Accelerates CoPoS Development" — CoPoS 310x310mm panel standard; 2026 validation, 2027 pilot, 2H 2028 mass production; glass core substrate post-2030; <180°C low-temp dielectrics + laser+etch two-step sub-10µm via passed IDM qualification; FOPLP base today is PMIC/RF. https://www.trendforce.com/presscenter/news/20260617-13107.html
