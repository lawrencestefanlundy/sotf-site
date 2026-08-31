---
type: concept
slug: inference
canonical_name: Inference
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
- kv-cache
frontier:
- Do shipped HBF stacks match HBM4 read bandwidth in measured decode workloads, or only in peak specification?
- What write endurance and write-latency limits does HBF impose on key-value cache updates, and do they force a hybrid HBM plus HBF memory tier?
- Did Sandisk HBF samples ship in H2 2026 and did inference-device samples follow in early 2027 as projected?
- What is the cost per token, not cost per GB, of HBF-based inference relative to an all-HBM baseline at equal model size?
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

Inference is the execution phase of a trained model: converting inputs into outputs (tokens) rather than updating weights. Its hardware demands differ from training in a way that the memory hierarchy makes explicit. The decode stage of autoregressive generation produces one token at a time, so each step must stream model weights and cached attention state past the arithmetic units with little opportunity to amortise those reads across a large batch. Throughput is therefore governed by memory read bandwidth and by how much state fits close to the accelerator, not primarily by peak floating-point rate.

That framing is what drives interest in near-package memory alternatives. High Bandwidth Flash (HBF) stacks NAND dies vertically, connects them with through-silicon vias, and places the stack next to the GPU on the package interposer, in the same topology used for HBM. The claimed result is read bandwidth comparable to an HBM4 stack with roughly ten times the capacity, because the medium is NAND rather than DRAM <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.

The key parameters for inference are consequently: read bandwidth per stack, capacity per stack, and the asymmetry of the storage medium. Flash carries tradeoffs relative to DRAM, and the argument advanced for HBF is that those tradeoffs are tolerable specifically for inference decode workloads, which are read-dominated <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>. Capacity matters because larger resident weight sets and longer key-value caches otherwise force model sharding across more accelerators or eviction to slower tiers.

## Competitive landscape

The relevant comparison for inference memory is HBM versus HBF. HBM (DRAM) offers symmetric read and write behaviour and is the incumbent for both training and inference; HBF (NAND) targets the read-heavy decode path, trading DRAM's write characteristics for roughly an order of magnitude more capacity at similar read bandwidth <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>. The sources do not support a comparison across accelerator architectures, quantisation approaches, or serving-software strategies, all of which also bear on inference cost.

## Evidence base

- HBF is described as a stack of NAND dies built the way an HBM stack is built, with TSVs, sitting next to the GPU on the package interposer <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.
- HBF is claimed to have the same read bandwidth as an HBM4 stack with roughly 10x the capacity, as of 7 July 2026 <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.
- First samples of HBF memory were expected from Sandisk in the second half of 2026 <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.
- Samples of the first AI inference devices built with HBF were expected in early 2027 <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.
- Flash tradeoffs are argued to be acceptable specifically for inference decode workloads rather than for inference generally <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.

## Frontier (open questions)

- Do shipped HBF stacks match HBM4 read bandwidth in measured decode workloads, or only in peak specification?
- What write endurance and write-latency limits does HBF impose on key-value cache updates, and do they force a hybrid HBM plus HBF memory tier?
- Did Sandisk HBF samples ship in H2 2026 and did inference-device samples follow in early 2027 as projected?
- What is the cost per token, not cost per GB, of HBF-based inference relative to an all-HBM baseline at equal model size?

*Synthesised 2026-08-31 from 2 KB sources by the resynth pipeline; citations are KB source slugs.*
