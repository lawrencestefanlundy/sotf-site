---
type: concept
slug: flow-wafer-sort-probe
canonical_name: Wafer sort / probe (process step)
seq: 40
phase: wafertest
related_concepts:
- probe-cards
- automated-test-equipment
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
neighbors:
- slug: probe-cards
  name: Wafer Probe Cards & Test Interconnect
  path: /manufacturing/equipment-processes/probe-cards/
  macro: manufacturing
- slug: automated-test-equipment
  name: Automated Test Equipment (ATE)
  path: /manufacturing/equipment-processes/automated-test-equipment/
  macro: manufacturing
---
> Step 40 of 56 in the semiconductor flow (WaferTest). Prev: [Parametric / in-line E-test (process step)](/semiconductor-process-flow/test-metrology/flow-parametric-e-test/) · Next: [Wafer backgrinding / thinning (process step)](/semiconductor-process-flow/packaging/flow-wafer-backgrind-thinning/)

## What this step does
Wafer sort (also called wafer probe, or circuit-probe / CP test) is the first time every individual die on a finished wafer is exercised as a working circuit, before the wafer is cut up. A prober steps the wafer under a probe card whose needles or MEMS tips touch the die bond pads; a tester (ATE) runs functional, structural and parametric vectors through those contacts and writes a pass/fail result into a wafer map. Bad die are inked or logged so they are discarded at assembly rather than packaged at cost. The sub-processes inside the step:
- **Probe-card-to-pad contact** by a prober at micron-scale alignment and controlled overdrive.
- **Functional / scan / BIST test** driven by the ATE pattern set (logic, SoC, memory built-in self-test).
- **At-speed and high-frequency test** for performance binning and speed sorting.
- **Wafer-map generation and bin inking** so downstream assembly only packages good die.

## Where it sits and why it matters
This is the gate between the wafer (front-end output) and assembly/packaging (back-end). It is distinct from the earlier [Parametric / in-line E-test (process step)](/semiconductor-process-flow/test-metrology/flow-parametric-e-test/), which measures process health on scribe-line structures; sort tests the actual product die. Its economic weight is rising fast because of chiplets and 2.5D/3D packaging: when eight HBM stacks and several compute tiles share one CoWoS interposer, a single bad die scraps a package that can cost USD 30,000 to build, so the industry needs Known Good Die (KGD) confidence before assembly, not after [4][5]. Value at this step accrues to the **test cell**: the tester, the prober, and above all the custom probe card that has become a binding supply constraint at the leading edge [3].

## Equipment market
The test cell splits into two equipment markets: ATE and probers.

ATE: global automated test equipment was about **USD 7.75bn in 2024**, projected to ~USD 10.2bn by 2030 at ~**4.8% CAGR** (Grand View); other houses put 2025 nearer USD 8.4bn [1]. Probers: about **USD 1.9bn in 2024**, ~6.7% CAGR [6].

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Advantest | Japan | ~31% ATE; ~95% duopoly w/ Teradyne [1][3] | Memory + HBM + high-end SoC; V93000 |
| Teradyne | US | ~23% ATE [1] | Logic / mobile / automotive SoC; UltraFLEX, J750 |
| Tokyo Electron (TEL) | Japan | Top-tier prober [3][6] | High-volume logic probers |
| Accretech (Tokyo Seimitsu) | Japan | Largest conventional prober share [6] | Test + back-end process breadth |
| SEMES (Samsung) | Korea | Captive / regional [3] | In-house prober supply |

Concentration note: ATE is a near-pure **duopoly (~95% Advantest + Teradyne)** split structurally, memory vs logic, not by negotiation [3]. Probers are a tighter Japan-centric oligopoly. Both are rough estimates from report-mill and trade sources, not Yole-precise.

## Materials & consumables
Sort consumes relatively little bulk material but a large recurring spend on **probe cards**, the custom interface between tester and wafer. The probe card market was about **USD 3.0-3.4bn in 2024** (estimates range USD 2.6-4.4bn across houses; ~USD 3.2bn is the central figure), with the **top five vendors holding ~64%** [2]. A leading-edge AI-accelerator probe card runs several hundred thousand dollars and wears out after hundreds of thousands of touchdowns, so it is genuinely recurring revenue, not a one-time tool sale [3].

| Vendor | HQ | Est. position | Notable |
|---|---|---|---|
| FormFactor | US | Co-leader [2] | Leading-edge logic + HBM, MEMS probes |
| Technoprobe | Italy | Co-leader [2] | Advanced logic / mobile SoC, AI-accelerator ramp |
| Micronics Japan (MJC) | Japan | Top-5 [2] | Memory parallelism (Samsung, SK hynix, Micron) |
| Japan Electronic Materials (JEM) | Japan | Tier-2 [2][3] | Memory / mid-range |
| MPI | Taiwan | Tier-2 [2] | Engineering + mid-range cards |

Other consumables: probe-tip cleaning materials, prober chucks/accessories, and contactor/load-board interface hardware.

## Volumes, revenue, profitability
The combined equipment-plus-consumables pool at this step is roughly **USD 13bn** (ATE ~USD 7.75bn + probers ~USD 1.9bn + probe cards ~USD 3.2bn). Asia-Pacific is ~79% of probe-card demand, tracking where foundry and memory capacity sits [2]. Margin profile of the value-capturing layer:
- **Advantest:** gross ~52%, operating ~20% (Q4 FY2024) [7].
- **Teradyne:** gross ~59%, operating ~20% (2024) [8].
- **FormFactor (probe cards):** segment gross ~41% FY2024, up from ~36% [9].
The testers earn the richest margins (duopoly pricing power, ~50-60% gross); probe cards earn lower gross but high stickiness because every new device needs a bespoke card. The margin sits with the IP-heavy tester duopoly and the design-locked probe-card incumbents, not with the prober mechanics.

## Market drivers, constraints & trends
Net read: this is one of the better-positioned steps in the flow, because test intensity is rising structurally faster than wafer volume, so the served pool grows even in a flat wafer-start year.
- **Drivers**
 - Test time per unit has jumped roughly 20-40x at the leading edge: a Blackwell-class accelerator can sit on the tester for over 20 minutes versus 30-60 seconds for a mobile SoC, and cost-of-test as a share of chip ASP has roughly tripled from under 2% toward 5-7% on the most complex AI packages [10].
 - Advantest puts the SoC-tester market at USD 6.9bn in CY25 rising to USD 8.7-9.5bn in CY26 and is ramping capacity from 7,500 to 10,000 systems a year to keep pace with Blackwell Ultra, MI400 and HBM4 [11]; Advantest's own SoC-tester share jumped from ~56% to ~66% in CY25 by sitting inside the AI-accelerator supply chain, evidence that test capture is concentrating where the AI content is [16].
 - HBM4 raises probe counts and cuts allowable pitch versus HBM3E, and chiplet/2.5D assembly means one bad die can scrap a USD 30k package, both of which pull probe-card content per wafer up [12].
- **Constraints**
 - The end-mix is still cyclical: PC and smartphone test demand is soft, which is why FormFactor is steering toward memory, automotive-power and photonics, targeting non-foundry/logic above 30% of sales by end-2026 [13].
 - China export controls and counter-cyclical domestic equipment build-out (local share 25%->35% 2024-2025) risk a sealed-off China test market served by domestic probers/cards rather than the incumbents [14].
 - Supply is consolidating: the Jan 2025 Advantest-FormFactor-Technoprobe partnership tightens the probe-card oligopoly and raises qualification lock-in [13].
- **Trends & inflections to watch**
 - Optical wafer test for silicon photonics / co-packaged optics is the new content layer: FormFactor launched the TRITON SiPh test system at OFC 2025 (co-developed with Advantest + TEL) and acquired Keystone Photonics in Dec 2025. Tripwire already tripping: in April 2026 foundries (TSMC, Tower) confirmed wafer-level optical test is now a mandatory gating step for CPO-destined silicon, which turns optical sort from optional R&D into a required production step and opens a fresh probe-card/ATE category [15][17].
 - HBM stack height climbing 12->16 layers with HBM4. Tripwire: HBM4 entering volume production at SK hynix/Micron in 2026 lifting probe-card DRAM revenue to fresh records [12].

## Connections
- [Wafer Probe Cards & Test Interconnect](/manufacturing/equipment-processes/probe-cards/) - the recurring consumable that captures much of the value at this step.
- [Automated Test Equipment (ATE)](/manufacturing/equipment-processes/automated-test-equipment/) - the tester duopoly that anchors the test cell.
- **Known Good Die Test Wedge** - thesis: rising KGD intensity from chiplets/HBM as the growth driver.
- **Back End Test Equipment No Wedge** - thesis: test/assembly capex grows off the lithography area-scaling treadmill.

## Sources
1. Grand View Research, Automated Test Equipment Market - https://www.grandviewresearch.com/industry-analysis/automated-test-equipment-market
2. Market Research Future / Global Growth Insights, Probe Card Market - https://www.marketresearchfuture.com/reports/probe-card-market-17763
3. SemiconductorX, Wafer Test (Sort): ATE Duopoly & Probe Card Supply - https://semiconductorx.com/mfg-back-end-testing.html
4. FormFactor, Wafer Test Challenges and Solutions (2025) - https://www.formfactor.com/blog/2025/wafer-test-challenges-and-solutions/
5. Silicon Analysts, CoWoS Packaging Cost / chiplet vs monolithic test (2026) - https://siliconanalysts.com/analysis/cowos-packaging-cost-chiplet-vs-monolithic-2026
6. Mordor / Stratview, Wafer Prober Market - https://www.mordorintelligence.com/industry-reports/wafer-prober-market
7. Macrotrends, Advantest gross/operating margin - https://www.macrotrends.net/stocks/charts/ATEYY/advantest/gross-margin
8. Macrotrends, Teradyne operating margin - https://m.macrotrends.net/stocks/charts/TER/teradyne/operating-margin
9. FormFactor FY2024 10-Q, probe-card segment gross margin - https://www.sec.gov/Archives/edgar/data/0001039399/000103939924000035/form-20240928.htm
10. Data Gravity, The Chip Testing Bottleneck (test time + cost-of-test growth) - https://www.datagravity.dev/p/the-chip-testing-bottleneck
11. Data Gravity / Advantest guidance, SoC tester market CY25-CY26 + 10k-system ramp - https://www.datagravity.dev/p/the-chip-testing-bottleneck
12. FinancialContent, The Testing Wall: FormFactor in the HBM4 Era (probe count / pitch) - https://markets.financialcontent.com/stocks/article/finterra-2026-3-25-the-testing-wall-a-comprehensive-analysis-of-formfactor-inc-form-in-the-hbm4-era
13. FormFactor Q1 FY2026 earnings 8-K + Jan 2025 Advantest/FormFactor/Technoprobe partnership - https://www.sec.gov/Archives/edgar/data/0001039399/000103939926000020/ex9901-earningsreleasexq126.htm
14. CSIS, China localization drive in semiconductors under export controls - https://www.csis.org/analysis/chinas-localization-drive-semiconductors-gains-impetus-allied-chip-export-controls
15. FormFactor, Pioneering high-throughput wafer testing for silicon photonics with TRITON + Keystone Photonics acquisition - https://www.formfactor.com/blog/2025/pioneering-high-throughput-wafer-testing-for-silicon-photonics-with-triton/
16. RCR Wireless, Advantest rises with the AI tide (SoC tester share 56%->66% CY25) - https://www.rcrwireless.com/20260130/test-measurement/advantest-rises-with-the-ai-tide
17. FormFactor, TRITON - Scaling silicon photonics wafer test for high-volume manufacturing (Apr 2026 foundry gating step for CPO) - https://www.formfactor.com/blog/2026/triton-scaling-silicon-photonics-wafer-test-for-high-volume-manufacturing/
