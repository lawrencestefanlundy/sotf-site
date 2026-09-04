---
type: concept
slug: quantum-repeaters
canonical_name: Quantum Repeaters
aliases: []
kind: technology
parent_concepts:
- communications
- quantum-comms
related_concepts: []
sources:
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
frontier:
- Can multimode memories combine the demonstrated large mode counts (16,340 temporal modes) with storage lifetimes long enough for segments of hundreds of kilometres, or does mode capacity trade directly against lifetime and efficiency?
- 'Given the Gaussian no-go theorem, which non-Gaussian resource wins on cost per node: matter qubits with cryogenics, or bosonic GKP encodings claimed to be room-temperature compatible?'
- When does a two-node repeater experiment demonstrate a measured end-to-end advantage over direct transmission on the same fibre, rather than component fidelities plus an extrapolated rate?
- Can source and memory be co-fabricated with matched bandwidths at yields and stability suitable for field operation, beyond the single-chip silicon-carbide demonstration at 88.1% visibility?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 22
last_reorg_date: '2026-05-14'
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Later (5-10yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 2
sources_30d: 7
recent_mentions:
- slug: 2024-12-16-willow-and-the-race-to-quantum-advantage
  title: Willow and The Race to Quantum Advantage (Feat. Kris Kaczmarek)
  date: '2024-12-16'
  kind: substack
neighbors: []
---
**Quantum repeaters are the relay nodes needed to break the exponential photon-loss limit of optical fibre, and while their individual components (memories, sources, swapping, purification) now work at high fidelity in the lab, no source here shows a full link delivering useful rates.**

## Summary

Photons sent down optical fibre are lost exponentially with distance, and because quantum states cannot be copied, classical amplification is unavailable. A quantum repeater splits a long link into shorter segments, generates entanglement across each segment, stores it in quantum memories until neighbouring segments are ready, then joins the segments by entanglement swapping (a Bell-state measurement at the intermediate node). Errors accumulated along the way are removed by entanglement purification/distillation, or, in later-generation designs, by encoding the transmitted qubits in an error-correcting code so that loss and dephasing are corrected rather than filtered.

The parameters that decide the technology are narrow and unforgiving. Photons must be indistinguishable, because two-photon interference fidelity sets the quality of every Bell-state measurement and fusion gate; recent work reports raw Hong-Ou-Mandel visibilities above 0.95 from a tin-vacancy centre in diamond with an inferred intrinsic indistinguishability up to 0.999. Photon sources must be spectrally matched to the memory, which for rare-earth and atomic ensembles means bandwidths of hundreds of MHz or less, hard to reach with integrated photonics. Memories must combine efficiency, fidelity, storage time and, critically, multimode capacity, since the rate of a repeater scales with the number of modes that can be multiplexed into one attempt entanglement distribution and quantum storage of more than 8.

There is also a hard theoretical boundary. A 2026 no-go theorem shows that a repeater chain built only from Gaussian operations, homodyne measurement and classical communication cannot exceed the quantum capacity of direct transmission over a pure-loss channel, so the experimentally demanding non-Gaussian resources (single-photon detection, matter qubits, or non-Gaussian bosonic codes such as GKP) are not optional. The engineering question is therefore not whether a cheap all-optical shortcut exists, but how fast and how cheaply the expensive route can be made to run.

## Viability (3/5)

The component evidence is genuinely strong. Entanglement swapping with integrated narrowband sources reached a net HOM visibility of 0.99 ± 0.01 and a net swapped-state visibility of 0.88 ± 0.06, enough to violate a Bell inequality. A Yb:YSO repeater node entangled a telecom photon travelling through 25.3 km of fibre with a 979 nm photon stored for 125 µs across 16,340 temporal modes, and distributed entanglement over 5.66 km of the Geneva metropolitan network. A separate memory achieved efficiency above 80% and storage fidelity above 99% on 11-dimensional spatial modes. Purification has been shown on silicon chips, including recovery of residual entanglement from failed events.

What is missing in these sources is the system. The most explicit long-distance figure is an estimate, not a measurement: 3.56 bits of quantum information over a 1000 km repeater link in one minute. Storage lifetimes in the multimode telecom demonstration are tens of microseconds (76.6 µs memory lifetime, 125 µs demonstrated storage), matched to a 25 km segment rather than a continental link. Logical-level repeaters exist as simulation: QRE-CEC distributes logical Bell pairs at 0.91 fidelity in a discrete-event simulator with realistic noise models. Solid-state emitters face temperature limits from spin-phonon decoherence that current Markovian models mispredict. A 3 reflects credible, contested: the physics is demonstrated piecewise, the integration and rate are not.

**TLDR: Every subsystem now works at credible fidelity; no source shows an assembled link beating direct transmission.**

## Drivers (3/5)

On the supply side, the enabling technologies are converging on fabricable platforms. High-Q silicon microrings now reach an intrinsic Q of 1.26 × 10^6 with a photon-pair generation rate of 9.19 MHz and Franson visibility of 98.0 ± 0.2% using standard CMOS-compatible processes. Source and memory have been co-integrated on a single platform using dual silicon-carbide microrings, with photon-memory entanglement verified at 88.1 ± 10.6% visibility. Public funding is explicit and ongoing: the NSF Engineering Research Center for Quantum Networks received an award of $6,000,001 dated 17 July 2026.

Demand is another matter. The stated pull applications are distributed quantum computing, networked quantum sensing and physics-based communications security. None of the supplied sources contains a customer, a procurement, a price, or a service that is waiting on repeaters. Two of the three named applications depend on quantum computers that do not yet need long-haul interconnects. This is a supply-push field on the evidence available.

**TLDR: Supply is pushed by sustained public research funding and integrated-photonics manufacturability; demand is asserted rather than evidenced in these sources.**

## Novelty (3/5)

Measured against the prior art within quantum networking, the increments are real and quantified. Multiplexing schemes such as zero-added-loss multiplexing convert probabilistic heralded entanglement into quasi-deterministic pair generation, and the time-bin plus spectral-shearing variant extends this to time-bin encoding with experimentally verified phase compatibility. High-dimensional entanglement swapping, previously blocked by the need for strong nonlinearities and demonstrated only in two dimensions, is shown to be implementable with linear optics and ancillary photons in a four-dimensional hyper-entangled design. A new distillation protocol search distils Werner states at a higher rate than previously discovered protocols and improves the best-known lower bound on the two-way-assisted quantum capacity of the depolarising channel.

The crucial comparison, repeater versus direct transmission, is characterised negatively rather than positively: the Gaussian no-go theorem establishes that a large and experimentally convenient class of repeater designs offers exactly zero advantage over direct fibre. That is a useful result because it prunes the design space, but it also means the sources do not contain a demonstrated end-to-end margin over the incumbent. Against the real incumbent for long-distance secure key, trusted-node relaying, these sources offer no comparison at all.

**TLDR: Clear improvements over prior repeater components and protocols; the comparison against classical trusted-node relaying is not made anywhere in these sources.**

## Diffusion (2/5)

Deployment evidence is thin: a single field distribution of entanglement over 5.66 km of Geneva metropolitan fibre, using a laboratory rare-earth memory. Everything else in these sources is bench-scale or simulated. The barriers named by the researchers themselves are systems-level rather than conceptual: narrowband photons compatible with atomic memories are hard to generate on chip and hard to stabilise across a swapping experiment, spectral matching between source and memory remains a major integration challenge, and solid-state spin qubits are constrained in operating temperature by phonon-induced decoherence.

The counterweight is that the field is deliberately migrating onto manufacturable substrates: silicon photonics for purification circuits, silicon microrings for sources, silicon carbide for co-integrated source-plus-memory nodes. Even measurement instrumentation is being built for repeater operation, for example single-shot single-photon spectroscopy resolving 120 MHz frequency modes matched to Pr:YSO memory channel spacing. That is the right direction of travel, but it does not yet amount to diffusion.

**TLDR: One short metropolitan field deployment, cryogenic and narrowband-matching requirements, and no standards or products in evidence.**

## Impact (4/5)

Quantum repeaters are the gating technology for anything that needs entanglement between distant sites: distributed quantum computing, networked sensing with sensitivity beyond classical limits, privacy-preserving access to remote quantum processors and physics-based communications security. Multiple papers frame repeaters as the backbone of a quantum internet and as the only route past exponential fibre attenuation beyond metropolitan distances. Because there is no classical substitute for distributing entanglement, the technology is enabling rather than incremental, which justifies a high conditional score.

The qualification is that the impact is conditional on rates that remain far from useful. The only long-distance throughput figure available is an estimate of 3.56 bits per minute over 1000 km. At that order of magnitude the addressable applications shrink to key distribution and clock or sensor synchronisation rather than distributed computing. None of the sources attaches a market size or economic value to any of this, so the 4 reflects breadth of dependence, not demonstrated value.

**TLDR: If long-haul entanglement becomes routine it underpins an entire class of applications, though none of these sources quantifies the value.**

## Timing Later (5-10yr)

The subsystem milestones are landing continuously through 2026: swapping with integrated narrowband sources in July, a 16,340-mode telecom memory node with a metropolitan field trial in August, on-chip purification in June. Expect multi-node metropolitan testbeds within the near term because the pieces exist and public funding is in place.

The long-haul case is further out. Storage lifetimes of tens of microseconds are matched to segments of a few tens of kilometres, error-corrected repeaters exist as simulations rather than hardware, and the theory has just closed off the cheapest hardware route. Nothing in these sources supports a 0-5 year timeline for a useful continental repeater chain.

**TLDR: Component demonstrations are happening now; a repeater link that beats direct transmission at useful rates is not close on this evidence.**

## Overrated or underrated? Fairly rated

As a research programme, quantum repeaters are correctly valued: the physics is no longer in doubt, the fidelities are at or near the thresholds that swapping and purification require (0.99 HOM visibility, 0.999 intrinsic indistinguishability, >99% memory storage fidelity, >80% memory efficiency), and the field has moved onto chip-scale platforms that could in principle be manufactured. The theoretical work is also doing real service by eliminating dead ends rather than adding protocols nobody can build.

Anyone treating repeaters as a near-term commercial technology, however, is reading the same evidence too generously. The single long-distance throughput number available is an extrapolated 3.56 bits per minute at 1000 km, and the only field trial covers 5.66 km. The gap between component fidelity and system rate is the whole story here, and multiplexing capacity (thousands to tens of thousands of modes) is the variable to watch, because it is the only lever in these sources that attacks rate by orders of magnitude rather than percentages.

## Prediction

By 31 December 2029 no peer-reviewed experiment will report a memory-based quantum repeater distributing entanglement over more than 100 km of deployed (non-spooled) fibre at a rate exceeding one Bell pair per second.

## Evidence base

- 4 June 2026: a no-go theorem proves that repeater chains built from Gaussian operations, homodyne measurement and classical communication cannot exceed the quantum capacity of direct transmission over a pure-loss channel, forcing non-Gaussian hardware.
- 14 August 2026: a Yb:YSO repeater node (250 MHz bandwidth, 76.6 µs lifetime) entangled a telecom photon through 25.3 km of fibre with a photon stored 125 µs across 16,340 temporal modes, plus a 5.66 km field deployment on the Geneva metropolitan network.
- 31 July 2026: entanglement swapping with integrated narrowband sources achieved net HOM visibility 0.99 ± 0.01 and net swapped-state visibility 0.88 ± 0.06, sufficient to violate a Bell inequality.
- 17 August 2026: an 11-dimensional spatial-mode memory reached >80% efficiency and >99% storage fidelity, with an estimated 3.56 bits distributed over a 1000 km repeater link in one minute.
- 27 July 2026: a tin-vacancy centre in diamond produced raw HOM visibilities above 0.95 with intrinsic indistinguishability inferred up to 0.999, with residual limits attributed to technical rather than decoherence effects.
- 17 July 2026: the NSF Engineering Research Center for Quantum Networks received $6,000,001 to build quantum-internet foundations, PI Saikat Guha.

## Open questions

- Can multimode memories combine the demonstrated large mode counts (16,340 temporal modes) with storage lifetimes long enough for segments of hundreds of kilometres, or does mode capacity trade directly against lifetime and efficiency?
- Given the Gaussian no-go theorem, which non-Gaussian resource wins on cost per node: matter qubits with cryogenics, or bosonic GKP encodings claimed to be room-temperature compatible?
- When does a two-node repeater experiment demonstrate a measured end-to-end advantage over direct transmission on the same fibre, rather than component fidelities plus an extrapolated rate?
- Can source and memory be co-fabricated with matched bandwidths at yields and stability suitable for field operation, beyond the single-chip silicon-carbide demonstration at 88.1% visibility?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
