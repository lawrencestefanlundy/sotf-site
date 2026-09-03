---
type: concept
slug: silicon-photonics
canonical_name: Silicon Photonics
aliases: []
kind: technology
parent_concepts:
- photonic-systems
- pic-platforms
related_concepts: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2026-04-17-state-of-the-future-friday-four-67c]]'
- '[[2026-06-05-recursive-until-the-power-bill]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2026-04-14-the-photonic-foundry-fallacy]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2026-07-28-laser-on-a-chip-w-matt-crowley-scintil]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
scorecard:
  viability: 4
  drivers: 4
  novelty: 3
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 159
descendants:
- avalanche-photodiode
- optical-gyroscope
sources_7d: 1
sources_30d: 3
recent_mentions:
- slug: 2026-07-28-laser-on-a-chip-w-matt-crowley-scintil
  title: Laser on a Chip w/ Matt Crowley @ Scintil Photonics
  date: '2026-07-28'
  kind: substack
- slug: 2026-07-11-neutral-pdk-heterogeneous-integration-landscape
  title: Neutral PDK / EDA layer for heterogeneous photonic integration — landscape check (Scintil essay correction research)
  date: '2026-07-11'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-15-gf-investor-day-2026
  title: GlobalFoundries Investor Day 2026 (presentation)
  date: '2026-06-15'
  kind: web
- slug: 2026-06-09-photonic-foundry-capacity-silicon-photonics-chips-the
  title: 'Silicon Photonics Chips: The Foundry War'
  date: '2026-06-09'
  kind: web
- slug: 2026-06-05-recursive-until-the-power-bill
  title: Recursive, Until the Power Bill
  date: '2026-06-05'
  kind: substack
- slug: 2026-05-30-optical-interconnect-ma-ledger
  title: Optical-interconnect / photonic-packaging M&A ledger (2019-2026)
  date: '2026-05-30'
  kind: web
- slug: 2026-05-02-bto-pockels-modulator-on-silicon-photonics-jlt-2019
  title: BTO Pockels modulator on silicon photonics (JLT 2019)
  date: '2026-05-02'
  kind: web
neighbors: []
---
**Silicon photonics builds optical circuits in the silicon device layer of CMOS wafers, and is now shipping as commercial foundry platforms whose remaining weaknesses (no Pockels effect, no native laser) are being patched by wafer-scale heterogeneous integration of lithium niobate, III-V and electronic chiplets.**

## Summary

Silicon photonics (SiPh) means patterning waveguides, splitters, resonators and detectors into the silicon layer of a silicon-on-insulator wafer using the same lithography, etch and deposition toolset as CMOS logic. The canonical geometry is a 220 nm thick silicon layer, used both for single-mode strip waveguides and, in recent work, for freely propagating slab beams steered by etched total-internal-reflection mirrors that avoid sidewall-roughness loss altogether. Germanium grown on silicon supplies the photodetectors, and in monolithic platforms such as GlobalFoundries Fotonix the transistors sit on the same die as the optics. Silicon nitride is used alongside silicon where lower loss or shorter wavelengths are needed.

The platform has two structural gaps. Silicon has no linear electro-optic (Pockels) effect, so modulation relies on carrier depletion or thermal tuning, which limits speed, linearity and energy. And silicon's indirect bandgap means no on-chip laser. Both gaps are being closed by bonding or printing other materials onto the same wafer: thin-film lithium niobate (TFLN) and barium titanate for modulators <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://opg.optica.org/jlt/abstract.cfm?uri=jlt-37-5-1456" title="BTO Pockels modulator on silicon photonics (JLT 2019)" rel="noopener">ref</a></sup>, III-V quantum-dot gain sections for 1.3 um lasers, phase-change films such as Sb2Se3 for non-volatile reconfiguration, and even BiCMOS electronic chiplets printed directly onto the photonic die. Micro-transfer printing has emerged as the wafer-scale vehicle for this.

Beyond datacom, the same fabrication base is being reused for mid-infrared biosensing in germanium-on-silicon, hardware security primitives, quantum-graph physics platforms, and optical computing architectures including microring ROM lookup engines and fully optical convolutional networks. These derivative uses are at very different maturities from the interconnect use case and should not be scored together.

## Viability (4/5)

The evidence base here is unusually hard for a deep-tech page: these are fabricated and measured parts, not concepts. A monolithic receiver analogue front end in the GlobalFoundries Fotonix platform was fabricated and characterised to 64 GBaud with 28.9 GHz bandwidth, 61.7 dBohm gain and 9.22 mW consumption from a 1.2 V supply, giving 0.08 pJ/bit. A 3D-integrated receiver built by printing a 0.06 mm2 BiCMOS chiplet onto a silicon photonic IC delivered 224 Gb/s PAM-4 at minus 5.2 dBm OMA sensitivity and 0.51 pJ/b. On the manufacturing side, TFLN micro-transfer printing has been run across four full 200 mm wafers with 3-sigma placement accuracy down to 420 nm, printing yield above 95 per cent, insertion loss below 2 dB across 600 phase modulators and a half-wave voltage of 4 V.

What holds this back from a 5 is that the two hardest pieces are the least settled. The 1.3 um III-V quantum-dot laser work in the sources is a numerical study of coupling into 220 nm silicon waveguides, not a measured device, and the wafer-scale LN modulator variability work is explicitly a simulation framework fed by pilot-line data, with feasibility shown theoretically rather than in volume. The 400 Gb/s coherent co-packaged transmitter is a link-level model in a commercial process, not silicon. The sources also carry no reliability, ageing or qualification data at all.

**TLDR: Fabricated, measured hardware in commercial foundry processes, with the heterogeneous steps now demonstrated at 200 mm wafer scale.**

## Drivers (4/5)

On the demand side, the sources are consistent and explicit. The micro-transfer printing work opens on AI and data centre growth driving demand for photonic interconnects combining high speed with low energy, with scalability as the critical requirement. The 3D BiCMOS receiver is framed the same way. Co-packaged optics is described as the response to bandwidth, shoreline density and energy efficiency requirements of future GPUs and network switches for AI, and chip-to-chip silicon photonics is described as gaining traction in scale-up interconnect domains.

On the supply side, the enabling asset is that silicon photonics rides existing CMOS infrastructure. Multiple named commercial platforms appear across the sources (GlobalFoundries Fotonix and 45SPCLO), and a dedicated 200 mm pilot line supplies the fabrication-variation data used for wafer-scale modulator design. Inverse design tooling has shifted over the past five to ten years from university proof of concept towards commercial foundries and practical silicon photonics, which lowers the design-cost driver. The sources give no market size, capacity or capex figures, so the demand judgement rests on stated motivation rather than measured volume.

**TLDR: AI datacentre bandwidth and energy demand is named repeatedly as the pull; foundry PDKs and 200 mm pilot lines are the push.**

## Novelty (3/5)

Silicon photonics is a two-decade-old field by the sources' own account, with inverse design for it reviewed as an established discipline and Pockels modulators on silicon photonics dating to at least a 2019 journal paper <sup class="ref"><a href="https://opg.optica.org/jlt/abstract.cfm?uri=jlt-37-5-1456" title="BTO Pockels modulator on silicon photonics (JLT 2019)" rel="noopener">ref</a></sup>. Scoring it as a novel technology would be wrong. What is new in this evidence window is the combination step: putting TFLN, BiCMOS electronics and phase-change films onto a standard SiPh die at wafer scale. That is where the measurable deltas sit. Printing electronics directly onto the photonic IC is described as pioneering relative to prior micro-transfer printing work that only moved photonics, and the claimed gain is a record-small footprint plus 0.51 pJ/b at 224 Gb/s by removing inter-process parasitics.

What is it better than? Against pure-silicon carrier-depletion modulation, TFLN on SiPh reached 320 Gb/s unamplified with a 100 GHz germanium photodiode <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup>. Against electrical I/O, the sources assert but do not quantify the advantage. Against thermally tuned reconfiguration, Sb2Se3 offers non-volatile, reversible, ultra-low-loss tuning at telecom wavelengths on standard 220 nm silicon photonics, again without a stated power-saving figure. The absence of head-to-head baselines in these sources is the main reason not to score higher.

**TLDR: The platform itself is mature, not novel; the genuine step change is heterogeneous augmentation of silicon rather than silicon alone.**

## Diffusion (4/5)

Diffusion is further along than for most technologies on this taxonomy. Independent groups are designing into named commercial silicon photonics processes and getting parts back: Fotonix for a monolithic receiver front end, 45SPCLO for a device-level photonic ROM study, and a foundry-provided commercial process for coherent CPO transmitter modelling. Inverse design has been translated to commercial foundries. The 220 nm silicon thickness constraint is treated as the compatibility line that designs must respect to stay CMOS-compatible.

The barriers are specific. First, the light source: quantum-dot III-V lasers give temperature insensitivity but their high-index (Al)GaAs makes coupling to 220 nm silicon hard, which is why many designs use thicker, non-standard silicon. Second, heterogeneous yield: 95 per cent print yield and 420 nm placement 3-sigma are good but are four-wafer results, and the accompanying variability framework exists precisely because performance stability across a wafer is not yet a solved problem. Third, test and diagnostics: optical frequency-domain reflectometry exists for infrared silicon photonics but visible PICs lacked an equivalent until spectral-domain OCT was adapted, achieving 50 dB dynamic range, 8 um axial resolution in silicon nitride and 2 mm imaging depth. Fourth, at system level, circuit-switched photonic interconnects impose non-negligible reconfiguration overhead that has to be scheduled around rather than ignored.

**TLDR: Already inside commercial PDKs and 200 mm lines; the barriers are the laser, the heterogeneous yield ramp, and test.**

## Impact (4/5)

If the interconnect case holds, the value is large and the sources are consistent about where it lands: bandwidth, shoreline density and energy efficiency for GPUs and switches, and chip-to-chip links in scale-up domains. Energy per bit is the number that matters and it is moving: 0.51 pJ/b for a full 224 Gb/s PAM-4 receiver and 0.08 pJ/bit for a monolithic front end.

The secondary applications broaden the impact but are earlier. Mid-infrared germanium-on-silicon waveguide sensing reached a 2.20 mg/L limit of detection for phenytoin against a 10 to 20 mg/L therapeutic window, which validates silicon photonics for point-of-care biomedical spectroscopy. Optical computing on the same platform is far weaker evidence: a fully photonic CNN reaching 94 per cent on MNIST is a proof of principle on a trivial benchmark, and the photonic ROM is device-level simulation only. Impact should be underwritten by interconnect, not by photonic compute.

**TLDR: Sits on the AI interconnect bottleneck, with credible secondary reach into sensing, security and quantum on the same fab base.**

## Timing Now (0-2yr)

For the core datacom use case the answer is now. Measured parts in commercial foundry platforms exist today at 224 Gb/s PAM-4 and 64 GBaud, and 320 Gb/s unamplified transmission has been shown on a foundry-compatible platform <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup>. The technology is not waiting on a discovery.

The heterogeneous layer is on a slower clock. TFLN on 200 mm SiPh is at four-wafer demonstration with a variability framework only just published, which reads as a 2 to 5 year path to PDK-grade availability. Coherent CPO beyond PAM-4 is still at link-level simulation. Photonic compute and quantum uses on this platform sit further out and the sources give no timeline for them.

**TLDR: Datacom transceiver and receiver components are already fabricated in commercial processes; wafer-scale TFLN augmentation is 2 to 5 years behind that.**

## Overrated or underrated? Fairly rated

Silicon photonics is correctly understood as the default integrated photonics platform, and the evidence here supports that reading rather than overturning it. The specific claim worth pushing back on is the framing of a materials contest with a single winner. The imec result is explicitly indexed as evidence that heterogeneous TFLN on silicon photonics represents multi-platform coexistence rather than convergence to one platform <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup>, and the printing data supports that: silicon supplies the wafer, the passives, the germanium detectors and the CMOS, while lithium niobate, III-V and phase-change films are added locally where silicon is physically incapable.

The part of the story that is overrated in the sources is photonic computing on this substrate. A 94 per cent MNIST result and a simulated microring ROM carry nowhere near the weight of the transceiver evidence, and an investor pricing silicon photonics on optical AI accelerators is pricing a different, much earlier technology than the one that has 200 mm wafer yield data.

## Prediction

By 31 December 2028, at least one commercial silicon photonics foundry will offer heterogeneously integrated thin-film lithium niobate modulators as a supported PDK element on 200 mm wafers, building on the greater than 95 per cent print yield and 420 nm 3-sigma placement accuracy demonstrated in May 2026.

## Evidence base

- 22 April 2026: 320 Gb/s unamplified transmission using a 100 GHz germanium photodiode and a TFLN Mach-Zehnder modulator on a foundry-compatible silicon photonics platform at imec, indexed as evidence for multi-platform coexistence rather than convergence <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup>.
- 29 May 2026: TFLN micro-transfer printing across four full 200 mm silicon photonics wafers with 3-sigma placement accuracy down to 420 nm, printing yield above 95 per cent, insertion loss below 2 dB over 600 phase modulators and a 4 V half-wave voltage.
- Published 28 November 2025: a BiCMOS electronic chiplet of 0.06 mm2 printed directly onto a silicon photonic IC gave 224 Gb/s PAM-4 at minus 5.2 dBm OMA sensitivity (BER 2.4e-4) and 0.51 pJ/b.
- Published 7 May 2026: a monolithic receiver front end in the GlobalFoundries Fotonix platform achieved 28.9 GHz bandwidth, 61.7 dBohm gain, validation to 64 GBaud and 0.08 pJ/bit from 9.22 mW at 1.2 V.
- 28 May 2026: wafer-scale integration of lithium niobate modulators on silicon photonics via micro-transfer printing shown to be feasible only theoretically, using fabrication-variation data from a dedicated pilot line.
- Published 2 March 2026: mid-infrared germanium-on-silicon waveguide sensing of phenytoin reached a 2.20 mg/L limit of detection against a 10 to 20 mg/L therapeutic window, validating silicon photonics for biomedical infrared spectroscopy.

## Open questions

- Does the 95 per cent micro-transfer-printing yield and sub-2 dB insertion loss hold across hundreds of wafers rather than four, and what is the resulting known-good-die cost penalty versus monolithic silicon modulators?
- Can a CMOS-compatible 220 nm silicon waveguide III-V quantum-dot laser be demonstrated experimentally, or does on-chip gain continue to require non-standard silicon thicknesses?
- Do the simulated coherent CPO figures (400 Gb/s offset-QAM-16 at 9.65 dBm laser power) survive fabrication in a commercial process, or does thermal drift in microring modulators erode the link budget?
- What is the measured energy-per-bit and cost advantage of silicon photonic chip-to-chip links over electrical I/O at equivalent reach, net of reconfiguration overhead in circuit-switched topologies?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
