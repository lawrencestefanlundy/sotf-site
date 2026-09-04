---
type: concept
slug: co-packaged-optics
canonical_name: Co-Packaged Optics
aliases:
- cpo
kind: technology
parent_concepts:
- manufacturing
- packaging
related_concepts: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2026-04-17-state-of-the-future-friday-four-67c]]'
- '[[2026-06-05-recursive-until-the-power-bill]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2026-04-14-the-photonic-foundry-fallacy]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2026-07-28-laser-on-a-chip-w-matt-crowley-scintil]]'
- '[[2026-07-10-the-next-vc-meme-is]]'
- '[[2026-03-12-optical-displaces-copper-broadcom-ships-tomahawk-6-world-s]]'
- '[[2026-05-02-co-packaged-optics-2026-2036-idtechex]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-07-26-ai-backend-network-optics-2026]]'
- '[[2026-06-17-sjtu-ge-si-photodetector-110ghz-fowlp]]'
- '[[2026-06-15-gf-investor-day-2026]]'
- '[[2026-05-26-optical-displaces-copper-the-global-co-packaged-optics]]'
- '[[2026-04-15-semianalysis-isscc-2026]]'
- '[[2026-04-10-photonic-light-source-supply-co-packaged-optics-cpo-scaling]]'
- '[[2026-05-30-senko-gf-cpo-detachable-fiber]]'
- '[[2026-06-23-photonic-foundry-capacity-co-packaged-optics-is-not-delayed]]'
scorecard:
  viability: 4
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 68
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-28-laser-on-a-chip-w-matt-crowley-scintil
  title: Laser on a Chip w/ Matt Crowley @ Scintil Photonics
  date: '2026-07-28'
  kind: substack
- slug: 2026-07-26-ai-backend-network-optics-2026
  title: 'Dell''Oro: AI back-end switching past $100B by 2030, optical transport $16B in 2025'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-11-neutral-pdk-heterogeneous-integration-landscape
  title: Neutral PDK / EDA layer for heterogeneous photonic integration — landscape check (Scintil essay correction research)
  date: '2026-07-11'
  kind: web
- slug: 2026-07-10-the-next-vc-meme-is
  title: The Next VC Meme Is...
  date: '2026-07-10'
  kind: substack
- slug: 2026-07-02-semianalysis-ectc2026-advanced-packaging
  title: 'ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More'
  date: '2026-07-02'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
neighbors: []
---
**Co-packaged optics moves the optical transceiver out of the front-panel cage and into the same package as the switch or accelerator die, and after years as a research programme it is now entering commercial switch products, with NVIDIA citing early-2026 availability for Quantum-X InfiniBand CPO and 2H 2026 for Spectrum-X Ethernet CPO <sup class="ref"><a href="https://www.genaitech.net/p/nvidias-4b-cpo-bet-scaleout-first" title="NVIDIA's $4B CPO Bet: Scale-Out First, Scale-Up Later" rel="noopener">ref</a></sup>.**

## Summary

In a conventional data centre switch, electrical signals travel from the ASIC across the printed circuit board to a front-panel cage holding a pluggable optical transceiver, where they are converted to light. At 800G and 1.6T per port, those centimetres of copper trace become the dominant cost in power and signal integrity. Co-packaged optics (CPO) eliminates the journey: the photonic integrated circuit (PIC), containing modulators, photodetectors and wavelength multiplexers, is mounted on the same substrate, interposer or 3D stack as the switch or compute die, with fibre attached directly to the package. The argument for it is that copper interconnect is running out of headroom at high symbol rates, so introducing optics into the scale-up network becomes, in the words of one recent survey, no longer optional but essential.

The engineering is a packaging problem more than a photonics problem. The parameters that decide it are: fibre-to-chip coupling (grating couplers must cover wide wavelength ranges with low loss, a design problem now being attacked with neural-network-driven optimisation); modulator choice and its temperature behaviour; and thermal coupling between a hot logic die and a temperature-sensitive PIC. The last is the sharpest constraint. Micro-ring resonators, favoured for their compactness and natural fit with dense wavelength-division multiplexing, drift with temperature: analysis of TSMC's COUPE architecture cites a tolerance of around plus or minus 1.7 nm in resonant wavelength before bit error rate degrades measurably. That is why the field is simultaneously pursuing thermally robust modulator materials, with thin-film lithium tantalate shown to hold bandwidth and DC bias stability at 120°C (and a 10% reduction in Vπ at high temperature), positioning it for uncooled CPO operation.

There is no single winning device stack. Silicon photonics with germanium detectors provides the foundry base; thin-film lithium niobate has been heterogeneously integrated onto a foundry-compatible SiPh platform at imec for 320 Gb/s unamplified transmission with a 100 GHz Ge photodetector <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup>; barium titanate reached a 300mm high-volume-manufacturing-compatible integration process on silicon photonics in January 2026 <sup class="ref"><a href="https://www.imec-int.com/en/press/veeco-imec-develop-300mm-compatible-process-enable-integration-barium-titanate-silicon" title="Veeco and imec develop 300mm-compatible process to enable integration of barium titanate on silicon photonics" rel="noopener">ref</a></sup>; and VCSEL-based engines are argued to be the low-cost, low-latency, high-wall-plug-efficiency route for short-reach scale-up. Integration architectures are equally plural, from 2.5D optical interposers in SiON/Si carrying flip-chipped InP electro-absorption modulated lasers to 3D stacks inside 3.5D heterogeneous packages.

The honest counter-position within the field is that CPO is being treated as a component optimisation when it is an architectural commitment that redraws the boundary between photonics, electronics and system design, and that standardisation, serviceability and thermal-aware co-design, not device performance, will decide whether it moves from early deployment to widespread adoption.

## Viability (4/5)

The strongest evidence is commercial rather than academic: NVIDIA announced on 2 March 2026 early-2026 availability for Quantum-X InfiniBand CPO switches and 2H 2026 for Spectrum-X Ethernet CPO switches, behind a reported $4B commitment <sup class="ref"><a href="https://www.genaitech.net/p/nvidias-4b-cpo-bet-scaleout-first" title="NVIDIA's $4B CPO Bet: Scale-Out First, Scale-Up Later" rel="noopener">ref</a></sup>. That is a vendor-stated schedule rather than an audited shipment count, but it is the difference between a research programme and a product line. On the laboratory side, a 2.5D co-packaged optical I/O chipset on a SiON/Si interposer has been experimentally demonstrated as a 400 Gb/s single-fibre transceiver with clear eye diagrams, and a monolithic multidimensional silicon photonic engine has been measured above 1.8 terabit/s per wavelength.

What is not yet demonstrated is stable in-package thermal control at production scale. The +/- 1.7 nm micro-ring drift budget is tight, and the leading published mitigation, predictive firmware scheduling holding compensated CPO spectral drift below 0.36 nm (21% of the stated tolerance budget), is explicitly an engineering projection from pre-silicon characterisation awaiting validation. Higher-order modulation approaches that would push a CPO lane beyond PAM-4, such as microring-based offset-QAM-16 reaching 400 Gb/s at 9.65 dBm laser power, remain simulation on a foundry process rather than measured hardware. Score 4 for switch CPO; the compute-attached case would score lower on its own.

**TLDR: Switch-side CPO has announced product availability dates; the harder compute-side and thermal-control problems are still being solved on paper.**

## Drivers (4/5)

Demand is unambiguous and quantified. LightCounting forecasts LPO plus CPO ports exceeding 30% of total 800G and 1.6T ports deployed across 2026-2028 <sup class="ref"><a href="https://www.lightcounting.com/newsletter/en/march-2026-ethernet-optics-382" title="LightCounting: January 2025 Optics for AI Clusters report (March 2026 release)" rel="noopener">ref</a></sup>, and the wider silicon photonics market is projected at $9.6B by 2030 at 28% CAGR with transceivers holding the largest share <sup class="ref"><a href="https://www.wissenresearch.com/silicon-photonics-market/" title="Silicon Photonics Market - Wissen Research" rel="noopener">ref</a></sup>. The underlying pull is that AI workloads need distributed clusters to behave as a single computational unit, which requires interconnect reach and latency that copper cannot deliver at these rates.

Supply is the weaker side. CPO rides on the same advanced packaging infrastructure as AI accelerators, where TSMC CoWoS capacity is identified as the leading bottleneck for accelerator volume with expansion running through 2026, and Samsung X-Cube and Intel Foveros each represent roughly 30% of TSMC volume **2024 Yole Advanced Packaging 2024**. Component supply for the photonic layer looks healthier: multiple modulator platforms are reaching manufacturable form, including 300mm-compatible barium titanate on silicon <sup class="ref"><a href="https://www.imec-int.com/en/press/veeco-imec-develop-300mm-compatible-process-enable-integration-barium-titanate-silicon" title="Veeco and imec develop 300mm-compatible process to enable integration of barium titanate on silicon photonics" rel="noopener">ref</a></sup> and TFLN modulator PIC sales forecast at $0.75B by 2029 against $3B total silicon photonics chip sales <sup class="ref"><a href="https://www.lightcounting.com/newsletter/en/may-2024-silicon-photonics-linear-drive-pluggable-and-co-packaged-optics-291" title="Sales of Silicon Photonics chips will reach $3 billion by 2029" rel="noopener">ref</a></sup>. The binding constraint is package substrate and assembly capacity shared with the accelerators CPO is meant to serve.

**TLDR: Demand is the AI cluster bandwidth wall and copper's failure at high symbol rates; supply is constrained by advanced packaging capacity rather than photonics.**

## Novelty (3/5)

What CPO is better than is well identified: front-panel pluggable transceivers and the copper traces feeding them. The claimed advantages are energy per bit, spatial bandwidth density (shoreline density, the bandwidth achievable per millimetre of die edge) and latency, with the assertion that copper traces are simply inefficient at the required speeds. Where the supplied sources do quantify a gain, it tends to be within the photonic subsystem rather than against a pluggable baseline: eliminating power-hungry DSP and bulky discrete multiplexers in a monolithic engine is reported as a greater than 5,000-fold improvement on a stated metric relative to state-of-the-art DSP, alongside capacity above 1.8 Tb/s per wavelength.

The most striking quantified claim is architectural rather than component-level: a fibre delay-line memory design using co-packaged optics, multi-core fibre and all-optical regeneration is estimated to cut weight-delivery energy by over 70% versus traditional HBM3e configurations across 10,000 accelerators. That is a case-study evaluation, not a build. Score 3 rather than 4 because the sources here assert the CPO-versus-pluggable advantage far more often than they measure it, and because a credible strand of the field argues the community has been optimising device metrics that are not the ones limiting deployment.

**TLDR: Clearly better than copper at high rates and structurally better than pluggables on energy and shoreline density, but the sources give few head-to-head measured deltas.**

## Diffusion (3/5)

A pluggable transceiver that fails is swapped in the field in minutes. A co-packaged optical engine that fails may condemn the switch or accelerator package. The field's own review names standardisation, serviceability and thermal-aware co-design as decisive for whether CPO moves from early deployment to widespread adoption. Test and calibration is a second, less visible barrier: as PICs scale, testing depends on effective on-chip phase modulation, and the choice between thermal and carrier-based modulation forces trade-offs between speed, energy and tuning controllability with no universally correct answer. Fibre-to-chip coupling across wide wavelength ranges remains a hard design problem, with automated design tools still producing under 5% spectral error in only around 351 of roughly 1,000 test cases.

The adoption path visible in the sources is sequenced, not wholesale. NVIDIA's programme is characterised as scale-out first, scale-up later, with InfiniBand switches ahead of Ethernet <sup class="ref"><a href="https://www.genaitech.net/p/nvidias-4b-cpo-bet-scaleout-first" title="NVIDIA's $4B CPO Bet: Scale-Out First, Scale-Up Later" rel="noopener">ref</a></sup>. The LightCounting figure that matters most is a combined LPO plus CPO share above 30% of 800G and 1.6T ports for 2026-2028 <sup class="ref"><a href="https://www.lightcounting.com/newsletter/en/march-2026-ethernet-optics-382" title="LightCounting: January 2025 Optics for AI Clusters report (March 2026 release)" rel="noopener">ref</a></sup>: linear-drive pluggables are a genuine competing answer to the same power problem that requires none of the packaging upheaval, and the sources do not separate the two. Score 3: real deployment, contested share, unresolved operational model.

**TLDR: Serviceability, standardisation and test are the real barriers, and the first deployment wave is deliberately staged into scale-out before scale-up.**

## Impact (4/5)

The direct value is removing the interconnect ceiling on AI cluster scaling. Optical interconnect extends transmission distance and reduces latency such that distributed clusters can operate as a unified computational unit, which is precisely the constraint that currently bounds how large a coherent training or inference domain can be. On the financial side, the addressable market indicators are meaningful but not transformative on their own: $9.6B silicon photonics by 2030 <sup class="ref"><a href="https://www.wissenresearch.com/silicon-photonics-market/" title="Silicon Photonics Market - Wissen Research" rel="noopener">ref</a></sup> sits alongside chiplet-attributed packaging revenue growing from around $7.5B in 2024 to over $30B by 2030 **2024 Yole Advanced Packaging 2024**. The value captured by CPO components is small relative to the accelerator systems it unblocks.

The second-order impact is larger and more speculative. If optical I/O is cheap and dense enough inside the package, architectures that are currently impossible become arguable, including using recirculating fibre as delay-line memory for immutable LLM weights and eliminating redundant weight storage across ten thousand accelerators. That would touch the DRAM supply constraint directly. Score 4 rather than 5 because the demonstrated impact so far is a better switch, and the architecture-changing consequences remain case studies.

**TLDR: If in-package optics becomes routine it changes the unit of computation from the rack to the cluster, and potentially the memory hierarchy too.**

## Timing Now (0-2yr)

For network switches the timing question is essentially resolved: availability was stated as early 2026 for Quantum-X InfiniBand and 2H 2026 for Spectrum-X Ethernet <sup class="ref"><a href="https://www.genaitech.net/p/nvidias-4b-cpo-bet-scaleout-first" title="NVIDIA's $4B CPO Bet: Scale-Out First, Scale-Up Later" rel="noopener">ref</a></sup>, and analyst forecasts already put LPO and CPO above 30% of 800G and 1.6T ports for the 2026-2028 window <sup class="ref"><a href="https://www.lightcounting.com/newsletter/en/march-2026-ethernet-optics-382" title="LightCounting: January 2025 Optics for AI Clusters report (March 2026 release)" rel="noopener">ref</a></sup>. Buyers should be evaluating it now, including the serviceability and spares implications.

For optics attached to the compute die, the horizon is later. The COUPE thermal work is framed around the A16 / 2 nm node, the Intel 3.5D compensation results await silicon validation on the 18A platform, and the vendor sequencing itself is scale-out before scale-up <sup class="ref"><a href="https://www.genaitech.net/p/nvidias-4b-cpo-bet-scaleout-first" title="NVIDIA's $4B CPO Bet: Scale-Out First, Scale-Up Later" rel="noopener">ref</a></sup>. Treat compute-side CPO as Soon (2-5yr), gated on thermal control and on whichever modulator platform proves stable uncooled.

**TLDR: Switch-side CPO is shipping or imminent in 2026; compute-attached and scale-up CPO is the 2-5 year problem.**

## Overrated or underrated? Fairly rated

CPO is neither vapour nor a foregone conclusion. The switch use case has crossed into product with dated availability and a large capital commitment behind it <sup class="ref"><a href="https://www.genaitech.net/p/nvidias-4b-cpo-bet-scaleout-first" title="NVIDIA's $4B CPO Bet: Scale-Out First, Scale-Up Later" rel="noopener">ref</a></sup>, and the physical driver, copper failing at high symbol rates, is not going to reverse. That justifies the current level of attention. What the enthusiasm tends to skip is that the forecast most often cited in support bundles CPO with linear-drive pluggables into a single greater-than-30% figure <sup class="ref"><a href="https://www.lightcounting.com/newsletter/en/march-2026-ethernet-optics-382" title="LightCounting: January 2025 Optics for AI Clusters report (March 2026 release)" rel="noopener">ref</a></sup>, and LPO solves much of the same power problem without demanding a new field-service model.

The most useful sceptical framing comes from inside the field: CPO is an architectural commitment, and the binding constraints are packaging, thermal management, serviceability and standardisation rather than device figures of merit. On the evidence supplied, the thermal control story for micro-ring-based engines is still projection rather than validated silicon, and the material platform question is genuinely open, with silicon, TFLN, thin-film lithium tantalate, barium titanate, InP and VCSELs all live <sup class="ref"><a href="https://techxplore.com/news/2026-04-silicon-photonics-gained-powerful-ally.html" title="320 Gb/s Unamplified Transmission Using 100 GHz Ge PD and TFLN MZM on a Foundry-Compatible SiPh Platform" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.imec-int.com/en/press/veeco-imec-develop-300mm-compatible-process-enable-integration-barium-titanate-silicon" title="Veeco and imec develop 300mm-compatible process to enable integration of barium titanate on silicon photonics" rel="noopener">ref</a></sup>. Investors underwriting a single platform are taking more risk than investors underwriting the packaging and assembly layer.

## Prediction

By 31 December 2027, CPO volume will remain concentrated in network switch platforms, with no merchant (non-captive) CPO-attached AI accelerator providing compute-side optical scale-up I/O in production shipment.

## Evidence base

- NVIDIA announced on 2 March 2026 early-2026 availability for Quantum-X InfiniBand CPO switches and 2H 2026 for Spectrum-X Ethernet CPO switches, backed by a reported $4B commitment <sup class="ref"><a href="https://www.genaitech.net/p/nvidias-4b-cpo-bet-scaleout-first" title="NVIDIA's $4B CPO Bet: Scale-Out First, Scale-Up Later" rel="noopener">ref</a></sup>.
- LightCounting (March 2026 release) forecasts LPO and CPO ports together exceeding 30% of total 800G and 1.6T ports deployed in 2026-2028 <sup class="ref"><a href="https://www.lightcounting.com/newsletter/en/march-2026-ethernet-optics-382" title="LightCounting: January 2025 Optics for AI Clusters report (March 2026 release)" rel="noopener">ref</a></sup>.
- Analysis of TSMC's COUPE architecture at the A16 / 2 nm node states that a resonant wavelength deviation of merely +/- 1.7 nm in PIC-layer micro-ring resonators causes measurable BER degradation (18 May 2026).
- Pre-silicon co-simulation of Intel 3.5D packaging reports compensated CPO spectral drift below 0.36 nm, 21% of the stated TSMC tolerance budget, with silicon validation on Intel 18A still pending (30 June 2026).
- Thin-film lithium tantalate modulators retain electro-optic modulation and bandwidth with DC bias stability at 120°C, and show a 10% Vπ reduction at higher temperatures, supporting uncooled CPO operation (30 April 2026).
- A 2.5D co-packaged optical I/O chipset on a SiON/Si interposer with flip-chipped InP EMLs and photodetectors was experimentally demonstrated as a 400 Gb/s single-fibre transceiver (9 February 2026).

## Open questions

- Does the predictive thermal compensation approach holding CPO spectral drift to 0.36 nm survive silicon validation on Intel 18A, or does micro-ring drift force a shift to thermally insensitive modulators such as thin-film lithium tantalate?
- In the LightCounting forecast of over 30% of 800G/1.6T ports for LPO plus CPO in 2026-2028, what is the CPO-only share, and does linear-drive pluggable optics cap CPO adoption at the switch?
- What is the field failure and repair model for a co-packaged optical engine, and has any hyperscaler accepted package-level RMA in place of transceiver swap?
- Do coherent CPO schemes such as offset-QAM-16 move from foundry-process simulation to measured hardware at 400 Gb/s per lane, and at what laser power and package temperature?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
