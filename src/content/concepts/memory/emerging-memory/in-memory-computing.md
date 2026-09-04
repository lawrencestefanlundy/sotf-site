---
type: concept
slug: in-memory-computing
canonical_name: In-Memory Computing
aliases:
- in-memory compute
kind: technology
parent_concepts:
- memory
- emerging-memory
related_concepts:
- memcapacitor
- analog-computing
- memory-wall
- von-neumann-bottleneck
- processing-in-memory
sources:
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2026-05-14-compute-is-defence-now]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2026-04-28-making-ai-inference-cheap-with-analog]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2024-10-23-optical-dram-integrated-non-reciprocal-magneto-optics-with]]'
scorecard:
  viability: 3
  drivers: 4
  novelty: 4
  diffusion: 2
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 60
descendants:
- adc-bottleneck
- analog-in-memory-compute
- capram
- charge-domain-compute
- digital-in-memory-compute
- processing-in-memory
- sram-cim
sources_7d: 4
sources_30d: 7
recent_mentions:
- slug: 2026-08-12-snapdragon-ar1-sensing-hub-micro-npu
  title: Snapdragon AR1 Gen 1 Platform Product Brief — Sensing Hub with Micro NPU for audio and sensors
  date: '2026-08-12'
  kind: web
- slug: 2026-07-31-inference-silicon-roster-sprint
  title: 'Inference-silicon roster verification sprint: 10 companies for the competitive-analysis capital map'
  date: '2026-07-31'
  kind: web
- slug: 2026-05-14-compute-is-defence-now
  title: Compute Is Defence Now
  date: '2026-05-14'
  kind: substack
- slug: 2026-04-28-making-ai-inference-cheap-with-analog
  title: Making AI inference Cheap with Analog Computing w/ Shwetank Kumar @ EnCharge AI
  date: '2026-04-28'
  kind: substack
- slug: 2026-01-22-ai-chips-computeram-and-the-future
  title: 'AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara'
  date: '2026-01-22'
  kind: substack
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2024-12-04-cubits-in-a-fridge-why-is-nobody
  title: Silicon Spin Quantum Computing (Feat. Himadri Majumdar, SemiQon)
  date: '2024-12-04'
  kind: substack
- slug: 2024-10-29-deploy-intelligence-too-cheap-to
  title: Deploy! Intelligence too cheap to meter @ $0.0001 per million tokens.
  date: '2024-10-29'
  kind: substack
neighbors:
- slug: memcapacitor
  name: Memcapacitor
  path: /memory/emerging-memory/memcapacitor/
  macro: memory
- slug: analog-computing
  name: Analog Computing
  path: /compute/non-conventional/analog-computing/
  macro: compute
- slug: memory-wall
  name: The Memory Wall
  path: /compute/compute-architecture/memory-wall/
  macro: compute
- slug: von-neumann-bottleneck
  name: Von Neumann Bottleneck
  path: /compute/compute-architecture/von-neumann-bottleneck/
  macro: compute
- slug: processing-in-memory
  name: Processing-in-Memory (PIM)
  path: /memory/emerging-memory/processing-in-memory/
  macro: memory
---
**In-memory computing performs arithmetic inside the memory array itself, using the physics of resistive, ferroelectric, magnetic or photonic memory cells to do matrix-vector multiplication where the data already sits, and it is now producing fabricated chips in narrow edge roles while its large datacentre efficiency claims remain simulation-bound.**

## Summary

Conventional processors spend most of their energy moving data between memory and arithmetic units, not on the arithmetic. In-memory computing (IMC, also called compute-in-memory or processing-using-memory) removes that movement by encoding numbers as the conductance, capacitance or optical transmission of memory cells arranged in a crossbar, then reading out a whole matrix-vector multiplication (MVM) in one analog step. A related, more conservative family is processing-in-memory (PIM), which places modest digital compute units next to memory banks to exploit internal bandwidth rather than computing with device physics directly. Both target the same class of problem: workloads that are memory-bound rather than arithmetic-bound, such as neural network inference, graph traversal and approximate nearest neighbour search.

The device layer is unusually fragmented. Filamentary memristors (Ag/Cu in amorphous silicon) are the classic crossbar element; phase-change memory with superlattice materials is used where multi-level, low-voltage programming matters; magnetic tunnel junction MRAM and antiferromagnetic tunnel junctions offer non-volatility, endurance and picosecond switching; ferroelectric HfO2/ZrO2 capacitors give non-destructive readout; standard-CMOS floating-gate arrays give a cheap route with no exotic materials; and silicon photonic arrays trade device density for bandwidth.

The parameters that decide the technology are all non-idealities rather than headline throughput. Device-to-device and cycle-to-cycle variation arises because conduction is carried by a small number of discrete filaments rather than uniformly across the device area. Conductance drifts, so inference accuracy decays after programming. Read windows are small: ferroelectric non-volatile capacitors have a memory window of 1-10 fF/um and sense margins of the order of a few millivolts, and antiferromagnetic junctions have low tunnel magnetoresistance that breaks standard MRAM sense amplifiers. On-chip training adds a further problem: asymmetric weight updates drag the weights towards a device-specific symmetric point that does not coincide with the optimum, and calibrating that point costs pulse updates. System-level gains also depend on conversion and external memory access overheads, not just the array.

The consequence is that IMC is currently strongest where the workload is small, fixed, tolerant of noise and starved of power: an implanted 32-channel brain-machine interface SoC in 65 nm CMOS uses an IMC spike detector and runs at 3.53 uW per channel with 0.034 mm2 per channel. The large claims, LLM inference acceleration and Monte Carlo tree search at tens of milliwatts, sit at the architecture-simulation level with fabricated device parameters as inputs.

## Viability (3/5)

The physics works and silicon exists. A single-poly floating-gate analog IMC array has been fabricated in standard 65 nm CMOS and measured; a fabricated IMC chip was used to emulate a nonlinear closed-loop MIMO decoder; a complete event-based implant SoC with an IMC spike detector has been built in 65 nm; ferroelectric HfO2/ZrO2 stacks have been integrated in the CMOS back end of line with 1 ns multi-level writes below 5 V, endurance above 10^11 cycles and 10-year retention. Photonic arrays are fabricated on a standard GlobalFoundries silicon photonics process.

What holds the score at 3 is that the same literature is dominated by defect papers. Conduction in filamentary memristors is carried by a handful of discrete filaments, which is the direct cause of device-to-device and cycle-to-cycle spread, and systematic studies of filament statistics are described as scarce even though large arrays have been demonstrated. Ferroelectric capacitor memory windows collapse above 1 MHz read frequency, requiring a new sub-RC 20 ps readout method to get around it. Retention loss degrades inference accuracy, and even with circuit compensation plus batch-normalisation recalibration the baseline is only recovered to within 2-4% after 60 days. Analog on-device training remains the weakest link, with update asymmetry biasing convergence and calibration itself carrying a pulse cost that has only recently been characterised theoretically. This is a technology that works when co-designed end to end, not one that drops in.

**TLDR: Arrays and small SoCs are fabricated and measured, but every device family still has an unresolved non-ideality that has to be compensated in circuits or algorithms.**

## Drivers (4/5)

On the demand side the sources give several independent pulls. Graph-based approximate nearest neighbour search is described as fundamentally memory-bound, with CPU throughput capped by main memory bandwidth and GPUs lacking the high-bandwidth memory capacity to hold billion-scale indexes. State-space model inference on conventional architectures suffers quadratic intermediate materialisation and excessive memory traffic. 6G MIMO detection imposes a 0.1 ms latency budget that motivates nanosecond analog MVM rather than faster algorithms alone. Implantable channel counts are scaling, forcing compute onto the implant at microwatt budgets. Edge continual learning generates data movement between processors and memory that makes it impractical without IMC. Monte Carlo tree search is quoted at 55-300 W on conventional processors, which excludes it from edge deployment.

On the supply side, the enabling trend is that IMC-capable devices are being built in or on top of standard processes rather than bespoke lines: back-end-of-line ferroelectric layers on CMOS, floating-gate arrays in a standard 65 nm CMOS flow, MTJ-based MRAM described as CMOS-compatible with high endurance, and a commercial silicon photonics process. The supporting tool chain is visibly lagging: existing compact models fail to capture small-signal capacitance, variability and cycling degradation, the parameters circuit designers actually need. The sources do not show volume manufacturing commitments or product roadmaps from memory makers, so this is demand-led rather than supply-led.

**TLDR: Demand is clear and multi-sector: memory-bound AI workloads, microwatt implants and sub-0.1 ms radio latency; supply is a broad but immature menu of device options.**

## Novelty (4/5)

Two caveats keep this from a 5. First, the GPU comparisons in these sources come from simulation and modelling rather than measured full-system silicon, so they carry the usual optimism of projected accelerator numbers. Second, where honest system modelling is done, absolute numbers are modest: a 1x256-bit single-wavelength photonic SRAM array sustains 1.5, 0.9 and 1.3 TOPS on three HPC kernels at an average 2.5 TOPS/W once external memory access and opto-electronic conversion latency are accounted for. The advantage is real in the primitive but shrinks as the system boundary widens.

**TLDR: Reported advantages over CPUs and current GPUs are one to three orders of magnitude in energy, but nearly all cross-comparisons are architecture-level simulations calibrated on fabricated devices.**

## Diffusion (2/5)

The recurring phrase across these papers is co-design. SpecPCM integrates contributions at application, algorithm, circuit, device and instruction-set levels, and optimises different PCM materials for different tasks, specifically to overcome non-ideal device behaviour. AFMTJ arrays need a purpose-built asymmetric pulse driver and a self-timed sense amplifier because standard MRAM front ends are unreliable at those speeds and TMR levels. Monte Carlo tree search only maps onto IMC after a phase-to-primitive decomposition that rewrites each algorithmic phase into a hardware-native form, because IMC has been considered incompatible with irregular multi-phase algorithms. PIM ports of graph ANNS run into small local memories, costly inter-unit communication, host coordination overhead and weak in-memory compute units, which had pushed earlier designs onto lower-recall cluster indexes. Training support is described as poor and often incomplete, and IMC computation as noisy enough to significantly harm training accuracy.

That is the profile of a technology that diffuses per application rather than as a platform. Two further blockers appear directly in the sources: compact models adequate for circuit design do not yet exist for at least one important device family, and analog weights need periodic recalibration or algorithmic compensation to hold accuracy over weeks, which imposes a lifecycle burden on whoever deploys the part. Nothing in these sources indicates a commercial product, standard interface or software stack, so the near-term route is captive designs inside SoCs whose owner controls the whole stack, exactly as in the implant case.

**TLDR: Every reported win requires application-specific co-design across algorithm, circuit and device, and the design tooling for that co-design is admittedly incomplete.**

## Impact (4/5)

The value is asymmetric across settings. In the datacentre the prize is an efficiency multiple on LLM inference, quoted at 30 to 57 times over A100 and H100 class parts in a photonic-chiplet IMC design, which if even partly realised in silicon would matter to capital and power planning. In embedded settings the prize is qualitative rather than incremental: 55-300 W workloads collapsing to roughly 60 mW makes on-device tree search possible where it was previously impossible, and 3.53 uW per channel with on-chip motor decoding at about 0.62 R2 is the difference between an implant that works and one that overheats or needs a tether. Nanosecond MVM inside the radio chain addresses a latency requirement, 0.1 ms, that cannot be met by algorithm choice alone.

There is also a category of problem that IMC changes rather than accelerates: embedding an optimisation problem directly in the continuous-time dynamics of a nonlinear feedback network of memory arrays, so the solution emerges from physical relaxation instead of iterated linear algebra. Similarly, memory-centric dataflow for state-space models attacks quadratic intermediate storage structurally rather than by throwing bandwidth at it. The score stops at 4 because the sources do not demonstrate impact at delivered scale, only impact per fabricated array or per simulated system.

**TLDR: If the non-idealities are tamed, it changes what can be computed inside a power budget of milliwatts, which opens implants, edge learning and radio-layer inference as well as datacentre energy.**

## Timing Soon (2-5yr)

The earliest real uses are already here in the restricted sense: an IMC block inside a fabricated 65 nm implant SoC, and fabricated analog arrays and IMC chips used for measured experiments. Those are single-function, error-tolerant, owner-designed blocks and they can proliferate on a two to five year horizon without solving the general problem.

The general problem is further out. As of mid-2026 the literature is still publishing first theoretical characterisations of calibration cost for analog training, still calling systematic filament statistics scarce, and still building the compact models that circuit designers need before tape-out. Large-model inference acceleration remains at the level of simulated 3D-stacked photonic chiplet systems. Treat datacentre-scale analog IMC as a Later (5-10yr) proposition and the embedded wave as the thing to watch now.

**TLDR: Narrow, power-critical embedded roles are already in fabricated silicon; broad accelerator adoption depends on variation, retention and training problems that are still open research in 2026.**

## Overrated or underrated? Fairly rated

IMC is neither vapour nor imminent displacement of GPUs, and the source base supports exactly that middle position. The strong claims are all coherent and the physics argument, that moving the multiply to where the data lives removes the dominant energy cost, is not in dispute. But the 2026 evidence splits cleanly: what is fabricated and measured is small, narrow and tolerant of noise, while what promises 30 to 2,000 times efficiency over current GPUs is simulated architecture built on fabricated device parameters.

The sharper reading is that the field has quietly changed target. The papers here are less about beating GPUs at dense training and more about making specific memory-bound or power-bound problems tractable: billion-scale graph search that does not fit in HBM, 0.1 ms radio latency, continual learning on edge platforms, microwatt implants. Investors reading IMC as an AI-training play are likely to be disappointed; reading it as an enabling block for power-constrained and bandwidth-starved systems is well supported. The honest caution is that the discipline is still spending most of its effort compensating for its own devices, and one system-level modelling paper shows absolute throughput of a real fabricated photonic array in the single-TOPS range once overheads are counted.

## Prediction

By the end of 2028, published analog in-memory computing results claiming order-of-magnitude efficiency advantages over H100-class GPUs on large language model inference will still rest on architecture-level simulation rather than measured full-system silicon, while shipped IMC will remain confined to sub-milliwatt-class embedded blocks of the kind fabricated in 2026.

## Evidence base

- 2026-07-28: An RRAM-based multi-primitive IMC design runs 9x9 Go Monte Carlo tree search at about 60 mW at 22 nm with fabricated array parameters, reported at 96x CPU and 65x-2,059x H100 energy efficiency, and reaches a Go rating within sample-size uncertainty of open-source engines.
- 2026-06-02: A fabricated 32-channel event-based implant SoC in 65 nm CMOS with an IMC spike detector consumes 3.53 uW per channel, gives up to 26x frontend data compression and achieves about 0.62 decoding R2 in 0.034 mm2 per channel.
- 2026-06-03: Ferroelectric HfO2/ZrO2 layers integrated in the CMOS back end achieve 1 ns multi-level writes below 5 V, endurance above 10^11 cycles and 10-year retention, but the memory window collapses above 1 MHz read frequency, requiring a new 20 ps non-destructive readout method.
- 2026-07-29: On a 65 nm single-poly floating-gate analog IMC array, circuit compensation plus batch-normalisation recalibration recovers baseline inference accuracy to within 2-4% sixty days after programming on VGG-10/CIFAR-10 and WideResNet-28-10/CIFAR-100.
- 2026-06-07: A fabricated 1x256-bit single-wavelength photonic SRAM array on a standard GlobalFoundries silicon photonics process sustains 1.5, 0.9 and 1.3 TOPS on three HPC kernels at an average 2.5 TOPS/W once external memory access and opto-electronic conversion overheads are modelled.
- 2026-06-05: A PIM co-design for graph-based approximate nearest neighbour search shrinks the PIM-resident index footprint by 14.5x, addressing a workload where CPU throughput is capped by main-memory bandwidth and GPUs lack the HBM capacity for billion-scale indexes.

## Open questions

- Can device-to-device and cycle-to-cycle variation in filamentary crossbars be bounded by process control rather than by per-array calibration, given that conduction is carried by a small number of discrete filaments?
- Does retention-loss compensation hold beyond the 60-day, 2-4% accuracy recovery demonstrated on floating-gate arrays, over product lifetimes and across temperature?
- Will any of the simulated GPU comparisons, in particular the 30x to 57x photonic-chiplet efficiency claims, be reproduced on fabricated multi-chiplet silicon running a real model?
- Can on-device analog training converge without pre-calibration, and at what pulse cost, once symmetric-point drift is tracked dynamically at model scale?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
