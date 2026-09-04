---
type: concept
slug: dram
canonical_name: DRAM
aliases: []
kind: technology
parent_concepts:
- memory
- mainstream-memory
related_concepts: []
sources:
- '[[2026-07-03-thats-a-learning-curve-mate-not-rsi]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2026-08-07-the-memory-trade-isnt-over-weights]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-07-16-the-path-to-agi-runs-through-hbm]]'
- '[[2026-02-13-four-things-friday]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2026-07-10-the-next-vc-meme-is]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
scorecard:
  viability: 5
  drivers: 5
  novelty: 2
  diffusion: 5
  impact: 5
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 181
sources_7d: 3
sources_30d: 15
recent_mentions:
- slug: 2026-08-07-the-memory-trade-isnt-over-weights
  title: 'The Memory Trade Isn''t Over: Weights and KV Cache'
  date: '2026-08-07'
  kind: substack
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-31-positron-research-sprint
  title: 'Positron AI research sprint: architecture, funding, customers, manufacturing'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-27-arxiv-dynamic-rowhammer-threshold-managementtemperature-aware-thre
  title: Dynamic Rowhammer Threshold Management:Temperature-Aware Threshold Degradation for In-DRAM Defenses
  date: '2026-07-27'
  kind: paper
- slug: 2026-07-27-cxmt-star-market-debut
  title: CXMT's 466% STAR Market debut makes it China's most valuable mainland-listed company
  date: '2026-07-27'
  kind: web
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-16-the-path-to-agi-runs-through-hbm
  title: The Path To AGI Runs Through HBM
  date: '2026-07-16'
  kind: substack
- slug: 2026-07-15-kimi-k3-launch-moonshot
  title: Kimi K3 — Moonshot launch post (architecture, quantisation, serving requirements)
  date: '2026-07-15'
  kind: web
neighbors: []
---
**DRAM is the volatile main-memory technology that every computer and AI accelerator depends on, and because its bandwidth has grown roughly 100x while peak compute grew about 60,000x over two decades, it is now the binding constraint on machine learning inference rather than a solved commodity **2024 Gholami Ai And Memory Wall**.**

## Summary

Dynamic random-access memory stores each bit as charge on a capacitor accessed through a single transistor. That one-transistor-one-capacitor cell is why DRAM is dense and cheap relative to SRAM, and why it is volatile and must be periodically refreshed. Access is organised by rows and columns within banks and subarrays: a row is activated onto sense amplifiers, then columns are read out. This structure sets almost every performance parameter that matters, including activation latency, refresh overhead and the fact that reading is destructive and requires restoration. The technology appears in the market as a family of interface standards rather than one product: DDR for servers and desktops, LPDDR for mobile and unified-memory SoCs, GDDR for graphics, and HBM as stacked dies for accelerators. A current memory-system simulator has to model HBM3/4, LPDDR5/6 and GDDR7 simultaneously to be useful, which is a fair indication of how fragmented the interface landscape has become.

The parameter that decides DRAM's strategic position is the ratio of bandwidth to compute. Peak server FLOPS have scaled at roughly 3.0x every two years, DRAM bandwidth at about 1.6x and interconnect bandwidth at about 1.4x, producing the twenty-year divergence of ~60,000x compute against ~100x DRAM bandwidth and ~30x interconnect bandwidth **2024 Gholami Ai And Memory Wall**. The energy asymmetry runs the same way: an arithmetic operation costs sub-picojoule energy while an off-chip DRAM fetch costs roughly 1.3 to 2.6 nJ, so data movement, not arithmetic, dominates the power bill **2024 Gholami Ai And Memory Wall**. This is why LLM decode, state-vector quantum simulation and graph analytics all present as memory-bound workloads. A controlled study on Apple M4 Pro unified memory found every quantum gate implementation had arithmetic intensity at or below 0.38 FLOP/byte against roughly 224 GB/s of LPDDR5X STREAM bandwidth, well below the roofline ridge for any plausible peak compute.

The consequence is that DRAM is no longer a passive commodity tier. Three distinct lines of work are trying to move value into or around it. First, packaging and interface: proposals to give UCIe memory semantics and attach LPDDR6 or HBM dies through a logic die, or to have the DRAM die speak UCIe natively, claim up to 10x higher bandwidth density, up to 3x lower latency and up to 3x lower power than HBM4 and conventional on-package LPDDR. Second, computation in or near the array: processing-in-memory designs put logic on chiplets beside DRAM banks to serve memory-bound GEMV and flat GEMM in the decode phase, while processing-using-DRAM exploits simultaneous multiple-row activation to make each DRAM column a compute engine. Third, heterogeneous hierarchies that offload part of DRAM's job to ReRAM, MRAM or Flash because DRAM must currently hold static weights and dynamic KV caches at the same time, creating bandwidth contention.

Running underneath all of this is a reliability problem that gets worse as cells shrink. Read disturbance began with RowHammer and RowPress, where repeated access to one row flips bits in neighbours. ColumnDisturb is a distinct phenomenon that disturbs columns rather than rows and affects all cells across three consecutive subarrays. Denser arrays bring rows and columns closer together, so the same physics that delivers capacity scaling also erodes the correctness margin, and it corrupts in-DRAM computation as well as ordinary reads.

## Viability (5/5)

DRAM is not a candidate technology. It is the substrate every source here assumes: unified-memory SoCs, chiplet accelerators with HBM/DRAM stacks, edge inference hierarchies and the KV-cache offload software stack <sup class="ref"><a href="https://arxiv.org/abs/2510.09665" title="LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference" rel="noopener">ref</a></sup>. Simultaneously supporting HBM3/4, LPDDR5/6 and GDDR7 in a single simulator is evidence that all four families are live standards rather than roadmap items.

The caveat is directional, not existential. Density scaling is producing new failure modes faster than mitigations arrive: ColumnDisturb extends read disturbance from a few neighbouring rows to all cells across three consecutive subarrays, and the first proposed mitigations require per-subarray activation counters and targeted refresh. Characterisation of 112 DDR4 chips from 10 modules shows how much device-specific, undocumented behaviour sits inside commercial parts, enough to extract unique physical unclonable function responses from simultaneous multiple-row activation. DRAM works; each new node costs more in mitigation overhead to keep it working.

**TLDR: The incumbent in volume production across four interface families; the open question is the forward scaling path, not whether it works.**

## Drivers (5/5)

Demand side: inference, not training, is the forcing function. Decode is dominated by memory-bound GEMV and flat GEMM with low operational intensity, and KV cache size grows with context length, so models become memory-bound as context grows. On edge multimodal models, high-dimensional visual inputs inflate token sequences and therefore the KV cache, making data movement the dominant overhead. In current systems DRAM has to serve static weights and dynamic KV caches from the same bandwidth budget, which is itself the stated motivation for hybrid hierarchies. The commercial pull is visible in software too: KV-cache offload across CPU, disk and remote storage delivers 15x throughput improvement and has been absorbed into vLLM Production Stack, Dynamo, llm-d and KServe <sup class="ref"><a href="https://arxiv.org/abs/2510.09665" title="LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference" rel="noopener">ref</a></sup>.

Supply side: DRAM bandwidth scales at about 1.6x every two years against 3.0x for peak compute, so the gap widens structurally with each generation **2024 Gholami Ai And Memory Wall**. That mismatch is what funds the whole adjacent industry of HBM stacking, on-package UCIe memory, PIM chiplets and near-memory edge accelerators. Both curves point the same way: more spend on memory per unit of compute.

**TLDR: Demand is driven by memory-bound LLM decode and KV-cache growth; supply-side bandwidth scaling is the slower of the two curves by a factor of roughly two per generation.**

## Novelty (2/5)

As a device, DRAM is the reference point rather than the innovation. It is better than SRAM on density and cost and better than Flash on latency and write endurance, which is precisely why hybrid proposals keep DRAM for latency-critical attention traffic and push weights into denser non-volatile media: CHIME pairs monolithic 3D DRAM chiplets for low-latency attention bandwidth with RRAM chiplets for dense non-volatile weight storage, and QMC keeps DRAM in the loop while moving inlier weights to multi-level ReRAM and outliers to on-chip MRAM. Surveys of emerging room-temperature and cryogenic memories place DRAM and eDRAM alongside RRAM, MRAM and FeFET as one option among several rather than a deprecated one.

Where genuine novelty is claimed, it is at the boundary. Giving UCIe memory semantics, or making the DRAM die speak UCIe instead of the LPDDR6 bus, is claimed to beat HBM4 and on-package LPDDR by up to 10x on bandwidth density, up to 3x on latency and up to 3x on power. Chiplet PIM claims to escape the classic DRAM-process constraint that limited processing element capability and cost capacity when logic was placed inside the DRAM die. Processing-using-DRAM turns the array itself into a compute engine via simultaneous multiple-row activation, though experimental work on real chips shows results can be corrupted by interference from non-activated rows and from other columns computing concurrently. These are architectural rather than cell-level advances, and the ones measured on real silicon are still finding failure modes.

**TLDR: DRAM is the baseline others are measured against; the novelty lives in packaging, interfaces and in-array computation, not in the cell.**

## Diffusion (5/5)

Diffusion is complete. Every system described in these sources contains DRAM, from Apple unified-memory laptops to chiplet-based datacentre accelerators, and the research infrastructure needed to study it at scale is itself mature enough to be described as a laboratory with a standard characterisation tool covering multiple interface standards.

The meaningful barriers apply to the proposed extensions rather than the incumbent, and they are the classic ones for memory: standards conformance, cost per bit and validated reliability. The economics currently favour keeping value in software over commodity memory. KV-cache offload across CPU, disk and remote storage is shipping as commodity software rather than dedicated silicon, integrated into four separate serving stacks <sup class="ref"><a href="https://arxiv.org/abs/2510.09665" title="LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference" rel="noopener">ref</a></sup>. Anything that changes the DRAM die or its interface has to displace an installed base with a validated cost curve, and disturbance mitigations such as per-subarray activation counters add performance and energy overhead that has to be paid for in the same budget.

**TLDR: Already universal; the adoption question applies to the extensions, not to DRAM itself.**

## Impact (5/5)

The sources support a strong claim: the binding constraint on training and especially inference is increasingly memory bandwidth and capacity, not arithmetic throughput **2024 Gholami Ai And Memory Wall**. That makes DRAM the component that decides tokens per second per dollar and per watt. The energy figures make the point sharply: arithmetic costs sub-picojoule while an off-chip DRAM fetch costs roughly 1.3 to 2.6 nJ, a gap of three orders of magnitude, so any architecture that reduces DRAM traffic captures most of the available efficiency **2024 Gholami Ai And Memory Wall**.

Second-order effects reach further than performance. Memory-driven transfers inject large bursty flows into chiplet interposers, inflating tail latency and breaching service level agreements, which means DRAM traffic patterns now drive network-on-interposer topology design. Memory hierarchy transitions produce discontinuous, not gradual, performance cliffs: a reproducible 4.46x timing discontinuity at the 28 to 29 qubit transition on a fixed-bandwidth unified memory system. And DRAM's physical quirks are now a security surface in both directions, as an exploitable disturbance vulnerability and as a source of device-specific fingerprints usable as PUF responses.

**TLDR: DRAM bandwidth and capacity set the ceiling on AI inference economics, and the energy per fetch sets the power bill.**

## Timing Now (0-2yr)

The constraint is live now. Memory-bound decode, KV-cache growth and bandwidth contention between weights and caches are being addressed in production today, and the answer that has already shipped is software offload over commodity memory tiers integrated into mainstream serving stacks <sup class="ref"><a href="https://arxiv.org/abs/2510.09665" title="LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference" rel="noopener">ref</a></sup>. Interface and packaging changes are the next tranche: UCIe-attached LPDDR6 and HBM through a logic die is a proposal against HBM4 as the comparator, which places it on the current standards cycle rather than a research horizon.

**TLDR: DRAM is the current constraint and the current battleground; the extensions divide into shipping software, near-term packaging and longer-dated in-array computation.**

## Overrated or underrated? Fairly rated

The market has correctly identified that memory, not compute, is the constraint, and DRAM is priced accordingly. The quantification is unambiguous and has been for years: ~60,000x compute growth against ~100x DRAM bandwidth growth, with the underlying rates of 3.0x versus 1.6x every two years guaranteeing the gap keeps widening **2024 Gholami Ai And Memory Wall**. Nothing in these sources suggests DRAM is about to be displaced. The hybrid designs keep DRAM for what it is best at and add other media around it,.

Two things inside that consensus look mispriced. First, DRAM's reliability trajectory is underweighted. ColumnDisturb is described as fundamentally different from RowHammer and affects all cells across three consecutive subarrays, and it was discovered recently rather than being a known and bounded problem. If mitigation overhead grows with density, the effective bandwidth and capacity gains per node are smaller than the datasheet gains. Second, the assumption that value in the memory tier will be captured by novel silicon looks weaker than the assumption that it will be captured by software and packaging. Commodity software over commodity DRAM already delivered 15x throughput and shipped into four serving stacks <sup class="ref"><a href="https://arxiv.org/abs/2510.09665" title="LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference" rel="noopener">ref</a></sup>, while PIM remains a simulation-stage argument. Bet on the boundary of DRAM, not on replacing it.

## Prediction

Through end-2028, DRAM in one of its standard interface families (DDR, LPDDR, HBM or GDDR) remains the main-memory tier in every publicly documented production AI inference deployment, with ReRAM, MRAM and FeFET confined to research prototypes and edge co-design papers rather than displacing DRAM as the primary weight or KV-cache store.

## Evidence base

- Over twenty years peak hardware compute grew ~60,000x while DRAM bandwidth grew ~100x and interconnect bandwidth ~30x, with underlying rates of 3.0x, 1.6x and 1.4x every two years; an off-chip DRAM fetch costs ~1.3-2.6 nJ against sub-picojoule arithmetic (2024-03-21) **2024 Gholami Ai And Memory Wall**.
- Adding memory semantics to UCIe, reusing LPDDR6 or HBM behind a logic die or having the DRAM die speak UCIe natively, is claimed to give up to 10x higher bandwidth density, up to 3x lower latency and up to 3x lower power than HBM4 and existing on-package LPDDR (2025-10-07).
- Sangam decouples logic and DRAM into chiplets in heterogeneous nodes on an interposer with CXL attachment, on the argument that in-DRAM processing elements cost capacity and are limited by DRAM fabrication (2025-11-15).
- ColumnDisturb disturbs DRAM columns rather than rows and affects all cells across three consecutive subarrays; the first mitigations use two counters per subarray plus targeted refresh (2026-06-24).
- Characterisation of 112 DDR4 chips from 10 modules produced device-specific signatures via simultaneous multiple-row activation with average intra-Jaccard indices of 89.02% to 94.86% depending on the number of rows activated (2026-06-16).
- On Apple M4 Pro unified memory with ~224 GB/s LPDDR5X STREAM bandwidth, all quantum gate implementations showed arithmetic intensity at or below 0.38 FLOP/byte and a reproducible 4.46x timing discontinuity at the 28 to 29 qubit hierarchy transition (2026-05-09).

## Open questions

- How much performance and energy overhead do ColumnDisturb mitigations impose at the next density nodes, and does that overhead cancel the capacity gain that motivated the shrink?
- Do the claimed UCIe on-package memory advantages of up to 10x bandwidth density and 3x lower power survive silicon implementation and standardisation, or does HBM4 hold the socket?
- Can processing-using-DRAM be made deterministically correct on commercial chips given interference from non-activated rows and concurrently computing columns, or does it stay a research paradigm?
- Does any chiplet DRAM-PIM design reach production design-win volume, or is the retrieval and KV-cache tier permanently captured by software over commodity DRAM, CXL and SSD <sup class="ref"><a href="https://arxiv.org/abs/2510.09665" title="LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference" rel="noopener">ref</a></sup>?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
