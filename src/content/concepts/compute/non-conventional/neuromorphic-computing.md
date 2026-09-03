---
type: concept
slug: neuromorphic-computing
canonical_name: Neuromorphic Computing
aliases: []
kind: technology
parent_concepts:
- compute
- non-conventional
related_concepts: []
sources:
- '[[2025-09-23-the-compute-gradient]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2023-06-30-e06-the-model-t-moment-for-bits-llms]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2026-04-01-low-power-edge-compute-neuromorphic-computing-chip-patents]]'
- '[[2026-06-17-femtoai-spu-ces2026]]'
frontier:
- Does any emerging-device crossbar reach 10^4 to 10^6 cells with the device-to-device variability of the Ge3.5Te1 CBRAM result preserved, or does the variability advantage disappear with array size 2026 06 05 electrolyte bonding engineering for highly uniform gete base?
- Can the 95% charge-recovery assumption underpinning the memcapacitor efficiency figures be measured on a real scaled device, given it alone accounts for a 17.4 times multiplier demasius 2021 memcapacitor nature electronics?
- Is there a memory organisation that removes the new on-chip memory wall in digital neuromorphic processors, and what is the measured area and energy split after it is applied 2026 06 05 memory wall is not gone a critical outlook on memory archite?
- Does any neuromorphic system, digital or analog, beat a commercial accelerator on a workload a buyer already runs, rather than on a task chosen to suit the hardware?
- 'ANSWERED (20 Jul 2026, 2026 07 20 neuromorphic market sockets and algorithm vs hardware): Does any SPIKING chip find a volume socket beyond research/niche sensing? NO. The always-on edge volume sockets are real but won by conventional low-power digital (Ambiq 280M+, Syntiant 20M+) and sparse-digital (femtoAI 100k+), not spikes. Only defensible spiking wedge = defense RF signal classification, still POC (BrainChip FY25 revenue $1.89M). Base rate confirmed poor.'
- 'ANSWERED (20 Jul 2026): brain-inspired ALGORITHM (Camp A, >$2B in 2026 — Flourish, AMI/LeCun, Liquid, Sakana) runs on GPUs and does NOT need neuromorphic silicon; spiking HARDWARE (Camp B) is a separate ~$0.5B chip market. Never underwrite a hardware bet on the brain-inspired tailwind — it is a software story.'
- Do analog / memcapacitor devices become the substrate for neuromorphic, or stay separate?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 71
last_reorg_date: '2026-05-14'
descendants:
- spiking-neural-networks
scorecard:
  viability: 3
  drivers: null
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Later (5-10yr)
  verdict: Overrated
scorecard_status: draft
sources_7d: 2
sources_30d: 8
recent_mentions:
- slug: 2026-07-31-inference-silicon-roster-sprint
  title: 'Inference-silicon roster verification sprint: 10 companies for the competitive-analysis capital map'
  date: '2026-07-31'
  kind: web
- slug: 2026-06-17-femtoai-spu-ces2026
  title: femtoAI to Highlight its Sparse Processing Unit Edge AI Accelerator at CES 2026
  date: '2026-06-17'
  kind: web
- slug: 2026-04-01-low-power-edge-compute-neuromorphic-computing-chip-patents
  title: Neuromorphic Computing Chip Patents Surge 401% in 2025
  date: '2026-04-01'
  kind: web
- slug: 2026-01-22-ai-chips-computeram-and-the-future
  title: 'AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara'
  date: '2026-01-22'
  kind: substack
- slug: 2025-09-23-the-compute-gradient
  title: The Compute Gradient
  date: '2025-09-23'
  kind: substack
- slug: 2023-07-23-analog-computing-the-once-and-future
  title: '🔮 E09: Analog Computing: The Once and Future King'
  date: '2023-07-23'
  kind: substack
- slug: 2023-06-30-e06-the-model-t-moment-for-bits-llms
  title: '🔮 E06: Large Language Models and the Assembly Line'
  date: '2023-06-30'
  kind: substack
- slug: 2023-06-23-e05-the-future-of-edge-ai-brain-inspired
  title: '🔮 E05: Neuromorphic Computing & The Future of Edge AI'
  date: '2023-06-23'
  kind: substack
neighbors: []
---
**Neuromorphic computing builds hardware that computes the way brains are thought to: with spiking, event-driven, analog dynamics and weights stored where the arithmetic happens, and the demonstrated systems today range from a measured 100 W wafer-scale digital spiking machine to hundreds of small emerging-device arrays whose headline efficiency figures are extrapolations rather than measurements.**

## Summary

Conventional processors separate memory from arithmetic, so running a neural network means shuttling weights across a bus. Neuromorphic computing attacks that from two directions. The first is architectural and digital: build many small cores, each with local SRAM, that exchange sparse asynchronous events (spikes) rather than dense tensors. The second is physical: replace the multiply-accumulate with a device whose physics does the multiplication, typically a crossbar array in which each cell's conductance, capacitance, refractive index or magnetic state encodes a weight, so a whole matrix-vector product happens as one analog settling event.

The parameters that decide the field are unglamorous. Device-to-device variability determines whether a crossbar can be programmed in parallel at all: engineering the Ge:Te ratio in a CBRAM electrolyte suppressed stochastic resistance variation by roughly three orders of magnitude versus GeSe and only then allowed a 16x16 array to run a 4x4 Hopfield network with fully parallel Hebbian writes. Array size is the second parameter: nearly all quoted efficiency numbers come from arrays of tens to hundreds of devices, or from SPICE, not from megabit arrays. Third, on-chip memory itself has become the bottleneck the architecture was supposed to remove: SRAM and STT-MRAM now dominate area and energy in digital neuromorphic processors, producing what one critical review calls a new memory wall. Fourth, mundane integration questions such as IO pad rings and bonding strategy materially affect the power and yield of low-power neuromorphic chips.

## Viability (3/5)

The strongest evidence for viability is DarwinWafer: 64 Darwin3 chiplets integrated on a 300 mm silicon interposer, 0.15 billion neurons and 6.4 billion synapses per wafer, measured at ~100 W and 0.8 V/333 MHz with 4.9 pJ per synaptic operation, 64 TSOPS peak and 0.64 TSOPS/W, plus measured 10 mV supply droop and a 34 to 36 °C thermal profile under load. That is an engineered system with measured electricals, not a concept. FerroNDS is a second credible point: a 128-neuron analog compute-in-memory system doing short-time Fourier transforms and 500 ms-horizon forecasting at sub-watt power, 1.64 µJ per neuron per inference at 200 Hz and 3.18 ms per-layer latency.

Against that, the analog crossbar story is much earlier than its numbers imply. The founding memcapacitor work measured 156 devices at 50x50 µm cell size classifying 5x5-pixel letters, with 457 nJ per MAC actually measured; every TOPS/W figure in the paper is SPICE at a simulated 90 nm device, and the femtojoule claims are explicit seven-order-of-magnitude extrapolations from the measured device **Demasius 2021 Memcapacitor Nature Electronics**. Elsewhere the switching physics is still under investigation by molecular dynamics and kinetic Monte Carlo rather than settled, and the largest fabricated emerging-memory array in these sources is 16x16. Digital neuromorphic: works. Analog neuromorphic: works at toy scale, with the scaling argument still on paper.

**TLDR: Digital spiking hardware demonstrably works at wafer scale; the analog device path is real but still measured in hundreds of cells.**

## Drivers (unscored)

On supply the record is clear and can be described: within roughly two months of arXiv output there are ferroelectric, memristive, magnetic, photonic, mechanical, superconducting and moire-graphene routes to synaptic and neuronal function, several on CMOS-compatible platforms including 220 nm silicon photonics and SkyWater 130 nm CMOS for prototyping, plus a demonstrated chiplet-interposer flow for wafer-scale assembly. That is genuine supply-side momentum in materials and integration capability.

On demand the sources give nothing measurable. The stated pull is generic: energy-efficient processing for artificial intelligence and edge computing, asserted in paper introductions rather than evidenced by customers, revenue, procurement or deployment volumes. There is no funding, market-size, foundry-commitment or design-win data anywhere in this set. Scoring the driver dimension on assertions in abstracts would be inventing a judgement, so the score is null.

**TLDR: The sources show a broad supply-side research pipeline but contain no demand, market or deployment evidence, so no score is earned.**

## Novelty (3/5)

Where a like-for-like comparison exists, the gain is meaningful but bounded. FerroNDS reports 25 to 40 times area reduction versus SRAM-based digital implementations of the same neural dynamical system, with sub-watt real-time operation and 63.87 µs per-layer latency at 10 kHz. DarwinWafer's contribution is to replace PCB-level chip-to-chip links, which the authors argue cost orders of magnitude in bandwidth, latency and energy, with a wafer fabric, yielding a measured 4.9 pJ/SOP. The CBRAM electrolyte work delivers a clean three-orders-of-magnitude reduction in resistance variability versus GeSe devices, which is a variability advance rather than a performance one.

The headline claims are weaker than they look. The memcapacitor efficiency figures decompose into two hidden multipliers: 95% charge recovery is worth about 17.4 times (3,452.6 versus 198.5 TOPS/W worst case; 29,600 versus 1,702 TOPS/W for an MNIST perceptron), and the recovery figure itself is imported from adiabatic-circuit literature rather than measured on the device; the whole efficiency ladder rests on a seven-order-of-magnitude extrapolation from a 50x50 µm cell to a simulated 90 nm one **Demasius 2021 Memcapacitor Nature Electronics**. Similarly, the MRAM/STNO CNN is evaluated in simulation and the 5-bit (32-level) Sb2Se3 mode converter precision comes from FDTD. Novelty of mechanism is high; demonstrated novelty of end-to-end efficiency is a factor of tens, not thousands.

**TLDR: Real, quantified advantages over SRAM-based digital baselines at small scale; the large multipliers over mainstream accelerators remain simulated.**

## Diffusion (2/5)

The most serious diffusion barrier in these sources is internal to the architecture: distributed on-chip memory has itself become a dominant consumer of area and energy in digital neuromorphic processors, and the critical review concludes that without re-thinking memory organisation such processors may struggle to compete in edge and embedded applications, precisely the market usually claimed for them. Beneath that sits device variability, which prevents reliable parallel programming of memristor crossbars until it is engineered away composition by composition, and switching mechanisms that are still being reconstructed from atomistic simulation.

Integration friction is documented rather than assumed: IO pad and pad-ring design, bonding strategy and early I/O planning affect power, yield and redesign risk in low-power neuromorphic chips, and DarwinWafer needed a bespoke interposer-bump planner plus warpage-tolerant, pogo-pin demountable assembly to work at all. Training is a further barrier that only some platforms address: the transmission-line metamaterial work derives a physical in-situ backpropagation via the adjoint method precisely because gradient computation does not come free in analog hardware. The sources contain no evidence on software stacks, compilers or user adoption, which is itself a reason to keep this score low.

**TLDR: Variability, unresolved switching physics, and an on-chip memory bottleneck that reproduces the problem neuromorphic was meant to solve.**

## Impact (3/5)

Two impact cases are supported. First, temporal signal processing at the edge: neural dynamical systems map badly onto hardware built for dense matrix operations, and an analog implementation with native continuous-time integrators and oscillators forecasts periodic, quasi-periodic and chaotic signals in real time at sub-watt power with tens-of-microseconds layer latency. Excitable optical spiking neurons with calibrated all-or-none response, threshold control, temporal summation and refractory period point the same way for low-latency photonic edge processing at 1550 nm. Second, large-scale brain simulation: a single wafer carrying 0.15 billion neurons and 6.4 billion synapses at ~100 W is used for whole-brain simulations, two zebrafish brains per chiplet.

What the sources do not establish is displacement of GPUs for mainstream training or transformer inference. No source here benchmarks a neuromorphic system against a commercial AI accelerator on a commercially relevant workload; the comparisons are against SRAM-based digital equivalents of the same specialised task, or against PCB-level interconnect. Combined with the memory-wall critique of edge competitiveness, the defensible view is high value inside specific dynamical and event-driven niches and unproven value outside them.

**TLDR: Clear value in continuous-time, low-power sensing and simulation niches; the sources do not support a claim on mainstream AI compute.**

## Timing Later (5-10yr)

The digital branch is already deployable in the narrow sense: DarwinWafer is a measured, assembled, thermally characterised system today, and the SkyWater 130 nm prototyping route lowers the barrier for new SNN silicon. The gating question is not whether such chips exist but whether they beat conventional edge silicon once on-chip memory area and energy are counted honestly, and the current critical answer is that they may not.

The analog branch is on a longer clock. The distance between measured evidence and claimed performance is a full scaling programme: from 156 devices at 50 µm pitch and 457 nJ per MAC to a simulated 90 nm device carrying the femtojoule claims **Demasius 2021 Memcapacitor Nature Electronics**, from a 16x16 CBRAM crossbar to production array sizes, and from 128 analog neurons to systems that matter commercially. Each step requires variability control, endurance and write-circuit overheads that are not yet demonstrated at scale, which puts credible competitiveness in the five to ten year band rather than sooner.

**TLDR: Digital spiking systems are usable now for research and niche edge work; analog in-memory neuromorphic needs a scaling generation before it competes.**

## Overrated or underrated? Overrated

The engineering is real and some of it is impressive, but the field's public arithmetic is not. The single most useful document in this set is the audit of the memcapacitor paper: the measured quantity is 457 nJ per MAC on a 50x50 µm cell, and the widely quoted efficiency is reached by a seven-order-of-magnitude extrapolation to a simulated 90 nm device compounded by a 17.4 times charge-recovery assumption borrowed from other literature **Demasius 2021 Memcapacitor Nature Electronics**. That pattern, simulated architecture on top of a small measured device, recurs across the MRAM/STNO CNN and the photonic tensor core precision estimates. Anyone underwriting a neuromorphic thesis on TOPS/W numbers should assume, until shown otherwise, that they are projections.

The second reason for the call is that the core premise is under attack from inside the field: the memory wall reappears as on-chip SRAM and STT-MRAM dominate area and energy, to the point where digital neuromorphic processors may not win in edge and embedded. What is underrated within the overrated whole is the narrow case: continuous-time dynamical workloads where the analog primitive matches the maths and the measured advantage over SRAM digital is 25 to 40 times in area at sub-watt power, and wafer-scale spiking machines for brain-scale simulation. Judged as a replacement for mainstream AI compute, overrated; judged as specialised instrumentation, sound.

## Prediction

By 31 December 2029, no peer-reviewed analog neuromorphic crossbar of more than 10,000 fabricated devices will report a measured (not SPICE-extrapolated) energy per MAC within two orders of magnitude of the femtojoule-class figures projected in **Demasius 2021 Memcapacitor Nature Electronics**.

## Evidence base

- DarwinWafer integrates 64 Darwin3 chiplets on a 300 mm interposer for 0.15 B neurons and 6.4 B synapses per wafer, measured at ~100 W, 4.9 pJ/SOP and 0.64 TSOPS/W, with 10 mV supply droop and a 34 to 36 °C thermal profile (arXiv posted 30 Aug 2025).
- The founding memcapacitor paper (Nature Electronics, 11 Oct 2021) measured 156 devices at 50x50 µm cell size at 457 nJ per MAC; all TOPS/W figures are SPICE on a simulated 90 nm device and the femtojoule claims are seven-order-of-magnitude extrapolations, with charge recovery alone worth about 17.4 times (29,600 versus 1,702 TOPS/W on MNIST) **Demasius 2021 Memcapacitor Nature Electronics**.
- A critical architecture review (9 Apr 2026) finds on-chip SRAM and STT-MRAM have become significant consumers of area and energy in digital neuromorphic processors, creating a new memory wall and threatening competitiveness in edge and embedded use.
- FerroNDS (16 Jun 2026) runs a 128-neuron analog neural dynamical system on multi-bit ferrodiode compute-in-memory at 1.64 µJ per neuron per inference (200 Hz) and 0.29 µJ (10 kHz), with 25 to 40 times area reduction over SRAM-based digital and 63.87 µs per-layer latency at 10 kHz.
- Ge:Te composition engineering (4 Jun 2026) suppressed stochastic resistance variation by roughly three orders of magnitude versus GeSe CBRAM, enabling a selector-less 16x16 crossbar running a 4x4 Hopfield network with fully parallel Hebbian programming.
- A GaP electro-optomechanical spiking neuron on silicon photonics (17 Jan 2026) shows calibrated all-or-none optical spikes at 1550 nm using a 3 GHz mechanical mode, with demonstrated threshold control, temporal summation and refractory period.
- Atomistic work on filament formation in ECM and Ta/HfO2/Pt memristors (5 May and 29 May 2026) states that the mechanisms governing filament morphology and metal cation migration remain unclear or poorly understood.

## Open questions

- Does any emerging-device crossbar reach 10^4 to 10^6 cells with the device-to-device variability of the Ge3.5Te1 CBRAM result preserved, or does the variability advantage disappear with array size?
- Can the 95% charge-recovery assumption underpinning the memcapacitor efficiency figures be measured on a real scaled device, given it alone accounts for a 17.4 times multiplier **Demasius 2021 Memcapacitor Nature Electronics**?
- Is there a memory organisation that removes the new on-chip memory wall in digital neuromorphic processors, and what is the measured area and energy split after it is applied?
- Does any neuromorphic system, digital or analog, beat a commercial accelerator on a workload a buyer already runs, rather than on a task chosen to suit the hardware?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
