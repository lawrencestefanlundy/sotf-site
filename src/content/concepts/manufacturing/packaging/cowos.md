---
type: concept
slug: cowos
canonical_name: CoWoS (TSMC)
aliases: []
kind: technology
parent_concepts:
- manufacturing
- packaging
related_concepts: []
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2026-03-26-sotf-interview-dorian-haci-mintneuro]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-05-consensus-capital]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2023-10-13-e19-trusted-execution-environments]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
frontier:
- Do organic-substrate die-to-die links (Intel UCIe-S) or bridge approaches (TSMC Active LSI) let a meaningful share of accelerator designs step off silicon interposers by 2028, and at what bandwidth penalty?
- Do Samsung X-Cube and Intel Foveros move materially above the ~30%-of-TSMC-volume level cited for 2024, and do they get qualified by the top accelerator buyers?
- Does TSMC begin pricing advanced packaging to the scarcity, and if so does the rent shift from Nvidia to TSMC?
- Does co-packaged optics integration (COUPE) tighten packaging capacity again after 2028 by adding photonic yield and thermal-control steps, or is it additive capacity outside the CoWoS queue?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 828
last_reorg_date: '2026-05-13'
scorecard:
  viability: 5
  drivers: 5
  novelty: 3
  diffusion: 4
  impact: 5
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 7
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-31-etched-research-sprint
  title: Etched research sprint — tape-out speed, HBM supply, customer orders (4-lane web sweep)
  date: '2026-07-31'
  kind: web
- slug: 2026-07-31-inference-silicon-roster-sprint
  title: 'Inference-silicon roster verification sprint: 10 companies for the competitive-analysis capital map'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-10-inference-silicon-deep-research
  title: 'Deep research: measured vs claimed inference-silicon economics (adversarially verified, 23/25 claims confirmed)'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-09-in-die-microfluidic-cooling-sprint
  title: In-die microfluidic cooling — cluster research sprint
  date: '2026-07-09'
  kind: web
- slug: 2026-07-05-semianalysis-kyber-nvl144-delayed-2028
  title: 'SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled'
  date: '2026-07-05'
  kind: web
- slug: 2026-07-02-semianalysis-ectc2026-advanced-packaging
  title: 'ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More'
  date: '2026-07-02'
  kind: web
neighbors: []
---
**CoWoS is TSMC's silicon-interposer packaging platform that bolts logic dies and HBM stacks into a single module, and through 2026 it is the physical chokepoint metering how many AI accelerators the world can build <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>.**

## Summary

Modern AI accelerators are not single chips. A GPU or custom ASIC die is placed alongside several stacks of high-bandwidth memory on a silicon interposer, a passive slab of silicon carrying thousands of very fine wires, which is then mounted on an organic substrate. CoWoS is TSMC's version of that assembly step. HBM itself is defined around it: stacked DRAM on through-silicon vias over a base die, co-packaged on a silicon interposer, with bus widths of 1,024 bits for HBM3E rising to 2,048 bits for HBM4. Without an interposer of this class there is no way to land that many parallel connections between logic and memory at acceptable energy per bit.

The technology is not experimental. It is high-volume manufacturing, and the interesting parameters are industrial rather than physical: how many interposer-equivalent units per month exist, who holds the allocation, and what the lead time is. On the supplied evidence, capacity is fully booked through 2026, lead times run 50 to 104 weeks, and Nvidia alone booked roughly 55% of 2026 output <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>. Analysts consistently argue the gating constraint on HBM-based systems is the packaging, not the memory die, and Yole names TSMC CoWoS capacity as the leading bottleneck for AI accelerator volume, expanding through 2026 **2024 Yole Advanced Packaging 2024**.

The competitive picture has two axes. On capacity, Samsung X-Cube and Intel Foveros are described as credible secondary options but each at roughly 30% of TSMC volume **2024 Yole Advanced Packaging 2024**. On architecture, the roadmap is moving past plain 2.5D interposers: TSMC detailed an Active LSI bridge for higher in-package bandwidth, while Intel showed UCIe-S running fast die-to-die lanes over cheaper organic substrates, which is a direct attack on interposer necessity <sup class="ref"><a href="https://newsletter.semianalysis.com/p/isscc-2026-nvidia-and-broadcom-cpo" title="ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More" rel="noopener">ref</a></sup>. TSMC is also pulling optics into the package via its COUPE co-packaged-optics engine, where micro-ring resonators in the photonic layer degrade bit error rate on wavelength drift of about ±1.7 nm, making thermal management a first-class packaging problem.

The decisive variables for anyone assessing CoWoS are therefore: the rate of capacity addition versus accelerator demand; whether bridge and organic-substrate approaches let some designs step off silicon interposers; whether second sources get past ~30% of TSMC scale; and how long packaging stays the binding constraint before lithography takes over <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>.

## Viability (5/5)

There is no technical risk to assess in the usual sense. CoWoS-class interposer packaging is the substrate on which HBM-based accelerators are built, with defined generations (HBM3E at 1,024-bit, HBM4 at 2,048-bit) already in the field or in ramp. Demand evidence doubles as viability evidence: capacity sold out through 2026 and lead times of 50 to 104 weeks are the signature of a qualified, yielding process that customers cannot get enough of <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>.

The live engineering risk has moved up the stack rather than away. Once optics enter the package, thermal coupling becomes a yield and reliability issue: TSMC's COUPE architecture depends on micro-ring resonators whose resonant wavelength must be held within a tight budget, with ±1.7 nm deviation causing measurable bit-error-rate degradation. Work on rival 3.5D stacks quotes compensated spectral drift of 0.36 nm against a TSMC tolerance budget, but explicitly as pre-silicon engineering projections awaiting silicon validation. So the 2.5D core is proven; the optical extension is not.

**TLDR: Not a question of whether it works: it is sold out in volume production.**

## Drivers (5/5)

Demand: AI accelerators absorb 60% of TSMC N3 output in 2026 and a projected 90% in 2027, and essentially all of that silicon needs advanced packaging. HBM revenue moved from roughly $4B in 2023 to about $35B in 2025 with a claimed $100B TAM by 2028, and every one of those stacks needs an interposer to sit on. Chiplet-attributed revenue is tracked from ~$3B in 2021 to $7.5B in 2024 to $30B+ by 2030 **2024 Yole Advanced Packaging 2024**. Concentration adds to the squeeze: Nvidia booked around 55% of 2026 CoWoS while holding roughly 80% of AI accelerator revenue share, so a single buyer's roadmap sets the loading <sup class="ref"><a href="https://siliconanalysts.com/analysis/nvidia-ai-accelerator-market-share-2024-2026" title="NVIDIA AI GPU Market Share 2026: ~80% of AI Accelerators | Silicon Analysts" rel="noopener">ref</a></sup>.

Supply: TSMC is expanding through 2026, but the alternatives remain sub-scale, with Samsung X-Cube and Intel Foveros each put at about 30% of TSMC volume **2024 Yole Advanced Packaging 2024**. Pricing is a notable anomaly. SemiAnalysis argues Nvidia and TSMC have not raised prices to match the value their hardware unlocks despite being the binding supply bottleneck <sup class="ref"><a href="https://newsletter.semianalysis.com/p/ai-value-capture-the-shift-to-model" title="AI Value Capture - The Shift To Model Labs" rel="noopener">ref</a></sup>, which means allocation rather than price is doing the rationing and the economic driver to add capacity is weaker than the physical shortage implies.

**TLDR: Demand pull is overwhelming and supply additions have not caught it.**

## Novelty (3/5)

What CoWoS is better than, on the supplied evidence, is chiefly conventional substrate-only packaging: it is what makes 1,024- and 2,048-bit HBM interfaces physically possible at roughly 3 to 4 pJ/bit. Against rival advanced-packaging platforms the sources give a capacity gap, not a technical one: Samsung X-Cube and Intel Foveros are called credible secondary capacity at about 30% of TSMC volume each **2024 Yole Advanced Packaging 2024**. No source here quantifies a bandwidth, yield or cost advantage of CoWoS over those platforms, so the moat should be read as manufacturing scale plus customer lock-in via multi-year locked contracts that new entrants cannot replicate.

The direction of travel is also visible. TSMC's Active LSI bridge points to higher in-package bandwidth beyond passive interposers, while Intel's UCIe-S demonstrated fast die-to-die lanes over cheaper organic substrates <sup class="ref"><a href="https://newsletter.semianalysis.com/p/isscc-2026-nvidia-and-broadcom-cpo" title="ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More" rel="noopener">ref</a></sup>. If organic-substrate die-to-die links prove adequate for a class of designs, part of the CoWoS premium is competed away from below rather than displaced from above. That is why this scores 3 rather than higher: the incumbency is real, the demonstrated technical margin over alternatives is not documented in these sources.

**TLDR: Real advantage, but it is scale, yield and ecosystem rather than a quantified performance gap in the sources.**

## Diffusion (4/5)

Diffusion within the segment that matters is close to saturation. Yole expects over 60% of leading-edge AI accelerators to ship as multi-die chiplet stacks by 2027, and HBM-based designs are defined around interposer co-packaging **2024 Yole Advanced Packaging 2024**. The barrier is not designer reluctance but queue position: 50 to 104 week lead times and one customer holding roughly 55% of 2026 output mean smaller buyers are rationed. Tier-2 fabless designers such as MediaTek, Marvell and Qualcomm are only expected to ship first chiplet products by 2027, and UCIe Phase 2 multi-vendor mix-and-match reaches first commercial products around the same time **2024 Yole Advanced Packaging 2024**, so broader access is a 2027-onwards story.

Two structural barriers remain. First, cost keeps interposer packaging on leading-edge AI and HPC parts rather than the wider market; the cheaper-organic-substrate route Intel showed at ISSCC exists precisely because of that <sup class="ref"><a href="https://newsletter.semianalysis.com/p/isscc-2026-nvidia-and-broadcom-cpo" title="ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More" rel="noopener">ref</a></sup>. Second, geography: leading-edge output remains heavily concentrated in Taiwan, with Arizona still under about 5% of leading-edge volume, so second-region packaging capacity is a live gap rather than a solved one <sup class="ref"><a href="https://newsletter.semianalysis.com/p/apple-tsmc-the-partnership-that-built" title="Apple-TSMC: The Partnership That Built Modern Semiconductors" rel="noopener">ref</a></sup>.

**TLDR: Already the default for leading-edge AI silicon; adoption is limited by allocation, not by willingness.**

## Impact (5/5)

When a single process step is the acute supply constraint on the fastest-growing capital-goods category in technology, its impact is not in doubt. Patel places HBM plus CoWoS advanced packaging as the acute supply constraints for 2025 to 2026, with CoWoS sold out through 2026 <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>. Downstream, packaging is named alongside TSMC, Nvidia, memory and lithography as one of the upstream layers capturing structural rents in the AI economy, protected by multi-year locked contracts. The market it enables is large in its own right: chiplet-attributed revenue to $30B+ by 2030 and an HBM TAM claimed at $100B by 2028 **2024 Yole Advanced Packaging 2024**.

Two qualifications on who captures that value. TSMC is reported not to have priced to the scarcity <sup class="ref"><a href="https://newsletter.semianalysis.com/p/ai-value-capture-the-shift-to-model" title="AI Value Capture - The Shift To Model Labs" rel="noopener">ref</a></sup>, so much of the economic rent from the bottleneck accrues to the accelerator vendor holding the allocation rather than to the packager. And the bottleneck itself is expected to move: Patel frames the constraint as shifting from CoWoS to EUV lithography post-2028 <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>. High impact now, with an explicit expiry on the chokepoint premium.

**TLDR: It currently meters global AI accelerator output, which makes it one of the highest-leverage steps in the stack.**

## Timing Now (0-2yr)

CoWoS is already gating shipments: sold out through 2026, lead times of 50 to 104 weeks, and capacity expansion running through 2026 <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup> **2024 Yole Advanced Packaging 2024**. Any investment or design decision keyed to advanced packaging scarcity has to be made against the current window, not a future one.

The second-order timing question is when it loosens. Patel's framework has the constraint rotating between logic, memory and power, with the durable post-2028 ceiling being ASML and EUV, since ASML produces fewer than roughly 100 EUV machines a year <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>. Alternative routes mature on a similar clock: UCIe Phase 2 first commercial products by 2027 and tier-2 fabless chiplet parts by 2027 **2024 Yole Advanced Packaging 2024**. So expect the acute phase to be a 2026-2027 phenomenon, with the packaging platform itself remaining strategically important but no longer the single ceiling.

**TLDR: This is the binding constraint today, and the sources expect it to stop being so around 2028.**

## Overrated or underrated? Fairly rated

The consensus reading, that CoWoS is the physical bottleneck on AI accelerator supply, is correct and well evidenced: sold out through 2026, 50 to 104 week lead times, one customer at roughly 55% of allocation, and analysts explicitly naming the packaging rather than the memory die as the gate <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>. There is no case for calling this overhyped as a description of 2026 reality.

Where the narrative overreaches is durability and value capture. The same source that names CoWoS as today's constraint says the constraint shifts to EUV lithography after 2028 <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>; the alternatives are visibly moving, with Intel's UCIe-S over cheap organic substrates and TSMC's own Active LSI bridge both pointing beyond passive interposers <sup class="ref"><a href="https://newsletter.semianalysis.com/p/isscc-2026-nvidia-and-broadcom-cpo" title="ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More" rel="noopener">ref</a></sup>; and TSMC is reported not to be pricing to the scarcity, so the rent from the bottleneck largely lands with the accelerator vendor holding the allocation <sup class="ref"><a href="https://newsletter.semianalysis.com/p/ai-value-capture-the-shift-to-model" title="AI Value Capture - The Shift To Model Labs" rel="noopener">ref</a></sup>. Treat CoWoS as a hard near-term supply variable and a genuine strategic asset, but not as a permanent toll booth.

## Prediction

TSMC CoWoS-class advanced packaging capacity will still be reported as fully allocated through calendar 2027, with Nvidia holding at least 40% of that allocation.

## Evidence base

- Yole's 2024 advanced packaging analysis names TSMC CoWoS capacity as the leading bottleneck for AI accelerator volume, expanding through 2026, with Samsung X-Cube and Intel Foveros each at roughly 30% of TSMC volume **2024 Yole Advanced Packaging 2024**.
- Mid-2026 HBM synthesis: HBM rides on TSMC CoWoS, Nvidia booked ~55% of 2026 CoWoS, lead times 50-104 weeks, and CoWoS rather than the memory die is widely argued to be the gating constraint.
- March 2026: HBM plus CoWoS are framed as the acute 2025-26 supply constraints, CoWoS sold out through 2026, with the durable post-2028 ceiling shifting from CoWoS to ASML/EUV at fewer than ~100 EUV machines a year <sup class="ref"><a href="https://www.dwarkesh.com/p/dylan-patel" title="SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)" rel="noopener">ref</a></sup>.
- ISSCC 2026: TSMC detailed an Active LSI bridge for higher-bandwidth in-package interconnect while Intel showed UCIe-S running fast die-to-die lanes over cheaper organic substrates <sup class="ref"><a href="https://newsletter.semianalysis.com/p/isscc-2026-nvidia-and-broadcom-cpo" title="ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More" rel="noopener">ref</a></sup>.
- Yole 2024: over 60% of leading-edge AI accelerators ship as multi-die chiplet stacks by 2027, chiplet-attributed revenue $7.5B (2024) to $30B+ (2030), UCIe Phase 2 first commercial products by 2027 **2024 Yole Advanced Packaging 2024**.
- May 2026: Nvidia and TSMC are argued to have not raised pricing to match the value their hardware unlocks despite being the binding supply bottleneck <sup class="ref"><a href="https://newsletter.semianalysis.com/p/ai-value-capture-the-shift-to-model" title="AI Value Capture - The Shift To Model Labs" rel="noopener">ref</a></sup>.

## Open questions

- Do organic-substrate die-to-die links (Intel UCIe-S) or bridge approaches (TSMC Active LSI) let a meaningful share of accelerator designs step off silicon interposers by 2028, and at what bandwidth penalty?
- Do Samsung X-Cube and Intel Foveros move materially above the ~30%-of-TSMC-volume level cited for 2024, and do they get qualified by the top accelerator buyers?
- Does TSMC begin pricing advanced packaging to the scarcity, and if so does the rent shift from Nvidia to TSMC?
- Does co-packaged optics integration (COUPE) tighten packaging capacity again after 2028 by adding photonic yield and thermal-control steps, or is it additive capacity outside the CoWoS queue?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
