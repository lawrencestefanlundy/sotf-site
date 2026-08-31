---
type: concept
slug: superconducting-qubits
canonical_name: Superconducting Qubits
aliases: []
kind: technology
parent_concepts:
- compute
- quantum-computing
related_concepts: []
sources:
- '[[2023-05-24-launching-state-of-the-future]]'
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2025-09-18-qphox-and-rigetti-awarded-58m-contract-from-afrl-to-enable-o]]'
- '[[2026-06-12-hku-sic-cryogenic-neuromorphic-chip-10mk]]'
frontier:
- Does the superfluid-density dissipation bound represent a genuine floor for transmon coherence, or can material or geometry choices circumvent the trapped-quasiparticle channel it attributes the loss to 2026 05 04 universal bound on microwave dissipation in superconducting ?
- How common are TLS defects that couple to two or more qubits at once, and do the resulting correlated, non-Markovian error patterns break the independence assumptions of standard error-correction thresholds 2026 05 28 non local and non markovian effects of a microscopic two lev?
- Can radon plate-out during fabrication and packaging be controlled cheaply enough that its area-scaling alpha background does not set an upper limit on usable die size 2026 06 02 accelerating surface radiation content to investigate the im?
- Does the 0.19% gate-fidelity penalty of optical I/O hold as the number of multiplexed channels grows from two towards hundreds, and what is the net cryogenic thermal budget compared with coaxial wiring 2026 06 07 all optical control and multiplexed readout of multiple supe?
- Do protected designs such as cos(2φ) ever escape the residual first-harmonic 1/f flux-noise limit measured at the flux symmetry point, or does each new protection mechanism simply expose a different dominant channel 2026 05 08 coherence limitations of a fourier engineered cos2varphi tra?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 75
last_reorg_date: '2026-05-13'
scorecard:
  viability: 4
  drivers: null
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 10
recent_mentions:
- slug: 2026-06-12-hku-sic-cryogenic-neuromorphic-chip-10mk
  title: HKU world-first cryogenic neuromorphic chip at 10 mK (silicon carbide, impact-ionisation spiking)
  date: '2026-06-12'
  kind: web
- slug: 2025-09-18-qphox-and-rigetti-awarded-58m-contract-from-afrl-to-enable-o
  title: QphoX and Rigetti awarded $5.8M Contract from AFRL to enable optical networks of superconducting qubits - TU Delft
  date: '2025-09-18'
  kind: web
- slug: 2024-12-04-cubits-in-a-fridge-why-is-nobody
  title: Silicon Spin Quantum Computing (Feat. Himadri Majumdar, SemiQon)
  date: '2024-12-04'
  kind: substack
- slug: 2024-11-20-nuclear-fusion-the-state-of-play
  title: 'Nuclear Fusion: A Primer'
  date: '2024-11-20'
  kind: substack
- slug: 2023-05-24-launching-state-of-the-future
  title: '💡 E01: Launching State of the Future: The Worlds First Deep Tech Tracker'
  date: '2023-05-24'
  kind: substack
neighbors: []
---
**Superconducting qubits are microwave circuits containing Josephson junctions that behave as controllable artificial atoms, and they are the most engineering-mature solid-state route to a quantum processor, but the 2026 literature is still dominated by the discovery of new decoherence and readout-failure mechanisms rather than by evidence of a solved path to scale.**

## Summary

A superconducting qubit is an electrical circuit, cooled to millikelvin temperatures, in which one or more Josephson junctions supply the nonlinearity that turns a harmonic microwave resonator into an anharmonic system with addressable, well-separated energy levels. Because the level spacing is unequal, a microwave pulse can drive one transition without exciting the rest, so the lowest two levels act as a qubit. Control and measurement are done with microwave cavities under the framework of circuit quantum electrodynamics, which emerged in the early 2000s and made these circuits leading candidates for scalable quantum devices; the two dominant designs today are the transmon and the fluxonium. Readout is normally dispersive: a probe tone on a coupled resonator picks up a qubit-state-dependent frequency shift, ideally a projective, quantum non-demolition measurement.

The parameters that decide the technology are coherence time, single- and two-qubit gate fidelity, readout fidelity and its non-destructiveness, qubit count with useful connectivity, and the wiring and power overhead per qubit. Each of these is currently set by a different physical obstacle. Coherence is attacked by two-level-system (TLS) defects in the amorphous materials and tunnel barriers of the device, by 1/f flux and charge noise, by residual microwave dissipation in the superconductor itself, and by ionising radiation that generates phonons and quasiparticles. Readout is attacked by measurement-induced state transitions, where a strong probe drive pushes the qubit out of the computational subspace. Scaling is attacked by input/output: conventional architectures need independent microwave cables per qubit, and dense cable arrays impose prohibitive footprint, thermal load and cost constraints at hundreds of qubits.

Most of the current research effort splits into two directions. The first is materials and error physics: an empirical scaling relation between microwave dissipation and superfluid density across amorphous films, resonators, 3D cavities and transmons points to an intrinsic bulk loss channel from nonequilibrium quasiparticles, independent of surface dielectric loss, and sets a material-determined coherence limit. The second is circuit design: intrinsically protected qubits such as the cos(2φ) circuit, which allows only paired Cooper-pair tunnelling and so suppresses charge-induced errors, plus more speculative proposals using Andreev-spin hybrids, altermagnetic Josephson junctions and fractional vortices in 0-π junctions qubit states based on fractional vortices in 0 pi josephson.

Alongside computation, the same circuits are used as quantum simulators and as hybrid platforms, coupling qubits to mechanical resonators, acting as single-photon switching elements, and hosting engineered many-body physics such as quantum solitons in capacitively coupled transmon arrays.

## Viability (4/5)

There is no doubt the platform functions. Multi-qubit superconducting processors run digital algorithms: a nine-qubit processor with a multiply-connected Platonic lattice geometry was used to variationally prepare low-energy eigenstates of a transverse-field Ising model on an eight-qubit register and extract 3D Ising critical exponents. Optical control and multiplexed optical readout of two qubits has been demonstrated end to end with no measurable degradation of coherence and only a 0.19% reduction in single-qubit gate fidelity relative to standard microwave operation. Theory for readout errors now matches experiment closely: numerical models of measurement-induced state transitions in a fluxonium predicted eleven experimentally identified high-error regions across the flux range.

What holds the score below 5 is that the 2026 literature reads as a catalogue of newly identified error channels rather than of closed ones. A TLS defect sitting in a transmon's tunnel barrier was found to couple resonantly to the readout resonator and shift its frequency enough to spoil the readout signal, a failure route distinct from ordinary decoherence. A single TLS in a tunable coupler was shown to couple to two spatially distant qubits and induce correlated, non-Markovian dynamics, with a reconstructed 1/f noise spectrum spanning more than ten orders of magnitude from 0.1 mHz to 1 MHz. Even the flagship protected design underperforms: the Fourier-engineered cos(2φ) transmon is limited at the flux symmetry point by 1/f flux noise arising from residual first-harmonic content. The sources contain no data on error-corrected logical qubits, so viability at fault-tolerant scale is not assessed here.

**TLDR: The devices unambiguously work and produce publishable physics, but every layer of the stack still has open failure modes.**

## Drivers (unscored)

No supplied source addresses demand: there is no revenue figure, customer, procurement programme or market forecast anywhere in this set. Nor is there anything on the supply side in the industrial sense, no fabrication capacity, dilution-refrigerator supply, or component vendors. Assigning a driver score would be fabrication.

The only adjacent signal is technical rather than commercial. Scaling motivation is stated explicitly as an I/O constraint: processors hosting hundreds of qubits face a severe input/output bottleneck from dense microwave cable arrays, with consequences for footprint, thermal load, wiring complexity and cost. Separately, energy is beginning to be treated as a first-class design constraint, with a framework proposed to benchmark the energy efficiency of quantum computing architectures and comparisons drawn across superconducting qubits, silicon spin qubits, trapped ions, neutral atoms and photonic qubits. Both indicate that cost and infrastructure pressure is real, but neither quantifies demand.

**TLDR: The sources are almost entirely physics papers and say nothing about funding, markets or supply chains.**

## Novelty (3/5)

Superconducting qubits are a mature line of work, dating in their circuit-QED form to the early 2000s, and a review in this set describes them as leading candidates for scalable quantum devices. That is a positioning claim, not a measurement. The competing platforms are named in these sources, including trapped ions, ultracold atoms, Rydberg arrays and photonic systems for simulation and silicon spin qubits, trapped ions, neutral atoms and photonic qubits for energy, but no supplied excerpt gives a head-to-head figure of merit. So the margin of superiority cannot be quantified from this evidence.

Where genuine novelty sits is in the sub-branches. Circuit engineering allows qubit spectra and interactions to be designed, which the alternatives cannot do so freely, and this is exploited both for protection and for simulation: an experimentally realised cos(2φ) qubit using interference to suppress odd harmonics of the effective potential, proposals to encode information in a transmon entangled with the spin of a trapped Andreev quasiparticle to escape the usual protection tradeoff, and altermagnetic Josephson junctions calculated to give tunable splitting, anharmonicity and gate times with good decoherence protection. All-optical I/O is the most consequential novelty in this set because it attacks a scaling constraint rather than a coherence one.

**TLDR: Not a new idea, and the sources assert rather than measure its advantage over rival platforms.**

## Diffusion (2/5)

Diffusion within research is already broad: these circuits appear as quantum simulators, as hybrid electromechanical platforms coupled to mechanical resonators, and as one of several platforms for single-photon switching. Simulation and design tooling is maturing in parallel, including new singular finite-element basis functions for modelling fields near conducting wedges in complex 3D geometries and instruction-set-level waveform emulation coupled to non-perturbative open-system solvers.

The barriers to diffusion beyond the laboratory are hard and physical. Wiring is the immediate one: one microwave line per qubit does not survive contact with hundreds of qubits. Materials variability is the second: dissipation is tied to a bulk property, the superfluid density, implying a material-determined coherence ceiling rather than one that better cleanroom hygiene alone can lift. Third, the environment must be controlled to an unusual degree, including radioactivity introduced during manufacture: long-lived daughters of radon-222 plate out on device and packaging surfaces throughout the fabrication and testing lifecycle, producing local alpha decays that stay active for decades and scale with chip area. That last item is a supply-chain and cleanroom-protocol constraint that gets worse, not better, as dies grow.

**TLDR: Widely used inside physics laboratories; the barriers to anything larger are materials-level and infrastructural, not software.**

## Impact (3/5)

The larger claim, that superconducting processors will deliver commercially decisive computation, is not supported or refuted by anything supplied. The one economic-adjacent framing here is energy: whether quantum machines are more efficient than classical counterparts is posed as an open question and given only the beginnings of a benchmarking framework. A score of 3 reflects demonstrated but bounded impact, not an extrapolation.

**TLDR: Demonstrated scientific value at small scale; the sources do not evidence economic impact.**

## Timing Now (0-2yr)

As a research platform superconducting qubits matter today. Processors are running variational algorithms and yielding physics results now, hybrid electromechanical and photonic uses are active, and the error models are becoming quantitatively predictive rather than descriptive.

The timing of the thing investors actually care about, a large error-corrected machine, cannot be dated from this evidence. The relevant enablers are at demonstration stage: optical I/O has been shown for two qubits, protected qubit designs are at first-realisation or theory stage, and a material-level dissipation floor has just been proposed. Treat any specific fault-tolerance date as unsupported by this source set.

**TLDR: The hardware is already a working scientific instrument; the scaling question it is judged on is not resolved by anything in these sources.**

## Overrated or underrated? Fairly rated

The platform deserves its status as the most engineering-advanced solid-state qubit: it is fabricable, controllable, measurable, and it is producing results that other simulation methods struggle with. At the same time, the 2026 literature does not look like a field polishing a solved design. It looks like a field still finding new ways for the device to fail. Within a few weeks of each other, papers report a TLS in a tunnel barrier corrupting readout by dressing the resonator, a single TLS in a coupler producing correlated non-Markovian errors across two distant qubits, measurement-induced leakage into superinductor array modes, and decades-lived alpha-emitting radon daughters plated onto packaging during manufacture whose effect scales with chip area. Correlated and area-scaling error sources are precisely the ones error correction handles worst.

The strongest counterweight is that the field is now identifying limits with predictive models rather than empirically chasing them: an empirical scaling of microwave dissipation with superfluid density gives a data-driven basis for material selection, and MIST theory matched eleven experimental error regions. Fairly rated, therefore: real, leading, and further from a settled scaling recipe than the platform's reputation implies.

## Prediction

By 30 June 2028, no published demonstration will have operated a superconducting processor of more than ten qubits with control and readout delivered exclusively over optical links, the two-qubit multiplexed result of June 2026 remaining the reference point.

## Evidence base

- 4 May 2026: review confirms superconducting qubits are Josephson-junction circuits acting as artificial atoms with anharmonic spectra, controlled via microwave cavities under circuit QED since the early 2000s, with transmon and fluxonium as the two dominant platforms.
- 4 May 2026: an empirical scaling between microwave dissipation and superfluid density, spanning amorphous films to record-quality-factor resonators, 3D cavities and transmons, identifies an intrinsic bulk loss channel independent of surface dielectric loss and an associated coherence limit.
- 5 May 2026: a TLS defect inside a transmon's tunnel barrier was shown to couple resonantly to the readout resonator, shifting its frequency and spoiling the readout signal.
- 28 May 2026: a single coherent TLS in a tunable coupler was observed coupling to two spatially distant qubits, with a reconstructed 1/f frequency-noise spectrum spanning 0.1 mHz to 1 MHz and quantum process tomography showing correlated qubit dynamics.
- 2 June 2026: long-lived radon-222 daughters plating out on device and packaging surfaces during fabrication and testing were identified as a decades-lived local alpha source whose impact scales with chip area.
- 7 June 2026: a complete optical I/O architecture achieved frequency-multiplexed optical readout of two qubits with no measurable coherence degradation and a 0.19% reduction in optically driven single-qubit gate fidelity versus microwave control.
- 16 June 2026: a nine-qubit superconducting processor with Platonic lattice connectivity was used to extract 3D Ising critical exponents from an eight-qubit encoded register via an extended variational eigensolver.

## Open questions

- Does the superfluid-density dissipation bound represent a genuine floor for transmon coherence, or can material or geometry choices circumvent the trapped-quasiparticle channel it attributes the loss to?
- How common are TLS defects that couple to two or more qubits at once, and do the resulting correlated, non-Markovian error patterns break the independence assumptions of standard error-correction thresholds?
- Can radon plate-out during fabrication and packaging be controlled cheaply enough that its area-scaling alpha background does not set an upper limit on usable die size?
- Does the 0.19% gate-fidelity penalty of optical I/O hold as the number of multiplexed channels grows from two towards hundreds, and what is the net cryogenic thermal budget compared with coaxial wiring?
- Do protected designs such as cos(2φ) ever escape the residual first-harmonic 1/f flux-noise limit measured at the flux symmetry point, or does each new protection mechanism simply expose a different dominant channel?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
