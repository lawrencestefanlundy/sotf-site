---
type: concept
slug: flow-burn-in-reliability
canonical_name: Burn-in & reliability (process step)
seq: 55
phase: finaltest
related_concepts:
- wafer-level-burn-in
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
- slug: wafer-level-burn-in
  name: Wafer-Level Test & Burn-In (WLTBI)
  path: /manufacturing/equipment-processes/wafer-level-burn-in/
  macro: manufacturing
---
> Step 55 of 56 in the semiconductor flow (FinalTest). Prev: [Final test (ATE) (process step)](/semiconductor-process-flow/test-metrology/flow-final-test-ate/) · Next: [Marking, tape & reel, final inspection (process step)](/semiconductor-process-flow/packaging/flow-marking-tape-reel/)

## What this step does
Burn-in stresses parts at elevated temperature and voltage (typically 125-150C, sometimes higher current/voltage) to force "infant-mortality" failures, the weak devices that would otherwise die in the first weeks of field use, out before shipment. Reliability testing extends this to lifetime characterisation. It is the screen that turns a part that passes electrical test into a part trusted in a car, a satellite, or an AI server rack. Sub-processes inside this step:
- Package-level burn-in (PLBI): packaged parts loaded into burn-in boards inside ovens/chambers, powered and heated for hours.
- Wafer-level burn-in (WLBI): stress applied to the whole wafer before dicing, the route to known-good-die.
- High-temperature operating life (HTOL) and other reliability quals (HTRB, temperature cycling, HAST) for qualification lots.
- Dynamic / monitored burn-in, where parts run real patterns and are watched for failure, not just baked.

## Where it sits and why it matters
This sits after [Final test (ATE) (process step)](/semiconductor-process-flow/test-metrology/flow-final-test-ate/) and before [Marking, tape & reel, final inspection (process step)](/semiconductor-process-flow/packaging/flow-marking-tape-reel/). For commodity logic it is often skipped or sampled. It becomes mandatory the moment a die is going into something expensive or unforgiving: SiC and GaN power devices for EVs, automotive-grade parts, and now AI accelerators and HBM stacks. The economic driver is brutal arithmetic: in a 2.5D/3D package with eight HBM stacks plus a compute die, one latent failure scraps a module worth thousands. That pushes stress-screening earlier in the flow ("shift left") and onto the wafer, which is the **Known Good Die Test Wedge**.

## Equipment market
Burn-in *systems* (ovens, drivers, WLBI tools) are a small, fragmented niche inside test. Independent estimates put the burn-in test *system* market at roughly $0.8bn in 2025 growing ~8-10% CAGR [1][2]; the broader "wafer-level burn-in & reliability" bucket (including sockets, contactors, probe cards) is sized far larger at ~$2.3bn in 2025, ~15% CAGR, but that figure double-counts consumables and contactors [3]. Treat the pure-systems pool (~$0.8-1bn) as the honest number.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Advantest | Japan | leading (PLBI/ATE adjacency) | Burn-in alongside its ATE franchise [4] |
| Aehr Test Systems | USA | leader in WLBI pure-play | FOX WLBI + Sonoma PLBI (acquired Incal 2024) [4][5] |
| Chroma ATE | Taiwan | significant | Burn-in + reliability systems [4] |
| Micro Control / Espec / Aetrium | USA / Japan | niche | Burn-in ovens, chambers, drivers [4] |
| Teradyne | USA | adjacency | Test platform, limited dedicated burn-in [4] |

Concentration: "competitive and fragmented... no single company holding a dominant share" [4]. WLBI is the exception, where Aehr is effectively the scaled pure-play.

## Materials & consumables
The recurring spend lives below the system: burn-in boards (custom PCBs that fail and get replaced), and the sockets/contactors that touch each part. The burn-in & test socket market is ~$1.5bn+ and growing ~6-7% CAGR, with Yamaichi, Cohu, and Smiths Interconnect together ~40% of it; Enplas, Aries, 3M follow [6][7]. WLBI adds wafer contactors and full-wafer contact assemblies. These are genuinely recurring (sockets wear, boards are device-specific), so the consumable layer compounds with unit volume in a way the capital-tool layer does not.

## Volumes, revenue, profitability
There is no clean "units" metric; volume tracks the share of devices that *must* be screened (automotive, power, AI/HBM), not total wafer starts. Pool: systems ~$0.8-1bn, sockets/boards ~$1.5bn, so the whole step is a low-single-digit-billion revenue pool inside a ~$8-9bn test-equipment market. Margins: the value-capturing layer earns well. Aehr in its 2024 SiC peak posted non-GAAP net income of $35.8m on $66.2m revenue [8]; the 2025 diversification year softened to $59.0m revenue, GAAP net loss $(3.9)m, non-GAAP net income $4.6m as it absorbed lower-margin Incal product [9]. So the economics are gross-margin-rich (50%+ typical for the leaders) but operationally lumpy and order-driven at this scale. The socket/board vendors earn steadier consumable margins.

## Competitive landscape & value capture
The moat is qualification, not raw technology: getting a burn-in tool and socket recipe designed-into a customer's automotive or AI flow is sticky and slow to displace, which is why incumbents persist and why Aehr's AI-processor design-wins (lead hyperscaler ASIC, silicon-photonics WLBI follow-on orders in 2026 [5][10]) matter more than headline TAM. Value accrues to (a) the WLBI tool owner where shift-left is real, and (b) the consumable socket/contactor specialists who earn on every device. The vulnerability is that burn-in is a *cost* customers route around when yields are mature, so demand is concentrated in the hard cases.

## Market drivers, constraints & trends
Net read: the served pool grows steady-to-accelerating, but the acceleration is concentrated in two pockets (AI optical I/O and HBM/KGD), while the old SiC growth engine is in a cyclical trough through 2027.

- **Drivers**
 - AI/datacentre is now the swing factor. Aehr booked $37.2m in Q3 FY2026 at a book-to-bill above 3.5x, guided H2 bookings to the high end of $60-80m, and ran one AI customer at 42.1% of Q3 revenue against an effective backlog of $50.9m [11][12][18]. The growth is moving from SiC to AI processors, HBM and silicon photonics.
 - Silicon photonics / optical I/O is the newest WLBI line: Aehr's H2-2026 follow-on orders ship FOX-XP systems rated up to 3,500W per wafer (the June 2026 order tests nine wafers in parallel) for data-centre optical interconnects, a segment that barely existed two years ago [13][19].
 - HBM volume pulls reliability spend: HBM grew ~130% in 2025 and is forecast ~70% in 2026, and HBM4's 16-high stacks push a known-good-die requirement that mandates wafer-level burn-in before dicing [14].
 - One latent die in a $30k+ HBM4 wafer or a multi-thousand-dollar 2.5D module makes shift-left screening economically forced, not optional [15].

- **Constraints**
 - Burn-in equipment overcapacity is capping the aggregate: independent reads put burn-in *system* growth at only ~3% CAGR despite the AI pull, because the tool base over-built into the 2019-24 SiC cycle [16].
 - SiC, the prior demand engine, is in a downturn to 2027-2028 with upstream utilisation near 50% and the EV ramp delayed [17].
 - Burn-in is a cost customers route around as yields mature, so demand stays concentrated in hard cases (auto, power, AI/HBM) rather than broadening (see §Competitive landscape above).
 - Customer concentration: the listed pure-play's AI exposure rests on one or two hyperscaler-ASIC accounts, so a single design slip swings the number.

- **Trends & inflections to watch**
 - Thermal redline: AI processors now need 2.5-3.5kW per-wafer dissipation, forcing liquid-cooled chucks and kiloamp probe cards. Tripwire: a second WLBI vendor shipping a >3kW liquid-cooled production tool would confirm the optical/AI line is multi-sourced and structural [13][14].
 - HBM4 stays on microbumps; hybrid bonding (sub-10um) slips to HBM4E ~2027. Tripwire: a foundry/OSAT qualifying hybrid-bonded HBM in volume re-rates the KGD/WLBI requirement upward [14].
 - Burn-in-board pull as a leading indicator: Trio-Tech booked a $5.3m AI-GPU burn-in-board order in March 2026. Tripwire: repeat eight-figure board/socket orders tied to named AI platforms confirm the consumable layer is compounding ahead of tools [15].

## Connections
- [Wafer-Level Test & Burn-In (WLTBI)](/manufacturing/equipment-processes/wafer-level-burn-in/) — the shift-left technique central to this step
- **Known Good Die Test Wedge** — the thesis: KGD/WLBI goes mandatory for 2.5D/3D and AI dies by 2028
- [Final test (ATE) (process step)](/semiconductor-process-flow/test-metrology/flow-final-test-ate/) — upstream electrical test
- [Marking, tape & reel, final inspection (process step)](/semiconductor-process-flow/packaging/flow-marking-tape-reel/) — downstream finishing

## Sources
1. SNS Insider, Burn-In Test System for Semiconductor Market — https://www.globenewswire.com/news-release/2026/01/13/3217840/0/en/Burn-In-Test-System-for-Semiconductor-Market-Size-to-Grow-1530-25-Million-by-2033-SNS-Insider.html
2. Market Report Analytics, Burn-in Test Equipment ~$756m 2025, ~9.9% CAGR — https://www.marketreportanalytics.com/reports/burn-in-test-equipment-for-semiconductor-394837
3. Virtue Market Research, Wafer-Level Burn-In & Reliability Testing (~$2.26bn 2025, 14.8% CAGR) — https://virtuemarketresearch.com/report/wafer-level-burn-in-reliabilit-testing-market
4. SemiconductorX / market vendor lists (Advantest, Aehr, Chroma, Teradyne, Incal, Espec) — https://www.24marketreports.com/semiconductor-and-electronics/global-burnin-test-system-for-semiconductor-forecast-market
5. Aehr, momentum in package-level burn-in alongside WLBI (Incal acquisition, capacity) — https://www.aehr.com/2025/11/aehr-seeing-momentum-in-package-level-burn-in-alongside-expanding-wafer-level-burn-in-demand/
6. Yole Group, Burn-in and Test Sockets Market Monitor — https://www.yolegroup.com/product/quarterly-monitor/semiconductor-test-consumables---burn-in-and-test-sockets-market-monitor/
7. Global Growth Insights, Test & Burn-in Sockets (Yamaichi/Cohu/Smiths ~40%) — https://www.globalgrowthinsights.com/market-reports/semiconductor-test-and-burn-in-sockets-market-115895
8. Aehr Test Systems FY2024 results — https://www.sec.gov/Archives/edgar/data/0001040470/000165495424009008/aehr_ex991.htm
9. Aehr Test Systems FY2025 full-year results ($59.0m rev, GAAP net loss $(3.9)m) — https://www.aehr.com/2025/07/aehr-test-systems-reports-fiscal-2025-fourth-quarter-and-full-year-financial-results-expands-total-addressable-market-and-diversifies-customer-base/
10. Aehr, follow-on WLBI order from silicon-photonics customer (Jun 2026) — https://www.aehr.com/2026/06/aehr-receives-follow-on-order-from-major-silicon-photonics-customer-for-fully-automated-wafer-level-burn-in-system-for-hyperscale-data-center-optical-interconnect/
11. Seeking Alpha, Aehr targets high side of $45-50m FY2026, effective backlog $50.9m — https://seekingalpha.com/news/4573152-aehr-targets-high-side-of-45m-50m-fy2026-revenue-as-effective-backlog-reaches-50_9m
12. Aehr Q3 FY2026 8-K (Customer A 42.1% of Q3 revenue, $37.2m bookings) — https://www.sec.gov/Archives/edgar/data/1040470/000165495426003310/aehr_ex991.htm
13. Aehr, follow-on WLBI order for AI optical I/O / silicon photonics, FOX-XP up to 3,500W/wafer, ships H2-2026 (Mar 2026) — https://www.aehr.com/2026/03/aehr-receives-follow-on-order-for-fully-automated-wafer-level-burn-in-systems-powering-ai-optical-i-o-and-data-center-interconnects/
14. Virtue Market Research, WLBI & reliability ~$2.26bn 2025 → $4.51bn 2030 (14.8% CAGR); HBM ~130% 2025 / ~70% 2026, HBM4 KGD mandates WLBI, 2.5kW+/wafer liquid-cooled chambers — https://virtuemarketresearch.com/report/wafer-level-burn-in-reliabilit-testing-market
15. Temple8 Capital, the burn-in tax: $30k wafers, shift-left economics, Trio-Tech $5.3m AI-GPU burn-in-board order (Mar 2026) — https://temple8capital.substack.com/p/semiconductor-burn-in-testing-ai-hbm4-reliability-stocks
16. IDTechEx, power electronics market — burn-in system overcapacity offsets growth, ~3% CAGR — https://www.idtechex.com/en/research-report/power-electronics-market/1152
17. Yole Group, Power SiC overcapacity downturn to 2027-2028, utilisation ~50%, device market to ~$10bn by 2030 — https://www.semiconductor-today.com/news_items/2025/dec/yole-181225.shtml
18. Aehr Test Systems, Q3 FY2026 over $37.2m bookings, book-to-bill >3.5x, H2 bookings to high end of $60-80m, lead hyperscaler PLBI + CoWoS/HBM WLBI interest — https://www.aehr.com/2026/04/aehr-test-systems-reports-over-37-million-in-quarterly-bookings-driven-by-strong-ai-and-data-center-infrastructure-demand/
19. Aehr Test Systems, follow-on production order for FOX-XP testing nine wafers in parallel from a data-centre optical-transceiver silicon-photonics customer (Jun 2026) — https://www.aehr.com/2026/06/aehr-receives-follow-on-order-from-major-silicon-photonics-customer-for-fully-automated-wafer-level-burn-in-system-for-hyperscale-data-center-optical-interconnect/
