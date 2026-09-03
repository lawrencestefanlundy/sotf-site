---
type: concept
slug: pvd-sputtering
canonical_name: PVD / Sputtering
aliases:
- PVD
- physical vapor deposition
- sputtering
- magnetron sputtering
- HiPIMS
- ion beam sputtering
- IBS
- IBD
- ion beam deposition
kind: technology
parent_concepts:
- manufacturing
- equipment-processes
- deposition
related_concepts:
- chemical-vapor-deposition
- ald-atomic-layer-deposition
- ru-w-co-metallisation
- low-k-dielectrics
- thin-films-coatings
- semiconductor-equipment
sources: []
frontier:
- Can sputtered multilayers be made periodic below a 4 nm period, or is interfacial intermixing a hard floor that pushes short-period applications to MBE 2026 05 05 structural evolution of ticu multilayers as a function of pe?
- Do sputtered V or NbN resonators reach internal quality factors competitive with established Nb and Ta processes, and is the loss surface-dominated in a way that deposition changes can fix 2026 07 02 vanadium superconducting microwave resonators on silicon waf?
- Does the cold-sintering route to sputtering targets scale beyond 2-inch diameter and generalise beyond calcium hydroxide to other thermally unstable target chemistries 2026 06 02 hydrothermally assisted sintering of calcium hydroxide sputt?
- Does the interface-sharpness deficit of sputtering versus MBE actually degrade device performance in interface-sensitive applications such as CISS spin valves, or is it only visible in structural characterisation 2026 06 30 microscopic and macroscopic characterization mbe grown versu?
- Can any ion-beam deposition reach HVM throughput? Every prior IBD-to-HVM attempt died on rate; the live test is Halltech's 12-inch demonstrator and the Sept/Oct 2026 Intel coupon path.
- 'Cu-to-Ru/Mo at <=17nm lines (2027-29): how does the seed/barrier/fill split fall between PVD seed, ALD/CVD fill, and IBD-quality films? IBD has published superiority for Ru (IEEE IITC 2022).'
- Does AMAT's PVD dominance ('free ride', per Lam's own read) ever get contested, or does the segment stay a one-vendor toll?
- 'HiPIMS: does near-100% ionisation move beyond hard coatings and specialty niches into mainstream semi metallisation?'
- 'Powder/bulk-feedstock PVD (LAYRR): does coating the feedstock rather than the wafer open a materials-supply business the tool oligopoly never fights for?'
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 55
last_reorg_date: '2026-05-13'
scorecard:
  viability: 5
  drivers: 4
  novelty: 2
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
sources_7d: 1
sources_30d: 12
recent_mentions: []
neighbors:
- slug: chemical-vapor-deposition
  name: CVD (Chemical Vapor Deposition)
  path: /manufacturing/equipment-processes/chemical-vapor-deposition/
  macro: manufacturing
- slug: ald-atomic-layer-deposition
  name: ALD (Atomic Layer Deposition)
  path: /manufacturing/equipment-processes/ald-atomic-layer-deposition/
  macro: manufacturing
- slug: ru-w-co-metallisation
  name: Ru / W / Co Metallisation
  path: /manufacturing/equipment-processes/ru-w-co-metallisation/
  macro: manufacturing
- slug: low-k-dielectrics
  name: Low-K Dielectrics
  path: /materials/functional-layers/low-k-dielectrics/
  macro: materials
- slug: thin-films-coatings
  name: Thin Films & Coatings
  path: /materials/advanced-materials/thin-films-coatings/
  macro: materials
- slug: semiconductor-equipment
  name: Semiconductor Equipment
  path: /manufacturing/equipment-processes/semiconductor-equipment/
  macro: manufacturing
---
**Sputtering is the vacuum deposition workhorse in which ion bombardment knocks atoms off a solid target onto a substrate, and the 2026 literature shows it moving from a commodity coating step into epitaxy-grade territory for superconductors, GaN power devices and photovoltaic contact stacks.**

## Summary

The parameters that decide outcomes are few but unforgiving. Reactive gas partial pressure sets the phase: in Cu-O films, increasing oxygen partial pressure drives Cu2O to Cu2O/Cu4O3 to CuO, and boron doping widens the window in which the useful mixed-valence phases survive. Buffer layers set the crystallography: delta-NbN grows epitaxially on TiN-buffered sapphire at room temperature with picometre-scale surface roughness, described as the lowest reported, and vanadium films on an Nb buffer show more uniform lattice orientation and smaller grains than V grown directly on silicon. Target quality and availability set the material palette: dense Ca(OH)2 targets, otherwise hard to make because heating dehydrates the material, have been produced at up to 98 per cent theoretical density by cold sintering at 100 to 300 degrees C and 400 MPa, and scaled to 2-inch diameter for CaO film deposition. Geometry matters too, because deposition is line-of-sight: on microwire scaffolds inclined at 0, 30 and 45 degrees, CoFe/IrMn film thickness falls systematically with inclination, and the exchange bias field tracks it.

Sputtering competes with molecular beam epitaxy, MOCVD, pulsed laser deposition and thermal evaporation, and the comparisons in the sources are mixed. For Au/Co/Au stacks, MBE gives sharper interfaces and a narrower Au(111) rocking curve than magnetron sputtering. VO2 films grown by pulsed laser deposition and dc sputtering differ in grain size and hence in metal-insulator transition behaviour. Thermal laser evaporation, a newer PVD variant using a 1 kW 1070 nm fibre laser focused onto a target rod, claims the ability to evaporate essentially any solid element including refractory metals such as W. Two other uses of the same physics appear in the sources and should not be confused with deposition: argon-ion sputtering as a depth-profiling tool, used to reconstruct XPS spectra with 0.23 nm layer resolution, and sputtering as unwanted erosion of fusion plasma-facing components, where the design goal is to enrich the surface with low-Z species such as Li or Al to obtain benign sputtering characteristics.

## Viability (5/5)

The sources contain no failed-deposition story. Sputtered films are reported as functioning superconducting coplanar waveguide resonators, as epitaxial single-crystalline delta-NbN with picometre roughness grown at room temperature, as phase-pure layered FeWN2 across a broad composition range, and as templates for MOCVD overgrowth of GaN on Si(111) with ohmic, low-resistance vertical conduction. This is a process with a century of industrial history behind it and the current literature treats it as infrastructure rather than as a hypothesis.

The residual viability questions are at the extremes of the parameter space, not at the level of the technique. Ti/Cu multilayers lose periodic contrast at a 4 nm period, attributed to extended interfacial regions and partial Cu-Ti intermixing, and only become regular at larger periods. Reactive sputtering has a documented bias towards metastable rocksalt-derived nitride structures, which had to be corrected here with post-deposition NH3 annealing. Those are bounded, well-characterised limits rather than open feasibility risks.

**TLDR: Not in question: sputtering produces device-grade films across superconductors, magnetics, oxides and nitrides today.**

## Drivers (4/5)

Demand appears in the sources as explicit application motivation rather than market data. Silver supply chain concerns are driving a move to copper solar cell metallisation, which in turn requires transparent conductive Cu diffusion barriers, addressed with amorphous In-Zn-O layers. Superconducting quantum circuits need low-loss films and are pulling material exploration towards sputtered V, Nb and Ta stacks and towards NbN for single-photon detectors, hot-electron bolometers and qubit architectures. Vertical GaN-on-silicon for cost-effective power electronics and high-resolution micro-LEDs is a third pull, where the stated bottleneck is buffer layer resistance rather than the deposition step itself. OLED multilayer structures are cited as an existing use of vapour-deposited organic glasses.

On the supply side, the binding constraint visible in the sources is the target. Materials that decompose or dehydrate on heating cannot easily be made into dense sputtering targets, which is why a cold-sintering route to 98 per cent dense Ca(OH)2 targets at 100 to 300 degrees C, scaled to 2 inches, is presented as a route to a new film chemistry. No source gives equipment cost, throughput or market size, so this score rests on the breadth and specificity of the application pull rather than on commercial evidence.

**TLDR: Strong demand pull from PV metallisation, superconducting quantum hardware and GaN power electronics; supply side constrained mainly by target materials.**

## Novelty (2/5)

As a class, sputtering is not new and the sources do not claim it is. What is new is narrow and incremental: HiTUS for polycrystalline Mn3+xSn1-x heterostructures, boron co-doping to widen the reactive-sputtering phase window for mixed-valence Cu-O, cold-sintered targets for hydroxide chemistries, and a sputtered sub-nanometre (0.5 nm) silicide template demonstrated across 25 different metallic species as a GaN-on-Si buffer.

Against the alternatives the picture is genuinely mixed, which is what keeps this score low. MBE-grown Au/Co/Au shows sharper interfaces and a narrower Au(111) rocking-curve width than the sputtered equivalent. Thermal laser evaporation offers elemental coverage that includes the most refractory metals. Where sputtering clearly wins it wins on cost and temperature: room-temperature epitaxial delta-NbN with the lowest reported roughness, framed explicitly as a cost-effective alternative to harder synthesis routes, and a scalable low-cost path to device-grade vertical GaN. That is an economics advantage at comparable quality in specific systems, not a step change in capability.

**TLDR: The technique is commodity; the novelty is in specific variants and process windows, and it still loses to MBE on interface sharpness.**

## Diffusion (4/5)

The real barriers are technical and specific. Line-of-sight deposition means thickness, and therefore magnetic behaviour, varies systematically with substrate inclination on non-planar scaffolds, which limits use on 3D architectures without compensating strategies. Interface abruptness degrades below roughly 10 nm multilayer periods and collapses at 4 nm. Target availability gates which chemistries can be attempted at all. The score is 4 rather than 5 because the sources document laboratory diffusion only; none report production line adoption, yields or throughput.

**TLDR: Already the default deposition tool across at least six unrelated research domains; remaining barriers are geometric and interfacial, not institutional.**

## Impact (4/5)

The value sits in what sputtering unlocks downstream. Replacing silver with copper in solar cell metallisation depends on a working transparent conductive diffusion barrier, and that barrier is a sputtered oxide. Vertical GaN-on-silicon, described as a transformative leap for cost-effective power electronics and high-resolution micro-LEDs, is bottlenecked by buffer resistance that a sputtered silicide template addresses. Chalcopyrite tandem bottom cells reaching 16 per cent at 1.0 eV with VOC above 550 mV use a sputtered oxide layer in the stack, and the study found no systematic dependence on oxygen flow during that sputtering step, which is a positive robustness result for manufacturing.

The cap on this score is attribution. Sputtering is a shared input rather than a differentiated product, so the value it creates is largely captured by the device makers rather than by the process. The sources provide no cost, yield or market figures, so 4 reflects breadth and criticality of use as demonstrated, not a quantified economic claim.

**TLDR: It is the enabling layer under several high-value transitions, though the sources measure device outcomes rather than economic value.**

## Timing Now (0-2yr)

Nothing here waits on a scientific breakthrough. Room-temperature epitaxial NbN, boron-widened Cu-O phase windows and cold-sintered targets scaled to 2 inches are all demonstrations on standard equipment that could be reproduced in any competent thin-film facility immediately.

The device-level consequences run on longer clocks set by their own industries. The sputtered GaN-on-Si template still requires MOCVD overgrowth and full device fabrication before its power electronics or micro-LED claims are tested, and the copper metallisation transition in PV depends on cell manufacturers, not on the barrier layer alone. Assess sputtering itself as Now; assess any given downstream claim on its own timeline.

**TLDR: The process is in use today; the open work is process-window refinement, and the specific 2026 results are near-term transferable.**

## Overrated or underrated? Underrated

The process is invisible because it is old, and that hides where the interesting movement is. Two results in the sampled window show sputtering delivering quality that would normally be assumed to require epitaxy or high-temperature growth: single-crystalline delta-NbN with picometre-scale roughness deposited at room temperature on a TiN-buffered sapphire substrate, and a 0.5 nm sputtered silicide interlayer that accommodates the GaN/Si lattice mismatch and supports device-grade vertical conduction, demonstrated across 25 metallic species. If that trend holds, the cost floor for several classes of device drops without any new equipment category being invented.

The qualification is that sputtering does not win everywhere and the sources say so. MBE still gives sharper interfaces and better crystalline order in Au/Co/Au, and sputtered multilayers degrade below a 10 nm period. The underrated element is therefore specific: the adjacent supply chain of target materials and reactive process windows, not the deposition chamber, is where capability is currently being added.

## Prediction

By 30 June 2028, at least one peer-reviewed report will demonstrate a working vertical GaN-on-Si device (power transistor or micro-LED) built on the sputtered sub-nanometre silicide/amorphous-interlayer template route described in May 2026.

## Evidence base

- 4 May 2026: a sputtering-based in-situ silicide template only 0.5 nm thick, demonstrated across 25 metallic species, produced GaN epitaxial films on Si(111) with low vertical resistance and ohmic behaviour, and served as a platform for MOCVD overgrowth.
- 18 June 2026: room-temperature sputtering produced single-crystalline delta-NbN on TiN-buffered c-sapphire with picometre-scale surface roughness, reported as the lowest to date.
- 5 May 2026: Ti/Cu multilayers sputtered with periods from 4 to 52.5 nm lost periodic contrast at 4 nm due to Cu-Ti intermixing, and only became regular at larger periods.
- 2 June 2026: cold sintering at 100 to 300 degrees C and 400 MPa produced Ca(OH)2 sputtering targets at up to 98 per cent theoretical density, scaled to 2-inch diameter, without thermal dehydration.
- 30 June 2026: comparing Au/Co/Au stacks, MBE growth gave sharper interfaces and a narrower Au(111) rocking-curve width than magnetron sputtering.
- 1 July 2026: a CuInSe2 bottom cell at 1.0 eV reached 16 per cent efficiency with VOC above 550 mV, and no systematic influence of oxygen flow during sputtering of the GaOx-adjacent oxide layer was found.

## Open questions

- Can sputtered multilayers be made periodic below a 4 nm period, or is interfacial intermixing a hard floor that pushes short-period applications to MBE?
- Do sputtered V or NbN resonators reach internal quality factors competitive with established Nb and Ta processes, and is the loss surface-dominated in a way that deposition changes can fix?
- Does the cold-sintering route to sputtering targets scale beyond 2-inch diameter and generalise beyond calcium hydroxide to other thermally unstable target chemistries?
- Does the interface-sharpness deficit of sputtering versus MBE actually degrade device performance in interface-sensitive applications such as CISS spin valves, or is it only visible in structural characterisation?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
