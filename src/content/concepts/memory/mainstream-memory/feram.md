---
type: concept
slug: feram
canonical_name: FeRAM (Ferroelectric)
aliases: []
kind: technology
parent_concepts:
- memory
- mainstream-memory
related_concepts: []
sources:
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
frontier:
- Can HZO device-to-device variability be reduced by process control, or only characterised and compensated statistically as in the PCA/K-means approach 2026 05 04 an unsupervised machine learning based framework for wafer s?
- Does the sharp laser-energy threshold for HZO crystallisation 2026 05 05 tracking visible pulsed laser annealing of hf05zr05o2 hetero leave a process window wide enough for a production stack across thickness and electrode variation?
- Since the polar orthorhombic phase fraction depends on oxygen vacancy concentration 2026 05 05 role of oxygen vacancies in stabilizing the orthorhombic pha, what does that imply for retention and endurance under cycling, which none of the sources report?
- Is any non-destructive readout scheme experimentally viable, or does ferroelectric memory remain locked into destructive read plus write-back 2026 05 15 machine learning identified two dimensional van der waals mu?
- Can HfO2 FeRAM / FeCAP endurance and retention reach DRAM-replacement bars (FMC DRAM+)?
- Does FeCAP-based compute become a credible memcapacitor competitor?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 149
last_reorg_date: '2026-05-14'
descendants:
- fefet
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: null
  timing_band: Unclear
  verdict: Too early to say
scorecard_status: draft
sources_7d: 4
sources_30d: 16
recent_mentions:
- slug: 2025-26-lapedus-next-gen-ferroelectric-memory
  title: Next-Gen Ferroelectric Memory Still A Work In Progress
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
- slug: 2024-yole-emerging-memories-2024
  title: Yole Group — Emerging Non-Volatile Memories 2024
  date: '2024-10-15'
  kind: web
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
neighbors: []
---
**FeRAM stores a bit as the direction of a switchable electric polarisation in a ferroelectric film; the hafnium-zirconium oxide (HZO) variant is back-end-of-line compatible with CMOS, but wafer-scale device-to-device variability arising from its sensitive crystallisation kinetics is currently named as the binding barrier to high-volume manufacturing.**

## Summary

Ferroelectric RAM stores information in the remanent electric polarisation of a thin ferroelectric layer: apply a field one way and the polarisation points one way, reverse it and the bit flips, and the state persists with no power. The polarisation can be sensed either through the charge released when it switches (which destroys the stored state and requires a write-back) or indirectly through its effect on a transistor channel, as in a ferroelectric FET. The absence of a good non-destructive readout scheme is still treated as an open problem in the current literature on ferroelectric memory concepts.

The reason ferroelectric memory is being taken seriously as a mainstream embedded technology rather than a niche is hafnium-zirconium oxide, Hf0.5Zr0.5O2 (HZO). It is described as a strong candidate for embedded non-volatile memory because it is compatible with CMOS back-end-of-line processing, scalable, and high performance. The catch is physical: the ferroelectric response comes from a metastable orthorhombic phase whose formation depends on crystallisation conditions, film thickness, electrode stack and defect chemistry. Oxygen vacancy concentration, set by annealing atmosphere, controls the fraction of orthorhombic phase in small (~7 nm) HZO nanoparticles, with chemical strain from the vacancies stabilising the polar phase. Crystallising the film within a BEOL thermal budget is being addressed with laser annealing: in a Si3N4/TiN/HZO stack irradiated with visible nanosecond pulses, the ferroelectric phase fraction shows sharp threshold behaviour in pulse energy density, with the threshold depending on film thickness. The consequence of that sensitivity is unpredictability across a wafer, which is explicitly called a formidable barrier to high-volume manufacturing; recent work applies PCA and K-means clustering to intra-die device-to-device data to predict the behaviour of unseen dies.

A second, much earlier research track uses van der Waals ferroelectrics rather than oxides. A switchable SnSe/alpha-In2Se3 p-n heterojunction has been used to build a ferroelectric junction field-effect transistor memory with 0.1 pA reverse leakage, a diode ideality factor of 1.95, 900 meV ferroelectric barrier modulation and a 1.8 V memory window. Machine-learning screening of the 2D ABC2X6 family has proposed AuCrP2S6 as a multiferroic four-state memory cell with 7.46 pC/m out-of-plane polarisation, a ~130 meV/f.u. switching barrier and a bulk-photovoltaic non-destructive readout channel. Sliding ferroelectricity in CVD-grown 3R-WSe2 bilayers is being probed with graphene-channel FE-FETs, where intrinsic disorder and multi-domain kinetics dominate switching behaviour.

The parameters that decide the technology, on the evidence available, are: the reproducible fraction of ferroelectric phase per device and its spread across a wafer; the thermal budget needed to get it; memory window and leakage; and whether readout can be made non-destructive. A fourth, less comfortable parameter is measurement hygiene. Series capacitance and other extra circuit components can produce apparent ferroelectric D-E hysteresis loops even under the double-wave method, and suspicious loops have been identified in published papers using that method; piezoelectric strain loops are argued to be the more reliable proof of ferroelectricity. A related caution comes from compressively strained SrTiO3 capacitors, which show butterfly capacitance-voltage hysteresis and domain-like electromechanical response yet are judged inconsistent with a stable ferroelectric state, the polarity instead attributed to inhomogeneous internal fields.

## Viability (3/5)

The physics is not in doubt for the leading material system. HZO is treated across the sources as an established BEOL-compatible ferroelectric, and the work being published is process engineering rather than existence proof: controlling the metastable orthorhombic phase through oxygen vacancy concentration, and crystallising it with visible nanosecond laser pulses in a CMOS-like Si3N4/TiN/HZO stack, where the ferroelectric phase fraction shows a sharp energy threshold. That is the profile of a technology past feasibility and into yield.

What holds the score at 3 is that the yield problem is stated bluntly and not yet solved: sensitive crystallisation kinetics produce significant device-to-device non-uniformity and unpredictability of performance at wafer scale, described as a formidable barrier to high-volume manufacturing, with unsupervised learning offered as a predictive workaround rather than a fix. The sources contain no endurance, retention, cycling or array-level data, so the standard memory qualification questions cannot be assessed here at all. The field also carries a demonstrated risk of false positives in ferroelectricity claims, both from measurement artefacts and from misattributed polar responses in oxide capacitors, which should discipline how any single device demonstration is read.

**TLDR: Ferroelectric switching in CMOS-compatible HZO is real and integrable, but per-device reproducibility across a wafer is unresolved.**

## Drivers (3/5)

On supply, the pipeline is visibly moving: BEOL laser annealing to fit the thermal budget, defect-chemistry control of the polar phase, statistical wafer-scale variability frameworks, and better design tooling in the form of a GPU-accelerated Ginzburg-Landau solver computing the full polarisation vector field with proper electrostatics, which the authors argue existing CPU-based, reduced-dimensional solvers cannot do. Screening infrastructure is also improving: a unified definition of ferroelectricity based on switchable polarisation differences between energetically equivalent states enables high-throughput identification of candidates among already-synthesised materials, including Ba3I6 and Cs2PdC2 with low switching barriers.

On demand, the sources are thin. The only statement is that with skyrocketing AI workload, demand for non-volatile and computational memories is growing exponentially, an assertion in a paper introduction with no market figures, no customer, and no comparison against competing embedded NVM. There is no pricing, capacity, foundry or product evidence anywhere in this source set. Treat the 3 as resting almost entirely on the supply half.

**TLDR: Supply-side process work is active and specific; the demand case rests on a single unquantified assertion about AI memory demand.**

## Novelty (3/5)

The meaningful comparison the sources do support is internal to ferroelectrics. HZO is preferred over classical perovskite ferroelectrics on BEOL compatibility, scalability and performance, and the contrast is visible in the perovskite papers themselves: BaTiO3 charged domain wall conductivity collapses by several orders of magnitude when the crystal passes below roughly 5 degrees Celsius into the orthorhombic phase, and room-temperature out-of-plane ferroelectricity in strained SrTiO3 remains unrealised 25 years after prediction. Against that background, an oxide that works at room temperature in a TiN stack is a large practical step.

The device-level novelty claims are specific but early. The vdW ferroelectric junction FET memory reports a fundamentally different memory mechanism with 900 meV barrier modulation, 1.8 V memory window and 0.1 pA reverse leakage; the 2D multiferroic route proposes four states per cell plus a photocurrent-based non-destructive read, which would address two of ferroelectric memory's structural weaknesses at once, but the candidates are computational and the paper itself notes the scarcity of synthesisable ones. Nothing in the sources benchmarks FeRAM against flash, DRAM or MRAM on density, energy or endurance, so the headline question of how much better it is than the incumbent cannot be scored from this evidence.

**TLDR: Clear advantage over conventional ferroelectric oxides on CMOS integration; no quantified comparison against the incumbent memories it would displace.**

## Diffusion (2/5)

The 2D and vdW routes are further from diffusion again: sliding ferroelectricity in CVD-grown 3R-WSe2 is dominated by intrinsic structural defects and domain structure whose role is described as poorly understood, and the vdW junction memory relies on hand-assembled band-aligned heterojunctions. The sources contain no fab, foundry, product or qualification information of any kind, so this score reflects only the difficulty of the barriers on display, not evidence about how fast anyone is clearing them.

**TLDR: The named barrier is manufacturing uniformity, and the sources show it being characterised rather than overcome.**

## Impact (unscored)

Every source here is a materials-physics or device-physics paper. None quantifies what a working FeRAM would be worth: there is no density, cost-per-bit, energy-per-operation, endurance or system-level figure, and no comparison against the memories it would displace. The nearest thing to an impact claim is the assertion that AI workloads are driving exponentially growing demand for non-volatile and computational memories, which is directional at best and appears without supporting data.

Two qualitative pointers exist and are worth recording without scoring. First, if four-state multiferroic cells with photocurrent readout were realisable, they would combine higher per-cell state count with non-destructive read, both of which bear directly on where ferroelectric memory currently loses. Second, ferroelectrics are being used to control other degrees of freedom, for example room-temperature electric-field control of the anomalous Hall effect in Py/BaTiO3/La0.7Sr0.3MnO3 heterostructures, which suggests adjacent value beyond straight bit storage. Neither can be converted into a defensible 1-5 judgement from this evidence.

**TLDR: The sources do not support an assessment: no quantified benefit, no comparison against incumbent memories, no application sizing.**

## Timing Unclear

The nature of the HZO problems being published points to something close to industrialisation: intra-die and die-to-die statistics, wafer-scale performance prediction, BEOL-compatible anneal windows,. Nobody works on wafer-level variability for a material that is a decade from a fab. That argues for a near-term band.

Against that, the source set contains no product, foundry or qualification evidence at all, and the device architectures that would make ferroelectric memory competitive on density and non-destructive readout are at the screening and first-device stage: AuCrP2S6 is a computational candidate, and the SnSe/In2Se3 junction memory is a single exfoliated-stack demonstration. Those are five-to-ten-year timelines at best. With no commercial signal in the evidence, an honest band is Unclear: the HZO capacitor track could matter within a few years, the architectural track much later, and the sources do not let us pick.

**TLDR: HZO work sits at the pre-production yield stage while the concepts that would fix FeRAM's read and density limits are still computational.**

## Overrated or underrated? Too early to say

The interesting thing about this evidence base is where the difficulty has migrated. Nobody in these papers is arguing about whether HZO is ferroelectric or whether it can be put in a CMOS back end; they are arguing about how uniformly it can be made, and that is a manufacturing question, not a physics one,. That is a genuinely more advanced position than most emerging-memory candidates occupy. But the sources supply no endurance, retention, array or commercial data, so any verdict on FeRAM as mainstream memory would be constructed rather than earned.

Two cautions should be carried forward. First, the sensitivity of the polar phase to oxygen vacancy concentration and anneal conditions means variability is not incidental noise but a direct consequence of how the useful phase is stabilised, which makes it harder to engineer away than a process defect. Second, this is a field with a demonstrated artefact problem: apparent hysteresis loops can be produced by series capacitance and have been found in published double-wave-method results, and a polar-looking oxide capacitor with butterfly C-V and domain-like piezoresponse can still turn out not to be ferroelectric. Discount single-device claims accordingly, particularly from the 2D end.

## Prediction

No experimentally fabricated single-device demonstration of a four-state 2D van der Waals multiferroic memory cell with non-destructive photocurrent readout, of the AuCrP2S6 type proposed in, will be published before 31 December 2028.

## Evidence base

- 4 May 2026: HZO is described as a strong embedded non-volatile memory candidate on BEOL compatibility, scalability and performance, but its sensitive crystallisation kinetics cause significant device-to-device non-uniformity, with process-induced variability called a formidable barrier to high-volume manufacturing; PCA and K-means clustering are used to predict performance of unseen dies.
- 5 May 2026: in situ TEM of visible nanosecond laser annealing of a Si3N4/TiN/HZO stack shows sharp threshold behaviour in pulse energy density for crystallisation, with the threshold linked to HZO film thickness, supporting a BEOL fabrication route.
- 5 May 2026: in ~7 nm Hf0.5Zr0.5O2 nanoparticles the fraction of orthorhombic phase depends on oxygen vacancy concentration set by annealing atmosphere, with chemical strain from vacancies stabilising the ferroelectric o-III phase.
- 8 May 2026: a SnSe/alpha-In2Se3 ferroelectric junction FET memory reports 0.1 pA reverse leakage, ideality factor 1.95, 900 meV ferroelectric barrier modulation and a 1.8 V memory window with ultrafast switching.
- 15 May 2026: machine-learning screening of the 2D ABC2X6 family identifies AuCrP2S6 with 7.46 pC/m out-of-plane polarisation and a ~130 meV/f.u. switching barrier, proposing bulk-photovoltaic non-destructive readout for four-state memory; the paper cites scarcity of synthesisable candidates and lack of non-destructive readout as the field's blockers.
- 14 May 2026: series circuit components can produce apparent ferroelectric D-E hysteresis loops even under the double-wave method, and suspicious loops are identified in existing published work; strain-field loops are argued to be the more reliable evidence of ferroelectricity.

## Open questions

- Can HZO device-to-device variability be reduced by process control, or only characterised and compensated statistically as in the PCA/K-means approach?
- Does the sharp laser-energy threshold for HZO crystallisation leave a process window wide enough for a production stack across thickness and electrode variation?
- Since the polar orthorhombic phase fraction depends on oxygen vacancy concentration, what does that imply for retention and endurance under cycling, which none of the sources report?
- Is any non-destructive readout scheme experimentally viable, or does ferroelectric memory remain locked into destructive read plus write-back?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
