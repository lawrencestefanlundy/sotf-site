---
type: concept
slug: waveguides
canonical_name: Waveguides
aliases: []
parent_concepts:
- pic-platforms
- photonic-systems
related_concepts: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2026-04-17-state-of-the-future-friday-four-67c]]'
- '[[2026-04-14-the-photonic-foundry-fallacy]]'
- '[[2026-07-07-the-asml-killer]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-07-10-the-next-vc-meme-is]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 158
scorecard:
  viability: 5
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
frontier:
- Does slab-engineered crosstalk cancellation survive real fabrication tolerance, temperature and wavelength ranges across a full reticle, or is the demonstrated zero-crosstalk condition too narrow to become a design rule 2026 05 28 universal zero crosstalk photonic integration via slab engin?
- Can the PLACE isotropic-etch route to low-loss 1.2 cm PPLN be run at wafer scale and with the yield a foundry needs, or does it stay a laboratory process 2026 05 28 isotropic fabrication of centimeter scale low propagation lo?
- How far below dB/cm can visible-band lithium tantalate loss be pushed while keeping the 5 dBm power stability advantage over lithium niobate, and does that advantage hold at higher powers 2026 05 14 robust and active visible light integrated photonics on thin?
- What pump power and waveguide length does the cavity-less comb architecture actually require to beat a microresonator on total system efficiency, given the resonator's inherently lower threshold 2026 05 28 a cavity less architecture for high power integrated frequen?
sources_7d: 1
sources_30d: 9
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-10-the-next-vc-meme-is
  title: The Next VC Meme Is...
  date: '2026-07-10'
  kind: substack
- slug: 2026-07-07-the-asml-killer
  title: The ASML Killer?
  date: '2026-07-07'
  kind: substack
- slug: 2026-07-02-semianalysis-ectc2026-advanced-packaging
  title: 'ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More'
  date: '2026-07-02'
  kind: web
- slug: 2026-06-16-trapped-ion-landscape-2026
  title: Trapped-ion quantum computing landscape 2026 (vendors, scale, integrated photonics)
  date: '2026-06-16'
  kind: web
- slug: 2026-06-15-barry-silverstein-rochester-cxr
  title: University of Rochester hires former Meta exec Barry Silverstein to direct Center for Extended Reality
  date: '2026-06-15'
  kind: web
- slug: 2026-06-04-q-memory-site
  title: Q-Memory — company website (q-memory.tech)
  date: '2026-06-04'
  kind: web
- slug: 2026-05-25-ai-glasses-display-timing-waveguide-display-technology
  title: Waveguide Display Technology Trends and Outlook 2026
  date: '2026-05-25'
  kind: web
neighbors: []
---
**A waveguide is the basic wire of integrated photonics, a channel that confines light (or spin waves, or microwaves) by refractive-index or material contrast, and the current research frontier is no longer whether it works but which material platform, loss figure and crosstalk pitch you can get out of a foundry.**

## Summary

A waveguide is a structure that confines an electromagnetic wave to a cross-section much smaller than free-space propagation would allow and carries it along a defined path. In photonic integrated circuits (PICs) this is usually a high-index core (silicon, silicon nitride, lithium niobate, lithium tantalate) patterned on a lower-index cladding, either as a fully etched strip or as a rib sitting on a residual slab. Everything else on a PIC, modulators, splitters, resonators, delay lines, detectors, is built by locally perturbing a waveguide or by coupling two of them together. The same physics is being reused outside optics: spin-wave waveguides written directly into yttrium iron garnet carry magnons for on-chip microwave processing, and dielectric waveguides feeding movable "pinching" antennas are being proposed as a base-station radio architecture.

The parameters that decide a waveguide are few and unforgiving. Propagation loss in dB/cm sets how long a device can be and therefore how much nonlinear or electro-optic interaction you can accumulate; anisotropic etching of lithium niobate has historically pinned fully poled PPLN waveguides at a few dB/cm, and an isotropic process that poles the planar film before defining the guide has now produced a 1.2 cm low-loss PPLN waveguide. Mode confinement sets how tightly you can bend and how strongly an overlaid material (graphene, an exciton layer, a quantum dot) interacts with the field. Dispersion engineering decides whether a plain waveguide can replace a resonator for comb generation. Crosstalk between neighbouring guides sets the pitch, and therefore the integration density of the whole chip. Material choice sets the wavelength band and the power handling: thin-film lithium tantalate waveguides and modulators at 532 nm survived 5 dBm of modulated optical power for an hour where equivalent thin-film lithium niobate structures did not.

A second, more speculative use of waveguides is as a physics substrate rather than a wire. Arrays of coupled waveguides implement tight-binding lattices in which light propagating along the array plays the role of time evolution, and this has been used to observe Anderson localisation of single photons from a room-temperature hexagonal boron nitride emitter and end-to-end topological pumping in a quasiperiodic Fibonacci chain. Structured waveguides give access to chirality and topology: glide-plane photonic-crystal slow-light waveguides show electrically switchable chiral light-matter coupling, valley photonic crystal edge states transport optical spin skyrmions directionally, and time-modulated metasurface waveguides open intermodal momentum band gaps that permit directional amplification. These two uses have very different maturity and should be assessed separately.

## Viability (5/5)

The sources contain working hardware, not proposals: a 1.2 cm PPLN nanophotonic waveguide with low propagation loss and uniform poling; visible-band lithium tantalate waveguides at dB/cm-scale loss driving 112 Gb/s over a 3 m underwater link and 64 Gb/s over 9 m; experimentally measured zero crosstalk between adjacent rib waveguides across silicon-on-insulator and silicon nitride; a monolithic imaging chip combining waveguides, splitters, delay lines and 3D remappers that reconstructs images of cells in flow; and comb generation in dispersion-engineered waveguides without any cavity. Waveguide arrays are routine enough to serve as experimental testbeds for condensed-matter physics.

The caveat is that viability is uneven across the sub-branches. Cryogenic graphene phase modulators on silicon nitride are a theoretical and simulation study only, the giant-atom state transfer scheme is analytical, and photonic time crystals in metasurface waveguides are theory. The score reflects the waveguide as a component, not the exotic functions layered on it.

**TLDR: The core primitive is demonstrated repeatedly and at system level, not simulated.**

## Drivers (4/5)

On supply, the binding constraint named repeatedly is process. Existing crosstalk-suppression strategies are described as relying on specialised nanostructures or platform-specific designs that hinder adoption in standard foundry processes, which is exactly why a slab-thickness-only solution matters. Likewise, PPLN performance was limited by an etching anisotropy problem rather than by physics, and the magnonic mesh result is framed around a single-step direct laser writing process. The sources contain no market-size, capacity or investment data, so the demand side is inferred from stated application targets rather than measured.

**TLDR: Demand from optical computing, quantum and short-reach links is explicit; supply is gated by foundry process compatibility.**

## Novelty (3/5)

Nothing here claims the waveguide is new. What is new is measurable against named baselines. Slab-engineered mode hybridisation cancels coupling between adjacent standard rib waveguides using only slab thickness, and is better than the incumbent because the incumbent required specialised nanostructures or platform-specific designs; the claim is universality across silicon-on-insulator and silicon nitride. Isotropic PPLN fabrication is better than anisotropic etching, which had pinned fully domain-inverted waveguides at a few dB/cm, and it delivers 1.2 cm of usable length. Lithium tantalate at 532 nm is better than thin-film lithium niobate specifically on stability, holding 5 dBm modulated output for an hour where the niobate counterpart could not, with flat response to about 50 GHz. Cavity-less combs are better than microresonator combs on pump-to-comb conversion efficiency, line-spacing tunability and power per line, at the cost of the resonator's low power threshold.

The more novel material and structural work is earlier stage. NbOI2 van der Waals waveguides show giant optical spin splitting via the optical spin Hall effect but propagation is imaged over tens of micrometres. Magnonic waveguides preserve phase coherence for hundreds of wavelengths and show complete periodic power transfer in coupled pairs, moving magnonics past isolated elements to cascaded programmable networks. The sources do not quantify how these compare with the electronic or photonic incumbents they would replace, so the novelty score is anchored on the incremental but well-benchmarked photonic results.

**TLDR: The waveguide itself is old; the 2026 increments are real but bounded, and each is better than a specific named incumbent.**

## Diffusion (3/5)

The adoption barrier is stated plainly in the sources: crosstalk-suppression methods that depend on specialised nanostructures or one particular material system do not travel into standard foundry processes, and the value claimed for the slab-engineering route is precisely that it is foundry-compatible and demonstrated across several material platforms including silicon-on-insulator and silicon nitride. That is the right shape for fast diffusion, because it is a design-rule change rather than a new process module. Against that, other advances here carry process baggage: femtosecond-laser photolithography-assisted chemo-mechanical etching for PPLN, direct laser writing in yttrium iron garnet, exfoliated ferroelectric van der Waals slabs, and cryogenic operation for graphene modulators.

The honest limit on this score is that the sources are all research papers. There is no data on foundry PDK availability, volumes, yields, cost per die or customer adoption, and no company is named. The score of 3 reflects a credible but unmeasured diffusion path: platform-agnostic design fixes should spread quickly, new material platforms slowly, and the sources do not let anyone put a rate on either.

**TLDR: Foundry compatibility is explicitly the gate, and one result clears it; deployment evidence is absent from the sources.**

## Impact (4/5)

Impact follows from position in the stack. Crosstalk accumulating across cascaded components is described as fundamentally degrading signal fidelity, limiting system-level performance and constraining integration density; removing that constraint changes how large a photonic processor or quantum circuit can be, not just how one component performs. Waveguide loss is the direct multiplier on nonlinear conversion efficiency and on the achievable scale of photonic integration in PPLN. The lithium tantalate work converts a component-level property, power stability at 532 nm, into a first integrated-external-modulator underwater link at 112 Gb/s over 3 m, which is the clearest example in these sources of a waveguide-platform improvement propagating to a system capability.

The ceiling on the score is that the sources demonstrate enabling value rather than measure economic value. There are no cost, energy-per-bit or throughput comparisons against incumbent electronic or free-space systems, beyond the qualitative claim that on-chip spatio-temporal encoding replaces bulky free-space optics, long dispersive elements and alignment-sensitive setups. A 5 would require evidence that these improvements displace an incumbent at scale, which the sources do not provide.

**TLDR: It is the substrate everything else in integrated photonics sits on, and the crosstalk and loss limits it imposes are system-level limits.**

## Timing Now (0-2yr)

Waveguides as PIC building blocks are current technology, and the specific 2026 advances are at the stage of measured devices and working links rather than concepts: a system-level 112 Gb/s underwater transmission, a fabricated 1.2 cm PPLN guide, measured zero crosstalk across multiple platforms and a demonstrated on-chip imaging system. A design-rule change that needs no new process module is the fastest thing to adopt, so the crosstalk result should be the first to appear in production layouts.

The other branches sit later. Cryogenic graphene modulators exist only as optimised simulations; passive giant-atom state transfer is analytical, with 87% fidelity at two coupling points and above 99% at ten or more but no device; multimode photonic time crystals are theory; programmable magnonic meshes have working cascaded elements but the sources describe them as newly past the isolated-element stage. Treat those as Later.

**TLDR: The component and its near-term improvements are already in hardware; the topological, time-varying and magnonic branches are further out.**

## Overrated or underrated? Fairly rated

Waveguides are correctly understood as the foundation of integrated photonics, and the sources do not support any claim that a step change is underway. What they do support is a shift in where the binding constraint sits. Propagation loss remains a live target and is still being pushed down through fabrication changes, but the argument that inter-channel crosstalk accumulates across cascaded components and constrains integration density is the more consequential framing for anyone building large photonic processors. If you are assessing PIC platforms, waveguide pitch and crosstalk deserve as much weight as the dB/cm number that usually dominates datasheets.

The second underappreciated line is material choice by wavelength band and power handling rather than by loss alone. The lithium tantalate result is interesting less because of its loss figure, which is only dB/cm scale, than because it holds 5 dBm for an hour at 532 nm where lithium niobate does not. The exotic end, topological transport of spin skyrmions, photonic time crystals, non-Hermitian trimers, is good physics with no demonstrated application in these sources and should not be priced as near-term technology.

## Prediction

By 31 December 2027, at least one silicon-photonics or silicon-nitride foundry process design kit will publish a reduced minimum waveguide pitch justified by slab-engineered mode hybridisation or an equivalent geometry-only crosstalk cancellation, following the multi-platform demonstration reported on 28 May 2026.

## Evidence base

- 28 May 2026: zero crosstalk between adjacent standard rib waveguides demonstrated experimentally via slab thickness engineering across silicon-on-insulator and silicon nitride, presented as a foundry-compatible alternative to specialised nanostructures.
- 14 May 2026: thin-film lithium tantalate waveguides at 532 nm with dB/cm-scale loss and modulators flat to about 50 GHz, stable at 5 dBm modulated output for an hour where thin-film lithium niobate was not, supporting 112 Gb/s over 3 m and 64 Gb/s over 9 m underwater.
- 28 May 2026: a 1.2 cm periodically poled lithium niobate nanophotonic waveguide with low propagation loss, produced by poling the planar film before waveguide definition to avoid the anisotropic etching that had held fully poled devices at a few dB/cm.
- 28 May 2026: on-chip frequency comb generation without a cavity, using non-degenerate cascaded four-wave mixing in dispersion-engineered waveguides, claiming higher pump-to-comb conversion efficiency, tunable line spacing and higher power per line than microresonator combs.
- 6 May 2026: Anderson localisation observed with single photons from a hexagonal boron nitride emitter at room temperature in disordered coupled-waveguide lattices, showing waveguide arrays are mature enough to serve as quantum-transport testbeds.
- 4 May 2026: cascaded programmable magnonic circuits written in a single laser-writing step in yttrium iron garnet, with phase-coherent spin-wave propagation over hundreds of wavelengths and complete periodic power transfer between coupled waveguides.

## Open questions

- Does slab-engineered crosstalk cancellation survive real fabrication tolerance, temperature and wavelength ranges across a full reticle, or is the demonstrated zero-crosstalk condition too narrow to become a design rule?
- Can the PLACE isotropic-etch route to low-loss 1.2 cm PPLN be run at wafer scale and with the yield a foundry needs, or does it stay a laboratory process?
- How far below dB/cm can visible-band lithium tantalate loss be pushed while keeping the 5 dBm power stability advantage over lithium niobate, and does that advantage hold at higher powers?
- What pump power and waveguide length does the cavity-less comb architecture actually require to beat a microresonator on total system efficiency, given the resonator's inherently lower threshold?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
