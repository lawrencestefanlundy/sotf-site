---
type: concept
slug: memory-wall
canonical_name: The Memory Wall
aliases:
- memory bandwidth wall
parent_concepts:
- memory
related_concepts:
- von-neumann-bottleneck
- hbm
- hbm-cowos-bottleneck
- prefill-vs-decode
- processing-in-memory
- in-memory-computing
sources:
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2025-08-12-scaling-the-memory-wall-the-rise-and-roadmap-of-hbm]]'
scorecard:
  viability: 5
  drivers: 4
  novelty: 2
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 16
descendants:
- inference-economics
- token-cost-stack
sources_7d: 2
sources_30d: 2
recent_mentions:
- slug: 2026-07-31-positron-research-sprint
  title: 'Positron AI research sprint: architecture, funding, customers, manufacturing'
  date: '2026-07-31'
  kind: web
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
- slug: 2026-01-22-ai-chips-computeram-and-the-future
  title: 'AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara'
  date: '2026-01-22'
  kind: substack
- slug: 2025-08-12-scaling-the-memory-wall-the-rise-and-roadmap-of-hbm
  title: 'Scaling the Memory Wall: The Rise and Roadmap of HBM'
  date: '2025-08-12'
  kind: web
neighbors:
- slug: von-neumann-bottleneck
  name: Von Neumann Bottleneck
  path: /compute/compute-architecture/von-neumann-bottleneck/
  macro: compute
- slug: hbm
  name: HBM (High-Bandwidth Memory)
  path: /memory/mainstream-memory/hbm/
  macro: memory
- slug: hbm-cowos-bottleneck
  name: HBM / CoWoS Bottleneck
  path: /compute/compute-architecture/hbm-cowos-bottleneck/
  macro: compute
- slug: prefill-vs-decode
  name: Prefill vs Decode (LLM inference phases)
  path: /compute/ai-edge/prefill-vs-decode/
  macro: compute
- slug: processing-in-memory
  name: Processing-in-Memory (PIM)
  path: /memory/emerging-memory/processing-in-memory/
  macro: memory
- slug: in-memory-computing
  name: In-Memory Computing
  path: /memory/emerging-memory/in-memory-computing/
  macro: memory
---
**The memory wall is the widening gap between how fast processors can compute and how fast memory can feed them: peak hardware compute grew roughly 60,000x over two decades while DRAM bandwidth grew about 100x, which is why modern AI inference is limited by bytes moved rather than arithmetic **2024 Gholami Ai And Memory Wall**.**

## Summary

**What it is.** "The memory wall" names a structural imbalance in computer architecture: arithmetic throughput has compounded far faster than the bandwidth and capacity of the memory that supplies operands to it. The canonical quantification comes from Gholami et al. (blog 2021, Hot Chips 2023, IEEE Micro 2024): over twenty years peak hardware compute rose ~60,000x, DRAM bandwidth ~100x, and interconnect bandwidth ~30x. Underneath those totals, peak server FLOPS scale at ~3.0x every two years, DRAM bandwidth at ~1.6x and interconnect bandwidth at ~1.4x **2024 Gholami Ai And Memory Wall**. Because the rates differ, the share of workloads that are memory-bound rather than compute-bound grows monotonically with each hardware generation, regardless of any single design decision.

**How it bites.** Two mechanisms. First, throughput: if a kernel has low arithmetic intensity (few operations per byte fetched), the arithmetic units idle while weights arrive. In LLM serving the decode phase is the bandwidth-bound one, and one commentary describes GPU arithmetic units as spending most of their time stalled waiting for weights from HBM <sup class="ref"><a href="https://stateofthefuture.substack.com/p/ai-chips-computeram-and-the-future" title="AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara" rel="noopener">ref</a></sup>. Second, energy: an arithmetic operation costs sub-picojoule while an off-chip DRAM fetch costs roughly 1.3 to 2.6 nJ, so data movement, not computation, dominates the energy bill **2024 Gholami Ai And Memory Wall**. Reasoning-style models make both worse, because long output sequences, low arithmetic intensity and tight latency budgets all push demand for bandwidth up and system utilisation down.

**The parameters that decide it.** For any given workload the wall is set by bytes fetched per useful operation (arithmetic intensity), by achievable bandwidth per package, by memory capacity per package (which decides how much of a model or KV cache stays local), and by the fraction of peak bandwidth a design can actually realise. That last parameter is where the commercial fight is: Positron's second-generation Asimov silicon claims over 90% memory bandwidth utilisation on real transformer workloads against under 30% claimed for GPUs, using commodity LPDDR5x rather than HBM, at 864GB to 2.3TB capacity per chip and 2.76 TB/s realisable bandwidth <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>. Groq attacks the same parameter from the other end, placing 230MB of on-die SRAM at 80 TB/s, roughly an order of magnitude above HBM bandwidth, at the cost of tiny capacity <sup class="ref"><a href="https://stateofthefuture.substack.com/p/ai-chips-computeram-and-the-future" title="AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara" rel="noopener">ref</a></sup>.

**The mitigations, and their own walls.** Four families are visible in the literature: more bandwidth per package (HBM, with a roadmap through HBM4 and custom base dies <sup class="ref"><a href="https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/" title="Scaling the Memory Wall: The Rise and Roadmap of HBM" rel="noopener">ref</a></sup>); moving computation into memory (processing-in-memory using RRAM, PCM or MRAM); better interconnect, including 3D electronic-photonic stacks benchmarked above 10 TB/s/mm2 bandwidth density; and distributed on-chip memory as in digital neuromorphic processors. The last of these is instructive: an analysis of current digital neuromorphic chips finds on-chip SRAM and STT-MRAM have themselves become dominant consumers of area and energy, producing what the authors call a new memory wall. The wall moves; it does not obviously disappear.

## Viability (5/5)

The memory wall is a measured trend rather than a projection: ~60,000x compute growth against ~100x DRAM bandwidth and ~30x interconnect over twenty years, with per-generation rates of 3.0x, 1.6x and 1.4x per two years respectively **2024 Gholami Ai And Memory Wall**. Because the rates are ratios of exponentials, the conclusion follows arithmetically rather than by argument: the memory-bound fraction of workloads grows unless arithmetic intensity rises to compensate.

Corroboration is broad and independent of the original authors. A 2026 architecture paper opens by stating LLM inference performance is increasingly bottlenecked by the memory wall and that GPUs struggle on bandwidth-bound workloads; a PIM simulator paper takes the wall as the motivation for its entire design space; a device-level review frames PIM as a response to it; and a critical neuromorphic outlook accepts the premise while arguing the fixes recreate it. The only serious caveat is definitional: "memory wall" is used loosely for at least three distinct constraints (off-package bandwidth, capacity, and on-chip memory area and energy), and conflating them produces bad architectural arguments.

**TLDR: Not a hypothesis. The divergence is measured, the mechanism is understood, and independent 2026 papers treat it as the starting premise.**

## Drivers (4/5)

**Demand.** The workload mix is moving towards the worst case for memory. Reasoning LLM applications combine long output sequences, low arithmetic intensity and tight latency constraints, which demand significantly higher memory bandwidth and cause system utilisation to drop. Decode, the phase that dominates long-generation serving, is the bandwidth-bound phase **2024 Gholami Ai And Memory Wall**. Capital is following the diagnosis: the Nvidia-Groq arrangement is characterised as a $20 billion deal about precisely this problem <sup class="ref"><a href="https://stateofthefuture.substack.com/p/ai-chips-computeram-and-the-future" title="AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara" rel="noopener">ref</a></sup>.

**Supply.** Vendors are responding along every axis at once, which is why the score is 4 rather than 5. HBM has a live roadmap including custom base dies with HBM4, plus system-level answers such as KV cache offload and disaggregated prefill/decode <sup class="ref"><a href="https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/" title="Scaling the Memory Wall: The Rise and Roadmap of HBM" rel="noopener">ref</a></sup>. Interconnect work targets bandwidth density above 10 TB/s/mm2 via 3D optical vias, and one level up, copper's reach is shrinking as bandwidth rises, pushing links optical <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>. None of these changes the underlying scaling exponents reported by Gholami, so they buy generations rather than removing the constraint.

**TLDR: Demand-side pressure is rising sharply with reasoning-model inference; supply-side response exists but scales at a slower exponent.**

## Novelty (2/5)

As a concept the memory wall is a restatement of the von Neumann bottleneck, and the energy half of the argument dates to Horowitz's ISSCC 2014 figures on DRAM fetch cost versus arithmetic cost **2024 Gholami Ai And Memory Wall**. Nothing about the diagnosis is a discovery. The contribution of the Gholami line of work is measurement discipline: it turned a qualitative complaint into specific growth rates and ratios that can be used to price architectures, which is why it functions as the standard citation for "compute outran memory".

The genuinely newer content in the recent literature is second-order and more interesting than the headline. The claim that distributed on-chip memory does not escape the problem, because SRAM and STT-MRAM arrays become the dominant area and energy consumers and constitute a new memory wall, is a real update on the naive "put compute next to memory and the problem goes away" position. Similarly, the observation that realisable bandwidth utilisation (over 90% claimed versus under 30% for GPUs) can matter more than peak bandwidth reframes the wall as partly an architectural inefficiency rather than purely a DRAM physics limit <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>.

**TLDR: The idea is decades old; what is new is the quantification and the finding that the wall reappears inside its own cures.**

## Diffusion (3/5)

Diffusion of the diagnosis is essentially complete within the field: it is the opening premise of papers across computer architecture, emerging technologies and systems in 2026, and it drives the commercial narratives of HBM suppliers <sup class="ref"><a href="https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/" title="Scaling the Memory Wall: The Rise and Roadmap of HBM" rel="noopener">ref</a></sup> and of challenger silicon <sup class="ref"><a href="https://stateofthefuture.substack.com/p/ai-chips-computeram-and-the-future" title="AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara" rel="noopener">ref</a></sup>.

Diffusion of the responses is much thinner, and this is where the score is set. Real PIM hardware remains scarce, which is why simulation is the primary means of exploring the design space, and the memristor PIM literature still centres on reliability and device-level optimisation as prerequisites for commercially viable systems. Photonic interconnect is presented as a proposed and benchmarked platform with a pathway to industry-ready design, not as shipped product, and coherent optics inside the data centre is blocked on DSPs that consume 3-4x more power and cost 3-5x more than intensity-based systems <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>. On the merchant silicon side, Positron's Asimov is at tape-out October 2026 with production early 2027 <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>. The near-term deployed answers remain HBM scaling plus software-level tricks such as KV cache offload and disaggregated prefill/decode <sup class="ref"><a href="https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/" title="Scaling the Memory Wall: The Rise and Roadmap of HBM" rel="noopener">ref</a></sup>.

**TLDR: The framing is already consensus among architects; the architectural cures are mostly pre-deployment, and the sources say so.**

## Impact (4/5)

If bandwidth and capacity, not FLOPS, are the binding constraint, then the wall determines which chips are worth buying, how models are partitioned and served, and what a token costs. The energy asymmetry, sub-picojoule arithmetic against 1.3-2.6 nJ per off-chip DRAM fetch, means data movement dominates the power bill of AI data centres, so the wall also sets the ceiling on deployable capacity per megawatt **2024 Gholami Ai And Memory Wall**. It explains a $20 billion commercial arrangement premised on bypassing HBM <sup class="ref"><a href="https://stateofthefuture.substack.com/p/ai-chips-computeram-and-the-future" title="AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara" rel="noopener">ref</a></sup> and the entire HBM supply chain build-out <sup class="ref"><a href="https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/" title="Scaling the Memory Wall: The Rise and Roadmap of HBM" rel="noopener">ref</a></sup>.

The score stops at 4 because the size of the prize attributable to solving it is asserted rather than demonstrated in these sources. Positron's 5x tokens per dollar and 5x tokens per watt versus NVIDIA Rubin, and its over-90% versus under-30% bandwidth utilisation comparison, are company figures for silicon not yet in production <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>. Groq's 80 TB/s from 230MB of SRAM is roughly an order of magnitude above HBM bandwidth but buys very little capacity, so the system-level economics depend on model size and batching in ways the sources do not resolve <sup class="ref"><a href="https://stateofthefuture.substack.com/p/ai-chips-computeram-and-the-future" title="AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara" rel="noopener">ref</a></sup>. And at least one credible analysis argues the recovered value is partly given back, because on-chip memory becomes the new area and energy sink.

**TLDR: It sets inference cost per token and therefore the economics of AI serving; the largest quantified gains are vendor claims, not independent measurements.**

## Timing Now (0-2yr)

The constraint is present tense. Inference is described as increasingly bottlenecked by the memory wall today, with utilisation dropping on reasoning workloads, and the industry is already restructuring serving around it through KV cache offload and disaggregated prefill/decode <sup class="ref"><a href="https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/" title="Scaling the Memory Wall: The Rise and Roadmap of HBM" rel="noopener">ref</a></sup>.

The mitigations split across bands. HBM roadmap steps and software-level workarounds are Now. Non-HBM merchant accelerators are at the 0-2 year boundary, with Positron's Asimov taped out October 2026 and in production early 2027 <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>. Memristor-based PIM is later: the review still treats reliability and device optimisation as open problems for commercial viability, and hardware scarcity forces the field to work in simulation. 3D electronic-photonic interconnect is presented as benchmarked with a pathway to industry-ready design rather than deployed.

**TLDR: Already the binding constraint on LLM inference; the fixes arrive over a longer horizon than the problem.**

## Overrated or underrated? Fairly rated

The memory wall as a diagnosis is correctly priced and hard to argue with. It is quantified from two decades of data **2024 Gholami Ai And Memory Wall**, accepted as the premise across independent 2026 architecture literature, and visibly shaping capital allocation from HBM supply chains to challenger silicon. Anyone building or buying AI compute who still reasons primarily in FLOPS is making a mistake the field settled some time ago.

What is mispriced is the inference people draw from it. "The memory wall is real" is not the same statement as "my non-HBM architecture wins", and the sources contain the counterexample: digital neuromorphic processors that distribute memory on chip end up with SRAM and STT-MRAM dominating area and energy, a new memory wall rather than an escape. The credible near-term moves are unglamorous: raise realisable bandwidth utilisation on ordinary memory <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>, buy capacity with commodity DRAM, trade capacity for bandwidth with on-die SRAM <sup class="ref"><a href="https://stateofthefuture.substack.com/p/ai-chips-computeram-and-the-future" title="AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara" rel="noopener">ref</a></sup>, and keep extending HBM <sup class="ref"><a href="https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/" title="Scaling the Memory Wall: The Rise and Roadmap of HBM" rel="noopener">ref</a></sup>. The exotic answers, memristive PIM and 3D photonic interconnect, are where the concept is most often invoked and where the evidence is thinnest.

## Prediction

By 31 December 2027, no memristor-based processing-in-memory device (RRAM, PCM or MRAM logic) will be shipping in volume as an AI data-centre inference product; the deployed responses to the memory wall will remain HBM scaling, on-die SRAM and high-utilisation commodity DRAM designs such as Positron's Asimov.

## Evidence base

- Over twenty years peak hardware compute grew ~60,000x while DRAM bandwidth grew ~100x and interconnect bandwidth ~30x; per-generation rates are 3.0x, 1.6x and 1.4x every two years **2024 Gholami Ai And Memory Wall** (2024-03-21).
- Arithmetic costs sub-picojoule per operation while an off-chip DRAM fetch costs ~1.3-2.6 nJ, so data movement dominates energy (Horowitz ISSCC 2014, via **2024 Gholami Ai And Memory Wall**, 2024-03-21).
- Reasoning LLM workloads combine long output sequences, low arithmetic intensity and tight latency constraints, driving higher bandwidth demand and falling system utilisation on GPUs (2026-06-05, paper published 2026-02-20).
- Digital neuromorphic processors that distribute memory on chip find SRAM and STT-MRAM become significant consumers of area and energy, creating a new memory wall (2026-04-09).
- Real processing-in-memory hardware remains scarce, so simulation is the primary way to explore the PIM design space (2026-07-28).
- Positron's Asimov claims LPDDR5x rather than HBM, 864GB-2.3TB per chip, 2.76 TB/s realisable bandwidth, over 90% memory bandwidth utilisation versus under 30% for GPUs, and 5x tokens per dollar and per watt versus NVIDIA Rubin; tape-out October 2026, production early 2027 <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup> (2026-07-31).
- Groq places 230MB of on-die SRAM at 80 TB/s, roughly one order of magnitude above HBM bandwidth, in an arrangement with Nvidia described as a $20 billion deal <sup class="ref"><a href="https://stateofthefuture.substack.com/p/ai-chips-computeram-and-the-future" title="AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara" rel="noopener">ref</a></sup> (2026-01-22).

## Open questions

- Do Positron's over-90% memory bandwidth utilisation and 5x tokens-per-dollar claims against NVIDIA Rubin survive independent measurement once Asimov reaches production in early 2027 <sup class="ref"><a href="https://www.positron.ai/asimov" title="Positron AI research sprint: architecture, funding, customers, manufacturing" rel="noopener">ref</a></sup>?
- Does the new on-chip memory wall identified in digital neuromorphic processors generalise to SRAM-heavy inference accelerators, and at what model size does the area and energy cost of on-die memory exceed the saving in off-chip fetches?
- Which reliability metric is the actual blocker for commercially viable memristive PIM, and is there any experimentally demonstrated logic family that meets it at scale?
- Do custom HBM4 base dies change the effective DRAM bandwidth scaling rate above the historical ~1.6x per two years, or only shift the cost curve <sup class="ref"><a href="https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/" title="Scaling the Memory Wall: The Rise and Roadmap of HBM" rel="noopener">ref</a></sup> **2024 Gholami Ai And Memory Wall**?

---
*Assessment drafted 2026-08-31 from up to 10 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
