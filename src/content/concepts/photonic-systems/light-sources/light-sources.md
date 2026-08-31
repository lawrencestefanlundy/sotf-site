---
type: concept
slug: light-sources
canonical_name: Light Sources
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2026-05-02-energetiq-euv-light-sources]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
descendants:
- dfb-dbr-lasers
- external-laser-source
- frequency-combs
- laser-display-light-engines
- lasers
- quantum-cascade-lasers
- single-photon-sources
- vcsels
mention_count: 71
sources_7d: 0
sources_30d: 12
recent_mentions:
- slug: 2026-05-02-energetiq-euv-light-sources
  title: Energetiq EUV light sources
  date: '2026-05-02'
  kind: web
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2023-08-31-e13-chiplets-how-chip-lego-is-driving
  title: '🔮 E13: Chiplets - How Chip Lego is Driving AI Progress'
  date: '2023-08-31'
  kind: substack
neighbors: []
---
## Physics / mechanism

A light source converts pump energy (optical, electrical, chemical or kinetic) into an emitted optical field with defined spectral, spatial, temporal and quantum-statistical properties. Three mechanism families dominate current research. In stimulated-emission sources, a gain medium inside a resonator produces coherent output above threshold, and the resonator geometry sets mode spacing, linewidth, directionality and mode selection. At the nanoscale, resonators can be coupled: optically pumped ZnO nanowire lasers separated by gaps below 10 nm exhibit full and partial frequency locking, in which all or a subset of lasing modes align, and coupling can suppress the multi-mode emission of the individual wires to yield single-mode operation, with the locking regime selected by spatially controlling the excitation frequency locking in lasing zno nanowire pairs. In dielectric microcavities of arbitrary boundary shape, the ray dynamics can be tuned from regular to fully chaotic, which reshapes the underlying wavefunctions and hence the emission pattern; "chaos-assisted light emission" couples evanescently localised modes to the far field via chaotic orbits, the lasing analogue of chaos-assisted tunnelling chaotic billiard lasers.

In quantum light sources the emitter is a single dipole or a nonlinear medium, and the surrounding nanostructure controls extraction efficiency and the local density of optical states. Circular Bragg gratings (CBGs) around deterministically positioned GaAs quantum dots provide broadband Purcell enhancement and directional out-coupling; a fabrication-minimal route using aspect-ratio-dependent etching produces monolithic free-standing CBG cavities in a single top-down step, avoiding the strain and scalability limits of multi-layer processing and flip-chip bonding free standing circular bragg gratings enabling efficient gaa. Positioning accuracy is the limiting variable: room-temperature AFM-assisted nano-oxidation lithography placed dots with a radial displacement of 51(28) nm, and the resulting free-standing asymmetric CBGs gave a 245-fold photoluminescence enhancement while retaining fine-structure splitting comparable to bulk dots, which matters for polarisation-entangled pair emission deterministic positioning of circular bragg gratings using a. Emitter growth is the other lever: local droplet etching forms symmetric nanoholes (in-plane aspect ratio 1.14) in In0.52Al0.48As, filled with InxGa1-xAs to give low-density (10^9 cm^-2) telecom-band dots local droplet etching assisted quantum dot epitaxy for telec. Dopant-based emitters follow the same logic: Er3+ implanted into Si3N4 nanocylinder arrays supporting Mie-type resonances showed a photoluminescence enhancement factor of about 18 at 390 nm cylinder radius after annealing, with a near ten-fold lifetime reduction identifying the Purcell effect as the dominant mechanism strong enhancement of er3 emission at room temperature in si.

Nonlinear parametric sources need no population inversion. Spontaneous parametric down-conversion in subwavelength nanostructures generates photon pairs whose directionality and spectral distribution are set by the resonator modes rather than by phase matching over a long crystal efficient photon pair emission from a nanostructured resonat. In van der Waals NbOBr2, the second-order nonlinearity produces correlated pairs, and a 90-degree twisted stack induces quantum interference between the two layers' generation amplitudes, yielding polarisation-entangled telecom photons tunable via pump polarisation entangled telecom photon generation using twisted van der wa. Resonant four-wave mixing in alkali vapour exploits the large nonlinearity of Rb to reach wavelengths that lack convenient laser gain: a chip-scale micromachined cell produced roughly 20 µW of continuous-wave blue light over a very short interaction length with a measured linewidth of about 1 MHz, and outperformed a glassblown cell in coherent blue-light generation efficiency despite the shorter path nonlinear frequency translation in micromachined rb vapor ce.

Free-electron sources decouple wavelength from any material resonance. Seeded free-electron lasers imprint temporal coherence from an external laser onto a relativistic electron bunch; a demonstration reached fully coherent short-wavelength output driven by a single sub-microjoule seed, against conventional schemes that demand hundred-megawatt peak-power seed lasers and, for echo-enabled harmonic generation, dual-modulator complexity fully coherent short wavelength free electron laser driven b. Smith-Purcell radiation from electrons passing over a periodic structure offers a further route: using a non-chiral, non-resonant silicon grating and converting the transverse spin angular momentum of electron-induced evanescent waves into longitudinal form, broadband tunable chiral emission was obtained with a degree of polarisation of 0.87, without relying on metasurface phase engineering or resonant mode interference observation of the inherent chiral smith purcell effect via .

## Competitive landscape

| Approach | Emission type | Reported figure of merit | Source |
|---|---|---|---|
| Coupled ZnO nanowire lasers | Coherent, mode-locked | Frequency locking at gaps < 10 nm; single-mode from coupled pair | frequency locking in lasing zno nanowire pairs |
| GaAs QD in free-standing CBG | Deterministic single photons / pairs | 245-fold PL enhancement; 51(28) nm positioning | deterministic positioning of circular bragg gratings using a |
| Er3+ in Si3N4 metasurface | Telecom-band luminescence | PL enhancement ~18; ~10x lifetime reduction | strong enhancement of er3 emission at room temperature in si |
| Nanostructured SPDC resonator | Photon pairs | First measurement of directional and spectral emission properties | efficient photon pair emission from a nanostructured resonat |
| Twisted NbOBr2 stack | Polarisation-entangled telecom pairs | Entanglement via 90-degree twist interference, pump-polarisation tunable | entangled telecom photon generation using twisted van der wa |
| Chip-scale Rb four-wave mixing | CW blue and mid-IR | ~20 µW blue, ~1 MHz linewidth | nonlinear frequency translation in micromachined rb vapor ce |
| Seeded FEL | Coherent EUV / X-ray | Full coherence from sub-microjoule seed | fully coherent short wavelength free electron laser driven b |

Deterministic emitters (quantum dots in cavities) and probabilistic parametric sources (SPDC in nanostructures or twisted crystals) address the same quantum-communication use case with different trade-offs: the former requires nanometre-scale spatial registration between emitter and resonator, the latter requires no positioning but inherits Poissonian pair statistics. Sources based on free electrons occupy a separate regime where no gain material exists at the target wavelength, at the cost of accelerator-scale infrastructure. Emission directionality itself is becoming an engineered property: two phase-programmable atoms coupled to a spinning whispering-gallery-mode resonator produced bright antibunched emission in one direction and bunched emission in the other, with correlation and brightness isolations up to 65 dB and 17.3 dB respectively quantum interference amplifies weak chirality into giant qua.

## Evidence base

- 5 May 2026: optical coupling and frequency locking demonstrated between ZnO nanowire lasers at gaps below 10 nm, including suppression of multi-mode lasing into single-mode emission in a coupled pair frequency locking in lasing zno nanowire pairs.
- 5 May 2026: monolithic free-standing circular Bragg grating cavities with deterministically positioned GaAs quantum dots realised via single-step aspect-ratio-dependent etching, avoiding flip-chip bonding and multi-layer processing free standing circular bragg gratings enabling efficient gaa.
- 5 May 2026: Er3+-implanted Si3N4 nanocylinder metasurfaces gave ~18x room-temperature PL enhancement at 390 nm radius with a near ten-fold lifetime reduction attributed to the Purcell effect strong enhancement of er3 emission at room temperature in si.
- 5 May 2026: micromachined Rb vapour cell generated ~20 µW CW blue light with ~1 MHz measured linewidth via resonant four-wave mixing, exceeding a glassblown cell's efficiency at shorter interaction length nonlinear fr

*Synthesised 2026-08-31 from 12 KB sources by the resynth pipeline; citations are KB source slugs.*
