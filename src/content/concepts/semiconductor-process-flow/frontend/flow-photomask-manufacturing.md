---
type: concept
slug: flow-photomask-manufacturing
canonical_name: Photomask manufacturing (process step)
seq: 14
phase: design
related_concepts:
- mask-blank-manufacturing
- lithography
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
- slug: mask-blank-manufacturing
  name: Mask Blank Manufacturing
  path: /manufacturing/lithography/mask-blank-manufacturing/
  macro: manufacturing
- slug: lithography
  name: Lithography
  path: /manufacturing/lithography/lithography/
  macro: manufacturing
---
> Step 14 of 56 in the semiconductor flow (Design). Prev: [Mask data prep & computational litho (OPC/ILT) (process step)](/semiconductor-process-flow/design/flow-mask-data-prep-opc/) · Next: [Polysilicon (electronic-grade silicon) (process step)](/semiconductor-process-flow/wafer-materials/flow-polysilicon-egs/)

## What this step does

A photomask (reticle) is the physical master that the scanner projects onto the wafer. Once the OPC-corrected layout from [Mask data prep & computational litho (OPC/ILT) (process step)](/semiconductor-process-flow/design/flow-mask-data-prep-opc/) is fractured into machine instructions, the mask shop turns that data file into a patterned piece of glass, one mask per layer, 60 to 100 masks for a full advanced-node set. The unit sub-processes inside this step:

- Start from a blank: a low-thermal-expansion quartz substrate coated with chrome (optical/DUV) or a Mo/Si multilayer plus absorber (EUV), supplied as a finished blank.
- Resist coat, then pattern-write the layout with a multi-beam electron-beam mask writer.
- Develop, etch the absorber, strip resist, clean.
- Inspect for defects, repair defects (e-beam/nanomachining), measure critical dimension and registration.
- Mount a pellicle (protective membrane) and ship the qualified reticle to the fab.

## Where it sits and why it matters

This is the hinge between design and manufacturing. Every wafer printed at a node depends on a correct mask set, and a single printable defect on one reticle scraps yield across every wafer that uses it. At leading edge the mask set is a multi-million-dollar fixed cost amortised over the production run, which is exactly why advanced nodes only pay off at high volume. The reticle is also a recurring consumable: EUV reticles have shorter usable lives and need replacement, so mask demand tracks both new tape-outs and ongoing production.

## Equipment market

The mask-shop tool fleet is small in unit terms but extremely concentrated and high-ASP. The headline pieces are the multi-beam mask writer and the mask inspection/repair tools.

Multi-beam mask writer market ~$0.96B in 2025, ~12% CAGR [1]. EUV/advanced mask inspection is a separate multi-hundred-million pool dominated by two names [4].

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| IMS Nanofabrication (Intel-owned, TSMC stake) | Austria | ~82% of multi-beam mask writers (2024) [3] | The reference multi-beam writer for sub-3nm masks; Intel acquired, TSMC took a minority stake |
| NuFlare Technology (Toshiba group) | Japan | #2 multi-beam writer [3] | Long-time e-beam writer incumbent, also single-beam |
| Lasertec | Japan | Sole supplier of actinic EUV mask inspection (ACTIS/MATRICS) [4] | Virtual monopoly on at-wavelength EUV defect inspection |
| KLA | US | ~28-34% of mask inspection [4] | Broad inspection/metrology; DUV mask inspection leader |
| JEOL / Raith / Vistec | Japan / Germany | Remainder of e-beam writing [3] | Research and lower-volume e-beam |

Concentration note: this is a near-monopoly stack. One company effectively owns the leading-edge mask writer (IMS), and one owns actinic EUV inspection (Lasertec). The chokepoints sit in the tools, not in the mask shops themselves.

## Materials & consumables

The mask shop consumes finished mask blanks and pellicles, plus resists, etchants and cleaning chemistries. The two materials pools that actually carry pricing power:

- Mask blanks (the glass substrate plus coating). DUV blanks are a commodity-ish quartz business; EUV blanks are not. EUV mask blanks were ~$591M in 2024, growing ~12% CAGR to ~$1.36B by 2031 [2]. AGC and Hoya hold ~93% combined of EUV blanks, with AGC >59% by one read and Hoya >75% by another (estimates differ; both point to a two-supplier market) [2]. See [Mask Blank Manufacturing](/manufacturing/lithography/mask-blank-manufacturing/) for the upstream detail.
- EUV pellicles. The protective membrane over an EUV reticle. Market ~$558M in 2024 growing ~14% CAGR toward ~$1.6B by 2030 [5]. Mitsui Chemicals produces the membranes under an ASML license; imec plus Mitsui are commercialising carbon-nanotube pellicles for high-power EUV [5].

Recurring-revenue note: blanks and pellicles are consumed per mask and replaced over a reticle's life, so they are a consumable annuity that grows with EUV adoption, not a one-time tool sale.

## Volumes, revenue, profitability

Mask sets are low-volume, high-value. A leading-edge optical mask runs ~$100k; a single EUV mask is ~$300k on average and $500k to $1M at the top end; a full advanced mask set of 60-100 masks runs ~$5-15M [6][7].

Total photomask market: roughly $5.1-5.8B in 2024, growing ~4-8% CAGR depending on source (treat the high single digits as optimistic; report-mill spreads are wide) [1]. Note a structural quirk: the merchant market is only part of this. The largest mask makers by total volume are captive shops inside the foundries and IDMs; TSMC calls itself the largest captive mask maker, and DNP plus Toppan (now Tekscend) plus Photronics are the merchant big three, with TSMC sitting third overall counting captive output [8].

Margins of the value-capturing layer: the merchant mask maker Photronics ran FY2024 revenue ~$867M; in FY2025 it printed quarterly gross margin ~33-35% and operating margin ~22-24%, with high-end (advanced IC) at ~51% of revenue [9][10]. The equipment monopolists earn far more: IMS and Lasertec sit inside high-margin tool businesses. So margin rises as you move upstream from the mask shop into the writer and the actinic inspector.

## Competitive landscape & value capture

Value accrues to chokepoint tool and material suppliers, not to the mask shops. The merchant mask business is a respectable mid-20s-operating-margin manufacturing business but it is capital-heavy and competes with foundries' own captive shops. The real moats are: the multi-beam writer (IMS, effectively single-source for leading edge), actinic EUV inspection (Lasertec, single-source), and EUV blanks and pellicles (AGC/Hoya duopoly; Mitsui near-sole pellicle maker). These are textbook picks-and-shovels positions on the EUV ramp.

European / seed angle: the leading-edge writer maker IMS Nanofabrication is Austrian (now Intel-owned, so not investable directly). imec (Belgium) anchors the CNT-pellicle roadmap with Mitsui. Genuine seed-stage entry into mask writing, actinic inspection, or EUV blanks is near-impossible (capital, IP, multi-decade incumbency). The credible early-stage wedges sit adjacent: novel pellicle membranes, mask-defect inspection software/AI, and computational approaches that reduce mask count or cost (see **Computational Litho Ai For Mask**).

## Market drivers, constraints & trends

Net read: the served pool (mask-shop tools plus EUV blanks and pellicles) grows mid-teens at the EUV edge while the broad merchant mask market plods at high single digits; the upside is concentrated in the consumable annuity and a one-off High-NA refresh, the downside in a thin two-supplier blank chain and export-control demand loss.

- **Drivers**
  - EUV layers per chip rise from ~14-18 at 5nm to 25-30+ at 2nm, multiplying blank and pellicle consumption per wafer-out, and AI/HPC pulls 3nm/2nm into high-volume manufacturing where almost every advanced part uses EUV [11].
  - High-NA brings a new high-value reticle class: 0.55 NA anamorphic optics need larger 6x10.5" half-field reticles versus 6x6", a fresh blank/pellicle spec, and a refresh cycle rather than a like-for-like swap [12][13].
  - 93% of mask professionals expect multi-beam writer purchases to rise over the next three years, driven by curvilinear/ILT masks whose write time is fixed regardless of shape complexity [14].
  - Recurring annuity: EUV blanks ~$835M in 2025 toward ~$1.94B by 2032 (~13% CAGR), EUV pellicles ~$558M (2024) to ~$1.6B (2030, ~14%) [15][5].
- **Constraints**
  - Two-supplier blank duopoly (AGC, Hoya) with defect densities above ~5/cm2 forcing scrap of up to 25% of EUV blanks at $50-100k each, capping throughput and inflating fab ramp cost [15].
  - Substrate chokepoint upstream: Shin-Etsu and Tosoh control 80%+ of ultra-low-expansion quartz, and Shin-Etsu's $545M Gunma capacity does not arrive until 2026 [15].
  - Export controls cut China off from EUV blanks, pellicles and Lasertec actinic inspection, removing the fastest-growing fab-build demand pool from the single-source vendors [15].
  - Curvilinear/ILT data-volume explosion strains mask data prep and inspection; full-chip curvilinear EUV write/inspect remains slow enough to gate cost and turnaround [14].
- **Trends & inflections to watch**
  - High-NA half-field reticles at Intel 14A and Samsung SF1.4. Tripwire: first High-NA high-volume tape-out (Intel/Samsung 2027-28) confirms the new blank/pellicle spec ramps; TSMC at A14 (~2028) is the volume switch [12][13].
  - CNT pellicles for 600W+ EUV sources (imec/Mitsui), transmitting >94% and surviving >1000W. Tripwire: first fab HVM qualification of a CNT pellicle (road-mapped 2025-26) re-rates the pellicle annuity upward [11].
  - Curvilinear ILT going mainstream at 2nm logic. Tripwire: a step-change in multi-beam writer bookings (IMS/NuFlare) as ILT becomes standard, lifting the writer pool above its ~12% trend [14].

## Connections

- [Mask Blank Manufacturing](/manufacturing/lithography/mask-blank-manufacturing/) - the upstream blank (quartz, multilayer, absorber) that this step patterns
- [Lithography](/manufacturing/lithography/lithography/) - the downstream scanner step the reticle feeds
- **Lithography Patterning Market** - the cluster thesis on where lithography/patterning value pools
- [Mask data prep & computational litho (OPC/ILT) (process step)](/semiconductor-process-flow/design/flow-mask-data-prep-opc/) - prior step that produces the write-ready data
- **Computational Litho Ai For Mask** - adjacent software wedge that affects mask count/cost

## Sources

1. IMARC / SNS / Verified Market - Photomask market ~$5.1-5.8B 2024, ~4-8% CAGR; Photronics ~35% / Toppan ~30% merchant share. https://www.imarcgroup.com/photomask-market
2. Valuates Reports - EUV mask blanks ~$591M (2024) to ~$1.36B (2031), 12.2% CAGR; AGC + Hoya ~93%. https://finance.yahoo.com/news/euv-mask-blanks-market-size-150100933.html
3. GMInsights / 360iResearch - Multi-beam mask writer ~$0.96B 2025, ~12% CAGR; IMS Nanofabrication ~82% (2024); NuFlare #2. https://www.gminsights.com/industry-analysis/multi-beam-e-beam-lithography-system-market
4. GMInsights / SemiEngineering - KLA ~28-34% and Lasertec ~22% of mask inspection; Lasertec sole actinic EUV inspection. https://www.gminsights.com/industry-analysis/euv-mask-inspection-market
5. Grand View / imec / Mitsui - EUV pellicle ~$558M 2024 to ~$1.6B 2030, ~14% CAGR; Mitsui under ASML license; imec+Mitsui CNT pellicles. https://www.grandviewresearch.com/industry-analysis/euv-pellicle-market-report
6. SemiEngineering - EUV mask ~$300k avg, $500k-$1M top end; optical ~$100k; recurring due to short reticle life. https://semiengineering.com/disruptive-changes-ahead-for-photomasks/
7. SemiconductorX / SemiWiki - Advanced mask set ~$5-15M, 60-100 masks. https://semiconductorx.com/semiconductor-photomasks.html
8. EE Times / SemiEngineering - TSMC largest captive mask maker; DNP largest overall; Toppan (Tekscend), DNP, Photronics merchant big three. https://www.eetimes.com/tsmc-claims-to-be-largest-captive-mask-maker/
9. Photronics FY2024 8-K - revenue ~$867M, ~25.6% operating margin. https://www.sec.gov/Archives/edgar/data/0000810136/000114036124048970/ef20039799_ex99-1.htm
10. Photronics Q4 FY2025 slides - revenue $215.8M, gross margin 35.0%, operating margin 24.1%, high-end 51% of revenue. https://www.investing.com/news/company-news/photronics-q4-2025-slides-record-ic-revenue-drives-earnings-beat-stock-surges-93CH-4401322
11. SemiEngineering / Reportprime - EUV layers rise 14-18 (5nm) to 25-30+ (2nm) multiplying pellicle consumption; AI/HPC drives 3nm/2nm EUV demand; CNT pellicles >94% transmission, >1000W. https://www.reportprime.com/euv-mask-blanks-r3197
12. Internet Pros / aminext - High-NA EXE:5200, 0.55 NA anamorphic, 6x10.5" half-field reticle vs 6x6"; Intel 14A / Samsung SF1.4 first adopters 2027-28. https://internet-pros.com/blog/high-na-euv-lithography-asml-twinscan-2026/
13. TrendForce - High-NA 2027-28 adoption: Intel/Samsung/SK hynix first, TSMC at A14 (~2028); reticle/blank refresh. https://www.trendforce.com/news/2026/02/16/news-asmls-high-na-euv-for-2027-28-which-giants-are-betting-big-intel-samsung-sk-hynix-or-tsmc/
14. SemiEngineering / eBeam Initiative - 93% expect multi-beam writer purchases to rise over 3 years; curvilinear ILT write time fixed vs shape complexity; curvilinear data-volume strain on mask data prep. https://semiengineering.com/multi-beam-writers-are-driving-euv-mask-development/
15. 360iResearch / IntelMarketResearch - EUV blanks ~$835M (2025) to ~$1.94B (2032), ~12.8% CAGR; AGC/Hoya only suppliers, >5/cm2 defects scrap up to 25% at $50-100k each; Shin-Etsu/Tosoh 80%+ of ULE quartz, Gunma capacity 2026; China export-control demand loss. https://www.intelmarketresearch.com/euv-mask-blanks-market-11463
