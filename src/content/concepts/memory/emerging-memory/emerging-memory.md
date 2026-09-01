---
type: concept
slug: emerging-memory
canonical_name: Emerging Memory
aliases:
- emerging memories
sources:
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2024-yole-emerging-memories-2024]]'
- '[[2026-06-22-beyond-cmos-device-layer-research]]'
- '[[2026-07-25-thoughts-on-ai-and-power]]'
verified: false
last_updated: '2026-08-31'
tags:
- concept
- stub
descendants:
- adc-bottleneck
- all-optical-switching
- analog-in-memory-compute
- analog-non-volatile-memory
- capram
- charge-domain-compute
- computational-storage
- cxl
- digital-in-memory-compute
- gain-cell-ram
- in-memory-computing
- magnetic-tunnel-junction
- magneto-optical
- memcapacitor
- memristor
- pcm-phase-change-memory
- photonic-memory
- processing-in-memory
- rram-reram
- sot-mram
- spintronics
- sram-cim
- st-fmr
- storage-class-memory
mention_count: 12
frontier:
- Does GF 22FDX FeFET convert its 2026-2027 design wins into publicly named volume customers, or does the timeline slip as sample-grade eNVM programmes often have?
- What end-to-end energy improvement does M3D BEOL cache scaling actually deliver for LLM serving beyond the 40MB L2 baseline, and at what capacity does the benefit saturate?
- Can analog crossbar arrays built from these devices demonstrate a workload harder than MNIST at array scale, given 10% device-to-device variation and 0.1% write noise?
- Does SOT-MRAM clear the endurance, density and integration bar for last-level cache, or does it remain a pilot-line technology as it has been through 2024-2026?
- Does continued scaling of BEOL M3D on-chip memory reduce total LLM serving energy, or does the saving from avoided off-chip HBM traffic saturate below the added array and thermal cost 2026 07 30 llmet enabling cross layer evaluation of emerging m3d memories for energy efficient llm serving?
- Does SOT-MRAM move from pilot to a qualified last-level-cache product at any foundry, and at what node and yield, given it was still R&D as of 2024-26 2026 06 22 beyond cmos device layer research?
- Does the 10% device-to-device variation measured on 300mm SOT-MRAM hold at full array scale, and does the 2-bit quantisation ceiling extend to workloads harder than MNIST 2026 06 05 evaluation of wafer scale sot mram for analog crossbar array?
- Does FeFET/HfO2-FeRAM actually reach ≥5% of embedded NV units by 2030, and which GF 22FDX design wins ship in the 2026-2027 window 2024 yole emerging memories 2024?
scorecard:
  viability: 3
  drivers: 4
  novelty: 4
  diffusion: 3
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
parent_concepts:
- memory
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-07-high-bandwidth-flash-the-full-report
  title: 'High Bandwidth Flash: The Full Report'
  date: '2026-07-07'
  kind: web
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
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
**Emerging memory is the family of non-volatile devices (MRAM, ReRAM/PCM, FeFET/FeRAM, ECRAM) being inserted where embedded flash stops scaling and where data movement dominates energy, with MRAM already in volume foundry production and the compute-in-memory applications still in the lab.**

## Summary

"Emerging memory" is shorthand for a set of device technologies that store state by means other than trapped charge in a floating gate or charge on a capacitor: resistance change (ReRAM/RRAM, phase-change memory), magnetic orientation (MRAM, in spin-transfer-torque and spin-orbit-torque variants), ferroelectric polarisation (FeFET, HfO2-based FeRAM), and electrochemical ion insertion (ECRAM). A recent survey chapter groups these alongside the incumbents (SRAM, DRAM, eDRAM, NAND/NOR flash) and extends the list to cryogenic options such as UTBB-SOI pseudo-static cells and Josephson-junction FET devices for superconducting and quantum platforms.

Two distinct commercial theses sit under the same label, and they should be judged separately. The first is substitution: embedded flash hits an economic scaling wall at 28/22nm, needing 6 to 8 extra mask steps against roughly 3 for MRAM, which is the stated reason foundries and IDMs are moving to alternative embedded non-volatile memory. This is already happening. Embedded MRAM is in volume production at TSMC 22nm (16nm qualifying, automotive 2025), Samsung 28nm FD-SOI (mass production since 2019, quoted at roughly 1000x faster write and around 1/400 the write energy of its own eFlash) and GlobalFoundries 22FDX (production February 2020).

The second thesis is architectural: because these devices are non-volatile, dense and often BEOL-compatible, they can be placed inside or next to the compute fabric and used to do arithmetic in place, collapsing the data movement that dominates modern workload energy. The research literature is concentrated here. Wafer-scale 300mm-compatible SOT-MRAM has been measured at 150% tunnel magnetoresistance ratio, 2 ns switching, sub-1V operation, 350 fJ per write, 0.1% write noise and 10% device-to-device variation, reaching 95% on MNIST after 2-bit quantisation-aware and noisy training. ECRAM is being proposed for in-memory continual learning at the edge, explicitly against the twin obstacles of noisy compute operations degrading training accuracy and incomplete architectural support for training. Monolithic 3D integration of cache at the back end of line is being simulated as a way to expand L2 beyond 40MB and cut off-chip HBM traffic during LLM serving.

The deciding parameters are mask-adder cost versus eFlash at a given node, endurance and retention at automotive temperature, device-to-device variation and conductance noise (which set achievable bit precision in analog arrays), and whether the workload tolerates non-idealities. The mass-spectrometry work is instructive: it reformulates search as binary hyperdimensional computing precisely so that ReRAM/PCM in-memory and 3D NAND/FeNAND in-storage processing can tolerate device-level non-idealities.

## Viability (3/5)

Judged as a category the answer is split, and averaging is misleading. Embedded MRAM is manufacturable today at three major foundries, with quantified advantage over the incumbent it replaces. FeFET on GF 22FDX is described as moving from sample-grade to volume design wins with customer adoption in 2026 to 2027 **2024 Yole Emerging Memories 2024**. That is a working technology, not a curiosity.

The analog and in-memory-compute path is earlier. SOT-MRAM is still R&D or pilot line as of 2024 to 2026 despite imec demonstrating integrated 300mm perpendicular SOT-MRAM with field-free switching aimed at last-level cache, and a 64kb beta-tungsten array switching in 1ns. The best array-level result reported in the sources is 95% on MNIST from measured devices with 2-bit quantisation and noise mitigation, which is a device-characterisation milestone rather than a system one. ECRAM work is explicit that IMC training accuracy is harmed by noisy operations and that resource-efficient training support is poor or incomplete. A 3 reflects a proven beachhead attached to an unproven main claim.

**TLDR: One member of the family is in volume production; the headline compute-in-memory use case is not.**

## Drivers (4/5)

Supply: 28/22nm is described as the last node for embedded flash, and the reason is economic rather than purely physical, 6 to 8 extra masks versus roughly 3 for MRAM. This is given as the explicit stated reason foundries and IDMs are migrating to alternative eNVM. Doped-HfO2 ferroelectricity makes FeRAM CMOS and BEOL compatible and sub-10nm scalable, unlike legacy PZT, which removes the historical blocker on that branch. A customer who wants embedded non-volatile storage below 28nm has no incumbent option, which is the strongest kind of driver.

Demand: the framing across the research sources is consistent. Conventional scaling is hitting power limits while machine learning, graph analytics and scientific computing demand more bandwidth, lower latency and better energy efficiency. LLM serving energy is presented as a system-level constraint driven by data movement between on-chip cache and off-chip HBM, and the mass-spectrometry workload is described as dominantly limited by reference data movement rather than computation. Held to 4 rather than 5 because the sources also show the incumbents holding: eFlash retains more than 50% of embedded NV at 40nm and above via 3D stacking **2024 Yole Emerging Memories 2024**.

**TLDR: Supply side has a hard forcing function in the eFlash scaling wall; demand side is data-movement energy.**

## Novelty (4/5)

Against embedded flash the margin is large and quantified, not directional: Samsung's 28nm FD-SOI eMRAM is cited at roughly 1000x faster write and around 1/400 the write energy of its own eFlash, at a lower mask adder. On the device metrics that matter for analog arrays, wafer-scale SOT-MRAM shows 150% TMR, 2 ns switching, sub-1V operation and 350 fJ writes, with device-to-device variation of 10% and write noise of 0.1%. FeFET adds a genuinely new capability rather than a better version of an old one, supporting logic-in-memory and compute-in-memory.

The boundary matters as much as the margin. Yole is direct that FeFET does not displace HBM at the AI accelerator memory layer through 2030 **2024 Yole Emerging Memories 2024**. Where the pressure on the AI memory hierarchy is being answered commercially in the near term, it is by stacked NAND: High Bandwidth Flash is described as matching HBM4 stack read bandwidth at roughly 10x the capacity, with first memory samples expected from Sandisk in the second half of 2026 and inference devices in early 2027 <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>. Emerging NVM is a large improvement inside a bounded niche, not a general replacement for DRAM.

**TLDR: Roughly 1000x faster and ~400x lower write energy than the eFlash it replaces, but explicitly not a DRAM or HBM substitute.**

## Diffusion (3/5)

The trajectory in the only market-share source available is slow. FeFET plus HfO2-FeRAM go from under 0.5% of embedded NV units in 2024 to at least 5% in 2030, MRAM holds the embedded NV slot specifically where endurance binds, and eFlash keeps more than 50% at 40nm and above by adopting 3D stacking **2024 Yole Emerging Memories 2024**. Six years to 5% is adoption by attrition at the leading edge of the specialty nodes, not displacement. GF 22FDX FeFET volume customer adoption in 2026 to 2027 is the datable near-term event **2024 Yole Emerging Memories 2024**.

The barriers visible in the sources are foundry availability at the required node, endurance and qualification (TSMC 16nm eMRAM qualifying, automotive 2025), and for the compute-in-memory path a toolchain and algorithm problem rather than a device problem. Analog arrays only work when the workload is reformulated to tolerate noise, whether by quantisation-aware and noisy training or by recasting the algorithm into binary hyperdimensional primitives. That is per-application engineering, which is the classic diffusion tax on novel hardware.

**TLDR: Real adoption is under way but the sources forecast emerging NVM as a minority of embedded non-volatile units even in 2030.**

## Impact (3/5)

On the substitution thesis the value is bounded and modest by semiconductor standards: embedded eNVM is put at roughly $2.6B by 2029. Winning most of that is a good specialty-foundry business, not an industry-reshaping one, and the same source's forecasts have emerging NVM sharing that pool with a still-dominant eFlash **2024 Yole Emerging Memories 2024**.

The larger claim is energy. If dense BEOL-integrated memory can hold enough working set on-chip to cut off-chip HBM traffic, it touches the cost structure of LLM serving directly, which is why LLMET was built to test whether continuously scaling on-chip memory with emerging technologies actually improves serving energy efficiency. The excerpt available shows the question posed and the framework validated, with L2 expansion studied from a 40MB baseline, but does not give the resulting efficiency numbers. Similarly, the edge continual-learning and open-modification-search work identifies large data-movement overheads without the sources here supplying end-to-end speedup or energy figures. A 3 records real but unquantified upside.

**TLDR: Direct market is small; the larger prize is data-movement energy in AI serving, which the sources model but do not yet quantify.**

## Timing Now (0-2yr)

For the substitution path the timing is already resolved: eMRAM has been in mass production since 2019 at Samsung 28nm FD-SOI and since February 2020 at GF 22FDX, with TSMC 16nm qualifying and automotive in 2025. The next datable checkpoint is GF 22FDX FeFET volume customer adoption in 2026 to 2027 **2024 Yole Emerging Memories 2024**, and the share milestone is 5% or more of embedded NV units by 2030 **2024 Yole Emerging Memories 2024**.

For the architectural path, later. SOT-MRAM remains pilot as of 2024 to 2026 even with 300mm field-free switching demonstrated and last-level cache as the stated target. Analog crossbar results are at the MNIST and single-device level, and M3D cache work is at the validated-simulator stage. Anyone underwriting AI memory economics in the next two years should be watching stacked NAND, where samples are dated to the second half of 2026 and devices to early 2027 <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>, rather than emerging NVM.

**TLDR: The embedded NVM substitution is happening now; in-memory compute on these devices is a 5-10 year question.**

## Overrated or underrated? Fairly rated

The category is priced about right in aggregate but wrongly on both halves. The embedded NVM story is underappreciated relative to how unglamorous it is: it has a forcing function (eFlash cannot economically scale past 28/22nm), a quantified advantage over the incumbent, and three foundries already shipping. It is also small, slow and confined to specialty nodes, with emerging NVM projected at 5% or more of embedded NV units by 2030 rather than a majority **2024 Yole Emerging Memories 2024**.

The compute-in-memory story is where over-enthusiasm lives. The device metrics are genuinely good, but every application paper in this set has to reshape its algorithm to survive device non-idealities, whether through 2-bit quantisation-aware and noisy training or through binary hyperdimensional reformulation, and the training-side support is described as poor and incomplete. The clearest discipline in the sources is Yole's statement that FeFET does not displace HBM at the accelerator memory layer through 2030 **2024 Yole Emerging Memories 2024**. Treat emerging memory as a specialty-foundry and edge-inference story with a long option on the memory hierarchy, not as an answer to the AI memory bottleneck this decade.

## Prediction

By 31 December 2027, embedded MRAM and FeFET will remain the only emerging non-volatile memories in named volume foundry production, with SOT-MRAM still at R&D or pilot stage rather than shipping as last-level cache.

## Evidence base

- Embedded MRAM is in volume production at Samsung 28nm FD-SOI since 2019 (cited at roughly 1000x faster write and around 1/400 the write energy of its own eFlash), GF 22FDX since February 2020, and TSMC 22nm with 16nm qualifying and automotive in 2025.
- 28/22nm is described as the last node for embedded flash, requiring 6 to 8 extra masks versus roughly 3 for MRAM, and this economics is the stated reason for the migration to emerging eNVM.
- FeFET plus HfO2-FeRAM are forecast to grow from under 0.5% of embedded non-volatile memory units in 2024 to at least 5% in 2030, while eFlash retains more than 50% at 40nm and above and FeFET does not displace HBM through 2030 **2024 Yole Emerging Memories 2024**.
- Wafer-scale 300mm-compatible SOT-MRAM measured at 150% TMR, 2 ns switching, sub-1V operation, 350 fJ, 0.1% write noise and 10% device-to-device variation, reaching 95% on MNIST with 2-bit quantisation-aware and noisy training (published 29 October 2025).
- SOT-MRAM remained R&D or pilot rather than volume as of 2024-2026, with imec showing integrated 300mm perpendicular SOT-MRAM with field-free switching for last-level cache and a 64kb beta-tungsten array switching in 1ns.
- A cross-platform survey published 21 July 2026 found reference data movement, not computation, dominates open modification search, and had to use a binary hyperdimensional formulation to tolerate device-level non-idealities on ReRAM/PCM and 3D NAND/FeNAND architectures.
- High Bandwidth Flash, a NAND stack with HBM4-class read bandwidth at roughly 10x capacity, is expected to sample from Sandisk in the second half of 2026 with inference devices in early 2027 <sup class="ref"><a href="https://www.chipstrat.com/p/high-bandwidth-flash-the-full-report" title="High Bandwidth Flash: The Full Report" rel="noopener">ref</a></sup>.

## Open questions

- Does GF 22FDX FeFET convert its 2026-2027 design wins into publicly named volume customers, or does the timeline slip as sample-grade eNVM programmes often have?
- What end-to-end energy improvement does M3D BEOL cache scaling actually deliver for LLM serving beyond the 40MB L2 baseline, and at what capacity does the benefit saturate?
- Can analog crossbar arrays built from these devices demonstrate a workload harder than MNIST at array scale, given 10% device-to-device variation and 0.1% write noise?
- Does SOT-MRAM clear the endurance, density and integration bar for last-level cache, or does it remain a pilot-line technology as it has been through 2024-2026?

---
*Assessment drafted 2026-08-31 from up to 12 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
