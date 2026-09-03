---
type: concept
slug: biosensing
canonical_name: Biosensing
aliases: []
parent_concepts:
- sensing
related_concepts: []
sources:
- '[[2026-07-03-thats-a-learning-curve-mate-not-rsi]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2026-06-04-magnetoresistive-gmr-mtj-biosensor-turbid-samples]]'
- '[[2026-06-04-tmr-sensors-sub-pt-detectivity-biomagnetic-review]]'
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 41
descendants:
- biosensors
sources_7d: 2
sources_30d: 4
recent_mentions:
- slug: 2026-07-03-thats-a-learning-curve-mate-not-rsi
  title: That’s a learning curve mate, not RSI
  date: '2026-07-03'
  kind: substack
- slug: 2026-06-04-magnetoresistive-gmr-mtj-biosensor-turbid-samples
  title: Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related GMR/MTJ bead-detection literature)
  date: '2026-06-04'
  kind: web
- slug: 2026-06-04-tmr-sensors-sub-pt-detectivity-biomagnetic-review
  title: Tunnel-magnetoresistance sensors with sub-pT detectivity for detecting bio-magnetic fields
  date: '2026-06-04'
  kind: web
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
- slug: 2023-07-23-analog-computing-the-once-and-future
  title: '🔮 E09: Analog Computing: The Once and Future King'
  date: '2023-07-23'
  kind: substack
neighbors: []
---
**Biosensing is the engineering of transducers that convert a biological event into an electrical, optical, magnetic or acoustic signal, and the current frontier is less about new recognition chemistry than about picking a transducer that survives real samples: turbid broth, salty buffer, live cells and skin.**

## Summary

A biosensor has two halves: a recognition layer that binds or reacts with the target (antibody, enzyme, aptamer, or in label-free schemes nothing at all), and a transducer that turns that event into a measurable signal. Almost all the interesting engineering now sits in the transducer, because that is what determines whether a device works in a real sample rather than in clean buffer. The sources here span essentially every transducer family in current research: plasmonic and Raman optics, magnetoresistive (GMR and magnetic tunnel junction) chips, nitrogen-vacancy centres in diamond, surface acoustic wave resonators, solid-state nanopores, impedance electrodes, chemiresistive carbon nanotubes and paper-based colourimetry read by hyperspectral cameras.

Each family fails in a characteristic way, and the recent literature is largely a catalogue of those failure modes and their fixes. Optical plasmonic sensors deliver huge field enhancement but heat the sample, which matters in heat-sensitive biosensing; one approach places hexagonal boron nitride flakes under gold nanospheres as an in-plane heat spreader, characterised by finite-element simulation and cross-grating wavefront nanothermometry. Optical sensors also fail outright in turbid, high-cell-density media, which is the stated rationale for magnetoresistive readout: GMR/MTJ sensors detect magnetic beads directly and "enable detection without relying on optical properties", and because they read bead magnetisation rather than analyte charge they are not gated by the roughly 0.7 nm Debye length that limits ISFET and electrochemical sensing in high-salt media <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>. Acoustic sensors are strongly attenuated in liquid, addressed here by a phononic metasurface that confines shear-horizontal surface resonances and raises quality factor under water loading without reflectors.

The parameters that decide a given platform are therefore: sensitivity in the relevant band, tolerance of the actual matrix (turbidity, ionic strength, cells, debris), whether labels are required, whether the readout can be integrated into standard semiconductor manufacturing, and per-device cost. Two sources give hard sensitivity anchors. TMR sensors with low-resistance junctions, thick CoFeSiB free layers and magnetic flux concentrators reach 0.94 pT/root-Hz at 1 Hz and 0.05 pT/root-Hz at 1 kHz in the 1 to 1000 Hz biomagnetic band, though only with those engineering aids and not from a bare junction <sup class="ref"><a href="https://pubs.aip.org/aip/apl/article/126/16/160503/3344956/Tunnel-magnetoresistance-sensors-with-sub-pT" title="Tunnel-magnetoresistance sensors with sub-pT detectivity for detecting bio-magnetic fields" rel="noopener">ref</a></sup>. A CMOS-integrated NV diamond biosensor using a custom 40 nm SPAD array is estimated at roughly 90 nT/root-Hz per pixel, against a requirement of sub-microtesla sensitivity to resolve ODMR shifts from SPION-labelled HEK293T cells.

On the application side, the same funding pipeline pushes towards products: needle-free continuous glucose monitoring to displace subcutaneous sensors that must be replaced every 10 to 14 days, a wearable carbon nanotube array reading pre-seizure volatile organic compounds to warn 10 to 45 minutes before onset, paper-based multi-biomarker maternal health tests read by hyperspectral camera and AI, and single-particle nanopore plus optical trapping to classify AAV capsids as empty, partial or full during gene therapy manufacture.

## Viability (3/5)

Where the sources give measured results, they are real. TMR detectivity of 0.94 pT/root-Hz at 1 Hz is an achieved sensor number, not a projection <sup class="ref"><a href="https://pubs.aip.org/aip/apl/article/126/16/160503/3344956/Tunnel-magnetoresistance-sensors-with-sub-pT" title="Tunnel-magnetoresistance sensors with sub-pT detectivity for detecting bio-magnetic fields" rel="noopener">ref</a></sup>. SERS on 100 nm diameter, 2 micron tall plasmonic nanotubes has been used to monitor electroporation-induced membrane permeability in individual live cells, with fibronectin coating to secure attachment, which is a working measurement on live biology. Gold nanoparticle to photosynthetic protein conjugates give a measured circular dichroism enhancement factor of 3 over free protein, backed by simulation. GMR bead immunoassay has around 20 years of academic prior art including BARC and Stanford work <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>.

Against that, a large share of the frontier here is pre-experimental. The CMOS NV biosensor sensitivity of about 90 nT/root-Hz per pixel is an estimate from an efficiency analysis, not a measurement. The topology-optimised plasmonic trapping metasurfaces are numerical designs using Maxwell stress tensor force calculations with no fabricated device reported, and the Circular Huygens Dipole is explicitly numerically demonstrated only. Nanodiamond probes carry documented material constraints: lattice strain and surface noise shorten T1 and T2, destabilise the NV charge state, and produce pronounced particle-to-particle variability in top-down produced nanodiamonds, which complicates quantitative interpretation. Three is the honest aggregate: credible and partly demonstrated, contested at the device level.

**TLDR: The transduction physics is demonstrated across several families, but most of the platforms in these sources are simulations, estimates or Phase I awards.**

## Drivers (4/5)

On supply, the recurring move is to collapse optics-heavy or bench-scale instruments onto semiconductor processes. The NV work targets a custom 40 nm CMOS SPAD array with on-chip active quenching and digital readout, explicitly framed as a path from optics-heavy quantum diamond microscopes to compact integrated biosensors. Magnetoresistive bead sensing is described as semiconductor-compatible via MEMS/CMOS fabrication, supporting an on-chip claim <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>. Inverse design is arriving as a second supply-side lever, with density-based topology optimisation producing metasurface trapping designs under imposed manufacturing constraints. The community infrastructure is also visible: the 22nd Hilton Head Solid-State Sensors workshop expected close to 500 attendees on 31 May to 2 June 2026 with an explicit biosensing focus, and NSF runs a dedicated BIOSENS-Biosensing programme.

**TLDR: Supply is riding CMOS/MEMS integration and nanophotonic design tools; demand is a named list of unmet clinical and bioprocess needs with money attached.**

## Novelty (3/5)

The clearest novelty claims are comparative rather than absolute. Magnetoresistive readout is better than optical, Raman and NIR probes specifically in turbid or opaque samples where optical biosensors would fail, and better than ISFET or electrochemical readout in high-salt media because it is not gated by the roughly 0.7 nm Debye length; the stated novelty of applying it to enzymatic turnover on beads rather than affinity capture is narrower still <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>. The phononic metasurface SAW device is better than conventional reflector-based SAW sensors, giving significantly higher quality factors under water loading while removing reflectors and their fabrication complexity and miniaturisation penalty. Label-free single-molecule sensing is better than tag-based methods in that attaching a chemical tag or anchoring a molecule changes its behaviour and can make results misleading.

By how much is harder to pin down. The circular dichroism enhancement is a factor of 3 over free protein, which is a real but small number. The NV platform's 90 nT/root-Hz per pixel is an estimate and sits far above the sub-picotesla numbers achievable with TMR, though the two address different measurement geometries: TMR reaches 0.94 pT/root-Hz at 1 Hz only with flux concentrators and optimised stacks <sup class="ref"><a href="https://pubs.aip.org/aip/apl/article/126/16/160503/3344956/Tunnel-magnetoresistance-sensors-with-sub-pT" title="Tunnel-magnetoresistance sensors with sub-pT detectivity for detecting bio-magnetic fields" rel="noopener">ref</a></sup>, while NV offers widefield imaging of SPION-labelled cells. The hBN heat-spreader result quantifies cooling as a function of flake thickness, in-plane conductivity and interfacial conductance but the sources do not state the resulting temperature reduction.

**TLDR: Genuine step changes against named incumbents in specific matrices, but the quantitative deltas reported are modest or estimated.**

## Diffusion (2/5)

The most useful diffusion evidence in these sources is negative. GMR and MTJ bead biosensing has roughly two decades of academic prior art, including BARC bead-array counters and the Stanford GMR line, yet limited commercial penetration in bioprocess, with the open question identified as execution and manufacturing rather than feasibility <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>. That is the canonical biosensing pattern: transducer physics is settled, and the sensor still does not ship. Reinforcing this, the highest-sensitivity magnetic results depend on non-standard sensor-grade stacks with thick soft free layers and flux concentrators, distinct from a memory-style junction, so they do not inherit an existing high-volume manufacturing line <sup class="ref"><a href="https://pubs.aip.org/aip/apl/article/126/16/160503/3344956/Tunnel-magnetoresistance-sensors-with-sub-pT" title="Tunnel-magnetoresistance sensors with sub-pT detectivity for detecting bio-magnetic fields" rel="noopener">ref</a></sup>.

Other barriers are material rather than commercial. Nanodiamond probes show pronounced particle-to-particle variability from top-down production, which is a reproducibility barrier for any assay standardisation. Nanopore sensing of AAV capsids requires miniaturised filtration to remove debris and concentrate particles before measurement, that is, sample preparation is part of the product. Several of the consumer-facing efforts are at NSF Phase I scale, around 305,000 dollars for the seizure-prediction wearable and 304,898 dollars for the non-invasive glucose optoelectronics. The sources say nothing about regulatory clearance, reimbursement outcomes or installed-base displacement, so the barriers listed here are almost certainly incomplete.

**TLDR: The one documented long-run case, GMR bead biosensing, has 20 years of academic work and limited commercial penetration.**

## Impact (4/5)

The value case does not depend on a single application. Non-invasive continuous glucose monitoring would remove the 10 to 14 day sensor replacement cycle that discourages use, with a stated reach across diabetes, prediabetes and the wellness market. Seizure prediction 10 to 45 minutes before onset would create a new category of predictive neurological monitoring for a US population above 3.4 million, replacing detection-after-onset devices. Single-particle AAV capsid loading measurement moves quality control upstream in gene therapy manufacture, where late discovery of bad batches wastes millions and carries patient risk. Earlier detection of hypertensive disorders, heart failure and gestational diabetes from a low-cost paper device would displace tests requiring specialised laboratories and multiple visits.

On the research-tool side the impact is on measurement capability rather than markets: label-free methods that avoid perturbing molecules with tags, repeated non-destructive measurement of the same live cell without lysis, and biomagnetic sensing of cardiac and neural fields in the femtotesla to picotesla range <sup class="ref"><a href="https://pubs.aip.org/aip/apl/article/126/16/160503/3344956/Tunnel-magnetoresistance-sensors-with-sub-pT" title="Tunnel-magnetoresistance sensors with sub-pT detectivity for detecting bio-magnetic fields" rel="noopener">ref</a></sup>. Not a 5, because the sources establish the size of the problems but contain no evidence that any of these platforms has yet solved one at product scale.

**TLDR: If the transducers hold up in real matrices, the addressable problems are large and specific: metabolic monitoring, neurological warning, biomanufacturing release testing.**

## Timing Soon (2-5yr)

The portfolio splits by transducer maturity. Magnetoresistive bead detection and impedimetric cell assays rest on established physics and standard fabrication, so the limiting step is manufacturing and validation rather than discovery <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>. Paper-based vertical flow with hyperspectral readout and AI inference uses commodity components and could move quickly if the analytical performance holds. Both wearable programmes are at Phase I as of June 2026, which places any product well beyond the current window.

The quantum and nanophotonic end is on a longer clock. The CMOS NV biosensor is presented as progress towards a platform with a sensitivity estimate rather than a measured device, nanodiamond material constraints are still being catalogued as a perspective problem in August 2026, and the trapping metasurfaces and Huygens-dipole scatterers remain numerical. Treat those as five years plus.

**TLDR: Bead-based magnetic and impedance platforms and paper-plus-camera assays could reach fielded use within a few years; CMOS quantum diamond and biomagnetic TMR are further out.**

## Overrated or underrated? Fairly rated

Biosensing is neither hyped nor neglected; it is persistently misdiagnosed. The sources make clear that the binding constraint is rarely the recognition chemistry or even the headline sensitivity figure. It is matrix tolerance and manufacturing. The strongest single insight in this set is the GMR maturity caveat: two decades of academic prior art, real physical advantages over optical and electrochemical readout in turbid and high-salt samples, and still limited commercial penetration, with execution rather than feasibility named as the open question <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>. That should be the default prior applied to every platform in this list.

The correctly calibrated position is therefore to be bullish on transducers whose advantage is a matrix problem the incumbent cannot solve at all, and sceptical of those whose advantage is a sensitivity number achieved in clean conditions. Magnetic readout in opaque bioprocess broth and single-particle nanopore classification of AAV capsids fall in the first category, because there is no working alternative today. Plasmonic and quantum-diamond platforms currently fall in the second: the hBN heat-spreader work exists because plasmonic sensors damage the thing they measure, and nanodiamond variability undermines quantitative interpretation before any assay is built.

## Prediction

By the second Label-Free Single Molecule Sensing Gordon Research Conference on 6 to 11 June 2027, no CMOS-integrated NV diamond biosensor will have published a measured, rather than estimated, per-pixel magnetic sensitivity at or better than 90 nT/root-Hz on live cells.

## Evidence base

- TMR sensors reached 0.94 pT/root-Hz at 1 Hz and 0.05 pT/root-Hz at 1 kHz in the 1 to 1000 Hz biomagnetic band, but only with low-resistance junctions, thick CoFeSiB free layers and magnetic flux concentrators, per an Applied Physics Letters perspective published 21 April 2025 <sup class="ref"><a href="https://pubs.aip.org/aip/apl/article/126/16/160503/3344956/Tunnel-magnetoresistance-sensors-with-sub-pT" title="Tunnel-magnetoresistance sensors with sub-pT detectivity for detecting bio-magnetic fields" rel="noopener">ref</a></sup>.
- A CMOS-integrated NV diamond biosensor using a custom 40 nm SPAD array is estimated at about 90 nT/root-Hz per pixel, against a sub-microtesla requirement for SPION-labelled HEK293T cells (published 24 February 2026).
- GMR/MTJ bead biosensing has roughly 20 years of academic prior art but limited commercial penetration in bioprocess, with execution and manufacturing rather than feasibility named as the open question; the transducer is not limited by the roughly 0.7 nm Debye length that constrains ISFET and electrochemical sensing (4 June 2026) <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>.
- A phononic metasurface produced reflector-free, laterally confined shear-horizontal surface resonances with significantly higher quality factors than conventional SAW devices under water loading, fabricated and tested (24 July 2026).
- SERS on 100 nm diameter, 2 micron tall plasmonic nanotubes monitored electroporation-induced membrane permeability dynamics in individual live cells without lysis or exogenous reporters (14 August 2026).
- NSF awarded 300,000 dollars on 15 July 2026 for multimodal nanopore plus optical-trap sensing to classify individual AAV capsids as empty, partial or full, because DNA loading quality currently cannot be checked until after production.

## Open questions

- Does the CMOS-integrated NV SPAD platform achieve its estimated 90 nT/root-Hz per pixel in measurement, and is that sufficient for the sub-microtesla requirement to resolve ODMR shifts from SPION-labelled cells?
- Given 20 years of GMR/MTJ bead biosensing prior art with limited commercial penetration, what specifically changes the manufacturing or execution economics now <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>?
- Can top-down nanodiamond production be brought to a particle-to-particle uniformity that supports quantitative, standardised assays rather than single-probe demonstrations?
- Do the non-invasive glucose and pre-seizure VOC wearables survive contact with real human variability, or do they fail on inter-subject calibration in the way the sources do not address?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
