---
type: concept
slug: photonics
canonical_name: Photonics
aliases:
- photonics-optics
- Photonics & Optics
kind: theme
parent_concepts:
- photonic-systems
- pic-platforms
related_concepts: []
sources:
- '[[2025-09-23-the-compute-gradient]]'
- '[[2025-04-23-what-if-ai-can-already-feel]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2026-04-17-state-of-the-future-friday-four-67c]]'
- '[[2026-06-05-recursive-until-the-power-bill]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2026-04-22-detecting-proteins-in-blood-with]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2026-04-14-the-photonic-foundry-fallacy]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2022-12-15-im-doing-research-in-venture-capital]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2026-07-07-the-asml-killer]]'
- '[[2026-07-17-the-once-and-future-kimi]]'
- '[[2026-04-24-state-of-the-future-friday-four-002]]'
- '[[2026-07-16-the-path-to-agi-runs-through-hbm]]'
- '[[2026-05-01-state-of-the-future-friday-four-7b7]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2026-07-28-laser-on-a-chip-w-matt-crowley-scintil]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-07-10-the-next-vc-meme-is]]'
scorecard:
  viability: null
  drivers: null
  novelty: null
  diffusion: null
  impact: null
  timing_band: Unclear
  verdict: ''
scorecard_status: draft
mention_count: 1048
descendants:
- diffractive-deep-neural-network
- free-space-photonics
- microwave-photonics
- mid-ir-photonics
- optical-frequency-comb
- optical-frequency-division
- optoelectronic-oscillator
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-24-nist-researchers-supersize-quantum-technology-to-help-detect
  title: NIST Researchers Supersize Quantum Technology to Help Detect Faint Photons
  date: '2026-08-24'
  kind: web
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-08-05-uk-neocloud-landscape-sweep
  title: UK neocloud landscape sweep — filling the coverage gap under the neocloud/serving map
  date: '2026-08-05'
  kind: web
- slug: 2026-08-03-spad-single-photon-market-scan
  title: SPAD / single-photon detector market scan — incumbent structure and company cohort
  date: '2026-08-03'
  kind: web
- slug: 2026-07-31-memory-optics-packaging-chips-act-targets-ais-compute-bottle
  title: 'Memory, optics, packaging: CHIPS Act targets AI''s compute bottleneck - Electronics360'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-31-inference-silicon-roster-sprint
  title: 'Inference-silicon roster verification sprint: 10 companies for the competitive-analysis capital map'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-29-serenity-globalfoundries-receives-support-from-the-us-chips-
  title: 'Serenity: GlobalFoundries receives support from the US CHIPS Act, benefiting Sivers and Lumentum - Bitget'
  date: '2026-07-29'
  kind: web
- slug: 2026-07-29-aeluma-secures-loi-for-up-to-30-million-in-chips-act-funding
  title: Aeluma Secures LOI for Up to $30 Million in CHIPS Act Funding to Advance Photonics Semiconductor R&D - Quiver Quantitative
  date: '2026-07-29'
  kind: web
neighbors: []
---
**Photonic integrated circuits are chip-scale optical systems built from waveguides, modulators, detectors and gain elements, and the current evidence shows a field consolidating around silicon photonics as a foundry base with multiple exotic materials bolted on top rather than converging on one winning platform.**

## Summary

Photonics, in the sense used here, means integrated photonics: routing and manipulating light in lithographically defined waveguides on a chip, in the same way electronics routes current in metal traces. A working photonic integrated circuit (PIC) needs four functional blocks: passive waveguides to move light with low loss, a modulator to imprint electrical signals onto it, a photodetector to convert back, and increasingly a gain medium (laser or amplifier) on the same die. No single material does all four well. Silicon provides excellent low-loss waveguides and CMOS-compatible manufacturing but is a poor modulator material; silicon nitride and aluminium oxide extend transparency to visible and ultraviolet wavelengths but are passive; indium phosphide provides gain and nonlinearity; thin-film lithium niobate (TFLN), thin-film lithium tantalate (TFLT) and barium titanate provide strong electro-optic (Pockels) modulation. The dominant engineering strategy in the sources is therefore heterogeneous integration: bonding or growing the exotic material onto a foundry silicon or nitride platform.

The clearest demonstration of that strategy is a 320 Gb/s unamplified link built from a 100 GHz germanium photodiode and a TFLN Mach-Zehnder modulator on a foundry-compatible silicon photonics platform at imec, dated April 2026, which is read in the sources as evidence for multi-platform coexistence rather than convergence to a single material <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup>. Comparable platform-extension results appear at the wavelength extremes and in gain: the first integrated ultraviolet electro-optic modulator on TFLT reports a VπL of 85 mV·cm at 375 nm, 22.7 dB extinction ratio and 1.3 dB insertion loss, claimed as up to four orders of magnitude better bandwidth/VπL than bulk crystals; ytterbium gain integrated into an aluminium oxide platform delivers over 0.5 W output, above 70% optical-to-optical conversion efficiency, a 3.3 dB noise figure and 14 kW peak power in femtosecond amplification.

The parameters that decide any given photonic platform are: insertion loss per component and per centimetre, modulation efficiency (VπL) against bandwidth, whether gain is on-chip or off-chip, operating temperature, and whether the process exists inside a commercial foundry with a design kit. That last one is doing most of the work commercially. Two of the compute-oriented results in this set are explicitly designed against named foundry processes, a photonic ROM lookup-table engine simulated on the GlobalFoundries 45SPCLO silicon photonics platform, and the integrated ytterbium gain platform is stated to be compatible with heterogeneous integration into standard photonic platforms.

Beyond interconnect, the sources cover two speculative application layers. Optical computing: an InP semiconductor-optical-amplifier all-optical neuron using cross-gain modulation as the nonlinearity, analysed at system level, reports 47 TMAC/s (about 2.5 times a then-state-of-the-art GPU), 12 pJ/MAC (about 2 times better) and under 20 pJ/op including transceivers and electrical control when synapses per neuron exceed 18. Quantum photonics: an integrated rare-earth quantum memory in Eu:Y2SiO5 reaching 80.3% storage-retrieval efficiency and 69.8% for telecom-heralded single photons, but only at cryogenic temperature <sup class="ref"><a href="https://arxiv.org/abs/2511.05928" title="Efficient integrated quantum memory for light (¹⁵¹Eu³⁺:Y₂SiO₅, AFC, telecom-heralded)" rel="noopener">ref</a></sup>.

## Viability (unscored)

## Drivers (unscored)

## Novelty (unscored)

## Diffusion (unscored)

## Impact (unscored)

## Timing Unclear

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
