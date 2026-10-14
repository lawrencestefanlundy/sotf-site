---
type: concept
slug: wafer-scale
canonical_name: Wafer Scale
aliases: []
parent_concepts:
- compute-architecture
- compute
related_concepts: []
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 18
frontier:
- What per-layer yield floor makes the "known good-enough" five-wafer stack economic, and what is the compound yield after five hybrid-bonded joins compared with a monolithic wafer-scale die?
- Has any of the five proposed functional wafers, in particular the dedicated cooling wafer and the optical IO wafer, been demonstrated in silicon rather than in a roadmap deck?
- Can hybrid bonding hold alignment and interconnect yield across a full 300 mm wafer pair when the two wafers come from different fabs on different processes, given differing thermal expansion and wafer bow?
- Does variability-tolerant design deliver measurable cost or performance advantage on a wafer-scale part, and can unsupervised variability models of the kind demonstrated on Hf0.5Zr0.5O2 predict device performance well enough to substitute for per-die test?
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-04-30-has-the-time-come-to-take-mortal
  title: Has the time come to take Mortal Computing seriously?
  date: '2025-04-30'
  kind: substack
neighbors: []
---
## Physics / mechanism

Wafer scale integration abandons the step of dicing a finished wafer into individual chips. Instead the reticle-stitched die array is kept intact and interconnected across scribe lines, so that inter-die communication happens over on-wafer metal rather than package substrate or board traces. The economic and physical trade is bandwidth and latency against yield: a single wafer contains defects that would normally be discarded with the bad die, so the architecture must tolerate dead cores, and it must supply power and remove heat over an area two orders of magnitude larger than a conventional package.

The declared next step at Cerebras moves from a monolithic Wafer Scale Engine to a heterogeneous stack of five full wafers, each fabricated on a process dedicated to its function and at a different fab: memory, power, compute, optical IO and cooling. Each wafer is finished, probed and sorted at its home fab on a "known good-enough" criterion that deliberately tolerates imperfect per-layer yield, then the wafers are joined as full wafers before dicing at a backend fab using Cu/SiO₂ redistribution layers and hybrid bonding between each pair. Dedicating whole wafers to power delivery and to cooling makes explicit that these are first-class architectural layers at this scale, not packaging afterthoughts.

Because a wafer-scale part cannot be binned die by die, process variability across the wafer becomes a design constraint rather than a test-and-sort problem. This is the same variability that limits high-volume manufacturing of emerging memories: ferroelectric Hf0.5Zr0.5O2 is attractive as embedded non-volatile memory for its CMOS back-end-of-line compatibility and scalability, but sensitive crystallisation kinetics produce significant device-to-device non-uniformity and unpredictable performance over wafer scale. Approaches to this split between suppressing variability and exploiting it: the "mortal computing" framing argues that the industry spends heavily on fungibility, with a 3 nm chip costing up to a billion dollars and a mask set alone $30-50 m, and that an alternative is to build devices that accept high variability instead of fighting it <sup class="ref"><a href="https://stateofthefuture.substack.com/p/has-the-time-come-to-take-mortal" title="Has the time come to take Mortal Computing seriously?" rel="noopener">ref</a></sup>.

## Competitive landscape

Thermal transport is the shared bottleneck across all high-density integration paths, and carbon nanotubes have been surveyed as a candidate material for datacentre thermal problems <sup class="ref"><a href="https://stateofthefuture.substack.com/p/carbon-nanotubes-in-the-datacentre" title="Carbon Nanotubes in the Datacentre" rel="noopener">ref</a></sup>.

## Evidence base

## Frontier (open questions)

*Synthesised 2026-08-31 from 6 KB sources by the resynth pipeline; citations are KB source slugs.*
