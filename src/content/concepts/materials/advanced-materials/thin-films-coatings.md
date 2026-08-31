---
type: concept
slug: thin-films-coatings
canonical_name: Thin Films & Coatings
aliases: []
kind: technology
parent_concepts:
- materials
- advanced-materials
related_concepts: []
sources: []
frontier:
- Do the thin-film lithium niobate and lithium tantalate loss and coupling figures (below 0.1 dB/cm, 0.9 dB per interface) hold across full wafers and after packaging, or only on selected devices 2026 06 16 octave bandwidth 3d printed couplers for low loss thin film ?
- Can tantalum phase selection be made deterministic across substrates, given that its polymorphism is what produces the variation in superconducting properties and coherence 2026 06 15 tantalum as a base material for superconducting integrated c?
- Does the weak correlation between in situ RHEED embeddings and ex situ RMS roughness mean surface morphology cannot be controlled in real time, and if so which additional in situ probe closes that gap 2026 06 15 multi modal machine learning analysis of gase molecular beam?
- Is defect-enabled ferroelectricity of the Bi2SeO5 type stable under repeated cycling, or does the vacancy population that enables switching also cause the degradation that vacancies normally cause 2026 06 16 confined oxygen vacancy migration drives ferroelectric switc?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 44
last_reorg_date: '2026-05-13'
scorecard:
  viability: 4
  drivers: 4
  novelty: 4
  diffusion: 3
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
**Thin films and coatings are engineered layers from a few to a few hundred nanometres thick whose composition, crystal phase and thickness set the performance ceiling of RF filters, integrated photonics, superconducting qubits, displays and sensors, and the June 2026 literature shows the field's centre of gravity moving from finding new film materials to controlling their growth process precisely enough to hit device specifications.**

## Summary

A thin film is a layer of material deposited onto a substrate, typically between one and a few hundred nanometres thick, grown by methods such as molecular beam epitaxy (MBE), sputtering, chemical vapour deposition or bonding-and-thinning of bulk crystals. Because the layer is thinner than most relevant physical length scales, its thickness becomes a design variable in its own right: it sets the resonant frequency of an acoustic device, the phase response of an optical meta-atom, the charge distribution in a transistor channel, or the impedance match of a microwave absorber. The material itself may be identical to a bulk crystal, but confined to a film it acquires different phases, strain states, defect populations and interface physics.

The supplied sources show this playing out across four device families. In photonics, thin-film lithium niobate (TFLN) and the emerging lithium tantalate on insulator (LTOI) platform provide a strong Pockels effect in a waveguide geometry: an 800 nm X-cut TFLN chip was poled at a 1425 nm period to demonstrate backward-wave difference-frequency generation with idler output from 1244 to 1290 nm, while LTOI waveguides showed propagation losses below 0.1 dB/cm with 3D-printed polymer couplers at 0.9 dB per interface over an 850 to 1740 nm band. In RF, 500 nm 128-degree Y-cut lithium niobate on silicon supports higher-order XBAR resonators whose quality factor turns out to depend on in-plane orientation, not only on coupling coefficient. In quantum hardware, superconducting circuit performance is described as fundamentally limited by material losses, with tantalum films attracting attention after strong resonator and qubit results, complicated by the fact that tantalum is polymorphic and the phase that grows depends on the substrate. In electronics, a dual-layer a-IGZO/a-IZO oxide transistor model identifies an optimal top-layer thickness of 9 to 12 nm from the competition between charge confinement and oxygen-vacancy trap density.

The parameters that decide outcomes are therefore process parameters, not just chemistry: substrate temperature, flux ratio, growth rate, thickness, crystallographic orientation and the sequence of fields applied during processing. The measured outputs used as proxies are X-ray rocking-curve full width at half maximum and atomic-force-microscope RMS roughness. A machine-learning study of GaSe MBE found growth rate dominates rocking-curve FWHM while the Se/Ga flux ratio dominates roughness, and that in situ RHEED patterns correlate strongly with FWHM but weakly with roughness. Growth windows can be wide: Mn intercalation to form Mn2In2Se5 worked across substrate temperatures of 250 to 450 degrees C and Se:Mn flux ratios of 1.1 to 3.1, yielding 1.5 nm RMS films and, with longer deposition, 8 nm MnSe layers with 0.35 degree rocking-curve FWHM.

Running alongside this is an automation layer. Closed-loop workflows now search over entire processing histories rather than end-state compositions: an evolutionary search coupled to uncertainty-aware deep kernel learning discovered scanning-probe bias waveforms that enhanced the nonlinear electromechanical response of ferroelectric thin films by de-aging them, and the NIMO platform packages twelve AI algorithms for self-driving laboratories, with thin-film exploration among six demonstrated applications.

## Viability (4/5)

The evidence base is device-level rather than conceptual. LTOI circuits show propagation loss below 0.1 dB/cm, coupling loss of 0.9 dB (strip) and 1.25 dB (rib) per interface, more than an octave of 3 dB bandwidth and stable operation at 1 W optical input. A thin-film lithium niobate photonic tensor core reduced high-speed digital-to-analogue and electro-optic hardware overhead from O(n^2) to O(n). An integrated terahertz photonic receiving frontend delivered undegraded link noise across three windows from 140 to 450 GHz. Epitaxial growth of new film compositions is reproducible over wide process windows.

The qualifier is that viability is uneven within the category. Some entries are simulation or modelling only: the helical carbon coil microwave absorber is a coarse-grained electrodynamic model with representative parameters chosen for demonstration, the phase-change varifocal metalens is an inverse-design study, and the Bi2SeO5 vacancy mechanism is first-principles work matched to an experimental polarisation of about 16 microcoulombs per square centimetre. Fabrication difficulty is also acknowledged directly: the short quasi-phase-matching periods needed for counter-propagating nonlinear optics are described as hard to achieve with standard workflows, and were only reached by poling before etching. So: the platforms work, specific extreme-specification devices remain fabrication-limited.

**TLDR: Working devices with measured, competitive numbers across several independent film platforms.**

## Drivers (4/5)

On the demand side the sources name specific pulls. Terahertz is framed as a key enabler for 6G wireless, with transistor-based frontends failing because both on-chip antenna efficiency and transistor noise degrade near cut-off, leaving photonics as the alternative route. Photonic computing needs high-speed modulation, energy efficiency and large-scale integration simultaneously, which is what drives interest in TFLN tensor cores. Superconducting quantum circuits are described as fundamentally limited by material-related losses, which makes film choice and film growth a direct performance lever rather than a manufacturing detail. RF filtering demands both bandwidth and quality factor from thickness-defined resonators.

On the supply side, the driver is process control tooling. Autonomous synthesis platforms combining machine learning with in situ diagnostics are explicitly aimed at reducing manual tuning in thin-film growth, and the GaSe work notes that MBE application of these methods remains underdeveloped, which is a statement of headroom rather than maturity. NIMO addresses the practical bottleneck of coupling heterogeneous lab robots to varied AI algorithms via a modular CSV-mediated interface. What the sources do not provide is any market sizing, capital expenditure or equipment-demand data, so the commercial magnitude of the pull cannot be assessed here.

**TLDR: Demand pull from 6G, photonic computing and quantum coherence; supply push from ML-guided growth and self-driving labs.**

## Novelty (4/5)

The comparisons are stated against named incumbents. For terahertz reception, the baseline is state-of-the-art electronics, and most microwave photonic links historically performed substantially worse on noise; the reported frontend outperforms electronic frontends across 140 to 450 GHz. For quantum circuits, the incumbents are aluminium and niobium, and tantalum-based circuits reportedly show cryogenic behaviour not seen in either. For photonic computing, the improvement is architectural and quantified as a scaling change from O(n^2) to O(n) in high-speed conversion hardware, plus elimination of beam-combining loss. LTOI is positioned as an emerging alternative to established platforms on transparency window and Pockels effect, with the polymer out-of-plane couplers described as a first implementation for LTOI waveguides.

There is also genuine conceptual novelty in how films are designed. Oxygen vacancies, conventionally treated as defects causing leakage and polarisation degradation, are identified as the mechanism enabling switching in Bi2SeO5, establishing defect-enabled ferroelectricity as a design route. Anomalous Nernst effect engineering is extended from binary alloy optimisation to ternary composition space, reaching a heat-flux sensitivity near 0.24 micrometres per amp in Gd-Co-Pt. Van der Waals intercalation is used as a synthesis route to ternary chalcogenides that would be awkward to grow directly. What is not novel is thin-film technology as a whole; the novelty is concentrated in specific platform-plus-process combinations.

**TLDR: Films are now beating the incumbents they replace: photonics over THz transistors, tantalum over aluminium and niobium, ternary over binary alloy design.**

## Diffusion (3/5)

Several adoption barriers are named explicitly. Tantalum's polymorphism means crystalline structure, superconducting properties and coherence all depend on substrate and growth conditions, which is a process-control burden for anyone standardising a fab flow. Sub-2-micron quasi-phase-matching periods are difficult with standard fabrication workflows and required reordering the process (poling before etching). MBE still depends on manual tuning, and the ML-guided route is described as underdeveloped for MBE specifically. Nucleation on patterned substrates is sensitive in ways that are not monotonic: boron-compound mask growth temperature changes where GaN nucleates within SiO2 openings, with masks grown at 700 to 750 degrees C producing edge-biased distributions and higher-temperature masks giving sparser, inward-shifted domains.

Counting in favour of diffusion, the demonstrated integrations use substrates and interfaces that are compatible with existing manufacturing: 500 nm lithium niobate on silicon, polymer couplers written by 3D direct laser writing onto LTOI waveguides, and oxide TFT models whose electrostatic treatment is claimed to extend to most dual-layer TFT systems rather than one stack. But there is no data here on wafer yields, uniformity across large areas, throughput or cost, and no named commercial adopter, so a score above 3 would not be earned.

**TLDR: Technical adoption barriers are well documented; the sources contain no manufacturing, yield or cost evidence, so the commercial diffusion picture is unresolved.**

## Impact (4/5)

The leverage is high because the film sets a hard ceiling elsewhere in the system. If superconducting circuit performance is fundamentally limited by material losses, then film-level improvements propagate directly into qubit coherence and hence into the cost of any fault-tolerant machine. If transistor-based terahertz frontends cannot meet both antenna efficiency and noise requirements, a thin-film photonic receiver that matches or beats electronics from 140 to 450 GHz changes what 6G link budgets can assume. Reducing high-speed conversion hardware from O(n^2) to O(n) alters the economics of photonic matrix engines at scale. Even the incremental results carry design consequence: knowing that XBAR quality factor peaks near 0 degrees and dips at 90 degrees to the material x-axis changes how filters are laid out, and a 9 to 12 nm optimum for the a-IGZO layer is directly actionable for display and sensor backplanes.

The limit on this score is that the sources quantify device metrics, not value. None gives a system-level cost, energy or revenue figure, and several of the more spectacular claims (non-volatile varifocal metalenses at visible wavelengths, chiral carbon coil absorbers across 2 to 18 GHz) are computational. Impact is judged from criticality of position in the stack, not from measured economic outcomes.

**TLDR: Thin-film choice sits on the critical path of 6G receivers, optical compute, quantum coherence and display electronics, all at once.**

## Timing Soon (2-5yr)

The device layer is close. Waveguide propagation loss below 0.1 dB/cm with sub-1 dB coupling and octave bandwidth is a specification a system designer can build against today, and terahertz photonic frontends already exceed electronic noise performance in three bands. Oxide TFT stack optimisation is at the stage of analytic design rules rather than exploration. Those point to near-term insertion in specific products, subject to manufacturing data the sources do not supply.

The automation layer is further out. ML-guided MBE is explicitly described as underdeveloped, with the current contribution being correlation of RHEED embeddings to rocking-curve FWHM and identification of which growth knobs matter most. Closed-loop protocol discovery on ferroelectric films is demonstrated with a scanning-probe tip as the actuator, which is a research instrument, not a production tool. Self-driving-lab middleware is at the platform-and-perspective stage. A two-to-five-year band captures both: individual film platforms hardening now, autonomous growth optimisation arriving later in that window.

**TLDR: Photonic and RF thin-film platforms are already at competitive device metrics; the process-automation layer that would make them routine is early.**

## Overrated or underrated? Fairly rated

Thin films are not a hype category, and the June 2026 literature reads accordingly: incremental, quantitative, and mostly honest about what is modelled versus measured. The results are real and the comparisons are made against named incumbents rather than straw men. Nothing here suggests the field is oversold, and nothing suggests a discontinuity is being missed by the market.

The defensible position is narrower: within thin films, value is migrating from film composition to process control and heterogeneous integration. The papers that will matter commercially are not the ones reporting a new ternary compound but the ones showing that a wide, reproducible growth window exists, that a fabrication reordering unlocks a previously inaccessible feature size, that an interface problem can be solved with an additive rather than lithographic step, or that in situ diagnostics can be mapped onto ex situ quality metrics well enough to close a control loop. Investors treating thin films as a materials-discovery play are looking at the wrong layer; the scarce asset is repeatable nanometre-scale process control on manufacturable substrates.

## Prediction

By June 2029, at least one peer-reviewed report will demonstrate a closed-loop, in situ-diagnostic-driven controller (of the kind prototyped for GaSe MBE in) running on a production-scale deposition tool rather than a single research chamber, with reported run-to-run variance in rocking-curve FWHM or RMS roughness as the success metric.

## Evidence base

- 16 June 2026: LTOI photonic circuits reported propagation loss below 0.1 dB/cm with 3D-printed polymer couplers at 0.9 dB (strip) and 1.25 dB (rib) per interface, over 850 to 1740 nm and stable at 1 W input.
- 16 June 2026: an integrated terahertz photonic receiving frontend delivered undegraded link noise across 140 to 450 GHz and outperformed electronic frontends, which had previously been the better option on noise.
- 15 June 2026: a review of tantalum for superconducting integrated circuits attributes recent qubit and resonator gains to the film, while identifying polymorphism and substrate-dependent phase selection as the central control problem.
- 16 June 2026: backward-wave difference-frequency generation was demonstrated in 800 nm X-cut TFLN using a 1425 nm poling period achieved by poling before etching, with idler output from 1244 to 1290 nm.
- 15 June 2026: Mn intercalation produced single-crystalline Mn2In2Se5 across substrate temperatures of 250 to 450 degrees C and Se:Mn flux ratios of 1.1 to 3.1, giving 1.5 nm RMS films and 8 nm MnSe with 0.35 degree rocking-curve FWHM.
- 15 June 2026: a two-equation electrostatic model of dual-layer a-IGZO/a-IZO transistors identified an optimal a-IGZO thickness of 9 to 12 nm from the trade-off between charge confinement and oxygen-vacancy trap density.

## Open questions

- Do the thin-film lithium niobate and lithium tantalate loss and coupling figures (below 0.1 dB/cm, 0.9 dB per interface) hold across full wafers and after packaging, or only on selected devices?
- Can tantalum phase selection be made deterministic across substrates, given that its polymorphism is what produces the variation in superconducting properties and coherence?
- Does the weak correlation between in situ RHEED embeddings and ex situ RMS roughness mean surface morphology cannot be controlled in real time, and if so which additional in situ probe closes that gap?
- Is defect-enabled ferroelectricity of the Bi2SeO5 type stable under repeated cycling, or does the vacancy population that enables switching also cause the degradation that vacancies normally cause?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
