---
type: concept
slug: barium-titanate
canonical_name: Barium Titanate
aliases:
- bto
- batio3
kind: material
parent_concepts:
- materials
- functional-layers
related_concepts:
- lithium-niobate-tfln
- lithium-tantalate-tflt
- silicon-nitride
- heterogeneous-photonic-integration
sources:
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2026-07-28-laser-on-a-chip-w-matt-crowley-scintil]]'
- '[[2026-01-27-photonics-material-class-war-veeco-and-imec-develop-300mm]]'
frontier:
- Is the gap between bulk r42 above 1200 pm/V and the 154 pm/V effective coefficient measured in devices a fundamental consequence of film domain structure, or can domain-wall engineering capture the predicted local response above 4000 pm/V?
- What are the retention and endurance figures for non-volatile ferroelectric phase shifters over thermal cycling and repeated switching? The sources report switching speed and static power but no drift or cycling data.
- Over what temperature range does a BTO device keep its specified electro-optic and domain state, given the tetragonal-orthorhombic transition near 5 degrees Celsius and its documented effect on domain-wall behaviour?
- Can sputtered or self-buffered epitaxial BTO be produced with wafer-scale uniformity and yield acceptable to a photonics foundry, and does the unetched-BTO hybrid approach preserve enough modulation efficiency to be preferred over etched BTOI?
last_updated: '2026-08-31'
tags:
- concept
- material
mention_count: 32
last_reorg_date: '2026-05-13'
scorecard:
  viability: 4
  drivers: 4
  novelty: 4
  diffusion: 3
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Underrated
scorecard_status: draft
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2026-07-28-laser-on-a-chip-w-matt-crowley-scintil
  title: Laser on a Chip w/ Matt Crowley @ Scintil Photonics
  date: '2026-07-28'
  kind: substack
- slug: 2026-05-02-hybrid-bto-sin-ultra-low-power-tuning-acs-photonics
  title: Hybrid BTO-SiN ultra-low power tuning (ACS Photonics)
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-self-buffered-bto-epitaxy-on-oxide-insulator-light-sci-app-2
  title: 'Self-buffered BTO epitaxy on oxide insulator (Light: Sci & App 2025)'
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-bto-permittivity-pockels-coefficients-mhz-thz-nature-materia
  title: BTO permittivity & Pockels coefficients MHz-THz (Nature Materials 2025)
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-bto-pockels-modulator-on-silicon-photonics-jlt-2019
  title: BTO Pockels modulator on silicon photonics (JLT 2019)
  date: '2026-05-02'
  kind: web
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
- slug: 2026-01-27-photonics-material-class-war-veeco-and-imec-develop-300mm
  title: Veeco and imec develop 300mm-compatible process to enable integration of barium titanate on silicon photonics
  date: '2026-01-27'
  kind: web
neighbors:
- slug: lithium-niobate-tfln
  name: Lithium Niobate (TFLN)
  path: /materials/functional-layers/lithium-niobate-tfln/
  macro: materials
- slug: lithium-tantalate-tflt
  name: Thin-Film Lithium Tantalate (TFLT)
  path: /materials/functional-layers/lithium-tantalate-tflt/
  macro: materials
- slug: silicon-nitride
  name: Silicon Nitride
  path: /materials/substrates/silicon-nitride/
  macro: materials
- slug: heterogeneous-photonic-integration
  name: Heterogeneous Photonic Integration
  path: /photonic-systems/pic-platforms/heterogeneous-photonic-integration/
  macro: photonic-systems
---
**Barium titanate (BaTiO3, BTO) is a ferroelectric perovskite oxide with an exceptionally large Pockels coefficient and strong piezoelectricity, now being made as thin films and membranes on silicon and oxide substrates, where it enables non-volatile, near-zero-static-power optical phase shifters and GHz free-space modulators that thermo-optic and lithium niobate devices cannot match.**

## Summary

Barium titanate is a classic ferroelectric: below its Curie point it has a spontaneous electric polarisation that can be reoriented by an applied field, and that polarisation couples strongly to the refractive index (linear electro-optic, or Pockels, effect) and to strain (piezoelectricity). Its bulk electro-optic response is unusually large, with r42 quoted above 1200 pm/V and r51 around 1300 pm/V. The technological question is not whether the bulk crystal is good, which has been known for decades, but whether thin films can be grown, etched and poled well enough to keep a useful fraction of that response inside a manufacturable waveguide or resonator.

As a functional layer, BTO appears in three device families in the current literature. First, integrated photonics: hybrid silicon-BTO and BTO-on-insulator (BTOI) modulators and phase shifters, with work traceable back to Pockels modulators on silicon photonics <sup class="ref"><a href="https://opg.optica.org/jlt/abstract.cfm?uri=jlt-37-5-1456" title="BTO Pockels modulator on silicon photonics (JLT 2019)" rel="noopener">ref</a></sup> and hybrid BTO-silicon-nitride low-power tuning <sup class="ref"><a href="https://pubs.acs.org/doi/10.1021/acsphotonics.9b00558" title="Hybrid BTO-SiN ultra-low power tuning (ACS Photonics)" rel="noopener">ref</a></sup>. Second, free-space and metasurface modulation, where BTO is one of the mainstream electro-optic materials compared against lithium niobate and organic polymers. Third, RF and quantum acoustics, where thin-film BTO surface acoustic wave resonators have been measured from room temperature down to millikelvin.

The parameters that decide the technology are: the effective Pockels coefficient actually realised in a device versus the bulk value; optical propagation loss after etching; the quality and reproducibility of the film, whether grown epitaxially with a self-buffering layer on oxide insulator <sup class="ref"><a href="https://www.nature.com/articles/s41377-025-02081-9" title="Self-buffered BTO epitaxy on oxide insulator (Light: Sci & App 2025)" rel="noopener">ref</a></sup>, sputtered, or released as a freestanding membrane; the ferroelectric domain configuration, which both limits and can enhance the response; and the frequency dependence of permittivity and electro-optic coefficient from MHz to THz, which sets the usable bandwidth <sup class="ref"><a href="https://www.nature.com/articles/s41563-025-02158-1" title="BTO permittivity & Pockels coefficients MHz-THz (Nature Materials 2025)" rel="noopener">ref</a></sup>.

A distinctive feature, absent from non-ferroelectric electro-optics, is non-volatility. Because domain orientation is remanent, a BTO phase shifter can hold its state with no applied bias, which is the basis of the first non-volatile field-programmable photonic gate array. The same ferroelectric physics also produces conductive charged domain walls and other reconfigurable phenomena that are still at the research stage.

## Viability (4/5)

The evidence base is device-level rather than conceptual. Monolithically etched BTOI nanophotonics reached intrinsic racetrack quality factors near one million with propagation losses of about 0.5 dB/cm, 75-degree etched sidewalls, photonic-crystal bandgap contrast above 40 dB and loaded Fabry-Perot Q up to 230k, with domain alignment verified by second-harmonic generation microscopy. A hybrid silicon-BTO programmable mesh with 58 unit cells and 116 actuators switched in 80 ns at 560 nW per π phase shift. Thin-film BTO SAW resonators showed k2eff of 0.14 at 5.2 GHz, operation to 7.8 GHz, an extracted d33eff of 53 pC/N comparable to bulk, and 100 ns switching. Free-space modulation at gigahertz speed was achieved on a 0.3 mm by 0.3 mm sputtered BTO/TiO2 metasurface with resonance Q above 1300 and transmittance modulation efficiency of about 0.020 per volt.

The main viability gap is the bulk-to-device penalty: the same monolithic BTOI work that cites bulk r42 above 1200 pm/V extracted an effective Pockels coefficient of 154 pm/V in the finished device. Freestanding membrane work shows that thin BTO is mechanically awkward, with a documented trade-off between crack suppression below 15 nm and dense nanoscale wrinkling at 5 nm, and time-dependent evolution of piezoresponse contrast after release. The sources contain no lifetime, endurance or yield data, so the score reflects demonstrated performance, not proven reliability.

**TLDR: Multiple independent, quantified device demonstrations, but device-effective electro-optic coefficients remain far below bulk.**

## Drivers (4/5)

On the demand side the pull is stated explicitly: scaling programmable integrated photonics has been prevented by the high power consumption and thermal crosstalk of conventional volatile phase shifters, which need constant power to hold a state. Free-space modulator performance is likewise described as limited by trade-offs between modulation efficiency, bandwidth and aperture, and conventional metasurfaces are inherently static, which limits their applications. There is a second, smaller demand vector in reconfigurable RF front-ends and parametric amplifiers, and in quantum hardware operating at millikelvin temperatures.

**TLDR: Demand comes from the power and thermal-crosstalk ceiling on programmable photonics; supply from multiple viable film growth routes.**

## Novelty (4/5)

Against thermo-optic phase shifters, the comparison is stark and quantified: BTO ferroelectric domain switching provides non-volatile memory so circuits retain their state without holding power or electrical bias, at 560 nW per π phase shift and 80 ns switching, versus devices that require constant power. That is a capability difference, not just an efficiency improvement. Against other electro-optic materials, BTO is positioned alongside lithium niobate and organic polymers as a mainstream option; its claimed advantage is the large bulk Pockels coefficient, above 1200 pm/V for r42, which permits modulator miniaturisation while keeping strong electro-optic performance.

The honest caveat on the margin is that measured device performance is 154 pm/V, not 1200 pm/V. The sources do not give a lithium niobate figure to compare against directly, so the size of the practical advantage cannot be quantified here. There is a plausible upside route: phase-field modelling predicts local electro-optic response exceeding 4000 pm/V near domain walls, several times the bulk single-crystal r51 of 1300 pm/V, which suggests domain engineering rather than film purity may be the lever. On the piezoelectric side the novelty is more modest: thin-film d33eff of 53 pC/N is presented as comparable to bulk, so the achievement is retention of bulk properties in a thin film rather than an improvement.

**TLDR: Non-volatility at 560 nW per π and a bulk Pockels coefficient above 1200 pm/V are step changes over thermo-optic tuning and competing electro-optic materials.**

## Diffusion (3/5)

Two design choices in the sources are specifically about lowering the adoption barrier. The metasurface work patterns TiO2 on an unetched BTO layer, deliberately combining scalable sputtered growth with mature TiO2 nanofabrication, and the programmable mesh uses a hybrid silicon-BTO platform rather than a wholly new one. Where BTO is etched directly, a dedicated process had to be developed and optimised to obtain anisotropic deep etching with acceptable loss, which is a real but surmountable barrier.

The harder barriers are material. Ferroelectric domain alignment must be verified and controlled, since domain structure strongly modifies the local electro-optic response. Released membranes crack and wrinkle in a thickness-dependent way, and apparent ferroelectric response evolves with time after release owing to switching, morphology, interfacial contact, charge screening and strain relaxation. BTO also has a phase transition near ambient conditions: charged domain wall conductivity falls by several orders of magnitude when the tetragonal phase transforms to orthorhombic below about 5 degrees Celsius, which flags a temperature-window concern for any device whose behaviour depends on domain configuration. The sources say nothing about foundry process design kits, qualification or volume manufacturing, so diffusion beyond research groups cannot be assessed from them.

**TLDR: Process compatibility is improving and hybrid routes avoid etching BTO, but domain control, film mechanics and temperature stability remain open.**

## Impact (4/5)

The claimed prize is explicit: non-volatile ferroelectric silicon photonics as a scalable, heat-free platform for the next generation of energy-efficient photonic systems, validated by configuring a mesh to perform tunable filtering, 4x4 linear unitary transformations and optical routing. Static power and thermal crosstalk are the stated reasons large programmable meshes have not scaled, so a phase shifter drawing 560 nW per π and needing no holding bias addresses the binding constraint rather than a secondary one. Linear unitary transformations are the primitive underlying optical computing and beamforming, so the addressable value extends beyond communications.

Secondary impact channels are narrower but real: large-aperture gigahertz free-space modulation for beam steering and imaging, reconfigurable RF front-ends and parametric amplifiers using thin-film BTO piezoelectricity, extended to millikelvin for quantum hardware, and electric-field control of magnetic response in oxide heterostructures at room temperature, demonstrated for the anomalous Hall effect in Py/BTO/LSMO stacks. Charged-domain-wall electronics, ferron Hall transport and sub-THz domain wall modes are speculative and carry no near-term value in these sources.

**TLDR: If the non-volatile, heat-free phase shifter holds up, it removes the principal scaling limit on programmable photonics.**

## Timing Soon (2-5yr)

Component-level performance is already in place. Waveguide losses near 0.5 dB/cm and intrinsic Q near one million, a 58-cell programmable mesh with 80 ns non-volatile switching and gigahertz free-space modulation on a sputtered film are all dated 2026 and all at the level of working devices rather than proof of principle. Silicon-integrated modulator work on this platform goes back to 2019 <sup class="ref"><a href="https://opg.optica.org/jlt/abstract.cfm?uri=jlt-37-5-1456" title="BTO Pockels modulator on silicon photonics (JLT 2019)" rel="noopener">ref</a></sup>, so the learning curve is not new.

What is missing for a Now call is anything on reproducibility, retention, endurance or manufacturing yield. Membrane processing guidelines were still being established in mid-2026 and the thin-film piezoelectric properties were described as largely unexplored. The research-adjacent applications, charged-domain-wall circuits and ferron transport, sit in the Later or Distant bands on the evidence here.

**TLDR: The photonic components exist and perform now; process reproducibility and reliability data are what stand between demonstration and product.**

## Overrated or underrated? Underrated

The interesting claim is not that BTO has a big Pockels coefficient, which has been known for a long time, but that the ferroelectricity delivers a function no competing electro-optic material offers: a phase shifter that remembers its setting. The demonstrated combination of 560 nW per π, 80 ns switching and zero holding bias in a 58-cell mesh performing real linear-optics functions, together with 0.5 dB/cm loss and near-million intrinsic Q in monolithically etched BTOI, is a stronger package than the material's profile relative to thin-film lithium niobate would suggest. The sputtered BTO/TiO2 metasurface route, which avoids etching BTO altogether, further reduces the manufacturing objection.

The position is conditional on two things the sources do not settle. First, the effective Pockels coefficient is 154 pm/V against a bulk r42 above 1200 pm/V; if that eightfold penalty is structural rather than a domain-engineering problem, much of the material advantage evaporates. Second, ferroelectric non-volatility is only useful if it is stable, and the same physics that makes it attractive produces temperature-sensitive domain reconfiguration, including an orders-of-magnitude conductivity collapse at the transition near 5 degrees Celsius in charged-wall structures and time-dependent piezoresponse drift in released films. Retention and drift data, not peak coefficients, will decide this.

## Prediction

By the end of 2028, a peer-reviewed BTO integrated photonic device will report an effective in-device Pockels coefficient above 300 pm/V together with propagation loss at or below 1 dB/cm, or the field will still be reporting effective values near the 154 pm/V level demonstrated in 2026.

## Evidence base

- Monolithic BTO-on-insulator nanophotonics achieved intrinsic racetrack Q near 1 million, propagation loss about 0.5 dB/cm, photonic-crystal bandgap contrast above 40 dB, loaded Fabry-Perot Q up to 230k, and an effective Pockels coefficient of 154 pm/V against a bulk r42 above 1200 pm/V, reported 7 July 2026 
- The first non-volatile field-programmable photonic gate array, on a hybrid silicon-BTO platform, used 58 unit cells and 116 actuators with 80 ns switching and 560 nW per π phase shift, with no holding power or bias, reported 7 June 2026 
- Thin-film BTO surface acoustic wave resonators showed k2eff of 0.14 at 5.2 GHz, operation to 7.8 GHz, extracted d33eff of 53 pC/N comparable to bulk, and 100 ns low-voltage switching, measured from room temperature to millikelvin, 18 June 2026 
- A hybrid BaTiO3/TiO2 metasurface, patterned in TiO2 on an unetched sputtered BTO layer, reached guided-mode resonance Q above 1300, optical confinement factor about 0.8, and transmittance modulation efficiency of about 0.020 per volt over a 0.3 mm by 0.3 mm aperture at gigahertz speed, 4 August 2026 
- Phase-field modelling predicts local electro-optic response exceeding 4000 pm/V near domain walls in BaTiO3 thin films, several times the bulk single-crystal r51 of 1300 pm/V, 20 July 2026 
- Freestanding BaTiO3 membranes show a processing trade-off: reducing thickness from 15 nm to 5 nm suppresses visible cracking but promotes dense nanoscale wrinkling, with piezoresponse contrast evolving over time after release, 23 July 2026 
- Charged domain wall conductivity in BaTiO3 falls by several orders of magnitude below about 5 degrees Celsius as the tetragonal phase transforms to orthorhombic, explained by fragmentation of the wall into micron-scale segments, 14 May 2026 

## Open questions

- Is the gap between bulk r42 above 1200 pm/V and the 154 pm/V effective coefficient measured in devices a fundamental consequence of film domain structure, or can domain-wall engineering capture the predicted local response above 4000 pm/V?
- What are the retention and endurance figures for non-volatile ferroelectric phase shifters over thermal cycling and repeated switching? The sources report switching speed and static power but no drift or cycling data.
- Over what temperature range does a BTO device keep its specified electro-optic and domain state, given the tetragonal-orthorhombic transition near 5 degrees Celsius and its documented effect on domain-wall behaviour?
- Can sputtered or self-buffered epitaxial BTO be produced with wafer-scale uniformity and yield acceptable to a photonics foundry, and does the unetched-BTO hybrid approach preserve enough modulation efficiency to be preferred over etched BTOI?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
