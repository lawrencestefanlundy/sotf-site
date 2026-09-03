---
type: concept
slug: stm
canonical_name: STM (Scanning Tunneling Microscopy)
aliases:
- scanning tunneling microscopy
- scanning probe microscopy
parent_concepts:
- electron-scale-metrology
related_concepts:
- arpes
- electron-scale-metrology
sources: []
frontier:
- What are the per-operation yield and error rate of mechanosynthetic donation and abstraction, and does either scale beyond a single model build site 2026 06 15 towards atom by atom fabrication mechanosynthetic donation a?
- Can the coupled sample-and-instrument digital twin framework, demonstrated for amplitude-modulation scanning probe microscopy, be transferred to STM where tip state is unknown and drifts 2026 07 08 from closed loop optimization to open decision making couple?
- Does the proposed QPI tomography of the density matrix and quantum geometric tensor with unpolarised tips survive experimental test, and on which materials 2026 06 18 electron state tomography from quasiparticle interference ma?
- Is THz-STM able to resolve Floquet gaps and edge states experimentally, as the nonequilibrium Green's function treatment predicts 2026 07 20 probing topological floquet states in graphene with ultrafas?
- Can in-situ STM on growing films achieve useful throughput at industrial scale?
last_updated: '2026-08-31'
tags:
- concept
- semiconductors
- condensed-matter
public_expressions:
- IBM
- STM
mention_count: 38
scorecard:
  viability: 4
  drivers: 3
  novelty: 3
  diffusion: 3
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 1
sources_30d: 6
recent_mentions: []
neighbors:
- slug: arpes
  name: ARPES (Angular-Resolved Photoemission Spectroscopy)
  path: /manufacturing/equipment-processes/arpes/
  macro: manufacturing
- slug: electron-scale-metrology
  name: Electron-scale metrology
  path: /manufacturing/equipment-processes/electron-scale-metrology/
  macro: manufacturing
---
**Scanning tunnelling microscopy resolves the electronic structure of surfaces atom by atom, and across 2026 it is simultaneously the default characterisation tool for quantum materials and an early-stage fabrication tool being pushed towards positionally controlled atom-by-atom synthesis.**

## Summary

Scanning tunnelling microscopy (STM) brings a sharp conductive tip within a fraction of a nanometre of a conductive surface and measures the current that tunnels across the gap. Because that current depends exponentially on the gap width, a feedback loop holding it constant while the tip raster-scans produces a map with atomic lateral resolution. Sweeping the bias instead of scanning gives scanning tunnelling spectroscopy (STS), which reads out the local density of electronic states at a chosen point, so the instrument returns both structure and local electronic structure from the same measurement. Variants extend this: spin-polarised STM uses a magnetic tip to read spin contrast and to couple magnetically to the sample, the field-emission regime accesses image potential states above the surface, and quasiparticle interference (QPI) mapping around defects converts real-space standing waves into momentum-space information.

In the sources, the dominant use is metrology for correlated and topological matter. STM and STS resolve Dirac and flat bands in triangulene-based superatomic graphene, the hexagonal lattice and stacking of a single-layer conjugated metal-organic framework grown on graphite, charge density wave orders tuned by chemical doping in misfit layer compounds, and quantised collective modes of a Tomonaga-Luttinger liquid in mirror twin boundary segments as short as one nanometre. It is also used to monitor on-surface chemical synthesis reaction by reaction.

The manufacturing claim is separate and much younger. Inverted-mode STM with functionalised molecular tools has been used to demonstrate positionally controlled donation of carbon atoms and abstraction of silicon atoms at a model build site on an atomically clean, cryogenic silicon surface. That is a chemistry demonstration at single-site scale, not a process.

The parameters that decide STM's usefulness are: sample conductivity (insulating films need workarounds, which is why photoexcitation sensing on dielectric films has been moved to AFM instead); vacuum and cryogenic stability; the unknown and drifting state of the tip; serial single-tip throughput; and the human labour of labelling and interpreting the images, which is now being attacked with few-shot and unsupervised segmentation and with machine-learning regression of physical parameters directly from image data.

## Viability (4/5)

The metrology function is not in question. Independent groups in the source set resolve atomic lattices, molecular bonds, spin contrast and collective excitations across silicon, germanium, oxide, graphene, transition metal dichalcogenide, metal-organic framework and topological insulator surfaces, and pair the results with DFT and ARPES without apparent instrument-limited disagreement. Measurable, quantitative outputs are being extracted, for example a tip-induced energy shift of up to 10 meV in the spin-polarised surface state of Cr(001) that switches with field and tip-surface distance.

The fabrication function is much weaker. The mechanosynthesis result demonstrates donation of carbon and abstraction of silicon at a model build site under inverted-mode STM with functionalised molecular tools, on an atomically clean cryogenic surface. The sources give no yield, rate, error correction or scaling data, so nothing in them supports a claim that atom-by-atom fabrication is a viable process. The score of 4 reflects the instrument, not the factory.

**TLDR: As a measurement instrument it plainly works and is used routinely; as a fabrication process it is at single-site demonstration stage.**

## Drivers (3/5)

Demand in the sources is entirely scientific and it is intense. Every emerging materials class in the set requires local, real-space electronic information that averaging probes cannot give: altermagnetism in the one-unit-cell limit, curvature-modulated charge order, predicted nematic Wigner crystals in rhombohedral graphene whose proposed experimental signature is an STM measurement. There is also a device-adjacent driver: defect and adsorbate identification on Si(001) and Ge(001), including adsorbed AsH3 molecules, which is the surface chemistry of dopant placement.

On the supply side the constraints being relieved are analysis and autonomy rather than hardware. Few-shot and unsupervised segmentation removes the need for large manually annotated image sets and transfers across surfaces, and coupled digital twins of sample and instrument are being proposed to let planners forecast the outcome of candidate microscope operations before executing them, although that framework was realised for amplitude-modulation scanning probe microscopy rather than STM. The sources contain no market size, instrument shipment or price data, so the commercial driver cannot be assessed.

**TLDR: Strong research demand pull from quantum materials and atom-precision devices; the sources say nothing about commercial or industrial demand.**

## Novelty (3/5)

STM's differentiator is locality. In the misfit-compound and CrSb work it is combined with ARPES and DFT precisely because ARPES gives band structure but averages over the sample; the clearest example is the TiSe2-NbSe2 heterostructure where ARPES reports complete suppression of long-range charge order while high-resolution STM resolves its revival in curved regions. Against AFM the comparison is genuinely contested rather than one-sided: AFM gives bond-resolved chemical structure of on-surface reaction intermediates that STM does not, and photoexcitation detection in molecules on non-conductive dielectric films has been moved from STM to a synchronised-laser AFM scheme with angstrom contrast.

The novelty in the set is incremental and mode-specific: inverted-mode STM for mechanosynthesis, operation in the field-emission regime to create an active electric-field geometry and split image potential states, and proposed ultrafast terahertz STM as a real-space, energy-resolved probe of Floquet gaps and edge states with a supporting nonequilibrium Green's function formalism. A proposed method to reconstruct the density matrix and quantum geometric tensor from QPI maps around impurities using conventional unpolarised tips would add orbital resolution that local probes normally lack, but it is theory.

**TLDR: The base technique is mature; what is new is the mode zoo, and its advantage over momentum-space probes is spatial, not spectral.**

## Diffusion (3/5)

Within its niche adoption is complete: the source set alone spans groups across Europe, North America and Asia using STM as a default step in materials characterisation and on-surface synthesis. That is the ceiling of the current diffusion, and the barriers to going further are intrinsic to the physics. The sample must conduct, which is why dielectric-film experiments migrate to AFM. Measurements in the set are made at low temperature and in ultra-high vacuum, and require atomically clean surfaces; the mechanosynthesis build site is explicitly atomically clean and cryogenic, and the MOF growth uses a multi-step ultra-high-vacuum protocol.

The second barrier is human throughput. Identifying and labelling features against a background is described as labour-intensive and requiring significant human effort, which is the stated motivation for automated segmentation. Autonomy work is heading the same way, from closed-loop optimisation towards planners that forecast instrument and sample response before acting. If those succeed, STM diffuses further as a screening tool. The sources give no evidence of any production or inline industrial deployment, and no multi-tip or parallelised instrument appears anywhere in them, so the serial single-tip architecture remains the hard limit on manufacturing diffusion.

**TLDR: Already diffused throughout surface-science laboratories; essentially undiffused beyond them, and the barriers are structural.**

## Impact (3/5)

As a scientific instrument the impact is real and repeatedly decisive: it establishes the atomic-scale confinement limit of Luttinger-liquid behaviour in one-nanometre segments and identifies a new class of many-body quantum dots built from collective bosonic modes, provides the direct observation of interfacial exchange coupling in a magnetic tunnel junction relevant to spin-triplet superconductivity and the quantum anomalous Hall effect, and supplies the falsification test for theoretical phase diagrams such as nematic Wigner crystals. It also enables synthesis routes to be verified atom by atom, for instance periodic graphitic nitrogen substitution in graphene nanoribbons.

The larger claim, that STM becomes a manufacturing process rather than a metrology one, would change the economics of atomically precise devices. The sources support only the first chemical steps of that path, addition of a carbon atom and removal of a silicon atom under positional control, with no data on throughput or scale. Impact is therefore scored on what is demonstrated, not on the ambition.

**TLDR: Indispensable to quantum materials discovery; the much larger manufacturing prize is asserted rather than demonstrated.**

## Timing Now (0-2yr)

For characterisation the technology matters now. The source set is a few months of 2026 preprints and STM is the primary or corroborating evidence in almost all of them, including replaced and revised versions indicating active peer scrutiny. The near-term change is in software rather than hardware: automated feature segmentation and machine-learning extraction of physical parameters such as the Hubbard U directly from images are being demonstrated now, and autonomous decision-making frameworks are being formulated.

The atom-by-atom fabrication branch cannot be dated from the sources. A single-site donation and abstraction demonstration on a cryogenic silicon surface gives no basis for a schedule to useful structures, and the proposed THz-STM Floquet probe is still theory awaiting experiment.

**TLDR: The instrument is already load-bearing in quantum materials research; the fabrication branch is on a much longer clock the sources cannot date.**

## Overrated or underrated? Fairly rated

STM is correctly valued for what it actually is: a mature, indispensable local probe whose binding constraint has shifted from imaging capability to sample preparation, throughput and human interpretation time. Nothing in the sources suggests the community over- or under-estimates it as a measurement tool; it is simply used, and used well, including in combinations where its weaknesses are covered by AFM and ARPES.

The part that invites overrating is the manufacturing framing. Positionally controlled donation and abstraction of single atoms is a genuine result and a necessary step, but a very large author list and an explicit atom-by-atom fabrication banner sit on top of a model build site under cryogenic ultra-high vacuum with no reported rate, yield or scaling. Investors should treat STM metrology and STM fabrication as two different assets with two different risk profiles. The more credible near-term commercial thread in these sources is automation of STM data handling, where the bottleneck is explicit and the fixes are already working across three different surfaces.

## Prediction

By July 2029, published STM mechanosynthesis will still report only single-site or few-site positionally controlled atom addition and removal, with no demonstration of a parallel multi-tip STM fabrication tool in the literature.

## Evidence base

- 15 June 2026: inverted-mode STM with functionalised molecular tools demonstrated positionally controlled donation of carbon and abstraction of silicon atoms at a model build site on an atomically clean, cryogenic surface.
- 8 May 2026: low-temperature STM and STS visualised quantised collective modes of a Tomonaga-Luttinger liquid in mirror twin boundary segments of monolayer WSe2 as short as one nanometre.
- 30 June 2026: spin-polarised STM with an Fe-coated tip induced an energy shift of up to 10 meV in the spin-polarised surface state of Cr(001), switchable by external magnetic field.
- 4 June 2026: ARPES showed complete suppression of long-range charge density wave order in flat regions of a TiSe2-NbSe2 heterostructure while high-resolution STM resolved a curvature-driven revival.
- 19 June 2026: few-shot plus unsupervised segmentation of STM images removed the need for large manually annotated datasets and transferred across Si(001), Ge(001) and TiO2(110), including adsorbed AsH3.
- 17 June 2026: photoexcitation detection in single molecules on non-conductive dielectric films was implemented with laser-synchronised AFM rather than STM, achieving angstrom-scale sub-molecular contrast.

## Open questions

- What are the per-operation yield and error rate of mechanosynthetic donation and abstraction, and does either scale beyond a single model build site?
- Can the coupled sample-and-instrument digital twin framework, demonstrated for amplitude-modulation scanning probe microscopy, be transferred to STM where tip state is unknown and drifts?
- Does the proposed QPI tomography of the density matrix and quantum geometric tensor with unpolarised tips survive experimental test, and on which materials?
- Is THz-STM able to resolve Floquet gaps and edge states experimentally, as the nonequilibrium Green's function treatment predicts?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
