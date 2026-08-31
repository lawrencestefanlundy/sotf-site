---
type: concept
slug: mainstream-memory
canonical_name: Mainstream Memory
aliases: []
parent_concepts: []
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
descendants:
- 3d-dram
- adc-bottleneck
- agentic-workload-retrieval
- analog-in-memory-compute
- capram
- charge-domain-compute
- computational-storage
- cxl
- digital-in-memory-compute
- dram
- embedded-non-volatile-memory
- fefet
- feram
- hbm
- in-memory-computing
- inference-economics
- memcapacitor
- memory
- memory-wall
- mram
- nand-flash
- near-memory-compute
- pcm-phase-change-memory
- photonic-memory
- processing-in-memory
- rram-reram
- sram
- sram-cim
- storage-class-memory
- token-cost-stack
frontier:
- What are HBF's write bandwidth, write latency and programme/erase endurance, and do they permit KV-cache or weight-update traffic or only static weight residency?
- What is the measured read latency of an HBF stack relative to an HBM4 stack, and how much of it can be hidden in decode pipelines?
- What is the cost per bit and power per bit of an HBF stack versus HBM4 at equal read bandwidth, once TSV stacking yield is accounted for?
- Do the H2 2026 Sandisk memory samples and the early 2027 inference device samples arrive on schedule, and do measured parts hit the claimed HBM4-equivalent read bandwidth?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-07-high-bandwidth-flash-the-full-report
  title: 'High Bandwidth Flash: The Full Report'
  date: '2026-07-07'
  kind: web
neighbors: []
---
## Physics / mechanism

Mainstream memory covers the two commodity semiconductor storage classes in volume production: DRAM, which holds a bit as charge on a capacitor and must be refreshed, and NAND flash, which stores charge on a floating gate or charge-trap layer and retains it without power. The available sources address this category through one specific development at the boundary between the two: High Bandwidth Flash (HBF), which applies the packaging techniques of High Bandwidth Memory to NAND dies rather than DRAM dies <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.

The construction is the same as an HBM stack. Dies are stacked vertically, connected with through-silicon vias (TSVs), and the resulting stack is placed on the package interposer immediately adjacent to the GPU <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>. Bandwidth in this arrangement comes from the very wide, short parallel interface that TSV stacking and interposer proximity permit, not from raising the per-pin signalling rate.

The stated performance point is read bandwidth equal to an HBM4 stack with roughly 10x the capacity, achieved because NAND is the cheaper and denser of the two mainstream memory types <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>. The trade-offs of flash relative to DRAM are described as tolerable specifically for inference decode workloads, which are read-dominated <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>; the source does not quantify write bandwidth, latency or endurance.

## Competitive landscape

The comparison the source supports is between two ways of packaging mainstream memory next to an accelerator. HBM4 uses DRAM dies, and an HBF stack matches its read bandwidth while offering around 10x the capacity at NAND cost <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>. This positions HBF as a capacity tier rather than an HBM replacement, since the flash trade-offs are argued to be acceptable only for particular workload shapes, notably inference decode <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>. No pricing, power or endurance figures are given in the available material, so the cost-per-bit and total-cost-of-ownership comparison remains unquantified here.

## Evidence base

- HBF is a stack of NAND dies built the way an HBM stack is built: vertical stacking, TSV interconnect, mounted on the package interposer next to the GPU <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.
- HBF is stated to have the same read bandwidth as an HBM4 stack with roughly 10x the capacity <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.
- First samples of HBF memory are expected from Sandisk in the second half of 2026 <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.
- Samples of the first AI inference devices built with HBF are expected in early 2027 <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.
- The flash trade-offs are characterised as manageable for inference decode workloads specifically, rather than for memory workloads in general <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.

## Frontier (open questions)

- What are HBF's write bandwidth, write latency and programme/erase endurance, and do they permit KV-cache or weight-update traffic or only static weight residency?
- What is the measured read latency of an HBF stack relative to an HBM4 stack, and how much of it can be hidden in decode pipelines?
- What is the cost per bit and power per bit of an HBF stack versus HBM4 at equal read bandwidth, once TSV stacking yield is accounted for?
- Do the H2 2026 Sandisk memory samples and the early 2027 inference device samples arrive on schedule, and do measured parts hit the claimed HBM4-equivalent read bandwidth?

*Synthesised 2026-08-31 from 1 KB sources by the resynth pipeline; citations are KB source slugs.*
