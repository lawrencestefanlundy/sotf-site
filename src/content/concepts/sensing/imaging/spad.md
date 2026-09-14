---
type: concept
slug: spad
canonical_name: SPAD (Single-Photon Avalanche Diode)
aliases:
- single-photon avalanche diode
- SPADs
- Geiger-mode APD
parent_concepts:
- single-photon-detectors
related_concepts:
- avalanche-photodiode
- image-sensors
- time-of-flight
sources:
- '[[2026-08-03-spad-single-photon-market-scan]]'
- '[[2026-06-17-single-photon-detector-market-spad-snspd]]'
- '[[2026-06-02-singular-photonics-launch]]'
auto_stub: false
last_updated: '2026-08-31'
tags:
- concept
mention_count: 53
scorecard:
  viability: 4
  drivers: 4
  novelty: 4
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
frontier:
- Do the in-sensor processing architectures (spike encoders, on-chip LUT logic) preserve depth and photometric accuracy when scaled from 128 x 4 and 192 x 128 formats to large-format arrays, or does per-pixel logic area collapse fill factor?
- Can room-temperature SWIR photon counting in GeSi reach the PDE, dark count and afterpulsing figures already achieved in silicon at 785 nm, and at what yield in a standard CMOS flow?
- Does dead-time mitigation, whether by automatic attenuation control or statistical correction, hold up in real high-background field conditions such as daylight LiDAR, rather than in the analytical and numerical models presented?
- Will simulated datasets and diffusion-model priors close the training-data gap well enough that models trained synthetically transfer to real SPAD data across sensors and light levels, or does each sensor need its own captured corpus?
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: avalanche-photodiode
  name: Avalanche Photodiode (APD / SPAD)
  path: /photonic-systems/modulators-detectors/avalanche-photodiode/
  macro: photonic-systems
- slug: image-sensors
  name: Image Sensors
  path: /sensing/imaging/image-sensors/
  macro: sensing
- slug: time-of-flight
  name: Time-of-Flight (iToF, dToF)
  path: /sensing/ranging-detection/time-of-flight/
  macro: sensing
---
**A SPAD is a reverse-biased semiconductor diode operated above breakdown so that a single absorbed photon triggers a self-sustaining avalanche and a clean digital pulse, giving CMOS image sensors photon counting with picosecond-class timing and no readout noise; the device physics is now largely solved and the binding constraints have shifted to dead time, off-chip data bandwidth and wavelength coverage beyond silicon.**

## Summary

A single-photon avalanche diode is a photodiode biased beyond its breakdown voltage. A single photo-generated carrier initiates an avalanche that saturates the junction, producing a digital pulse rather than an analogue photocurrent. The avalanche must then be quenched and the pixel recharged, and during this dead time the pixel is blind. Because the output is a timestamp or a count rather than an integrated charge, SPAD arrays detect individual photons at each pixel with extreme temporal resolution and without readout noise, which is why they are the sensor of choice for low-light imaging and time-resolved measurement. They are also natively digital optical interfaces, which makes them unusually well suited to logic processing and event-driven computation placed directly next to the pixel.

The parameters that decide a SPAD are photon detection efficiency (PDE), dark count rate (DCR), afterpulsing probability, dead time, timing jitter, and array format. State of the art in silicon is strong: a thick-junction, backside-illuminated Si SPAD with a 50 V quenching readout has been reported at 84.4% PDE at 785 nm with 260 cps dark count rate and 2.9% afterpulsing at 268 K, in a compact module supporting free-running, gated and hybrid operation. Silicon's bandgap, however, caps sensitivity short of telecom wavelengths. Two routes are being pursued: germanium-on-silicon SPADs for the shortwave infrared, which moved from a first cryogenic demonstration in 2011 to a room-temperature demonstration in 2024, and non-avalanche alternatives such as a black-phosphorus (~350 meV absorber) van der Waals heterojunction detector aimed at room-temperature 1550 nm operation, positioned explicitly against InGaAs SPADs' lower efficiency, high dark counts, afterpulsing and fabrication hazards.

Two non-negotiable physical limits shape system design. First, dead time: at high photon flux a SPAD saturates, losing photons within a symbol (blocking loss) and smearing across symbols (inter-symbol interference), a problem now being modelled in closed form via renewal theory for slow regimes and Markov chains for regimes where symbol duration is shorter than dead time. Second, data volume: high-resolution SPAD arrays can generate tens of gigabytes per second of timestamps, so the output path, not the detector, sets the achievable resolution.

Consequently much of the current work is architectural rather than device-level: statistical sketch compression on FPGA achieving 512x compression against conventional histogram output on a 192 x 128 array, removal of time-to-digital converters altogether in favour of per-pixel spike encoders feeding spiking neural networks, moving FPGA-style look-up-table logic on-chip at pixel or cluster level, and generative reconstruction of images from sparse binary quanta frames using adapted latent diffusion models.

## Viability (4/5)

Silicon SPADs are not a laboratory question. Reported performance includes 84.4% PDE at 785 nm with 260 cps DCR and 2.9% afterpulsing in an integrated module, and commercial SPAD sensors are available in sufficient volume to be used as ground truth for validating simulation pipelines. Fabrication spans mature nodes for research arrays in 0.35 µm standard CMOS to a custom 40 nm CMOS SPAD array with on-chip active quenching and digital readout.

The deductions are specific rather than speculative. Dead time causes photon-counting saturation and non-linear distortion under strong background or high signal power, requiring either optical attenuation control or elaborate statistical correction. Array-format scaling is bounded by timestamp egress at tens of gigabytes per second, and the demonstrated in-sensor-processing chips remain small (128 x 4 for the spike-encoder imager). Beyond ~1 µm, silicon is unusable and the substitutes are only recently at room temperature.

**TLDR: The device works and is commercial; the remaining hard limits are dead time, data bandwidth and sub-silicon wavelength coverage.**

## Drivers (4/5)

On the demand side the sources show pull from at least six distinct directions: direct time-of-flight LiDAR, optical wireless communication for photon-starved links, quantum repeater instrumentation where a SPAD array reads out frequency-to-spatial mapping at 120 MHz mode spacing matched to Pr-doped Y2SiO5 memories, single-emitter spectroscopy resolving a bound triexciton feature 7.4 ± 1.9 meV from the exciton, quantum sensing with NV-diamond biosensors targeting roughly 90 nT/√Hz per pixel, and mid-infrared hyperspectral imaging via upconversion into the visible so that cheap Si-SPADs can be used at 2.9 to 3.6 µm. A second, unexpected demand vector is SPADs as stochastic or identity primitives rather than imagers: true random number generation with under 1% bias variation at 2 kHz per pixel passing all 16 NIST STS tests, imager PUF watermarking from dark signal non-uniformity, and p-bit arrays for combinatorial optimisation.

On the supply side, CMOS compatibility is the decisive advantage: SPADs can be fabricated in standard processes and co-integrated with quenching, counting and logic. The counterweight is stated plainly in the sources: high price and limited availability of SPAD sensors, and consequent scarcity of datasets, is holding back SPAD-specific and learning-based algorithm development, to the point where synthetic data pipelines are needed as a substitute.

**TLDR: Demand pull is unusually broad and CMOS compatibility supplies the manufacturing base, but cost and availability still throttle the research and algorithm ecosystem.**

## Novelty (4/5)

The comparison that matters most is against conventional integrating image sensors. SPADs deliver imaging in regimes where conventional cameras fail, with per-pixel single-photon sensitivity, extreme temporal resolution and no readout noise; classification from reconstructed fluxes has been examined down to about 5 mlux. That is a difference in kind, not degree. Within photon counting, the interesting result is that raw sensitivity is no longer the differentiator: long-term parallel operation of SiPM modules and PMTs in the MAGIC 17 m telescope camera found that SiPMs, despite higher photon detection efficiency, deliver only performance comparable to PMTs because their longer-wavelength response also collects more light of night sky, with the proposed way forward being SPADs used as truly digital sensors. The claim to beat is therefore about digital, per-photon, per-pixel information, not quantum efficiency.

Quantified margins elsewhere: 84.4% PDE at 785 nm with 260 cps DCR sets the silicon reference point; 512x data reduction versus histogram output is the readout-side margin; a low-complexity attenuation-control algorithm reduces computation by two orders of magnitude versus its convex-optimisation counterpart. Where SPADs are being displaced rather than improved is the telecom band: the van der Waals room-temperature 1550 nm detector is explicitly framed as an answer to the weaknesses of InGaAs SPADs.

**TLDR: Against conventional image sensors the gain is categorical in the photon-starved regime; against PMTs and SiPMs the claimed advantage is being digital rather than more sensitive.**

## Diffusion (3/5)

The barriers are documented rather than inferred. Cost and limited availability of SPAD sensors directly constrains the algorithm and dataset ecosystem that any broad adoption would depend on. The interface is the second barrier: timestamp streams at tens of gigabytes per second cannot be moved off chip at scale, so every high-resolution deployment needs a compression, sketching or in-sensor-inference layer to be viable. Third, dead time means a SPAD system is not drop-in: under strong background or high signal power it saturates and needs active attenuation control or scene-adaptive reconfiguration to hold performance.

What pushes the score up rather than down is that the mitigations are being built in the right place, on chip and in the pixel, and that adoption already spans instruments (MAGIC camera modules), laboratory spectroscopy and prototype LiDAR. The sources do not, however, contain volume, unit-cost or design-win data, so the commercial diffusion rate itself cannot be assessed from them.

**TLDR: Adoption is real but gated by sensor cost and availability, off-chip data volume, and the need for application-specific saturation management.**

## Impact (4/5)

If the readout and wavelength problems are solved, the addressable value is broad because the same primitive serves unrelated markets: automotive and robotics depth sensing, photon-starved optical wireless links, label-free mid-infrared molecular imaging of biological tissue without high-intensity illumination and its associated photodamage, frequency-multiplexed quantum repeaters, and compact quantitative magnetic imaging replacing optics-heavy quantum diamond microscopes.

The reason not to score 5 is that in several of these the SPAD is an enabling component whose share of the value is modest, and in at least one head-to-head test the incumbent held its ground: SiPMs in a Cherenkov telescope camera matched, rather than beat, PMTs. The most economically significant use cases in the sources, LiDAR and low-light consumer-style imaging, are also the ones where the data-rate and saturation constraints bite hardest.

**TLDR: A CMOS-compatible, photon-resolved, picosecond-timed digital pixel is a horizontal platform, and the sources show it reaching across imaging, comms, quantum and security.**

## Timing Now (0-2yr)

The core technology is present tense. Commercial SPAD sensors are purchasable and used experimentally, integrated silicon modules exceed 84% PDE, and SPAD arrays are working detectors in spectroscopy and quantum-optics instruments today.

The things that would change the technology's character are later. In-sensor spike encoding and on-chip FPGA-style logic exist as proofs of concept at small array formats; sketch-based compression is still demonstrated on an external FPGA with a 192 x 128 array. SWIR photon counting reached room temperature in GeSi only in 2024, and the 1550 nm van der Waals route is a single-device demonstration, both of which read as 2-5 years or longer before productisation.

**TLDR: Silicon SPADs are already commercial and deployed; the frontier capabilities (in-sensor compute, SWIR at room temperature) land in the 2-5 year window.**

## Overrated or underrated? Fairly rated

SPADs are neither hyped nor overlooked: they are a maturing silicon platform whose limits are well characterised and whose research community has largely stopped arguing about the detector and started arguing about the pipeline. The evidence for that shift is that four of the strongest recent contributions are not device papers at all but readout and reconstruction papers: 512x sketch compression, TDC elimination via in-pixel spike encoders, on-chip reconfigurable logic and diffusion-model reconstruction from Bernoulli photon statistics. Investors should read the value as migrating from the diode to the sensor-plus-compute stack and to the datasets, given that data scarcity is an explicit blocker.

The two places where the consensus may be wrong in the underrated direction are the non-imaging uses of SPAD non-idealities, where dark-count variability is turned from a defect into an entropy source or a p-bit activation function, and the argument from Cherenkov astronomy that the real advantage of the family is being digital rather than being sensitive. Both are early: 64 x 64 arrays and 26-spin problem instances are not yet evidence of a market.

## Prediction

By 30 June 2028, at least one commercially available SPAD image sensor will ship with on-chip timestamp compression or in-sensor spike/neural encoding integrated at pixel or cluster level, removing the need for an external FPGA in the raw-data path, as prototyped in 2025-2026.

## Evidence base

- A thick-junction, backside-illuminated Si SPAD module reached 84.4% photon detection efficiency at 785 nm with a 260 cps dark count rate and 2.9% afterpulsing at 268 K, using a 50 V quenching readout (published 24 July 2025).
- GeSi SPADs progressed from a first cryogenic SWIR single-photon demonstration in 2011 to a room-temperature demonstration in 2024 (review, 8 May 2026).
- High-spatial-resolution SPAD arrays can produce tens of gigabytes per second of timestamps; an FPGA sketch implementation on a 192 x 128 array achieved 512x compression versus conventional histogram output with histogram-free online depth reconstruction (11 February 2026).
- Transporter, a 128 x 4 SPAD sensor with per-pixel D flip-flop ring spike encoders, eliminates time-to-digital converters and histogramming in favour of in-sensor spike encoding for spiking neural networks (7 November 2025).
- Dead time imposes both intra-symbol blocking loss and inter-symbol interference in SPAD-array optical wireless receivers, modelled exactly by renewal theory below dead time and by a Markov chain above it (28 May 2026); a companion paper proposes automatic attenuation control with a low-complexity variant cutting computation by two orders of magnitude (28 May 2026).
- Long-term parallel operation of SiPM modules and PMTs in the MAGIC 17 m telescope camera showed SiPMs deliver only comparable performance to PMTs despite higher PDE, motivating the use of SPADs as truly digital sensors (23 February 2026).
- A 64 x 64 perimeter-gated SPAD array in 0.35 µm CMOS achieved under 1% bias variation at 2 kHz per pixel and passed all 16 NIST Statistical Test Suite tests after Von Neumann debiasing (18 June 2025), and the same array class ran the Probabilistic Approximate Optimization Algorithm on 26-spin Sherrington-Kirkpatrick instances with up to 17 layers (15 February 2026) 

## Open questions

- Do the in-sensor processing architectures (spike encoders, on-chip LUT logic) preserve depth and photometric accuracy when scaled from 128 x 4 and 192 x 128 formats to large-format arrays, or does per-pixel logic area collapse fill factor?
- Can room-temperature SWIR photon counting in GeSi reach the PDE, dark count and afterpulsing figures already achieved in silicon at 785 nm, and at what yield in a standard CMOS flow?
- Does dead-time mitigation, whether by automatic attenuation control or statistical correction, hold up in real high-background field conditions such as daylight LiDAR, rather than in the analytical and numerical models presented?
- Will simulated datasets and diffusion-model priors close the training-data gap well enough that models trained synthetically transfer to real SPAD data across sensors and light levels, or does each sensor need its own captured corpus?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
