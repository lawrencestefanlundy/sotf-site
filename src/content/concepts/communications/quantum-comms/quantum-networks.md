---
type: concept
slug: quantum-networks
canonical_name: Quantum Networks
aliases: []
kind: technology
parent_concepts:
- communications
- quantum-comms
related_concepts: []
sources: []
frontier:
- Can on-chip telecom memory efficiency rise from 23.3% towards the levels needed for multi-hop links without sacrificing the 277.6 s comb lifetime or the 20 MHz programmable routing 2026 05 15 programmable cavity enhanced telecom quantum memory in thin ?
- Do the room-temperature Purcell-enhanced single erbium ions in silicon carbide retain usable spin coherence and support spin-photon entanglement, or is room-temperature operation limited to bare single-photon emission 2026 05 08 room temperature purcell enhanced single erbium ions in sili?
- How short is the operational correlation length in practice, and does it cap useful entanglement-swapping paths at a handful of hops in deployed metropolitan fibre 2026 05 28 emergent operational entanglement graphs and sub quadratic a?
- Does any demand exist beyond entanglement-based key distribution, given that the sources contain no customer, funding or procurement evidence of any kind?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 131
last_reorg_date: '2026-05-14'
scorecard:
  viability: 3
  drivers: null
  novelty: 4
  diffusion: 2
  impact: 3
  timing_band: Later (5-10yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 3
sources_30d: 22
recent_mentions: []
neighbors: []
---
**Quantum networks distribute entanglement rather than copies of bits between distant nodes, enabling entanglement-based key distribution, distributed quantum computing and distributed sensing, and the 2026 literature shows working component demonstrations and a maturing protocol stack but no service-carrying network beyond metropolitan-scale testbeds.**

## Summary

A quantum network moves quantum states, and more usefully shared entanglement, between separated nodes. The defining constraint is that entanglement cannot be copied or amplified, so every classical networking assumption about buffering, retransmission and broadcast breaks. End-to-end links are built by generating entanglement over short segments and joining them with entanglement swapping, which means the network is really a scheduling and resource-allocation problem over a stochastic, decaying resource. Satellite architectures inherit the same constraint: because long-lived buffering is technologically limited in near-term devices, useful service requires fixed optical ground infrastructure and simultaneous availability of every hop on a path at once.

The stack has three layers under active work. At the physical layer sit spin-photon interfaces and quantum memories. Diamond colour defects are the most developed node candidate, combining good optical properties, fast spin control and long spin coherence, and have already supported metropolitan-scale network demonstrations. Erbium is the competing route because it emits natively in the telecom C-band and so is compatible with installed fibre; a 2026 demonstration put single implanted Er3+ ions in a silicon-carbide-on-insulator microring with roughly 70x Purcell enhancement operating at room temperature. Memories are the bottleneck: a cavity-enhanced erbium-doped thin-film lithium niobate memory reached 23.3 ± 0.5% on-chip storage efficiency for 100 ns storage, with a 277.6 ± 52.6 s atomic frequency comb lifetime, frequency-selective routing at up to 20 MHz and inter-channel crosstalk below 1e-4, and stored and retrieved time-energy-entangled telecom photons violating an entanglement witness by more than 11 standard deviations.

Above that sits link-level entanglement generation. Photonic approaches depend on fusion gates, which without ancillas succeed only half the time; a 2026 proposal reaches 3/4 total success using four ancillary single photons and passive linear optics, succeeding directly with probability 5/8 and recovering the rest by distillation. Waveguide-QED routes aim at deterministic transfer instead: giant atoms coupled to 1D waveguides give 87% transfer fidelity with two coupling points and above 99% with ten or more.

The top layer, network control, has moved fastest. There is now a full protocol stack with a Global Entanglement Module maintaining a network-wide view of entanglement resources, improving entanglement generation rates by about 20% over a globally optimal but non-adaptive fixed-tree baseline and more than two-fold over connectionless approaches, and online schedulers that defer, retry or drop entanglement reservations and beat static TDMA baselines on completion time, completion ratio and throughput while degrading gracefully under overload. The parameters that decide the field are memory efficiency and lifetime, spin-photon interface efficiency at telecom wavelengths, and how fast entanglement fidelity decays along swapped paths.

## Viability (3/5)

The physics is not in doubt and the demonstrations are real: entangled telecom photons stored and retrieved from an on-chip memory with an 11-sigma entanglement witness violation, single telecom-band emitters Purcell-enhanced by ~70x at room temperature, and metropolitan-scale networks built on diamond colour defects. What is missing is the composition of these into a system that survives its own loss budget. The memory figure of 23.3% efficiency for 100 ns storage is the honest state of the art on chip, and a chain of hops multiplies such numbers together.

The sources also contain an internal admission of the gap. A 2026 encryption protocol assuming a quantum computer with quantum memory and functioning quantum networks states that, in the absence of the latter at present, the protocol can only be demonstrated in the laboratory on existing quantum computing platforms. Meanwhile a transport analysis shows Bell correlations decaying exponentially along entanglement-swapping paths under realistic loss and decoherence, producing finite operational correlation lengths and sparse rather than fully connected entanglement graphs. That is a physical ceiling on reach, not an engineering detail, and it is why a 3 rather than a 4.

**TLDR: Every component has been demonstrated somewhere, none at the numbers a service network needs.**

## Drivers (unscored)

On the supply side there is clear momentum: a large volume of coordinated work in a short window spanning device physics, protocol stacks, satellite constellation design and foundational certification theory, with national research institutes involved in the photonic detection work. The problem set has moved from single-link physics to network-level questions such as scheduling and resource provisioning, which is what happens when a field starts to believe deployment is the next step.

On the demand side the supplied material says nothing usable. There are no customers, contracts, market sizes, telco commitments, regulatory mandates or funding figures anywhere in these sources. The satellite backbone study targets a traffic matrix of major population and financial centres, but that is an assumed demand model in a simulator, not observed demand. Scoring this dimension would mean inventing the half of the picture that decides it, so it is left null.

**TLDR: The sources are entirely supply-side research output; they contain no demand, funding or procurement evidence.**

## Novelty (4/5)

Against the classical alternative the comparison is categorical rather than incremental. Device-independent certification of a quantum state from measurement statistics alone has no classical analogue, and a 2026 protocol removes the scalability barrier by self-testing almost all n-qubit states with polynomial rather than exponentially many samples, using only a linear number of ancillary Bell pairs plus standard projective and Bell measurements. Distributed sensing over a Gaussian network achieves quadratic scaling of precision with total photon number while retaining privacy properties. Network nonlocality itself has been pushed to its minimal instance, a triangle network with no input choices and binary outcomes.

Against prior quantum baselines the improvements are real and measured, though mostly single-digit multiples. Boosted type-I fusion moves success probability from 1/2 to 3/4 using only single-photon ancillas rather than probabilistically prepared Bell pairs. Adaptive entanglement scheduling gives about 20% over the best static plan and more than 2x over connectionless approaches. Room-temperature operation of a telecom single-photon emitter removes a cryogenic requirement outright. The one deduction: a substantial fraction of the novelty here is proposal-stage, including the carbon nanotube plasmonic spin-photon interface with its projected ~100 Hz residual backscattering.

**TLDR: The core capabilities have no classical equivalent, and the recent step changes over prior quantum baselines are quantified.**

## Diffusion (2/5)

The barriers are stacked. Entanglement fidelity falls exponentially with the number of swaps under realistic loss and decoherence, so a large network does not become a fully connected one; the operational entanglement graph stays sparse and the number of CHSH-usable Bell pairs scales only linearly with network size. Satellite service does not rescue this, because absent long-lived buffering it demands fixed optical ground infrastructure and every hop of a path available simultaneously, with performance sensitive to ground-station lattice geometry and constellation inclination. On-chip memory efficiency of 23.3% for 100 ns storage compounds badly across hops.

There are genuine easing factors. Telecom C-band emitters are compatible with installed fibre by construction, heterogeneous integration of diamond nanophotonics with photonic integrated circuits is improving node manufacturability, and the authentication overhead for entanglement-based QKD networks appears to scale as Theta(N log N) rather than quadratically under sparse-mixing assumptions, which removes a presumed classical-overhead blocker at scale. Even so, nothing in these sources shows an operator running a network, and none of them quantifies cost.

**TLDR: Cryogenics, sub-25% memory efficiency and exponential fidelity decay along swap paths confine deployment to sparse metropolitan graphs.**

## Impact (3/5)

What pins this at 3 rather than higher is that the sources contain no economic or operational quantification of any of these, and the physics-imposed sparsity of the entanglement graph suggests the near-term addressable service is a set of short, high-value links rather than a general-purpose substrate. The upside case rests on distributed quantum computing being valuable, which nothing here establishes independently.

**TLDR: Credible new capability classes in security, distributed computing and sensing, but the sources assert value rather than quantify it.**

## Timing Later (5-10yr)

The near-term picture is already visible: metropolitan-scale demonstrations with diamond colour defects exist, integrated telecom memories store and retrieve entangled photons with verified quantum character, and the control-plane software is being written and benchmarked in simulation. That is a field in the demonstrator phase, not the deployment phase.

The gating items are slow ones. Memory efficiency needs several multiples of improvement, room-temperature telecom emitters need to be shown to carry spin-photon entanglement rather than only single-photon emission, and satellite service needs buffering capability that the architecture literature explicitly treats as unavailable for near-term devices. None of those resolves on a two-year clock. Sub-quadratic authentication scaling removes one long-term blocker, which supports a five to ten year band rather than pushing it beyond.

**TLDR: Metro testbeds and component records now; a network carrying useful service to multiple users is not within two to five years on this evidence.**

## Overrated or underrated? Fairly rated

The technical community is being more honest about the limits than the framing usually suggests. The same body of 2026 work that builds a full protocol stack also shows Bell correlations decaying exponentially along swap paths and concludes that real metropolitan networks have sparse operational entanglement graphs with linearly rather than quadratically many usable Bell pairs, and the satellite architecture work opens by conceding that long-lived buffering is technologically constrained. Read against those constraints, the field's own claims are proportionate.

Where expectations run ahead of the evidence is the phrase "global quantum internet". Nothing in these sources supports a general-purpose, arbitrarily connected substrate. What they support is a sparse set of short high-value links, with entanglement treated as a scheduled, perishable resource, and with the strongest near-term value in certification, key distribution and distributed sensing rather than distributed computing. The bottleneck is unambiguously the memory: 23.3% on-chip storage efficiency for 100 ns is the number that determines whether any of the elegant control-plane work ever runs on hardware.

## Prediction

By 31 December 2028, published integrated on-chip telecom-band quantum memories will still report storage efficiencies below 50%, against the 23.3 ± 0.5% demonstrated in the erbium-doped thin-film lithium niobate microring in May 2026.

## Evidence base

## Open questions

- Can on-chip telecom memory efficiency rise from 23.3% towards the levels needed for multi-hop links without sacrificing the 277.6 s comb lifetime or the 20 MHz programmable routing?
- Do the room-temperature Purcell-enhanced single erbium ions in silicon carbide retain usable spin coherence and support spin-photon entanglement, or is room-temperature operation limited to bare single-photon emission?
- How short is the operational correlation length in practice, and does it cap useful entanglement-swapping paths at a handful of hops in deployed metropolitan fibre?
- Does any demand exist beyond entanglement-based key distribution, given that the sources contain no customer, funding or procurement evidence of any kind?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
