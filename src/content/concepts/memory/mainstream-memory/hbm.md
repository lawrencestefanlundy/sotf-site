---
type: concept
slug: hbm
canonical_name: HBM (High-Bandwidth Memory)
aliases:
- High Bandwidth Memory
- HBM3E
- HBM4
kind: technology
parent_concepts:
- memory
- mainstream-memory
related_concepts:
- dram
- cowos
- hbm-cowos-bottleneck
- advanced-packaging
- hybrid-bonding
- tsv-through-silicon-via
sources:
- '[[2025-09-23-the-compute-gradient]]'
- '[[2023-10-06-e18-the-state-of-silent-speech-and]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-06-23-semidoped-daily-update]]'
- '[[2026-06-22-sintered-metal-die-attach-landscape]]'
- '[[2026-06-01-hbm-state-of-play]]'
- '[[2026-07-10-workload-phase-silicon-sweep]]'
- '[[2026-07-31-etched-research-sprint]]'
- '[[2026-06-16-hbm-supercycle-2026]]'
- '[[2026-03-03-ai-power-thermal-binding-nvidia-vera-rubin-and-feynman]]'
- '[[2026-07-02-semianalysis-ectc2026-advanced-packaging]]'
- '[[2024-02-26-micron-hbm3e-volume-production]]'
- '[[2025-08-12-scaling-the-memory-wall-the-rise-and-roadmap-of-hbm]]'
- '[[2024-09-26-sk-hynix-12-layer-hbm3e-volume-production]]'
- '[[2026-07-07-high-bandwidth-flash-the-full-report]]'
- '[[2026-07-13-sk-hynix-record-fall-hbm4-three-supplier]]'
- '[[2026-04-15-semianalysis-isscc-2026]]'
- '[[2026-07-31-positron-research-sprint]]'
- '[[2026-05-29-silicon-shock-the-macro-of-tech-inflation]]'
- '[[2024-02-27-samsung-36gb-hbm3e-12h]]'
scorecard:
  viability: 5
  drivers: 5
  novelty: 4
  diffusion: 5
  impact: 5
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 75
sources_7d: 0
sources_30d: 4
recent_mentions:
- slug: 2026-07-31-etched-research-sprint
  title: Etched research sprint — tape-out speed, HBM supply, customer orders (4-lane web sweep)
  date: '2026-07-31'
  kind: web
- slug: 2026-07-31-positron-research-sprint
  title: 'Positron AI research sprint: architecture, funding, customers, manufacturing'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-27-cxmt-star-market-debut
  title: CXMT's 466% STAR Market debut makes it China's most valuable mainland-listed company
  date: '2026-07-27'
  kind: web
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-17-the-once-and-future-kimi
  title: The Once and Future Kimi
  date: '2026-07-17'
  kind: substack
- slug: 2026-07-15-kimi-k3-launch-moonshot
  title: Kimi K3 — Moonshot launch post (architecture, quantisation, serving requirements)
  date: '2026-07-15'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-13-sk-hynix-record-fall-hbm4-three-supplier
  title: SK Hynix record one-day fall as HBM4 goes three-supplier
  date: '2026-07-13'
  kind: web
neighbors:
- slug: dram
  name: DRAM
  path: /memory/mainstream-memory/dram/
  macro: memory
- slug: cowos
  name: CoWoS (TSMC)
  path: /manufacturing/packaging/cowos/
  macro: manufacturing
- slug: hbm-cowos-bottleneck
  name: HBM / CoWoS Bottleneck
  path: /compute/compute-architecture/hbm-cowos-bottleneck/
  macro: compute
- slug: advanced-packaging
  name: Advanced Packaging
  path: /manufacturing/packaging/advanced-packaging/
  macro: manufacturing
- slug: hybrid-bonding
  name: Hybrid Bonding (Cu-Cu)
  path: /manufacturing/packaging/hybrid-bonding/
  macro: manufacturing
- slug: tsv-through-silicon-via
  name: TSV / Through-Silicon Via
  path: /manufacturing/packaging/tsv-through-silicon-via/
  macro: manufacturing
---
**HBM is stacked DRAM bonded over through-silicon vias and co-packaged with an accelerator on a silicon interposer, and it is now the single component that sets the bandwidth, capacity and cost ceiling of AI compute, with revenue rising from roughly $4B in 2023 to around $35B in 2025.**

## Summary

High-Bandwidth Memory is DRAM turned on its side. Instead of placing memory chips on a motherboard and talking to them over a narrow, fast serial bus, HBM stacks 8 to 16 DRAM dies vertically over a base die, connects them with through-silicon vias, and sits the whole stack next to the processor on a silicon interposer (in the dominant case, TSMC's CoWoS). Bandwidth then comes from brute bus width rather than pin speed: HBM3E uses a 1,024-bit interface, HBM4 doubles that to 2,048-bit. Per-stack figures run from roughly 460 GB/s at 16GB for HBM2E, through about 1.2 TB/s at 24-36GB for HBM3E, to roughly 2.0-3.3 TB/s at 36-64GB for HBM4, with HBM4E at 3+ TB/s expected in 2027. Energy is about 3-4 pJ/bit.

The parameters that decide HBM are not really the DRAM cells. Three matter. First, packaging: HBM only exists as part of an advanced package, and CoWoS supply is widely argued to be the true gating constraint, with lead times of 50-104 weeks and Nvidia reported to have booked around 55% of 2026 capacity. Second, the base die: from HBM4 onward it becomes a logic die, which splits the industry along a foundry fault line, with SK Hynix and Micron using TSMC N12-class and Samsung using in-house SF4. Third, wafer intensity: 1GB of HBM consumes roughly 3-4 times the wafer capacity of 1GB of DDR5, so HBM growth cannibalises commodity DRAM supply, with AI absorbing about 20% of global DRAM wafer capacity in 2026.

HBM's importance is best read from the papers that treat it as the thing to be worked around. LLM inference is described as bottlenecked by the capacity and bandwidth of GPU HBM; reasoning models with long output sequences and low arithmetic intensity make the memory wall worse; mixture-of-experts weights strain HBM capacity and cost efficiency; and billion-scale vector search cannot fit in HBM at all. A whole research literature now proposes to displace or supplement it: UCIe-attached on-package memory, high-bandwidth flash, monolithic-3D on-chip cache, photonic memory appliances and even optical delay-line "fiber memory". None of it ships. HBM does.

## Viability (5/5)

This is not a technology with a viability question. HBM2E through HBM3E are in production, HBM4 is the current transition with a logic base die, and HBM4E is dated to 2027. Three suppliers stand behind it, and Samsung demonstrated HBM4 running well past JEDEC pin speeds at ISSCC 2026 <sup class="ref"><a href="https://newsletter.semianalysis.com/p/isscc-2026-nvidia-and-broadcom-cpo" title="ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More" rel="noopener">ref</a></sup>. SK Hynix's 2026 output was reported booked out as of October 2025, with inventory falling from 17 weeks to 2-4 weeks.

The residual engineering risk is in the package, not the concept. ECTC 2026 material shows HBM4E signal integrity as a live problem: at 12 Gb/s the eye opening is about 67% of a unit interval without receiver equalisation, roughly 72.5% with a one-tap DFE, and above 60% at 12.8, 14 and 16 Gb/s <sup class="ref"><a href="https://newsletter.semianalysis.com/p/ectc2026" title="ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, " rel="noopener">ref</a></sup>. That is a workable margin obtained with active equalisation, which is a fair summary of where HBM sits generally: it works, and each generation costs more circuit and packaging effort to keep working.

**TLDR: Shipping in volume across four generations, three qualified suppliers, sold out.**

## Drivers (5/5)

Demand: TrendForce figures cited in the research base show HBM bit demand up about 130% in 2025, 70-77% in 2026 and 68% in 2027, with revenue moving from roughly $4B (2023) to $17B (2024) to about $35B (2025) and a TAM near $100B by 2028. HBM now represents around one third of DRAM value. The upstream driver is AI infrastructure spending, put at $725B of capex with NVIDIA holding 77% of the chip race. Workload mix reinforces it: reasoning models and long-sequence decode are bandwidth-bound rather than compute-bound, so each additional unit of useful throughput requires disproportionately more memory bandwidth.

Supply: constrained on two axes. HBM consumes 3-4 times the wafer area per gigabyte versus DDR5, and AI is taking about 20% of global DRAM wafer capacity in 2026, which is why DRAM ASPs rose 80-90% in a single quarter. Separately, CoWoS interposer capacity rather than the DRAM die is the widely argued binding constraint, with 50-104 week lead times. The DRAM price and availability pressure is explicit enough that it is now cited as the motivation for exotic alternatives such as optical delay-line memory.

**TLDR: Demand growth of +130% in 2025 and ~+70% in 2026 against wafer-intensive, packaging-gated supply.**

## Novelty (4/5)

Against what it replaced, the margin is large and demonstrated: HBM converts a pin-speed problem into a bus-width problem, taking per-stack bandwidth from roughly 460 GB/s to 3+ TB/s across four generations, with HBM4 doubling the interface to 2,048 bits, at roughly 3-4 pJ/bit. No conventional off-package DRAM organisation is in the same range, which is why every merchant AI accelerator uses it.

Against what wants to replace it, the claims are substantial but paper-stage. A UCIe-based on-package memory proposal claims up to 10x bandwidth density, 3x lower latency, 3x lower power and lower cost than HBM4 and LPDDR on-package memory, either by putting a logic die in front of LPDDR6/HBM or by making DRAM natively speak UCIe. A photonic memory appliance claims to break the silicon beachfront limit that fixes the memory-to-compute ratio, offering 32 TB of shared memory with 115 Tbps of switching and simulated gains of 3.66x throughput and 1.40x latency in LLM inference. A 3D electronic-photonic stack using through-silicon optical vias claims to beat 3D electrical interconnect at >10 TB/s/mm², and fiber memory claims >70% lower weight-delivery energy than HBM3E configurations across 10,000 accelerators. Every one of these is a simulation or an architecture proposal, and one of them (the photonic appliance) uses HBM3E inside itself. HBM's real vulnerability visible in the sources is capacity and cost, not bandwidth.

**TLDR: Decisively better than commodity DRAM per package; the proposals that claim to beat it are simulation-only.**

## Diffusion (5/5)

Diffusion is essentially complete within the segment that can afford it. HBM is the assumed baseline in every architecture paper in this set, from chiplet GPUs where the concern is remote HBM traffic to HBM-PIM designs that exploit the HBM4 logic base die as a stack-local control point. The constraint is not persuasion; it is allocation, with 2026 capacity booked and CoWoS lead times up to two years.

The genuine limits on further diffusion are cost, capacity and heat. HBM does not reach the broader computing continuum, which is precisely the gap the UCIe on-package memory proposal targets. Within AI, capacity ceilings push work off HBM: billion-scale vector indexes do not fit, MoE expert weights are increasingly uneconomic to hold in it, and on-chip M3D cache expansion is being evaluated specifically to cut off-chip HBM traffic and its energy. Fragmentation is also starting: ECTC 2026 covered custom HBM alongside HBM4 packaging challenges <sup class="ref"><a href="https://newsletter.semianalysis.com/p/ectc2026" title="ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, " rel="noopener">ref</a></sup>, which suggests the standard part may not stay the only part.

**TLDR: Already the default in AI accelerators; the barriers are allocation and cost, not adoption.**

## Impact (5/5)

Financially, HBM is roughly a third of DRAM industry value on a path to a ~$100B TAM by 2028, and its wafer intensity is repricing the whole commodity memory market, with DRAM ASPs up 80-90% in a quarter. That is a rare case where one component's demand curve moves an entire upstream industry's pricing.

Technically, HBM is the term that decides serving economics. LLM inference is bandwidth- and capacity-bound at HBM, and system utilisation falls as reasoning workloads push output length up and arithmetic intensity down. Data movement between on-chip cache and off-chip HBM is identified as a key contributor to chip energy dissipation as serving scales into power and thermal limits. The knock-on reaches yield engineering too: die stacking for HBM makes wafer-level defect screening central, to the point of motivating quantum-classical classifier studies on wafer maps.

**TLDR: Sets the throughput and cost of AI inference and already commands about a third of DRAM value.**

## Timing Now (0-2yr)

HBM is not a future technology; the timing question is about the next node and the supply chain around it. HBM4 with its logic base die is the current transition, Samsung showed it running past JEDEC pin speeds at ISSCC 2026, and HBM4E is placed at 2027 with 3+ TB/s per stack <sup class="ref"><a href="https://newsletter.semianalysis.com/p/isscc-2026-nvidia-and-broadcom-cpo" title="ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More" rel="noopener">ref</a></sup>. Demand growth is forecast at 68% into 2027, so the near-term binding question is packaging and wafer allocation, not device physics.

The challengers are on a different clock. UCIe-attached memory, high-bandwidth flash, M3D cache, photonic fabrics and fiber memory are all at simulation or proposal stage in these sources, and one of them, HBF, is already shown to degrade tiled matrix multiplication by up to an order of magnitude through read amplification unless the memory layout is redesigned. Anything that meaningfully displaces HBM volume sits in the Later band; HBM-adjacent changes such as HBM-PIM on the HBM4 logic die and custom HBM variants <sup class="ref"><a href="https://newsletter.semianalysis.com/p/ectc2026" title="ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, " rel="noopener">ref</a></sup> are the plausible Soon events.

**TLDR: HBM4 is the live transition, HBM4E is dated 2027, and the competitive question resolves inside two years.**

## Overrated or underrated? Fairly rated

HBM is correctly understood to be the constraint on AI compute, and the market has priced that: sold out through 2026, a third of DRAM value, and an order-of-magnitude revenue increase in three years. There is little mispricing left in the headline story. What is under-attended is where the value actually accrues. The die is not the scarce thing; CoWoS interposer capacity is, with lead times of 50-104 weeks and around 55% of 2026 capacity reportedly booked by one customer. And from HBM4 the base die is a logic die, which means part of HBM's margin now depends on foundry access and yield, splitting SK Hynix and Micron (TSMC N12-class) from Samsung (in-house SF4). That is the fault line worth watching, not bit growth.

On the displacement narrative, be sceptical for now. The alternatives in these sources are architecturally interesting and quantitatively bold, but they are analytical models, and where one has been stress-tested against real GEMM behaviour it broke badly before mitigation. The realistic near-term outcome is that HBM keeps the bandwidth tier and cedes ground on capacity to flash and pooled or optical memory sitting behind it, which is exactly the topology in both the HBF and photonic-fabric proposals.

## Prediction

By 31 December 2027, HBM (HBM4 or HBM4E) will remain the sole on-package memory in every volume-shipping merchant AI training accelerator, with no UCIe-attached DRAM, high-bandwidth flash or optical memory alternative in commercial production as a replacement for the HBM bandwidth tier.

## Evidence base

- Per-stack bandwidth scales from ~460 GB/s (HBM2E, 16GB) to ~2.0-3.3 TB/s (HBM4, 36-64GB) and 3+ TB/s (HBM4E, 2027), driven by bus width doubling from 1,024-bit to 2,048-bit, at ~3-4 pJ/bit.
- HBM revenue path: ~$4B (2023), ~$17B (2024), ~$35B (2025 Micron TAM), ~$32.7B (2026 UBS), ~one third of DRAM value, ~$100B TAM by 2028; bit demand +130% in 2025, +70-77% in 2026, +68% in 2027.
- CoWoS is widely argued to be the gating constraint rather than the DRAM die, with 50-104 week lead times and Nvidia reported to have booked ~55% of 2026 capacity; from HBM4 the base die becomes a logic die split between TSMC N12-class (SK Hynix, Micron) and Samsung SF4.
- At ISSCC 2026 Samsung demonstrated HBM4 running well past JEDEC pin speeds, alongside LPDDR6 from Samsung and SK Hynix <sup class="ref"><a href="https://newsletter.semianalysis.com/p/isscc-2026-nvidia-and-broadcom-cpo" title="ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More" rel="noopener">ref</a></sup>.
- HBM4E signal integrity at ECTC 2026: ~67% unit-interval eye at 12 Gb/s without receiver equalisation, ~72.5% with a one-tap DFE, and >60% at 12.8/14/16 Gb/s <sup class="ref"><a href="https://newsletter.semianalysis.com/p/ectc2026" title="ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, " rel="noopener">ref</a></sup>.
- A UCIe-based on-package memory proposal claims up to 10x bandwidth density, 3x lower latency, 3x lower power and lower cost than HBM4 and LPDDR on-package memory, using either a logic die in front of LPDDR6/HBM or DRAM that natively speaks UCIe.
- A photonic memory appliance integrating HBM3E, an on-module photonic switch and external DDR5 reports up to 32 TB shared memory, 115 Tbps all-to-all switching and simulated 3.66x throughput and 1.40x latency improvement in LLM inference, aimed at removing the silicon beachfront limit on memory-to-compute ratio.

## Open questions

- Does the HBM4 logic base die decide market share? Specifically, does Samsung's in-house SF4 base die yield and perform well enough against SK Hynix and Micron on TSMC N12-class to hold three-supplier parity?
- Which constraint actually binds through 2027: CoWoS interposer capacity and its 50-104 week lead times, or DRAM wafer capacity given HBM's 3-4x wafer intensity versus DDR5?
- Can large-granularity memory (high-bandwidth flash) close the read-amplification gap in production, given it can degrade tiled GEMM by up to an order of magnitude at kilobyte access granularity?
- Does custom HBM fragment the JEDEC standard, and if so does that concentrate or dilute supplier pricing power <sup class="ref"><a href="https://newsletter.semianalysis.com/p/ectc2026" title="ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, " rel="noopener">ref</a></sup>?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
