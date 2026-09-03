---
type: concept
slug: euv-light-sources
canonical_name: EUV Light Sources
aliases:
- euv
kind: technology
parent_concepts:
- manufacturing
- lithography
related_concepts: []
sources:
- '[[2026-07-07-the-asml-killer]]'
- '[[2026-05-02-energetiq-euv-light-sources]]'
frontier:
- What is the current delivered in-band source power, conversion efficiency and availability, and does High-NA EUV require more source power per exposure than the 0.33-NA generation?
- Is the light source, rather than optics or precision stages, the binding constraint on ASML's sub-100-unit annual output?
- Could a free-electron-laser source of the kind demonstrated with sub-microjoule seeding 2026 05 28 fully coherent short wavelength free electron laser driven b ever reach lithographic average power and cost per photon, or is the repetition-rate and stability gap structural?
- If the MATCH Act passes and bans maintenance of previously sold machines 2026 06 24 sovereignty semi bifurcation dutch government irritated by, how quickly does an unserviced installed base lose usable source uptime?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 4
last_reorg_date: '2026-05-13'
scorecard:
  viability: 4
  drivers: 4
  novelty: 3
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-17-the-once-and-future-kimi
  title: The Once and Future Kimi
  date: '2026-07-17'
  kind: substack
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-07-the-asml-killer
  title: The ASML Killer?
  date: '2026-07-07'
  kind: substack
- slug: 2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology
  title: IBM Debuts World's First Sub-1 Nanometer Chip Technology
  date: '2026-06-25'
  kind: web
- slug: 2026-06-24-sovereignty-semi-bifurcation-dutch-government-irritated-by
  title: Dutch government irritated by U.S. plans for new ASML export restrictions
  date: '2026-06-24'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-19-sovereignty-semi-bifurcation-us-tells-asml-it-has-evidence
  title: US Tells ASML It Has Evidence EUV Lithography Tool Reached China
  date: '2026-06-19'
  kind: web
neighbors: []
---
**The EUV light source is the plasma-based subsystem that generates extreme-ultraviolet photons inside a lithography scanner, and because its power and uptime set wafer throughput it sits underneath what analysts now call the single durable ceiling on AI compute scaling.**

## Summary

Extreme-ultraviolet lithography prints the smallest features in modern logic and memory by exposing wafers with photons far shorter in wavelength than the deep-ultraviolet light used previously. The hard part is making those photons in industrial quantity. EUV is absorbed strongly by essentially all materials, which is why the field has almost no transmissive optics at these wavelengths and why optics research is still working on basic components: a 2026 demonstration of the first broadband transmissive EUV metagrating describes strong material absorption as the limiting factor and reports phase-based operation up to 50 eV photon energy with an octave-spanning 25 eV bandwidth. The production answer to photon generation is laser-produced plasma (LPP): a high-power drive laser strikes a target to create a hot plasma that radiates in the EUV band <sup class="ref"><a href="https://www.sciencedirect.com/science/article/pii/S270947232200017X" title="Laser-produced plasma EUV development (ScienceDirect)" rel="noopener">ref</a></sup>.

The parameters that decide the technology are source power (photons per second delivered to the wafer, which sets exposure time and therefore wafers per hour), collector and optics efficiency, and availability, because a scanner costing tens of millions of euros is worthless while its source is down. None of those numbers appear in the sources supplied here, and that is the single biggest gap in this assessment: the sources establish the industrial and geopolitical position of EUV very well and its source-level engineering not at all.

What the sources do establish is the economic frame. EUV lithography is a single-vendor business: ASML guides to 51-53% gross margin in 2026 with a 2030 target of 56-60%, margins that hold through the cycle <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/937966/000162828026025147/presentationinvestorrela.htm" title="ASML Q1 2026 Earnings: Margin Stability in Lithography Monopoly" rel="noopener">ref</a></sup>, on 2026 revenue guidance of EUR 36-40bn <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/937966/000162828026025147/pressreleasefinancialresul.htm" title="ASML Holding NV - Form 6-K - FY2026 Q1 Results and Guidance" rel="noopener">ref</a></sup>. SemiAnalysis frames AI-compute scaling as gated by three rotating bottlenecks (logic/lithography, memory, power) and pins the long-run ceiling to ASML producing fewer than roughly 100 EUV machines a year, with the binding constraint shifting from advanced packaging to EUV post-2028 <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>. Every EUV machine that ships needs a working light source, so source output rate and source throughput are upstream of that ceiling.

There are alternative EUV generation architectures in the physics literature. A 2026 experiment demonstrated a fully coherent echo-enabled harmonic generation free-electron laser driven by a single sub-microjoule seed, removing the hundred-megawatt peak-power laser systems and dual-laser synchronisation that previously restricted such machines to kilohertz repetition rates. That work targets time-resolved ultrafast spectroscopy, not lithography, and the sources make no claim about FEL sources reaching lithographic power or cost.

## Viability (4/5)

The deployment evidence is solid. EUV-patterned 300 mm CMOS is being used well beyond mainstream logic: a 7x7 silicon quantum dot array of 392 dots was fabricated in a 300 mm CMOS process patterned by EUV lithography and characterised statistically. High-NA EUV is past the demonstration stage as a research tool, appearing as ASML's named contribution to IBM's Nanostack 0.7 nm architecture announced in June 2026 <sup class="ref"><a href="https://newsroom.ibm.com/2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology" title="IBM Debuts World's First Sub-1 Nanometer Chip Technology" rel="noopener">ref</a></sup>, with ASML's own planning putting first commercial EXE:5000 shipments in 2024-2025 and volume in 2027+ **2024 Asml Investor Day Export Controls**.

The score is held at 4 rather than 5 because the supplied sources contain no source-level engineering data at all: no in-band power figure, no conversion efficiency, no collector lifetime, no availability statistic, no comparison of LPP against discharge-produced plasma or FEL architectures for lithography duty. The LPP development review is indexed but not cached <sup class="ref"><a href="https://www.sciencedirect.com/science/article/pii/S270947232200017X" title="Laser-produced plasma EUV development (ScienceDirect)" rel="noopener">ref</a></sup>. A reader wanting to know whether source power is currently the throughput limiter, or whether High-NA optics demand more of the source, cannot answer that from this evidence base.

**TLDR: EUV is unambiguously in volume production; the sources say nothing about source power, conversion efficiency or uptime.**

## Drivers (4/5)

Demand: SemiAnalysis places lithography as the ultimate ceiling on AI compute post-2028 into 2030, with the acute constraint rotating from HBM and CoWoS packaging (sold out through 2026) and power build-out towards EUV <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>. Buyer capex is committed at scale: TSMC's Arizona campus carries USD 65bn+ of announced capex plus USD 6.6bn CHIPS grants and USD 5bn loan capacity **2024 Tsmc Arizona Capex Disclosure**, and Intel's Terafab foundry expansion is described as needing on the order of more than USD 100bn, prompting the argument that Intel should raise roughly USD 25bn of equity into strength amid an AI-driven wafer shortage <sup class="ref"><a href="https://newsletter.semianalysis.com/p/intel-should-raise-capital" title="Intel Should Raise Capital" rel="noopener">ref</a></sup>.

Supply: the constraint is the tool builder's unit output, put at fewer than roughly 100 EUV machines per year <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>, with margins that expand rather than compress through the cycle (51-53% in 2026, target 56-60% by 2030) <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/937966/000162828026025147/presentationinvestorrela.htm" title="ASML Q1 2026 Earnings: Margin Stability in Lithography Monopoly" rel="noopener">ref</a></sup> - the signature of a supply-constrained chokepoint rather than a competitive market. Policy trims the addressable market rather than the demand: China revenue is expected to normalise to about 20% of sales in 2026 from 33% in 2025 <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/937966/000162828026025147/pressreleasefinancialresul.htm" title="ASML Holding NV - Form 6-K - FY2026 Q1 Results and Guidance" rel="noopener">ref</a></sup>. What the sources do not tell us is whether the light source specifically, versus optics, precision stages or assembly labour, is the binding constraint on that ~100-unit rate.

**TLDR: Demand is being pulled hard by AI compute; supply is capped at fewer than about 100 machines a year.**

## Novelty (3/5)

The clearest comparator in the sources is not another EUV source but the absence of EUV. TechInsights confirmed SMIC N+3 in volume production at a 5 nm-class node using only DUV multi-patterning <sup class="ref"><a href="https://www.techinsights.com/blog/smic-n3-confirmed-kirin-9030-analysis-reveals-how-close-smic-5nm" title="SMIC N+3 Confirmed: Kirin 9030 Analysis Reveals How Close SMIC Is to 5nm" rel="noopener">ref</a></sup>, and a teardown analysis puts N+3 at a ~32.5 nm minimum M0 metal pitch, roughly 10% tighter than Intel 18A's 36 nm, at roughly TSMC N6-class logic density of ~113 MTr/mm2 - achieved at a steep price in process complexity, mask count, efficiency and process control versus EUV-based nodes <sup class="ref"><a href="https://newsletter.semianalysis.com/p/steel-smic-n3-teardown" title="Is SMIC N+3's Metal Pitch Smaller than Intel 18A's?" rel="noopener">ref</a></sup>. That bounds the claim: EUV wins on economics, mask count and yield, not because DUV cannot reach the pitch. It also means the value of a better EUV light source is measured in cost per printed layer, not in feature sizes nobody else can reach.

On the source architecture itself the sources do not support an assessment. LPP is identified as the development line <sup class="ref"><a href="https://www.sciencedirect.com/science/article/pii/S270947232200017X" title="Laser-produced plasma EUV development (ScienceDirect)" rel="noopener">ref</a></sup> but no efficiency or power numbers are given, and the seeded EEHG free-electron laser result - a genuine simplification, replacing hundred-megawatt peak-power seed lasers with a single sub-microjoule seed and removing dual-laser synchronisation - is presented for ultrafast spectroscopy, with no lithography power, cost or repetition-rate comparison offered.

**TLDR: EUV's edge over DUV multi-patterning is cost and complexity, not an absolute resolution wall; source architecture alternatives are unassessed.**

## Diffusion (4/5)

There is no adoption question at the leading edge: EUV appears in production logic, in the roadmap for sub-1 nm architectures via High-NA at IBM's Albany complex <sup class="ref"><a href="https://newsroom.ibm.com/2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology" title="IBM Debuts World's First Sub-1 Nanometer Chip Technology" rel="noopener">ref</a></sup>, and in research-scale 300 mm quantum device fabrication. The barriers are all on the supply and permission side. Unit output of fewer than ~100 machines a year rations access <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>; capital intensity rations buyers, with the second Western leading-edge supplier needing >USD 100bn for its buildout <sup class="ref"><a href="https://newsletter.semianalysis.com/p/intel-should-raise-capital" title="Intel Should Raise Capital" rel="noopener">ref</a></sup> and TSMC's Arizona phases slipping on construction, labour disputes and skilled-worker shortages **2024 Tsmc Arizona Capex Disclosure**.

Policy is the sharpest barrier and it is getting sharper, not looser. EUV NXE platforms have been export-controlled to China across the October 2022, October 2023 and December 2024 BIS rounds **2024 Bis Export Controls China Semis**, and ASML's own planning assumes EUV shipments to China stay blocked through at least 2027 in the central case and 2030 in the conservative case **2024 Asml Investor Day Export Controls**. As of June 2026 the US Commerce Secretary had accused ASML of circumventing restrictions with EUV systems reaching China, and the proposed MATCH Act would let the US determine allied countries' chip exports and ban maintenance of machines already sold <sup class="ref"><a href="https://nltimes.nl/2026/06/24/dutch-government-irritated-us-plans-new-asml-export-restrictions" title="Dutch government irritated by U.S. plans for new ASML export restrictions" rel="noopener">ref</a></sup>. A maintenance ban is specifically a light source and consumables issue, since these tools require continuous servicing.

**TLDR: Adopted by every Western leading-edge fab that can get a tool; the barriers are unit output, capital and export policy, not willingness.**

## Impact (4/5)

If EUV source power and availability improve, wafers per hour per tool rises and the effective supply of leading-edge silicon rises without new tool units - directly relaxing the constraint SemiAnalysis identifies as the ultimate ceiling post-2028, ahead of power (judged solvable via aeroderivative turbines, fuel cells and behind-the-meter generation) and memory (large but not the durable ceiling, absorbing about 30% of hyperscaler capex by 2026) <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>. The value captured at this chokepoint is visible in the margin structure: 51-53% gross margin in 2026 rising to a 56-60% 2030 target on EUR 36-40bn of 2026 revenue <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/937966/000162828026025147/presentationinvestorrela.htm" title="ASML Q1 2026 Earnings: Margin Stability in Lithography Monopoly" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/937966/000162828026025147/pressreleasefinancialresul.htm" title="ASML Holding NV - Form 6-K - FY2026 Q1 Results and Guidance" rel="noopener">ref</a></sup>.

The cap on the score is that impact runs through the whole scanner, and the sources do not isolate the light source's contribution. Nor do they quantify how much headroom exists: without a current in-band power figure or a High-NA power requirement, the size of the prize from a better source is not calculable from this evidence. The counterweight is SMIC's demonstration that competitive density is achievable without EUV at a cost penalty <sup class="ref"><a href="https://newsletter.semianalysis.com/p/steel-smic-n3-teardown" title="Is SMIC N+3's Metal Pitch Smaller than Intel 18A's?" rel="noopener">ref</a></sup>, which caps the counterfactual damage of EUV stagnating.

**TLDR: Throughput of EUV exposure sets the ceiling on leading-edge wafer supply, which analysts now place above memory and power as the durable limit on AI compute.**

## Timing Now (0-2yr)

This is not an emerging technology; it is an operating chokepoint. EUV is already patterning production logic and research CMOS, and ASML's planning had first commercial High-NA EXE:5000 shipments in 2024-2025 with volume in 2027+ **2024 Asml Investor Day Export Controls**. The commercially decisive window for source improvements is therefore immediate: any gain in power or availability shows up in wafer supply within the current tool fleet.

The strategic timing is a step later. SemiAnalysis puts the acute constraint in 2025-26 on HBM and CoWoS packaging and on grid power, with the ceiling moving to EUV lithography post-2028 into 2030 <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>. Node roadmaps that depend on High-NA reach production later still: IBM projects a Nanostack production pathway within about five years, i.e. around 2031 <sup class="ref"><a href="https://newsroom.ibm.com/2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology" title="IBM Debuts World's First Sub-1 Nanometer Chip Technology" rel="noopener">ref</a></sup>.

**TLDR: In volume production today, with the High-NA generation ramping to volume from 2027 and the supply constraint binding hardest post-2028.**

## Overrated or underrated? Fairly rated

The market and the analyst consensus have converged on the same view and the evidence supports it: EUV is a single-supplier chokepoint whose unit output, put at fewer than roughly 100 machines a year, is the crisp long-run cap on AI compute <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>, and the pricing power that implies is visible in margins guided up rather than down through the cycle <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/937966/000162828026025147/presentationinvestorrela.htm" title="ASML Q1 2026 Earnings: Margin Stability in Lithography Monopoly" rel="noopener">ref</a></sup>. There is no discount to exploit and no obvious hype to deflate.

Two qualifications matter. First, the SMIC N+3 result should temper the strongest version of the EUV-as-absolute-barrier claim: a 5 nm-class node in volume production on DUV multi-patterning at ~32.5 nm M0 pitch and ~113 MTr/mm2 <sup class="ref"><a href="https://www.techinsights.com/blog/smic-n3-confirmed-kirin-9030-analysis-reveals-how-close-smic-5nm" title="SMIC N+3 Confirmed: Kirin 9030 Analysis Reveals How Close SMIC Is to 5nm" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://newsletter.semianalysis.com/p/steel-smic-n3-teardown" title="Is SMIC N+3's Metal Pitch Smaller than Intel 18A's?" rel="noopener">ref</a></sup> shows the gap is economic and yield-related rather than physical, which is a weaker moat than the monopoly framing implies. Second, on the light source subsystem specifically these sources support no view at all. Anyone underwriting the throughput half of the EUV thesis - the part that depends on source power and availability rather than tool count - is doing so on evidence not present here, and that is the honest limit of this page.

## Prediction

By 31 December 2029, no EUV lithography exposure tool using a light source architecture other than laser-produced plasma will be in volume semiconductor production, and annual EUV system shipments will remain below 100 units.

## Evidence base

- SemiAnalysis pins the long-run ceiling on AI compute to ASML producing fewer than roughly 100 EUV machines a year, with the binding constraint shifting from CoWoS packaging to EUV post-2028 (14 Mar 2026) <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>.
- ASML guides 51-53% gross margin for 2026 with a 2030 target of 56-60%, on 2026 revenue guidance of EUR 36-40bn and China normalising to ~20% of sales from 33% in 2025 (15 Apr 2026) <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/937966/000162828026025147/presentationinvestorrela.htm" title="ASML Q1 2026 Earnings: Margin Stability in Lithography Monopoly" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/937966/000162828026025147/pressreleasefinancialresul.htm" title="ASML Holding NV - Form 6-K - FY2026 Q1 Results and Guidance" rel="noopener">ref</a></sup>.
- TechInsights confirmed SMIC N+3 in volume production at a 5 nm-class node using DUV multi-patterning only, no EUV (11 Dec 2025) <sup class="ref"><a href="https://www.techinsights.com/blog/smic-n3-confirmed-kirin-9030-analysis-reveals-how-close-smic-5nm" title="SMIC N+3 Confirmed: Kirin 9030 Analysis Reveals How Close SMIC Is to 5nm" rel="noopener">ref</a></sup>; a follow-up teardown puts it at ~32.5 nm M0 pitch and ~113 MTr/mm2 at steep cost in complexity and mask count (14 Jun 2026) <sup class="ref"><a href="https://newsletter.semianalysis.com/p/steel-smic-n3-teardown" title="Is SMIC N+3's Metal Pitch Smaller than Intel 18A's?" rel="noopener">ref</a></sup>.
- IBM announced Nanostack at a 0.7 nm node with ASML High-NA EUV as a named ecosystem contribution, ~100bn transistors on a fingernail-sized chip and a production pathway within about five years (25 Jun 2026) <sup class="ref"><a href="https://newsroom.ibm.com/2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology" title="IBM Debuts World's First Sub-1 Nanometer Chip Technology" rel="noopener">ref</a></sup>.
- A 392-dot, 7x7 silicon quantum dot array was fabricated in a 300 mm CMOS process patterned by EUV lithography, reaching threshold-voltage variability below 63 mV standard deviation at 17 nm oxide thickness (14 May 2026).
- The first broadband transmissive EUV metaoptic reports 0.04 deg/nm angular dispersion, directionality up to 5.8 and phase-based operation to 50 eV, framed against strong material absorption that limits transmissive optics at EUV wavelengths (8 Jul 2026).
- US export controls have blocked EUV NXE platforms to China across the Oct 2022, Oct 2023 and Dec 2024 BIS rounds **2024 Bis Export Controls China Semis**; the proposed MATCH Act would additionally ban maintenance of previously sold machines (24 Jun 2026) <sup class="ref"><a href="https://nltimes.nl/2026/06/24/dutch-government-irritated-us-plans-new-asml-export-restrictions" title="Dutch government irritated by U.S. plans for new ASML export restrictions" rel="noopener">ref</a></sup>.

## Open questions

- What is the current delivered in-band source power, conversion efficiency and availability, and does High-NA EUV require more source power per exposure than the 0.33-NA generation?
- Is the light source, rather than optics or precision stages, the binding constraint on ASML's sub-100-unit annual output?
- Could a free-electron-laser source of the kind demonstrated with sub-microjoule seeding ever reach lithographic average power and cost per photon, or is the repetition-rate and stability gap structural?
- If the MATCH Act passes and bans maintenance of previously sold machines <sup class="ref"><a href="https://nltimes.nl/2026/06/24/dutch-government-irritated-us-plans-new-asml-export-restrictions" title="Dutch government irritated by U.S. plans for new ASML export restrictions" rel="noopener">ref</a></sup>, how quickly does an unserviced installed base lose usable source uptime?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
