---
type: concept
slug: silicon-nitride
canonical_name: Silicon Nitride
aliases:
- sin
- silicon-nitride
kind: material
parent_concepts:
- materials
- substrates
related_concepts: []
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-05-24-mose2-exciton-polariton-all-optical-switch]]'
- '[[2026-03-13-photonic-foundry-capacity-new-origin-to-collaborate-with]]'
- '[[2026-06-04-q-memory-site]]'
- '[[2023-09-04-sinq-csa-catapult]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-06-16-trapped-ion-landscape-2026]]'
scorecard:
  viability: 4
  drivers: 4
  novelty: 3
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
mention_count: 99
sources_7d: 2
sources_30d: 16
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-06-16-trapped-ion-landscape-2026
  title: Trapped-ion quantum computing landscape 2026 (vendors, scale, integrated photonics)
  date: '2026-06-16'
  kind: web
- slug: 2026-06-04-q-memory-site
  title: Q-Memory — company website (q-memory.tech)
  date: '2026-06-04'
  kind: web
- slug: 2026-05-24-mose2-exciton-polariton-all-optical-switch
  title: New light-based switch could cut chip energy use and speed future AI photonics
  date: '2026-05-24'
  kind: web
- slug: 2026-05-02-hybrid-bto-sin-ultra-low-power-tuning-acs-photonics
  title: Hybrid BTO-SiN ultra-low power tuning (ACS Photonics)
  date: '2026-05-02'
  kind: web
- slug: 2026-03-13-photonic-foundry-capacity-new-origin-to-collaborate-with
  title: New Origin to Collaborate with Imec to Scale Photonic IC Manufacturing in Industrial Environment
  date: '2026-03-13'
  kind: web
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
neighbors: []
---
**Silicon nitride is the low-loss, CMOS-compatible dielectric that has become the default waveguide layer for integrated photonics, carrying everything from soliton microcombs driving 300 GHz wireless links to 3D optical interposers and quantum photonic meshes.**

## Summary

Silicon nitride (Si3N4, usually written SiN in device papers) is a dielectric thin film deposited on oxidised silicon wafers and etched into waveguides. It guides light by index contrast against a silica cladding, in the same way silicon-on-insulator does, but with three differences that decide where it is used: a wider bandgap, so it is transparent from the visible through the telecom band where silicon is opaque below roughly 1.1 µm; very low propagation loss and no two-photon absorption at telecom powers, which makes it the material of choice for high-Q resonators and nonlinear optics; and no native electro-optic effect or optical gain, so it cannot modulate or emit light on its own.

That last point defines the architecture of almost every system built on it. SiN supplies the passive circuit and the active function is grafted on: thin-film lithium niobate bonded in the back end of line for 100 GHz modulators alongside Si/SiN passives and 56 GHz germanium photodetectors, barium titanate for low-power tuning <sup class="ref"><a href="https://pubs.acs.org/doi/10.1021/acsphotonics.9b00558" title="Hybrid BTO-SiN ultra-low power tuning (ACS Photonics)" rel="noopener">ref</a></sup>, dual-layer graphene for cryogenic phase modulation in quantum processors, or erbium implanted directly into the nitride to make it emit at telecom wavelengths. The same films also serve non-photonic roles, for example as the electron-transparent membrane windows in environmental TEM cells and as the dielectric stack in ferroelectric HZO transistor test structures.

The parameters that decide a SiN design are index contrast and confinement (high confinement for compact nonlinear resonators, low confinement for ultra-low-loss delay lines and links), thickness and stress in the deposited film, thermal tuning behaviour, and how the passive layer interfaces with whichever active material provides modulation or gain. Recent work shows those parameters are still being pushed: waveguides with 50 nm cores formed by filling etched glass trenches and fusion-bonding two Borofloat wafers to give a thick symmetric cladding, two-layer 3D routing to eliminate waveguide crossings, and slab-engineered mode hybridisation in rib waveguides to cancel crosstalk between neighbours in standard foundry processes.

The honest framing is that SiN is not an emerging material. It is an incumbent substrate whose capability envelope is being extended, and whose main open question is how far active function can be added without losing the fabrication simplicity that made it attractive.

## Viability (4/5)

The demonstrations in these sources are devices measured, not concepts proposed. A soliton microcomb in an integrated SiN microring generated a 300 GHz carrier that carried 10 Gbps with a bit-error rate below 1e-9, without forward error correction or offline processing. A two-layer SiN interposer realised a fully connected 12-node optical network and cut average loss per waveguide by 45.8% against a planar baseline. A programmable SiN Mach-Zehnder mesh implementing a unitary transformation was operated experimentally as a physical unclonable function. A narrowband SiN photon-pair source fed a heralded telecom single-photon scheme.

The score is held at 4 rather than 5 because the sources also expose live engineering gaps. Simulated and measured resonance frequencies of Si3N4/SiO2 microrings diverge because thermo-refractive coefficients are wrongly assumed to be non-dispersive, with a 7% variation measured across an octave from telecom to visible; design tools are still catching up with the material. There is also no wafer-scale yield, propagation-loss or volume-production data in these sources, so viability is judged on device results rather than on manufacturing evidence.

**TLDR: Working experimental hardware across communications, computing interconnect, sensing and quantum, in multiple independent groups.**

## Drivers (4/5)

On demand, the sources are explicit. The growth of artificial intelligence, cloud computing and large-scale machine learning is named as the driver for short-reach optical interconnects with large bandwidth, low power and low cost using CMOS processes, and photonic interposers are positioned as the alternative to electrical links for modern computing workloads. Separately, ultra-high-capacity wireless demand is pulling systems towards the 300 GHz band, and visible photonic circuits are being pulled by AR/VR and quantum control.

On supply, the recurring argument is that SiN sits inside standard CMOS and foundry flows: metasurface light sources are framed as a route to active sources in CMOS-compatible photonic devices, the crosstalk-cancellation method is presented as foundry-compatible in standard rib waveguides rather than requiring specialised nanostructures, and the glass-bonding route is explicitly motivated by reducing fabrication cost while keeping technological simplicity. Both sides of the market therefore point the same way.

**TLDR: Demand from AI interconnect bandwidth, THz wireless capacity, visible-band and quantum PICs; supply from CMOS-compatible foundry processes.**

## Novelty (3/5)

SiN is not better than an alternative in the way a new material is. It is the baseline. What these sources show is capability being added at its edges: erbium implanted into SiN metasurfaces gives an 18-fold photoluminescence enhancement at telecom wavelength with a near ten-fold lifetime reduction, attacking the material's lack of native emission; graphene overlays are proposed to give it phase modulation at cryogenic temperatures where conventional modulators struggle; and hydrostatic pressure up to 5 GPa was shown to shift a Fabry-Perot resonance by up to 30 nm and reduce refractive index by up to 4%, giving a tuning mechanism that adds no free carriers, in what is claimed as the first extreme-pressure-tunable polarisation-converting metasurface.

Where the sources allow a comparison, it is architectural rather than material: 3D routing cut intralayer crossings from 495 to 150, below the theoretical 153 lower bound for any all-planar layout, and cut average per-waveguide loss by 45.8%. The crosstalk work demonstrates the same technique across silicon-on-insulator and silicon nitride, treating them as peer platforms rather than ranking them. There are no quantitative loss, bandwidth or density comparisons against silicon or lithium niobate in these sources, so the score reflects genuine incremental advance without a measured margin over the alternatives.

**TLDR: The material is an incumbent, not an invention; the novelty is in what is now being added to it, and head-to-head benchmarks are thin.**

## Diffusion (4/5)

Diffusion is visible in the source set itself: SiN appears as the substrate in unrelated work from independent groups covering THz communications, HPC interposers, hardware security, single-photon sources, metrology and cryogenic quantum modulators. It also appears as the passive layer inside platforms named after other materials, for instance Si/SiN passives with low-loss fibre interfaces alongside bonded thin-film lithium niobate modulators in a single-chip transceiver process. That is the signature of a substrate that has already diffused.

The residual barriers are specific. First, the platform depends on heterogeneous integration for modulation and gain, and those processes carry incompatibility risk, which is precisely why the lithium niobate work had to be moved to the back end of line after CMOS processing was complete. Second, test and diagnostics lag: visible-band PICs lacked a nondestructive high-resolution diagnostic comparable to infrared reflectometry until spectral-domain OCT was adapted, giving 8 µm axial resolution in silicon nitride with 50 dB dynamic range. Third, fabrication variability is real enough that uncontrollable waveguide variation is exploitable as a security primitive, which is useful for PUFs and unhelpful for everything else.

**TLDR: Already the shared passive layer across silicon photonics, quantum and interconnect work; the barrier is active function, not acceptance.**

## Impact (4/5)

If photonic interposers displace electrical links inside AI and HPC systems, the routing layer that makes dense low-crossing topologies possible is a structural component of that market, and the demonstrated 3D SiN scheme is described as scalable to higher node counts, more layers and other wavelengths. Microcomb-driven THz links open a new spectral band for wireless capacity, with the analysis of error-free threshold power pointing to free-space feasibility. In quantum information the platform supplies both photon-pair generation and, prospectively, the low-loss compact cryogenic modulators that fully cryogenic photonic processors require.

The reason this is not a 5 is that the value is heavily shared. SiN provides the low-loss circuit; the differentiated performance in most of these systems comes from the bonded or implanted active material. Economically, substrate suppliers usually capture less than the component makers built on top of them, and none of these sources gives cost, volume or market data to argue otherwise.

**TLDR: It is the connective tissue for optical interconnect, microcomb sources and quantum photonics; the value accrues broadly rather than in one product.**

## Timing Now (0-2yr)

The baseline capability is present now. SiN passives are integrated into a CMOS-compatible transceiver platform alongside 56 GHz germanium photodetectors and 100 GHz modulators, and the crosstalk-cancellation technique is presented as usable in standard foundry rib waveguides without specialised nanostructures, which is a short path to adoption.

The newer layers are earlier. The 3D interposer is described as a prototype, the low-confinement glass-bonded waveguides are a proof of concept with straight waveguides only, the cryogenic graphene modulators are a theoretical investigation, and the THz link was run back-to-back in a short waveguide configuration rather than over free space. Expect those to mature over roughly two to five years, on top of a substrate that is already shipping.

**TLDR: Passive SiN circuits are already in use today; the active and 3D extensions in these sources are prototypes moving in the two to five year window.**

## Overrated or underrated? Underrated

Attention in integrated photonics tends to follow the active material of the moment, lithium niobate, barium titanate, graphene, diamond chiplets. In this source set, every one of those appears bolted onto or beside a silicon nitride circuit: TFLN modulators over Si/SiN passives, BTO for low-power tuning of SiN <sup class="ref"><a href="https://pubs.acs.org/doi/10.1021/acsphotonics.9b00558" title="Hybrid BTO-SiN ultra-low power tuning (ACS Photonics)" rel="noopener">ref</a></sup>, graphene phase modulators on SiN waveguides, diamond quantum micro-chiplets integrated into PICs characterised in silicon nitride. The substrate is doing the structural work and getting none of the billing.

The counter-argument is fair and should be stated: because SiN cannot modulate or emit, it will always be a component of a hybrid stack, and the hard engineering, plus most of the margin, sits in the bonding and the active layer. An investor should treat SiN as a platform bet on integrated photonics volume rather than as a differentiated technology in itself. But the erbium metasurface result, giving an 18-fold PL enhancement in the nitride itself, is a signal that even the gain constraint is not fixed.

## Prediction

By June 2028, a silicon nitride photonic interposer with more than two routing layers or more than 12 fully connected nodes will be reported with measured average per-waveguide loss below the equivalent all-planar routing baseline, extending the 45.8% reduction demonstrated in April 2026.

## Evidence base

- 14 May 2026: error-free 10 Gbps transmission in the 300 GHz band, BER below 1e-9 without FEC, using a soliton microcomb in an integrated SiN microring.
- 14 Apr 2026: a two-layer 3D SiN photonic interposer cut intralayer crossings from 495 to 150 for a 12-node fully connected network, below the 153 all-planar lower bound, and reduced average per-waveguide loss by 45.8%.
- 5 May 2026: Er3+ implanted into Si3N4 nanocylinder metasurfaces gave roughly 18-fold room-temperature photoluminescence enhancement at telecom wavelength with a near ten-fold lifetime reduction, attributed to the Purcell effect.
- 8 Dec 2025: back-end-of-line die-to-wafer bonding of thin-film lithium niobate onto an active silicon photonics platform delivered Si/SiN passives, 56 GHz Ge photodetectors and 100 GHz TFLN modulators on one chip.
- 5 Jun 2026: measured 7% variation in Si3N4 and SiO2 thermo-refractive coefficients across a telecom-to-visible octave, with the material contribution to dneff/dT 1.3 times that from modal confinement, explaining simulation-measurement discrepancies in microrings.
- 15 May 2026: hydrostatic pressure to 5 GPa shifted a Fabry-Perot resonance in SiN nanostructures by up to 30 nm with a 4% relative index decrease, enabling a pressure-tunable polarisation-converting metasurface.
- 29 May 2026: low-confinement SiN waveguides with 50 nm core height and 1.3 to 3.5 µm widths were formed by trench-filling and thermal fusion bonding of Borofloat 33 glass wafers to give thick symmetric cladding.

## Open questions

- Does erbium-implanted Si3N4 reach net optical gain on chip, or does it stop at photoluminescence enhancement of roughly 18-fold with a ten-fold lifetime reduction?
- Can back-end-of-line bonding of active materials such as TFLN onto finished SiN and silicon photonics be run at commercial yield, or does the trench-based die-to-wafer approach stay a laboratory route?
- Once dispersive thermo-refractive coefficients are included, with 7% variation measured across a telecom-to-visible octave, how much do existing octave-spanning microcomb and phase-matching designs need to be revised?
- Does the glass fusion-bonding route for 50 nm-core low-confinement waveguides survive the transition from straight test structures to functional circuits with bends and couplers?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
