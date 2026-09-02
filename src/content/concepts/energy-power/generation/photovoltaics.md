---
type: concept
slug: photovoltaics
canonical_name: Photovoltaics
aliases: []
parent_concepts:
- generation
- energy-power
related_concepts: []
sources:
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2026-08-31-qcells-tandem-iec-ul-certification-tuv-rheinland]]'
- '[[2025-06-25-meyer-burger-insolvency-europe]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 40
frontier:
- 'If bulk point-defect Shockley-Read-Hall recombination cannot explain the efficiency limits of trigonal selenium cells 2026 06 16 defect tolerance in trigonal selenium photovoltaics, what does: interfaces, contacts, grain boundaries or transport?'
- Can the deep-level defects and mixed cation valences in solution-deposited Bi2FeCrO6 and Bi2MnCrO6 films be suppressed enough to yield a working cell, and what open-circuit voltage does that give 2026 05 06 beyond lead halide perovskites visible light photovoltaics w?
- Does the luminescent angle restrictor's predicted non-equilibrium emission profile survive an experimental test, and what measured efficiency gain does it produce over a flat-plate control 2026 07 24 emergent non equilibrium emission profiles via luminescent a?
- How many other reported photovoltaic enhancement mechanisms with high replication rates fail a photon-statistics or equivalent mechanism-level test, as Yb3+:CsPbCl3 did 2026 07 01 photon statistics from yb3 doped cspbcl3 are inconsistent wi?
- Does the predicted defect tolerance of trigonal selenium translate into measured open-circuit voltage deficits in fabricated devices, and if not, which non-point-defect loss channel dominates? 2026 06 16 defect tolerance in trigonal selenium photovoltaics
- Can Bi2MCrO6 (M = Fe, Mn) films be processed to eliminate mixed cation valences and deep-level defects, and what cell efficiency results? 2026 05 06 beyond lead halide perovskites visible light photovoltaics w
- Do any Yb3+-doped halide perovskite compositions pass a photon-bunching test for genuine quantum cutting, or is the reported above-unity quantum yield an artefact across the whole family? 2026 07 01 photon statistics from yb3 doped cspbcl3 are inconsistent wi
- What power density and conversion efficiency can transverse thermophotovoltaic devices achieve experimentally, and how does impurity scattering set the practical ceiling? 2026 05 28 transverse thermophotovoltaics from nonreciprocal plasmon dr
- By how much does luminescent angle restriction raise achievable conversion efficiency above the flat-plate detailed-balance limit in a measured cell? 2026 07 24 emergent non equilibrium emission profiles via luminescent a
scorecard:
  viability: 2
  drivers: 3
  novelty: 3
  diffusion: null
  impact: null
  timing_band: Later (5-10yr)
  verdict: Too early to say
scorecard_status: draft
sources_7d: 2
sources_30d: 4
recent_mentions:
- slug: 2026-08-31-qcells-tandem-iec-ul-certification-tuv-rheinland
  title: Qcells secures TUV Rheinland certification for perovskite-silicon tandem solar tech (pv magazine, 16 Jul 2026; pv-tech corroborating)
  date: '2026-08-31'
  kind: web
- slug: 2025-06-25-meyer-burger-insolvency-europe
  title: Meyer Burger files Chapter 11 / European insolvency, Chinese overcapacity kills European module manufacturing
  date: '2025-06-25'
  kind: web
- slug: 2024-10-29-deploy-intelligence-too-cheap-to
  title: Deploy! Intelligence too cheap to meter @ $0.0001 per million tokens.
  date: '2024-10-29'
  kind: substack
neighbors: []
---
**Photovoltaics converts light directly into electricity in a semiconductor absorber, and the research frontier visible in current work is not silicon but the hunt for lead-free, defect-tolerant absorbers plus light-management schemes that beat the standard detailed-balance assumptions.**

## Summary

A photovoltaic (PV) cell is a semiconductor absorber in which photons above the band gap create electron-hole pairs that are separated by a built-in asymmetry (usually a junction) and extracted as current. The ceiling on efficiency comes from detailed balance, the Shockley-Queisser argument that relates the non-equilibrium operating cell to an equilibrium radiative reference state, with the angular and spectral radiative channels conventionally set by the cell's equilibrium absorptivity and emissivity. The parameters that decide a given material are therefore: band gap matched to the illuminating spectrum, absorption strength, carrier density and mobility, and the rate at which photogenerated carriers recombine, radiatively or via defects.

Most of the current literature on this concept is upstream absorber search. Lead toxicity and ambient instability in lead halide perovskites are driving work on alternatives: solution-deposited 350-450 nm films of the bismuth oxide double perovskites Bi2FeCrO6 and Bi2MnCrO6 show monoclinic P21/c structure, strong visible absorption (alpha around 10^4-10^5 cm^-1) and carrier densities of 10^17-10^20 cm^-3, but also mixed cation valences and deep-level defects. Trigonal selenium has re-emerged because its wide gap suits tandem top cells and indoor use; first-principles work across a large set of point defects finds it intrinsically defect tolerant, because non-radiative multi-phonon capture is suppressed by large lattice reorganisations and energy releases of at least 0.5 EG per event, so bulk Shockley-Read-Hall recombination cannot account for measured device losses. Adjacent work targets the charge-separation step itself: in epitaxial WS2-graphene heterostructures, a 0 degree twist gives efficient charge separation while at 30 degrees electron and hole transfer proceed at similar rates, which cancels the separation.

The second cluster is photon and spectrum management. A proposed luminescent angle restrictor places a vertically aligned nanorod overlayer on a flat-plate absorber, near-transparent to near-normal sunlight, and argues that in such nanophotonic architectures the conventional equilibrium absorptivity/emissivity assumption in detailed balance needs re-examination. Indoor photovoltaics, aimed at powering IoT devices, is analysed by detailed balance under commercial white LEDs from 2200 K to 6500 K correlated colour temperature and colour rendering index 70, 80 and 90, finding that high-CRI sources change the optimal band gap, contrary to the prior assumption that CRI is negligible. Further out, transverse thermophotovoltaics has been given a microscopic formalism in which a transverse current appears in a 2D metal sheet via nonreciprocal surface plasmon polaritons driven by near-field thermal radiation, a paradigm explicitly distinct from junction-based PV and previously lacking theory.

One result in this set cuts the other way. Yb3+-doped CsPb(Cl,Br)3 has been widely reported as a broadband quantum cutter with photoluminescence quantum yield above 100%, a candidate for improving the blue-green response of silicon cells; photon-correlation analysis shows no bunching, and instead anti-bunching under focused excitation, consistent with Auger quenching rather than quantum cutting. A reader should treat that as the calibration for how much of this frontier will survive independent measurement.

## Viability (2/5)

Judged on the emerging-absorber and photon-management frontier that these sources describe, the evidence is early. The bismuth oxide double perovskites are real, measured films with band edges located by ultraviolet photoelectron spectroscopy, but they carry mixed cation valences and deep-level defects. Trigonal selenium's defect tolerance is a computational claim, and its practical implication is negative in the near term: the calculations remove the assumed explanation for observed efficiency limits without identifying the real one. Transverse thermophotovoltaics exists as a formalism, not a device, and the luminescent angle restrictor is a proposed architecture analysed theoretically.

The reproducibility signal is the most useful datum. Many groups reproduced above-100% quantum yields in Yb3+:CsPbCl3, yet photon-correlation analysis shows the photon statistics are inconsistent with quantum cutting. That is a direct warning that quantum-yield-style figures of merit in this field can survive replication and still be misattributed. Note that these sources say nothing about the viability of PV as a deployed generation technology; the score here refers only to the research routes described.

**TLDR: The frontier sampled here is first-principles calculation, thin-film characterisation and theory, with no device efficiencies reported and one headline enhancement mechanism contradicted.**

## Drivers (3/5)

On the demand side, three pulls are stated explicitly. Lead poisoning and ambient instability in halide perovskites are given as the motivation for alternative absorbers. Wide-gap absorbers are wanted for tandem and indoor applications, which is why trigonal selenium is back in play. Indoor photovoltaics is framed as a response to growing IoT demand for sustainable indoor power, with the design constraint that cells must be matched to specific artificial light sources.

On the supply side the sources show only research capacity, not manufacturing. Public funding is present but small: $600,000 for time-domain atomistic simulation of ultrafast dynamics relevant to photovoltaics and photocatalysis and $393,875 for a cryogen-free sub-Kelvin variable-temperature characterisation system. A separate driver is computational: predictor-guided gradient optimisation for crystal design reportedly outperformed generative and Bayesian baselines on perovskite band gap, formation energy and tolerance factor while using predictors trained on roughly one tenth of the data, which lowers the cost of searching absorber space. There is no cost, capacity or deployment data in the source set, so this score reflects research-level drivers only.

**TLDR: Clear technical drivers (lead-free requirement, tandem top cells, IoT indoor power) and modest public funding for the enabling theory; no market data in the sources.**

## Novelty (3/5)

The strongest novelty claims are in method rather than performance. The parameter-free ab initio electron-phonon transport framework reproduces measured mobilities, temperature exponents and optical-conductivity fingerprints across five molecular crystals without assuming a transport mechanism, and overturns the prevailing microscopic picture for DNTT by tracing its transient localisation to correlated on-site disorder from acoustic phonons. The crystal-design method is better than named alternatives on a defined benchmark with about a tenth of the training data. Machine-learned polaron dynamics extends accessible simulation from picoseconds to several nanoseconds and finds small-polaron mobility at reduced rutile TiO2(110) suppressed by several orders of magnitude relative to bulk, a large and specific correction to how surface transport is modelled.

On physics, two entries challenge received assumptions rather than beating a benchmark: detailed balance's use of equilibrium absorptivity and emissivity is questioned for nanophotonic architectures, and colour rendering index is shown to matter for indoor cell band-gap choice where it was previously assumed negligible. What is missing throughout is a comparison against an incumbent cell: no source reports a device efficiency, so "better than what, by how much" cannot be answered at the device level.

**TLDR: Genuine methodological advances with quantified comparisons, but none of the sources demonstrate a device better than an incumbent.**

## Diffusion (unscored)

Nothing in this source set addresses production scale-up, module cost, supply chains, qualification, bankability or installed capacity. The only adoption-shaped constraints that can be inferred are technical: lead content and ambient instability as reasons to displace halide perovskites; the need for indoor cells to be matched to the specific colour temperature and colour rendering index of the lighting they will sit under, which fragments the product specification; and the difficulty of translating twist-angle-controlled charge separation in epitaxially grown 2D heterostructures into anything manufacturable at area.

An additional, indirect barrier is measurement credibility. If a widely replicated above-100% quantum yield can be attributed to the wrong mechanism, then buyers of these enhancement layers will demand more than photoluminescence data before designing them into a product. That is a real friction, but it is not enough to score the dimension.

**TLDR: The sources contain no manufacturing, cost or adoption evidence, so no score is defensible.**

## Impact (unscored)

The sources are silent on magnitude. There are no efficiency figures for any fabricated cell, no cost per watt, no capacity or generation numbers, and no market sizing. The nearest thing to a stated application value is qualitative: indoor photovoltaics as a renewable power source for a growing installed base of IoT devices, and Yb3+-doped perovskite layers as a way to improve the blue-green spectral response of silicon cells, a route these results now put in doubt.

Two of the routes described are large in principle if they work: a lead-free absorber with halide-perovskite-like optoelectronics would remove a regulatory and stability obstacle from an entire class of cells, and a wide-gap, defect-tolerant tandem top cell raises the ceiling above single-junction silicon. But "in principle" with no quantification is not an impact assessment, and the honest output is null.

**TLDR: No source quantifies efficiency gain, cost reduction or energy delivered, so the value if it works cannot be assessed here.**

## Timing Later (5-10yr)

The maturity distribution in these sources sets the band. Transverse thermophotovoltaics has just acquired its first microscopic theory and no device; the bismuth oxide double perovskites are films with deep-level defects and mixed valences that still need defect engineering before cell performance follows; the selenium result identifies what is not the loss mechanism, leaving the actual limiter to be found. Twist-angle control of charge separation is a laboratory finding on epitaxial heterostructures. Routes at that stage do not reach commercial relevance inside five years.

The exception is spectrum-matched indoor photovoltaics, described as currently in development, where the detailed-balance result on colour temperature and colour rendering index is actionable design guidance today for anyone choosing an absorber band gap for LED-lit environments. Note that the source set gives no timelines or roadmaps, so this banding is inferred from research stage rather than from any stated schedule.

**TLDR: The absorber and non-junction routes here are at DFT, thin-film and formalism stage; only the indoor-PV design guidance is usable now.**

## Overrated or underrated? Too early to say

These sources describe the upstream research frontier of photovoltaics, not photovoltaics as a deployed generation technology, and they do not contain the cost, efficiency or deployment evidence that would let anyone rate the field as a whole. Within the frontier they do describe, the substance is real but pre-device: two credible advances in predictive method, one useful reframing of loss attribution in a candidate tandem absorber, one measured but defect-laden lead-free absorber, and one prominent enhancement mechanism that appears to have been misidentified.

The position I will take is narrower than a rating: the most valuable output from this cluster is not a new material but better loss accounting. Two independent results say the community has been attributing performance to the wrong microscopic cause, in selenium cells and in Yb-doped perovskite downconverters. Programmes that budget for photon-correlation and defect-level verification before scaling a claimed enhancement layer will save more money over the next three years than programmes chasing the next candidate composition.

## Prediction

By July 2028, the above-100% quantum-yield "quantum cutting" interpretation of Yb3+-doped CsPb(Cl,Br)3 as a spectral converter for silicon cells will have been revised in the peer-reviewed literature towards an Auger-quenching account rather than reaffirmed, following the photon-correlation evidence in.

## Evidence base

- 6 May 2026: solution-deposited 350-450 nm Bi2FeCrO6 and Bi2MnCrO6 films show monoclinic P21/c double-perovskite structure, visible absorption of 10^4-10^5 cm^-1 and carrier density 10^17-10^20 cm^-3, but with mixed cation valences and deep-level defects 
- 16 June 2026: first-principles calculations across a large point-defect set find trigonal selenium intrinsically defect tolerant, with non-radiative capture suppressed by energy releases of at least 0.5 EG per recombination event, so bulk SRH recombination cannot explain observed device losses 
- 1 July 2026: photon-correlation analysis of Yb3+-doped CsPbCl3 nanocrystals and bulk material shows anti-bunching rather than the bunching expected of a quantum cutter, consistent with Auger quenching and questioning earlier above-100% quantum-yield descriptions 
- 7 August 2026: detailed-balance calculations across white LEDs of 2200-6500 K and CRI 70, 80 and 90 show that high-CRI illumination changes the optimal indoor-PV band gap, contradicting the prior assumption that CRI has negligible impact 
- 6 May 2026: trARPES on epitaxial WS2-graphene heterostructures shows efficient charge separation at 0 degree twist, while at 30 degrees electron and hole transfer occur at similar rates 
- 28 May 2026: transverse thermophotovoltaics, previously proposed only conceptually as an alternative to junction-based photovoltaics, is given a microscopic formalism based on nonreciprocal surface plasmon polaritons in a 2D metal sheet 
- 17 June 2026: predictor-guided gradient optimisation for crystal design outperformed generative and Bayesian baselines on perovskite band gap, formation energy and tolerance factor under two hard constraints, using predictors trained on roughly one tenth of the data 

## Open questions

- If bulk point-defect Shockley-Read-Hall recombination cannot explain the efficiency limits of trigonal selenium cells, what does: interfaces, contacts, grain boundaries or transport?
- Can the deep-level defects and mixed cation valences in solution-deposited Bi2FeCrO6 and Bi2MnCrO6 films be suppressed enough to yield a working cell, and what open-circuit voltage does that give?
- Does the luminescent angle restrictor's predicted non-equilibrium emission profile survive an experimental test, and what measured efficiency gain does it produce over a flat-plate control?
- How many other reported photovoltaic enhancement mechanisms with high replication rates fail a photon-statistics or equivalent mechanism-level test, as Yb3+:CsPbCl3 did?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
