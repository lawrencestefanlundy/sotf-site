---
type: concept
slug: piezoelectric
canonical_name: Piezoelectric
aliases: []
kind: technology
parent_concepts:
- materials
- functional-layers
related_concepts: []
sources:
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
scorecard:
  viability: 4
  drivers: 4
  novelty: 4
  diffusion: 3
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Underrated
scorecard_status: draft
mention_count: 57
sources_7d: 1
sources_30d: 10
recent_mentions:
- slug: 2023-08-25-e12-nanomechanical-computing-gears
  title: '🔮E12: Nanomechanical Computing- Gears of Space War? Old Ideas at New Scales'
  date: '2023-08-25'
  kind: substack
neighbors: []
---
**Piezoelectricity is the linear coupling between strain and electric polarisation in non-centrosymmetric crystals, and it is currently being re-engineered as a thin-film functional layer for millimetre-wave RF filters, programmable photonics, cryogenic quantum hardware and cell-scale acoustic tools.**

## Summary

A piezoelectric material converts mechanical strain into electric polarisation and, in reverse, converts an applied field into strain. The strength of the coupling is set by the piezoelectric tensor (commonly quoted as the coefficient d33 in pC/N, or e33 in the stress form), the elastic stiffness C33 and the clamped permittivity. These are not independent: one 2026 analysis resolves a long-standing gap between first-principles permittivity for scandium aluminium nitride (about 11.7) and measured values near 15 by showing the difference is the inverse piezoelectric effect inflating the lattice, with an effective permittivity of epsilon_33^S + e_33^2/C_33. A parallel theory paper finds that in strongly polar wurtzites (AlN, AlScN, AlBN, GaN, ZnO) electrostriction and elastic moduli are themselves polarisation-dependent, so the piezoelectric coefficient is strongly nonlinear in polarisation, including the counterintuitive case where reducing polarisation increases the strain response.

As a functional layer, the interesting question is not whether the effect exists but which material can be deposited on a wafer, at what coupling, with what loss, and whether it survives the surrounding process. Three materials families dominate the 2026 record here. Aluminium scandium nitride, patterned into periodically polarised (P3F) stacks, has produced 19 GHz bulk acoustic wave ladder-lattice filters with 1.3 dB minimum insertion loss, 6.26% fractional 3 dB bandwidth, 30 dB average out-of-band rejection and a 348 x 476 micrometre footprint, converting single-ended to balanced signals without a balun. Thin-film barium titanate has been shown as surface acoustic wave resonators with effective electromechanical coupling k2eff of 0.14 at 5.2 GHz, operation to 7.8 GHz, an extracted d33eff of 53 pC/N comparable to bulk BTO, and 100 ns ferroelectric switching for reconfigurable front-ends, characterised from room temperature down to millikelvin. Potassium sodium niobate, long celebrated in bulk ceramics but blocked from microelectronics by thermodynamic stability and planar process incompatibility, has been reworked on 8-inch wafers, where Mn-doped films need a Na-rich composition above 70 at.% (not the bulk equimolar optimum) to suppress pyrochlore and phase segregation and give fully (001)-oriented columnar growth.

The application pull is broad rather than concentrated. Piezoelectric actuators sit under silicon nitride waveguides in a fully monolithic, all-CMOS piezo-optomechanical photonic platform, with 200 mm photonic wafers built by back-end-of-line processing directly on completed CMOS driver wafers, motivated by architectures needing thousands to millions of reprogrammable photonic devices per chip. In quantum hardware, a piezoelectric actuator provides the feedback path that cools two translational modes of a magnetically levitated milligram sensor to below 2 picometre amplitude and below 10 mK, at Q factors of 3.8 x 10^6 and 5.5 x 10^6, and a piezoelectric-2DEG heterostructure is analysed as a quantum-limited acoustoelectric phonon amplifier. At the low-glamour end, a single piezoelectric transducer plus a model-free control algorithm delivers two-dimensional manipulation of individual cells across three cell lines, and a piezo-driven micropipette loads particles from 170 nm to 6 micrometres into in-vacuum optical traps with trapping efficiency as high as 93%.

## Viability (4/5)

What holds this below 5 is that the highest-coefficient materials remain the least viable in process. KNN's own literature is described as a rollercoaster, with microelectronics integration lagging because of thermodynamic stability and poor planar process compatibility, and the fix required abandoning the bulk equimolar composition for Na-rich films above 70 at.%. There is also a measurement hygiene problem: series parasitic components can produce apparently ferroelectric D-E hysteresis in non-ferroelectric capacitors even under the double-wave method, and suspicious published loops have been identified, with strain-field (S-E) loops argued to be the more reliable proof. Some fraction of claimed piezo/ferroelectric performance in the literature should be treated as unverified.

**TLDR: Device-level results at 19 GHz and wafer-scale integration are already in hand; the newest materials routes are not.**

## Drivers (4/5)

On demand: the RF pull is explicit, with the 19 GHz single-ended-to-balanced topology aimed at interfacing differential antennas directly to single-ended amplifiers and removing baluns and other passives from the front-end. The photonics pull is stated as thousands to millions of reprogrammable devices per chip for AI, sensing and quantum computing, with piezo-optomechanical actuation selected for low power, high speed, cryogenic compatibility and optical transparency from ultraviolet to infrared. The energy-harvesting pull is attributed to wearables, soft robotics and IoT systems needing inorganic piezoelectrics that scavenge weak biomechanical energy. Biomedical tooling adds a smaller but real channel via acoustofluidic single-cell control from one transducer.

On supply: the enabling development is that piezo layers are now being demonstrated at production wafer formats and inside conventional flows, with Mn-doped KNN on 8-inch wafers and 200 mm photonic wafers built by back-end-of-line processing on completed CMOS driver wafers. Theory and characterisation supply is also improving, from closed-form treatment of the electromechanical contribution to permittivity to automated extraction of composition-property pairs from figures in the literature, which addresses the data bottleneck for screening these compositions. The counter-driver is that piezoelectric stacks are themselves an obstacle for low-loss microwave hybrid quantum devices, which is why a 3D integration route with 10 micrometre pitch indium bumps and NbN films was developed to keep single-photon internal quality factors above 10^5.

**TLDR: Demand from millimetre-wave RF, million-element programmable photonics and cryogenic quantum hardware; supply from 8-inch and 200 mm process demonstrations.**

## Novelty (4/5)

Judged against what it replaces, the gains are specific. In RF, the P3F AlScN filters remove baluns and passive matching components entirely while holding 1.3 to 1.58 dB insertion loss and 30 to 33 dB rejection at 19 GHz in roughly 0.17 to 0.19 mm2. In photonics, the claimed first is monolithic co-fabrication of piezo-optomechanical circuits with commercial CMOS control electronics, a combination previously not demonstrated, and the case against incumbent modulation is low power, high speed, cryogenic operation and broadband transparency. Thin-film BTO's contribution is preserving bulk-like d33eff (53 pC/N) in a film while adding fast 100 ns ferroelectric reconfiguration and millikelvin operation, which bulk BTO characterisation of past decades did not cover.

On mechanism, the sources make a credible claim of new degrees of freedom rather than incremental optimisation. Chirality engineering is presented explicitly as a departure from composition, defect, strain and orientation control, with piezoresponse force microscopy resolving a consistent enantiomeric difference in selenium nanowires of identical composition. The wurtzite electrostriction work overturns the standard assumption that piezoelectric coefficients scale linearly with polarisation, opening the possibility that lowering polarisation raises strain response. Thermally driven polar-state reconfiguration in Li-substituted NaNbO3 raises Curie temperature and hardens the piezoelectric response through lattice geometry alone. These are early-stage: coefficient differences and design principles, not devices. Note the citation for the electrostriction paper is.

**TLDR: The effect is old; what is new is coupling strength at millimetre-wave frequencies, CMOS-monolithic actuation, and mechanisms beyond composition tuning.**

## Diffusion (3/5)

Two of the sources describe the barriers in their own words. KNN's decades-long failure to reach microelectronics is attributed to thermodynamic stability issues and poor planar process compatibility, and the successful 8-inch result required rewriting the phase diagram for the thin-film case, suppressing pyrochlore formation and chemical phase segregation with a Na-rich stoichiometry. In hybrid quantum circuits, exotic and complex material stacks including piezoelectrics make low microwave loss hard to achieve, which is precisely why a separate 3D integration process with indium bump interconnects was built rather than co-locating the materials. Multi-domain microstructure is a further complication: extracting d33eff for thin-film BTO required finite-element modelling of the domain structure alongside measurement.

The positive diffusion signals are that the hardest integration step has now been shown at least once. Photonic wafers were built at 200 mm directly on finished CMOS driver wafers using back-end-of-line processing, connecting piezoelectric actuators to a high-density driver array. Low-end diffusion is easier still: acoustofluidic single-cell control uses one piezoelectric transducer and a model-free algorithm requiring no prior calibration or physical model, and observing strain-field loops has been reduced to an inexpensive electret microphone plus a small circuit extension. The sources give no information on yield, cost or qualification at volume, so 3 is where the evidence stops.

**TLDR: Integration is the whole barrier: process compatibility, microwave loss and domain structure, not the physics.**

## Impact (4/5)

The value case rests on position rather than performance headroom. Piezoelectric films are the acoustic element in filters at frequencies where communications systems are moving, and the 19 GHz demonstration is described as competitive for wireless communications filters while eliminating discrete passives from the front-end. If the CMOS-monolithic piezo-optomechanical platform scales, it addresses the stated requirement for thousands to millions of reprogrammable photonic devices per chip with low power and cryogenic compatibility, which is the actuation bottleneck for optical computing and photonic quantum architectures. Reconfigurable RF front-ends and parametric amplifiers are the named target for BTO's low-voltage 100 ns switching.

Secondary impact channels are narrower but real: quantum-limited acoustoelectric amplification in piezoelectric-2DEG heterostructures would give phonon gain with derived quantum noise; piezo actuation is already the control channel for a levitated gravity sensor at picometre and millikelvin scales, a prerequisite for gravity experiments on quantum superpositions; and label-free single-cell manipulation opens single-cell analysis and controlled cell-cell contact experiments. The sources do not quantify markets, energy savings or cost, so the impact judgement is on technical leverage only, not economic size.

**TLDR: A layer that sits under RF front-ends, large-scale programmable photonics and cryogenic actuation is high-leverage even at modest coefficients.**

## Timing Soon (2-5yr)

Piezo actuation as instrumentation is already deployed: micropipette launchers integrated into three different optical trapping geometries, the feedback path in a levitated gravity sensor and single-transducer acoustofluidic cell control. These need no further invention.

**TLDR: Laboratory instruments are now; wafer-scale RF and photonic integration is the two to five year window; new-mechanism materials are further out.**

## Overrated or underrated? Underrated

Piezoelectricity reads as commodity physics, which is why the 2026 record is easy to miss. The specific thing that has changed is that piezo layers are being placed inside standard high-volume flows and are holding useful coupling there: 200 mm photonic wafers grown on completed CMOS driver wafers with piezoelectric actuators under the waveguides, 8-inch KNN with full (001) polar orientation after a compositional rethink, and thin-film BTO retaining bulk-comparable d33eff (53 pC/N) with 100 ns switching and millikelvin operation. The 19 GHz AlScN filter result is a device-level metric that would matter to anyone building millimetre-wave front-ends. Assessed as an enabling functional layer rather than a standalone product, the position is stronger than the low profile suggests.

Two cautions against overreading. First, the theory work implies the community's understanding of its own material constants was incomplete until recently, both in permittivity, where the electromechanical contribution e_33^2/C_33 accounts for the gap between 11.7 and about 15 in ScAlN, and in the assumed linearity of piezoelectric response with polarisation. Second, there is a documented contamination problem in the literature, with parasitic series elements producing fake ferroelectric hysteresis loops that survive the double-wave method. Treat single-paper coefficient records, especially in nanomaterials, as provisional until strain-field loops or device-level coupling are shown.

## Prediction

By July 2029, a piezo-optomechanical photonic integrated circuit monolithically co-fabricated with CMOS drivers will be reported with at least 1,000 independently addressable piezoelectric actuators on a single die, building on the 200 mm back-end-of-line platform demonstrated in July 2026.

## Evidence base

- 2 June 2026: periodically polarised AlScN BAW ladder-lattice filters at 19 GHz achieved 1.3 dB minimum insertion loss, 6.26% fractional 3 dB bandwidth and 30 dB average out-of-band rejection in a 348 x 476 micrometre footprint, with no balun required.
- 18 June 2026: thin-film barium titanate SAW resonators showed k2eff of 0.14 at 5.2 GHz, operation to 7.8 GHz, extracted d33eff of 53 pC/N comparable to bulk, and 100 ns low-voltage switching, characterised from room temperature to millikelvin.
- 3 July 2026: a fully monolithic all-CMOS platform placed piezoelectric actuators under silicon nitride waveguides, with 200 mm photonic wafers built by back-end-of-line processing on completed commercial CMOS driver wafers.
- 5 June 2026: Mn-doped K1-xNaxNbO3 on 8-inch wafers required a Na-rich composition above 70 at.%, diverging from the bulk equimolar optimum, to suppress pyrochlore and phase segregation and obtain complete (001) polar orientation.
- 6 May 2026: the discrepancy between calculated ScAlN permittivity of about 11.7 and measured values near 15 was attributed to the inverse piezoelectric effect, with epsilon_eff = epsilon_33^S + e_33^2/C_33.
- 14 May 2026: series parasitic components were shown to produce apparent ferroelectric D-E hysteresis in non-ferroelectric capacitors even under the double-wave method, with suspicious loops identified in published work and strain-field loops proposed as the more reliable test.

## Open questions

- Does the Na-rich Mn-doped KNN process reproduce across wafers and lots at 8 inches, and what piezoelectric coefficient and leakage does it deliver in a released device rather than a blanket film?
- Do the 19 GHz P3F AlScN filters retain 1.3 dB insertion loss and 30 dB rejection at power, temperature and over lifetime, and can the periodic polarisation be manufactured at volume yield?
- How many piezoelectric actuators per die does the 200 mm CMOS back-end-of-line photonic process yield, and what is the per-actuator power and crosstalk at that density?
- Can the predicted nonlinear, polarisation-dependent piezoelectric response in wurtzites be measured directly, including the anomalous regime where lower polarisation gives larger strain?
- Does the chirality-derived enhancement in selenium nanowires survive translation from piezoresponse force microscopy on single wires to a working harvester output?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
