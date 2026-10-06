---
type: concept
slug: chemical-vapor-deposition
canonical_name: CVD (Chemical Vapor Deposition)
aliases:
- CVD
- PECVD
- LPCVD
- FCVD
- HDP-CVD
- CVD growth
- cvd-growth
kind: technology
parent_concepts:
- deposition
related_concepts:
- ald-atomic-layer-deposition
- pvd-sputtering
- initiated-cvd-icvd
- epitaxy
- low-k-dielectrics
- ru-w-co-metallisation
- thin-films-coatings
- semiconductor-equipment
sources:
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
frontier:
- Can AI-guided synthesis with real-time optical diagnostics actually close the wafer-scale reproducibility gap for 2D semiconductors, and on what timescale relative to the NSF-DFG award period beginning August 2026 2026 08 10 nsf 2522671 collaborative research dmref nsf dfg ai ?
- Does the pulsed-precursor thickness gain seen in hot-wire CVD of a-Si:H transfer to other precursors and reactor geometries, or is it specific to filament dissociation of silane 2026 06 02 catalytic precursor dissociation in hot wire cvd and compari?
- Is the intrinsic disorder and multi-domain structure of CVD-grown 3R-WSe2 a recipe problem that better growth control removes, or an inherent limit of the CVD route for sliding-ferroelectric devices 2026 06 02 impact of disorder dynamics and multi domain kinetics on the?
- How do CVD-grown films compare directly against MBE and PVD on defect density, uniformity and cost per wafer for the same material? No source supplied makes that comparison.
- Do air gaps (k=1.0) and amorphous BN take the tightest-pitch dielectric layers, or does enhanced SiCOH (Black Diamond lineage) keep extending?
- Can any CVD/ALD chemistry ever reach hydrogen-free carbon nitride, or does the precursor-hydrogen constraint stand (the Halltech premise)?
- Where does flowable CVD gap-fill hit its limit in 3D-NAND / GAA high-aspect-ratio structures?
- Does low-temperature (sub-450C) diamond and dielectric CVD open a die-level thermal market (the PROUD 400C window)?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 42
descendants:
- cvd-growth
scorecard:
  viability: 5
  drivers: 4
  novelty: 2
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 2
sources_30d: 9
recent_mentions:
- slug: 2025-07-01-a-primer-carbon-nanotubes
  title: 'A Primer: Carbon Nanotubes'
  date: '2025-07-01'
  kind: substack
neighbors:
- slug: ald-atomic-layer-deposition
  name: ALD (Atomic Layer Deposition)
  path: /manufacturing/equipment-processes/ald-atomic-layer-deposition/
  macro: manufacturing
- slug: pvd-sputtering
  name: PVD / Sputtering
  path: /manufacturing/equipment-processes/pvd-sputtering/
  macro: manufacturing
- slug: initiated-cvd-icvd
  name: Initiated CVD (iCVD)
  path: /manufacturing/equipment-processes/initiated-cvd-icvd/
  macro: manufacturing
- slug: epitaxy
  name: Epitaxy
  path: /manufacturing/equipment-processes/epitaxy/
  macro: manufacturing
- slug: low-k-dielectrics
  name: Low-K Dielectrics
  path: /materials/functional-layers/low-k-dielectrics/
  macro: materials
- slug: ru-w-co-metallisation
  name: Ru / W / Co Metallisation
  path: /manufacturing/equipment-processes/ru-w-co-metallisation/
  macro: manufacturing
- slug: thin-films-coatings
  name: Thin Films & Coatings
  path: /materials/advanced-materials/thin-films-coatings/
  macro: materials
- slug: semiconductor-equipment
  name: Semiconductor Equipment
  path: /manufacturing/equipment-processes/semiconductor-equipment/
  macro: manufacturing
---
**Chemical vapour deposition grows solid films by reacting gas-phase precursors on a heated substrate, and in the 2026 literature it is the default route to almost every emerging semiconductor film, from thick β-Ga2O3 power epitaxy to 200 mm silicon nitride photonics and 2D transition metal dichalcogenides.**

## Summary

Chemical vapour deposition (CVD) is a family of processes in which volatile precursors are transported over a heated substrate, dissociate, and react to leave a solid film. The variants differ mainly in how the precursor is broken apart and at what pressure. Low-pressure CVD (LPCVD) uses thermal dissociation in a reduced-pressure furnace and is the workhorse for dielectric films and thick epitaxial layers. Metalorganic CVD (MOCVD) uses organometallic precursors and dominates compound semiconductor epitaxy such as GaN. Plasma-enhanced and low-energy plasma-enhanced CVD add electrical dissociation so growth can happen at lower substrate temperatures, which is how planar hexagonal germanium was stabilised on m-plane CdS. Hot-wire CVD instead cracks precursor on a filament held above 1600 °C.

The parameters that decide outcomes are precursor chemistry and dose, partial pressures, substrate temperature and its gradient, carrier gas composition, and the kinetics of adsorption and surface diffusion relative to growth rate. These are not free knobs: in three-zone CVD of MnSe, precursor vapour pressure rather than temperature alone determined whether α-phase nanorods or β-phase triangular flakes formed. In vanadium-doped WS2, non-equilibrium growth kinetics caused dopants to segregate along crystallographic bisectors, producing tensile strain channels of about 0.70 percent rather than a random dopant distribution. Growth kinetics, in other words, write structure into the film whether or not the operator intends it.

CVD is not a new technology and is not in question as a technique. The live question is process control: whether the recipe space for each new material can be mapped fast enough, and whether the resulting films are uniform and reproducible enough across a wafer for devices. That is precisely where public money is going, with an NSF-DFG programme funding AI-guided 2D synthesis with real-time optical growth diagnostics at $1,440,000 and $160,000 across two collaborating institutions, and a national user facility building data infrastructure over roughly twenty thousand samples grown by MOCVD, MBE and bulk crystal growth.

Read this page, therefore, not as an assessment of whether CVD works, but of where the frontier of CVD sits and what it is currently unlocking.

## Viability (5/5)

The caveat is material-specific. For newer systems the films work but carry defects that matter: CVD-grown 3R-WSe2 bilayers show ferroelectric switching whose behaviour is governed by intrinsic disorder and multi-domain kinetics that remain poorly understood, and reproducible wafer-area production of atomically thin films is explicitly described as an unsolved manufacturing challenge. Viability of the technique is not at issue; viability of any given recipe is earned one material at a time.

**TLDR: Demonstrated at device grade and in a 200 mm CMOS pilot line; the question is recipe development, not feasibility.**

## Drivers (4/5)

On the demand side, the sources point to several independent pulls. Vertical GaN-on-silicon is framed as a route to cost-effective power electronics and high-resolution micro-LEDs, bottlenecked by buffer layer resistance rather than by the epitaxy itself. Commercialisation of optical interconnects, quantum computing, AR/VR and medical diagnostics is given as the driver for low-loss SiN photonics in the visible to near-infrared. Two-dimensional semiconductors are pursued for smaller, faster and more energy-efficient devices than silicon.

On the supply side, CVD's attraction is repeatedly stated in the same terms: simplicity, low cost, scalability and widespread existing adoption in the semiconductor industry, which is why it was chosen for the first CVD synthesis of doped iron germanium telluride nanosheets. Public funding is flowing into the control layer rather than the hardware, via AI-guided synthesis with real-time in-situ diagnostics and shared data infrastructure covering around twenty thousand samples. The sources do not quantify equipment markets or capital spend, so the commercial magnitude of the driver is not directly evidenced.

**TLDR: Demand pull from wide-bandgap power, visible photonics and 2D electronics; supply side is cheap, CMOS-compatible and already installed.**

## Novelty (2/5)

CVD is described in the sources as conventional and widely adopted, not as an innovation. The novelty sits in specific process refinements, and those are measurable. Pulsing silane in hot-wire CVD raised a-Si:H film thickness from 175 ± 5 nm to 425 ± 8 nm for the same 75 cm3 (STP) precursor dose split into 15 pulses, a substantial gain in precursor utilisation from a scheduling change alone. Borazine-based CVD tuned between 800 and 1000 °C moves boron nitride from fully amorphous to mixed amorphous-crystalline, taking cross-plane thermal conductivity from below 0.5 W m-1 K-1 to 1.5 W m-1 K-1 and Young's modulus from 7.5 ± 0.7 GPa to 53 ± 5 GPa. Plasma-free Ga-assisted etching inside an LPCVD reactor produced deep mesas with electrical characteristics closely matching unetched planar devices, avoiding plasma damage.

## Diffusion (4/5)

Diffusion of the tool is effectively complete for established films: LPCVD nitride sits inside a 200 mm CMOS pilot line as a standard layer and inside commercial-style MEMS diaphragms, and CMOS compatibility is cited as a reason to prefer CVD for new materials. Because the equipment base and process know-how already exist, adoption friction for a new CVD film is far lower than for a new deposition modality.

The barrier is per-material process development and yield, not installation. Phase selection in MnSe depends sensitively on precursor vapour pressure, and the resulting flakes are 15 to 30 nm thick with lateral sizes up to 20 µm, far from wafer-scale continuous film. Dopant distribution in CVD WS2 is kinetically determined and anisotropic rather than controllable by intent. Reproducible large-area 2D growth is named as a major scientific and manufacturing challenge in current funding calls. The general pattern of nanomaterials taking decades from lab demonstration to routine product use is documented for carbon nanotubes <sup class="ref"><a href="https://stateofthefuture.substack.com/p/a-primer-carbon-nanotubes" title="A Primer: Carbon Nanotubes" rel="noopener">ref</a></sup>, and there is no evidence in these sources that 2D CVD films are moving faster.

**TLDR: Already ubiquitous in incumbent uses; each new material still needs its own recipe, and 2D films are the hard case.**

## Impact (4/5)

If CVD process control keeps improving at the rate these papers imply, the downstream consequences are large and diverse. Thick, controllably doped β-Ga2O3 epitaxy at up to 16.6 µm/h is the precondition for high-voltage vertical devices. Low-resistance GaN on silicon would unlock cost-effective power electronics and micro-LEDs on large silicon wafers. LPCVD SiN underpins a visible-to-near-infrared photonic platform aimed at interconnects, quantum computing and AR/VR. Further out, CVD-grown materials are the substrate for research device classes: air-stable Mo2C nanoflakes showing a superconducting diode effect above 40 percent efficiency at 4 K, sliding ferroelectric 3R-WSe2 for non-volatile memory, and doped FGT for spintronics.

The honest limit is that none of the supplied sources put a number on market size, cost per wafer, or displaced incumbent spend. The impact judgement here rests on breadth of enabled applications and demonstrated device metrics, not on economics, and a 5 would require evidence the sources do not contain.

**TLDR: It is the enabling step for wide-bandgap power devices, visible photonics and 2D electronics, though the sources do not quantify economic value.**

## Timing Now (0-2yr)

For dielectrics and photonic films, the timing question is closed: dual LPCVD SiN layers are being run in a 200 mm CMOS pilot line today. Wide-bandgap epitaxy is close behind, with LPCVD β-Ga2O3 producing thick doped films and working Schottky diodes with field termination in 2026, and MOCVD-based GaN-on-Si strategies at the demonstration stage.

The 2D and magnetic van der Waals systems are on a slower clock. MnSe growth still yields micron-scale flakes, Ni-doped FGT is at first-synthesis stage, and the AI-guided synthesis programmes intended to solve wafer-scale reproducibility have only just been awarded. Those programmes' results, not the deposition hardware, set the date for 2D CVD in manufacturing.

**TLDR: CVD is already in production tooling; the frontier material systems split between now and five-plus years depending on the material.**

## Overrated or underrated? Fairly rated

CVD is correctly understood as infrastructural: cheap, scalable, CMOS-compatible and the default first attempt for any new film. Nobody is over-claiming it in these sources, and nobody is ignoring it. The paper trail across 2026 is consistent with a mature technique being pointed at successively harder material systems and mostly succeeding, with the LPCVD β-Ga2O3 mobility and growth rate results and the 200 mm SiN pilot line as the strongest evidence.

The part that is arguably underrated within that fair rating is process control as a discipline in its own right. The interesting results here are not new reactors but new schedules and diagnostics: pulsing precursor flow to more than double film thickness per dose, recognising that growth kinetics deterministically write dopant and strain patterns rather than randomising them, and building sample-tracking and AI-guided feedback over tens of thousands of growths. Investors looking at CVD should be looking at the control and data layer, not the chamber.

## Prediction

By 31 December 2028, a peer-reviewed report will demonstrate LPCVD-grown Sn-doped β-Ga2O3 homoepitaxy with room-temperature Hall mobility above 113 cm2 V-1 s-1 at a carrier concentration near 1 × 10^17 cm-3, exceeding the value reported in August 2026.

## Evidence base

## Open questions

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
