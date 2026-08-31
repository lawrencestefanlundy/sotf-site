---
type: concept
slug: compute-logic
context_concept: true
canonical_name: Compute & Logic
aliases:
- Compute & Logic
- compute-and-logic
kind: theme
parent_concepts:
- compute-architecture
- compute
related_concepts:
- photonic-compute
- neuromorphic-computing
- in-memory-computing
- risc-v
- chiplets
sources: []
frontier:
- Does the 8.8x PIM advantage for qLDPC decoding survive the move from uPIMulator simulation and ideal syndrome measurements to real DPU hardware with measurement noise, and does it hold against a GPU rather than a 16-logical-CPU baseline?
- Is the two-week autonomous specification-to-RTL loop reproducible by a second team on a different accelerator target, and does the resulting silicon meet its performance model in fabricated form?
- Which specific hardware implementation challenges limit RVV 1.0 platforms against NVIDIA Grace, and are they microarchitectural, memory-system or compiler problems, since only the last is quickly fixable?
- Do the analog frequency-domain and rate-based neuromorphic approaches have any measured silicon results, and at what precision, given that the neuromorphic gains are stated to be bounded by arithmetic precision?
- Which non-von-Neumann paradigm (analog in-memory, photonic, neuromorphic) reaches production AI inference scale first?
last_updated: '2026-08-31'
tags:
- concept
- category
- stub
mention_count: 74
scorecard:
  viability: 4
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 5
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: photonic-compute
  name: Photonic Compute
  path: /photonic-systems/photonic-compute/photonic-compute/
  macro: photonic-systems
- slug: neuromorphic-computing
  name: Neuromorphic Computing
  path: /compute/non-conventional/neuromorphic-computing/
  macro: compute
- slug: in-memory-computing
  name: In-Memory Computing
  path: /memory/emerging-memory/in-memory-computing/
  macro: memory
- slug: risc-v
  name: RISC-V
  path: /compute/conventional-logic/risc-v/
  macro: compute
- slug: chiplets
  name: Chiplets
  path: /compute/compute-architecture/chiplets/
  macro: compute
---
**Compute & Logic covers the physical substrates and architectures that execute computation, from CPUs and GPUs to domain-specific ASICs, processing-in-memory, neuromorphic and analog circuits, and the 2026 evidence says the binding constraint is no longer arithmetic but memory bandwidth and data movement.**

## Summary

Compute & Logic sits at the root of the compute-architecture taxonomy: it is the set of design choices about how arithmetic and control are physically implemented and how operands reach them. In practice this means five families that the current literature treats as competing answers to the same question. General-purpose GPUs remain the flexible default and the workhorse of training. Domain-specific ASICs such as TPUs, Trainium, Groq and Cerebras win at scale on stable, high-volume workloads. Reconfigurable FPGAs occupy a middle ground. Processing-in-memory and near-memory architectures move computation to where the data already sits. Neuromorphic and photonic approaches remain emerging.

The organising insight of the field in 2026 is the memory wall. Applying roofline analysis to the transformer, the decisive constraint on LLM acceleration is not FLOPs: the autoregressive decode phase is bandwidth-bound, the key-value cache can rival the model weights in size, and energy is dominated by data movement rather than by the multiply-accumulate itself. That reframing explains most of the current architectural activity. Near-memory work is not a curiosity but the most promising near-term response, and the same conclusion appears outside AI: mapping normalised min-sum belief propagation decoding of a **144,12,12** bivariate bicycle qLDPC code onto a DPU-based PIM architecture yields a projected 1.071 x 10^7 decodes/s across 2,560 DPUs versus 1.22 x 10^6 decodes/s on a 16-logical-CPU baseline, an 8.8x improvement, precisely because BP over sparse Tanner graphs is a data-movement problem.

The second organising force is the mismatch of timescales. Architectural definition precedes volume silicon by years while workloads shift in months, so decisions are committed under deep uncertainty and paid for twice: once in generality added as a hedge, once when new workloads map badly onto frozen silicon. With Moore's Law stagnating, specialisation is the main remaining source of performance-per-watt, which requires a design cycle running at workload cadence. This is why design automation now belongs inside the compute-architecture story rather than beside it.

The parameters that decide outcomes here are therefore: achievable memory bandwidth and locality per watt; how much of a workload is stable enough to justify frozen silicon; the maturity of the software stack and compiler for any non-GPU target; and the speed at which a design can be specified, verified and taped out. Open-ISA and exotic-substrate efforts live or die on the third of those, not the first.

## Viability (4/5)

The centre of the field is unambiguously working. Commercial parts were presented at Hot Chips in August 2026 including OpenAI's Jalapeño, Cerebras CS-5, Groq 3 LPX and Apple M6 <sup class="ref"><a href="https://www.latent.space/p/ainews-hot-chips-openais-jalapeno" title="[AINews] Hot Chips: OpenAI’s Jalapeño, Cerebras CS-5, Groq 3 LPX, Apple M6" rel="noopener">ref</a></sup>, and the accelerator survey compares GPUs, TPUs, Trainium, Groq and Cerebras as deployed platforms rather than proposals. Open-ISA compute is at an earlier but real stage: RVV 1.0 has been ratified and adopted by commercially available silicon including SiFive X280 in Tenstorrent Blackhole, SpacemiT X60 and X100/A100, and T-Head C920v2, and delivers significant gains over scalar execution on BLAS, FFTW, HPL, HPCG and STREAM, while hardware-specific implementation challenges remain and comparison against NVIDIA Grace exposes hurdles to becoming an HPC mainstay.

The periphery is thinner. Analog vector-matrix multiplication in the frequency domain via coupled oscillators and MEMS/NEMS resonators is presented as a small-signal circuit model, not as measured silicon. The neuromorphic rate-based work is a set of design principles for digital accelerators, showing multi-bit packets beat spikes in packet-switched networks and that higher-order ODE solvers cut both computation and communication while reducing numerical error, with benefits ultimately bounded by arithmetic precision. The PIM qLDPC decoding result is a simulation using uPIMulator with ideal syndrome measurements and a projection to 2,560 DPUs, not hardware. A 4 rather than 5 reflects that the exciting margins are still modelled.

**TLDR: Mainstream digital accelerators are shipping and measured; the alternative substrates split sharply between working silicon and circuit models.**

## Drivers (4/5)

Demand is explicit and growing: LLMs place unprecedented and still-growing demands on the hardware that trains and serves them, across both cloud and edge deployment. Beyond AI, real-time quantum error correction creates a hard classical-compute demand with low and predictable latency requirements as syndrome workloads grow, and physical AI creates demand for single-batch, low-power, ultra-low-latency inference parts.

On the supply side, the state is now a direct funder and gatekeeper. The Department of Commerce announced letters of intent with seven companies for $874 million to accelerate semiconductor R&D for the compute supply chain on 29 July 2026 <sup class="ref"><a href="https://news.google.com/rss/articles/CBMitAFBVV95cUxOZzcxTXJ1dkYwSHNnbU11YUx6ZVM2RDZFb0ltd1NfeFRVdWxNXzBJcVRCZHV3OUJqS0p6V1ZjZl9wVDc0M2k3LVVJRWo0ZGJXTXF0Tmp6a3ZUejhUakJldnRrR19JeTdPSXpINHBfZnFFTXhBTUUxNWFUdk1LYmJTY0JobEJWaU84a2U1T0VKWTBqRmFpNFN4TW9iV3hKNWlOVGhQUm1yZTJBdlRoY251VTh6d0o?oc=5" title="Department of Commerce Announces Letters of Intent With 7 Companies for $874 Million to Accelerate Semiconductor R&D for" rel="noopener">ref</a></sup>, and moved in August 2026 to block Chinese AI firms from remote access to advanced chips <sup class="ref"><a href="https://news.google.com/rss/articles/CBMi0AFBVV95cUxQNXZaemdNRW8tX2R1U3YxS0h1QWplU1huWWlKUm9kZ3RtQkU5N25wSWtkMlBkTl9ESHpMRDFidGFaTldTU1BFdXZvZHB3MFJZWld5bWRGdUtPOWwybThtZzVGU0RfUFg2emhKWDhaLTluRG5reGZfTU1YWHpTektlTmRiWVNQNzNoRGNiZWNXcTJaZ2ZNb2d3TXB4UXJ4VVhlZldjaFZjd04ybEloUDIxdU5Eb3poMGJubEJQNXhvQl9lWkxhYVUwZnFxemU2Z0Mt?oc=5" title="U.S. Commerce Department moves to block China AI firms from remote access to advanced chips - 디지털투데이" rel="noopener">ref</a></sup>. Controls on access are themselves a driver of architectural diversity, since restricted buyers have an incentive to fund alternatives; the sources do not quantify that effect, so it is a directional read rather than a measured one. The remaining structural driver is negative: Moore's Law stagnation means specialisation is the main remaining source of performance-per-watt.

**TLDR: LLM demand plus state industrial policy on the supply side, with export controls now shaping who gets what.**

## Novelty (3/5)

The quantified improvements in these sources are mostly against soft baselines. PIM's 8.8x is against a 16-logical-CPU baseline for qLDPC decoding, not against a GPU or a bespoke decoder ASIC. RVV 1.0 is better than scalar execution on the same RISC-V cores, while the meaningful comparison, against a state-of-the-art HPC ARM64 chip in NVIDIA Grace, is where the hurdles show. The survey's own conclusion is that no single architecture is optimal across workloads and that PIM enters systems as a heterogeneous complement rather than a replacement. That is the signature of an incremental, portfolio-shaped field rather than a step change.

The strongest novelty claim is on design cadence rather than on the logic itself. Redwood is reported as a frontier AI accelerator whose performance model, RTL, UVM environments, formal proofs, firmware and kernels were autonomously generated in under two weeks from a high-level specification by two human architects, with no human intervention below the specification and every block reaching 95% coverage via commercial tooling. A supporting datapoint from EDA: DeepSeq3's hierarchical circuit representation learning reduces bounded model checking solving time by 18% on large-scale benchmarks. If a two-week specification-to-silicon loop is reproducible, it changes the economics of specialisation more than any individual microarchitecture here does; the sources give one demonstration and no independent replication.

**TLDR: Real, quantified gains over CPU and scalar baselines, but the incumbent GPU comparison is where the numbers are thinnest.**

## Diffusion (3/5)

The survey compares platforms on compute, memory, energy, programmability and scalability and finds GPUs remain the flexible default, with domain-specific ASICs winning only for stable, high-volume workloads. That is a precise statement of the diffusion barrier: a non-GPU part must find a workload that will not move before the silicon is obsolete, which is exactly the timescale mismatch that makes architectural commitments expensive. PIM's path is easier because it enters as a heterogeneous complement rather than demanding a wholesale migration.

RISC-V shows what the barrier looks like in detail. Silicon exists and vectors work, but hardware-specific implementation challenges remain across the four platforms tested and the authors frame the question as whether RISC-V can become a mainstay in HPC, not whether it has. On the EDA side, adoption of circuit representation learning is explicitly hindered by the scale of industrial netlists. Policy adds a further gate: export controls now reach remote access to advanced chips, so geography determines availability independently of technical merit <sup class="ref"><a href="https://news.google.com/rss/articles/CBMi0AFBVV95cUxQNXZaemdNRW8tX2R1U3YxS0h1QWplU1huWWlKUm9kZ3RtQkU5N25wSWtkMlBkTl9ESHpMRDFidGFaTldTU1BFdXZvZHB3MFJZWld5bWRGdUtPOWwybThtZzVGU0RfUFg2emhKWDhaLTluRG5reGZfTU1YWHpTektlTmRiWVNQNzNoRGNiZWNXcTJaZ2ZNb2d3TXB4UXJ4VVhlZldjaFZjd04ybEloUDIxdU5Eb3poMGJubEJQNXhvQl9lWkxhYVUwZnFxemU2Z0Mt?oc=5" title="U.S. Commerce Department moves to block China AI firms from remote access to advanced chips - 디지털투데이" rel="noopener">ref</a></sup>.

**TLDR: GPUs are the default because they are programmable; every challenger's barrier is software and integration, not silicon.**

## Impact (5/5)

The value at stake is visible in what depends on it. AI capability is gated by hardware whose demands are unprecedented and still growing, with energy dominated by data movement, meaning architectural choices set both the cost and the power envelope of everything built on top. Fault-tolerant quantum computing has a classical-compute dependency: real-time error correction needs decoders with low and predictable latency at growing syndrome volumes, and the proposed answer is an architectural one. Quantum device engineering itself is compute-bound, with fully simulated gate-voltage sweeps for charge stability diagrams described as computationally expensive.

Governments are pricing this accordingly, committing $874 million in letters of intent with seven companies specifically for the compute supply chain <sup class="ref"><a href="https://news.google.com/rss/articles/CBMitAFBVV95cUxOZzcxTXJ1dkYwSHNnbU11YUx6ZVM2RDZFb0ltd1NfeFRVdWxNXzBJcVRCZHV3OUJqS0p6V1ZjZl9wVDc0M2k3LVVJRWo0ZGJXTXF0Tmp6a3ZUejhUakJldnRrR19JeTdPSXpINHBfZnFFTXhBTUUxNWFUdk1LYmJTY0JobEJWaU84a2U1T0VKWTBqRmFpNFN4TW9iV3hKNWlOVGhQUm1yZTJBdlRoY251VTh6d0o?oc=5" title="Department of Commerce Announces Letters of Intent With 7 Companies for $874 Million to Accelerate Semiconductor R&D for" rel="noopener">ref</a></sup> and treating access to advanced chips as an instrument of policy <sup class="ref"><a href="https://news.google.com/rss/articles/CBMi0AFBVV95cUxQNXZaemdNRW8tX2R1U3YxS0h1QWplU1huWWlKUm9kZ3RtQkU5N25wSWtkMlBkTl9ESHpMRDFidGFaTldTU1BFdXZvZHB3MFJZWld5bWRGdUtPOWwybThtZzVGU0RfUFg2emhKWDhaLTluRG5reGZfTU1YWHpTektlTmRiWVNQNzNoRGNiZWNXcTJaZ2ZNb2d3TXB4UXJ4VVhlZldjaFZjd04ybEloUDIxdU5Eb3poMGJubEJQNXhvQl9lWkxhYVUwZnFxemU2Z0Mt?oc=5" title="U.S. Commerce Department moves to block China AI firms from remote access to advanced chips - 디지털투데이" rel="noopener">ref</a></sup>. The caveat on the 5 is that it applies to the category, not to any one architecture within it: the sources are clear that no single approach dominates, so value accrues to the portfolio and to whoever controls the memory hierarchy, not necessarily to any particular challenger.

**TLDR: Compute architecture is the rate-limiter on AI capability, on error-corrected quantum computing and on national industrial policy simultaneously.**

## Timing Now (0-2yr)

Multiple commercial accelerators were presented in August 2026 <sup class="ref"><a href="https://www.latent.space/p/ainews-hot-chips-openais-jalapeno" title="[AINews] Hot Chips: OpenAI’s Jalapeño, Cerebras CS-5, Groq 3 LPX, Apple M6" rel="noopener">ref</a></sup> and RVV 1.0 silicon is already benchmarkable across four distinct vendors, so the category is in deployment, not development. PIM is described as the most promising near-term response to the memory wall and as already entering systems as a heterogeneous complement, which puts it inside the same window.

The longer-dated items are the substrate changes. Analog frequency-domain vector-matrix multiplication is at the small-signal circuit-model stage with no reported measured device performance, and the rate-based neuromorphic work outlines design principles for accelerators yet to be built, with benefits explicitly bounded by arithmetic precision. The sources give no dates for either, so anything beyond "not now" for those two would be invention.

**TLDR: The commercial layer is already shipping; the memory-centric and AI-designed layers land within this window, the analog and neuromorphic ones do not.**

## Overrated or underrated? Fairly rated

The category as a whole is correctly seen as central, and the money and export-control attention confirm it <sup class="ref"><a href="https://news.google.com/rss/articles/CBMitAFBVV95cUxOZzcxTXJ1dkYwSHNnbU11YUx6ZVM2RDZFb0ltd1NfeFRVdWxNXzBJcVRCZHV3OUJqS0p6V1ZjZl9wVDc0M2k3LVVJRWo0ZGJXTXF0Tmp6a3ZUejhUakJldnRrR19JeTdPSXpINHBfZnFFTXhBTUUxNWFUdk1LYmJTY0JobEJWaU84a2U1T0VKWTBqRmFpNFN4TW9iV3hKNWlOVGhQUm1yZTJBdlRoY251VTh6d0o?oc=5" title="Department of Commerce Announces Letters of Intent With 7 Companies for $874 Million to Accelerate Semiconductor R&D for" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://news.google.com/rss/articles/CBMi0AFBVV95cUxQNXZaemdNRW8tX2R1U3YxS0h1QWplU1huWWlKUm9kZ3RtQkU5N25wSWtkMlBkTl9ESHpMRDFidGFaTldTU1BFdXZvZHB3MFJZWld5bWRGdUtPOWwybThtZzVGU0RfUFg2emhKWDhaLTluRG5reGZfTU1YWHpTektlTmRiWVNQNzNoRGNiZWNXcTJaZ2ZNb2d3TXB4UXJ4VVhlZldjaFZjd04ybEloUDIxdU5Eb3poMGJubEJQNXhvQl9lWkxhYVUwZnFxemU2Z0Mt?oc=5" title="U.S. Commerce Department moves to block China AI firms from remote access to advanced chips - 디지털투데이" rel="noopener">ref</a></sup>. The misallocation is internal. Attention and specification sheets still lead with arithmetic throughput, while the 2026 analysis says the decisive constraint is memory: decode is bandwidth-bound, the KV cache can rival weight storage, and data movement dominates energy. On that reading, near-memory and processing-in-memory are underrated relative to peak-FLOPs announcements, and the independent qLDPC decoding result showing 8.8x over a CPU baseline from the same data-locality logic is corroborating evidence from an unrelated domain.

The other underweighted item is design cadence. If specification-to-verified-RTL in under two weeks with 95% block coverage generalises beyond one accelerator, the hedge-generality tax that keeps GPUs dominant gets cheaper to avoid, and the ASIC-versus-GPU calculus shifts for workloads that today are too unstable to justify custom silicon. That is a single unreplicated demonstration from one team, so it is a thesis to test rather than a conclusion. Conversely, treating analog and neuromorphic substrates as near-term contenders is not supported: the sources present circuit models and design principles, not measured competitive parts.

## Prediction

By 31 December 2028, no RVV 1.0 RISC-V platform will be shown in a peer-reviewed HPL or HPCG benchmark to match NVIDIA Grace per socket, and processing-in-memory will still be shipping in commercial LLM inference systems as a complement to HBM-attached GPUs and ASICs rather than as a standalone replacement.

## Evidence base

- 31 August 2026: roofline analysis across GPUs, TPUs, Trainium, Groq, Cerebras, FPGAs, PIM, neuromorphic and photonic platforms concludes the decisive LLM constraint is memory, not arithmetic, with PIM the most promising near-term response and no single architecture optimal across workloads.
- 31 August 2026: normalised min-sum BP decoding of the **144,12,12** bivariate bicycle qLDPC code on a DPU-based PIM architecture projects 1.071 x 10^7 decodes/s across 2,560 DPUs versus 1.22 x 10^6 decodes/s on a 16-logical-CPU baseline, an 8.8x improvement.
- 31 August 2026: RVV 1.0 silicon from SiFive, SpacemiT and T-Head beats scalar execution on BLAS, FFTW, HPL, HPCG and STREAM, but hardware-specific implementation challenges remain versus NVIDIA Grace.
- 31 August 2026: Redwood, an accelerator for single-batch low-power ultra-low-latency physical-AI inference, had its performance model, RTL, UVM environments, formal proofs, firmware and kernels autonomously generated in under two weeks, every block reaching 95% coverage.
- 31 August 2026: DeepSeq3 hierarchical circuit representation learning reduces bounded model checking solving time by 18% on large-scale benchmarks.
- 29 July 2026: the Department of Commerce announced letters of intent with seven companies for $874 million to accelerate semiconductor R&D for the compute supply chain <sup class="ref"><a href="https://news.google.com/rss/articles/CBMitAFBVV95cUxOZzcxTXJ1dkYwSHNnbU11YUx6ZVM2RDZFb0ltd1NfeFRVdWxNXzBJcVRCZHV3OUJqS0p6V1ZjZl9wVDc0M2k3LVVJRWo0ZGJXTXF0Tmp6a3ZUejhUakJldnRrR19JeTdPSXpINHBfZnFFTXhBTUUxNWFUdk1LYmJTY0JobEJWaU84a2U1T0VKWTBqRmFpNFN4TW9iV3hKNWlOVGhQUm1yZTJBdlRoY251VTh6d0o?oc=5" title="Department of Commerce Announces Letters of Intent With 7 Companies for $874 Million to Accelerate Semiconductor R&D for" rel="noopener">ref</a></sup>; on 29 August 2026 it moved to block Chinese AI firms from remote access to advanced chips <sup class="ref"><a href="https://news.google.com/rss/articles/CBMi0AFBVV95cUxQNXZaemdNRW8tX2R1U3YxS0h1QWplU1huWWlKUm9kZ3RtQkU5N25wSWtkMlBkTl9ESHpMRDFidGFaTldTU1BFdXZvZHB3MFJZWld5bWRGdUtPOWwybThtZzVGU0RfUFg2emhKWDhaLTluRG5reGZfTU1YWHpTektlTmRiWVNQNzNoRGNiZWNXcTJaZ2ZNb2d3TXB4UXJ4VVhlZldjaFZjd04ybEloUDIxdU5Eb3poMGJubEJQNXhvQl9lWkxhYVUwZnFxemU2Z0Mt?oc=5" title="U.S. Commerce Department moves to block China AI firms from remote access to advanced chips - 디지털투데이" rel="noopener">ref</a></sup>.

## Open questions

- Does the 8.8x PIM advantage for qLDPC decoding survive the move from uPIMulator simulation and ideal syndrome measurements to real DPU hardware with measurement noise, and does it hold against a GPU rather than a 16-logical-CPU baseline?
- Is the two-week autonomous specification-to-RTL loop reproducible by a second team on a different accelerator target, and does the resulting silicon meet its performance model in fabricated form?
- Which specific hardware implementation challenges limit RVV 1.0 platforms against NVIDIA Grace, and are they microarchitectural, memory-system or compiler problems, since only the last is quickly fixable?
- Do the analog frequency-domain and rate-based neuromorphic approaches have any measured silicon results, and at what precision, given that the neuromorphic gains are stated to be bounded by arithmetic precision?

---
*Assessment drafted 2026-08-31 from up to 11 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
