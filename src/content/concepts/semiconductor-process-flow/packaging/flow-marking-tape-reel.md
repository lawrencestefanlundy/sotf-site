---
type: concept
slug: flow-marking-tape-reel
canonical_name: Marking, tape & reel, final inspection (process step)
seq: 56
phase: finaltest
related_concepts:
- packaging
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
- packaging
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
- slug: packaging
  name: Semiconductor Packaging
  path: /manufacturing/packaging/packaging/
  macro: manufacturing
---
> Step 56 of 56 in the semiconductor flow (FinalTest). Prev: [Burn-in & reliability (process step)](/semiconductor-process-flow/test-metrology/flow-burn-in-reliability/) · 

## What this step does
The last cosmetic-and-logistics gate before a packaged, tested device ships. Three commodity sub-processes, usually run on one integrated turret handler:
- **Marking**: a fiber laser etches part number, date code, lot/wafer traceability and a 2D data-matrix code onto the package top (legacy ink stamping is mostly gone).
- **Final visual / AOI inspection**: 2D/3D automated optical inspection checks marking legibility, lead coplanarity, chip-outs, micro-cracks and orientation; rejects are binned out.
- **Tape and reel**: good die are placed pocket-by-pocket into embossed carrier tape, sealed with cover tape and wound onto reels (or loaded into trays/tubes) for the customer's surface-mount line.

## Where it sits and why it matters
This is the physical handoff from the chipmaker/OSAT to the board assembler. It adds almost no device value but is unavoidable: traceability marking is mandated by automotive/industrial quality regimes, and tape-and-reel is the only economic format for high-speed pick-and-place (used on ~79% of placement lines running above 30,000 units/hour per industry surveys). Get it wrong, mislabel a code, mis-pocket a part, ship an illegible mark, and you create field-traceability failures or stop a customer's line. So it is low-value, high-discipline work: the margin is in throughput, yield and zero-defect logistics, not technology.

## Equipment market
No single "marking + tape-reel + final-inspect" equipment number exists; it splits across three overlapping commodity tool markets:

| Vendor | HQ | Est. share / position | Notable |
|---|---|---|---|
| Cohu / ISMECA | US / Switzerland | Leader in integrated turret handlers | NY-series turret integrates test, laser mark, 3D AOI and tape-and-reel in one tool, full wafer-to-reel traceability |
| ASMPT | Singapore / HK | ~17% of broad packaging-equipment market | Marking and tape-and-reel modules inside assembly lines |
| Nordson (YESTECH) | US | Top-tier AOI for advanced packaging | 2D/3D AOI for PCBA and panel/wafer-level packaging |
| Koh Young / Omron / CyberOptics / Saki | KR / JP / US | AOI specialists | 3D AOI leadership, mostly SMT-adjacent |
| Han's Laser / Trumpf / Coherent | CN / DE / US | Fiber-laser marking sources and systems | IC-chip laser marking machine segment ~USD 1.45bn (2025) [3] |

Sizing the pieces (all third-party report-mill estimates, treat as order-of-magnitude): the **whole** laser-marking-machine market (all industries) was ~USD 4.2bn in 2024 growing ~10% [1]; the **IC-chip-specific** laser marker slice ~USD 1.45bn in 2025 at ~7.8% CAGR [3]; **AOI equipment** (all electronics) ~USD 1.7bn in 2025, with a fast headline ~19% CAGR claim [2]. Concentration is moderate: Cohu/ISMECA dominate the integrated semiconductor-test-and-finish handler; AOI is more fragmented across Koh Young, Omron, Nordson, CyberOptics, Saki.

## Materials & consumables
The recurring-revenue layer, and bigger than the tools, is the carrier-tape consumable:
- **Embossed carrier tape + cover tape**: market ~USD 0.65bn (2025) [4], shipping >58bn components/year; widths 8mm-32mm, cavity tolerance ±0.02mm for sub-3mm parts.
- **Plastic reels** and trays/tubes: separate ~USD 0.1bn+ niche.
Top tape makers, top five hold ~50%: 3M, Advantek, Shin-Etsu, Zhejiang Jiemei, C-Pak; then Sumitomo Bakelite, DENKA, TCTEC, Asahi Kasei [5]. Production is concentrated in East Asia. This is genuine recurring spend, every reel is consumed once, but it is a thin-margin precision-plastics business, not IP.

## Volumes, revenue, profitability
Volumes are enormous and the per-unit economics tiny: >1.15 trillion semiconductor units/year, >740 million metres of carrier tape consumed annually [6]. The combined equipment + consumables revenue pool here is roughly **USD 2-3bn/year** (IC laser markers ~1.5bn + a slice of AOI + ~0.65bn carrier tape), a rounding error against front-end fab tooling. Margins: laser-marking and AOI tool builders run gross margins in the 35-50% range with mid-teens or lower operating margins (Cohu's whole back-end-test business has cycled between low-double-digit and low-single-digit operating margins). Carrier-tape converters are lower, commodity precision-plastics gross margins (often sub-30%). Most of the actual marking/inspect/tape work is done in-house by the **OSAT** ([OSAT (outsourced assembly & test) services (process step)](/semiconductor-process-flow/packaging/flow-osat-assembly-test-services/)) as the final line step, so the OSAT books the finishing fee, the tool and tape vendors take a one-time and a recurring cut respectively.

## Competitive landscape & value capture
Value capture is weak and dispersed. There is no moat in the step itself, it is a price-and-throughput game; switching cost lives in the integrated handler (qualifying a new wafer-to-reel traceability flow is painful, which is what gives Cohu/ISMECA its stickiness) and in tape-converter qualification for automotive parts. Real value accrues upstream (the device, the test) and is merely passed through here. EU exposure: ISMECA (Switzerland) inside Cohu is the one credible European-rooted asset; tape supply is almost entirely Asian/US. Seed-relevant angle is thin, the only non-commodity wedge is AI-vision defect detection (micro-crack/marking AOI) and traceability-data software, where a smaller player could differentiate on algorithms rather than mechanics; even there incumbents (Nordson, Koh Young, Cohu NV-Core) are entrenched.

## Market drivers, constraints & trends
Net read: low-single-digit growth in the commodity core, with one genuine up-mix lever (inspection moving up-value as packaging gets harder to look at).
- **Drivers**
  - Unit volume + miniaturisation: >740m metres of carrier tape consumed/year, and sub-3mm parts force tighter ±0.02mm cavity tolerance, a higher-spec (higher-ASP) tape; embossed-tape pool ~USD 0.67bn 2026 at ~3.4% CAGR [10].
  - Traceability mandates: AEC-Q100 automotive qualification and lifetime root-cause tracing make a per-die 2D data-matrix mark non-optional, locking marking volume to every automotive/industrial part [11].
  - Advanced-packaging up-mix: chiplet / 3D-IC / heterogeneous integration needs custom-cavity tape and AI defect classification, and pushes a new wafer-level marking slice (wafer laser marker ~USD 222m 2023 to ~334m 2030, 6.2% [12]) growing faster than legacy package marking.
- **Constraints**
  - Commoditisation: Chinese builders (Han's Laser et al) price entry fiber/CO2 markers 50-70% below Western tools, compressing margins (Han's net ~7% 2025); the step's economics get worse, not better [13].
  - Cyclicality + pass-through: revenue tracks unit shipments and OSAT capex, no pricing power; value accrues upstream and is merely passed through here.
- **Trends & inflections to watch**
  - AI/deep-learning AOI: rule-based inspection gives way to trained models (>99% vs ~80% human), the one place a smaller player can differentiate on algorithms [14]. Tripwire: an OSAT publicly qualifying a deep-learning ADC AOI line as primary (not assist) by 2027.
  - Glass-substrate / FOPLP shift: glass reportedly renders legacy AOI obsolete (transparent/reflective), implying an inspection replacement super-cycle [15]; but pilot only in 2026, >20% penetration not before 2028 [15]. Absolics' Covington (Georgia) high-volume glass line is now built, targeting AMD/Amazon AI-package contracts by end-2026 [16], which forces new transparent-substrate AOI. Tripwire: a named panel/TGV-substrate AOI tool qualified into an Absolics or Samsung Electro-Mechanics glass line in volume by 2027-28.

## Connections
[Semiconductor Packaging](/manufacturing/packaging/packaging/)

- Owning idea: **Legacy Assembly Commoditised** (commodity assembly (recorded pass)).

## Sources
1. Fortune Business Insights, Laser Marking Machine Market (USD 3.22bn 2024 / 4.16bn variant, ~10% CAGR). https://www.fortunebusinessinsights.com/laser-marking-machine-market-109809
2. Mordor Intelligence, Automated Optical Inspection Equipment Market (~USD 1.7bn 2025, ~19% CAGR). https://www.mordorintelligence.com/industry-reports/automated-optical-inspection-equipment-market
3. IntelMarketResearch / Valuates, IC Chip Laser Marking Machine Market (~USD 1.45bn 2025, ~7.8% CAGR). https://www.intelmarketresearch.com/ic-chip-laser-marking-machine-market-37291
4. 360 Research / Global Growth Insights, Embossed Carrier Tape Market (~USD 0.65bn 2025, 58bn components/yr). https://www.globalgrowthinsights.com/market-reports/embossed-carrier-tape-market-103708
5. Embossed carrier tape vendor shares (top 5 ~50%: 3M, Advantek, Shin-Etsu, Jiemei, C-Pak). https://datahorizzonresearch.com/embossed-carrier-tape-market-29353
6. Business Research Insights, Carrier Tape Market volumes (>740m metres/yr; >1.15tn units). https://www.businessresearchinsights.com/market-reports/carrier-tape-market-100594
7. Cohu, Cohu to Acquire Ismeca (back-end finishing handler, wafer-to-reel traceability). https://cohu.gcs-web.com/news-releases/news-release-details/cohu-acquire-ismeca
8. Cohu, Ismeca NY32 Turret and Inspection Handler (integrated test/mark/3D-AOI/tape-reel). https://www.cohu.com/ny32/
9. Nordson Test & Inspection, AOI for advanced semiconductor packaging. https://www.nordson.com/en/divisions/test-and-inspection/our-technologies---automated-optical-inspection
10. 360 Research Reports, Embossed Carrier Tape Market (~USD 672m 2026, ~3.4% CAGR; chiplet/3D-IC custom cavities; sub-3mm ±0.02mm). https://www.360researchreports.com/market-reports/embossed-carrier-tape-market-204679
11. DapraMarking / AMD Machines, 2D Data Matrix direct-part marking + AEC-Q100 lifetime traceability. https://www.dapramarking.com/part-id-traceability/data-matrix-codes
12. 24 Market Reports, Wafer Laser Marking Machine Market (~USD 222m 2023 to ~334m 2030, 6.2% CAGR). https://www.24marketreports.com/semiconductor-and-electronics/global-wafer-laser-marking-machine-forecast-market
13. DigiTimes / Han's Laser, China laser price-down 50-70% vs Western tools, Han's net margin ~7% 2025, mix shift to higher-value semi/PV. https://www.digitimes.com/news/a20250915PD233/laser-semiconductor-industry-demand-equipment-industrial.html
14. ITES / Onto Innovation, AI deep-learning AOI (>99% vs ~80% human; automatic defect classification for advanced packaging). https://global.iteschina.com/en/news/details/2924
15. Aminext, Glass substrate packaging 2026 (legacy AOI rendered obsolete, inspection replacement super-cycle; pilot 2026, >20% penetration not before 2028; Absolics/Intel Georgia line). https://www.aminext.blog/en/post/glass-substrate-advanced-packaging-2026-trend
16. MIT Technology Review, Future AI chips could be built on glass (Absolics Covington GA high-volume line, ~12,000 m2/yr ≈ 2-3m H100-size packages, AMD/Amazon contracts targeted end-2026). https://www.technologyreview.com/2026/03/13/1134230/future-ai-chips-could-be-built-on-glass/
