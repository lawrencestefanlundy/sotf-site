---
type: concept
slug: photodetector
canonical_name: Photodetector & Optical Receiver Front-End
aliases:
- photodiode
- Ge-on-Si photodiode
- optical receiver
- APD
- TIA
parent_concepts:
- photonic-integrated-circuits
related_concepts:
- germanium-photodiodes
- ingaas-photodiodes
- avalanche-photodiode
- co-packaged-optics
- optical-interconnect
- silicon-photonics
- external-laser-source
- uni-traveling-carrier-photodiode
sources:
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
frontier:
- What are the yield, throughput and long-term reliability of micro-transfer printing an electronic chiplet onto a silicon photonic IC at production volume, given the 0.06 mm2 BiCMOS demonstration is described as a first of its kind 2026 06 05 a 3d integrated bicmos silicon photonics high speed receiver?
- Does the 71 fJ/b figure for the 32-channel WDM receiver hold across temperature, process corners and ageing once ring and MZI tuning must track a real data-centre thermal environment 2026 06 07 single chip 1024 tbs optical receiver for high speed optical?
- Is above minus 5 dBm RF power from the 206 GHz MUTC photodiode sufficient for practical sub-THz wireless links, or does it still require amplification that erases the efficiency gain 2026 05 28 modified uni travelling carrier photodiodes with 206 ghz ban?
- Will any fast room-temperature 3.0 to 3.7 micron detector reach commercial availability, given the stated scarcity, and at what price and package 2026 06 17 ghz bandwidth inasinassbp barrier infrared detectors for the?
- Does any merchant/discrete datacom receiver supply chain de-integrate from the SiPh die (the laser precedent) — or does Ge-on-Si keep detection monolithic and commoditised?
- Does a single-photon detector (SPAD array / SNSPD) cross from niche into a system play big enough to escape the commodity-detector ceiling, outside incumbent capture?
last_updated: '2026-08-31'
tags:
- concept
- photonics
- orientation
descendants:
- avalanche-photodiode
- uni-traveling-carrier-photodiode
mention_count: 22
scorecard:
  viability: 5
  drivers: 4
  novelty: 4
  diffusion: 3
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Underrated
scorecard_status: draft
sources_7d: 2
sources_30d: 3
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
neighbors:
- slug: germanium-photodiodes
  name: Germanium Photodiodes
  path: /photonic-systems/modulators-detectors/germanium-photodiodes/
  macro: photonic-systems
- slug: ingaas-photodiodes
  name: InGaAs Photodiodes
  path: /photonic-systems/modulators-detectors/ingaas-photodiodes/
  macro: photonic-systems
- slug: avalanche-photodiode
  name: Avalanche Photodiode (APD / SPAD)
  path: /photonic-systems/modulators-detectors/avalanche-photodiode/
  macro: photonic-systems
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: optical-interconnect
  name: Optical Interconnect
  path: /communications/optical-interconnect/optical-interconnect/
  macro: communications
- slug: silicon-photonics
  name: Silicon Photonics
  path: /photonic-systems/pic-platforms/silicon-photonics/
  macro: photonic-systems
- slug: external-laser-source
  name: External Laser Source (ELS) for Co-Packaged Optics
  path: /photonic-systems/light-sources/external-laser-source/
  macro: photonic-systems
- slug: uni-traveling-carrier-photodiode
  name: Uni-Traveling-Carrier Photodiode (UTC-PD)
  path: /photonic-systems/modulators-detectors/uni-traveling-carrier-photodiode/
  macro: photonic-systems
---
**The photodetector and its receiver front-end convert light back into electrical bits, and recent fabricated demonstrations, including a single-chip 1.024 Tb/s CMOS receiver at 71 fJ/b and a 206 GHz photodiode, show the receiver is now where much of the remaining energy and bandwidth headroom in optical links sits.**

## Summary

An optical receiver front-end is the input half of any optical link. A photodetector, usually a reverse-biased photodiode, converts incoming photons into a photocurrent; a transimpedance amplifier (TIA) turns that small current into a voltage swing large enough for a decision circuit or ADC. Everything that matters about a link's power budget converges here: the detector's responsivity in amps per watt, its 3 dB bandwidth, the parasitic capacitance between detector and amplifier, and the amplifier's input-referred noise, which sets the minimum received optical power (sensitivity) for a given bit error rate.

The design tension is structural. Photodiode quantum efficiency and bandwidth trade against each other, because a thicker absorption region catches more light but slows carrier transit; work on modified uni-travelling-carrier (MUTC) photodiodes attacks this directly, with an InP waveguide-integrated device reaching a 206 GHz 3 dB bandwidth at 0.81 A/W external responsivity and a bandwidth-efficiency product above 130 GHz. The second tension is integration: detector and amplifier fabricated in different processes accumulate parasitics at the interface, which is the explicit motivation for 3D heterogeneous integration by micro-transfer printing of a 0.06 mm2 BiCMOS chiplet onto a silicon photonic IC, giving 224 Gb/s PAM-4 at minus 5.2 dBm OMA sensitivity and 0.51 pJ/b.

The parameters that decide the field are therefore: energy per bit, bandwidth density, sensitivity, and whether the front-end can be built in a commercial foundry flow. Two 2026 results set the current markers. A monolithic analogue front-end in the GlobalFoundries Fotonix platform achieves 28.9 GHz bandwidth and 61.7 dBohm gain at 9.22 mW and 0.08 pJ/bit, with under 737 nA RMS input-referred noise current and PAM-4 eyes measured to 64 GBaud. A 32-channel WDM receiver monolithically integrated in 45nm CMOS runs 1.024 Tb/s aggregate at 71 fJ/b including photonic tuning and control power, with 4 Tb/s/mm2 bandwidth density and BER below 1e-12 with no equalisation, error correction or DSP.

Outside data-centre links, the same component class is under pressure from three other directions: sub-THz wireless, where the photodiode is the photonic mixer generating RF power; mid-infrared sensing and free-space optics, where fast room-temperature detectors are scarce; and quantum systems, where the receiver choice determines what information survives measurement at all.

## Viability (5/5)

The core evidence is hardware. The 45nm CMOS WDM receiver is a single chip with all 32 channels running simultaneously at 32 Gb/s and BER below 1e-12 without equalisation or FEC. The Fotonix front-end was designed, fabricated and characterised for DC, noise and time-domain behaviour, with PAM-4 electrical eyes to 64 GBaud. The micro-transfer-printed BiCMOS-on-SiPIC receiver delivers a measured 224 Gb/s PAM-4 link with quoted sensitivity. The 206 GHz MUTC photodiode is packaged with WR-5.1 waveguide output and delivers above minus 5 dBm RF power. These are the signatures of a technology past the question of whether it works.

The caveat is that viability is uneven across sub-branches. Mid-infrared GHz photodetection at room temperature is demonstrated at device level but the sources state that commercial availability in the 3.0 to 3.7 micron band remains scarce. Upconversion photon counting and non-degenerate two-photon absorption detection are single-laboratory results. The score reflects the mainstream telecom and datacom receiver, which is unambiguously real; treat the exotic wavelength and quantum variants as separate, earlier-stage bets.

**TLDR: Fabricated, measured silicon in commercial foundry platforms, not simulation.**

## Drivers (4/5)

Demand: the stated framing is that copper reach shrinks as bandwidth rises, from across the data centre floor a decade ago to not making it out of the rack now, pushing optics closer to the chip <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>. Conversion cost in power and latency is the bottleneck, and coherent systems, which extract more per wavelength, carry DSPs consuming 3 to 4 times more power and costing 3 to 5 times more than intensity-based systems <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>. That makes low-energy direct-detect front-ends the volume battleground. Rack-scale optical memory architectures are entering vendor roadmaps, with a multi-rack optical shared-memory architecture for AI inference announced <sup class="ref"><a href="https://semiengineering.com/chip-industry-week-in-review-150/" title="Chip Industry Week in Review (7 Aug 2026)" rel="noopener">ref</a></sup>. Secondary demand comes from sub-THz wireless sources and from the I/O bottleneck in superconducting quantum processors, where fibre-integrated photodiode arrays replace per-qubit microwave cables.

Supply: the enabling change is that these front-ends are being built in named commercial platforms, GlobalFoundries Fotonix, GlobalFoundries 45SPCLO and 45nm CMOS, plus micro-transfer printing as a route to co-integrating electronics with photonics. The sources do not give volumes, prices or capacity figures, so the supply side is assessed on process availability only.

**TLDR: Demand pulled hard by AI interconnect and copper's shrinking reach; supply enabled by commercial photonic foundry platforms.**

## Novelty (4/5)

Against what, and by how much. On energy and density: 71 fJ/b including electronics plus photonic tuning and control, and 4 Tb/s/mm2, both stated as records for an integrated WDM receiver, achieved with no equalisation, error correction or digital processing. On a per-lane basis, 0.08 pJ/bit at 9.22 mW from a 1.2 V supply for a 56 GBaud-class analogue front-end, and 0.51 pJ/b with record-small footprint for a 224 Gb/s PAM-4 receiver built by 3D printing electronics directly onto the photonic die, the stated novelty being that prior micro-transfer printing work targeted photonics rather than electronics-on-photonics. On the detector itself, a bandwidth-efficiency product above 130 GHz is claimed as a new benchmark against the standard efficiency-bandwidth trade-off.

In the sensing and quantum branches the deltas are larger in ratio but from a lower base. Non-degenerate two-photon absorption in a silicon avalanche photodiode under 3 micron mid-infrared pumping gives a signal counting rate enhancement of about 1e5 and NEP improved by two orders of magnitude versus conventional near-infrared pumping. An upconversion detector reaches 80% conversion efficiency, 37% overall detection efficiency and NEP of 1.8e-17 W/Hz^1/2 at 3 microns, with photon-number resolving to 9 photons described as a first. The nBp barrier detector's 2.4 GHz 3 dB bandwidth is called the best confirmed optically in its class of mid-infrared detectors. These are real advances, but each is a single group's claim; the score is 4 rather than 5 because independent replication is not in the sources.

**TLDR: Several results are explicitly framed as records against the prior receiver state of the art, with numbers attached.**

## Diffusion (3/5)

The strongest diffusion argument is that these are not exotic one-off processes. Front-ends built in Fotonix, 45SPCLO and 45nm CMOS inherit an existing manufacturing base. The 1.024 Tb/s receiver's use of inverse-designed broadband grating couplers also lowers the packaging and alignment burden.

The barriers the sources do surface: micro-transfer printing of electronic chiplets onto photonic ICs is presented as pioneering rather than qualified, so yield, reliability and throughput at volume are unaddressed. WDM receivers depend on ring and MZI demultiplexers with capacitive tuning, and the honest accounting of that tuning power is included in the 71 fJ/b figure but its behaviour across temperature and process corners in the field is not reported. Outside datacom, the sources state directly that fast mid-infrared detectors have scarce commercial availability, and the cryogenic and single-photon variants serve niches by construction. No cost, qualification or volume data appears in any source, which caps confidence at 3.

**TLDR: Foundry compatibility removes one barrier; heterogeneous integration yield, wavelength tuning and mid-IR supply remain unresolved in the sources.**

## Impact (4/5)

If optical links replace copper progressively from the rack down to the board <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>, the per-bit energy of the receiver front-end multiplies across every link in a fleet. A receiver hitting 71 fJ/b including its own photonic control power while needing no equalisation, FEC or DSP attacks exactly the cost structure the newsletter identifies, where coherent DSPs draw 3 to 4 times the power and 3 to 5 times the cost of intensity-based systems <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>. Bandwidth density of 4 Tb/s/mm2 matters separately, because escape bandwidth per unit of chip edge or area is what constrains accelerator I/O.

Beyond datacom the leverage is narrower but real. Photodiodes as sub-THz mixers with above minus 5 dBm output at WR-5.1 could underpin photonic wireless backhaul. In quantum computing, replacing per-qubit microwave cabling with optical I/O and fibre-integrated photodiode arrays addresses a stated scaling bottleneck of footprint, thermal load and cost, with only a 0.19% single-qubit gate fidelity reduction measured. The score is held at 4 because none of the sources quantifies system-level or economic impact; the inference from component numbers to fleet savings is mine, not theirs.

**TLDR: Receiver energy per bit is a first-order term in AI data-centre interconnect economics, and the demonstrated numbers are large improvements.**

## Timing Soon (2-5yr)

Nothing in these results waits on a physics breakthrough. The 1.024 Tb/s receiver, the 0.08 pJ/bit Fotonix front-end and the 224 Gb/s micro-transfer-printed receiver are all fabricated and measured in 2025 to 2026 on commercial platforms. What separates them from products is reliability qualification, packaging, test and yield of the integration step, none of which the sources address. That is normally a multi-year gap, hence 2 to 5 years for these specific architectures to appear in shipping transceivers or optical I/O engines.

The adjacent branches run later. Fast room-temperature mid-infrared detection is at best-in-class device demonstrations with acknowledged commercial scarcity. Full optical I/O for superconducting processors is a two-qubit closed-loop demonstration, which puts useful deployment further out than this band.

**TLDR: The component class already ships; the specific record front-ends here are foundry-fabricated prototypes that need qualification, not invention.**

## Overrated or underrated? Underrated

Attention in photonics concentrates on lasers, modulators and switch fabrics; the receiver is treated as the easy end. The 2026 numbers argue otherwise, and in the right direction. A receiver that delivers BER below 1e-12 with no equalisation, no FEC and no DSP at 71 fJ/b removes a large block of the link power and latency that the coherent-versus-IMDD debate is actually about <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>. Similarly, the argument that parasitics between separately fabricated photonic and electronic dies are the limiting factor, and that printing a 0.06 mm2 BiCMOS chiplet onto the photonic IC fixes it at 0.51 pJ/b and 224 Gb/s, reframes the receiver as an integration problem rather than a circuit problem. That is a more tractable, and more investable, framing.

The qualification: this verdict applies to the datacom and telecom front-end. The mid-infrared, upconversion and cryogenic photon-counting work in these sources is genuinely impressive on its own metrics but is single-group, small-market and should not be bundled into the same thesis. And the sources contain no cost, yield or volume data at all, so anyone pricing this needs numbers that do not exist here.

## Prediction

By June 2029, at least one further single-chip integrated optical receiver will be published or productised exceeding 1.024 Tb/s aggregate throughput at an energy efficiency at or below 71 fJ/b including photonic tuning and control power, improving on the 45nm CMOS result reported in January 2026.

## Evidence base

- A 32-channel WDM receiver monolithically integrated in 45nm CMOS reached 1.024 Tb/s aggregate at 32 Gb/s per channel, 71 fJ/b including electronics and photonic tuning, 4 Tb/s/mm2 bandwidth density and BER below 1e-12 with no equalisation, FEC or DSP, reported 12 January 2026.
- A 3D heterogeneously integrated receiver made by micro-transfer printing a 0.06 mm2 BiCMOS chiplet onto a silicon photonic IC achieved 224 Gb/s PAM-4 at minus 5.2 dBm OMA sensitivity, BER 2.4e-4 and 0.51 pJ/b, reported 28 November 2025.
- A monolithic analogue front-end in the GlobalFoundries Fotonix platform measured 28.9 GHz bandwidth, 61.7 dBohm gain, 9.22 mW from 1.2 V, under 737 nA RMS input-referred noise and 0.08 pJ/bit, with PAM-4 eyes to 64 GBaud, reported 7 May 2026.
- An InP waveguide-integrated modified uni-travelling-carrier photodiode achieved a 206 GHz 3 dB bandwidth, 0.81 A/W external responsivity, bandwidth-efficiency product above 130 GHz and above minus 5 dBm RF power at WR-5.1 output, reported 28 May 2026.
- An InAs/InAsSbP nBp barrier detector for 3.0 to 3.7 microns achieved 2.4 GHz 3 dB and 8.0 GHz 20 dB bandwidth at room temperature from a 121 micron diameter device, described as best in class, while noting commercial availability of such detectors remains scarce, reported 17 June 2026.
- A mid-infrared upconversion detector translated 3 micron photons to the visible at 80% conversion efficiency, giving 37% overall detection efficiency, NEP of 1.8e-17 W/Hz^1/2 and photon-number resolving to 9 with 0.14% noise probability per pulse, reported 4 June 2026.
- Optical I/O for superconducting qubits using fibre-integrated photodiode arrays for control delivery showed only a 0.19% single-qubit gate fidelity reduction versus microwave operation, reported 24 December 2025.

## Open questions

- What are the yield, throughput and long-term reliability of micro-transfer printing an electronic chiplet onto a silicon photonic IC at production volume, given the 0.06 mm2 BiCMOS demonstration is described as a first of its kind?
- Does the 71 fJ/b figure for the 32-channel WDM receiver hold across temperature, process corners and ageing once ring and MZI tuning must track a real data-centre thermal environment?
- Is above minus 5 dBm RF power from the 206 GHz MUTC photodiode sufficient for practical sub-THz wireless links, or does it still require amplification that erases the efficiency gain?
- Will any fast room-temperature 3.0 to 3.7 micron detector reach commercial availability, given the stated scarcity, and at what price and package?

---
*Assessment drafted 2026-08-31 from up to 17 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
