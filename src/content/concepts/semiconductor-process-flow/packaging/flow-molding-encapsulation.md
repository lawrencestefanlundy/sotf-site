---
type: concept
slug: flow-molding-encapsulation
canonical_name: Molding / encapsulation (process step)
seq: 48
phase: assembly
related_concepts:
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
- slug: advanced-packaging
  name: Advanced Packaging
  path: /manufacturing/packaging/advanced-packaging/
  macro: manufacturing
---
> Step 48 of 56 in the semiconductor flow (Assembly). Prev: [Lead frame manufacturing (process step)](/semiconductor-process-flow/packaging/flow-leadframe/) · Next: [Solder ball attach / BGA (process step)](/semiconductor-process-flow/packaging/flow-solder-ball-bga/)

## What this step does
After the die is attached and wire-bonded (or flip-chip joined) onto its [Lead frame manufacturing (process step)](/semiconductor-process-flow/packaging/flow-leadframe/) or substrate, the assembly is encased in a hard plastic body that protects the silicon and the interconnects from moisture, handling, and mechanical shock. The encapsulant is a filler-loaded epoxy resin (epoxy molding compound, EMC) shaped under heat and pressure. The sub-processes inside this step:
- **Transfer molding** — granulated/pelletised EMC is melted and pushed through runners into multiple cavities over a leadframe strip; the workhorse for commodity QFN/QFP/BGA.
- **Compression molding** — EMC (granule, sheet, or liquid) is dosed directly into a cavity and the mold closes onto it; low-pressure, low-flow, the method of choice for thin wafer-level and panel-level packages and for HBM stacks where flow must not disturb fragile through-silicon-via (TSV) joints.
- **Capillary / no-flow underfill** — for flip-chip, a liquid resin is wicked under the die to fill the solder-bump gap before or after molding, redistributing thermo-mechanical stress.
- **Post-mold cure, marking, deflash/dejunk** before singulation.

## Where it sits and why it matters
Encapsulation is the reliability gate of the package. Almost every plastic IC in the world passes through it, so volumes are enormous and the materials are consumed every cycle. The step is also where advanced packaging gets hard: warpage, void-free fill over tall stacks, and stress on micro-bumps are dominated by the EMC formulation and the molding tool. That is why HBM and 2.5D/3D have pulled value toward a small set of compression-molding specialists.

## Equipment market
Semiconductor molding (compression + transfer + fully-automatic) equipment is roughly **$1.2B in 2024**, growing at about **8.9% CAGR** toward ~$2.5B by 2033 [1]; the compression-molding sub-segment grows faster on advanced-packaging pull. This is a rough report-mill range; treat the compression-specific HBM pull as the real driver.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| TOWA | Japan | ~19-22% of all molding equip; ~60% transfer-molding; ~80-90% HBM compression [1][2][3] | Dominant in HBM/wafer-level compression; guides 30-45 HBM systems/yr [3] |
| ASMPT | Singapore | top-3 | Broad assembly + automated molding |
| Hanmi Semiconductor | South Korea | top-5 | TC bonders + molding, HBM-adjacent |
| Yamaha Motor Robotics (ex-Apic Yamada) | Japan | top-5 | Transfer/compression systems |
| Kitagawa Seiki | Japan | niche | Specialty molding presses |

Concentration: in the part that matters (compression molding for HBM and advanced packaging) the market is effectively a **near-monopoly** held by TOWA. Commodity transfer molding is more contested but mature and slow-growing.

## Materials & consumables
This step consumes EMC and underfill on every package, making it a textbook recurring-revenue layer (tool sold once, material bought forever).
- **EMC** market ~**$2.0-2.5B (2024-25)**, CAGR ~**6-6.7%**, to ~$3.6B by 2030 [4][5]. Top-10 hold ~70% [4]. Vendors: Resonac (ex-Showa Denko/Hitachi Chemical, #1 at ~40-50% of the overall EMC pool, the leader in high-end advanced-packaging EMC) [6]; Sumitomo Bakelite (long-time leader, deep OSAT ties); Panasonic; Shin-Etsu; KCC (Korea); Chang Chun (Taiwan). Resonac + Sumitomo Bakelite + Panasonic together ~40% of advanced-packaging EMC [4][6].
- **Underfill** market ~**$590-720M (2024)**, CAGR ~**9-10.5%**, to ~$1.15-1.45B by 2031-32 [7][8]. Vendors: Henkel (capillary + no-flow leader), Resonac/Namics, Panasonic, Shin-Etsu, MacDermid Alpha, Fuji Chemical. Wafer/panel-level underfill is ~65% of the segment [7].

## Volumes, revenue, profitability
Combined revenue pool for this step is roughly **$3.5-4B of materials** (EMC + underfill) plus ~**$1.2B of equipment** per year, so call it a **~$5B step**, with materials about 3x the tool spend and growing on a recurring base. Margins split sharply by layer: the EMC/underfill chemistry is a specialty-materials business with mid-to-high gross margins but commodity-grade EMC compresses to low-double-digit operating margins; the differentiated value is in advanced-packaging grades. On the equipment side, TOWA's molding segment runs ~**22% operating margin** [2], and its HBM compression franchise earns the best economics in the whole step because there is no credible second source. The margin accrues to (a) TOWA in HBM/advanced-packaging tools and (b) Resonac/Sumitomo Bakelite/Henkel in the high-spec material grades.

## Market drivers, constraints & trends
Net read: the served market grows clearly faster than the ~6-9% headline because the value is migrating into the HBM and advanced-packaging grades that are pulling hardest, even as commodity transfer molding stays flat.
- **Drivers**
  - HBM is the engine: HBM4 entered mass production in Feb 2026 at Samsung and SK Hynix, with 16-high 48GB stacks pushing to Q3 2026 [9][10]. Every stack needs void-free mold underfill over fragile TSV joints, the exact job that pulls TOWA's compression tools and high-spec EMC; the HBM-grade EMC sub-pool is sized small (~$500M 2025) but quoted at ~15% CAGR vs ~6% for the base pool [11].
  - TSMC, Samsung and Intel are standing up advanced-packaging capacity through 2025-26, and fan-out wafer-level packaging now takes >25% of advanced-packaging EMC demand, shifting the mix toward ultra-low-warpage compounds [11].
  - Automotive/power electronics is a second leg: EV inverters and SiC/GaN modules need high-heat-resistant, thermally conductive encapsulants, and Sumitomo Bakelite is adding JPY20bn of Shizuoka capacity explicitly for AI plus automotive power [12].
- **Constraints**
  - Warpage is the physical ceiling on panel scale-up: the CTE gap between silicon (~2.6ppm/C) and EMC (~7ppm/C) drives warpage of several mm on a 600mm panel, gating how fast FOPLP and glass adopt [13].
  - China localization compresses the commodity tail: Sumitomo Bakelite's new Suzhou plant lifts capacity ~1.3x and domestic Chinese suppliers are pressuring Resonac's share and margin in standard grades [12][14].
  - Cyclicality plus single-source concentration cuts both ways: TOWA's HBM franchise is exposed to any pause in AI capex, and a TOWA tool slip would cap the whole step.
- **Trends & inflections to watch**
  - Panel-level / glass: Rapidus is building 600mm-square glass-interposer packaging on Lam panel systems [13]. Tripwire: a named molding-tool order (TOWA/ASMPT) for a 600mm glass PLP line booked in 2026-27 confirms the served market widening beyond wafer scale.
  - HBM4 to HBM4E ramp: tripwire is TOWA guiding HBM compression-system shipments above its current 30-45/yr in any FY26-27 update [9].
  - Mold-underfill displacing capillary underfill at 16-high (TOWA Ultra Narrow Gap, SK Hynix MR-MUF) [9][10]: tripwire is a 16-high HBM4 part shipping in volume on a molded-underfill flow in 2026, shifting dollars from underfill chemistry into the molding tool/EMC.

## Connections
[Advanced Packaging](/manufacturing/packaging/advanced-packaging/)

- Owning idea: **Legacy Assembly Commoditised** (commodity assembly (recorded pass)).

## Sources
1. Verified Market Reports / Intel Market Research — Semiconductor Compression Molding Equipment Market (~$1.2B 2024, ~8.9% CAGR). https://www.verifiedmarketreports.com/product/semiconductor-compression-molding-equipment-market/ ; https://www.intelmarketresearch.com/semiconductor-compression-molding-equipment-market-22699
2. TOWA Corporation Integrated Report 2024 (segment operating margin, molding leadership). https://www.towajapan.co.jp/en/wp-content/uploads/sites/3/2024/11/tr2024A4e.pdf
3. Investing.com — TOWA FY3/27 guidance, HBM systems cadence (30-45/yr). https://www.investing.com/news/earnings/japans-chipmaker-towa-guides-for-17-sales-rise-in-fy327-93CH-4675662
4. Spherical Insights / market summaries — EMC top-10 ~70%, Sumitomo Bakelite + Showa Denko + Chang Chun ~45%. https://www.sphericalinsights.com/blogs/top-25-companies-in-global-semiconductor-epoxy-mold-compound-market-market-strategic-overview-and-future-trends-2024-2035
5. MarkSpark / Valuates — EMC in semiconductor packaging ~$2.0-2.5B, ~6-6.7% CAGR, ~$3.6B by 2030. https://marksparksolutions.com/reports/epoxy-molding-compound-semiconductor-packaging-market
6. Zion / Resonac product pages — Resonac #1 EMC, advanced-packaging grade leadership. https://www.zionmarketresearch.com/report/epoxy-molding-compound-market ; https://www.resonac.com/products/semi-backend-process/76
7. 24chemicalresearch / Global Growth Insights — Underfill ~$590M 2024, ~8.8% CAGR, wafer/panel ~65%. https://www.24chemicalresearch.com/reports/286231/global-underfills-for-semiconductor
8. OpenPR / QYResearch — Underfill to ~$1.44B by 2031, ~10.5% CAGR; vendors (Henkel, Namics, Resonac, Shin-Etsu, MacDermid Alpha). https://www.openpr.com/news/4224990/semiconductor-underfill-market-trends-the-global ; https://www.qyresearch.com/industry-news/8722/underfill
9. Digitimes / TOWA — HBM4 Ultra Narrow Gap Mold Underfill, YPM/CPM capacity expansion, PLP investment, 30-45 HBM systems/yr cadence. https://www.digitimes.com/news/a20250401PD226/equipment-packaging-sales-hbm4-growth.html ; https://www.towajapan.co.jp/en/wp-content/uploads/sites/3/2025/03/news_20250321_eng.pdf
10. Digitimes / TrendForce / TechPowerUp — HBM4 mass production Feb 2026 (Samsung, SK Hynix); 16-high 48GB stacks to Q3 2026; SK Hynix MR-MUF molded underfill. https://www.digitimes.com/news/a20251226PD223/samsung-sk-hynix-production-hbm4-2026.html ; https://www.trendforce.com/news/2026/01/09/news-nvidia-demand-fuels-hbm4-race-12-layer-ramps-16-layer-push-by-sk-hynix-samsung-and-micron/
11. MarketResearchForecast / market summaries — EMC-for-HBM ~$500M 2025 at ~15% CAGR; FOWLP >25% of advanced-packaging EMC; TSMC/Samsung/Intel adv-packaging capex 2025-26. https://www.marketresearchforecast.com/reports/epoxy-molding-compound-for-hbm-packaging-67290
12. Sumitomo Bakelite — Suzhou new plant (~1.3x capacity, 2025 mass production) + JPY20bn Shizuoka expansion for AI/automotive power. https://www.sumibe.co.jp/english/topics/2024/it-materials/0924_01/index.html ; https://www.openpr.com/news/4467347/global-epoxy-molding-compound-in-semiconductor-packaging
13. SemiEngineering / TrendForce — FOPLP warpage from Si-vs-EMC CTE mismatch (~2.6 vs ~7ppm/C) on 600mm panels; Rapidus 600mm glass interposer on Lam panel systems. https://semiengineering.com/fan-out-panel-level-packaging-hurdles/ ; https://www.trendforce.com/news/2026/05/26/news-rapidus-reportedly-taps-lam-research-panel-level-packaging-system-for-600mm-square-glass-interposer-push/
14. PortersFiveForce / market summaries — Chinese domestic EMC suppliers pressuring Resonac share and margin in standard grades 2025. https://portersfiveforce.com/blogs/competitors/resonac
