---
type: concept
slug: substrates
canonical_name: Substrates
aliases: []
parent_concepts:
- materials
related_concepts: []
sources:
- '[[2025-04-23-what-if-ai-can-already-feel]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2025-02-05-you-like-ai-agents-you-are-gonna]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2026-08-07-the-memory-trade-isnt-over-weights]]'
- '[[2026-04-14-the-photonic-foundry-fallacy]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 179
descendants:
- 2d-materials
- aluminium-gallium-nitride
- compound-semiconductors
- diamond
- gaas
- gallium-antimonide
- gallium-arsenide
- gallium-nitride
- gallium-oxide
- gallium-phosphide
- gan-on-diamond
- gan-on-silicon
- ge-on-si-mid-ir
- germanium-on-silicon
- graphene
- graphene-2d-materials
- hbn-hexagonal-boron-nitride
- hgcdte
- iii-v-compound-semiconductors
- indium-antimonide
- indium-arsenide
- indium-gallium-arsenide
- indium-gallium-nitride
- indium-phosphide
- silicon-carbide
- silicon-carbide-photonics
- silicon-germanium
- silicon-nitride
- single-crystal-diamond
- tmds-mos2-wse2
- wide-bandgap-semiconductors
- zinc-oxide
- zinc-selenide
frontier:
- Does the 0.5 nm silicide template plus amorphous-like interlayer hold uniformity, vertical resistance and thermal stability across a 150 or 200 mm silicon wafer, and through full device processing, rather than on test coupons?
- Does the roughly 25x sub-kelvin thermal conductivity advantage of high-resistivity silicon over sapphire survive at the level of a packaged, wired, multi-chip cryogenic module, where interfaces and on-chip routing may dominate the thermal path?
- Can confocal subsurface backscattering microscopy be run at in-line inspection throughput on production SiC wafers, and does the dislocation count it reports correlate with measured reverse leakage and device lifetime?
- Does offcut-optimised heteroepitaxial beta-Ga2O3 on sapphire reach the doping control and mobility needed for power devices, or is the improvement confined to structural metrics such as roughness and rocking-curve width?
- Does the 0.5 nm silicide/amorphous interlayer route on Si(111) hold its low vertical resistance and ohmic behaviour at 150 mm or 200 mm wafer scale and after full device thermal budgets, and what is the measured specific interface resistance an advanced epitaxial strategy enabling vertical g
scorecard:
  viability: 4
  drivers: 3
  novelty: 4
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
sources_7d: 5
sources_30d: 14
recent_mentions:
- slug: 2026-08-31-qcells-tandem-iec-ul-certification-tuv-rheinland
  title: Qcells secures TUV Rheinland certification for perovskite-silicon tandem solar tech (pv magazine, 16 Jul 2026; pv-tech corroborating)
  date: '2026-08-31'
  kind: web
- slug: 2026-08-07-the-memory-trade-isnt-over-weights
  title: 'The Memory Trade Isn''t Over: Weights and KV Cache'
  date: '2026-08-07'
  kind: substack
- slug: 2026-07-02-semianalysis-ectc2026-advanced-packaging
  title: 'ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More'
  date: '2026-07-02'
  kind: web
- slug: 2026-06-17-nawah-vacnt-technology
  title: NAWAH Architectured Nanomaterials — VACNT technology & positioning
  date: '2026-06-17'
  kind: web
- slug: 2026-06-04-bezos-flourish-brain-core-algorithm
  title: Jeff Bezos Is Funding a Wild Hunt for the Brain's 'Core Algorithm'
  date: '2026-06-04'
  kind: web
- slug: 2026-06-04-droplet-microfluidics-directed-evolution-throughput
  title: High-throughput droplet-based microfluidics for directed evolution of enzymes
  date: '2026-06-04'
  kind: web
- slug: 2026-04-15-semianalysis-isscc-2026
  title: 'ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More'
  date: '2026-04-15'
  kind: web
- slug: 2026-04-14-the-photonic-foundry-fallacy
  title: The Photonic Foundry Fallacy
  date: '2026-04-14'
  kind: substack
neighbors: []
---
**The substrate is the wafer or support film underneath a device layer, and recent work shows it is an active design variable, with measured cases where changing substrate material, miscut angle or interfacial template alters crystal quality, vertical resistance, cryogenic heat flow and mechanical distortion by factors of several to tens.**

## Summary

A substrate is the base on which a functional layer is grown or deposited: a single-crystal wafer (silicon, sapphire, SiC, GaAs, MgO, LaAlO3, scandates), a coated glass (fluorine-doped tin oxide), an oxidised silicon wafer, or a polymer sheet. Its conventional job is mechanical support plus a crystallographic template. The papers collected here show it doing considerably more than that: it fixes the epitaxial strain state and hence the magnetic or electronic ground state of the film, carries heat out of the device, participates optically as a layered medium that mediates coupling between resonators on top of it, screens excitons dielectrically, and sets the mechanical strain field seen by whatever is patterned above.

Where the substrate cannot supply the right lattice, an engineered interlayer substitutes for it. A sputtering-plus-rapid-thermal-annealing route forms a sub-nanometre (0.5 nm) silicide template on Si(111), demonstrated across 25 different metallic species, producing an amorphous-like interlayer that accommodates mismatch and supports MOCVD overgrowth of GaN with low vertical resistance and ohmic behaviour, the stated bottleneck for vertical GaN-on-silicon power devices and micro-LEDs. Sapphire also serves as a template for stabilising phases that are not otherwise stable: metastable TaO2 was epitaxially stabilised on r-plane Al2O3 (1-102) as single-oriented, monodomain anisotropically strained films synthesis of epitaxial tao2 thin films on al2o3 by suboxide.

Outside epitaxy, the substrate is chosen for a non-structural property. For cryogenic quantum integration, measured sub-kelvin thermal conductivity at 300 mK spans high-resistivity silicon at 5x10^-2 W/m.K against low-resistivity silicon at 8x10^-4, borosilicate at 2x10^-3 and sapphire at 2x10^-3 W/m.K, a spread of more than an order of magnitude that directly sets the achievable thermal budget for co-integrated qubits, control and readout. For stretchable displays, a line-patterned hard PDMS network embedded in soft PDMS gives a near-zero effective Poisson ratio, suppressing the lateral contraction that otherwise distorts the display under tensile strain. For nanophotonics, a T-matrix framework shows the substrate contributes direct, substrate-mediated interparticle and substrate-mediated self-coupling channels between high-index nanoparticles, with the response depending on array density, particle-substrate distance and substrate index. For biointerfaces, nanostructured zirconia films selectively enhanced glial calcium signalling relative to flat zirconia substrates of the same chemistry.

## Viability (4/5)

The specific engineered routes are earlier stage. The silicide-template GaN-on-Si work reports ohmic vertical behaviour, thermal stability and STEM confirmation of the amorphous-like interlayer, plus versatility across 25 metals, but the source gives no wafer diameter, yield, uniformity or device reliability figures. The zero-Poisson elastomer is a demonstrated architecture rather than a qualified display substrate. The cold-sintered calcium hydroxide sputtering target route reaches up to 98% theoretical density at 100 to 300 degrees C under 400 MPa and has been scaled to 2-inch diameter targets, which is real but small. Four, not five, because the underlying physics is settled while the manufacturing claims are not yet evidenced at scale.

**TLDR: Substrate effects are measured, quantified and reproduced across independent systems; the newer templates and engineered supports are single-group, small-area demonstrations.**

## Drivers (3/5)

Demand is stated explicitly in device terms rather than commercial terms. Vertical GaN-on-silicon is framed as a route to cost-effective power electronics and high-resolution micro-LEDs, bottlenecked specifically by the vertical resistance of conventional buffer layers, which is a substrate-stack problem. Large-scale quantum systems are said to require close integration of qubits, control electronics and readout, making cryogenic thermal management central, which turns substrate thermal conductivity into a system-level constraint. Stretchable displays for wearables, soft sensors and AR/VR motivate the zero-Poisson substrate. In SiC, high threading dislocation density is tied to reverse leakage and degradation, and commercial inspection based on surface profiling and photoluminescence dark contrast is said to miss nanoscale dislocations, which is a demand signal for substrate metrology.

On the supply side the enabling processes are deposition techniques that already exist in industry: sputtering with rapid thermal annealing followed by MOCVD overgrowth, HVPE at growth rates up to 30 micrometres per hour, suboxide MBE and thermal laser epitaxy synthesis of epitaxial tao2 thin films on al2o3 by suboxide, non-vacuum spin coating on FTO glass, and low-temperature target sintering. The score is held at 3 because none of the sources quantifies substrate demand, wafer pricing or supply constraints, so the commercial half of the driver argument is unevidenced here.

**TLDR: Clear technical pull from power electronics cost, micro-LEDs, cryogenic quantum integration and wearables; the sources contain no market, price or capacity data.**

## Novelty (4/5)

The comparisons are explicit and mostly quantified. Against conventional GaN-on-silicon buffer layers, whose high vertical resistance is named as the deployment bottleneck, the 0.5 nm silicide template plus amorphous-like interlayer delivers ohmic vertical behaviour and exceptionally low vertical resistance while remaining compatible with MOCVD overgrowth, and the alternative it displaces is the expensive bulk GaN substrate. Against on-axis sapphire, an 8 degree offcut gives a 5.4x reduction in roughness and a 2.4x reduction in rocking-curve FWHM for beta-Ga2O3. Against sapphire and borosilicate, high-resistivity silicon offers roughly 25x higher thermal conductivity at 300 mK. Against ordinary elastomers with high Poisson ratio, the heterogeneous-modulus PDMS substrate reaches near-zero effective Poisson ratio while staying soft and transparent.

Some novelty is conceptual rather than incremental. Epitaxial stabilisation of metastable TaO2 on r-plane sapphire produces a compound that is not otherwise accessible, so the substrate is the synthesis tool, not a support synthesis of epitaxial tao2 thin films on al2o3 by suboxide. A ferroelectric twisted bilayer hBN substrate is predicted to split valley-degenerate excitons in a TMD monolayer by about 3 meV without any external magnetic field, and to select between dark charge-transfer and quasi-1D Wannier excitons depending on dielectric environment, which is a substrate acting as an electronic control knob. That last result is first-principles theory, not measurement, and is weighted accordingly.

**TLDR: Several results beat the obvious incumbent by a stated factor: order-of-magnitude cryogenic thermal conductivity, more than halved rocking-curve width, and ohmic vertical conduction where buffers were previously resistive.**

## Diffusion (3/5)

Adoption favours substrate innovations that reuse existing equipment, and several here do: sputtering and rapid thermal annealing before standard MOCVD, commercially available Si(111), sapphire and SiC wafers, and low-temperature target sintering scaled to a 2-inch diameter. Against that, the barriers visible in the sources are real. Reproducibility is one: conflicting published results for GaSe on GaAs are attributed to an uncontrolled substrate surface preparation step, meaning the recipe is not yet transferable between groups. Inspection is another: commercial defect systems reportedly miss nanoscale threading dislocations in SiC because they lack surface signatures and band-edge photoluminescence is quenched, so confocal subsurface backscattering microscopy is proposed as a nondestructive alternative that also distinguishes dislocation types. A substrate cannot be qualified for volume production faster than it can be measured.

**TLDR: Process routes are deliberately fab-adjacent, but everything shown is small-area, single-group, and the metrology needed to qualify substrates is itself still being invented.**

## Impact (4/5)

The leverage argument is strong because the same lever appears in unrelated value chains. In power electronics and micro-LEDs, moving vertical GaN onto silicon is described as a transformative cost change, gated entirely on the buffer or template layer. In SiC power devices, substrate dislocation density is tied directly to reverse leakage and degradation, that is, to yield and field reliability. In quantum systems, a substrate choice buys or loses more than an order of magnitude in sub-kelvin thermal conductivity, which propagates into how much control and readout electronics can be co-integrated at the qubit stage, and substrate and material selection is an explicit design consideration in proposals for transmons operating above 10 GHz rather than the usual 4 to 6 GHz.

**TLDR: The substrate is a low-cost part that sets ceilings on cost, defect density, thermal budget and even which phases exist, across power electronics, quantum hardware, spintronics and displays.**

## Timing Now (0-2yr)

For the general lever, the timing is now. Choosing high-resistivity silicon over sapphire for a cryogenic quantum chip, or an 8 degree offcut sapphire over on-axis, are decisions available to anyone today with measured consequences. The same applies to formalising substrate surface preparation as a controlled process step in 2D-on-3D epitaxy.

The specific new routes sit further out and the sources do not date them. Silicide-templated vertical GaN on silicon has to survive wafer-scale uniformity, device fabrication and reliability testing before it displaces anything; zero-Poisson elastomeric substrates have to be integrated with actual emissive pixel arrays; subsurface dislocation microscopy has to be shown at in-line wafer throughput. Treat those as a 2 to 5 year question, with the ferroelectric-substrate exciton engineering, currently a first-principles prediction, later still.

**TLDR: Substrate selection and miscut are already the binding variable in published device work; the engineered templates and elastomeric substrates need longer.**

## Overrated or underrated? Underrated

The caveat is that this is an assessment of a category, not of a product, and category-level optimism should not be transferred to any individual claim. The silicide template for vertical GaN-on-silicon is the highest-value single result in this set and also the one with the least evidence beyond a first preprint. Anyone investing on that specific line should treat it as unreplicated. The defensible position is that substrate and interface engineering, including the metrology to qualify it, deserves more attention and capital than it receives relative to the device layers it constrains.

## Prediction

By June 2028, at least one group independent of the original authors will report vertical GaN grown on Si(111) using a sub-nanometre metal-silicide interfacial template with ohmic vertical conduction, on wafers of 100 mm diameter or larger, following the route described in May 2026.

## Evidence base

## Open questions

- Does the 0.5 nm silicide template plus amorphous-like interlayer hold uniformity, vertical resistance and thermal stability across a 150 or 200 mm silicon wafer, and through full device processing, rather than on test coupons?
- Does the roughly 25x sub-kelvin thermal conductivity advantage of high-resistivity silicon over sapphire survive at the level of a packaged, wired, multi-chip cryogenic module, where interfaces and on-chip routing may dominate the thermal path?
- Can confocal subsurface backscattering microscopy be run at in-line inspection throughput on production SiC wafers, and does the dislocation count it reports correlate with measured reverse leakage and device lifetime?
- Does offcut-optimised heteroepitaxial beta-Ga2O3 on sapphire reach the doping control and mobility needed for power devices, or is the improvement confined to structural metrics such as roughness and rocking-curve width?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
