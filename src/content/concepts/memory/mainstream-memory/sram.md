---
type: concept
slug: sram
canonical_name: SRAM
aliases: []
kind: technology
parent_concepts:
- memory
- mainstream-memory
related_concepts: []
sources:
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2026-06-16-cim-landscape-2026]]'
- '[[2026-07-25-thoughts-on-ai-and-power]]'
- '[[2026-07-10-workload-phase-silicon-sweep]]'
- '[[2026-07-31-etched-research-sprint]]'
- '[[2026-07-10-inference-silicon-deep-research]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-07-02-semianalysis-ectc2026-advanced-packaging]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2026-06-04-globalfoundries-emram-22fdx-availability]]'
- '[[2026-07-07-high-bandwidth-flash-the-full-report]]'
- '[[2026-01-13-semianalysis-interconnects-beyond-copper]]'
- '[[2026-06-15-gf-investor-day-2026]]'
- '[[2026-06-17-femtoai-spu-ces2026]]'
- '[[2026-07-31-inference-silicon-roster-sprint]]'
- '[[2026-05-13-semianalysis-cerebras-faster-tokens]]'
- '[[2026-06-03-tendrils-compute]]'
- '[[2026-04-15-semianalysis-isscc-2026]]'
- '[[2026-08-14-chip-tail-verification-sweep]]'
- '[[2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology]]'
scorecard:
  viability: 5
  drivers: 4
  novelty: 2
  diffusion: 5
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 95
sources_7d: 0
sources_30d: 5
recent_mentions:
- slug: 2026-08-14-chip-tail-verification-sweep
  title: 'Chip-comparison tail verification sweep: 37 companies re-verified, consolidation wave confirmed'
  date: '2026-08-14'
  kind: web
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
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-10-workload-phase-silicon-sweep
  title: 'Workload-phase silicon sweep: pre-training / RL / prefill / decode procurement split'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-10-inference-silicon-deep-research
  title: 'Deep research: measured vs claimed inference-silicon economics (adversarially verified, 23/25 claims confirmed)'
  date: '2026-07-10'
  kind: web
neighbors: []
---
**SRAM is the fast, volatile, six-transistor on-chip memory that every processor's caches and every AI accelerator's local buffers are built from, and in 2026 it is simultaneously the performance enabler of memory-bound AI workloads and the area/energy bottleneck that a dozen emerging memory technologies are explicitly benchmarked against.**

## Summary

Static random-access memory stores each bit in a cross-coupled latch of transistors (classically six, hence "6T") rather than in a capacitor like DRAM or a resistive/ferroelectric element like the emerging non-volatile memories. Because the bit is held actively by the latch, SRAM needs no refresh, reads and writes in nanoseconds or less, is built in the same logic process as the compute it sits next to, and has effectively unlimited endurance. The costs are equally structural: six transistors per bit make it the least dense memory in the hierarchy, and the latch leaks continuously, so a large SRAM array burns static power even when idle. Those two properties, fast and sparse, set the shape of every modern memory hierarchy: SRAM for registers, caches and accelerator scratchpads; DRAM/HBM for capacity and bandwidth; Flash for bulk storage.

The parameters that decide SRAM's fate are bitcell area at a given node, leakage per bit, and the ratio of on-chip capacity to working-set size for the workload in question. Recent architecture literature makes the tension explicit. For small language model inference on edge platforms, "SRAM provides fast access but has low density" while DRAM suffers bandwidth contention between static weights and dynamic KV cache, which is the stated motivation for hybrid ReRAM/MRAM memory organisations. In digital neuromorphic processors, on-chip SRAM and STT-MRAM have themselves "become significant consumers of area and energy, leading to a new memory wall". At the other extreme, when there is enough of it, SRAM removes the bottleneck entirely: mapping 2D stencils onto the Cerebras WSE-3, whose distributed on-chip SRAM and mesh interconnect "effectively eliminate the off-chip memory bottlenecks common in GPU implementations", gave speedups up to 342x over a single-precision port of a state-of-the-art GPU stencil solver on an A100.

The most useful way to read SRAM in 2026 is as the industry's unit of account. Nearly every emerging-memory paper in this corpus states its result in SRAM-equivalent terms: SOT-MRAM bitcells with back-end-of-line read selectors achieve 10-40% area reduction and "eventually match sub-N3 SRAM"; NOR-type IGZO FeFETs reach a 10-A "SRAM-equivalent bitcell area" of roughly 0.016 um2 at 7 nm ground rules with sub-5 ns random access; two-terminal SOT-MRAM with out-of-plane torque efficiency of 0.051 at 20 nm reaches "write energies approaching SRAM at the 7nm technology node". Parity with SRAM, not superiority, is the target being claimed, and in these papers it is reached in design-technology co-optimisation models rather than in shipped silicon.

SRAM is also increasingly a compute substrate rather than only storage. SRAM appears as one device option in heterogeneous processing-in-memory arrays alongside ReRAM, FeFET, PCM and MRAM, is assigned latency-critical attention operations in a heterogeneous SRAM-PIM plus HBM-PIM LLM accelerator, supplies the buffers feeding systolic arrays in chiplet-based DRAM-PIM modules, and has even been implemented photonically: a 1x256 bit single-wavelength photonic SRAM array in a standard GlobalFoundries silicon photonics process sustains up to 1.5 TOPS at an average 2.5 TOPS/W in system-level modelling of HPC kernels.

## Viability (5/5)

There is no viability question about SRAM as a technology. It is the assumed on-chip memory in every architecture paper here, from 512 bytes on a 16-bit MSP430 microcontroller with no hardware multiplier to wafer-scale distributed arrays on the Cerebras WSE-3, and it is the shared budget against which accelerator designs are compared: an NTT-versus-SumCheck zero-knowledge-proof study evaluates both primitives "under the same level on-chip SRAM and off-chip bandwidth budgets".

The live question is not whether SRAM works but whether it keeps scaling. The sources document the two failure modes directly: high leakage power of CMOS-based SRAM as the motivation for non-volatile SRAM designs, and low density versus memristive alternatives that are "nonvolatile, have low leakage, and are dense in comparison to CMOS-based memories like SRAM". Neither is presented as an existential threat in the near term; both are presented as reasons to build hybrid hierarchies around SRAM rather than without it.

**TLDR: The incumbent: shipped in essentially every digital device and used as the reference point by everyone trying to displace it.**

## Drivers (4/5)

Demand: the workload mix has moved towards operations SRAM is uniquely good for. LLM decoding is dominated by memory-bound GEMV or flat GEMM with low operational intensity, and the KV cache grows with context length. That makes low-latency local storage the scarce resource: HPIM maps latency-critical attention to its SRAM-PIM subsystem specifically to exploit ultra-low latency and computational flexibility, leaving weight-intensive GEMV to HBM-PIM. Edge deployment pushes in the same direction, where memory, latency and energy budgets are all binding at once. One source also cites a multi-year global semiconductor supply constraint as a reason to refactor models to fit memory already in mass production.

Supply: the constraint is area and static power, not fabrication readiness. In digital neuromorphic processors, on-chip memory has become a dominant area and energy consumer, and the authors argue that without re-organising memory these processors "may struggle to compete effectively in edge and embedded applications". The DTCO literature frames future nodes as "sub-N3 SRAM" targets that alternatives can now reach, which is a supply-side signal that per-bit density improvement is getting harder.

**TLDR: Demand for on-chip capacity is rising sharply with memory-bound AI decoding; supply-side bitcell scaling and leakage are the binding constraints.**

## Novelty (2/5)

Judged as a technology to be excited about, SRAM is old and its advantages are being encroached on from several directions at once. Against SRAM on density: FeFET NOR bitcells at 10-A SRAM-equivalent area (~0.016 um2, 7 nm ground rules) with sub-5 ns random access; a 4T cross-coupled FeFET differential bit-cell smaller than conventional 6T SRAM and many prior nvSRAM designs, with 0.13 uW store power and 2 ns store time and no explicit backup-and-restore; and a 128-neuron ferroelectric compute-in-memory system claiming 25-40x area reduction over SRAM-based digital systems. Against SRAM on leakage: memristive memories are non-volatile with low leakage and higher density.

What SRAM is still better than, on the evidence here, is everything else on latency and write cost. The most advanced two-terminal SOT-MRAM projection only reaches "write energies approaching SRAM" at 7 nm and needs emerging out-of-plane-torque materials to do it. SOT-MRAM cells that match sub-N3 SRAM area do so with a read penalty: low-drive IGZO-FET selectors cost up to 3-5 ns latency and diode selectors 2.5-5x energy relative to 2T1R. FeFETs still have acknowledged writability challenges, and emerging non-volatile memories introduce device noise that quantised models must be designed around. Low score here reflects maturity, not weakness.

**TLDR: SRAM is the baseline, not the novelty; its remaining edge is latency, write energy and endurance, and that edge is being narrowed to parity in models rather than in silicon.**

## Diffusion (5/5)

SRAM requires no new process, no new toolchain and no reliability qualification programme, which is precisely why it appears as the default in every source here across microcontrollers, GPUs and wafer-scale engines, PIM accelerators and chiplet memory modules. Overview treatments of the memory landscape list SRAM first among volatile technologies alongside DRAM, eDRAM and Flash.

The real diffusion barrier is the inverse of the usual one: the cost of adding capacity. Because SRAM does not shrink as fast as designers need and leaks while idle, architecture teams are increasingly forced into heterogeneous organisations that use SRAM sparingly and alongside something denser, whether ReRAM plus MRAM at the edge or multi-device PIM chiplets whose scheduling across ReRAM, SRAM and FeFET tiers is itself a hard optimisation problem under power and thermal constraints. Displacement of SRAM in the parts of the hierarchy where latency dominates is not visible in these sources.

**TLDR: Already universal; the adoption question is how much of it a design can afford, not whether to use it.**

## Impact (4/5)

The clearest quantification in the corpus is the wafer-scale result: with enough distributed on-chip SRAM and a mesh interconnect to feed it, off-chip bottlenecks disappear and a 2D stencil framework achieved up to 342x speedup over an adapted state-of-the-art GPU solver at matched single precision, with roofline analysis confirming saturation of the achievable bound. That is a statement about how much value sits in SRAM capacity rather than in flops. Similarly, SRAM-PIM is what makes latency-critical attention tractable in a heterogeneous LLM accelerator, and SRAM-based buffers are what allow chiplet PIM modules to host systolic arrays that DRAM-process PIM could not support.

The counterweight, which keeps this below 5, is that SRAM is also where a growing share of area and energy goes, to the point that neuromorphic designs risk uncompetitiveness in edge and embedded roles because of it. The 342x figure is a single workload class on one specialised machine and should not be read as a general accelerator result. SRAM's impact is high but increasingly bounded by what a die can afford to spend on it.

**TLDR: On-chip SRAM capacity is one of the strongest single determinants of performance on memory-bound AI and HPC kernels; the demonstrated swing is orders of magnitude.**

## Timing Now (0-2yr)

Nothing about SRAM is prospective. It is in every device discussed here, and the architectural decisions being made now, how much on-chip capacity to buy, how to partition KV cache between SRAM and DRAM/HBM, whether to place compute inside the SRAM array, are live commercial choices.

The substitution timeline is later and less certain. The alternatives that claim SRAM-class area or write energy do so in DTCO and simulation at representative 7 nm nodes and require material or device advances that are not yet demonstrated at product scale: out-of-plane SOT materials with efficiency around 0.05 at 20 nm widths, positive-Vt engineering via ferroelectric layer thinning to fix sneak-current sensing margins in NOR FeFET arrays, and free-layer engineering to hit 0.1-100 s retention targets for last-level cache SOT-MRAM. Where substitution appears first is read-dominated and last-level tiers, not L1.

**TLDR: SRAM is deployed and decisive today; the interesting timing question is when its density and leakage limits force partial substitution.**

## Overrated or underrated? Fairly rated

SRAM's position is well understood by the people who build with it, and the sources bear out both halves of the consensus: it is the fastest thing on the die and the most expensive per bit, so the entire emerging-memory research programme is organised around reducing how much of it a design needs. The corpus contains a striking uniformity of framing: SOT-MRAM "matching sub-N3 SRAM" area, FeFETs at "SRAM-equivalent bitcell area", SOT write energy "approaching SRAM". When the aspiration of an entire competing field is parity, the incumbent is not in immediate danger.

If there is a mispricing, it is that the density-focused critique understates how much performance is currently being bought with SRAM capacity alone. The wafer-scale stencil result, 342x over an adapted GPU solver purely by removing off-chip access, suggests that in memory-bound regimes more SRAM is still one of the highest-leverage design choices available, even at poor density. Conversely, the neuromorphic critique that on-chip memory has itself become the new memory wall is the strongest argument that this cannot continue indefinitely. Both are correct; the resolution in the sources is hybrid hierarchies, not replacement.

## Prediction

By the end of 2028, emerging non-volatile memories (MRAM, FeFET, ReRAM) will have displaced SRAM only in last-level cache and read-dominated on-chip tiers in shipping products, with no commercial processor or AI accelerator replacing its L1/L2 SRAM, and published DTCO claims of SRAM parity will still exceed demonstrated silicon.

## Evidence base

- SRAM's core trade-off stated plainly for edge LLM inference: fast access but low density, with DRAM contending between static weights and dynamic KV cache and Flash inactive during inference, motivating hybrid ReRAM/MRAM hierarchies (2026-01-21).
- Distributed on-chip SRAM plus mesh interconnect on the Cerebras WSE-3 eliminated off-chip memory bottlenecks and produced up to 342x speedup over a single-precision port of a state-of-the-art GPU stencil solver on an A100 (2026-05-08).
- SOT-MRAM bitcells with BEOL read selectors achieve 10-40% area reduction and eventually match sub-N3 SRAM, but at a read cost of 3-5 ns extra latency (IGZO-FET selectors) or 2.5-5x energy (diode selectors) versus 2T1R (2025-08-25).
- NOR-type IGZO FeFETs deliver down to 10-A SRAM-equivalent bitcell area (~0.016 um2) at 7 nm ground rules with sub-5 ns random access, despite writability challenges and sneak-current sensing-margin penalties (2026-04-15).
- Two-terminal SOT-MRAM with out-of-plane SOT efficiency of 0.051 at 20 nm width reaches write energies approaching SRAM at 7 nm; conventional in-plane-torque SOT materials give little or no improvement over STT-MRAM (2025-12-05).
- In digital neuromorphic processors, on-chip SRAM and STT-MRAM have become significant consumers of area and energy, constituting a new memory wall that could make such processors uncompetitive at the edge (2026-04-09).
- A 4T cross-coupled FeFET differential bit-cell smaller than conventional 6T SRAM operates in volatile or non-volatile mode with 0.13 uW store power, 2 ns store time and no explicit backup-and-restore (2026-06-19).

## Open questions

- Do any of the SRAM-parity claims (10-40% SOT-MRAM area reduction, 10-A SRAM-equivalent FeFET bitcells, write energy approaching SRAM at 7 nm) survive fabrication and yield at a production node, or do they remain DTCO projections?
- At what accelerator scale does on-chip SRAM stop being worth its area and energy? The neuromorphic analysis says it has already crossed that line for edge and embedded designs; is the same true for datacentre inference silicon?
- For LLM decoding specifically, how much of the KV cache genuinely needs SRAM-class latency versus HBM or PIM-attached DRAM, given HPIM's partitioning of attention to SRAM-PIM and GEMV to HBM-PIM?
- Can nvSRAM variants such as the 4T cross-coupled FeFET bit-cell deliver leakage savings without endurance or write-disturb penalties in a real cache, and at what read margin?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
