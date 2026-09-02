---
type: concept
slug: mram
canonical_name: MRAM (STT/SOT-MRAM)
aliases: []
kind: technology
parent_concepts:
- memory
- mainstream-memory
related_concepts: []
sources:
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2024-yole-emerging-memories-2024]]'
- '[[2026-06-22-beyond-cmos-device-layer-research]]'
- '[[2026-04-29-optical-dram-everspin-reports-q1-2026-financial-results]]'
- '[[2026-06-04-globalfoundries-emram-22fdx-availability]]'
frontier:
- Can any real material deliver out-of-plane SOT efficiency near 0.05 at 20 to 30 nm device widths, which is the condition on which the 2T-SOT write-energy advantage over STT depends 2026 06 05 modeling and optimization of two terminal spin orbit torque ?
- Do the architectural fixes for read disturbance accumulation (selective tag comparison, per-read ECC discipline) hold up in measured silicon rather than gem5 simulation, and what is their true area and latency cost 2026 06 05 3rset read disturbance rate reduction in stt mram caches by  2026 06 05 enhancing reliability of stt mram caches by eliminating read?
- Does the 3.5 fJ per bit VCMA switching result survive transfer from single junctions to full arrays with process variation, and at what write error rate 2026 06 05 interface engineered voltage driven magnetic tunnel junction?
- Do cross-coupled bitcells that lift the high-to-low current ratio to 8000 cost enough area to erase MRAM's density advantage over SRAM for in-memory computing 2026 06 05 stride cross coupled stt mram enabling robust in memory comp?
- Does any MRAM-CIM (in-array compute) reach product, or does MRAM stay a cache / eNVM device?
- How far does eMRAM displace eFlash at advanced nodes?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 51
last_reorg_date: '2026-05-14'
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 1
sources_30d: 1
recent_mentions:
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-04-globalfoundries-emram-22fdx-availability
  title: GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform
  date: '2026-06-04'
  kind: web
- slug: 2026-04-29-optical-dram-everspin-reports-q1-2026-financial-results
  title: Everspin Reports Q1 2026 Financial Results
  date: '2026-04-29'
  kind: web
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
- slug: 2024-yole-emerging-memories-2024
  title: Yole Group — Emerging Non-Volatile Memories 2024
  date: '2024-10-15'
  kind: web
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
- slug: 2023-06-23-e05-the-future-of-edge-ai-brain-inspired
  title: '🔮 E05: Neuromorphic Computing & The Future of Edge AI'
  date: '2023-06-23'
  kind: substack
neighbors: []
---
**MRAM stores bits as the magnetic orientation of a nanoscale magnetic tunnel junction, and is being pushed as a non-volatile, near-zero-leakage replacement for SRAM caches and as a substrate for in-memory computing, but write energy and read/write error rates remain the binding constraints.**

## Summary

Magnetoresistive RAM (MRAM) stores each bit in a magnetic tunnel junction (MTJ): two ferromagnetic layers separated by a thin MgO barrier. When the free layer's magnetisation is parallel to the fixed reference layer the junction resistance is low; when antiparallel it is high. The ratio between the two states is the tunnel magnetoresistance (TMR), and it sets how easily a sense amplifier can tell a 1 from a 0. Modern cells use perpendicular magnetic anisotropy (PMA) so the magnetisation points out of plane, which allows scaling to small diameters while keeping enough thermal stability for retention.

The write mechanism defines the variants. In STT-MRAM, current passed through the junction itself carries spin angular momentum that torques the free layer; this is the mainstream approach and is described in the literature as the leading candidate to replace SRAM in on-chip caches on the strength of near-zero leakage power, higher density, non-volatility and immunity to radiation-induced upsets. Because write and read share the same current path, reads can accidentally flip the bit: the read disturbance error. In SOT-MRAM, write current runs through an adjacent heavy-metal line and injects spin current sideways, decoupling read from write, at the cost of a larger (typically three-terminal) cell; two-terminal SOT variants are under study to recover density. A third route uses voltage-controlled magnetic anisotropy (VCMA), where a gate field rather than a current lowers the switching barrier.

The parameters that decide the technology are: write energy per bit and write pulse length; write error rate at that pulse length; TMR and hence sense margin; read disturbance rate; endurance; and the resistance-area (RA) product of the barrier, which trades off read signal against write current density. These are not independent. Raising RA to strengthen VCMA suppresses STT and Joule contributions and changes the switching physics entirely, which is why RA is used experimentally to separate the three mechanisms. Similarly, shortening the DC write pulse improves endurance but pushes up write error rate unless the switching is assisted, for example by a prior radio-frequency spin-torque pulse or by shaping the STT pulse in combined SOT+STT field-free schemes.

## Viability (3/5)

There is genuine experimental substance here, not just simulation. Interface-engineered voltage-driven MTJs have demonstrated 3.5 fJ per bit switching in the sub-nanosecond regime while retaining TMR up to 160 per cent after a 400 C post-anneal, which matters because that anneal is a back-end integration requirement. Gate-voltage switching-field experiments on synthetic antiferromagnetic free layers separate STT, VCMA and Joule heating contributions quantitatively across barrier thicknesses. Field-free SOT+STT switching has been demonstrated experimentally in top-pinned stacks, with pulse shaping shown to reduce write error rate. Circuit work treats embedded STT-MRAM process flows as standard and CMOS-co-integrable.

What holds the score at 3 is that the failure modes are described as severe and unresolved in the same literature. Read disturbance is called a severe reliability challenge for STT-MRAM caches, and the parallel tag reads used in set-associative caches are shown to accumulate disturbance errors that materially degrade reliability. Combined SOT+STT switching introduces backhopping and an intermediate loss-of-determinism regime. For in-memory computing, inherently low distinguishability plus array non-idealities and process variation are reported to cause severe inference accuracy degradation without dedicated bitcell redesign. The sources contain no yield, volume-production or product-level data, so viability beyond the device and macro level cannot be judged from them.

**TLDR: The device physics works and is being measured on real junctions, but array-level reliability is still an active research problem rather than a solved one.**

## Drivers (4/5)

Demand: the stated pull is SRAM's leakage and density limits in on-chip caches, where MRAM's near-zero leakage, higher density and radiation immunity are the attraction. A second, currently louder driver is AI at the edge. Heterogeneous memory schemes place critical outlier weights in high-precision on-chip MRAM while bulk inlier weights sit in multi-level ReRAM, specifically because MRAM is the less noisy of the emerging non-volatile options. MRAM also appears as one device among several in 3D heterogeneous processing-in-memory accelerators for GNN training, as content-addressable memory for proteomics database search, and in security and stochastic-computing roles: PUFs from write-time variation and true random number generators at 0.5 to 1 Gb/s per superparamagnetic device.

Supply: MTJ stacks survive 400 C annealing with TMR intact, stochastic-write MTJ TRNGs are said to leverage standard CMOS MTJ process flows enabling co-integration with embedded STT-MRAM, and macros have been designed and evaluated at 28 nm and 7 nm. The supply-side constraint is materials: SOT layers providing only in-plane torque give little to no write-energy improvement over STT, and the gains depend on emerging materials with out-of-plane torque.

**TLDR: Demand is pulled hard by SRAM leakage and by edge AI memory budgets; supply is helped by CMOS-compatible MTJ flows, though the best-performing write mechanisms need new materials.**

## Novelty (3/5)

Against SRAM, the claimed advantages are lower leakage power, higher density, scalability, non-volatility and immunity to radiation-induced particles. The honest quantification comes from the 2T-SOT benchmarking: write energies only approach SRAM at the 7 nm node, and only for 20 nm-wide devices with an out-of-plane SOT efficiency of 0.051, a materials condition that is presented as emerging rather than available. So MRAM is not yet unambiguously better than SRAM on the metric that matters most for cache write traffic. The VCMA route posts 3.5 fJ per bit sub-nanosecond switching, which is the strongest single device-level number in these sources.

Against other non-volatile memories, MRAM's differentiator is high endurance and low device noise: it is preferred for outlier weight storage precisely because ReRAM multi-level noise degrades quantised models, and is singled out among NVMs for in-memory computing on endurance grounds. Its structural weakness relative to RRAM and PCM is low distinguishability between states, which is why cross-coupled bitcells are needed to lift the high-to-low current ratio to as much as 8000 and gain up to 3.86x sense margin. Antiferromagnetic tunnel junctions promise picosecond switching but with TMR so low that conventional MRAM read interfaces are reported as unreliable - a reminder that the next magnetic device generation may trade away the one thing MRAM sense circuits depend on.

**TLDR: Clearly better than SRAM on leakage and density and better than ReRAM/PCM on endurance and noise, but the write-energy advantage over SRAM only appears under conditions not yet met.**

## Diffusion (3/5)

The pattern across these sources is that MRAM cannot simply be dropped into an existing memory socket. Cache reliability requires either aggressive ECC on every read, which costs access time, or architectural changes such as selectively disabling tags that cannot hit, which reduces tag-array read disturbance rate by 71.8 per cent in gem5 full-system simulation. In-memory computing requires new bitcell topologies to make the states distinguishable at all, and new read/write front-ends when the magnetic device is faster or lower-TMR than existing drivers assume. Field-free switching is explicitly framed as a prerequisite for industrial deployment of SOT-MRAM, and is still being made deterministic through pulse shaping.

The counterweight is that the easiest diffusion paths avoid the hard problems. TRNG cells are read-only or use standard MTJ flows, occupy deep sub-0.01 square micrometre footprints, have passed NIST SP800 validation, and offer orders-of-magnitude better energy efficiency than CPU/GPU generators. PUFs exploit manufacturing variation rather than fighting it. Hybrid architectures use MRAM for a small, high-value slice of the weight tensor rather than the whole memory. Expect diffusion to happen sideways into these niches before it happens frontally into caches.

**TLDR: Adoption is being unblocked by architectural and circuit workarounds rather than by the device itself, which raises the integration cost of switching.**

## Impact (4/5)

If STT-MRAM genuinely replaces SRAM in on-chip cache, the payoff is structural: leakage power in large last-level caches disappears, density improves and the cache becomes non-volatile and radiation-hard. That is a change to every processor rather than a niche win. The compute-in-memory numbers are also substantial where reported: an event-driven spiking SOT-MRAM CIM macro in 28 nm reaches a peak 243.6 TOPS/W by encoding signals as spikes and removing the analogue front end; a 3D heterogeneous PIM accelerator including MRAM reports up to 3.8x energy efficiency and 6.8x compute density gains over prior PIM architectures; a 3T2MTJ SOT-MRAM CAM in 7 nm performs proteomics database search on a 131 GB dataset at 1.19 mJ setup for 2M spectra and 1.1 uJ per 1000 queries.

The caveat is that most of these figures come from simulation and macro-level evaluation rather than measured silicon at scale, and the value is contingent on the reliability fixes being cheap. Impact is scored on the size of the prize, which is large and well evidenced in direction if not in delivery.

**TLDR: Replacing leaky SRAM in caches or hosting compute-in-memory would be a first-order change to chip energy budgets, and the reported macro efficiencies are large.**

## Timing Soon (2-5yr)

The narrow applications look close. MTJ true random number generators already produce NIST-validated bit streams at 0.5 to 1 Gb/s per superparamagnetic device and are said to be compatible with most advanced CMOS nodes using standard MTJ flows. Hybrid memory hierarchies that use a small amount of on-chip MRAM for outlier weights need no new device physics, only a partitioning decision.

The headline use case is further out. Read disturbance accumulation in parallel-access caches was only formulated and quantified in work published on 2026-01-01, and the proposed fixes are simulated architectural schemes rather than shipped designs. Field-free SOT switching, described as a prerequisite for industrial deployment, was still being stabilised experimentally against backhopping as of 2026-04-24. The SOT write-energy case depends on out-of-plane-torque materials that do not yet exist in production form. On that evidence, broad cache-level substitution belongs in the 5 to 10 year band even if embedded and specialised uses arrive sooner.

**TLDR: Niche roles (TRNG, PUF, outlier weight storage, CAM accelerators) are near-term; SRAM cache replacement and field-free SOT-MRAM in volume are not.**

## Overrated or underrated? Fairly rated

MRAM is repeatedly called the most promising SRAM replacement in this literature, and the same literature undercuts the claim in useful detail. The device works, integrates at 400 C, retains 160 per cent TMR and can be switched with 3.5 fJ per bit in the sub-nanosecond regime under favourable interface engineering. But the two things that would make it a general SRAM substitute are missing: a write energy that beats SRAM without depending on unavailable out-of-plane SOT materials, and a read path that does not disturb the bit under the parallel-access patterns real caches use.

The realistic near-term value is narrower and, on this evidence, underpriced within the broader story: MRAM as the low-noise, high-endurance element in heterogeneous memory and in-memory-compute systems, plus randomness and identity primitives that turn its device variability into a feature. Treat claims of imminent wholesale SRAM displacement with scepticism; treat MRAM as a component in mixed-memory AI hardware as the live case. Note also that these sources are almost entirely academic preprints, with no production, cost or yield data, so this assessment is about technical trajectory rather than commercial position.

## Prediction

By the end of 2028, no published two-terminal SOT-MRAM cell will have experimentally demonstrated an out-of-plane spin-orbit torque efficiency at or above 0.05 in a 20 nm-scale device, leaving the SOT write-energy advantage over SRAM at 7 nm unrealised in silicon.

## Evidence base

- Experimental MTJs with Ir remote doping near the MgO-CoFeB interface switched at 3.5 fJ per bit in the sub-nanosecond regime while retaining TMR up to 160 per cent after 400 C annealing (published 2025-11-22).
- Benchmarking published 2025-12-05 found that in-plane-torque SOT materials give little to no write-energy improvement over STT-MRAM; only out-of-plane torque with efficiency 0.051 at 20 nm widths brings write energy near SRAM at the 7 nm node.
- Work published 2026-01-01 formulated read disturbance accumulation from parallel cache-set reads and showed it significantly increases STT-MRAM cache error rate under conventional ECC-on-request schemes; a related scheme cut tag-array read disturbance rate by 71.8 per cent in gem5 simulation (published 2025-11-27).
- Field-free combined SOT+STT switching in top-pinned devices showed STT-induced backhopping and an intermediate loss-of-determinism regime; STT pulse shaping experimentally reduced write error rate (published 2026-04-24).
- An event-driven spiking SOT-MRAM compute-in-memory macro designed in 28 nm reported peak 243.6 TOPS/W by replacing analogue circuitry with spike encoding (published 2025-11-05).
- MTJ true random number generators reached 0.5 to 1 Gb/s per superparamagnetic device with NIST SP800 validation and sub-0.01 square micrometre footprints, using flows compatible with embedded STT-MRAM (published 2025-09-16).
- Cross-coupled STT-MRAM bitcells lifted the bitcell high-to-low current ratio to up to 8000, giving up to 3.86x sense margin and 27.6 per cent read disturb margin improvement over standard MRAM in-memory-computing arrays (published 2026-04-06).

## Open questions

- Can any real material deliver out-of-plane SOT efficiency near 0.05 at 20 to 30 nm device widths, which is the condition on which the 2T-SOT write-energy advantage over STT depends?
- Do the architectural fixes for read disturbance accumulation (selective tag comparison, per-read ECC discipline) hold up in measured silicon rather than gem5 simulation, and what is their true area and latency cost?
- Does the 3.5 fJ per bit VCMA switching result survive transfer from single junctions to full arrays with process variation, and at what write error rate?
- Do cross-coupled bitcells that lift the high-to-low current ratio to 8000 cost enough area to erase MRAM's density advantage over SRAM for in-memory computing?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
