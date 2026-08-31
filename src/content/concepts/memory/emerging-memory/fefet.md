---
type: concept
slug: fefet
canonical_name: FeFET (Ferroelectric FET)
aliases:
- ferroelectric fet
- ferroelectric field-effect transistor
- fe-fet
parent_concepts:
- feram
related_concepts:
- feram
- rram-reram
- charge-domain-compute
- in-memory-computing
- embedded-non-volatile-memory
sources:
- '[[2024-yole-emerging-memories-2024]]'
- '[[2026-06-22-beyond-cmos-device-layer-research]]'
- '[[2025-26-lapedus-next-gen-ferroelectric-memory]]'
frontier:
- Do the reported 10^12-cycle endurance and 1000 s / 85 C retention figures survive full qualification across process corners and 150 C automotive conditions, or are they best-die demonstrator numbers?
- Can positive-Vt engineering (for example ferroelectric layer thinning) eliminate NOR-array sneak current without destroying the memory window, and what does that do to write voltage?
- Did the GF 22FDX FeFET volume adoption expected in 2026 to 2027 actually happen as a FeFET, or was the productised cell replaced by 1T1C FeRAM?
- In heterogeneous PIM, does FeFET hold its tier once real array non-idealities and write energy are substituted for simulated device models?
- Can HfO2 FeFET endurance and retention reach the bar for compute-in-memory (not just eNVM) at scale?
last_updated: '2026-08-31'
tags:
- concept
mention_count: 14
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2025-26-lapedus-next-gen-ferroelectric-memory
  title: Next-Gen Ferroelectric Memory Still A Work In Progress
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2024-yole-emerging-memories-2024
  title: Yole Group — Emerging Non-Volatile Memories 2024
  date: '2024-10-15'
  kind: web
neighbors:
- slug: feram
  name: FeRAM (Ferroelectric)
  path: /memory/mainstream-memory/feram/
  macro: memory
- slug: rram-reram
  name: RRAM / ReRAM
  path: /memory/emerging-memory/rram-reram/
  macro: memory
- slug: charge-domain-compute
  name: Charge-Domain Compute
  path: /compute/non-conventional/charge-domain-compute/
  macro: compute
- slug: in-memory-computing
  name: In-Memory Computing
  path: /memory/emerging-memory/in-memory-computing/
  macro: memory
- slug: embedded-non-volatile-memory
  name: Embedded Non-Volatile Memory
  path: /memory/emerging-memory/embedded-non-volatile-memory/
  macro: memory
---
**FeFET stores a bit as the remanent polarisation of a ferroelectric gate layer that shifts a transistor's threshold voltage, giving a one-transistor non-volatile cell with non-destructive read; device metrics have improved sharply but as of mid-2026 there is no high-volume production and no reported design wins **2025 26 Lapedus Next Gen Ferroelectric Memory**.**

## Summary

A ferroelectric field-effect transistor (FeFET) is an ordinary transistor with a ferroelectric layer inserted into the gate stack. Applying a gate voltage above the coercive field flips the layer's remanent polarisation, and that polarisation screens or reinforces the channel charge, shifting the device threshold voltage. The stored bit is read by sensing whether the transistor conducts at a given gate bias, so the read is non-destructive and does not disturb the state. Because the storage element is inside the gate rather than a separate capacitor or resistor, a cell can in principle be a single transistor, which is the density argument. The technology became interesting again when ferroelectricity was found in doped hafnium oxide, which unlike legacy PZT is compatible with CMOS and back-end-of-line processing and scales below 10 nm.

The parameters that decide FeFET are memory window (the Vt separation between polarisation states, which sets sensing margin), endurance (polarisation fatigue and gate-stack degradation under write cycling), retention at temperature, write voltage and speed, and array-level read margin. Recent device results claim the endurance ceiling has moved up substantially: an oxide-semiconductor-channel BEOL FeFET reported at 40 uA/um drive, 30 ns operation, 1000 s retention at 85 C and 10^12 cycles, and an IGZO-channel FeFET reported at >1.6 V memory window, >10^12 cycles and 20 ns operation **2025 26 Lapedus Next Gen Ferroelectric Memory**. Array design work identifies the remaining problems as writability and sneak current: in NOR-type IGZO FeFET arrays the negative programmed-state threshold voltage creates sneak paths that eat the sensing margin unless the ferroelectric is thinned or the Vt window is otherwise shifted positive, and read margin, not process, limits 3D FeNOR stacking density.

Two application vectors dominate the literature. The first is embedded non-volatile memory to replace embedded flash, which stops scaling around 28/22 nm for cost rather than physics reasons, plus dense BEOL RAM: an IGZO FeFET NOR bitcell has been projected down to roughly 0.016 um2, equivalent to a 10-transistor SRAM area at 7 nm ground rules, with sub-5 ns random access. The second is compute-in-memory, where FeFET appears repeatedly as one device option alongside ReRAM, PCM, MRAM and SRAM in heterogeneous processing-in-memory accelerators.

A separate research line uses the FeFET geometry as a measurement tool rather than a memory: sliding ferroelectricity in CVD-grown 3R-stacked WSe2 bilayers probed through a graphene ferroelectric-FET, where graphene senses polarisation-induced charge modulation and the study focuses on how structural disorder and multi-domain kinetics degrade switching. That is a different materials family from hafnia and should not be read as evidence about product-grade FeFET.

## Viability (3/5)

The strongest evidence is device-level. Reported FeFETs now reach 10^12 write cycles with 20 to 30 ns operation, 1000 s retention at 85 C and >1.6 V memory windows, above the prior 10^8 to 10^10 demonstrator frontier **2025 26 Lapedus Next Gen Ferroelectric Memory**. That removes the single objection that historically disqualified FeFET from anything but read-dominated tiers. The same survey is blunt that this is sampling and R&D: no high-volume production and no reported design wins as of mid-2026, and the leading oxide-channel FeFET is not offered as a foundry service to third parties. Note that this survey is a low-tier source; the specific numbers should be treated as claims from vendor demonstrators, not qualified product specifications.

**TLDR: Device metrics now clear the historic endurance objection, but arrays still fight writability and read margin and nothing is in volume production.**

## Drivers (4/5)

On the supply side the forcing function is external to FeFET: embedded flash stops at 28/22 nm on economics, needing 6 to 8 extra masks against roughly 3 for MRAM, which is the explicit stated reason foundries and IDMs are moving to emerging non-volatile memory. Hafnia ferroelectrics are CMOS and BEOL compatible and scale below 10 nm, so a FeFET can be built above the logic in the back end rather than consuming front-end area. Yole projects FeFET plus HfO2-FeRAM rising from under 0.5% of embedded non-volatile memory units in 2024 to at least 5% by 2030 **2024 Yole Emerging Memories 2024**, which is real growth from a negligible base rather than a takeover.

On the demand side, the pull is explicitly AI memory hierarchy. The DTCO case is framed around read-dominated AI memory tiers, on-chip BEOL RAM, hybrid-bonded memory chiplets and monolithic 3D FeNOR storage-class memory. Architecture work pulls the same way: heterogeneous PIM accelerators that mix FeFET with ReRAM, PCM, MRAM and SRAM report up to 3.8x energy efficiency and 6.8x compute efficiency over existing PIM architectures, and a 3D chiplet design pairs FeFET non-volatile chiplets with DRAM volatile chiplets for mixture-of-experts inference. The demand is architectural interest, not purchase orders, but it is broad and consistent across independent groups.

**TLDR: Supply push from the embedded-flash scaling wall and BEOL compatibility; demand pull from read-dominated AI memory tiers and compute-in-memory.**

## Novelty (3/5)

The comparisons the sources support are specific. Against embedded flash, FeFET wins on node reach and mask count, since flash is capped at 28/22 nm on cost. Against SRAM, an IGZO FeFET NOR bitcell is projected to a 10-transistor-SRAM-equivalent area of about 0.016 um2 at 7 nm ground rules while holding sub-5 ns random access, and a 4T differential bit-cell of two cross-coupled FeFETs plus two access transistors is smaller than a 6T SRAM cell and needs no backup-and-restore step, at 0.13 uW store power and 2 ns store time. Against legacy PZT ferroelectrics, hafnia is the enabling difference: CMOS and BEOL compatible, sub-10 nm scalable.

The reason this is a 3 rather than a 4 is that FeFET's real competitors are not flash. Embedded MRAM is already in volume production at 22 nm and 28 nm across three major foundries and holds the embedded slot where endurance binds **2024 Yole Emerging Memories 2024**. More awkwardly, the novelty of hafnia ferroelectricity can be captured by a capacitor cell instead: the productised 22FDX ferroelectric work is a 1T1C FeRAM, not a FeFET, operating sub-1 V at 8 nm film thickness with stable retention at 150 C **2025 26 Lapedus Next Gen Ferroelectric Memory**. FeFET's distinct claims, the 1T cell and non-destructive threshold-voltage read, are genuine, but the margin over the nearest ferroelectric alternative is not quantified anywhere in these sources.

**TLDR: Better than embedded flash on scaling and better than SRAM on area, but its closest rivals are MRAM in production and 1T1C hafnia FeRAM, which is being productised instead.**

## Diffusion (2/5)

The adoption picture is the weakest part of the case. As of mid-2026 there is no high-volume FeFET production and no reported design wins; the best-performing oxide-channel FeFET is not offered as a foundry service to third parties; the ferroelectric technology actually integrated at 22FDX is capacitor-based FeRAM rather than FeFET; and Micron and SK Hynix are exploring vertical ferroelectric NAND but not commercialising it, prioritising demand for existing products **2025 26 Lapedus Next Gen Ferroelectric Memory**. That last point matters: incumbent memory makers have no idle capacity motive to switch.

The sources conflict here and the conflict is informative. Yole's 2024 report expects GF 22FDX FeFET to reach volume customer adoption in 2026 to 2027 **2024 Yole Emerging Memories 2024**, while the 2026 device survey reports no design wins and characterises the GF 22FDX ferroelectric product line as 1T1C FeRAM **2025 26 Lapedus Next Gen Ferroelectric Memory**. Either the roadmap slipped or the productised cell changed shape. Beyond availability, the barriers are the usual ones for a new eNVM: it must be qualified in a foundry PDK with compact models and reliability data before any fabless customer will design against it, and the architecture papers that assume FeFET arrays are simulation studies that cannot be built on merchant silicon today. Ceiling expectations are modest even on the bull case: at least 5% of embedded non-volatile units by 2030, shared with hafnia FeRAM **2024 Yole Emerging Memories 2024**.

**TLDR: No design wins, no merchant foundry offering, and the two sources disagree on whether even one productisation path exists.**

## Impact (3/5)

The upside has a defined shape. If FeFET reaches production it takes share in embedded non-volatile memory where flash has stopped scaling, in BEOL RAM and hybrid-bonded memory chiplets, and in monolithic 3D storage-class memory, against an embedded eNVM market sized at roughly 2.6 billion dollars by 2029. The compute-in-memory upside is larger in efficiency terms than in revenue: a FeFET Bayesian inference engine reports 185 TOPS/W/mm2 with a 640 aJ per-sample Gaussian random number generator that performs no writes during inference, the kind of number that only a non-volatile threshold device with cheap stochasticity produces.

What caps the score is that the sources close off the biggest market directly: FeFET does not displace HBM at the AI accelerator memory layer through 2030 **2024 Yole Emerging Memories 2024**, and eFlash retains over 50% of embedded non-volatile memory at 40 nm and above via 3D stacking **2024 Yole Emerging Memories 2024**. In the heterogeneous PIM architectures where FeFET performs best, it is one tier among several rather than the substrate. That is a valuable specialty position, not a platform shift.

**TLDR: Real value in embedded NVM and compute-in-memory, but the sources explicitly rule out the largest prize.**

## Timing Soon (2-5yr)

The endurance and speed objections that held FeFET back appear to be answered at device level already, with 10^12 cycles and 20 to 30 ns operation reported **2025 26 Lapedus Next Gen Ferroelectric Memory**. What has not happened is productisation: no volume production and no design wins in mid-2026, and no third-party foundry offering of the best-performing variant **2025 26 Lapedus Next Gen Ferroelectric Memory**. Yole's expectation of volume customer adoption at 22FDX in 2026 to 2027 **2024 Yole Emerging Memories 2024** is the earliest credible date in the sources and it is already in tension with the 2026 device survey.

A reasonable reading is that first meaningful embedded FeFET revenue lands in the second half of this decade, consistent with the projection of at least 5% of embedded non-volatile units by 2030 for FeFET and hafnia FeRAM together **2024 Yole Emerging Memories 2024**. Compute-in-memory FeFET deployment is later still, because the architecture work is simulation on devices no one can buy, and 3D FeNOR density is currently limited by read margin rather than manufacturing.

**TLDR: Device physics is largely there now; qualified merchant availability and first design wins are the 2 to 5 year question.**

## Overrated or underrated? Fairly rated

FeFET is neither hype nor a lab curiosity. The physics case is solid, the hafnia gate stack is genuinely BEOL and CMOS compatible, the endurance ceiling has moved up by two to four orders of magnitude in reported demonstrators **2025 26 Lapedus Next Gen Ferroelectric Memory**, and the density arguments against SRAM are quantified. Equally, the market forecast in the sources gives it a low single-digit unit share of embedded non-volatile memory by 2030 shared with FeRAM, and explicitly excludes the AI accelerator main-memory layer **2024 Yole Emerging Memories 2024**. Those two positions are consistent with each other, which is what fairly rated means.

The one place the market is mispricing is the gap between the architecture literature and merchant silicon. FeFET appears as a standard device option in PIM and chiplet accelerator studies on the strength of assumed array behaviour, while the array-level work points at sneak current, writability and read margin as unresolved and the productisation record is empty **2025 26 Lapedus Next Gen Ferroelectric Memory**. Take FeFET seriously as an embedded non-volatile and read-dominated BEOL memory candidate; discount any accelerator projection whose energy numbers depend on frequent FeFET writes.

## Prediction

By 31 December 2027 no merchant foundry will list a 1T FeFET embedded non-volatile memory as a generally available third-party PDK option; productised hafnia ferroelectric memory at 22FDX-class nodes will remain capacitor-based 1T1C FeRAM.

## Evidence base

- Mid-2026: ferroelectric memory across the field is at sampling and R&D stage with no high-volume production and no reported design wins **2025 26 Lapedus Next Gen Ferroelectric Memory**.
- Reported FeFET device metrics: oxide-semiconductor-channel BEOL FeFET at 40 uA/um ION, 30 ns operation, 1000 s retention at 85 C and 10^12 cycles; IGZO FeFET at >1.6 V memory window, >10^12 cycles, 20 ns **2025 26 Lapedus Next Gen Ferroelectric Memory**.
- The 22FDX-integrated ferroelectric product is a 1T1C FeRAM, not a FeFET, at sub-1 V with 8 nm film and stable 150 C retention **2025 26 Lapedus Next Gen Ferroelectric Memory**.
- Yole 2024: FeFET plus HfO2-FeRAM go from under 0.5% of embedded NV units in 2024 to at least 5% by 2030; GF 22FDX FeFET volume adoption expected 2026 to 2027; FeFET does not displace HBM through 2030 **2024 Yole Emerging Memories 2024**.
- April 2026 DTCO study: IGZO FeFET NOR bitcell scalable to about 0.016 um2 (10-transistor SRAM-equivalent) at 7 nm ground rules with sub-5 ns random access, but sneak current from negative program-state Vt penalises sensing margin and read margin limits 3D FeNOR stacking.
- June 2026: 4T differential FeFET bit-cell smaller than 6T SRAM, 0.13 uW store power, 2 ns store time, no backup-and-restore; and a write-free FeFET Bayesian engine at 185 TOPS/W/mm2 with 640 aJ per Gaussian sample.

## Open questions

- Do the reported 10^12-cycle endurance and 1000 s / 85 C retention figures survive full qualification across process corners and 150 C automotive conditions, or are they best-die demonstrator numbers?
- Can positive-Vt engineering (for example ferroelectric layer thinning) eliminate NOR-array sneak current without destroying the memory window, and what does that do to write voltage?
- Did the GF 22FDX FeFET volume adoption expected in 2026 to 2027 actually happen as a FeFET, or was the productised cell replaced by 1T1C FeRAM?
- In heterogeneous PIM, does FeFET hold its tier once real array non-idealities and write energy are substituted for simulated device models?

---
*Assessment drafted 2026-08-31 from up to 11 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
