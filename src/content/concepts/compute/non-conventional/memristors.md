---
type: concept
slug: memristors
canonical_name: Memristors
aliases: []
kind: material
parent_concepts:
- compute
- non-conventional
related_concepts: []
sources:
- '[[2026-08-07-the-memory-trade-isnt-over-weights]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
frontier:
- Can filament formation be made deterministic enough for uniform multi-level analogue weights, given that as of 2026 charge transport is dominated by a small number of discrete filaments rather than uniform conduction 2026 05 05 investigation of filamentation in a siagcu memristors with a?
- How do the read/write and soft error mitigations for ReRAM and STT-RAM trade off in area and energy once applied at array scale, and does the density advantage over SRAM survive them 2026 06 18 nanoscale memristive devices threats and solutions?
- Does any memristive implementation beat a digital CMOS baseline on energy per inference for the same task, a comparison absent from the current sources?
- Do the CMOS-compatible integration routes, BEOL VO2 below 430 C and foundry photonic MEMS, reach production yields, or remain single-die demonstrations 2026 07 23 monolithically integrated vo2 mott oscillators for energy ef 2026 07 27 micro electromechanical photonic integrated memristors?
last_updated: '2026-08-31'
tags:
- concept
- material
mention_count: 19
last_reorg_date: '2026-05-14'
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Later (5-10yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 3
recent_mentions:
- slug: 2026-08-07-the-memory-trade-isnt-over-weights
  title: 'The Memory Trade Isn''t Over: Weights and KV Cache'
  date: '2026-08-07'
  kind: substack
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
neighbors: []
---
**Memristors are two-terminal devices whose resistance retains a memory of past electrical stimulus, offering dense non-volatile memory and analogue in-memory computing, but the 2026 literature is still resolving the stochastic switching physics that limits array-level reliability.**

## Summary

A memristor is a two-terminal element whose conductance depends on the history of the voltage or current applied to it, and holds that state without power. Placed at the crosspoints of a crossbar array, such devices store weights where the computation happens, so a matrix-vector multiply becomes a single analogue read of currents rather than a stream of data movements between memory and logic. That is the whole commercial argument: non-volatility, low leakage and higher density than SRAM, plus the option of doing multiply-accumulate in place. Its relevance to AI hardware is the memory bottleneck rather than raw arithmetic <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e14-the-real-ai-bottleneck-high-bandwidth" title="🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM) " rel="noopener">ref</a></sup>.

The honest reading of this source set is a field that has working devices in many material systems and is simultaneously still writing papers to establish what physically happens during a switching event.

## Viability (3/5)

The positive evidence is real and recent. Non-volatile, quasi-analogue switching down to nanosecond pulses has been shown in MgO magnetic tunnel junctions; Ta2O5 memristors have run time-series prediction tasks as a reservoir layer; VO2 spiking neurons have been monolithically integrated in the back end of line on a CMOS-compatible platform; and a photonic memristor with up to 5-bit phase storage and 50 kbit/s programming was produced in a CMOS foundry. Large-scale memristor arrays are described as having been successfully implemented.

**TLDR: Devices work and large arrays have been built, but stochastic switching and unresolved mechanisms keep reliability an open engineering problem.**

## Drivers (3/5)

On supply, the source set shows unusually wide activity: filamentary oxides, ECM silicon, Mott oxides, magnetic tunnel junctions, ionic nanofluidics in silicon nanopores and clay membranes, photonic MEMS, and intrinsic bistability engineered into a two-dimensional semiconductor without any filament at all. Several groups are moving from device demonstration to mechanism, including kinetic Monte Carlo and molecular dynamics with dynamic charge transfer, and public instrumentation funding continues to underwrite the underlying materials measurement capability.

On demand, the stated pull is that CMOS-based memories face functional challenges in deep submicron nodes, making non-volatile, low-leakage, dense memristors a candidate replacement for SRAM-class memory, plus the broader argument that memory bandwidth, not compute, is the binding constraint on modern AI systems <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e14-the-real-ai-bottleneck-high-bandwidth" title="🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM) " rel="noopener">ref</a></sup>. What the sources do not provide is any market size, shipment volume, design-win or roadmap commitment from a manufacturer. The demand case here is inferred from technical framing rather than demonstrated procurement, which caps this at 3.

**TLDR: Supply-side research is broad and active across many material platforms; demand is stated as CMOS memory scaling limits and the AI memory bottleneck, but the sources quantify neither.**

## Novelty (3/5)

The comparison the sources actually make is against CMOS memory: memristors are non-volatile, have low leakage and are dense relative to SRAM, with ReRAM and STT-RAM leading on process maturity, memory operation energy, latency and area. Within memristor variants there are quantified improvements: doping the oxide barrier of an MgO magnetic tunnel junction lowered memristive power consumption by 20 per cent while retaining linear, hysteresis-free magnetoresistance suitable for field sensing in the same device. The photonic MEMS memristor is explicitly positioned against existing optical memristors on durability, material-induced optical loss, large-scale reconfigurability and fabrication yield, and achieves 5-bit phase storage using only low-loss silicon nitride waveguides with no additional back-end materials. The VO2 work replaces discrete-component neuristors with a monolithic 1T-1MR cell, addressing integration density directly.

**TLDR: Clear functional advantage over SRAM on non-volatility, leakage and density, and credible efficiency claims for in-memory work, but almost no head-to-head numbers against digital baselines.**

## Diffusion (2/5)

**TLDR: Variability, reliability engineering and new security exposure stand between working devices and deployed systems; CMOS-compatible integration is the one barrier being visibly cleared.**

## Impact (3/5)

The upside case is structural. If weights can be stored non-volatilely at density and read at the point of computation, the data movement that dominates AI system cost is reduced rather than merely accelerated, and the sources frame memory, not compute, as the real constraint <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e14-the-real-ai-bottleneck-high-bandwidth" title="🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM) " rel="noopener">ref</a></sup>. Beyond accelerators, memristive parts could replace CMOS memories that are struggling at deep submicron nodes, support brain-inspired non-Boolean computing and sensing that is energy-efficient, error-tolerant and highly parallel, enable in-memory optical multiply-accumulate with readout at the speed of light, and open ionic computing circuits as a separate application family. Multifunctional devices that combine sensing and reprogrammable memory in one stack are an additional route to system-level value.

The restraint is that none of this is quantified in the supplied material. There is no joules-per-operation comparison, no array-level accuracy figure on a real workload, and no cost model. The clearest measured system result is a reservoir computing benchmark solved with two to six memristive channels, which is impressive as a demonstration of dynamical richness but is not a datacentre-scale claim. A 3 reflects a plausible large payoff with the magnitude unevidenced here.

**TLDR: Large in principle, since it attacks the memory bottleneck rather than arithmetic throughput, but the sources assert the value qualitatively rather than measuring it.**

## Timing Later (5-10yr)

Two clocks run at different speeds. As memory, ReRAM and STT-RAM are described as the process-mature options with competitive energy, latency and area, and the outstanding work is reliability engineering rather than physics. That is a nearer-term proposition. As a compute substrate, the 2026 papers are still establishing what governs filament morphology, how metal cations migrate in Ta/HfO2/Pt, and how filaments are spatially distributed in a device.

The integration milestones dated 2026, monolithic BEOL VO2 neurons and foundry-made photonic memristors, are first demonstrations rather than qualified processes. On this evidence, meaningful deployment of memristive analogue compute in commercial systems belongs in the five to ten year band, with embedded non-volatile memory arriving earlier and nanofluidic or ionic variants later still.

**TLDR: ReRAM and STT-RAM as memory are the near-term path; analogue memristive compute is still fighting basic variability and mechanism questions as of mid-2026.**

## Overrated or underrated? Fairly rated

## Prediction

## Evidence base

## Open questions

- Can filament formation be made deterministic enough for uniform multi-level analogue weights, given that as of 2026 charge transport is dominated by a small number of discrete filaments rather than uniform conduction?
- How do the read/write and soft error mitigations for ReRAM and STT-RAM trade off in area and energy once applied at array scale, and does the density advantage over SRAM survive them?
- Does any memristive implementation beat a digital CMOS baseline on energy per inference for the same task, a comparison absent from the current sources?
- Do the CMOS-compatible integration routes, BEOL VO2 below 430 C and foundry photonic MEMS, reach production yields, or remain single-die demonstrations?

---
*Assessment drafted 2026-08-31 from up to 14 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
