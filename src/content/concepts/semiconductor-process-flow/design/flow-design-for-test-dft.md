---
type: concept
slug: flow-design-for-test-dft
canonical_name: Design-for-test (DFT) (process step)
seq: 6
phase: design
related_concepts:
- eda-design-tools
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
- slug: eda-design-tools
  name: EDA & Design Tools
  path: /manufacturing/foundry-design/eda-design-tools/
  macro: manufacturing
- slug: automated-test-equipment
  name: Automated Test Equipment (ATE)
  path: /manufacturing/equipment-processes/automated-test-equipment/
  macro: manufacturing
---
> Step 6 of 56 in the semiconductor flow (Design). Prev: [Logic synthesis (process step)](/semiconductor-process-flow/design/flow-logic-synthesis/) · Next: [Floorplanning & power planning (process step)](/semiconductor-process-flow/design/flow-floorplanning-power/)

## What this step does
DFT inserts dedicated test structures into the gate-level netlist so the manufactured chip can be checked for defects cheaply on a tester later. It runs after synthesis and before physical design, adding logic that has no functional purpose but makes internal nodes observable and controllable. Where value accrues: this is software, sold by the same three EDA houses that own the rest of the design flow, and the structures it inserts are what later let expensive testers (ATE) run short, so DFT quality directly sets a fab customer's per-die test cost.
- Scan insertion: stitch flip-flops into shift registers (scan chains) so internal state can be loaded and read out.
- ATPG (automatic test pattern generation): compute the input vectors that expose stuck-at, transition and bridging faults, then compress them.
- Test compression: codec logic (e.g. Tessent TestKompress, Synopsys DFTMAX) that cuts pattern count and tester time, often 50-100x.
- MBIST / memory BIST: self-test engines built around on-chip SRAM/embedded memory, plus repair (BIRA/BISR).
- Logic BIST, boundary scan (JTAG / IEEE 1149.1), and increasingly in-system / in-field test and silicon lifecycle monitors.

## Where it sits and why it matters
DFT is a small slice of EDA spend but a large lever on manufacturing economics. A 1-2% silicon-area cost at design time can remove tens of percent of tester time downstream, and tester time is the dominant variable cost of test. As designs move to advanced nodes, chiplets and 3D stacks, untestable die are unsellable, so DFT has shifted from a back-end afterthought to an early ("shift-left") RTL concern. It is the hinge between the design world (EDA) and the test-floor world (ATE): the patterns DFT generates are the program the [tester](/manufacturing/equipment-processes/automated-test-equipment/) runs.

## Equipment market
There is no hardware "equipment" here; the tools are EDA software. The total EDA+IP market is roughly $18B in 2025, growing ~9-13% CAGR (SemiAnalysis; multiple report mills cluster 8-10%) [1][2][6]. The test-automation / DFT sub-segment is not separately disclosed by the vendors; a defensible estimate is ~5-8% of core EDA, i.e. roughly $0.8-1.4B in annual licence revenue (rough estimate, triangulated from the segment never being broken out and DFT being one of ~8 tool categories) [1][6].

| Vendor | HQ | Est. DFT share | Notable |
|--------|-----|----------------|---------|
| Siemens EDA (Tessent) | Germany / US (Wilsonville OR) | clear leader, ~50-60% (est.) | Tessent ScanPro, TestKompress, MemoryBIST, RTL Pro; the reference DFT tool at most fabless firms |
| Synopsys (TestMAX) | US (Sunnyvale) | #2, ~25-35% (est.) | TestMAX DFT/ATPG, formerly DFTMAX; bundled with the dominant synthesis/signoff flow |
| Cadence (Modus) | US (San Jose) | #3, smaller (est.) | Modus DFT; comprehensive but trails on DFT specifically |

Concentration note: the same big-three that hold >85% of all EDA hold essentially all of DFT [2][6]. DFT is the one major flow step where Siemens, generally the #3 EDA house overall (~13% total share), is the market leader, a legacy of the Mentor Graphics test franchise [2][4].

## Materials & consumables
Software, so no physical consumables. The recurring-revenue analogue is the licence model: EDA is sold as multi-year time-based licences (TBLs), so DFT revenue is sticky, ratable and renews. The true downstream "consumable" the step drives is tester time on ATE and the test patterns themselves, billed per second of [machine time](/manufacturing/equipment-processes/automated-test-equipment/) in an OSAT or in-house test floor. Better compression = fewer tester-seconds = lower cost-of-test per die, which is why fabless customers pay up for DFT quality.

## Volumes, revenue, profitability
Volume is measured in seats/licences and tape-outs, not units. Revenue pool: ~$0.8-1.4B/yr DFT licences (rough estimate) sitting inside an ~$18B EDA market [1][6]. The margin profile is the attraction: leading EDA vendors run ~80-90% gross margins and ~30-40% operating margins (Synopsys and Cadence both report GAAP operating margins in the low-to-mid 30s and non-GAAP in the 30-40s) [2][7]. Margin is captured almost entirely by the three EDA vendors; the value DFT creates (lower test cost) is realised by the fabless designer and the OSAT, but the tool licence is where the software profit pools.

## Competitive landscape & value capture
Moat: deep, multi-decade. DFT tools must be certified against every foundry's test methodology, integrate with the customer's synthesis and signoff flow, and be trusted on billion-transistor tape-outs where a missed fault class means field returns. Switching cost is high and the install base is locked to the rest of the EDA flow. Value accrues to the incumbent software layer (Siemens/Synopsys/Cadence), not to the tester makers (Advantest, Teradyne) who sit downstream and capture the much larger ~$8B ATE hardware pool but at lower margins and on a slower ~3% CAGR [3][5].

EU / seed-relevant angle: Siemens EDA is nominally German-headquartered but R&D-rooted in the US, so it is not an EU sovereignty play. The live disruption is silicon lifecycle management and in-field test (proteanTecs, Israel; plus the incumbents' SLM suites), pushing test from a one-time gate into continuous in-system telemetry. A genuinely independent DFT/ATPG startup is rare because the big-three bundle locks the flow; the more fundable EU/seed wedge sits adjacent (on-chip monitors, embedded analytics IP, AI-accelerator-specific test) rather than head-on against Tessent.

## Market drivers, constraints & trends
Net read: a small, sticky software pool riding two genuinely accelerating tailwinds (AI-accelerator test economics and chiplet test) but capped by the same oligopoly bundling that protects it, so the served market grows faster than core EDA without re-rating much on its own.

- **Drivers**
  - AI-accelerator test economics are exploding the value of DFT. A Blackwell-class part (two reticle-limited dies, eight HBM3E stacks, ~1,000W) can sit 20+ minutes on a tester, an order of magnitude more machine-hours per unit than a phone SoC; HBM alone can be 50% of package cost, so known-good-die assurance and dedicated HBM BiST are now mandatory, not optional [8][9].
  - Chiplets and 3D stacks multiply test points (every die-to-die link must be validated); the chiplet market is forecast to compound >40%/yr, pulling demand for IEEE 1838 multi-die DFT and die-to-die interconnect test [9][10].
  - In-field / silicon-lifecycle-management telemetry is a new recurring layer on top of one-time test: SLM is put at ~$1.0-2.3B in 2025 growing ~9% CAGR, driven by AI/cloud/5G reliability needs (Synopsys, Siemens, proteanTecs) [11][12].

- **Constraints**
  - Three-vendor oligopoly. DFT is bundled into the EDA flow and never separately monetised, so the segment captures only a sliver of the value it creates (lower tester-seconds accrue to the OSAT/fabless designer) and pricing power is the flow's, not DFT's [1][6].
  - Export controls are a live revenue tail-risk: the May 2025 BIS curbs briefly forced China licences on all three (China ~16% of Synopsys, ~12% of Cadence FY24 revenue) before being lifted in July 2025; the on-off pattern caps the China growth assumption [13][14].
  - Commoditisation pressure from "good enough" bundled ATPG limits any standalone DFT entrant; the moat is also the ceiling.

- **Trends & inflections to watch**
  - Shift-left to RTL DFT (Tessent RTL Pro, Synopsys RTL flows) moves insertion earlier and compresses schedules; AI-assisted test-point insertion already shows ~10x faster ATPG and ~2x pattern reduction, and at the May 2026 Samsung SAFE Forum Synopsys put TestMAX AI-assisted ATPG at up to ~20% test-efficiency gain, with AI embedded (no separate SKU, learns across designs) [15][16][17]. Tripwire: a vendor disclosing AI-ATPG as a named, separately-priced SKU or quantified attach-rate by 2027 would signal DFT pricing finally decoupling from the synthesis bundle, the AI-embedded-no-extra-charge framing so far points the other way [16][17].
  - SLM transition from one-time gate to continuous in-system monitoring. Tripwire: a hyperscaler or AI-accelerator vendor publicly standardising on embedded on-chip monitors / SLM telemetry in a flagship part would confirm the recurring-revenue layer [11][12].
  - Chiplet test standardisation. Tripwire: first high-volume multi-vendor chiplet product shipping under IEEE 1838 interconnect test (vs proprietary) would mark DFT demand broadening beyond single-die ATPG [9][10].

## Connections
- [EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/) — DFT is one tool category inside the EDA flow.
- [Automated Test Equipment (ATE)](/manufacturing/equipment-processes/automated-test-equipment/) — DFT generates the patterns the tester runs; the two markets are coupled.
- **Eda Chip Design** — the broader thesis on design-software value capture.

## Sources
1. SemiAnalysis, EDA Market Primer — https://newsletter.semianalysis.com/p/eda-market-primer
2. Klover.ai / report-mill synthesis on EDA shares (Synopsys ~31%, Cadence ~30%, Siemens ~13%) — https://www.klover.ai/synopsys-ai-strategy-analysis-of-dominance-in-tools-services-for-semiconductor-design-manufacturing/
3. Future Market Insights / Global Growth Insights, ATE market ~$8.2B 2025 — https://www.globalgrowthinsights.com/market-reports/automated-test-equipment-ate-market-110692
4. Siemens, Tessent Test Solutions (scan, ATPG, MBIST, RTL Pro) — https://eda.sw.siemens.com/en-US/ic/tessent/test/
5. Mordor Intelligence, Semiconductor Test Equipment Market (Advantest/Teradyne shares, ~3% CAGR) — https://www.mordorintelligence.com/industry-reports/semiconductor-test-equipment-market
6. The Business Research Company, EDA Market Report 2026 (~$18B 2026, ~9% CAGR) — https://www.thebusinessresearchcompany.com/report/electronic-design-automation-eda-global-market-report
7. Synopsys, TestMAX DFT datasheet — https://www.synopsys.com/content/dam/synopsys/resources/eda/test-automation/testmax-dft-ds.pdf
8. Semiconductor Engineering, AI Accelerator Testing Depends On DFT Innovations (Blackwell-class ~20min tester time, HBM ~50% of package cost, dedicated HBM BiST) — https://semiengineering.com/ai-accelerator-testing-depends-on-dft-innovations/
9. Semiengineering / 3DInCites, Chiplet integration and 3D-IC test, IEEE 1838 multi-die DFT — https://semiengineering.com/chiplet-integration-and-testing-key-lessons-for-next-gen-semiconductor-packaging/
10. Future Market Insights, Chiplet Integration & Die-to-Die Interconnect Test Solutions Market (chiplet market >40% CAGR) — https://www.futuremarketinsights.com/reports/chiplet-integration-and-die-to-die-interconnect-test-solutions-market
11. QY Research, Silicon Lifecycle Management (SLM) Market (~$995M 2024 → ~$1.84B 2031, ~9.3% CAGR; Synopsys/Siemens/proteanTecs) — https://www.qyresearch.com/reports/4646332/silicon-lifecycle-management--slm
12. WiseGuy Reports / Synopsys SLM (SLM ~$2.34B 2025 → ~$5.5B 2035, ~8.9% CAGR; AI/cloud/5G drivers) — https://www.synopsys.com/solutions/silicon-lifecycle-management.html
13. TrendForce, China revenue at risk as US EDA curbs hit Synopsys/Cadence/Siemens (China ~16% SNPS, ~12% CDNS FY24) — https://www.trendforce.com/news/2025/06/02/news-china-revenue-at-risk-as-u-s-curbs-slam-eda-giants-impact-on-synopsys-cadence-and-more/
14. Design-Reuse, Synopsys/Cadence/Siemens resume EDA supply to China (BIS lifts curbs Jul 2025) — https://www.design-reuse.com/news/202528998-synopsys-cadence-and-siemens-resume-eda-supply-to-china/
15. Siemens Tessent, Shift Left in DFT Design / RTL Pro (RTL-level DFT insertion) — https://blogs.sw.siemens.com/tessent/2025/04/10/shift-left-in-dft-design/
16. Siemens Tessent, Slashing DFT/ATPG time for AI chips (~10x faster ATPG, ~2x pattern reduction, ~30% pattern cut via test points) — https://blogs.sw.siemens.com/tessent/2019/02/01/meet-aggressive-time-to-market-for-ai-chips-by-slashing-dft-time/
17. Synopsys, AI & HPC chip test solutions / TestMAX AI-assisted ATPG (Samsung SAFE Forum, May 2026; up to ~20% test-efficiency gain, AI embedded with no separate model maintenance, learns across designs) — https://www.synopsys.com/blogs/chip-design/ai-hpc-chip-test-solutions-seq-compression-streaming-fabric.html
