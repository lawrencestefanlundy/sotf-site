---
type: concept
slug: mid-ir-photonics
canonical_name: Mid-Infrared Photonics
aliases:
- mid-IR
- mid-infrared
- MIR photonics
- quantum cascade laser
parent_concepts:
- photonics
- photonic-integrated-circuits
related_concepts:
- quantum-cascade-lasers
- hgcdte
- sensing-imaging
- spectral-sensing
- free-space-photonics
- compound-semiconductors
- photonic-imaging
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
scorecard:
  viability: 4
  drivers: 2
  novelty: 4
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Underrated
scorecard_status: draft
mention_count: 123
sources_7d: 5
sources_30d: 13
recent_mentions:
- slug: 2026-06-17-single-photon-detector-market-spad-snspd
  title: Single-photon detector market aggregation — SPAD, SiPM, SNSPD (2024–2035)
  date: '2026-06-17'
  kind: web
- slug: 2026-05-24-mose2-exciton-polariton-all-optical-switch
  title: New light-based switch could cut chip energy use and speed future AI photonics
  date: '2026-05-24'
  kind: web
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2023-10-05-nynomic-nlir-investment
  title: 'Nynomic AG: Expansion of technology portfolio / investment in NLIR ApS'
  date: '2023-10-05'
  kind: web
neighbors:
- slug: quantum-cascade-lasers
  name: Quantum Cascade Lasers
  path: /photonic-systems/light-sources/quantum-cascade-lasers/
  macro: photonic-systems
- slug: hgcdte
  name: Mercury Cadmium Telluride
  path: /photonic-systems/modulators-detectors/hgcdte/
  macro: photonic-systems
- slug: sensing-imaging
  name: Sensing & Imaging
  path: /sensing/imaging/sensing-imaging/
  macro: sensing
- slug: spectral-sensing
  name: Spectral Sensing
  path: /sensing/mems/spectral-sensing/
  macro: sensing
- slug: free-space-photonics
  name: Free-Space Photonics
  path: /communications/fibre-and-free-space/free-space-photonics/
  macro: communications
- slug: compound-semiconductors
  name: Compound Semiconductors
  path: /materials/substrates/compound-semiconductors/
  macro: materials
- slug: photonic-imaging
  name: Photonic Imaging
  path: /sensing/imaging/photonic-imaging/
  macro: sensing
---
**Mid-infrared photonics covers the sources, detectors and optics for roughly the 2-12 µm band where molecules absorb, and the current wave of work sidesteps poor infrared sensors by nonlinearly converting mid-IR light up into the near-infrared where silicon cameras and single-photon detectors already work.**

## Summary

The mid-infrared spans the wavelengths at which molecular bonds vibrate, so it is the natural band for chemical identification: gas sensing, combustion diagnostics, biomedical spectroscopy, materials inspection and thermal imaging all live there. The problem has never been the physics of absorption but the hardware. Mid-IR detectors are noisy, and array formats are limited by readout electronics and sensitivity, which caps frame rates for large pixel counts. Parallel spectrometers suffer the same penalty because every pixel in the array contributes noise.

The dominant technical answer in the recent literature is nonlinear upconversion. A mid-IR signal is mixed with a strong pump beam in a nonlinear crystal, producing a near-infrared replica that carries the same spectral or spatial information but can be read out with a silicon camera or a silicon single-photon detector. Because the conversion is low-noise and works at room temperature, the sensitivity penalty of the infrared sensor disappears. The same nonlinear step can be engineered to do optical work in passing: phase matching acts as a spatial-frequency filter, so edge enhancement and higher-order image differentiation can be imposed on the image during conversion rather than in software.

The parameters that decide the field are conversion efficiency, noise equivalent power, spectral bandwidth and resolution, and the pump power needed to get there. Recent work reports 22% peak conversion efficiency and a noise equivalent power of 0.3 fW/Hz^(1/2) using an external cavity to enhance a 1064 nm pump by a factor of 36 to 55 W intracavity average power. Spectrometers built on this route reach 0.5 cm^-1 resolution at illumination levels of 0.14 photons per nm per pulse across 2.4-4.2 µm, and hyperspectral imagers acquire 100 spectral bands over 2600-4085 cm^-1 in 10 ms.

Around this core sit two supporting layers. On the source and materials side: chip-scale rubidium vapour cells producing coherent mid-IR by four-wave mixing, two-colour femtosecond filaments in air giving tunable radiation near 3.3 µm, hexagonal GeSn alloys predicted to push a direct absorption edge into the mid-IR, and reference data on which transparent materials are usable for infrared coatings and windows. On the applications side: mid-IR used as a probe or pump in microscopy at sub-5 nm resolution, in photothermal super-resolution chemical imaging, and to drive lattice vibrations directly for room-temperature terahertz detection.

## Viability (4/5)

The deduction is for scale and complexity. The best sensitivity number depends on a low-loss external cavity building 55 W of intracavity average power from a single-longitudinal-mode pump, which is an optical table, not a product. Some results are still numerical rather than experimental, and the promising integrated source materials remain at density functional theory stage. Nothing in the sources shows a compact, self-contained instrument.

**TLDR: Repeated, quantified, room-temperature laboratory demonstrations across detection, spectroscopy and imaging, but all bench-scale.**

## Drivers (2/5)

Supply side, the pull is real and visible. A cluster of closely related results appeared within weeks covering detection, single-photon spectroscopy, high-speed videography, hyperspectral imaging and all-optical edge processing, largely from overlapping author groups. Enabling infrastructure is also maturing: nanophotonic supercontinuum sources covering 2.4-4.2 µm are being used as broadband illumination, and practical design references for infrared coatings and windows are being published with usable transparency thresholds of α < 10 cm^-1 for thin films and α < 1 cm^-1 for windows.

Demand side, the sources give nothing but assertion. Applications named include combustion diagnostics, explosion reactions, photosynthetic tracking, thermal surveillance, remote sensing, environmental monitoring, industrial inspection and astronomical observation, but no market size, no customer, no funding programme and no company appears anywhere in the supplied material. On the evidence available this is a technology push with a plausible but unmeasured pull, and the score reflects that gap rather than a judgement that demand is absent.

**TLDR: Strong supply-side momentum in a few academic groups; demand is asserted in abstracts, never evidenced.**

## Novelty (4/5)

The comparison class is direct mid-IR detection with cooled or noisy infrared sensors and raster-scanned or wavelength-tuned hyperspectral acquisition. Against that, upconversion claims at least a tenfold improvement in noise equivalent power over previous results in the same class, and replaces slow scanning with a 10 ms, 100-band cube. The single-pixel and time-stretch spectrometers explicitly target the failure mode of multi-pixel infrared arrays, where every element adds noise, and operate at 0.01 to 0.14 photons per pulse-level illumination. Doing Fourier-domain image processing inside the conversion crystal, with vortex transfer functions switchable from first to fourth order at 60 Hz, has no equivalent in a conventional infrared camera pipeline.

Adjacent claims carry similar margins. Polar dielectric transducers exceed metal thermoreflectance transducers by up to eight times, and by an order of magnitude in some cases. Mid-IR excitation of lattice vibrations needs power density nearly 300 times lower than visible excitation for comparable phonon enhancement. The score is 4 rather than 5 because the margins are reported by the originating groups against their own prior work, and no independent replication appears in the sources.

## Diffusion (2/5)

The adoption barriers are structural rather than incremental. High sensitivity is bought with 55 W of intracavity average power from a cavity-enhanced single-frequency pump. The imaging schemes need spatial light modulators, digital micromirror devices, acousto-optic tunable filters, temperature-controlled phase-matched crystals and computational reconstruction algorithms. Phase matching also couples performance to crystal temperature and angle, which is a calibration and stability burden in the field.

There are early signals of a miniaturisation route but they are weak. Micromachined rubidium vapour cells generate coherent mid-IR through an anodically bonded silicon window, but the collected power is around 50 nW. Foundry-compatible crosstalk elimination in standard rib waveguides has been demonstrated across silicon-on-insulator and other platforms, which matters for eventual integration density, but that work is not itself mid-IR. Direct-gap 2H-GeSn as an integrated mid-IR emitter or absorber is at the theory stage. The likely first diffusion path is high-end scientific instrumentation, not volume deployment.

**TLDR: Everything demonstrated depends on free-space nonlinear crystals, high-power pumps and expert alignment; no manufacturing or foundry path is shown.**

## Impact (3/5)

The upside is clear in kind if not in magnitude. If chemical imaging and spectroscopy in the molecular vibration bands can be done with silicon cameras and silicon single-photon detectors, the cost and sensitivity structure of an entire class of instruments changes, and the applications listed span industrial inspection, environmental monitoring, biomedical diagnosis and astronomy. Photon-starved and fast-transient regimes that are simply inaccessible today become measurable: 100 Hz hyperspectral cubes, and snapshot capture of distinct transient events within a single camera exposure.

Beyond sensing, mid-IR as an actuator has real scientific reach: resonant mid-IR photoexcitation is being used to create and track excitons in black phosphorus on picosecond timescales, and mid-IR driving of out-of-plane lattice vibrations in few-layer MoS2 offers a route to room-temperature terahertz detection. Chemical microscopy at sub-5 nm lateral resolution and super-resolved photothermal chemical imaging of live cells are real capability gains for life science. The score stops at 3 because no source in this set quantifies economic value, installed base displaced, or a customer prepared to buy.

**TLDR: Substantial if it decouples mid-IR sensing from expensive infrared sensors, but the sources demonstrate capability, not value captured.**

## Timing Soon (2-5yr)

The detection and imaging thread is past feasibility. Sensitivity, resolution and speed figures are measured, at room temperature, using off-the-shelf silicon detectors on the readout side. What remains is engineering: shrinking the pump, stabilising phase matching and packaging the reconstruction pipeline. That is a two-to-five year job for a specialist instrument vendor, not a physics problem.

The source and integration thread is on a longer clock. Chip-scale mid-IR generation is at the tens-of-nanowatt level, candidate direct-gap alloys are at DFT, and the foundry-compatible waveguide work has not yet been shown in the mid-IR. A genuinely integrated mid-IR photonic system is Later at best on this evidence.

**TLDR: Upconversion instrumentation is demonstration-ready now and plausible as specialist product within a few years; integrated chip-scale mid-IR sources are further out.**

## Overrated or underrated? Underrated

The consistently interesting move here is that the field has stopped trying to build better infrared detectors and instead moved the problem into silicon. That reframing is what produces the tenfold noise equivalent power gain, the sub-photon-per-nm spectroscopy and the 100 Hz hyperspectral cubes in the same few weeks of literature. It also buys optical computation for free, since the nonlinear crystal can be made to differentiate the image while converting it. Relative to the attention it receives, that is a strong position.

The caveat is concentration. A large share of the strongest results in this source set comes from overlapping author groups, and independent replication does not appear. The pump requirements are also a genuine commercialisation obstacle, not a detail. The call is Underrated on technical merit with the explicit condition that the sources contain no evidence of a customer, a company or a market, and no assessment of demand can be made from them.

## Prediction

By 31 December 2028, at least one research group with no author overlap with the Zeng/Huang collaboration will publish a mid-IR upconversion hyperspectral imager achieving 100 or more spectral bands at a cube refresh rate of 100 Hz or better, matching.

## Evidence base

- 29 May 2026: cavity-enhanced upconversion detection reaches 22% peak conversion efficiency and a noise equivalent power of 0.3 fW/Hz^(1/2), described as at least a tenfold improvement over previous results, using a 1064 nm pump enhanced 36x to 55 W intracavity.
- 29 May 2026: a wide-field upconversion hyperspectral imager acquires 100 spectral bands over 2600-4085 cm^-1 in 10 ms, a 100 Hz cube refresh rate, using a 10 kHz megapixel silicon camera.
- 29 May 2026: single-photon time-stretch spectroscopy over 2.4-4.2 µm achieves 0.5 cm^-1 resolution at 0.14 photons per nm per pulse; the compressive single-pixel variant reports 0.5 cm^-1 down to 0.01 photon-level flux across 3.1-3.9 µm.
- 14 May 2026: an upconversion differentiator at 3 µm performs tunable first- to fourth-order isotropic edge enhancement with real-time switching at up to 60 Hz onto a single-photon-sensitive silicon camera.
- 15 May 2026: mid-IR driving of out-of-plane lattice vibrations in few-layer MoS2 gives over 80% room-temperature phonon amplification at nearly 300x lower power density than visible excitation, stable over 2800 cycles and more than 15 hours.
- 5 May 2026: micromachined Rb vapour cells generate continuous-wave coherent mid-IR at only about 50 nW collected power, alongside ~20 µW of blue light with ~1 MHz linewidth, indicating how far chip-scale mid-IR sources still are from useful power.

## Open questions

- Can the 0.3 fW/Hz^(1/2) noise equivalent power be retained without a 55 W intracavity pump, or does sensitivity collapse when the cavity enhancement of 36 is removed?
- Do any of the upconversion results reproduce outside the originating groups, and at what performance penalty?
- How far can the demonstrated bands, currently 2.4-4.2 µm and 2600-4085 cm^-1, be extended into the longer-wavelength fingerprint region where most chemical discrimination lives?
- Is there a credible waveguide-integrated path for the nonlinear conversion stage, given that the demonstrated foundry-compatible mode-hybridisation work was not done at mid-IR wavelengths?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
