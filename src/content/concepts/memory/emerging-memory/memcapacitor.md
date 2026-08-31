---
type: concept
slug: memcapacitor
canonical_name: Memcapacitor
aliases:
- memcapacitive device
- charge-domain memory
- capacitive in-memory compute
- CapRAM
kind: technology
parent_concepts:
- memory
- emerging-memory
related_concepts:
- memristor
- rram-reram
- pcm-phase-change-memory
- mram
- feram
- sram
- charge-domain-compute
- 3d-monolithic-integration
sources:
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2026-06-16-cim-landscape-2026]]'
- '[[2026-07-02-semianalysis-ectc2026-advanced-packaging]]'
frontier:
- Has any memcapacitor array been fabricated below the 50 x 50 µm cell size of the 2021 device, and what is the measured energy per MAC at that size rather than the extrapolated figure?
- Does the 95% charge-recovery assumption, worth 17.4x in the founding paper's efficiency grid, survive measurement in a real adiabatic driver circuit attached to a memcapacitor crossbar?
- Can a ferroelectric HZO memcapacitor hold multi-level analogue state with the retention, endurance and cycle-to-cycle linearity that FCDC's simulations assume, and for how long relative to a serving session?
- If the field standardises on digital readout with reduced effective precision, does the memcapacitor's charge-domain advantage survive the conversion overhead, or does non-volatility alone justify it against switched-capacitor SRAM?
- Does SEMRON's 3D monolithic CapRAM growth scale at production yield by 2027? (Most binding technical risk for the architecture class.)
- ADC overhead — does the analog→digital conversion cost at column ends cap practical performance, as it has constrained RRAM- and PCM-based IMC?
- Retention and endurance at standard CMOS interface — does charge-trapping suffer the same drift problems as floating-gate flash, or stay clean because the read mode is non-destructive?
- Process portability — does the device work at a single foundry process node (TSMC N16/N12, GF 22FDX) or does it need bespoke fab integration that locks in single-sourcing?
- Temperature calibration — does CapRAM compute accuracy drift across operating temperature in ways that need on-chip compensation circuitry, eating into the energy advantage?
- Competitive cliff with FeFET — does the FeFET roadmap (HfO₂-based, GlobalFoundries 22FDX-FeFET, Sony) close the manufacturing-readiness gap before memcapacitor reaches HVM?
- Application boundary — does the architecture stay edge-only (constrained by ADC overhead at large arrays), or does it scale to LLM decode workloads at hyperscaler volume?
last_updated: '2026-08-31'
tags:
- concept
- technology
- analog-computing
- in-memory-computing
- semron
mention_count: 31
last_reorg_date: '2026-05-14'
descendants:
- capram
scorecard:
  viability: 2
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Later (5-10yr)
  verdict: Too early to say
scorecard_status: draft
sources_7d: 0
sources_30d: 4
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
- slug: memristor
  name: Memristor
  path: /memory/emerging-memory/memristor/
  macro: memory
- slug: rram-reram
  name: RRAM / ReRAM
  path: /memory/emerging-memory/rram-reram/
  macro: memory
- slug: pcm-phase-change-memory
  name: Phase-Change Memory (PCM)
  path: /memory/emerging-memory/pcm-phase-change-memory/
  macro: memory
- slug: mram
  name: MRAM (STT/SOT-MRAM)
  path: /memory/mainstream-memory/mram/
  macro: memory
- slug: feram
  name: FeRAM (Ferroelectric)
  path: /memory/mainstream-memory/feram/
  macro: memory
- slug: sram
  name: SRAM
  path: /memory/mainstream-memory/sram/
  macro: memory
- slug: charge-domain-compute
  name: Charge-Domain Compute
  path: /compute/non-conventional/charge-domain-compute/
  macro: compute
- slug: 3d-monolithic-integration
  name: 3D Monolithic Integration
  path: /compute/compute-architecture/3d-monolithic-integration/
  macro: compute
---
**A memcapacitor is a capacitor whose capacitance is programmable and retained, so a neural-network weight can be stored and multiplied in the charge domain with almost no resistive current, but the only measured device is a 156-cell crossbar with 50 x 50 µm cells and 457 nJ per MAC, and every headline efficiency figure is extrapolation **Demasius 2021 Memcapacitor Nature Electronics**.**

## Summary

**What it is.** A memcapacitor is the capacitive counterpart of the memristor: a two-terminal or gated element whose *capacitance* holds a programmable, non-volatile analogue value. In a crossbar, applying an input voltage to a row causes charge to be redistributed in proportion to the stored capacitance, so the column charge is a multiply-accumulate over the stored weights. The distinction from resistive analogue compute-in-memory (RRAM, PCM) is that ideally no steady current flows through the storage element. The energy is reactive rather than dissipative, which opens the door to adiabatic circuits that push charge back into the supply instead of dumping it to ground.

**The parameters that decide it.** First, capacitance per unit area: the compute signal is charge, so the entire proposition depends on getting useful capacitance out of a cell three orders of magnitude smaller laterally than the one that has been measured. For scale, manufactured MIM capacitors embedded in Intel's EMIB-T bridge sit around 500 nF/mm², with a roadmap target above 2,500 nF/mm² for decoupling structures <sup class="ref"><a href="https://newsletter.semianalysis.com/p/ectc2026" title="ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, " rel="noopener">ref</a></sup>. Second, charge recovery: in the founding paper the 95% recovery assumption, imported from the adiabatic-circuits literature rather than measured, is worth about 17.4x on its own (3,452.6 versus 198.5 TOPS/W in the worst case; 29,600 versus 1,702 TOPS/W on a one-layer MNIST perceptron) **Demasius 2021 Memcapacitor Nature Electronics**. Third, analogue precision under noise: FCDC's claim is that all-layer noise substitution costs +2.6% WikiText-2 perplexity on Qwen3-32B and +2.9% on Mistral-7B-v0.3, with a narrower KV-coprocessor serving mode under 0.5%. Fourth, and least discussed, whether the readout can stay analogue at all: the 2026 direction of travel in compute-in-memory is analogue compute with digital readout to manage noise and variability, which is a headwind for any pure multi-level analogue device <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>.

## Viability (2/5)

The physics is demonstrated and the device works as a trainable array: 156 memcapacitors, 50 x 50 µm cells, letter classification, 457 nJ per MAC measured **Demasius 2021 Memcapacitor Nature Electronics**. That is a working proof of principle and nothing more. The gap between what was measured and what is claimed is a seven-order-of-magnitude extrapolation to a simulated 90 nm device, plus a 17.4x multiplier from an unmeasured 95% charge-recovery assumption **Demasius 2021 Memcapacitor Nature Electronics**. Nothing in the sources shows a fabricated memcapacitor array at a scaled node, or a measured charge-recovery circuit operating with a memcapacitor crossbar.

The 2026 ferroelectric line does not close that gap. FCDC is explicitly simulation-based with no device fabricated, and its credibility rests on borrowed wafer-scale 10 nm HZO measurements rather than on a compute cell that exists. What has been established is that the accuracy question may be tractable (12 pretrained LLMs, downstream tasks within 5% of digital, a 128k-context replication). What has not been established is that a manufacturable cell delivers the assumed device behaviour at scale. Score 2, not 1, because the founding measurement is real and peer-reviewed; not 3, because no fabricated array has yet been shown at a node where the economics would work.

**TLDR: One measured crossbar at 50 µm cells; all attractive numbers are extrapolated or simulated.**

## Drivers (3/5)

**Demand.** The pull is the best-evidenced part of the story. Peak hardware compute has grown about 60,000x over twenty years while DRAM bandwidth grew about 100x and interconnect about 30x; the underlying rates are roughly 3.0x per two years for server FLOPS against 1.6x for DRAM bandwidth and 1.4x for interconnect, so an ever-larger share of workloads becomes memory-bound **2024 Gholami Ai And Memory Wall**. The energy asymmetry points the same way: arithmetic is sub-picojoule while an off-chip DRAM fetch is roughly 1.3 to 2.6 nJ **2024 Gholami Ai And Memory Wall**. LLM decode is the bandwidth-bound phase, and the KV cache that must stay resident and be re-read across a long session is precisely the target FCDC picks. Edge inference adds a second, power-limited demand channel.

**Supply.** Weak by comparison. There is one research group's fabricated device and one simulation study on a different material system. The nearest thing to a supply-side tailwind is that ferroelectric HZO has wafer-scale measurement data at 10 nm and that capacitor structures are routinely manufactured at high density in advanced packaging <sup class="ref"><a href="https://newsletter.semianalysis.com/p/ectc2026" title="ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, " rel="noopener">ref</a></sup>. Against that, the incumbent responses to the same demand signal are already further along: SK Hynix's AiM/AiMX processing-in-memory splits decode onto memory-side silicon and was demoed through CES 2026, and TetraMem has taped out a 22 nm multi-level analogue RRAM SoC <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>. Others are betting that ordinary memory used well is enough, as with Positron's choice of LPDDR5x over HBM at 2.76 TB/s realisable bandwidth and over 90% memory-bandwidth utilisation <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>.

**TLDR: Demand pull is well quantified and strong; supply-side readiness is a single research device.**

## Novelty (3/5)

The claim to novelty is structural: state stored as capacitance rather than conductance means the multiply happens without an Ohmic current path through the weight, and the energy is reactive and in principle recoverable. That is a real distinction from RRAM and PCM analogue compute-in-memory. The relevant comparison, though, is not GPUs. It is charge-domain compute-in-memory that already exists in switched-capacitor SRAM form: EnCharge claims above 150 TOPS/W against roughly 24 TOPS/W for an equivalent Nvidia chip, with an EN100 board at about 200 AI TOPS in roughly 8 W <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>. Strip the charge-recovery assumption from the memcapacitor projections and the simulated worst case is 198.5 TOPS/W **Demasius 2021 Memcapacitor Nature Electronics**, the same order as a vendor claim from a product that ships boards. The 3,452.6 and 29,600 TOPS/W figures only appear once you grant 95% charge recovery **Demasius 2021 Memcapacitor Nature Electronics**.

Where the memcapacitor is plausibly better *than* charge-domain SRAM is non-volatility and therefore density and standby power: FCDC's whole framing is a non-volatile analogue store that keeps the KV cache resident without refresh or re-read. That is the differentiator worth testing, and it is the one for which no measured device exists. The sources support a score of 3: a distinct and defensible mechanism, with a quantified advantage that shrinks sharply once the borrowed assumptions are removed.

**TLDR: Genuinely different from resistive CIM, but the honest efficiency edge over charge-domain SRAM is unproven.**

## Diffusion (2/5)

Three barriers stand out. First, scaling: the measured cell is 50 x 50 µm and the projections assume 90 nm and 45 nm devices **Demasius 2021 Memcapacitor Nature Electronics**. Nothing in the sources bridges that. Second, the direction of the surrounding field. The 2026 shift in compute-in-memory is towards analogue compute with digital readout and lower effective precision to get yield, described explicitly as a headwind for any pure multi-level analogue device including the memcapacitor <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>. Third, the baseline is moving. Delivered GPU cost per token is falling at a defensible floor of about 2.5 to 3x per year, with software alone lifting H100 MLPerf results up to 1.5x in one year and Epoch putting fixed-capability price decline at a median 50x per year. A device class whose measured hardware is a 2021 letter classifier has to hit a target that recedes at that rate.

There is also a cheaper competitor for the same job. Positron's Asimov claims 864 GB to 2.3 TB per chip on commodity LPDDR5x with over 90% memory-bandwidth utilisation versus under 30% for GPUs, targeting production in early 2027 <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>. If the memory wall can be substantially addressed by using ordinary DRAM better, the adoption case for an exotic analogue non-volatile capacitor narrows to the cases where standby energy or density genuinely dominate, most plausibly edge inference. If a 3D-stacked variant is ever proposed to get density, Walker's 3D NAND analysis is the warning: die cost per bit does not fall monotonically with layer count because deep-etch taper widens the top-of-stack cell pitch linearly in layer count, so there is a cost minimum beyond which more layers cost more **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**.

**TLDR: Three orders of lateral scaling unbuilt, an industry moving to digital readout, and a fast-falling GPU cost baseline.**

## Impact (4/5)

The prize is large and clearly identified. Data movement, not arithmetic, dominates the energy bill, with an off-chip DRAM fetch at roughly 1.3 to 2.6 nJ against sub-picojoule arithmetic, and the gap between compute growth and memory bandwidth growth is 60,000x versus 100x over twenty years **2024 Gholami Ai And Memory Wall**. A non-volatile charge-domain store that holds the KV cache and performs the attention matmuls in place removes both the re-read and the refresh from the hottest phase of LLM serving. FCDC's simulated accuracy envelope suggests the precision cost may be tolerable: +2.6% perplexity on Qwen3-32B under full substitution, under 0.5% in the narrower serving mode, five downstream tasks within 5% of digital across 12 models up to a 141B mixture-of-experts stress test.

Even the conservative simulated figure, 198.5 TOPS/W without charge recovery, sits roughly an order of magnitude above the ~24 TOPS/W attributed to an equivalent Nvidia part **Demasius 2021 Memcapacitor Nature Electronics** <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>. The reason this is 4 and not 5 is that the value is conditional on a device that has not been fabricated at scale, and the highest headline numbers depend on an assumption worth 17.4x that no one has demonstrated in a memcapacitor array **Demasius 2021 Memcapacitor Nature Electronics**.

**TLDR: If a scaled cell works, it attacks the decode bottleneck at both the energy and the residency level.**

## Timing Later (5-10yr)

The measured state of the art is a 2021 crossbar at 50 µm cell size **Demasius 2021 Memcapacitor Nature Electronics**, and the most recent work in the sources, from June 2026, still has no fabricated device. Five years of published work has moved the ball from a measured micrometre-scale device to a more rigorous simulation on a different material stack. For comparison, the nearest analogue-memory competitor with silicon, TetraMem's 22 nm multi-level RRAM SoC, only had evaluation kits targeted for the second half of 2026 <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>.

On that trajectory, datacentre-relevant memcapacitor deployment is a five-to-ten-year question at the earliest, and edge deployment depends on commercialisation activity the sources do not date. The two milestones to watch inside two years are a peer-reviewed fabricated memcapacitor array at a scaled node with measured rather than extrapolated energy, and a measured charge-recovery circuit operating with such an array. Until one of those lands, the timing is set by device engineering, not by market pull.

**TLDR: The near-term milestone is a fabricated scaled array, not a product; nothing in the sources dates one.**

## Overrated or underrated? Too early to say

The mechanism is credible and the target is the right one: the memory wall is quantified, decode is bandwidth-bound, and a non-volatile charge-domain store attacks exactly the re-read and residency problem **2024 Gholami Ai And Memory Wall**. But the evidence base does not yet support a rating of the technology, only of the claims made for it, and those claims are overstated. The circulated TOPS/W figures combine a seven-order-of-magnitude extrapolation from a 50 µm device with a 95% charge-recovery assumption worth 17.4x and imported from another literature **Demasius 2021 Memcapacitor Nature Electronics**. Once both are removed, what remains is 198.5 TOPS/W in simulation, comparable to a vendor claim from charge-domain SRAM hardware that already ships boards <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>.

The field is also drifting away from the memcapacitor's strongest assumption. Pure multi-level analogue readout is being displaced by analogue-compute-with-digital-readout hybrids for yield and noise reasons, which the landscape review names as a direct headwind for this device class <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>, while the cost baseline it must beat falls at roughly 2.5 to 3x per year. Judgement should be suspended until a fabricated array at a scaled node reports measured energy. Anyone treating the four- or five-figure TOPS/W numbers as a specification rather than a simulation is being sold something.

## Prediction

By 31 December 2028, no peer-reviewed paper will report a fabricated memcapacitor array with cell size below 1 µm and measured (not extrapolated or SPICE-simulated) energy efficiency above 1,000 TOPS/W.

## Evidence base

- 11 Oct 2021: the founding memcapacitor paper measured a 156-device crossbar at 50 x 50 µm cell size (gate lengths ~60 µm) classifying 5 x 5 pixel letters, at 457 nJ per MAC; all femtojoule and TOPS/W figures are seven-order-of-magnitude extrapolations to a simulated 90 nm device **Demasius 2021 Memcapacitor Nature Electronics**.
- 11 Oct 2021: the same paper's efficiency grid shows the 95% charge-recovery assumption is worth ~17.4x on its own (3,452.6 vs 198.5 TOPS/W worst case; 29,600 vs 1,702 TOPS/W on MNIST), with the 95% figure imported from the adiabatic-circuits literature **Demasius 2021 Memcapacitor Nature Electronics**.
- 30 Jun 2026: FCDC, an HZO ferroelectric memcapacitor for non-volatile charge-domain attention, reports +2.6% WikiText-2 perplexity on Qwen3-32B and under 0.5% accuracy cost in KV-coprocessor serving mode across 12 pretrained LLMs, but is simulation-based throughout with no device fabricated.
- 21 Mar 2024: peak hardware compute grew ~60,000x over twenty years against ~100x for DRAM bandwidth and ~30x for interconnect, with an off-chip DRAM fetch at ~1.3-2.6 nJ versus sub-picojoule arithmetic **2024 Gholami Ai And Memory Wall**.
- 16 Jun 2026: the 2026 compute-in-memory shift is towards analogue compute with digital readout and lower effective precision for yield, described as a headwind for pure multi-level analogue devices including the memcapacitor; EnCharge's switched-capacitor charge-domain SRAM claims >150 TOPS/W versus ~24 TOPS/W for an equivalent Nvidia chip <sup class="ref"><a href="https://spectrum.ieee.org/analog-ai-chip-architecture" title="Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM" rel="noopener">ref</a></sup>.
- 10 Jul 2026: the defensible floor for decline in GPU delivered cost per token is ~2.5-3x per year, with Epoch putting fixed-capability price decline at a median 50x per year, setting the moving target any new memory device must beat.

## Open questions

- Has any memcapacitor array been fabricated below the 50 x 50 µm cell size of the 2021 device, and what is the measured energy per MAC at that size rather than the extrapolated figure?
- Does the 95% charge-recovery assumption, worth 17.4x in the founding paper's efficiency grid, survive measurement in a real adiabatic driver circuit attached to a memcapacitor crossbar?
- Can a ferroelectric HZO memcapacitor hold multi-level analogue state with the retention, endurance and cycle-to-cycle linearity that FCDC's simulations assume, and for how long relative to a serving session?
- If the field standardises on digital readout with reduced effective precision, does the memcapacitor's charge-domain advantage survive the conversion overhead, or does non-volatility alone justify it against switched-capacitor SRAM?

---
*Assessment drafted 2026-08-31 from up to 13 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
