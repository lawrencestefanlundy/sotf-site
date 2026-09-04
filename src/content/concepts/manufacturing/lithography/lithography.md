---
type: concept
slug: lithography
canonical_name: Lithography
aliases: []
kind: technology
parent_concepts:
- manufacturing
- lithography
related_concepts: []
sources:
- '[[2026-07-03-thats-a-learning-curve-mate-not-rsi]]'
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2026-04-17-state-of-the-future-friday-four-67c]]'
- '[[2026-06-05-recursive-until-the-power-bill]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2026-04-14-the-photonic-foundry-fallacy]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2026-06-19-the-housefab-always-wins]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2026-07-07-the-asml-killer]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2026-07-28-laser-on-a-chip-w-matt-crowley-scintil]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
scorecard:
  viability: 5
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 204
descendants:
- computational-lithography
- directed-self-assembly
- duv-immersion-lithography
- e-beam-lithography
- euv-light-sources
- high-na-euv-lithography
- lithography
- lithography-tools
- mask-blank-manufacturing
- maskless-lithography
- nanoimprint-lithography
- photonic-manufacturing
- photoresists
- two-photon-polymerization
- x-ray-lithography
- xolography
sources_7d: 0
sources_30d: 7
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-28-laser-on-a-chip-w-matt-crowley-scintil
  title: Laser on a Chip w/ Matt Crowley @ Scintil Photonics
  date: '2026-07-28'
  kind: substack
- slug: 2026-07-09-in-die-microfluidic-cooling-sprint
  title: In-die microfluidic cooling — cluster research sprint
  date: '2026-07-09'
  kind: web
- slug: 2026-07-07-the-asml-killer
  title: The ASML Killer?
  date: '2026-07-07'
  kind: substack
- slug: 2026-07-03-thats-a-learning-curve-mate-not-rsi
  title: That’s a learning curve mate, not RSI
  date: '2026-07-03'
  kind: substack
- slug: 2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology
  title: IBM Debuts World's First Sub-1 Nanometer Chip Technology
  date: '2026-06-25'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-19-the-housefab-always-wins
  title: The House/Fab Always Wins
  date: '2026-06-19'
  kind: substack
neighbors: []
---
**Lithography is the set of techniques that define patterns on a substrate, and across the supplied evidence it is the step that sets cost per bit, device uniformity and yield for memory, CMOS qubit arrays, photonics and 3D micro-optics alike.**

## Summary

Lithography is pattern definition: transferring a designed geometry into a resist or mask layer so that subsequent etch, deposition or implant steps land where intended. The supplied sources span four distinct families. First, projection optical lithography, including EUV, used in high-volume 300 mm CMOS lines; one source characterises a 7x7 silicon MOS quantum dot array with 392 dots patterned by EUV lithography in a 300 mm CMOS process. Second, serial charged-particle and scanning-probe writing: electron-beam lithography combined with ion implantation for chip-scale optical data storage, AFM nano-oxidation to place quantum dots, and electrochemical AFM writing of sub-10 nm graphene nanoribbon FETs. Third, two-photon lithography and two-photon polymerisation, which write true 3D microstructures in a photoresist by nonlinear absorption at a focal voxel. Fourth, computational lithography: inverse mask optimisation that pre-distorts the drawn layout so the fabricated result matches intent.

The parameters that decide any lithography choice are resolution, throughput, cost per critical layer, and pattern fidelity, meaning how faithfully corners, sidewall angles and edge placement survive. Fidelity is not a cosmetic issue. A study of Ge2Sb2Te5 metasurfaces shows that trapezoidal sidewall deviations from the drawn rectangle degrade the quasi-BIC quality factor, with an inverse-quadratic scaling of Q with disorder amplitude in the loss-free limit. In inverse-designed photonics the same effect compounds through cascaded circuits, which is the stated reason inverse-designed devices underperform their simulations.

The economic parameter is mask count. A rigorous 3D NAND cost model shows that adding device layers does not monotonically reduce die cost per bit: because any deep etch has a non-zero taper angle, the cell pitch at the top of the stack grows linearly with layer count, so array footprint eventually rises with layers and die cost passes through a minimum **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. The same paper shows that a lithography-intensive layered approach using three critical masks per device layer can reach a smaller die and undercut the vertical-channel approach on total cost **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. Lithography steps are therefore a design variable to be traded, not simply a cost to be eliminated.

A fifth pattern in the evidence is displacement: moving the hard lithography off the awkward substrate. Silicon masks fabricated in commercial semiconductor foundries are microtransfer-printed onto diamond, replacing bespoke direct writing on diamond and yielding hundreds of quantum microchiplets with improved uniformity, yield and throughput.

## Viability (5/5)

There is no question of feasibility. EUV lithography is used inside a 300 mm CMOS process to pattern dense quantum dot arrays, with 392 dots characterised statistically and threshold voltage variability held below 63 mV standard deviation at the optimal 17 nm oxide. The 3D NAND cost analysis treats lithography as a costed, well-understood production step **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. Electron-beam lithography plus ion implantation delivers deterministic, multi-bit grayscale encoding over millimetre areas.

The emerging modalities are also past proof of principle, though at very different maturity. Two-photon lithography has produced centimetre-scale continuous 3D structures with grayscale voxel control using a DMD to temporally focus femtosecond pulses at above 10 kHz refresh, and TPL-patterned substrates have induced 2.2% biaxial strain in monolayer MoS2 stable over months. Scanning-probe writing reaches sub-10 nm graphene features and 51(28) nm placement accuracy for quantum dots, but as inherently serial techniques their viability claim is for research and small-volume use, not volume manufacturing.

**TLDR: Working in high-volume production and demonstrated across every emerging modality in the evidence set.**

## Drivers (4/5)

Demand is well evidenced and comes from several directions at once. AI systems scaling to multi-chiplet and wafer-level architectures have outpaced electrical interconnects, driving electronic-photonic integration and with it the need for fabrication-aware physical design and yield optimisation. Growth in global data generation is cited as the motivation for chip-fabricated optical storage using EBL. Quantum hardware needs uniform, reproducible patterning at scale, which is the explicit reason for using EUV in a CMOS line for spin qubit arrays and for shifting diamond photonics onto foundry-made masks. Memory cost per bit remains a direct commercial driver of lithography strategy **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**.

On supply the evidence is thin. None of the sources addresses lithography tool availability, exposure tool cost, resist or mask supply chains, or fab capacity, so nothing here supports a view on whether supply constrains adoption. The one supply-side signal is software rather than hardware: adoption of variable-dose TPP has been held back by a lack of slicer software and validated measurement methods, which one source addresses with an open-source slicer and a refractive index calibration methodology.

**TLDR: Strong, diverse demand pull; the sources say almost nothing about equipment supply or capex.**

## Novelty (3/5)

Lithography itself is not novel, so the question is what the new variants beat and by how much. Computational inverse lithography is established in electronics but the source states plainly that photonics lacks a systematic, flexible mask optimisation flow, and that calibrating fabrication models is costly and expertise-heavy, requiring repeated fabrication cycles. Filling that gap is a real novelty claim, extended to a full physical design flow including placement and routing. Mask transfer printing is novel against the incumbent of sequential direct lithography on diamond, claiming improved uniformity, yield and throughput, though the source gives no numeric margin.

In two-photon lithography the claimed advance is the first demonstration of true continuous 3D nanolithography with full-bandwidth data streaming, against prior parallel-exposure approaches whose practical rate on large parts was limited by toolpath, data transfer and stop-and-go stitching. Scanning-probe writing is offered as lower cost and simpler than photo and e-beam lithography for sub-10 nm graphene devices, but no throughput or cost comparison is given. The most contrarian novelty in the set is conceptual rather than technical: the demonstration that a lithography-intensive layered 3D memory, at three critical masks per device layer, can undercut a low-mask-count vertical-channel architecture on total cost **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**.

**TLDR: The base technology is mature; the genuinely new items are computational mask flows for photonics, mask transfer printing and continuous 3D writing, and the improvement margins are mostly unquantified.**

## Diffusion (3/5)

For mainstream projection lithography the barrier is not adoption but access and cost per critical layer, which the memory cost model treats as the central trade **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. For the newer branches the stated barriers are consistent across sources. Two-photon lithography is limited by practical fabrication rate on large structures, attributed to bandwidth mismatch between toolpath generation, data transfer and laser patterning, and to stop-and-go stitching. Variable-dose TPP has been held back by absent software and validation techniques, a high barrier of entry that an open-source slicer is intended to lower. Quality control is not solved either: static computer vision models cannot detect unseen defect classes or adapt to new part geometries, motivating few-shot and domain-adaptation frameworks for TPL inspection.

Metrology is a second gate. Recovering 3D surface geometry from SEM signals is hard enough that a neural field method is needed to resolve 478 nm layered features in two-photon lithography samples. For computational lithography in photonics the barrier is model calibration cost and the need for repeated fabrication cycles, which puts it out of reach of most designers today. Scanning-probe lithography, being serial and tip-based, has no diffusion path to volume in anything the sources show; its role is research prototyping and deterministic placement.

**TLDR: Projection lithography is already diffused; the direct-write and computational branches are gated by throughput, software, calibration and metrology.**

## Impact (4/5)

The clearest quantified impact is economic. The 3D NAND model shows die cost per bit does not fall monotonically with layer count and instead passes through a minimum, because top-of-stack cell pitch grows linearly with layers through the taper term 2·N_L(L_g + L_s)·tanθ; a lithography-intensive layered alternative can reach a smaller die and lower total cost **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. That reframes lithography spend as the lever on memory economics rather than a tax on it. In photonics, lithography-induced deviation is the stated cause of large optical response drift, low yield and the gap between simulated and fabricated performance for inverse-designed circuits, with a quantified mechanism in metasurfaces where Q scales inverse-quadratically with sidewall disorder amplitude.

Enabling impact is broad but mostly demonstrated at device rather than system level: 245-fold photoluminescence enhancement from AFM-positioned quantum dots in circular Bragg gratings, roughly 0.4 eV band gap tuning, about 25% of the intrinsic gap, in monolayer MoS2 strained on TPL-patterned substrates, hundreds of diamond quantum microchiplets from foundry masks, and 3D exchange-biased microwires built by combining two-photon lithography with sputtering. The sources do not quantify market or macroeconomic value, which is why this is not a 5.

**TLDR: In the domains the sources cover, lithography choice decides cost per bit, device uniformity and photonic yield outright.**

## Timing Now (0-2yr)

Projection lithography is in production and is already the cost and uniformity determinant in the applications shown, from EUV-patterned 300 mm qubit arrays to memory die cost modelling **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. Nothing here is waiting on a physics result.

The adjacent branches are converging on the practical layer rather than the physical one. In 2026 the published work is about slicers, calibration methods, inspection models, mask optimisation flows and SEM reconstruction. That is the profile of a field in the two-year tooling phase, not a decade-out research phase. The exception is scanning-probe lithography, where the sources show no throughput path and give no timing signal at all.

**TLDR: Mainstream lithography is already the deciding variable; the newer branches are in the software and metrology consolidation phase now.**

## Overrated or underrated? Fairly rated

Lithography's centrality is not in dispute and the evidence does not suggest anyone underestimates it. Two sub-claims inside the field are mispriced, however. The first is the assumption that architectures which reduce lithography steps automatically reduce cost. The 3D NAND analysis dismantles that for vertical-channel memory, showing a cost minimum in layer count driven by etch taper, and showing that three critical masks per device layer can win on total cost **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. Any roadmap that treats mask count as a pure cost to be minimised should be checked against that mechanism.

The second is that the binding constraint on the newer lithography modalities is no longer resolution. Two-photon lithography already writes centimetre-scale continuous 3D parts with grayscale voxel control; what limits it is data bandwidth, slicer software, inspection and metrology. Likewise the gap between simulated and fabricated inverse-designed photonics is a mask-flow and calibration problem, not an optics problem. Value in the next few years accrues to the software and metrology layer around lithography rather than to new exposure physics.

## Prediction

By 31 December 2028, at least one commercial silicon photonics foundry will offer a photonics-aware inverse lithography or mask optimisation option as a documented part of its PDK, closing the gap identified in.

## Evidence base

- November 2013: a rigorous 3D NAND cost model shows die cost per bit passes through a minimum in layer count because etch taper grows top-of-stack cell pitch linearly with layers, and that a layered approach using three critical masks per device layer can undercut vertical-channel on total cost **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**.
- 14 May 2026: a 7x7 silicon MOS quantum dot array patterned by EUV lithography in a 300 mm CMOS process yields 392 characterised dots, with threshold voltage variability below 63 mV standard deviation at an optimal 17 nm SiO2 thickness.
- 6 May 2026: room-temperature AFM nano-oxidation lithography positions GaAs quantum dots to 51(28) nm radial displacement, giving 245-fold photoluminescence enhancement in circular Bragg gratings with polarisation imbalance below 5%.
- 8 May 2026: in Ge2Sb2Te5 metasurfaces the quasi-BIC quality factor scales inverse-quadratically with the amplitude of trapezoidal lithography disorder in the loss-free limit, quantifying how sidewall fidelity rather than resolution sets device performance.
- 28 December 2025 (indexed 5 June 2026): line-illumination temporal focusing two-photon lithography using a DMD at above 10 kHz refresh demonstrates continuous, full-bandwidth 3D writing of centimetre-scale structures with grayscale voxel tuning.
- 27 January 2026 (indexed 5 June 2026): silicon masks made in commercial foundries and microtransfer-printed onto diamond produce hundreds of quantum microchiplets, shifting the demanding pattern-definition step off the diamond substrate and improving uniformity, yield and throughput.

## Open questions

- Does the layer-count cost minimum identified for vertical-channel 3D NAND still bind at current stack heights, and has the lithography-intensive layered alternative ever been costed against a modern process flow? **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**
- What throughput and cost per part does line-illumination temporal focusing two-photon lithography achieve against existing commercial TPL tools, in parts per hour rather than peak patterning rate? 
- How much fabrication data is needed to calibrate a photonics inverse lithography model to useful accuracy, and does the yield gain survive on a foundry PDK the designer cannot probe? 
- Does foundry mask transfer printing onto non-standard substrates such as diamond scale beyond hundreds of chiplets, and with what quantified yield relative to direct writing? 

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
