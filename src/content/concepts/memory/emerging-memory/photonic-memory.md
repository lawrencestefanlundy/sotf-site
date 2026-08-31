---
type: concept
slug: photonic-memory
canonical_name: Photonic Memory
aliases:
- optical memory
- optical data storage
kind: technology
parent_concepts:
- memory
- emerging-memory
related_concepts: []
sources:
- '[[2023-07-14-e08-optical-computing]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2025-02-25-data-driven-vc-is-over]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2026-06-01-hbm-state-of-play]]'
- '[[2026-04-29-optical-dram-everspin-reports-q1-2026-financial-results]]'
- '[[2026-04-20-optical-dram-photonic-memory-device-technology-2026-patsnap]]'
- '[[2026-05-07-optical-dram-startup-funding-q1-2026]]'
scorecard:
  viability: 2
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Later (5-10yr)
  verdict: Overrated
scorecard_status: draft
mention_count: 81
sources_7d: 1
sources_30d: 6
recent_mentions:
- slug: 2026-06-01-hbm-state-of-play
  title: HBM state of play (mid-2026) — technology, supercycle, three-supplier standing
  date: '2026-06-01'
  kind: web
- slug: 2026-05-07-optical-dram-startup-funding-q1-2026
  title: 'Startup Funding: Q1 2026'
  date: '2026-05-07'
  kind: web
- slug: 2026-04-29-optical-dram-everspin-reports-q1-2026-financial-results
  title: Everspin Reports Q1 2026 Financial Results
  date: '2026-04-29'
  kind: web
- slug: 2026-04-20-optical-dram-photonic-memory-device-technology-2026-patsnap
  title: Photonic Memory Device Technology 2026 — PatSnap Eureka
  date: '2026-04-20'
  kind: web
- slug: 2025-12-19-lfg-for-semiconductors
  title: LFG (for semiconductors)
  date: '2025-12-19'
  kind: substack
- slug: 2025-04-16-the-state-of-photonic-computing
  title: 'Photonic Computing: A Primer'
  date: '2025-04-16'
  kind: substack
- slug: 2025-02-25-data-driven-vc-is-over
  title: data-driven VC is over
  date: '2025-02-25'
  kind: substack
- slug: 2023-07-14-e08-optical-computing
  title: '🔮E08: Optical Computing'
  date: '2023-07-14'
  kind: substack
neighbors: []
---
**Photonic memory is the attempt to hold information in, or addressably alongside, light rather than in charge on a transistor, and it matters because the absence of a good one is the standing reason photonic computers still have to convert back to electronics.**

## Summary

Light is an excellent carrier of information and a terrible container for it. A photon in a waveguide does not sit still, so any "photonic memory" has to do one of four quite different things: recirculate the light (delay lines, mirror cavities), park it in an atomic ensemble and retrieve it later, freeze it into a material state that light can subsequently read (phase-change alloys, implanted colour centres, magnetic domains), or exploit nonlinear feedback so an optical cavity settles into one of several stable states. The label covers all four, and they share almost nothing but the word.

The benchmark to beat is unforgiving. HBM3E already delivers around 1.2 TB/s per stack at roughly 3-4 pJ/bit, HBM4 doubles the bus to 2,048 bits for 2.0-3.3 TB/s, and the market was around $35B in 2025 heading for a claimed $100B TAM by 2028. Nothing in the photonic memory literature is currently quoted against those numbers, which is itself informative.

## Viability (2/5)

The obstacles named in the sources are physical, not engineering slippage: the diffraction limit on density, thermal accumulation during high-speed writing, the scalability ceiling of point-by-point laser writing, and the extinction coefficient of crystalline GST making arrays lossy. Two of these now have credible routes around them. None has been closed in a fabricated, characterised array. A 2 rather than a 3 because no source shows a rewritable photonic memory with quoted retention, endurance and energy per bit.

**TLDR: Real demonstrations exist, but each is either simulated, millisecond-scale, or write-once at lithography cost.**

## Drivers (3/5)

On demand, the case is strong and comes from two directions. Archival: global data generation growth is the stated motivation for chip-fabricated optical storage, on capacity, lifespan and energy grounds. Compute: the entire photonic accelerator thesis is memory-bound, which is the explicit argument of the photonic computing primer, subtitled "All You Need Is Memory" <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup>, and the surrounding market is a DRAM supercycle where HBM already represents roughly a third of DRAM value. Quantum networking adds a third, smaller pull, where a physical memory module is a named component of repeater architectures spanning 1,000 km at 9 km spacing.

On supply, capital is arriving but not addressed to this category. Olix raised a $220M Series A for an optical tensor processing unit with integrated memory <sup class="ref"><a href="https://semiengineering.com/startup-funding-q1-2026/" title="Startup Funding: Q1 2026" rel="noopener">ref</a></sup>: memory as a subsystem of a compute product. The incumbent alternative in non-volatile embedded memory is meanwhile converting, with Everspin reporting 238 MRAM design wins in 2025 ramping to production <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/0001438423/000162828026028376/mram-20260331xexx991.htm" title="Everspin Reports Q1 2026 Financial Results" rel="noopener">ref</a></sup>. Fabrication supply is a mild positive, since the highest-density approach deliberately reuses EBL and ion implantation rather than requiring new tooling. The sources say nothing about foundry PDK support for photonic PCM cells, which is the supply question that actually matters for the compute branch.

**TLDR: Demand pull from the AI memory wall is real; supply-side funding flows to compute boxes with memory inside, not to memory.**

## Novelty (3/5)

**TLDR: Clear, quantified gains over prior photonic approaches; no quoted comparison against electronic memory anywhere in the sources.**

## Diffusion (2/5)

Three barriers dominate. First, loss: every cell in an optical path eats signal, which is precisely why the GST array problem is described as serious rather than incremental. This caps array depth in a way that has no electronic analogue and forces photonic memory into small, shallow, co-packaged roles. Second, write throughput and reversibility: the densest demonstrated medium is written by electron-beam lithography, which confines it to cold archival mastering rather than any read/write tier. Third, ecosystem: HBM rides CoWoS with lead times of 50-104 weeks and Nvidia booking around 55% of 2026 capacity, a packaging and qualification pipeline that a new memory physics does not enter casually.

The likely diffusion path is therefore capture rather than substitution. An optical TPU with integrated memory raising $220M <sup class="ref"><a href="https://semiengineering.com/startup-funding-q1-2026/" title="Startup Funding: Q1 2026" rel="noopener">ref</a></sup> and an MRAM incumbent booking 238 design wins into production <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/0001438423/000162828026028376/mram-20260331xexx991.htm" title="Everspin Reports Q1 2026 Financial Results" rel="noopener">ref</a></sup> are the two shapes this takes: memory as a feature of a photonic accelerator, or the emerging-memory socket already filled by a shipping electronic alternative. The quantum-networking branch diffuses on a separate and slower clock tied to repeater deployment. Loose labelling does not help: at least one source tagged to this concept is a photonic quantum processor used to seed a generative model for peptide design, with no memory content at all.

**TLDR: Loss budgets, write throughput and an entrenched HBM ecosystem mean this diffuses inside other products or not at all.**

## Impact (4/5)

The value is leveraged rather than direct. Photonic computing's advantage is speed and energy in the linear-algebra path, and its recurring defeat is that weights and intermediate results must be held somewhere electronic, imposing conversion cost and latency; the framing that memory is the whole problem is the central claim of the primer literature <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup> and sits behind the longer-running question of whether electronics are a path dependency or a permanent optimum <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e08-optical-computing" title="🔮E08: Optical Computing" rel="noopener">ref</a></sup>. A low-loss, multilevel, non-volatile cell that can be programmed by direct laser writing and stacked into a tensor core array does not incrementally improve a photonic accelerator; it is the difference between a demo and a product.

The two adjacent payoffs are meaningful in their own right. High-capacity, long-lifespan, low-energy archival storage addresses a data-growth problem that current media are stated not to meet, and a workable photonic memory module is load-bearing for repeater chains that would carry entanglement over 1,000 km. Not a 5, because the sources give no evidence that photonic memory displaces the mainstream DRAM or HBM tier, where the money currently is; the impact is on enabling other things, not on replacing the incumbent.

**TLDR: It is the named blocker on photonic computing; solving it unlocks a category, and archival and quantum networking are bonuses.**

## Timing Later (5-10yr)

The nearest-term deliverable is a fabricated Sb2Se3 mode-converter array demonstrating in hardware the 32 levels currently shown in simulation; that is a two-to-four year item and it would arrive inside a photonic accelerator, following the pattern of an optical TPU with integrated memory <sup class="ref"><a href="https://semiengineering.com/startup-funding-q1-2026/" title="Startup Funding: Q1 2026" rel="noopener">ref</a></sup>. Archival optical storage has a working chip-scale write and multiplexed read today but needs a write economics story before pilots.

**TLDR: Fabricated multilevel arrays and archival pilots plausibly this decade; anything competing with an electronic memory tier is beyond it.**

## Overrated or underrated? Overrated

The value capture argument compounds the timing one. Money went to a photonic compute box with memory inside <sup class="ref"><a href="https://semiengineering.com/startup-funding-q1-2026/" title="Startup Funding: Q1 2026" rel="noopener">ref</a></sup>, while the socket a non-volatile emerging memory would occupy is being taken by an incumbent shipping into 238 design wins <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/0001438423/000162828026028376/mram-20260331xexx991.htm" title="Everspin Reports Q1 2026 Financial Results" rel="noopener">ref</a></sup>. Expect photonic memory to matter as a component of photonic accelerators and, separately, as an archival medium, and expect very little of it to be owned by companies named after it. The underrated part is narrow: the loss budget of the storage cell, not the memory concept, is what determines whether photonic tensor cores ever scale.

## Prediction

## Evidence base

## Open questions

- Does a fabricated Sb2Se3 programmable mode converter array reproduce the simulated 5-bit, 32-level programming, and what is the measured insertion loss per cell and the resulting maximum array depth?
- What are the write energy, write throughput and endurance of any photonic memory cell, expressed per bit, so it can be set against the 3-4 pJ/bit of HBM?
- Can the EBL-plus-ion-implantation storage medium be rewritten, or is its addressable market permanently cold archival?
- Does any foundry offer a qualified PCM photonic memory cell in a PIC process design kit, and on what schedule?

---
*Assessment drafted 2026-08-31 from up to 16 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
