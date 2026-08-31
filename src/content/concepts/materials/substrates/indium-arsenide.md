---
type: concept
slug: indium-arsenide
canonical_name: Indium Arsenide
aliases:
- InAs
- indium arsenide
parent_concepts:
- compound-semiconductors
related_concepts:
- indium-antimonide
- gallium-antimonide
- indium-gallium-arsenide
- indium-phosphide
- topological-qubits
- topological-insulators
sources: []
scorecard:
  viability: 4
  drivers: 3
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 25
sources_7d: 2
sources_30d: 5
recent_mentions: []
neighbors:
- slug: indium-antimonide
  name: Indium Antimonide
  path: /materials/substrates/indium-antimonide/
  macro: materials
- slug: gallium-antimonide
  name: Gallium Antimonide
  path: /materials/substrates/gallium-antimonide/
  macro: materials
- slug: indium-gallium-arsenide
  name: Indium Gallium Arsenide
  path: /materials/substrates/indium-gallium-arsenide/
  macro: materials
- slug: indium-phosphide
  name: Indium Phosphide (InP)
  path: /materials/substrates/indium-phosphide/
  macro: materials
- slug: topological-qubits
  name: Topological Qubits (Microsoft Majorana)
  path: /compute/quantum-computing/topological-qubits/
  macro: compute
- slug: topological-insulators
  name: Topological Insulators
  path: /materials/advanced-materials/topological-insulators/
  macro: materials
---
**Indium arsenide is a narrow-gap III-V semiconductor that has become the default host material for three separate frontier device families: mid-infrared photodetectors, epitaxial quantum-dot photon sources, and superconductor-semiconductor hybrid quantum devices including Microsoft's tetron qubits.**

## Summary

Indium arsenide (InAs) is a binary III-V compound semiconductor, grown epitaxially (typically by molecular beam epitaxy) either as a bulk layer, as a quantum well inside a heterostructure, or as self-assembled nanoscale islands (quantum dots) embedded in a wider-gap host such as GaAs or InP. It is used as a substrate, as an active layer, and as a lattice-matching reference for other epitaxial materials such as Heusler compounds grown for spintronics.

Three properties explain almost all of its current use. First, its narrow bandgap puts absorption and emission in the mid-infrared, which is why InAs/InAsSbP barrier detectors address the 3.0-3.7 µm band and why InAs p-i-n diodes are candidates for thermoradiative energy harvesting, where a diode radiates to a cold sky and generates power. Second, it makes clean, high-transparency contact with superconductors and carries strong spin-orbit coupling, which is why hybrid Al/InAs and InAs/Pb structures dominate the superconductor-semiconductor literature: tetron qubits, Josephson junction arrays, gate-tunable Josephson oscillators, microwave probes of exotic superconducting states, and InAs/GaInSb quantum spin Hall insulators. Third, InAs islands strain-nucleate into near-ideal single-photon emitters when grown on GaAs or InP, giving InAs/GaAs and InAs/InGaAs quantum dots and, at telecom wavelengths, InAs dots in InP microdisks.

The parameters that decide InAs in each role differ. For detectors it is bandwidth, room-temperature sensitivity and structural simplicity. For thermoradiative and energy-harvesting diodes it is reverse saturation current relative to the radiative limit and breakdown voltage, both of which are still far from ideal. For quantum photonics it is dot inhomogeneity, cavity quality factor and the refractive-index mismatch that complicates coupling III-V gain material to standard silicon waveguides. For hybrid quantum devices it is interface quality, parasitic bulk conduction and electrostatic control.

## Viability (4/5)

The sources describe InAs as a "mature material platform" and back that with measurements rather than projections. An InAs/InAsSbP nBp barrier detector 121 µm in diameter reached a -3 dB electrical bandwidth of 2.4 GHz and -20 dB bandwidth of 8.0 GHz at room temperature, with photodetection above 19 GHz, achieved without cascaded structures or type-II superlattices. An InAs-Pb tetron device showed a 20 second parity lifetime. InAs quantum dots in an InP microdisk gave emission directionality of 0.985 with cavity enhancement of 3.3 in the 1260-1360 nm telecom band, and an InAs/GaAs dot supplied deterministic single photons for a Bell-like inequality violation of 380 standard deviations. GaAs photonic crystal split cavities designed for two InAs dots achieved average Q of at least 20,000, limited by e-beam lithography rather than by sidewall scattering.

The counterweight is that in the least developed application the material is far from adequate: MBE-grown InAs thermoradiative diodes showed breakdown voltages above only 0.3 V and reverse saturation current densities 200 times the radiative limit, even at the optimised growth condition of 450 C with As2 flux around three times stoichiometry. Viability is therefore high for the material as a platform and application-specific below that. A 5 is not earned because nothing in these sources demonstrates a manufactured, qualified product.

**TLDR: A mature epitaxial platform with hard measured device results across several independent fields, though some target applications remain far from their physical limits.**

## Drivers (3/5)

On demand, the sources name specific pulls. Fast mid-wave infrared photodetection is driven by high-rate free-space optical communication and optical frequency comb spectroscopy, and the authors state that commercial availability of multi-GHz room-temperature detectors in this band "remains scarce", which is a demand signal and a supply gap in one sentence. Compact, energy-efficient 1.3 µm integrated lasers are described as a critical focus for data communications and optical interconnects, with InAs/(Al)GaAs quantum dots chosen for their temperature insensitivity. Quantum information processing pulls on both the photonic side, where chiral telecom-band interfaces are called essential building blocks for deterministic gates and entanglement generation, and the solid-state side via tetrons.

On supply, the enabling capability is III-V molecular beam epitaxy and its refinement: growth-parameter optimisation is the explicit subject of the thermoradiative diode work, and high-quality Al/InAs and InAs/GaInSb/InAs heterostructures on AlSb quasi-substrates are being produced by multiple independent groups. There is no volume, price or capacity information in any source, so the score stops at 3.

**TLDR: Demand pull is clearly articulated in several directions; the sources contain no market data, so the force behind it cannot be sized.**

## Novelty (3/5)

The honest reading of these sources is that InAs is the reference material against which newer candidates are measured. Predicted magnetic Weyl semimetals such as Co3Sn2S2 give strong, broadband, magnet-free nonreciprocal thermal radiation that outperforms "the conventional semiconductor such as InAs", which requires an external magnetic field. In a DFT survey of zincblende III-V and II-VI semiconductors, aluminium-containing compounds, particularly AlSb, gave the largest shift-current response, with InAs among the also-rans.

Where novelty is real, it is device-level rather than material-level, and it is quantified. The MWIR barrier detector result is stated as the best in its class confirmed optically, and notably obtained with a simpler structure than the cascaded or type-II superlattice designs it competes with. InAs quantum dots supply the first reported chiral quantum interface in the original telecom band, an interface the authors say did not previously exist. InAs/(Al)GaAs dot lasers trade better temperature insensitivity for harder III-V/Si coupling because of the high refractive index of (Al)GaAs. That is a genuine but bounded advantage over the alternatives named.

**TLDR: InAs is more often the incumbent benchmark than the new thing, and in two documented comparisons other materials beat it.**

## Diffusion (3/5)

Against that, the detector work explicitly frames the mature InAs platform as opening perspectives for accessible devices, while conceding that commercial availability of comparable detectors is currently scarce. Most of the hybrid quantum work requires cryogenic and often high magnetic-field operation, which limits diffusion outside laboratories and, for the telecom dot interface, required a strong magnetic field to tune transitions into the cavity.

**TLDR: Integration and process-control barriers are specific and documented, and one source states outright that the commercial supply is thin.**

## Impact (4/5)

The breadth is the argument. If the mid-infrared detector results transfer to product, the value is real but contained: faster free-space optical links and comb spectroscopy instruments. If InAs quantum dot lasers integrate cleanly on standard 220 nm silicon, the payoff is larger, because 1.3 µm on-chip sources address data-centre interconnect volumes. The asymmetric term is the hybrid superconductor-semiconductor stack: a 20 second parity lifetime in an InAs-Pb tetron is a measured milestone on a fault-tolerance route whose success would reset quantum computing economics, and the same material system underpins tunable Josephson junction arrays, gate-controlled microwave comb sources for cryogenic electronics and quantised helical edge transport.

The discount is that InAs is an enabling substrate, not a proprietary technology, and in some functions it is already being displaced on paper by better materials. No source in this set quantifies commercial or economic value, so the impact judgement rests on the technical significance of the demonstrations only.

**TLDR: Modest incremental value in most niches, but InAs is the host material under one of the highest-stakes quantum computing routes on record.**

## Timing Now (0-2yr)

InAs needs no waiting as a platform. Room-temperature multi-GHz mid-infrared detection has been demonstrated on it now, and InAs quantum dots are a working component in current quantum optics experiments. The near-term question for these is supply and packaging rather than physics, given the noted scarcity of commercial devices.

The applications that would make InAs strategically important are later. Topological qubits are at single-device parity-lifetime characterisation; quantum spin Hall devices are at the stage of proving that electrostatic control suppresses parasitic conduction; the CMOS-compatible dot laser is still a simulation; and thermoradiative diodes are two orders of magnitude off their radiative limit. Anyone investing on the quantum thesis should plan on a Later horizon even though the material itself is available today.

**TLDR: The material is already in productive use today; the transformative applications sit five to ten years out.**

## Overrated or underrated? Fairly rated

InAs is infrastructure. It is priced and understood as a mature III-V platform, and the evidence here matches that: multiple independent groups get good results from it, the growth recipes are being tuned rather than invented, and where a better material exists for a given function the literature says so plainly, as with magnetic Weyl semimetals for magnet-free nonreciprocal thermal radiation and AlSb for shift-current generation. There is no hidden mispricing to exploit at the material level.

The useful position is that claims should be read one layer down. The interesting variance is not "is InAs good" but which device family converts its properties into a product: the barrier detector, whose 2.4 GHz room-temperature bandwidth was obtained with an unusually simple structure, the telecom chiral interface at 0.985 directionality, or the tetron. If forced to flag an underappreciated element, it is that MBE process control, not device concept, is the binding constraint in at least two of these lines.

## Prediction

By 31 December 2028, at least one commercially catalogued room-temperature photodetector for the 3.0-3.7 µm band built on the InAs platform will be specified at a -3 dB electrical bandwidth of 2 GHz or above, closing the availability gap noted in June 2026.

## Evidence base

- 6 May 2026: MBE-grown 1x1 mm2 InAs p-i-n thermoradiative diodes grown at 450 C reached breakdown voltages above 0.3 V but reverse saturation current densities 200 times the radiative limit.
- 14 May 2026: single photons deterministically generated from an InAs/GaAs quantum emitter produced a Bell-like noncontextual hidden-variable inequality violation of 380 standard deviations.
- 3 June 2026: a 20 second parity lifetime was reported in an InAs-Pb tetron device.
- 17 June 2026: a 121 µm diameter InAs/InAsSbP nBp barrier detector achieved 2.4 GHz -3 dB and 8.0 GHz -20 dB bandwidth at room temperature in the 3.0-3.7 µm band, with detection above 19 GHz, described as the best in its class confirmed optically on a mature InAs platform whose commercial supply remains scarce.
- 22 July 2026: dual-gated InAs/GaInSb/InAs trilayer quantum wells on AlSb quasi-substrates showed an insulating bulk and quantised edge resistance robust over a broad electric-field range.
- 24 July 2026: InAs quantum dots coupled to a waveguide-coupled InP microdisk gave 3.3x cavity enhancement and 0.985 emission directionality in the 1260-1360 nm telecom band, reported as the first chiral quantum interface at telecom wavelengths.
- 16 June 2026: first-principles work predicts magnetic Weyl semimetals outperforming InAs for magnet-free nonreciprocal infrared thermal radiation.

## Open questions

- Can MBE growth optimisation close the gap between InAs thermoradiative diodes and the radiative limit, currently a factor of 200, and raise breakdown voltage well above 0.3 V?
- Does the 20 second parity lifetime measured in a single InAs-Pb tetron hold when the same stack is scaled to multi-qubit arrays with routing and readout?
- Will the proposed epitaxial design for coupling InAs/(Al)GaAs quantum dot gain to 220 nm silicon waveguides survive fabrication, or does CMOS compatibility force a different gain material?
- In functions where InAs is the incumbent benchmark, such as nonreciprocal thermal radiation, do the predicted alternatives (magnetic Weyl semimetals) actually reach device-grade material quality?

---
*Assessment drafted 2026-08-31 from up to 16 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
