---
type: concept
slug: avalanche-photodiode
canonical_name: Avalanche Photodiode (APD / SPAD)
aliases:
- APD
- SPAD
- single-photon avalanche diode
- avalanche photodiode
- avalanche-photodiodes
- Avalanche Photodiodes
parent_concepts:
- photodetector
- photonic-integrated-circuits
- silicon-photonics
related_concepts:
- germanium-photodiodes
- ingaas-photodiodes
- hgcdte
- lidar
- time-of-flight
- free-space-photonics
- photonic-imaging
- quantum-cascade-lasers
sources:
- '[[2026-08-03-spad-single-photon-market-scan]]'
- '[[2026-06-17-single-photon-detector-market-spad-snspd]]'
- '[[2026-06-02-singular-photonics-launch]]'
frontier:
- What are the dark count rate, photon detection efficiency and afterpulsing figures of room-temperature Ge-Si SPADs relative to InGaAs SPADs, and are they good enough to displace them in SWIR imaging?
- Does on-chip processing (sketching, spike encoding, embedded LUT logic) scale from the 192 x 128 and 128 x 4 formats demonstrated to megapixel arrays without prohibitive pixel-area or power cost?
- Can dead-time mitigation schemes such as automatic attenuation control survive real deployment conditions, or does the count-rate ceiling remain the binding limit on SPAD data rates in optical wireless and LiDAR?
- 'Which mid-infrared route wins on cost and integrability: direct absorber SPADs, nonlinear upconversion into silicon devices, or non-avalanche room-temperature detectors such as van der Waals heterojunctions?'
- Can SPAD arrays integrated on 300 mm CMOS silicon reach single-photon timing jitter below 50 ps at wafer-level yield?
- Will InGaAs/InP APDs be displaced by Si-SPAD arrays for 1550 nm LiDAR as process nodes shrink, or does the NIR absorption edge remain a hard limit?
- What gating/quench circuit co-integration approach best amortises the per-pixel readout overhead in megapixel SPAD imagers?
- Does a single-photon detector (SPAD array / SNSPD) cross from niche into a system play big enough to escape the commodity-detector ceiling, outside incumbent capture? (see photonic photodetection layer)
last_updated: '2026-08-31'
tags:
- concept
- photonics
- photodetector
mention_count: 53
scorecard:
  viability: 4
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 1
sources_30d: 1
recent_mentions:
- slug: 2026-08-03-spad-single-photon-market-scan
  title: SPAD / single-photon detector market scan — incumbent structure and company cohort
  date: '2026-08-03'
  kind: web
- slug: 2026-06-17-single-photon-detector-market-spad-snspd
  title: Single-photon detector market aggregation — SPAD, SiPM, SNSPD (2024–2035)
  date: '2026-06-17'
  kind: web
- slug: 2026-06-02-singular-photonics-launch
  title: Singular Photonics — launch, SPAD portfolio + Meta collaboration (coverage)
  date: '2026-06-02'
  kind: web
neighbors:
- slug: germanium-photodiodes
  name: Germanium Photodiodes
  path: /photonic-systems/modulators-detectors/germanium-photodiodes/
  macro: photonic-systems
- slug: ingaas-photodiodes
  name: InGaAs Photodiodes
  path: /photonic-systems/modulators-detectors/ingaas-photodiodes/
  macro: photonic-systems
- slug: hgcdte
  name: Mercury Cadmium Telluride
  path: /photonic-systems/modulators-detectors/hgcdte/
  macro: photonic-systems
- slug: lidar
  name: LiDAR
  path: /sensing/ranging-detection/lidar/
  macro: sensing
- slug: time-of-flight
  name: Time-of-Flight (iToF, dToF)
  path: /sensing/ranging-detection/time-of-flight/
  macro: sensing
- slug: free-space-photonics
  name: Free-Space Photonics
  path: /communications/fibre-and-free-space/free-space-photonics/
  macro: communications
- slug: photonic-imaging
  name: Photonic Imaging
  path: /sensing/imaging/photonic-imaging/
  macro: sensing
- slug: quantum-cascade-lasers
  name: Quantum Cascade Lasers
  path: /photonic-systems/light-sources/quantum-cascade-lasers/
  macro: photonic-systems
---
**An avalanche photodiode is a reverse-biased semiconductor detector in which impact ionisation gives internal gain; biased past breakdown it becomes a single-photon avalanche diode (SPAD) that turns one photon into a digital pulse, and because it can be built in standard CMOS it is now the default building block for photon-counting arrays in LiDAR, quantum optics and low-light imaging.**

## Summary

An avalanche photodiode (APD) is a photodiode operated at high reverse bias, where photogenerated carriers are accelerated hard enough to knock further carriers out of the lattice. That impact-ionisation cascade provides internal gain. Push the bias above breakdown and the device enters Geiger mode: a single absorbed photon triggers a self-sustaining avalanche, producing a large digital pulse that must then be quenched before the pixel can fire again. The device in this mode is a single-photon avalanche diode (SPAD). The physics of the multiplication step is still being refined; a 2026 paper argues that the usual semiclassical treatments (local ionisation coefficients, Monte Carlo trajectories) break down in nanoscale high-field junctions and reformulates impact ionisation as a multi-particle self-energy in a non-equilibrium Green's function framework.

The parameters that decide a SPAD are: photon detection efficiency, dark count rate, dead time after each avalanche, afterpulsing, and the wavelength reach set by the absorber bandgap. Silicon SPADs are mature, run at room temperature and are CMOS-compatible, but their bandgap stops them well short of the 1550 nm telecom band; InGaAs SPADs reach 1550 nm but with lower efficiency, higher dark counts and afterpulsing. Germanium-on-silicon is the CMOS-friendly route into the shortwave infrared, moving from a first cryogenic demonstration in 2011 to a room-temperature demonstration in 2024. A third route sidesteps the detector entirely by converting infrared photons up into the visible and counting them with a silicon device, either via nonlinear frequency upconversion or via two-photon absorption inside the silicon APD itself.

The active research frontier is no longer the single diode but the array and what sits underneath it. SPADs are natively digital, so pixel-level logic is natural: recent work puts active quenching and digital readout in a 40 nm CMOS SPAD array, replaces per-pixel time-to-digital converters with spike encoders for neuromorphic processing, and moves FPGA-style look-up-table reconfigurability onto the sensor die. That is driven by a hard engineering constraint: a 192 x 128 SPAD array streaming timestamps can generate tens of gigabytes per second.

Two secondary uses exploit the device's imperfections rather than its sensitivity. Dark-signal non-uniformity across a perimeter-gated SPAD imager has been used as a physically unclonable function for image watermarking, and the same 64 x 64 array's dark-count randomness has been used as a source of stochastic p-bits for a probabilistic optimisation algorithm.

## Viability (4/5)

The core device is not in doubt. SPADs are described as widely used today in time-resolved imaging, simulation work is validated against two recent commercial SPAD sensors, and arrays are being fabricated in nodes from 0.35 µm to 40 nm CMOS with on-chip quenching and digital readout. Working systems built on them include a 192 x 128 LiDAR imager with real-time depth reconstruction and single-shot single-photon spectroscopy at 120 MHz mode spacing.

What is not yet settled is the extension beyond silicon's bandgap. Ge-Si SPADs only reached room-temperature operation in 2024 after a first cryogenic demonstration in 2011, and the incumbent InGaAs option carries acknowledged penalties in efficiency, dark count rate and afterpulsing. The upconversion workaround is real but system-heavy, requiring a nonlinear stage and pump; it achieved 80% conversion and 37% overall detection efficiency at 3 µm. The sources also show that the physical model of avalanche multiplication is still being reworked at nanoscale dimensions, which matters for design confidence at aggressive scaling.

**TLDR: Silicon SPAD arrays are commercial and working; the infrared extensions are credible demonstrations, not products.**

## Drivers (4/5)

On the demand side the sources span an unusually wide set of end uses for one device: automotive-style direct time-of-flight LiDAR, quantum networking and repeaters, where frequency-multiplexed schemes need single-shot spectral resolution matched to quantum memory mode spacing, NV-centre magnetometry for biosensing, label-free mid-infrared hyperspectral imaging of biological samples, single-emitter photon-correlation spectroscopy and photon-starved optical wireless links.

On the supply side, the decisive fact is that SPADs are CMOS-compatible, which lets array format, quenching circuitry and processing logic ride standard process scaling rather than requiring bespoke detector fabs. Ge-on-Si is being pursued explicitly to keep the shortwave-infrared version on the same substrate. The counterweight, stated directly in the sources, is that SPAD sensors remain high-priced and of limited availability, to the point where researchers build simulators because they cannot get datasets.

**TLDR: Demand pull from LiDAR, quantum networking, biosensing and photon-starved links; supply push from CMOS compatibility.**

## Novelty (3/5)

As a device concept the APD is long established, and the sources treat it as the reference detector rather than the novelty. Against conventional image sensors the advantage is categorical rather than incremental: single-photon sensitivity per pixel, extreme temporal resolution and no readout noise, which is what makes low-light imaging at around 5 mlux tractable. Against superconducting detectors the argument is room-temperature operation and the avoidance of cryogenic energy overhead, which is stated as the motivation for room-temperature single-photon detection generally.

The quantified novelty in these sources is mostly at system level. Two-photon absorption in a silicon APD under 3 µm pumping raised the signal counting rate by a factor of about 10^5 and improved noise equivalent power by two orders of magnitude over near-infrared pumping. An upconversion front end plus silicon APD reached a noise equivalent power of 1.8 x 10^-17 W/Hz^1/2 at 3 µm and, using a multi-pixel photon counter, resolved photon numbers up to 9 with 0.14% noise probability per pulse, claimed as a first at mid-infrared wavelengths. On the readout side, sketched compression achieved 512x reduction against conventional histogram output, and a low-complexity attenuation control algorithm cut computation by two orders of magnitude relative to the convex-optimisation version. Note also that the competition is moving: a van der Waals black-phosphorus heterojunction claims room-temperature single-photon detection at 1550 nm precisely to escape InGaAs SPAD limitations.

**TLDR: The diode is old; what is new is CMOS array integration, on-chip processing and infrared reach, with genuine but application-specific margins.**

## Diffusion (3/5)

Four barriers appear repeatedly. First, data volume: high-resolution SPAD arrays can produce tens of gigabytes per second of timestamps, forcing either on-chip compression, histogram-free spike encoding that removes the time-to-digital converters entirely, or on-chip reconfigurable logic. Second, dead time: SPADs saturate under strong background or high signal power, and the resulting blocking loss and inter-symbol interference are severe enough that whole analytical frameworks and attenuation-control schemes are being built to work around them. Detector count-rate capability is likewise called out as a system-level design constraint in the NV biosensor architecture.

Third, the raw data is unlike anything standard pipelines expect: sparse binary Bernoulli photon detections requiring bespoke reconstruction, which is why generative restoration methods are being adapted to the domain and why the first colour SPAD burst dataset has only just appeared. Fourth, cost and scarcity of the sensors themselves is explicitly slowing algorithm and dataset development, and device-to-device dark-count variability is large enough to give each chip a unique fingerprint. None of these is fatal, and each has a demonstrated mitigation, but together they mean adoption proceeds application by application rather than as a general sensor replacement.

**TLDR: Adoption is real but bottlenecked by data bandwidth, dead-time saturation, device non-uniformity, cost and availability.**

## Impact (4/5)

The breadth in these sources is the argument. The same device family enables depth imaging, chemically specific mid-infrared hyperspectral imaging of biological and polymeric samples across 2.9 to 3.6 µm without the photodamage of high-intensity illumination, a CMOS-integrated NV magnetometer estimated at roughly 90 nT/√Hz per pixel and aimed at replacing optics-heavy quantum diamond microscopes, and measurement of many-body excitations in single perovskite quantum dots, including a triexciton feature at 7.4 ± 1.9 meV. For quantum networking, the multiplexing capacity of frequency-multiplexed repeaters depends on being able to resolve single-photon-level modes at 120 MHz spacing.

The more speculative upside is the device being used as something other than a detector: a 64 x 64 perimeter-gated SPAD array in 0.35 µm CMOS has run the Probabilistic Approximate Optimization Algorithm on 26-spin Sherrington-Kirkpatrick instances using dark-count stochasticity as p-bits, with the algorithm learning around device-specific Gompertz-type activations rather than requiring calibration. That is a single small-scale demonstration and should not be weighted heavily, but it indicates the array is a usable stochastic computing substrate as well as an imager. The reason this is a 4 and not a 5 is that in most of these applications the SPAD is an enabling component within a larger system, and in the infrared it competes with alternatives that may displace it.

**TLDR: A general-purpose photon-counting primitive underlying LiDAR, quantum links, biological magnetometry and molecular imaging.**

## Timing Now (0-2yr)

For the visible and near-infrared, the timing question is settled. Commercial SPAD sensors are in use, arrays are fabricated in advanced CMOS with integrated quenching and readout, and the engineering effort has shifted to readout bandwidth and in-sensor processing, which is where mature technologies go.

The infrared story runs later. Ge-Si SPADs took roughly a decade and a half from the 2011 cryogenic demonstration to room-temperature operation in 2024, and the review frames applications as prospective rather than current. Upconversion-based mid-infrared counting is at laboratory demonstration, as is the van der Waals room-temperature 1550 nm alternative. Treat SWIR and mid-infrared single-photon arrays as a two-to-five-year question, with silicon-based systems available now.

**TLDR: Silicon SPAD arrays are already commercial and being designed into systems; SWIR and mid-infrared photon counting are at demonstration stage.**

## Overrated or underrated? Fairly rated

The SPAD is correctly regarded as the workhorse room-temperature photon counter, and the sources bear that out: it is commercially available, CMOS-integrable, and already the detector of record across LiDAR, quantum optics, biosensing and photon-starved communications. There is no hidden discontinuity here. The genuinely interesting movement is one level up, in the co-design of the array with its processing: 512x on-sensor compression, removal of time-to-digital converters in favour of spike encoders and on-die reconfigurable logic. Investors should be watching readout architecture, not diode structures.

The part of the field where expectations are most likely to be mispriced is wavelength reach. There are now three competing paths past silicon's bandgap: Ge-on-Si SPADs, now room-temperature; nonlinear upconversion feeding a silicon device, with 37% overall detection efficiency demonstrated at 3 µm; and non-avalanche room-temperature detectors such as van der Waals heterojunctions targeting 1550 nm. Each is a single-figure-of-merit demonstration and the sources do not let you rank them on manufacturability, yield or cost. Whoever wins that race determines whether SPAD arrays extend their franchise into SWIR imaging and telecom-band quantum links or stay a visible and near-infrared technology.

## Prediction

By 31 December 2028, at least one commercially marketed shortwave-infrared SPAD array based on germanium-on-silicon and operating without cryogenic cooling will be on sale, following the room-temperature device demonstration reported in 2024.

## Evidence base

- Ge-Si SPADs moved from a first cryogenic demonstration in 2011 to a room-temperature demonstration in 2024, per a review published 8 May 2026.
- A mid-infrared upconversion detector reported 4 June 2026 achieved 80% conversion efficiency at 3 µm, 37% overall detection efficiency, noise equivalent power of 1.8 x 10^-17 W/Hz^1/2, and photon-number resolution up to 9 with 0.14% noise probability per pulse when paired with a silicon APD.
- Non-degenerate two-photon absorption in a silicon APD pumped at 3 µm, reported 3 June 2026, raised signal counting rate by a factor of about 10^5 and improved noise equivalent power by two orders of magnitude over near-infrared pumping, at room temperature.
- An FPGA sketching implementation for a 192 x 128 SPAD LiDAR array, dated 11 February 2026, achieved 512x compression versus histogram output, addressing timestamp data rates that can reach tens of gigabytes per second.
- A 40 nm CMOS SPAD array with on-chip active quenching and digital readout, reported 24 February 2026, supports an estimated magnetic field sensitivity of approximately 90 nT/√Hz per pixel for NV-centre widefield ODMR biosensing.
- A 64 x 64 perimeter-gated SPAD array in 0.35 µm CMOS ran the Probabilistic Approximate Optimization Algorithm on 26-spin Sherrington-Kirkpatrick instances using dark-count stochasticity as p-bits, reported 15 February 2026.

## Open questions

- What are the dark count rate, photon detection efficiency and afterpulsing figures of room-temperature Ge-Si SPADs relative to InGaAs SPADs, and are they good enough to displace them in SWIR imaging?
- Does on-chip processing (sketching, spike encoding, embedded LUT logic) scale from the 192 x 128 and 128 x 4 formats demonstrated to megapixel arrays without prohibitive pixel-area or power cost?
- Can dead-time mitigation schemes such as automatic attenuation control survive real deployment conditions, or does the count-rate ceiling remain the binding limit on SPAD data rates in optical wireless and LiDAR?
- Which mid-infrared route wins on cost and integrability: direct absorber SPADs, nonlinear upconversion into silicon devices, or non-avalanche room-temperature detectors such as van der Waals heterojunctions?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
