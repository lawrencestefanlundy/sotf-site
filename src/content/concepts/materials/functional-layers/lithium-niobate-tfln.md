---
type: concept
slug: lithium-niobate-tfln
canonical_name: Lithium Niobate (TFLN)
aliases:
- tfln
- lithium niobate
- lithium-niobate
kind: material
parent_concepts:
- materials
- functional-layers
related_concepts: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
frontier:
- Can fibre-to-chip and laser-to-chip coupling losses be cut from the 15-16 dB bare-chip figures reported in hybrid TFLN transmitter arrays to link-budget-viable levels, and at what packaging cost 2026 06 05 hybrid integrated dfb laser coupled 1 8 thin film lithium ni?
- Is DC drift a material property that must be designed around at circuit level, or can buffer-layer and surface engineering eliminate it well enough for multi-year biased operation 2026 06 02 drift free characterization of electro optic tuning efficien?
- Does the >95% printing yield and 420 nm placement accuracy hold across many wafer lots and outside the originating pilot line 2026 05 29 micro transfer printing of lithium niobate on 200 mm silicon?
- How far does thin-film lithium tantalate encroach beyond the visible band, given its demonstrated advantage in sustained optical power handling at 532 nm 2026 05 14 robust and active visible light integrated photonics on thin?
last_updated: '2026-08-31'
tags:
- concept
- material
mention_count: 153
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
sources_7d: 3
sources_30d: 15
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-05-02-lightium-tfln-foundry-csem-spin-off
  title: Lightium TFLN Foundry (CSEM spin-off)
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-top-tfln-modulator-companies-2026
  title: Top TFLN Modulator Companies 2026
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-standardized-tfln-pics-ieee
  title: Standardized TFLN PICs (IEEE)
  date: '2026-05-02'
  kind: web
- slug: 2026-04-22-photonics-material-class-war-320-gb-s-unamplified
  title: 320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform
  date: '2026-04-22'
  kind: web
- slug: 2026-04-03-photonic-packaging-cpo-the-soitec-twin-a-massive
  title: The Soitec Twin? A Massive Undiscovered Foundational Photonics Play & The Fab Nobody Is Watching
  date: '2026-04-03'
  kind: web
- slug: 2026-03-30-photonics-material-class-war-silicon-photonics-and-photonic
  title: 'Silicon Photonics and Photonic Integrated Circuits 2026-2036: Technologies, Markets, and Forecasts'
  date: '2026-03-30'
  kind: web
- slug: 2026-03-12-photonics-material-class-war-hyperlight-umc-and-wavetek
  title: HyperLight, UMC, and Wavetek Announce Strategic Partnership for High-Volume Foundry Production of TFLN Chiplet Platform
  date: '2026-03-12'
  kind: web
neighbors: []
---
**Thin-film lithium niobate is a sub-micron single-crystal Pockels-effect layer bonded onto silicon or oxide wafers, and in 2026 it moved from lab modulators to 200 mm wafer-scale integration with >95% printing yield and 320 Gb/s unamplified links, while simultaneously setting records in integrated quantum optics such as 18 dB of on-chip squeezing <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup>.**

## Summary

Lithium niobate (LiNbO3) has been the workhouse crystal of telecoms modulators for decades, but as a bulk material it is used in centimetre-scale discrete components. Thin-film lithium niobate (TFLN) is the same crystal bonded as a sub-micron layer onto an insulator and etched into ridge waveguides, so that light is confined tightly enough for the electrodes to sit microns away from the optical mode. The physics being exploited is the Pockels effect: an applied voltage changes the refractive index linearly and essentially instantaneously, with no free-carrier injection. That gives modulators with flat, high-frequency response, low chirp and low optical loss, in contrast to silicon modulators which rely on carrier depletion. The same crystal has a large second-order nonlinearity (used for frequency conversion and photon-pair generation when the domains are periodically poled) and is piezoelectric (used for acousto-optic devices), so one material covers modulation, nonlinear optics and transduction.

The parameters that decide whether TFLN wins are not exotic. First, the voltage-length product VπL, which sets how short and how low-power a modulator can be: recent hybrid arrays report 2.52-2.68 V·cm with half-wave voltages of 3.60-3.83 V and >40 GHz 3 dB bandwidth. Second, insertion loss, and specifically fibre-to-chip and laser-to-chip coupling: the same array reports 15.19-16.55 dB bare-chip insertion loss plus additional DFB bonding loss, which is the sort of number that keeps a device in the lab. Third, manufacturability at silicon-photonics wafer scale, since LN is not a CMOS-line material and must be bonded or transfer-printed. Fourth, bias stability: DC drift from charge redistribution and surface screening makes even the characterisation of high-Q LN cavities unreliable under quasi-static voltage scans.

The 2026 evidence base splits into two distinct application stacks. In datacentre interconnect, micro-transfer printing has been demonstrated across four full 200 mm wafers with 3σ placement accuracy down to 420 nm, printing yield above 95%, insertion loss below 2 dB across 600 phase modulators and a 4 V half-wave voltage, with a variability-aware design workflow built on pilot-line fabrication data to make that repeatable, and a system demonstration of 320 Gb/s unamplified transmission pairing a 100 GHz germanium photodiode with a TFLN Mach-Zehnder modulator on a foundry-compatible silicon photonics platform <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup>. In quantum and nonlinear photonics, TFLN is producing the strongest integrated results anywhere: 18 dB of continuous-wave on-chip squeezing in a 1.6 cm adaptively poled waveguide, described as the highest for any integrated photonic platform; the first on-chip telecom quantum memory in TFLN using erbium doping; and cavity-enhanced memory with 23.3% on-chip storage efficiency plus electro-optic frequency routing at 20 MHz. Poling length, historically capped near 10 mm, has been pushed to 70 mm of continuous poled area at a 3 µm period.

## Viability (4/5)

The devices work, and the manufacturing evidence has moved beyond single hero chips. Micro-transfer printing of LN onto 200 mm silicon photonics has been shown across four full wafers with >95% printing yield, 420 nm 3σ placement accuracy, sub-2 dB insertion loss over 600 phase modulators and a 4 V half-wave voltage. A companion variability-aware simulation framework, calibrated on pilot-line fabrication-variation data, argues that stable performance across a wafer can be systematically engineered rather than found by luck. At system level, 320 Gb/s unamplified transmission has been shown with a TFLN modulator and 100 GHz Ge photodiode on a foundry-compatible platform <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup>. Long, uniform periodic poling, long the bottleneck for nonlinear devices, has gone from a practical ceiling near 10 mm to 70 mm continuous, and low-loss 1.2 cm PPLN waveguides have been fabricated with an isotropic-etch route that avoids the anisotropic etching that previously limited losses to a few dB/cm.

Two weaknesses are documented in the same sources and stop this being a 5. DC drift, arising from charge redistribution, surface screening or buffer-layer relaxation, makes sustained-bias operation and even measurement unreliable in high-Q LN cavities, demonstrated across 35 devices. And optical interfacing is still expensive: a hybrid DFB-coupled 1×8 modulator array reports 15.19-16.55 dB bare-chip insertion loss with further loss on laser bonding. Power handling is also a limit in the visible band, where thin-film lithium tantalate modulators remained stable at 5 dBm for an hour under conditions that TFLN counterparts of similar structure could not achieve.

**TLDR: Wafer-scale yield and loss numbers now exist on 200 mm silicon photonics; bias drift and coupling loss remain unsolved.**

## Drivers (4/5)

On demand, the sources are unambiguous about who is paying: the growth of AI and other datacentre applications is driving demand for photonic interconnects combining high speed with low energy, and scalability is stated as the critical requirement that motivates wafer-scale TFLN integration. A second demand vector is photonic analog computing, where lithium niobate photonics with channel equalisation delivered 6-bit precision homodyne multiplication at 128 GS/s with 6 ns latency. A third, slower vector is quantum networking, where TFLN is being positioned as the substrate for integrated repeaters and registers.

On supply, the shift is from university cleanrooms to institutional pilot lines: the variability-aware workflow is built on data from a dedicated pilot line, the 200 mm printing work carries a large industrial-scale author list, and standardisation of TFLN PICs is now the subject of IEEE publication <sup class="ref"><a href="https://ieeexplore.ieee.org/document/11046594/" title="Standardized TFLN PICs (IEEE)" rel="noopener">ref</a></sup>, though the content of that standardisation is not available in the supplied material. Enabling process capability is also improving independently, for example foundry-compatible zero-crosstalk waveguide designs demonstrated across multiple material platforms including lithium niobate.

**TLDR: AI datacentre interconnect demand is the explicit pull; supply side now has pilot lines, standardisation activity and transfer-printing tooling.**

## Novelty (4/5)

The comparison the sources support most cleanly is against integrated alternatives rather than bulk LN. In quantum optics, 18 dB of on-chip squeezing with 20 dB anti-squeezing at 1570 nm in a 1.6 cm adaptively poled waveguide is stated to be the highest squeezing reported for any integrated photonic platform, and the first with assumption-free statistical validation. In quantum memory, erbium-doped TFLN storage of 400 ns at 1.95% efficiency with 96.8% qubit fidelity is described as significantly outperforming conventional waveguide delay lines, and as the first on-chip memory in this platform; the cavity-enhanced version reaches 23.3% on-chip efficiency with a 277.6 s comb lifetime and sub-10⁻⁴ inter-channel crosstalk during electro-optic routing. Photon-pair generation with pump-polarisation-selectable Bell states needs no additional optical elements and uses existing LN fabrication, unlike transition-metal-dichalcogenide thin films which the authors note are neither widely available nor fabrication-compatible.

For interconnect, the numbers are strong but the head-to-head margin over silicon or polymer modulators is asserted rather than measured in these sources: VπL of 2.52-2.68 V·cm with >40 GHz bandwidth and ~25 dB extinction ratio in an eight-channel array and 320 Gb/s unamplified in a heterogeneous SiPh demonstration <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup>. Novelty is not absolute: thin-film lithium tantalate, a very close cousin, already beats TFLN on visible-band power stability while delivering ~50 GHz flat response at 532 nm, which suggests the material class rather than this specific crystal is what is novel.

**TLDR: Better than silicon modulators on bandwidth, chirp and drive voltage, and the best integrated platform on record for squeezing.**

## Diffusion (3/5)

The adoption strategy is explicit and sensible: rather than asking the industry to move to a new platform, TFLN is being heterogeneously placed onto existing 200 mm silicon photonics by micro-transfer printing, preserving the incumbent process flow. The imec demonstration is read in the supplied thesis material as evidence for multi-platform coexistence rather than convergence on a single winning material <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup>, which matters for diffusion: TFLN can be adopted as a functional layer in someone else's stack. Standardisation work has begun <sup class="ref"><a href="https://ieeexplore.ieee.org/document/11046594/" title="Standardized TFLN PICs (IEEE)" rel="noopener">ref</a></sup>.

The barriers are real. Packaging economics are dominated by coupling: 15-16 dB bare-chip insertion loss plus laser bonding loss in a current hybrid transmitter array is far from a shippable link budget. Long-term bias stability under DC drift is unresolved and, as of these sources, is being handled by changing the measurement method rather than the material. Wafer-scale poling uniformity is improving but duty-cycle variation still depends on electrode strategy. And in any application involving visible wavelengths or high on-chip optical power, lithium tantalate is a documented substitute. The sources do not contain shipment volumes, prices or qualification data, so the assessment here is of technical readiness for diffusion, not of diffusion itself.

**TLDR: Foundry compatibility is being engineered deliberately, but coupling loss, bias drift, immature standards and sibling materials all slow uptake.**

## Impact (4/5)

The value case rests on two large markets. In datacentre and AI interconnect, a modulator layer that supports 320 Gb/s unamplified links <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup> and can be printed onto existing 200 mm silicon photonics at >95% yield sits directly in the path of the bandwidth and energy-per-bit problem that the sources name as the driver. In photonic computing, LN-based homodyne logic at 128 GS/s with 6 ns latency addresses the analog-accuracy barrier that has held photonic accelerators back.

The second and less certain slice is quantum. TFLN now hosts record integrated squeezing, the first on-chip telecom quantum memory in the platform, programmable spectral routing of stored photons with entanglement preserved to more than 11 standard deviations of witness violation, tunable entangled-pair sources and acousto-optic transduction with a 1.004 V·cm half-wave voltage-length product. That is a plausible single-material route to a quantum repeater node, but memory efficiencies of 1.95% and 23.3% are far from what a repeater needs, so the impact here is contingent on further orders of magnitude.

**TLDR: If it holds, TFLN becomes the default active layer for high-speed optical I/O and the substrate for integrated quantum photonics.**

## Timing Soon (2-5yr)

The interconnect case is at the pilot-line-to-product transition. Four-wafer 200 mm printing with >95% yield and a variability-aware design flow are exactly the artefacts that precede a foundry process offering, not a research result, and standardisation activity has started <sup class="ref"><a href="https://ieeexplore.ieee.org/document/11046594/" title="Standardized TFLN PICs (IEEE)" rel="noopener">ref</a></sup>. What is missing before revenue is coupling-loss reduction and reliability data under sustained bias. Two to five years is the reasonable band for TFLN appearing as a routine option in commercial silicon photonics transmitters.

The nonlinear and quantum applications run later. Poling has only just reached 70 mm continuous length, and memory efficiency is in the single-to-low-double-digit percent range. The squeezing result is immediately usable for sensing and continuous-variable experiments, but network-scale deployment is not supported by these sources.

**TLDR: Wafer-scale manufacturing evidence exists now; qualified volume product and quantum applications are further out.**

## Overrated or underrated? Fairly rated

TFLN is one of the few photonics material stories where the hype and the data are roughly aligned. The 2026 record is not a set of isolated device demonstrations: it is wafer-scale yield statistics, a variability-aware design methodology, a system-level 320 Gb/s link, standardisation activity, and simultaneously the best integrated squeezing and first in-platform telecom quantum memory. That breadth across modulation, nonlinear optics, acousto-optics and quantum memory in one crystal is genuinely unusual and justifies the attention.

Where the enthusiasm needs discipline is on the boring integration numbers and on the assumption of a single winner. Bare-chip insertion losses in the mid-teens of dB and unresolved DC drift are the kind of problems that decide whether a platform ships. The supplied thesis material reads imec's heterogeneous approach as evidence of coexistence rather than convergence <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup>, and lithium tantalate already beats TFLN on visible-band power stability. The correct expectation is TFLN as a widely used functional layer inside silicon photonics, not a platform that displaces it.

## Prediction

By 31 December 2028, at least one commercial silicon photonics foundry will publish a PDK-supported heterogeneous TFLN modulator process on 200 mm or larger wafers, reporting half-wave voltage at or below 4 V and printing or bonding yield above 95%, replicating the imec pilot-line results.

## Evidence base

- 2026-05-29: Micro-transfer printing of TFLN across four full 200 mm silicon photonics wafers, 3σ placement accuracy down to 420 nm, printing yield >95%, insertion loss <2 dB over 600 phase modulators, 4 V half-wave voltage.
- 2026-04-22: 320 Gb/s unamplified transmission using a 100 GHz Ge photodiode and TFLN Mach-Zehnder modulator heterogeneously integrated on a foundry-compatible silicon photonics platform at imec <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup>.
- 2026-05-28: 18 dB continuous-wave on-chip squeezing and 20 dB anti-squeezing at 1570 nm in a 1.6 cm adaptively poled TFLN waveguide, stated as the highest for any integrated photonic platform.
- 2026-05-15: Cavity-enhanced erbium-doped TFLN microring memory with 23.3 ± 0.5% on-chip storage efficiency for 100 ns storage, 277.6 ± 52.6 s comb lifetime, electro-optic routing to 20 MHz with crosstalk below 10⁻⁴.
- 2026-06-05: Continuous wafer-scale periodic poling extended to 70 mm at 3 µm period with close to 50% duty cycle, against a prior practical ceiling near 10 mm.
- 2026-06-05: Hybrid DFB-coupled 1×8 TFLN modulator array with >40 GHz 3 dB bandwidth per channel, VπL 2.52-2.68 V·cm, ~25 dB extinction ratio, but 15.19-16.55 dB bare-chip insertion loss plus laser bonding loss.
- 2026-05-14: Thin-film lithium tantalate modulators at 532 nm remained stable delivering 5 dBm modulated optical power for an hour, which the authors state TFLN counterparts of similar structure cannot achieve.

## Open questions

- Can fibre-to-chip and laser-to-chip coupling losses be cut from the 15-16 dB bare-chip figures reported in hybrid TFLN transmitter arrays to link-budget-viable levels, and at what packaging cost?
- Is DC drift a material property that must be designed around at circuit level, or can buffer-layer and surface engineering eliminate it well enough for multi-year biased operation?
- Does the >95% printing yield and 420 nm placement accuracy hold across many wafer lots and outside the originating pilot line?
- How far does thin-film lithium tantalate encroach beyond the visible band, given its demonstrated advantage in sustained optical power handling at 532 nm?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
