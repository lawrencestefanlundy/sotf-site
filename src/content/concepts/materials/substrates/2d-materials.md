---
type: concept
slug: 2d-materials
canonical_name: 2D Materials
aliases: []
kind: technology
parent_concepts:
- materials
- substrates
related_concepts: []
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2026-05-24-mose2-exciton-polariton-all-optical-switch]]'
- '[[2026-01-13-semianalysis-interconnects-beyond-copper]]'
frontier:
- Does the MIGS dimensional scaling law of 2026 06 16 contacts to low dimensional semiconductors physical theory a identify a contact scheme that actually reaches low, reproducible contact resistance in fabricated 2D transistors, or only explain why present ones fail?
- Can 2.2% programmable strain and 0.4 eV gap tuning 2026 06 05 high magnitude spatially programmable and sustained strain e survive transfer from two-photon-lithography test substrates to wafer-scale, CMOS-compatible processing?
- Can single quantum emitters be created at deterministic sites with reproducible spectra, so that the electronic stabilisation and Stark tuning surveyed in 2026 05 08 electronic and photonic integration of single quantum emitte become a process step rather than a per-device intervention?
- Do the MLIPs trained on 50,000 MXene DFT calculations generalise to the 1000 genuinely larger systems well enough to replace DFT in screening, and does that transfer to other 2D families given the non-universality of functionals 2026 07 01 exchange correlation functionals in 2d materials application?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 61
last_reorg_date: '2026-05-13'
descendants: []
scorecard:
  viability: 3
  drivers: 3
  novelty: 4
  diffusion: 2
  impact: 3
  timing_band: Later (5-10yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 5
sources_30d: 12
recent_mentions:
- slug: 2026-05-24-mose2-exciton-polariton-all-optical-switch
  title: New light-based switch could cut chip energy use and speed future AI photonics
  date: '2026-05-24'
  kind: web
- slug: 2026-01-13-semianalysis-interconnects-beyond-copper
  title: Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More
  date: '2026-01-13'
  kind: web
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
neighbors: []
---
**2D materials are crystals one to a few atoms thick whose electronic, optical and thermal properties can be reprogrammed by thickness, twist angle, strain and substrate choice; the 2026 literature shows the physics and the control knobs working reliably at flake scale, while contacts, growth and metrology remain the gate on anything manufacturable.**

## Summary

A two-dimensional material is a crystal that is stable at a thickness of one or a few atomic layers, held together in-plane by strong covalent bonds and out-of-plane only by van der Waals forces. That weak interlayer bonding is the whole point: sheets of different materials can be stacked in arbitrary order and at arbitrary relative rotation without lattice-matching constraints, producing "van der Waals heterostructures" whose properties are not those of any bulk parent. The families that appear across current work are graphene, the transition metal dichalcogenides (MoS2, WS2, WSe2) as semiconductors, hexagonal boron nitride (hBN) as insulator, encapsulant and colour-centre host, MXenes such as Ti2CTy for catalysis, magnetic chromium halides, and nonlinear-optical crystals such as NbOBr2.

The engineering levers are unusual. Layer number changes the band structure and the exciton dynamics: in CrCl3 the emission energy is thickness-independent but relaxation is not, giving an out-of-plane exciton diffusivity of 4.5 x 10^-6 cm2/s with a 130 meV activation barrier. Twist angle changes it again, via atomic reconstruction of the moire lattice, which underlies flat bands in twisted bilayer graphene and Wigner crystallisation in TMDs. Strain is a direct bandgap dial because these membranes tolerate elastic deformation that bulk semiconductors cannot: conformal transfer of monolayer MoS2 onto two-photon-lithography substrates gives programmable biaxial strain up to 2.2%, stable for months, tuning the gap by about 0.4 eV, roughly 25% of the intrinsic value. Substrate choice is not passive either: substrate-induced dipolar scattering is proposed as the origin of the giant nonlinear conductivities above 1 micrometre per ohm-volt measured in van der Waals heterostructures.

The parameters that decide whether any of this becomes technology are less glamorous. First, contacts: metal-induced gap states set the Schottky barrier, transfer length and contact resistance, and a new analytical model finds a universal scaling law that depends on semiconductor dimensionality and explains recent carbon nanotube and 2D device data. Second, growth: the NSF 2D Crystal Consortium user facility now tracks roughly twenty thousand samples grown by bulk crystal growth, MOCVD and MBE through a single data platform with a REST API, an indication that synthesis is still a research-scale, sample-by-sample activity. Third, prediction: standard density functional theory handles quantum confinement, anisotropic screening and van der Waals interactions poorly, exchange-correlation functionals are non-universal across 2D families, and quantitative optical properties often require GW and Bethe-Salpeter treatment.

## Viability (3/5)

The positive evidence is specific and experimental, not aspirational. Programmable strain of 2.2% with 0.13 %/micrometre spatial resolution, stable over months and extended from monolayer MoS2 to WS2-MoS2 bilayers, is a real capability with a measured outcome (about 0.4 eV of gap tuning). A twisted NbOBr2 source produces polarisation-entangled telecom photons with Bell-state fidelity above 95% and a coincidence-to-accidental ratio near 335. TMD flakes on Si3N4 waveguides can be characterised in situ using the waveguide core's own defect photoluminescence as the probe. hBN flakes measurably spread heat away from optically driven gold nanoparticles in water, verified by wavefront-microscopy nanothermometry against finite-element models.

The limits are equally clear. The spectroscopy work uses exfoliated monolayers, the waveguide work uses flakes, quantum emitters still suffer blinking, spectral wandering and charge-noise broadening that must be suppressed by electrostatic stabilisation and Stark tuning, and contact resistance in low-dimensional channels is only now getting a unified physical description. None of the supplied sources reports yield, wafer-scale uniformity or device statistics. A 3 reflects reproducible laboratory function with the manufacturing question untouched.

**TLDR: The physics and the control knobs are demonstrated repeatedly at flake scale; nothing in these sources demonstrates manufacturable devices.**

## Drivers (3/5)

On demand, the clearest statement is from the adjacent carbon nanotube review: silicon CMOS scaling faces direct source-to-drain tunnelling, an unscalable subthreshold swing and the dark silicon thermal ceiling, which motivates the search for a replacement channel material. A second pull is quantum photonics, where scalable systems need triggered, stabilised, fibre- or circuit-coupled single-photon sources rather than bulky free-space excitation with post-selection. A third is thermal management at the nanoscale, where conventional cooling fails because of limited heat transport and high interfacial resistance. Catalysis provides a fourth, with MXene surface chemistry as the target.

On supply, the enabling machinery is real but institutional rather than industrial: an NSF-supported national user facility running MOCVD, MBE and bulk growth, with about twenty thousand catalogued samples and API access to synthesis and property data; machine-learning interatomic potentials trained on 50,000 DFT calculations to escape the cost of repeated first-principles evaluation; and new metrology such as dark-field TEM extraction of 3D atomic displacements and interlayer spacing in twisted bilayers. The sources give no funding figures, market sizes or industrial commitments, so the score stays at credible rather than strong.

**TLDR: Demand is articulated as a physics dead-end in silicon and a shortage of turnkey quantum light sources; supply-side infrastructure exists but at user-facility scale.**

## Novelty (4/5)

The most quantified comparison in the set is the NbOBr2 entangled-photon source, whose brightness is roughly one order of magnitude higher than recently reported telecom sources based on TMD 2D materials, at greater than 95% Bell fidelity. Against conventional semiconductors, the strain result is the sharpest differentiator: 2.2% sustained biaxial strain and about 25% bandgap modulation is a regime silicon strain engineering does not reach, and the authors state that no prior technique achieved strain that was simultaneously above 1%, long-term stable and spatially programmable. The deterministic strain work adds predictive design, with a two-component analytical model reproducing spatially resolved bandgap shifts in complex suspended geometries to better than 12% error, and demonstrated transfer to another material.

Novelty also shows up as new physics with no incumbent to beat: exciton diffusivity that can go negative through hybridisation with acoustic plasma modes, random-matrix quantum chaos in first-principles excitonic spectra of WS2-graphene, and nonlinear conductivities whose natural scale of 1 micrometre per ohm-volt existing theory could not account for. The score is 4 rather than 5 because most of the differentiation is measured against other laboratory demonstrations, not against deployed technology.

**TLDR: Several capabilities have no bulk-semiconductor equivalent, and one photon source beats the previous 2D benchmark by about an order of magnitude.**

## Diffusion (2/5)

The adoption barriers are structural. Device demonstrations rest on exfoliated material placed by hand: a WSe2 monolayer on Si/SiO2 for ultrafast spectroscopy, MoS2 and WS2 flakes transferred onto Si3N4 waveguides, hBN flakes deposited on glass. Contacts remain a first-order problem: a general physical description of metal contacts to low-dimensional semiconductors has been elusive, and the criteria for scalable, low-resistance contacts are only now being formulated. Quantum emitters need active electronic stabilisation to avoid blinking and spectral wandering before they can serve as turnkey sources.

Supporting infrastructure is thin but improving. There were previously no experimental methods for accessing 3D atomic distributions in reconstructed twisted stacks, which the authors say significantly impeded the field. Predictive simulation is unreliable across material families because exchange-correlation functionals are non-universal for 2D systems. Data management for synthesis and characterisation has only just been centralised at one national facility. Machine-learned potentials and irradiation-damage modelling for nanofabrication design point the right way, but on this evidence diffusion beyond research laboratories has not begun.

**TLDR: Everything of interest is still built from exfoliated flakes, contacts and growth are unresolved, and even the characterisation tools are papers from this year.**

## Impact (3/5)

The upside cases are legitimate and named. If a 2D channel can replace silicon, the prize is continued logic scaling past tunnelling and dark-silicon limits. If localised TMD excitons or hBN colour centres can be electrically driven, stabilised and waveguide-coupled, the result is compact on-chip sources for quantum communication and photonic quantum information processing, with telecom-band entangled-pair generation already demonstrated in a wavelength-scale crystal. Strain-programmed bandgap landscapes open wide-spectrum optoelectronics and engineered electronic landscapes in a single monolayer. MXene surface chemistry is a candidate catalysis platform whose configuration space is now tractable via ML potentials.

The restraint is that not one of these sources reports a system-level metric: no efficiency, cost, throughput or energy figure against an incumbent. The nearest-term impact visible here is narrower and more mundane, such as hBN used as a nanoscale heat spreader in heat-sensitive biosensing, nanophotonics and microelectronics. A 3 records a broad and credible value case that the supplied evidence does not size.

**TLDR: Plausibly large in logic, quantum photonics and catalysis, but the sources assert the stakes rather than quantify them.**

## Timing Later (5-10yr)

Three clocks run at different speeds. Metrology and simulation are landing now: dark-field TEM reconstruction of twisted stacks, on-chip source-free absorption spectroscopy, 20 fs angle-resolved 2D electronic spectroscopy, MLIP benchmarks for MXene catalysis and shared synthesis data at scale. Discrete photonic and thermal components sit in the middle: entangled telecom sources with fidelity above 95% exist as devices, and hBN heat spreading is quantified experimentally, but both are flake-based.

The electronics clock is the slow one. A unified analytical description of contacts to low-dimensional semiconductors was published only in mid-2026 and is presented as clarifying, not solving, the criteria for scalable low-resistance contacts. Predictive functionals remain non-universal across 2D families. On this evidence, meaningful non-research deployment sits at the far end of a five to ten year window, with the possibility of earlier niche wins in quantum light sources and thermal layers.

**TLDR: Research tools and passive uses are usable now; logic and quantum photonic products depend on contacts and growth problems that are still being framed rather than solved.**

## Overrated or underrated? Fairly rated

The field is scientifically productive in a way that is hard to dispute: within a two-month window the supplied literature contains a deterministic strain-to-bandgap design rule accurate to better than 12%, a strain platform holding 2.2% biaxial strain for months with 0.4 eV of gap tuning, an entangled telecom source an order of magnitude brighter than the previous 2D benchmark, and a first general theory of contacts to low-dimensional channels. That is a healthy, not hype-driven, evidence base.

Where expectations should be resisted is the "silicon successor" framing. The strongest statement of that case in these sources is made on behalf of carbon nanotubes, not 2D sheets, and 2D device work here remains flake-based with unresolved contacts, unstable emitters requiring electrostatic stabilisation and synthesis still organised around a national user facility. Treated as a substrate class that will first deliver photonic, sensing and thermal components while the electronics case matures, 2D materials are priced about right. Treated as a near-term CMOS replacement, they are overrated.

## Prediction

By July 2029, published 2D-material single-photon and entangled-photon sources will still be predominantly demonstrated on exfoliated or manually transferred flakes rather than on wafer-scale grown films with reported device yield statistics.

## Evidence base

- 5 May 2026: nanostructure geometry deterministically prescribes in-plane strain in suspended Ga2Se2 membranes, with a two-component analytical model predicting spatially resolved bandgap shifts to under 12% error and demonstrated transfer to other materials.
- Strain engineering result carried in the 5 June 2026 record: spatially programmable biaxial strain up to 2.2% in monolayer MoS2 at 0.13 %/micrometre resolution, stable for months, giving about 0.4 eV of local bandgap tuning, roughly 25% of the intrinsic gap, and extended to WS2-MoS2 bilayers.
- 15 May 2026: 90-degree twisted NbOBr2 generates polarisation-entangled telecom photon pairs with Bell fidelity above 95%, coincidence-to-accidental ratio around 335, and brightness about an order of magnitude above recent TMD-based telecom sources.
- 16 June 2026: an analytical metal-induced-gap-state model yields a universal scaling law set by semiconductor dimensionality and a unified formulation of Schottky barrier height, transfer length and contact resistance, explaining recent carbon nanotube and 2D experiments.
- 17 June 2026: the NSF 2D Crystal Consortium user facility reports a data platform hosting synthesis and property data on approximately twenty thousand samples grown by bulk crystal growth, MOCVD and MBE, accessible via REST API.
- 2 June 2026: a 50,000-calculation DFT training set plus 10,000 test and 1000 larger held-out systems is used to benchmark EquiformerV2, MACE, MatRIS and UPET for forces and formation energies on Ti2CTy MXenes, addressing the cost limit of DFT for realistic catalytic conditions.

## Open questions

- Does the MIGS dimensional scaling law of identify a contact scheme that actually reaches low, reproducible contact resistance in fabricated 2D transistors, or only explain why present ones fail?
- Can 2.2% programmable strain and 0.4 eV gap tuning survive transfer from two-photon-lithography test substrates to wafer-scale, CMOS-compatible processing?
- Can single quantum emitters be created at deterministic sites with reproducible spectra, so that the electronic stabilisation and Stark tuning surveyed in become a process step rather than a per-device intervention?
- Do the MLIPs trained on 50,000 MXene DFT calculations generalise to the 1000 genuinely larger systems well enough to replace DFT in screening, and does that transfer to other 2D families given the non-universality of functionals?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
