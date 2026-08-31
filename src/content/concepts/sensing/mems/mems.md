---
type: concept
slug: mems
canonical_name: MEMS
aliases: []
kind: technology
parent_concepts:
- sensing
- mems
related_concepts: []
sources:
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2026-06-21-mems-speaker-market]]'
- '[[2026-07-09-in-die-microfluidic-cooling-sprint]]'
- '[[2026-06-04-magnetoresistive-gmr-mtj-biosensor-turbid-samples]]'
- '[[2026-06-21-st-nxp-mems-acquisition]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2026-06-16-trapped-ion-landscape-2026]]'
- '[[2026-07-11-neutral-pdk-heterogeneous-integration-landscape]]'
- '[[2026-06-21-grandview-mems-microphones]]'
- '[[2026-06-03-datam-specialty-foundry-forecast-2035]]'
- '[[2026-06-21-yole-mems-market-momentum]]'
- '[[2026-06-21-marketsandmarkets-mems-2030]]'
scorecard:
  viability: 4
  drivers: 3
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
mention_count: 107
sources_7d: 1
sources_30d: 8
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-11-neutral-pdk-heterogeneous-integration-landscape
  title: Neutral PDK / EDA layer for heterogeneous photonic integration — landscape check (Scintil essay correction research)
  date: '2026-07-11'
  kind: web
- slug: 2026-07-09-in-die-microfluidic-cooling-sprint
  title: In-die microfluidic cooling — cluster research sprint
  date: '2026-07-09'
  kind: web
- slug: 2026-06-21-mems-speaker-market
  title: MEMS Speaker Market size and CAGR (SNS Insider / Transparency / Data Bridge)
  date: '2026-06-21'
  kind: web
- slug: 2026-06-21-st-nxp-mems-acquisition
  title: STMicroelectronics to acquire NXP's MEMS sensor business for up to $950M
  date: '2026-06-21'
  kind: web
- slug: 2026-06-21-grandview-mems-microphones
  title: MEMS Microphones Market Size — Industry Report to 2030 (Grand View Research)
  date: '2026-06-21'
  kind: web
- slug: 2026-06-21-yole-mems-market-momentum
  title: MEMS market regains momentum — Bosch, STMicroelectronics and TDK navigate the post-inventory growth era (Status of the MEMS Industry 2025)
  date: '2026-06-21'
  kind: web
- slug: 2026-06-21-marketsandmarkets-mems-2030
  title: Micro-Electro-Mechanical System (MEMS) Industry worth $21.99 billion by 2030 (MarketsandMarkets)
  date: '2026-06-21'
  kind: web
neighbors: []
---
**MEMS is the use of semiconductor lithography to build micrometre-scale mechanical parts that move under electrostatic or piezoelectric force, and the 2026 literature shows it shifting from a commodity sensor technology into a general-purpose actuation layer for silicon photonics, RF front ends, spectroscopy and quantum hardware.**

## Summary

Micro-electromechanical systems (MEMS) are mechanical structures such as cantilevers, diaphragms and suspended membranes fabricated with the same lithography, deposition and etch steps used for integrated circuits. A voltage applied across a narrow air gap produces an electrostatic force, or a piezoelectric film bends a beam, and the resulting micrometre or sub-micrometre motion is used either to sense something (a diaphragm deflecting under acoustic pressure) or to actuate something (a mirror, a waveguide coupler, a magnet). Because the moving part is silicon or silicon nitride rather than a material with special electro-optic or thermal properties, MEMS devices tend to hold their state with almost no static power and to work over broad wavelength or frequency ranges.

The sources here are almost all applications rather than MEMS research per se, which is itself the finding: MEMS now appears as the enabling component in domains that have nothing to do with accelerometers. A silicon photonics optical switch built in a zero-change foundry process with back-end-of-line post-processing achieves more than 30 dB extinction ratio in the C-band, under 1.5 dB insertion loss, and roughly 20 nW static power at maximum actuation voltage. A photonic memristor made from CMOS-foundry MEMS cantilevers over low-loss silicon nitride waveguides stores up to 5 bits of optical phase, programmed electrically at 50 kbit/s, with no back-end material integration. A 3 mm by 3 mm MEMS chip with a 100 nm LPCVD silicon nitride diaphragm and a 200 µm silicon microcavity forms a fibre-tip photoacoustic gas cell reaching 58.5 ppb at 1 s with a 6 s response time. Piezoelectric MEMS cantilevers carrying micromagnets tune magnonic RF devices: over 360 degrees of phase shift at 6.1 GHz from an area below 0.02 mm², tunable from 3 GHz to 8.2 GHz experimentally.

The parameters that decide a MEMS device are the gap, the spring stiffness, the actuation voltage and the pull-in threshold at which the moving element collapses irreversibly onto its electrode. At sub-100 nm gaps the Casimir force joins electrostatics in setting that collapse boundary, and it fixes the smallest gap a given stiffness and area can hold open at all. Above that, the practical constraints are quality factor, footprint, hermetic packaging, and whether the process can be run in a standard CMOS or MEMS foundry rather than requiring bespoke materials. Curiously, the same pull-in instability that is normally a failure mode can be exploited: driving commercial-style capacitive MEMS microphone dies into nonlinear pull-in and snap-back turns them into air-coupled ultrasonic transmitters, with a 28-die array at 83 and 93 kHz producing a directional 10 kHz difference tone.

## Viability (4/5)

The cap at 4 rather than 5 reflects scale. The photonic switch paper demonstrates a switch element, not a large port-count switch fabric, while acknowledging that large-scale switching is the goal. The magnonic devices are explicitly proof-of-concept, with the tunable element flip-chipped onto the magnonic waveguide rather than monolithically integrated. The dual-band infrared emitter is finite-element simulation only, with no fabricated device reported. Reliability over millions of actuation cycles, stiction and long-term drift are not addressed anywhere in these sources, and for electrostatic devices operating near pull-in those are the failure modes that decide product viability.

**TLDR: Working devices with measured performance across five unrelated application domains, mostly at single-device or small-array scale.**

## Drivers (3/5)

On supply, the case is good. The optical switch was made with a zero-change foundry-compatible process plus back-end-of-line post-processing, and the photonic memristor uses CMOS-foundry MEMS cantilevers requiring no additional back-end materials integration. Magnetoresistive biosensing similarly notes that MEMS/CMOS-compatible fabrication is demonstrated, supporting an on-chip semiconductor sensor claim <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>. Commercial-style microphone dies are available as a starting point for entirely new transducer functions. Tooling and design support are maturing too, with open-source real-time LQG control and hardware-in-the-loop simulation targeted at MEMS/NEMS on an affordable FPGA platform.

On demand, the sources assert pull without measuring it. Energy-efficient optical interconnect for data centres and AI/ML clusters is named as the motivation for photonic switching; beyond-6G telecommunications and the UWB-FR3 bands motivate the magnonics work; power equipment monitoring, minimally invasive diagnostics and in situ lithium-battery analysis motivate the microscale gas sensor. These are plausible but they are author framing, not procurement data, shipment volumes or pricing. There is a warning shot in the GMR source: roughly twenty years of academic prior art with limited commercial penetration, where execution and manufacturing rather than feasibility are the open question <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>. Nothing in this source set lets one distinguish a genuine demand pull from a research-community narrative.

**TLDR: Strong supply-side evidence of foundry compatibility; demand is stated by authors but nowhere quantified in the sources.**

## Novelty (3/5)

MEMS is not new and the sources say so: the quasi-static pull-in fold has been known in closed form for three decades, and magnetoresistive bead sensing on semiconductor-compatible processes has two decades of prior art <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>. What is new is substitution. In silicon photonics, a MEMS switch element offers greater than 30 dB extinction over the whole C-band with roughly 20 nW static power, which is the argument against thermo-optic tuning where holding a state costs continuous milliwatts, and against electro-optic materials that require non-standard integration; the paper claims MEMS can be used alongside standard silicon photonics components where footprint, extinction ratio, bandwidth and loss all matter simultaneously. For optical memristors the comparison is explicit: existing technologies suffer from durability, material-induced optical loss, limited large-scale reconfigurability or fabrication yield, and the MEMS cantilever version avoids back-end materials entirely while giving 5-bit non-volatile phase storage.

Other comparisons are less quantified but structurally similar: a 3 mm by 3 mm chip replaces a benchtop photoacoustic cell; millimetre-scale MEMS vapour cells substitute for centimetre-scale glass cells in quantum sensing and quantum memory platforms; a sub-0.02 mm² magnonic element replaces conventional RF phase-shifting hardware with more than 360 degrees of shift and multi-octave tunability. The score sits at 3 because the underlying inventiveness lies in the host technologies as much as in the MEMS, and because in several cases the alternative being displaced is not characterised numerically in these sources.

**TLDR: MEMS physics is decades old; the novelty is what it replaces in each host platform, and there the margins are large.**

## Diffusion (3/5)

The single strongest diffusion argument is that these devices can be made where chips are already made. Zero-change foundry compatibility with back-end-of-line post-processing and CMOS-foundry cantilevers needing no extra materials both lower the barrier to adoption inside existing supply chains. That MEMS holder chips are already routine laboratory consumables and that commercial microphone dies can be repurposed indicate a functioning commodity base for at least some device classes.

The barriers are specific and unaddressed here. Moving parts require controlled ambients and hermetic packaging, and the ultrasonic array paper flags aperture, fill factor and device uniformity as limiting factors, which is a yield statement in disguise. Electrostatic devices operate below a collapse boundary that depends on damping and, at sub-100 nm gaps, on the Casimir force, so process tolerance on the gap directly sets yield: the design study inverts a specification to a gap of 97.036 nm, a precision that implies tight fabrication control. The magnonic route currently needs flip-chip assembly of the MEMS cantilever onto the host device, an extra packaging step rather than monolithic integration. And the GMR precedent, twenty years of prior art with limited commercial penetration despite feasibility being settled, is the correct base rate to apply to each of these new applications <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>.

**TLDR: The manufacturing route is already standard, but every new application carries its own packaging, yield and reliability problem, and the sources do not resolve any of them.**

## Impact (4/5)

The breadth of the leverage is what earns the score. Large-scale photonic switches are described as essential devices for energy-efficient optical interconnect in data centres and AI/ML clusters, and the MEMS element addresses exactly the parameters that block scaling: insertion loss under 1.5 dB, extinction above 30 dB, and static power in the tens of nanowatts so that a large fabric does not burn power holding its configuration. Non-volatile 5-bit optical phase storage in a foundry process bears on in-memory optical computing and multiply-accumulate for neural networks. Tunable GHz signal processing in sub-0.02 mm² footprints touches the RF front end of every future handset and base station if it reaches production.

Beyond those, the impact is real but narrower: ppb-level trace gas sensing in space-constrained locations such as inside battery cells, millimetre-scale alkali vapour cells for quantum sensors and quantum memories, localised product detection in atomic-resolution catalysis experiments, and MEMS/NEMS resonators as elements in frequency-domain analogue vector-matrix multiplication. None of these sources quantifies economic value, so the score rests on the technical position of MEMS within high-value host systems rather than on any monetary estimate.

**TLDR: If the photonic switching and RF tuning results scale, MEMS becomes load-bearing infrastructure for AI datacentre interconnect and 6G front ends.**

## Timing Now (0-2yr)

The platform itself needs no waiting. Commercial microphone dies, commercial ETEM MEMS holder chips and CMOS-compatible MEMS processes are all in use today <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>. Anyone assessing MEMS as a whole is assessing something that is already installed.

The specific results here are earlier stage and split by domain. Photonics MEMS is closest, because the process is foundry compatible and the remaining step is scaling from a switch element to a large port-count fabric. The photonic memristor is a first demonstration of a device class with acknowledged incumbent problems, so call it mid-band. Magnonics is explicitly framed against beyond-6G, still requires flip-chip assembly, and the higher frequency range is simulation rather than measurement, placing it later. The infrared emitter is unfabricated.

**TLDR: MEMS is already a shipping manufacturing platform; the specific new device classes in these sources sit two to five years from product.**

## Overrated or underrated? Underrated

MEMS is generally filed as a solved, commoditised sensing technology: accelerometers, gyroscopes, microphones, pressure sensors. This source set shows something different. In five independent fields during a three-month window, the enabling component turned out to be a small piece of silicon that moves. Its advantage is not sensitivity but a combination that competing mechanisms cannot match: broadband operation because the mechanism is geometric rather than material, near-zero static power because a latched mechanical position costs nothing to hold, and fabrication in a standard foundry with no exotic back-end materials. That is a platform argument, and platform arguments are what get underrated.

The counterweight is honest. Nothing here is at production scale, packaging and reliability go unmentioned, actuation near the pull-in boundary is intrinsically a collapse risk that tightens process tolerances, and the GMR precedent shows a MEMS-compatible sensing technology can sit feasible-but-uncommercialised for twenty years <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup>. The correct position is therefore not enthusiasm for MEMS as a category, which would be meaningless, but attention to photonic MEMS specifically, where the foundry route, the loss and extinction figures and the static power number are all simultaneously good and the demand context is the one part of the semiconductor market with unconstrained capital.

## Prediction

By the end of 2028, at least one commercially announced silicon photonic optical circuit switch product will use a foundry-compatible MEMS actuator with per-element static power below 1 µW and insertion loss below 2 dB per element.

## Evidence base

- A foundry-compatible silicon photonics MEMS switch element achieved more than 30 dB extinction ratio in the C-band, under 1.5 dB insertion loss and roughly 20 nW static power at maximum actuation voltage, using a zero-change process with back-end-of-line post-processing (5 Aug 2026).
- A photonic memristor built from CMOS-foundry MEMS cantilevers over low-loss silicon nitride waveguides demonstrated up to 5-bit non-volatile optical phase storage at 50 kbit/s programming speed with no additional back-end materials integration (27 Jul 2026).
- A fibre-tip photoacoustic spectrometer using a 3 mm by 3 mm MEMS chip with a 100 nm LPCVD Si3N4 diaphragm and a 200 µm silicon microcavity reached 58.5 ppb at 1 s with a 6 s response time (7 Jul 2026).
- A micromagnet on a piezoelectrically actuated MEMS cantilever produced more than 360 degrees of RF phase shift at 6.1 GHz from a phase-shifting area below 0.02 mm², experimentally tunable from 3 GHz to 8.2 GHz and simulated to 14 GHz (15 Jun 2026).
- A CoFeB magnonic device on silicon with embedded SmCo micromagnets operated to about 12 GHz, with voltage tunability provided by a NiFeMo element on a piezoelectric MEMS cantilever flip-chipped onto the device (3 Aug 2026).
- Driven into nonlinear pull-in and snap-back, a 28-die array of commercial-style capacitive MEMS microphones operating at 83 and 93 kHz produced a directional 10 kHz difference-frequency component in air (4 Aug 2026).
- Magnetoresistive bead biosensing has roughly twenty years of academic prior art with demonstrated MEMS/CMOS-compatible fabrication but limited commercial penetration, leaving execution rather than feasibility as the open question <sup class="ref"><a href="https://www.mdpi.com/2079-6374/16/1/8" title="Integrated Microfluidic Giant Magnetoresistance (GMR) Biosensor Platform for Magnetoresistive Immunoassay (and related G" rel="noopener">ref</a></sup> (4 Jun 2026).

## Open questions

- Does the sub-1.5 dB insertion loss and 30 dB extinction of the single MEMS switch element hold when cascaded into a large port-count fabric, and what is the die yield of a full switch array in the zero-change foundry flow?
- What are the actuation cycle lifetime, stiction rate and drift of these electrostatic photonic MEMS devices under datacentre thermal and humidity conditions, given that no source reports reliability data?
- Can the magnonic tuning element be integrated monolithically rather than flip-chipped, and does the simulated operation above 8.2 GHz survive measurement?
- Which of these applications has a paying customer as opposed to a stated motivation, given that no source in this set contains market, shipment or pricing data?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
