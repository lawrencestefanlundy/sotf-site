---
type: concept
slug: ring-resonators
canonical_name: Ring Resonators
aliases: []
kind: technology
parent_concepts:
- photonic-systems
- modulators-detectors
related_concepts: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2024-10-23-optical-dram-integrated-non-reciprocal-magneto-optics-with]]'
frontier:
- How does per-ring tuning and locking power scale from the 32 channels reported at 71 fJ/b to the hundreds or thousands of resonators implied by co-packaged optics roadmaps?
- Does capacitive or piezoelectric actuation displace thermal tuning for resonance trimming, and what is the head-to-head power, speed and range comparison that no current source provides?
- Is closed-loop electronic wavelength locking sufficient against ±1.7 nm drift in a real hot package, or is workload-level thermal management genuinely required?
- For the visible and quantum applications, what quality factor and fabrication uniformity are actually needed, and how far above the demonstrated 7.0 x 10^4 in Ta2O5 does that sit?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 28
last_reorg_date: '2026-05-13'
scorecard:
  viability: 4
  drivers: 4
  novelty: 3
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 3
recent_mentions:
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2024-10-23-optical-dram-integrated-non-reciprocal-magneto-optics-with
  title: Integrated non-reciprocal magneto-optics with ultra-high endurance for photonic in-memory computing
  date: '2024-10-23'
  kind: web
neighbors: []
---
**Ring resonators are micron-scale looped optical waveguides that resonate at specific wavelengths, and they are the wavelength-selective workhorse of integrated photonics: already inside a monolithic CMOS receiver running 1.024 Tb/s at 71 fJ/b, but exquisitely temperature-sensitive, which turns their adoption problem into a control and thermal engineering problem rather than a physics one.**

## Summary

A ring resonator is a closed loop of optical waveguide placed next to a straight "bus" waveguide. Light couples into the loop and interferes with itself on each circuit; only wavelengths whose round-trip phase is an integer multiple of 2π build up. The result is a compact, wavelength-selective element with a comb of resonances, characterised mainly by its quality factor Q (how long light circulates before being lost), its free spectral range (resonance spacing, set by the loop circumference and effective index) and its coupling to the bus. Change the effective index slightly, thermally, electrically or piezoelectrically, and the resonance moves. That single property is why the same device serves as filter, wavelength (de)multiplexer, modulator, nonlinear-optics cavity and sensor.

In the modulator/detector role that matters commercially, rings are how wavelength-division-multiplexed (WDM) channels are separated on chip. A 45 nm CMOS monolithic receiver used an on-chip demultiplexer built from Mach-Zehnder interferometers and ring resonators with capacitive tuning to run 32 channels at 32 Gb/s each, 1.024 Tb/s aggregate, at 71 fJ/b including the electronics and the tuning and control of the photonic devices, with bit error rate below 1e-12 and no equalisation or forward error correction. That is the strongest single data point on this page: rings inside a working, energy-accounted system rather than a test structure.

The decisive parameter is thermal stability. In co-packaged optics, where the photonic layer sits next to hot logic, micro-ring resonators embedded in the PIC layer are described as exquisitely temperature-sensitive, with a resonant-wavelength deviation of only ±1.7 nm causing measurable bit-error-rate degradation, which motivates predictive scheduling of the compute workload as an early-warning layer for optical-engine drift. Everything else about ring adoption follows from this: how much power the tuning loop burns, how many rings you can lock simultaneously, and whether cheaper actuation exists. Piezo-optomechanical PICs, now co-fabricated monolithically with commercial CMOS drivers on 200 mm wafers, are pitched at exactly the regime of thousands to millions of reprogrammable photonic devices, offering low power consumption, high-speed modulation, cryogenic compatibility and ultraviolet-to-infrared transparency.

## Viability (4/5)

The strongest evidence is a full system rather than a component: 32 channels, 32 Gb/s each, 1.024 Tb/s aggregate on one 45 nm CMOS chip, with a ring-and-MZI demultiplexer giving enough channel isolation to hold bit error rate below 1e-12 without equalisation or error correction, at 71 fJ/b including tuning and control power and 4 Tb/s/mm2 bandwidth density. Reporting the tuning and control power inside the energy budget is what distinguishes this from a resonator characterisation paper. Fabrication maturity is also broad: rings are being made in silicon, silicon nitride under piezo actuators on 200 mm CMOS wafers, tantalum pentoxide by routine and scalable thin-film deposition and diamond-on-insulator on a stated fabrication-ready pathway.

The deduction is for thermal fragility, which the sources treat as a first-order system risk rather than a nuisance: ±1.7 nm of resonance drift is enough to degrade BER measurably in a co-packaged optical engine, and the proposed mitigation is to co-design the compute scheduler with the optics. Fabrication spread is the sibling problem; the squeezing work explicitly has to design for inhomogeneous resonator frequencies and component failures. Rings work; keeping thousands of them on resonance in a hot package is the open engineering question.

**TLDR: Working inside a monolithic CMOS Tb/s receiver with power and error rate accounted for; the remaining problem is drift, not function.**

## Drivers (4/5)

Demand: the pull comes from WDM interconnect for data centres, framed in the sources as the path to compact, high-bandwidth and energy-efficient links, and specifically from co-packaged optics integration at the A16 / 2 nm node, where micro-rings sit in the PIC layer of a named CPO engine architecture. A second demand vector is device count: next-generation photonic architectures for AI, sensing and quantum computing are stated to require thousands to millions of reprogrammable photonic devices per chip, and resonant elements are the compact way to get wavelength selectivity at that density.

Supply: the enabling shift is monolithic co-fabrication with electronics. Photonic wafers built by back-end-of-line processing directly on completed 200 mm CMOS driver wafers give the high-density electrical interconnection that per-ring control loops require. Material supply is broadening rather than narrowing: Ta2O5 on insulator for the visible using routine deposition and fabrication, and open-source finite-element tooling for ring modal analysis validated against a commercial mode solver, which lowers the design barrier. The one thing the sources do not give is market size, shipment volume or price, so the demand case here is technical and roadmap-based, not commercial.

**TLDR: Demand is AI-datacentre interconnect via co-packaged optics; supply is CMOS-compatible fabrication across several material platforms.**

## Novelty (3/5)

Critically, the sources do not isolate the ring's advantage over the alternative demultiplexing approaches. The record receiver uses a hybrid demultiplexer of MZIs and rings, so the ring's marginal contribution to the 71 fJ/b and 4 Tb/s/mm2 figures cannot be extracted. Nor do the sources compare thermal against capacitive against piezoelectric tuning on a common benchmark, even though all three appear. This is a component in incremental refinement across many platforms, not a step change.

**TLDR: The ring itself is a mature building block; the novelty in these sources is in materials, tuning mechanism and cascading, with real but bounded gains.**

## Diffusion (4/5)

Diffusion is further along than for most photonic components. Rings appear in a monolithic 45 nm CMOS receiver where the control overhead is inside the reported energy budget, and in the PIC layer of a named co-packaged-optics engine architecture at the leading logic node. Design tooling is being commoditised, with open-source FEM modal-analysis frameworks validated against a commercial solver, and process routes are described as routine and scalable in at least one new material system.

The adoption barriers are all downstream of resonance drift. A ±1.7 nm wavelength excursion degrades BER, which means every deployed ring needs a monitor, a heater or actuator and a locking loop, and in the CPO case the proposed answer reaches all the way up into the software scheduler. That is a system-integration burden crossing organisational boundaries between fab, package, driver ASIC and host software. The second barrier is fabrication spread across large arrays, which designers currently handle by making architectures tolerant of inhomogeneous resonator frequencies and component failures rather than by tightening the process. The third is control-wiring density, which monolithic photonics-on-CMOS is explicitly intended to solve.

**TLDR: Already inside CMOS-integrated systems and CPO roadmaps; the barrier is closed-loop wavelength locking at scale, not acceptance.**

## Impact (4/5)

The primary value is interconnect bandwidth density and energy per bit. A single chip delivering 1.024 Tb/s at 71 fJ/b and 4 Tb/s/mm2, with BER below 1e-12 and no forward error correction, describes the regime that co-packaged optics needs to reach for AI clusters. Removing equalisation and error correction also removes latency and digital power, which compounds the benefit. Since the resonator is what makes many wavelengths separable in a small area, this is load-bearing rather than incidental.

**TLDR: If ring-based WDM holds in hot packages, it is the wavelength layer of AI-scale optical interconnect; secondary value in quantum sources and photonic memory.**

## Timing Now (0-2yr)

For WDM interconnect the technology is at the present margin, not the future one. A monolithic CMOS receiver using ring-based demultiplexing already runs at 1.024 Tb/s with the tuning and control power counted, and rings are treated as an assumed constituent of a co-packaged optics engine at the A16 / 2 nm node, with the open work being drift mitigation rather than device demonstration. Monolithic photonics-on-CMOS for dense reprogrammable arrays is a 2026 first demonstration, so the high-device-count variants sit slightly behind.

**TLDR: The datacom use is already in integrated silicon and on CPO roadmaps; the quantum and memory uses are later.**

## Overrated or underrated? Fairly rated

Ring resonators are correctly valued as an unglamorous, load-bearing component. They are not a bet; they are already carrying a terabit per second on a CMOS die at 71 fJ/b with the control overhead included, which is the kind of result that ends arguments about whether a component works. Anyone pitching rings as a breakthrough is misreading the field: they are a mature primitive being pushed into new materials and new wavelength ranges, and the quantified gains in these sources are all relative to earlier rings.

Where the market attention is misallocated is one layer up. The binding constraint is stated plainly: ±1.7 nm of resonance drift degrades BER, in a package where the optics sits beside hot logic, and the response proposed is to make the compute scheduler an early-warning layer for optical drift. That means the value accrues to whoever owns the wavelength-locking stack, the actuation mechanism and the co-design across fab, package and software, not to the resonator geometry. Capacitive tuning inside the record receiver and piezoelectric actuation monolithically integrated with CMOS drivers are the parts of this story to watch. Judged as a component, fairly rated; judged as an investment thesis, look at the control layer instead.

## Prediction

By 31 December 2028, a peer-reviewed monolithically integrated CMOS ring-and-MZI WDM receiver will report an aggregate data rate above 1.024 Tb/s at an energy efficiency below 71 fJ/b with tuning and control power included; if no such result appears, the ring-based CPO scaling path has stalled on wavelength-locking overhead.

## Evidence base

## Open questions

- How does per-ring tuning and locking power scale from the 32 channels reported at 71 fJ/b to the hundreds or thousands of resonators implied by co-packaged optics roadmaps?
- Does capacitive or piezoelectric actuation displace thermal tuning for resonance trimming, and what is the head-to-head power, speed and range comparison that no current source provides?
- Is closed-loop electronic wavelength locking sufficient against ±1.7 nm drift in a real hot package, or is workload-level thermal management genuinely required?
- For the visible and quantum applications, what quality factor and fabrication uniformity are actually needed, and how far above the demonstrated 7.0 x 10^4 in Ta2O5 does that sit?

---
*Assessment drafted 2026-08-31 from up to 16 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
