---
type: concept
slug: batteries-energy-storage
canonical_name: Batteries & Energy Storage
aliases: []
kind: technology
parent_concepts:
- energy-power
- storage
related_concepts: []
sources: []
frontier:
- How many cycles does the Li6.6Si0.6Sb0.4S5I cell with the LiNbO3-coated LiNi0.7Co0.1Mn0.2O2 cathode survive, and at what capacity retention and temperature range?
- Does the isolated-metal reactivation mechanism identified by phase-field simulation in Na3SbS4 2026 07 20 phase field simulation of dendrite evolution in all solid st also govern lithium sulfide and halide electrolytes, and can electrolyte microstructure engineering suppress it?
- If the grind-measure protocol advocated in 2026 07 22 battery material comparisons should refocus on diffusivity w were applied retrospectively, how many of the published diffusivity rankings that guide screening datasets would reverse?
- Do composition-only predictors such as CrabNet 2026 07 20 machine learning for electrode materials property prediction and phonon descriptors such as Li-PDOS 2026 07 24 lithium projected phonon spectral distributions as robust de identify any material that is subsequently synthesised and confirmed experimentally, rather than only reranking known entries?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 50
last_reorg_date: '2026-05-14'
scorecard:
  viability: 3
  drivers: null
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-19-ainews-memory-prices-up-500-in-12-months
  title: '[AINews] Memory prices up 500% in 12 months'
  date: '2026-08-19'
  kind: web
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-06-01-micron-technology-secures-61b-chips-act-funding-for-us-memor
  title: Micron Technology secures $6.1B CHIPS Act funding for US memory fabs - Dealroom
  date: '2026-06-01'
  kind: web
- slug: 2025-11-06-successful-funding-round-for-empa-eth-spin-off-57-million-to
  title: 'Successful funding round for Empa-ETH spin-off: $ 5.7 million to industrialize ultra-thin solid-state batteries - admin.ch'
  date: '2025-11-06'
  kind: web
neighbors: []
---
## Summary

"Batteries and energy storage" here covers the materials layer of electrochemical storage: the cathodes, anodes and electrolytes whose ion transport, phase behaviour and interfacial stability set what a cell can do. The supplied evidence is almost entirely 2026 preprint-stage research on next-generation chemistries rather than on cells or packs. Three threads dominate. First, all-solid-state batteries (ASSBs), where a solid electrolyte replaces the flammable liquid: a sulfide iodide argyrodite, Li6.6Si0.6Sb0.4S5I, was synthesised by ball milling and heat treatment and reached 9.9 mS cm^-1 at room temperature, then paired with a LiNbO3-coated LiNi0.7Co0.1Mn0.2O2 cathode in a full solid-state cell. Second, sodium-ion, pursued as a lithium-free alternative: hard carbon anodes engineered by carbon-layer reorientation and closed-pore formation to break the trade-off between initial Coulombic efficiency and reversible capacity, layered oxide cathodes whose Na-vacancy ordering couples to symmetry-changing structural transitions, and speculative two-dimensional anodes with Na migration barriers as low as 0.19 eV.

The third and arguably more consequential thread is the computational toolchain. Machine-learned interatomic potentials (MLIPs) now substitute for ab initio molecular dynamics at a fraction of the cost, extending accessible timescales from picoseconds to nanoseconds and allowing whole alloy series to be swept. Examples: MACE and NequIP potentials trained on melt-quench data to probe structure and ion transport in molten Li2CO3, with MACE showing better transferability; the universal PET-MAD potential applied to the Li3YCl6xBr6(1-x) halide electrolyte alloy to separate lattice-parameter effects from chemical ordering; and machine-learned polaron dynamics extended to reduced oxide surfaces, finding small-polaron mobility suppressed by several orders of magnitude at the rutile TiO2(110) surface relative to bulk. Alongside this sit composition-only property predictors benchmarked against each other, with CrabNet beating MODNet and a Magpie random forest on the Materials Project Battery Explorer dataset, phonon-spectrum descriptors of ionic conductivity, and literature mining that recovered 13,740 X-ray absorption spectra across 66 absorbing elements from battery papers.

The parameters that decide outcomes are narrow and physical. For solid electrolytes: room-temperature ionic conductivity, electrochemical window against both lithium metal and high-voltage cathodes, and resistance to dendrite penetration along grain boundaries. Phase-field simulation of Na ASSBs shows why the last is hard: stripping is intrinsically asymmetric to plating because of grain-boundary geometry, leaving isolated metal that is kinetically stabilised at grain-boundary junctions and reactivated on the next plating step, so penetration accelerates cycle over cycle. For electrodes: ionic diffusivity, which depends on correctly measuring the active-material length scale. A review of 303 recent open-access battery papers found 49% used diffusivity values to support structure-property claims, but of those only 15% clearly stated that particle length scale was measured after grinding or that no grinding was used. That single statistic conditions how much of the rest of the literature can be trusted.

One outlier deserves flagging because it shares the vocabulary but not the field: "quantum batteries" are nanoscale devices exploiting collective quantum effects for a charging advantage, proposed here as a dual-use mode of superconducting circuits that can switch between energy storage and quantum sensing. This is quantum information research, not grid or vehicle storage, and should not be read as evidence about batteries in the commercial sense.

## Viability (3/5)

Against that, the sources describe the persistent blockers in unusually mechanistic detail rather than dismissing them. Dendrite penetration in solid electrolytes is not merely a rate problem but a ratcheting one, driven by residual isolated metal trapped at grain-boundary junctions between cycles. Sulfide electrolytes are described as constrained in practice by space-charge layers, slow interfacial transport and dendrite susceptibility. And the diffusivity audit implies that a large share of published transport comparisons rest on length scales measured in the wrong order. Nothing in the supplied material reports cycle counts, cell-level energy density or manufacturing yield, so viability beyond coin-cell scale cannot be judged from here.

**TLDR: Real full-cell and simulation results exist, but the headline failure modes remain unsolved and the measurement base is shaky.**

## Drivers (unscored)

No supplied source contains demand figures, price data, capacity additions, policy measures or capital flows. The nearest thing to a driver statement is technical framing inside abstracts: lithium halides are pursued partly because of "relatively low cost, high stability", sodium-ion work is motivated by the stated "rapid advancement" of the chemistry demanding better anodes, and solid-state lithium batteries are described as "increasingly recognized" for energy density and safety. These are researchers' motivations, not evidence about supply or demand.

One supply-side observation is supportable: the research input side is getting cheaper. Universal MLIPs, open benchmark datasets such as OBELiX and the Materials Project Battery Explorer, and mined experimental corpora of 13,740 XAS spectra lower the marginal cost of a candidate-material evaluation. That is a driver of research throughput, not of deployment, and I will not convert it into a score.

**TLDR: The sources are technical preprints with no market, cost or capacity data.**

## Novelty (3/5)

Where the sources compare against an alternative, the margins are stated. CrabNet consistently outperformed MODNet and a Magpie-feature random forest on electrode property prediction, validated with bootstrap resampling, leave-one-cluster-out and stratified 5-fold cross-validation, and held-out unseen experimental data. MACE showed better transferability and precision than NequIP for molten Li2CO3. Machine-learned polaron dynamics reached several nanoseconds where ab initio molecular dynamics is limited to picoseconds, a genuine change in accessible regime rather than a percentage gain. The Li-projected phonon density of states is proposed as a replacement for the common practice of compressing phonon information into a single scalar softness measure, with reported Spearman correlations between low-frequency Li spectral weight and conductivity on an untouched test set.

On materials, novelty is real but bounded. The Si-substituted argyrodite at 9.9 mS cm^-1 is a composition-tuning advance within an already "very actively studied" family. The BAs3 and BP3 monolayer anodes, with 0.19 eV and 0.26 eV Na migration barriers and metallic conductivity retained at maximum theoretical loading, are DFT-only candidates with no synthesis reported. The most methodologically novel item is the fault-tolerant quantum algorithm that reproduces open-system electrochemical observables, placing the LiFePO4 differential-capacity peak within the ±5 mV reproducibility of the experimental plateau using a single voltage anchor on an otherwise DFT-fixed Hamiltonian. That is an algorithmic result contingent on hardware that does not yet exist.

**TLDR: Clear, measured improvements over named baselines, but mostly incremental within existing methods rather than a change of kind.**

## Diffusion (2/5)

Read as the path from these results to usable cells, the barriers named are structural, not incidental. Grain-boundary microstructure in polycrystalline solid electrolytes drives asymmetric stripping and plating and the accumulation of isolated metal, meaning that cycling itself degrades the barrier to dendrite penetration; applied voltage, electrolyte microstructure and anode chemistry all modulate it. Sulfide electrolytes carry space-charge layers at the cathode interface, addressed here by a LiNbO3 coating. Sodium layered oxide cathodes undergo symmetry-changing phase transformations tied to Na-vacancy ordering at specific stoichiometries, which is precisely the kind of coupling that shortens cycle life at cell level.

There is also a diffusion barrier inside the research community itself. If only 15% of papers reporting diffusivity make the length-scale measurement procedure defensible, then screening pipelines trained or validated on that literature inherit the error, and industrial developers cannot rank candidates by published numbers. The counterweight is that the tooling layer diffuses easily: open datasets and universal potentials are cheap to adopt and require no new hardware,. On commercial adoption, manufacturing qualification or supply chains, the sources support no assessment.

**TLDR: Lab-to-cell barriers are identified in mechanistic detail; the sources say nothing about industrial uptake.**

## Impact (3/5)

The claimed payoffs are stated qualitatively: solid-state lithium batteries are pursued for "exceptional energy density and safety", with the safety argument resting on removal of the flammable liquid electrolyte, and the safety and energy-density case is echoed as the motivation for the dendrite modelling work. Sodium-ion work targets the ICE and reversible-capacity trade-off that currently limits hard carbon anodes. Reducible oxides are described as underpinning catalysis, photovoltaics and batteries simultaneously, so improvements to polaron-transport understanding spill across several energy sectors.

None of the sources gives a pack-level Wh/kg figure, a cost per kWh, a cycle-life target or an addressable market. The one place where impact can be sized in the sources' own terms is research productivity: a validated composition-only oracle for early-stage electrode screening plus a reproducible phonon descriptor of ionic conductivity trained on a few hundred materials compress the candidate-triage step. That is meaningful but second-order. A 3 reflects a large but unmeasured prize, not a demonstrated one.

**TLDR: The prize is credible and repeatedly asserted, but nowhere quantified in the supplied evidence.**

## Timing Soon (2-5yr)

Two clocks run at different speeds. The computational layer is effectively now: universal MLIPs are being applied to real alloy design spaces, benchmarked property predictors are proposed as early-stage screening oracles, and 13,740 mined experimental spectra are already published as an AI-ready resource. Expect these to become default practice within the next two years or so.

The materials clock is slower. The argyrodite result is a single new composition in a full cell with no cycling data given in the excerpt, and the dominant failure mechanism it must survive is described as cumulative across cycles. Candidate anodes such as BAs3 and BP3 exist only in DFT. The quantum-algorithm route to cathode voltage prediction is gated on fault-tolerant hardware and belongs to a later band entirely. On a 2-5 year view the visible change is better and faster candidate selection; the cells themselves arrive later, and the sources do not let one date that.

**TLDR: The machine-learned simulation and data-mining layer is already usable; the solid-state and sodium-ion materials it is screening are still at coin-cell stage.**

## Overrated or underrated? Fairly rated

Nothing in this evidence base justifies either dismissal or excitement about a breakthrough. The specific claims are modest and mostly well-controlled: a solid electrolyte at 9.9 mS cm^-1 integrated into a cell, a predictor validated under two cross-validation schemes against a control baseline, simulations that explain rather than merely reproduce a failure mode. This is a field grinding forward on known blockers, which is what a mature research programme looks like.

The sharper point is that individual reported material advances should be discounted more heavily than the field's own citation practice implies. If half of recent battery-materials papers lean on diffusivity to support structure-property claims and only a small fraction of those describe a defensible length-scale procedure, then the correct posture towards any single "improved transport" result is scepticism until the measurement protocol is stated. Within this concept, the underrated element is the boring infrastructure: reproducible descriptors, mined experimental corpora and measurement standards, all of which improve the signal-to-noise of everything downstream. The overrated element is the transfer of vocabulary: "quantum batteries" as dual-use superconducting hardware shares no engineering path with electrochemical storage and should not be scored alongside it.

## Prediction

By July 2028, published sulfide and halide lithium solid electrolytes will report room-temperature ionic conductivities above the 9.9 mS cm^-1 demonstrated in July 2026, while the dominant reported cause of full-cell failure in all-solid-state cells will still be grain-boundary dendrite penetration rather than insufficient bulk conductivity.

## Evidence base

- 15 June 2026: machine-learned polaron dynamics extended to oxygen-deficient rutile TiO2(110) reached several nanoseconds, versus the picosecond limit of ab initio molecular dynamics, and found small-polaron mobility suppressed by several orders of magnitude at the surface relative to bulk 
- 16 June 2026: a fault-tolerant quantum algorithm using a chain-mapped Caldeira-Leggett embedding placed the LiFePO4 differential-capacity peak within the ±5 mV reproducibility of the experimental plateau using a single voltage anchor on a DFT-fixed Hamiltonian 
- 20 July 2026: phase-field simulation of Na all-solid-state batteries with polycrystalline Na3SbS4 showed stripping is intrinsically asymmetric to plating, leaving isolated Na kinetically stabilised at grain-boundary junctions that is reactivated on subsequent plating and amplifies dendrite penetration 
- 22 July 2026: a procedural review of 303 recent open-access battery-materials papers found 49% used diffusivity values to support structure-property transport claims, and only 15% of those clearly stated that length scale was measured after grinding or that grinding was not used 
- 23 July 2026: Li6.6Si0.6Sb0.4S5I argyrodite synthesised by ball milling and heat treatment achieved 9.9 mS cm^-1 room-temperature ionic conductivity and was integrated with a LiNbO3-coated LiNi0.7Co0.1Mn0.2O2 cathode into an all-solid-state cell 
- 28 July 2026: multimodal mining of the battery literature produced an open dataset of 13,740 X-ray absorption spectra spanning 66 absorbing elements, with expert validation of extracted spectra and metadata 

## Open questions

- How many cycles does the Li6.6Si0.6Sb0.4S5I cell with the LiNbO3-coated LiNi0.7Co0.1Mn0.2O2 cathode survive, and at what capacity retention and temperature range?
- Does the isolated-metal reactivation mechanism identified by phase-field simulation in Na3SbS4 also govern lithium sulfide and halide electrolytes, and can electrolyte microstructure engineering suppress it?
- If the grind-measure protocol advocated in were applied retrospectively, how many of the published diffusivity rankings that guide screening datasets would reverse?
- Do composition-only predictors such as CrabNet and phonon descriptors such as Li-PDOS identify any material that is subsequently synthesised and confirmed experimentally, rather than only reranking known entries?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
