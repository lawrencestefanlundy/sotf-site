---
type: concept
slug: non-volatile-memory
canonical_name: Non Volatile Memory
aliases: []
parent_concepts:
- mainstream-memory
- memory
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
frontier:
- What are the measured write bandwidth, write latency and program/erase endurance figures for a package-attached NAND stack under sustained inference serving, and do they hold over a multi-year deployment?
- Does the claimed parity with HBM4 read bandwidth survive independent measurement on shipping silicon, and at what stack-level power per bit read?
- What cost per gigabyte does a TSV-stacked NAND assembly achieve after packaging yield losses, relative to both standard NAND packages and HBM?
- Which workloads beyond inference decode, if any, tolerate the read/write asymmetry of non-volatile memory placed on the interposer?
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

Non-volatile memory retains stored data without a continuously applied supply voltage, which distinguishes it from DRAM. In current mainstream practice the dominant non-volatile technology is NAND flash, which the sources characterise as the inexpensive tier of the memory hierarchy relative to DRAM <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.

The available source treats non-volatile memory at the package and system level rather than the cell level. Its central example is High Bandwidth Flash (HBF), in which NAND dies are stacked vertically, interconnected with through-silicon vias (TSVs), and placed on the same package interposer as a GPU, i.e. the assembly method used for HBM but with NAND rather than DRAM dies <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>. The claimed result is read bandwidth matching an HBM4 stack at roughly ten times the capacity <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.

The key parameters implied by this framing are read bandwidth, capacity per stack, cost per bit, and the asymmetry between read and write behaviour. The source states that flash carries tradeoffs, and argues these tradeoffs are tolerable specifically for AI inference decode workloads, which are read-dominated <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>. No cell-level endurance, retention or programming detail is present in the supplied material.

## Competitive landscape

Within package-attached memory, the comparison in the sources is NAND-based non-volatile memory against DRAM-based HBM. HBM offers the bandwidth baseline; HBF is presented as matching HBM4 read bandwidth while delivering approximately 10x capacity at NAND cost structures, with workload-dependent tradeoffs on the write and latency side <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>. The supplied material does not compare NAND against emerging non-volatile candidates such as resistive, magnetic or phase-change memories, so no position can be established for those here.

## Evidence base

- HBF stacks NAND dies vertically with TSVs and places the stack next to the GPU on the package interposer, mirroring HBM construction <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.
- HBF is claimed to have the same read bandwidth as an HBM4 stack with roughly 10x the capacity, using NAND rather than DRAM <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.
- First samples of HBF memory were expected from Sandisk in the second half of 2026 <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.
- Samples of the first AI inference devices built with HBF were expected in early 2027 <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.
- The source frames flash tradeoffs as acceptable specifically for inference decode workloads rather than for general-purpose memory duty <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.

## Frontier (open questions)

- What are the measured write bandwidth, write latency and program/erase endurance figures for a package-attached NAND stack under sustained inference serving, and do they hold over a multi-year deployment?
- Does the claimed parity with HBM4 read bandwidth survive independent measurement on shipping silicon, and at what stack-level power per bit read?
- What cost per gigabyte does a TSV-stacked NAND assembly achieve after packaging yield losses, relative to both standard NAND packages and HBM?
- Which workloads beyond inference decode, if any, tolerate the read/write asymmetry of non-volatile memory placed on the interposer?

*Synthesised 2026-08-31 from 1 KB sources by the resynth pipeline; citations are KB source slugs.*
