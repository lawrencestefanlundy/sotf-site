---
type: concept
slug: capram
canonical_name: CapRAM (SEMRON)
aliases:
- capram
- sempacitor
kind: technology
parent_concepts:
- memcapacitor
- in-memory-computing
related_concepts:
- memcapacitor
- charge-domain-compute
- 3d-monolithic-integration
- adc-bottleneck
sources:
- '[[2025-09-23-the-compute-gradient]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2026-07-17-the-once-and-future-kimi]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2026-06-16-cim-landscape-2026]]'
- '[[2026-07-10-inference-silicon-deep-research]]'
- '[[2026-07-02-semianalysis-ectc2026-advanced-packaging]]'
- '[[2026-07-31-positron-research-sprint]]'
frontier:
- Does the 95% charge-recovery assumption, which alone accounts for ~17.4x of the headline efficiency, survive measurement in a real circuit at a real clock rate, or does it collapse the way most adiabatic schemes do outside simulation?
- What effective precision does a CapRAM cell hold at manufacturable yield, and can it be paired with digital readout without giving back its energy advantage, given that hybrid readout is now the industry's route to manufacturability?
- If density depends on 3D stacking, what construction and layer count does CapRAM use, and where does its die-cost minimum fall under a taper-angle-aware cost model?
- Has any CapRAM test chip been taped out at 90nm or below, and does its measured energy per MAC land nearer the 198.5 TOPS/W no-recovery case or the recovery-enabled figures?
- Does CapRAM reach a product-grade test chip (named partner) or a Series A by mid-2027 — the near-dated checkpoint in the SEMRON thesis?
- Is the 20× chip-level energy claim a full-chip (ADC-inclusive) number or array-only?
- Does the CapRAM weight-write mechanism hold retention/endurance at the standard-CMOS interface, or drift like floating-gate flash?
last_updated: '2026-08-31'
tags:
- concept
- semron
- memcapacitor
- product-brand
mention_count: 53
scorecard:
  viability: 2
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Later (5-10yr)
  verdict: Overrated
scorecard_status: draft
sources_7d: 1
sources_30d: 8
recent_mentions:
- slug: 2026-07-31-positron-research-sprint
  title: 'Positron AI research sprint: architecture, funding, customers, manufacturing'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-17-the-once-and-future-kimi
  title: The Once and Future Kimi
  date: '2026-07-17'
  kind: substack
- slug: 2026-07-10-inference-silicon-deep-research
  title: 'Deep research: measured vs claimed inference-silicon economics (adversarially verified, 23/25 claims confirmed)'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-02-semianalysis-ectc2026-advanced-packaging
  title: 'ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More'
  date: '2026-07-02'
  kind: web
- slug: 2026-06-16-cim-landscape-2026
  title: 'Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM'
  date: '2026-06-16'
  kind: web
- slug: 2025-09-23-the-compute-gradient
  title: The Compute Gradient
  date: '2025-09-23'
  kind: substack
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2023-07-23-analog-computing-the-once-and-future
  title: '🔮 E09: Analog Computing: The Once and Future King'
  date: '2023-07-23'
  kind: substack
neighbors:
- slug: memcapacitor
  name: Memcapacitor
  path: /memory/emerging-memory/memcapacitor/
  macro: memory
- slug: charge-domain-compute
  name: Charge-Domain Compute
  path: /compute/non-conventional/charge-domain-compute/
  macro: compute
- slug: 3d-monolithic-integration
  name: 3D Monolithic Integration
  path: /compute/compute-architecture/3d-monolithic-integration/
  macro: compute
- slug: adc-bottleneck
  name: ADC Bottleneck (analog in-memory compute)
  path: /compute/compute-architecture/adc-bottleneck/
  macro: compute
---
## Summary

What has actually been measured is modest and should be stated first. The published demonstration is a crossbar of **156 memcapacitor devices at 50×50 µm² cell size**, with gate lengths around 60 µm, trained to distinguish the letters M, P and I from 5×5-pixel inputs. Measured reactive energy on that micron-scale device was **457 nJ per MAC** over 142 periods. Every femtojoule-per-MAC and TOPS/W number attached to this device class is a **SPICE simulation of a 90nm device**, with scaling projections running to roughly 45nm, and is therefore a seven-order-of-magnitude extrapolation from the measured hardware **Demasius 2021 Memcapacitor Nature Electronics**.

Two distinct multipliers hide inside the headline. The published grid separates them cleanly: worst case (erased cells, zero input sparsity) gives **3,452.6 TOPS/W with 95% charge recovery and 198.5 TOPS/W without**; an MNIST one-layer perceptron gives **29,600 with recovery and 1,702 without**. The charge-recovery assumption alone is worth about **17.4x**, and the 95% figure is imported from the adiabatic-circuits literature rather than measured on this device **Demasius 2021 Memcapacitor Nature Electronics**. So the number you take seriously depends entirely on which assumptions you accept.

The parameters that decide CapRAM are therefore: (1) does high-efficiency charge recovery survive in real circuits at real clock rates; (2) does a multi-level analog device hold enough effective precision at manufacturable yield, given that the 2026 direction of travel in CIM is toward analog-compute with **digital readout** specifically to manage noise and variability, which the KB flags as a headwind for any pure analog multi-level device including this one <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>; (3) whether the density story survives 3D stacking economics, where added layers stop reducing cost past a minimum **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**; and (4) whether the incumbent baseline stands still, which it does not, with a defensible floor of **~2.5-3x per year decline in GPU delivered cost per token**.

## Viability (2/5)

The physics is demonstrated and peer-reviewed: a 156-device memcapacitor crossbar at 50×50 µm² cells performed a real classification task, published in *Nature Electronics* on 11 October 2021 **Demasius 2021 Memcapacitor Nature Electronics**. That is a genuine device-level result and puts CapRAM above pure paper proposals. But the measured energy is **457 nJ per MAC** on micron-scale hardware, and the numbers that make the technology interesting commercially, the femtojoule MACs and the thousands of TOPS/W, are SPICE simulations of a 90nm device, a seven-order-of-magnitude extrapolation from what was built **Demasius 2021 Memcapacitor Nature Electronics**. No source here reports a scaled tape-out, a yield figure, retention data, or any third-party measurement of a CapRAM array.

For calibration on what a near-term analog memory looks like: TetraMem has **taped out MLX200, a 22nm multi-level RRAM analog-CIM SoC**, with eval kits targeted for 2H 2026 <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>. On the evidence in these sources, CapRAM is several development stages behind that. Score 2 reflects early but real evidence against unresolved obstacles at every step between the published device and a manufacturable one.

**TLDR: A working 156-device array exists; everything competitive about it is simulated.**

## Drivers (3/5)

**Demand.** The macro driver is documented and large. Over twenty years peak hardware compute grew **~60,000x** while DRAM bandwidth grew **~100x** and interconnect bandwidth **~30x**; the underlying rates are ~3.0x per two years for server FLOPS against ~1.6x for DRAM bandwidth, so an ever-larger share of workloads becomes memory-bound, with LLM decode the canonical bandwidth-bound phase **2024 Gholami Ai And Memory Wall**. The energy asymmetry is the same argument in another currency: arithmetic is sub-picojoule while an off-chip DRAM fetch is ~1.3-2.6 nJ, so data movement dominates the energy bill **2024 Gholami Ai And Memory Wall**. Anything that keeps weights where the multiply happens is pushing against a real wall.

**Supply and counter-drivers.** The sources give no evidence on fab access, process compatibility, tooling or capital requirement for CapRAM, so the supply side of this specific technology is unassessed. Meanwhile the same demand is being served by cheaper routes that are already in silicon: SK Hynix AiMX3 splits inference so the memory-bound decode stage runs on PIM and the compute-bound stage on the GPU <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>; Positron chose **commodity LPDDR5x over HBM**, claiming 864GB-2.3TB per chip, 2.76 TB/s realisable bandwidth and over 90% memory-bandwidth utilisation versus under 30% claimed for GPUs <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>. If ordinary memory used well closes most of the gap, the pull on exotic memory weakens. Score 3: the wall is real, the claim that CapRAM is what gets called to fix it is not established here.

**TLDR: Demand-side pull is well quantified; the supply-side case for this specific device is not.**

## Novelty (3/5)

What it is better than, on the claims: resistive analog CIM, because a capacitive weight carries no static conduction current and permits charge recovery; and digital accelerators, on energy per MAC. The nearest sourced comparator in the charge domain is EnCharge AI, switched-capacitor charge-domain **SRAM**, claiming **>150 TOPS/W against ~24 TOPS/W for an equivalent Nvidia chip**, with an EN100 board at ~200 AI TOPS in ~8W <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>. Against that, the memcapacitor's non-recovery worst-case simulation of **198.5 TOPS/W** is the same order of magnitude, and only the recovery-enabled figures (3,452.6 worst case, 29,600 for MNIST) open a real gap **Demasius 2021 Memcapacitor Nature Electronics**. The distinctive claim of CapRAM over charge-domain SRAM is that the weight is stored in the capacitive element itself rather than held in volatile SRAM, but no source here quantifies retention or the density benefit that would follow.

So the novelty is architectural and legitimate: this is a new device primitive, first demonstrated in a Nature Electronics paper co-authored by the founders **Demasius 2021 Memcapacitor Nature Electronics**. The magnitude of the improvement remains a modelling result, and the discipline for reading it is set by the third-party comparison points: measured edge energy anchors are scarce (Syntiant is the one MLPerf Tiny anchor at 31.5-43.8 µJ/inference for keyword spotting, with only four submitters in that round) and vendor efficiency claims routinely fail verification, as when **no measured Cerebras 70B figure survived adversarial checking**. Score 3, not 4, because 4 requires demonstrated results and the demonstrated result here is 457 nJ per MAC.

**TLDR: A genuinely new device class with a top-tier publication, but the size of its advantage is simulated, not measured.**

## Diffusion (2/5)

Third, the target moves. Delivered GPU cost per token declines at a defensible floor of **~2.5-3x per year**; software alone lifted H100 MLPerf results up to 1.5x in one year, and 8x B200 measured 3.0x over 8x H200 on Llama-2-70B Server. The same source shows that even shipping challengers win on one axis only: Groq measured 311 tok/s on Llama 3.3 70B at $0.61/M blended, 2-4.4x faster than mainstream GPU providers but 3.5-5x above the cheapest GPU price floor of $0.12-0.17/M. A novel memory device has to clear that bar from a standing start, on unproven process, into design cycles owned by incumbents. Score 2.

**TLDR: Three structural headwinds: the industry's shift to digital readout, 3D stacking cost, and a fast-moving incumbent baseline.**

## Impact (3/5)

The upside case is arithmetic on documented numbers. If data movement dominates energy, with off-chip DRAM fetches at ~1.3-2.6 nJ against sub-picojoule arithmetic **2024 Gholami Ai And Memory Wall**, then a non-volatile weight element that performs the multiply in place and recovers most of its charge removes the dominant term rather than optimising it. At the simulated 90nm figures, even the conservative no-recovery case (198.5 TOPS/W) would be competitive with the best claimed charge-domain SRAM parts **Demasius 2021 Memcapacitor Nature Electronics** <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>, and the recovery-enabled figures would be a step change rather than an increment.

**TLDR: Large if the extrapolations hold, but the sources locate the biggest value pool where CapRAM has shown least.**

## Timing Later (5-10yr)

The published hardware is at 50×50 µm² cells with ~60 µm gate lengths, and the competitive numbers are simulated at 90nm with projections to ~45nm **Demasius 2021 Memcapacitor Nature Electronics**. Nothing in these sources reports a CapRAM tape-out, a process partner, or third-party silicon measurement. The comparable milestone in a neighbouring technology, TetraMem's 22nm multi-level RRAM MLX200 with eval kits targeted 2H 2026, shows what the stage before productisation looks like <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>; CapRAM is not yet at that stage in any source here.

That places material revenue or design wins outside a five-year window on current evidence, with the caveat that the intermediate milestones are much nearer: a scaled test chip and an independently measured energy-per-MAC figure at a real node could arrive well inside the band and would be the events that move this assessment. The demand-side clock, by contrast, is already running, since the memory wall widens every year at 3.0x compute against 1.6x DRAM bandwidth per two years **2024 Gholami Ai And Memory Wall**.

**TLDR: The gap between a 50 µm demonstrator and a manufacturable node is the schedule.**

## Overrated or underrated? Overrated

This is a verdict on the circulating numbers, not on the physics. The memcapacitor is a real, peer-reviewed device primitive with a plausible reason to be more efficient than resistive CIM, and the founders published it in *Nature Electronics* rather than in a press release **Demasius 2021 Memcapacitor Nature Electronics**. But the figures that make CapRAM sound like a step change contain two stacked assumptions that are rarely disclosed together: a 95% charge-recovery assumption imported from the adiabatic-circuits literature, worth about 17.4x on its own, and a seven-order-of-magnitude extrapolation from a 50 µm measured device to a simulated 90nm one **Demasius 2021 Memcapacitor Nature Electronics**. Strip both and you are left with 198.5 TOPS/W in simulation against a competitor claiming >150 TOPS/W in shipping evaluation boards <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>.

The environment has also turned against the specific bet. The practical route to manufacturable precision in 2026 is analog compute with digital readout and lower effective precision for yield, which is explicitly a headwind for pure analog multi-level devices of this kind <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>, while the incumbent it must beat is getting ~2.5-3x cheaper per token per year and the pragmatic alternatives (PIM for decode, commodity LPDDR5x used at over 90% bandwidth utilisation) are already in or near production <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>. The honest read is a technically interesting device three or more stages from evidence that would justify its headline claims.

## Prediction

By 31 December 2028, no independently measured (third-party or peer-reviewed, non-simulated) CapRAM or memcapacitor array at a sub-100nm node will have published an energy-per-MAC or TOPS/W figure within one order of magnitude of the 3,452.6 TOPS/W charge-recovery case in the 2021 Nature Electronics paper.

## Evidence base

## Open questions

- Does the 95% charge-recovery assumption, which alone accounts for ~17.4x of the headline efficiency, survive measurement in a real circuit at a real clock rate, or does it collapse the way most adiabatic schemes do outside simulation?
- What effective precision does a CapRAM cell hold at manufacturable yield, and can it be paired with digital readout without giving back its energy advantage, given that hybrid readout is now the industry's route to manufacturability?
- If density depends on 3D stacking, what construction and layer count does CapRAM use, and where does its die-cost minimum fall under a taper-angle-aware cost model?
- Has any CapRAM test chip been taped out at 90nm or below, and does its measured energy per MAC land nearer the 198.5 TOPS/W no-recovery case or the recovery-enabled figures?

---
*Assessment drafted 2026-08-31 from up to 12 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
