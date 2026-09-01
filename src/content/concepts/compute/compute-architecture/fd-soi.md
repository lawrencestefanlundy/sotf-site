---
type: concept
slug: fd-soi
canonical_name: FD-SOI
aliases:
- fdsoi
kind: technology
parent_concepts:
- compute
- compute-architecture
related_concepts: []
sources:
- '[[2026-06-22-beyond-cmos-device-layer-research]]'
- '[[2024-eu-chips-act-final-text]]'
- '[[2026-08-03-spad-single-photon-market-scan]]'
- '[[2026-06-04-globalfoundries-emram-22fdx-availability]]'
- '[[2026-06-15-gf-investor-day-2026]]'
- '[[2026-05-21-gf-quantum-technology-solutions]]'
frontier:
- Is there an FD-SOI node below 22nm on any foundry roadmap, or is 22FDX/28nm the terminal generation for the platform?
- What is the measured power, area and RF advantage of 22nm FD-SOI against bulk 28nm and a comparable FinFET node for the always-on and edge-AI sockets it is being marketed into?
- Will cryogenic behaviour become a supported, qualified PDK corner on FDX, or does each design team have to repeat its own 4 K characterisation as CryoZip did?
- Does eMRAM/ReRAM on FDX win the post-eFlash embedded memory socket against GF's own FinFET and BCD eNVM offerings, or does FD-SOI lose its lead-platform status as the portfolio spreads?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 23
last_reorg_date: '2026-05-13'
scorecard:
  viability: 5
  drivers: 4
  novelty: 2
  diffusion: 3
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
sources_7d: 1
sources_30d: 4
recent_mentions:
- slug: 2026-08-03-spad-single-photon-market-scan
  title: SPAD / single-photon detector market scan — incumbent structure and company cohort
  date: '2026-08-03'
  kind: web
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-15-gf-investor-day-2026
  title: GlobalFoundries Investor Day 2026 (presentation)
  date: '2026-06-15'
  kind: web
- slug: 2026-06-04-globalfoundries-emram-22fdx-availability
  title: GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform
  date: '2026-06-04'
  kind: web
- slug: 2026-05-21-gf-quantum-technology-solutions
  title: GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing
  date: '2026-05-21'
  kind: web
- slug: 2024-eu-chips-act-final-text
  title: European Chips Act — Regulation (EU) 2023/1781
  date: '2023-09-20'
  kind: web
neighbors: []
---
**FD-SOI is a planar CMOS process family built on a thin silicon layer over a buried oxide, sold by non-leading-edge foundries as a low-leakage, RF- and analog-friendly alternative to bulk CMOS and FinFET, and it has quietly become the default substrate for always-on edge silicon, embedded non-volatile memory and cryogenic quantum control chips.**

## Summary

FD-SOI (fully depleted silicon-on-insulator) is a manufacturing platform rather than a device concept. The transistor channel sits in a very thin silicon film separated from the bulk wafer by a buried oxide, so the channel is fully depleted without heavy doping and the substrate under the channel remains electrically accessible. The commercial instances that appear in the sources are GlobalFoundries' 22FDX (22nm FD-SOI) and Samsung's 28nm FD-SOI, with ST and GlobalFoundries running FD-SOI specialty work at Crolles under EU Chips Act alignment **2024 Eu Chips Act Final Text**.

The practical consequences show up in the research literature. Because the PDK exposes transistor substrate terminals, designers can inject and measure substrate noise directly, which is how a 22nm FD-SOI ring VCO was used to characterise through-silicon-via coupling in 3D-IC stacks, yielding a -35.2 dBc sideband spur under a 1 GHz, 0.5 Vpp aggressor. The same platform is the vehicle for leakage-dominated always-on logic research, where feedforward leakage suppression logic is being explored specifically in FDSOI to cut standby power in the always-on domain of event-driven wearables and IoT devices. It is also where low-bit LLM accelerators are being prototyped: the AdaMX adaptive microscaling accelerator was implemented as a 22nm FD-SOI prototype.

Two commercial anchors matter more than the papers. First, embedded non-volatile memory: Samsung has mass-produced eMRAM on 28nm FD-SOI since 2019 and GlobalFoundries put eMRAM into production on 22FDX in February 2020, using perpendicular-MTJ STT-MRAM licensed from Everspin, in 2 Mb to 32 Mb macros with >10-year retention at 125 °C and survival through 260 °C solder reflow <sup class="ref"><a href="https://www.design-reuse.com/news/3730-globalfoundries-announces-availability-of-embedded-mram-on-leading-22fdx-fd-soi-platform/" title="GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform" rel="noopener">ref</a></sup>. GF's 2026 investor material lists a broad eNVM portfolio (eMRAM, ReRAM, Flash) across FDX, FinFET and BCD, with FDX as the lead platform, framed around "autonomous secure always-on AI-enabled IoT edge devices" and 39B+ connected IoT devices by 2030 <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>. Second, cryogenics: GF states its FDX platform delivers the cryogenic CMOS used for sensing, control and readout in quantum systems, built on more than a decade of US Government-partnered work, and has a $375M Department of Commerce letter of intent tied to a ~1% strategic equity stake <sup class="ref"><a href="https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/" title="GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing" rel="noopener">ref</a></sup>. Academic work corroborates the cryo path: CryoZip was implemented in 22nm FDSOI characterised at 4 K.

The deciding parameters are not transistor physics but platform economics: which nodes carry FD-SOI, which eNVM and RF options are qualified on them, whether the PDK exposes the back-gate/substrate for designers who want it, and whether cryogenic characterisation becomes a supported PDK corner rather than a one-off measurement campaign.

## Viability (5/5)

This is not a question of whether it works. Samsung has mass-produced eMRAM on 28nm FD-SOI since 2019 and GlobalFoundries has had eMRAM in production on 22FDX since February 2020, with published macro sizes, retention and reflow specs <sup class="ref"><a href="https://www.design-reuse.com/news/3730-globalfoundries-announces-availability-of-embedded-mram-on-leading-22fdx-fd-soi-platform/" title="GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform" rel="noopener">ref</a></sup>. GF's own 2026 investor deck lists FDX as a lead platform across its eNVM portfolio <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>.

**TLDR: In volume production at two foundries with productised embedded memory and multiple independent silicon-level design efforts.**

## Drivers (4/5)

Supply: FD-SOI is the core of a deliberate "feature-rich, not node-leading" specialty-foundry position at GlobalFoundries, organised in its 2026 investor material around Physical AI and IoT edge devices <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>. Public money reinforces it: ST/GlobalFoundries Crolles is listed as an FD-SOI specialty project aligned with the European Chips Act, which mobilised ~€43B public and private against a 20%-of-global-production target for 2030 **2024 Eu Chips Act Final Text**, and GF's quantum business carries a $375M Department of Commerce letter of intent with a ~1% equity stake <sup class="ref"><a href="https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/" title="GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing" rel="noopener">ref</a></sup>.

Demand: three distinct pulls are documented. Embedded non-volatile memory, where 28/22nm is the last node for embedded flash and eNVM (MRAM/ReRAM/FeRAM) is the stated migration path, with FDX carrying both eMRAM and ReRAM <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>. Always-on edge devices where leakage in the always-on domain, not active energy, is the bottleneck. And cryogenic control and readout for quantum systems, where GF names Diraq, Equal1, Google Quantum AI, Microsoft, NVIDIA, PsiQuantum and Quantinuum as partners or customers <sup class="ref"><a href="https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/" title="GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing" rel="noopener">ref</a></sup>.

**TLDR: Foundry strategy and state subsidy on the supply side; edge AI, embedded NVM and quantum control on the demand side.**

## Novelty (2/5)

FD-SOI is not new: 28nm FD-SOI eMRAM has been in mass production since 2019 and 22FDX since 2020. The differentiators visible in the sources are qualitative. The PDK exposes transistor substrate terminals on RF devices, which is what made controlled substrate-noise injection possible in the TSV study. FDSOI is treated as the enabling process for feedforward leakage suppression logic in always-on domains, as against the HVT/UHVT bulk approach. And it is the platform GF asserts delivers cryogenic CMOS for quantum sensing, control and readout <sup class="ref"><a href="https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/" title="GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing" rel="noopener">ref</a></sup>, corroborated by 22nm FDSOI being characterised at 4 K in academic work.

What the sources do not contain is a number. There is no measured power, area, RF or variability comparison of FD-SOI against bulk 28nm or against a comparable FinFET node in any supplied source, and the large memory ratios that do appear (~1000× faster write, ~1/400 write energy) belong to eMRAM versus eFlash, not to FD-SOI versus anything. The score reflects a mature, differentiated but unquantified platform, not a breakthrough.

**TLDR: A decade-old platform with genuinely useful differentiators, but the sources contain no quantified head-to-head against bulk CMOS or FinFET.**

## Diffusion (3/5)

Diffusion is already underway in the segments where FD-SOI's options matter: two foundries in production on FD-SOI eMRAM, a productised 22FDX eMRAM offering with automotive-relevant reflow and retention specs <sup class="ref"><a href="https://www.design-reuse.com/news/3730-globalfoundries-announces-availability-of-embedded-mram-on-leading-22fdx-fd-soi-platform/" title="GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform" rel="noopener">ref</a></sup>, European specialty capacity being funded at Crolles **2024 Eu Chips Act Final Text**, and an unusually broad set of academic groups designing on 22nm FD-SOI across RF, digital accelerator, always-on logic and cryogenic domains.

The barriers are structural rather than technical. The supplied sources name only a handful of FD-SOI suppliers (GlobalFoundries, Samsung, ST/Crolles), so multi-sourcing is hard; the SPAD scan illustrates the general risk of single-foundry dependence in specialty silicon and treats second-sourcing onto GlobalFoundries as a structural necessity rather than a nice-to-have. GF also spreads its eNVM portfolio across FinFET and BCD as well as FDX <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>, and TSMC's Dresden build is described as 28/22nm plus 16/12nm specialty **2024 Eu Chips Act Final Text**, so FD-SOI competes for the same designs against non-SOI specialty options. No source shows an FD-SOI node below 22nm, which caps the platform's reach into higher-performance sockets.

**TLDR: Real production and a live design ecosystem, but a narrow foundry set, no visible node roadmap below 22nm, and competition from bulk and FinFET for the same sockets.**

## Impact (3/5)

The upside case is one of enablement across several markets rather than a single large one. On the IoT side, GF frames 39B+ connected devices by 2030 as "virtually all requiring eNVM", with FDX carrying that portfolio and the value proposition being standby/refresh power versus SRAM and I/O power versus external memory <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>; the embedded eNVM market anchor in the research synthesis is ~$2.6B by 2029, which is a real but bounded number. On the quantum side, the leverage is disproportionate to the wafer volume: if cryogenic control and readout must be manufactured somewhere, and FDX is the platform GF is positioning for it with US Government backing and a partner list spanning superconducting, spin, ion-trap, photonic and topological modalities, FD-SOI sits on the critical path of a much larger system <sup class="ref"><a href="https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/" title="GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing" rel="noopener">ref</a></sup>.

The ceiling is set by the platform's own positioning. It is explicitly a feature-rich, non-node-leading proposition <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>, so it will not capture datacentre-class compute value. Scored 3 because the sources support broad, durable relevance without any evidence of a step change in aggregate value creation.

**TLDR: High leverage inside specific sockets (IoT eNVM, always-on edge, cryo control) with no claim on the leading edge.**

## Timing Now (0-2yr)

The core platform and its flagship option have been in production for years: 28nm FD-SOI eMRAM since 2019 and 22FDX eMRAM since February 2020 <sup class="ref"><a href="https://www.design-reuse.com/news/3730-globalfoundries-announces-availability-of-embedded-mram-on-leading-22fdx-fd-soi-platform/" title="GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform" rel="noopener">ref</a></sup>. ReRAM is a named multi-platform GF offering with 22FDX as lead <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>. Nothing here requires waiting.

The newer directions are earlier but not distant. Cryogenic CMOS on FDX is being commercialised now, with a business launched in May 2026 and a $375M Department of Commerce letter of intent <sup class="ref"><a href="https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/" title="GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing" rel="noopener">ref</a></sup>, while the supporting circuit work is at the characterised-prototype stage as of mid-2026. Edge-AI accelerator and always-on logic work on 22nm FD-SOI is likewise at prototype stage in 2026. European specialty capacity tied to Chips Act projects lands later, with TSMC Dresden opening 2027 **2024 Eu Chips Act Final Text**.

**TLDR: Already shipping; the open question is the pace of the cryogenic and edge-AI extensions, not the platform.**

## Overrated or underrated? Underrated

FD-SOI reads as boring specialty silicon and is usually discussed as a node-race also-ran. The sources show something more useful: a single production platform that is simultaneously the lead vehicle for embedded MRAM and ReRAM as embedded flash hits its 28/22nm wall <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>, the process being characterised at 4 K for quantum error-correction hardware, the platform a foundry is putting behind a state-backed quantum manufacturing business <sup class="ref"><a href="https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/" title="GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing" rel="noopener">ref</a></sup>, and the process of choice for both RF substrate-noise work and always-on leakage suppression. Platforms that sit under several independently growing demand curves at once tend to be undervalued relative to whichever single application is fashionable.

The caveat is that this is a judgement about strategic position, not about measured superiority. No supplied source quantifies FD-SOI against bulk 28nm or a FinFET node on power, area or RF performance, and none shows a node below 22nm. If the differentiators turn out to be replicable on non-SOI specialty processes, notably GF's own FinFET and BCD eNVM lines <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>, the platform argument weakens to a wafer-cost argument. Anyone underwriting FD-SOI should be underwriting the sockets (eNVM, always-on, cryo control), not the substrate.

## Prediction

By 31 December 2028, at least one of GlobalFoundries' named quantum partners (Diraq, Equal1, Google Quantum AI, Microsoft, PsiQuantum, Quantinuum) will publicly disclose a cryogenic control or readout chip fabricated on GF's FDX FD-SOI platform.

## Evidence base

- Samsung has mass-produced eMRAM on 28nm FD-SOI since 2019; GlobalFoundries put eMRAM into production on 22FDX in February 2020.
- GF's 22FDX eMRAM is perpendicular-MTJ STT-MRAM licensed from Everspin, in 2 Mb-32 Mb macros, surviving 260 °C solder reflow with >10-year retention at 125 °C <sup class="ref"><a href="https://www.design-reuse.com/news/3730-globalfoundries-announces-availability-of-embedded-mram-on-leading-22fdx-fd-soi-platform/" title="GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform" rel="noopener">ref</a></sup>.
- On 21 May 2026 GF launched Quantum Technology Solutions, stating that its FDX FD-SOI platform delivers the cryogenic CMOS for quantum sensing, control and readout, backed by a $375M Department of Commerce letter of intent and a ~1% strategic equity investment <sup class="ref"><a href="https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/" title="GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing" rel="noopener">ref</a></sup>.
- CryoZip (1 July 2026) was implemented and evaluated in 22nm FDSOI characterised at 4 K, reporting up to 48x syndrome compression and 4-26x energy savings.
- A 22nm FD-SOI PDK exposing RF transistor substrate terminals enabled controlled TSV substrate-noise injection into a ring VCO, measuring a -35.2 dBc spur at 1 GHz, 0.5 Vpp and a low-pass coupling response from -20.2 dBc at 500 MHz to -33.1 dBc at higher frequency (28 May 2026).
- GF's Investor Day 2026 names a broad eNVM portfolio (eMRAM, ReRAM, Flash) across FDX, FinFET and BCD, framed on 39B+ connected IoT devices by 2030 and a feature-rich, non-node-leading specialty position <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>.
- The European Chips Act (Regulation 2023/1781, in force September 2023) lists ST/GlobalFoundries Crolles as an FD-SOI specialty project within a ~€43B public-plus-private mobilisation targeting 20% of global production by 2030 **2024 Eu Chips Act Final Text**.

## Open questions

- Is there an FD-SOI node below 22nm on any foundry roadmap, or is 22FDX/28nm the terminal generation for the platform?
- What is the measured power, area and RF advantage of 22nm FD-SOI against bulk 28nm and a comparable FinFET node for the always-on and edge-AI sockets it is being marketed into?
- Will cryogenic behaviour become a supported, qualified PDK corner on FDX, or does each design team have to repeat its own 4 K characterisation as CryoZip did?
- Does eMRAM/ReRAM on FDX win the post-eFlash embedded memory socket against GF's own FinFET and BCD eNVM offerings, or does FD-SOI lose its lead-platform status as the portfolio spreads?

---
*Assessment drafted 2026-08-31 from up to 10 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
