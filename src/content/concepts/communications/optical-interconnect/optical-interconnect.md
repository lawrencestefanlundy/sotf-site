---
type: concept
slug: optical-interconnect
canonical_name: Optical Interconnect
aliases:
- optical-interconnects
- Optical Interconnects
kind: technology
parent_concepts:
- communications
- optical-interconnect
related_concepts:
- optical-circuit-switching
- optical-packet-switching
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-05-30-optical-interconnect-ma-ledger]]'
- '[[2026-06-23-semidoped-daily-update]]'
- '[[2026-03-02-nvidia-4bn-lumentum-coherent-photonics-investment]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-05-30-opsydia-glass-waveguide-packaging]]'
- '[[2026-05-30-intel-glass-substrates-program]]'
- '[[2026-03-31-scale-up-interconnect-nvidia-s-2-billion-bet-on-marvell-the]]'
- '[[2026-04-28-optical-displaces-copper-ofc-2026-semtech-advances-ai-data]]'
- '[[2026-06-15-optical-interconnect-cpo-transition-optical-interconnects]]'
- '[[2026-04-15-semianalysis-isscc-2026]]'
- '[[2026-03-01-optical-displaces-copper-lightcounting-100-billion-market]]'
scorecard:
  viability: 4
  drivers: 4
  novelty: 4
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 97
descendants:
- datacenter-network-stack
- lpo-linear-pluggable-optics
- optical-circuit-switching
- optical-interconnect
- optical-io-chip-level
- optical-packet-switching
- pluggable-transceivers
- rack-scale-interconnect
- rf-over-dielectric-waveguide
- serdes
sources_7d: 1
sources_30d: 7
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-08-06-the-year-ai-science-and-the-physical-ai-industry-came-alive
  title: The Year AI Science and the Physical AI Industry Came Alive
  date: '2026-08-06'
  kind: web
- slug: 2026-07-29-serenity-globalfoundries-receives-support-from-the-us-chips-
  title: 'Serenity: GlobalFoundries receives support from the US CHIPS Act, benefiting Sivers and Lumentum - Bitget'
  date: '2026-07-29'
  kind: web
- slug: 2026-07-26-ai-backend-network-optics-2026
  title: 'Dell''Oro: AI back-end switching past $100B by 2030, optical transport $16B in 2025'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-15-optical-interconnect-cpo-transition-optical-interconnects
  title: Optical Interconnects Become Critical to AI Factory Expansion; CPO/NPO Market Expected to Exceed US$39 Billion by 2030
  date: '2026-06-15'
  kind: web
- slug: 2026-05-30-optical-interconnect-ma-ledger
  title: Optical-interconnect / photonic-packaging M&A ledger (2019-2026)
  date: '2026-05-30'
  kind: web
neighbors:
- slug: optical-circuit-switching
  name: Optical Circuit Switching (OCS)
  path: /communications/optical-interconnect/optical-circuit-switching/
  macro: communications
- slug: optical-packet-switching
  name: Optical Packet Switching (OPS)
  path: /communications/optical-interconnect/optical-packet-switching/
  macro: communications
---
**Optical interconnect replaces copper wiring between and inside computers with light, and recent chip-scale demonstrations now reach 1.024 Tb/s on a single CMOS receiver at 71 fJ/b, moving the remaining risk from devices to packaging, thermal design and standardisation.**

## Summary

An optical interconnect carries data as modulated light over fibre or on-chip waveguides instead of as electrical signals over copper. A link needs four things: a light source (a laser, or a comb producing many wavelengths at once), a modulator that imprints data onto the light, a waveguide or fibre, and a receiver with a photodetector and amplifier. Capacity is scaled mainly by wavelength-division multiplexing, running many colours down one path simultaneously, and by higher-order modulation such as four-level pulse amplitude modulation (PAM-4). The interesting engineering is in shrinking all of this onto silicon so that it can sit next to, or on top of, a processor.

The recent literature shows this working at system-relevant numbers. A monolithic 32-channel WDM receiver in 45 nm CMOS runs 1.024 Tb/s aggregate at 71 fJ/b including photonic tuning and control, with 4 Tb/s/mm2 bandwidth density and bit error rate below 1e-12 with no equalisation or forward error correction. A separate receiver built by micro-transfer-printing a 0.06 mm2 BiCMOS electronic chiplet directly onto a silicon photonic circuit reaches 224 Gb/s PAM-4 at 0.51 pJ/b and -5.2 dBm sensitivity. On the transmit side, a thin-film lithium niobate 1x8 modulator array butt-coupled to a distributed-feedback laser shows over 40 GHz bandwidth per channel and roughly 25 dB extinction ratio.

The parameters that decide the technology are energy per bit, bandwidth per unit of chip edge or area, optical loss budget (which sets how much laser power, and therefore heat, the package must carry), and thermal and mechanical robustness once optics sit inside the compute package. The same TFLN transmitter that hits 40 GHz also carries 15.19 to 16.55 dB of bare-chip insertion loss plus a further coupling penalty from laser bonding, which is the sort of number that determines whether a link closes at acceptable power. Supporting components are moving in parallel: a PZT Pockels external-cavity laser with 82 nm tuning and 17 pm/V tuning efficiency, a thin-film lithium tantalate polarisation controller tracking at Mrad/s with under 0.3 dB polarisation-dependent loss, and cavity-less on-chip frequency combs aimed at higher power per line for multiwavelength sources.

The framing argument in the field is that the hard part has shifted. One review states plainly that as optics move closer to compute, packaging, thermal management and system-level robustness dominate performance and scalability, and that standardisation and serviceability will decide whether co-packaged optics moves from early deployment to widespread adoption.

## Viability (4/5)

The demonstrations are not simulations. A 45 nm CMOS receiver runs all 32 WDM channels simultaneously at 32 Gb/s each for 1.024 Tb/s aggregate, at 71 fJ/b including electronics and photonic tuning, with BER below 1e-12 and no equalisation or error correction. A 3D micro-transfer-printed BiCMOS-on-photonics receiver achieves 224 Gb/s PAM-4 at 0.51 pJ/b. A 3D silicon nitride interposer has been fabricated and measured, cutting waveguide crossings for a fully connected 12-node network from 495 to 150 and average per-waveguide loss by 45.8% relative to planar routing. Passive InP nanobeam laser cavities have been fabricated with measured Q above 170,000.

What holds the score below 5 is the loss and source side. The integrated TFLN transmitter array reports 15.19 to 16.55 dB bare-chip insertion loss with additional loss from DFB bonding, and the PZT tunable laser delivers 5 mW fibre-coupled output. Efficient III-V-to-silicon coupling on standard 220 nm silicon remains a design problem being addressed at the simulation stage rather than solved in volume. Receivers are further ahead than sources.

**TLDR: Working silicon at terabit rates and sub-picojoule-per-bit energies, with laser integration and coupling loss still the weak link.**

## Drivers (4/5)

On demand, the papers converge on one cause. Communication between devices is described as the key performance bottleneck in large-scale distributed LLM training, motivating combined chiplet and optical interconnect cluster designs. AI and accelerator workloads are cited as forcing a rethink of datacentre optical interconnect architecture, and AI-driven exabyte-scale transfer is cited as pushing conventional interconnects toward fundamental bandwidth and energy limits. Distributed learning traffic in large systems already runs over optical fibre, which is the premise for offloading gradient averaging into the optical domain. A second demand pull is appearing outside datacentres: superconducting quantum processors face an I/O bottleneck from per-qubit microwave cabling, and optical I/O is proposed as the way out.

On supply, capability is arriving from multiple independent directions rather than one fragile process: monolithic 45 nm CMOS photonics, micro-transfer printing of electronic chiplets onto photonic dies, thin-film lithium niobate and lithium tantalate modulators, PZT electro-optics and silicon nitride interposers. The sources contain no capital spending, capacity or pricing data, so the supply judgement rests on technical breadth only.

**TLDR: Demand is unambiguous and stated across the literature as the AI communication bottleneck; supply is broadening across several materials platforms, though the sources give no market figures.**

## Novelty (4/5)

The comparison class is electrical input/output. Photonic interposers are being pursued explicitly as an alternative to electrical links for energy efficiency and bandwidth, and co-packaged optics is framed as the answer to the energy and bandwidth limits of electrical I/O. The specific numbers that carry the case are 71 fJ/b at 4 Tb/s/mm2 for a full WDM receiver chip, described as records, and 0.51 pJ/b at 224 Gb/s PAM-4 in a record-small footprint via 3D heterogeneous integration. Within photonics itself, the 3D routing scheme beats the theoretical lower bound for planar crossings (150 versus a planar bound of 153) and cuts average waveguide loss by 45.8%.

The counter-case is specific and comes from the same literature. Terahertz silicon interconnects are proposed on the argument that the complexity and energy overhead of optics limit scalability in short-reach chiplet-based and on-chip systems, with a demonstrated CMOS-compatible centimetre-scale link at 1.004 Tbps aggregate. That does not threaten optics at rack or campus reach, but it makes the on-package and on-chip segment genuinely contested. Improved electrical-domain signal processing also narrows the gap at short reach: simplified MLSE cuts latency from 34 to 7 delay units and multipliers from 512 to 33 on a 112 Gbit/s PAM4 link over 2 km of single-mode fibre.

**TLDR: Clear measured advantage over electrical I/O on energy and bandwidth density, but short-reach on-chip links face a credible terahertz-electronic challenger.**

## Diffusion (3/5)

The baseline case for diffusion is already met at the network level: communication in large-scale systems uses optical fibres. The contested step is bringing optics into the compute package. Here the literature is explicit that co-packaged optics is an architectural commitment rather than a component swap, that packaging, thermal management and system-level robustness increasingly dominate scalability as optics move closer to compute, and that standardisation, serviceability and thermal-aware co-design will determine whether it goes from early deployment to widespread adoption. The title of that paper, arguing that solving the wrong problems stalls deployment, is itself the diffusion risk statement.

**TLDR: Fibre links are already standard in large systems, but co-packaged optics faces packaging, thermal, serviceability and standardisation barriers that the field itself calls decisive.**

## Impact (4/5)

The value case is that interconnect, not compute, is the binding constraint for large distributed training, which is the position taken by the cluster design work and the terahertz interconnect work alike. Relieving it changes achievable cluster scale and energy cost directly: a receiver at 71 fJ/b and 4 Tb/s/mm2 operates in a different regime from the electrical I/O it displaces. There are also second-order gains where the interconnect itself becomes computational, as in offloading gradient averaging and quantisation into Mach-Zehnder interferometers within the network, and where programmable photonic engines provide switching and reconfigurable add-drop multiplexing on the same platform.

A distinct and potentially large adjacent impact is quantum computing I/O. A full optical control and readout architecture for superconducting qubits has shown frequency-multiplexed optical readout of two qubits with no measurable degradation of coherence times and only a 0.19% reduction in single-qubit gate fidelity relative to microwave operation, addressing the cabling, thermal load and footprint bottleneck that limits scaling to hundreds of qubits. The sources do not quantify market size or cost savings in currency, so the impact judgement is technical rather than financial.

**TLDR: If package-level optics scales, it removes the stated bottleneck of large-model training and unlocks a second application in quantum processor I/O.**

## Timing Now (0-2yr)

Fibre already carries inter-server traffic in large-scale systems, and co-packaged optics is characterised as needing to make the transition from early deployment to widespread adoption, which implies deployment has begun. Receiver-side integration is at the record-setting demonstration stage now, with full-chip terabit operation reported in January 2026 and a 224 Gb/s 3D-integrated receiver in late 2025.

The items further out are the ones tied to sources, packaging and standards rather than to devices. Multi-channel TFLN transmitters with bonded lasers still carry double-digit decibel insertion loss, high-power on-chip comb sources are at the proof-of-concept stage, and optical I/O for superconducting qubits has been shown for two qubits, not hundreds. Expect the datacentre transition to be continuous rather than a step change, with the quantum I/O application on a longer horizon.

**TLDR: Optical links are already the backbone of large systems and co-packaged optics is described as in early deployment; the open question is the pace of the on-package transition, not whether it starts.**

## Overrated or underrated? Fairly rated

The device-level case is settled enough that arguing about it is no longer the interesting activity. Terabit-per-chip receivers at 71 fJ/b in a standard CMOS node, sub-picojoule 224 Gb/s links via 3D chiplet printing and 40 GHz-class integrated modulator arrays mean the physics and the process are not the constraint. The field's own most useful contribution here is the warning that continuing to optimise devices is solving the wrong problem, and that packaging, thermal management, serviceability and standardisation now decide the outcome. Enthusiasm should therefore be redirected rather than reduced.

Two caveats keep this from being an underrated call. First, the short-reach on-package segment is genuinely contested by terahertz silicon interconnects, which claim optics carries too much complexity and energy overhead at that reach and have demonstrated 1.004 Tbps on a CMOS-compatible chip-scale link. Second, transmit-side loss and laser power remain unresolved in the published integrated demonstrations, and heat inside a compute package is exactly where the review says the difficulty lies. The one place the sources point to a genuinely underpriced application is optical I/O for superconducting quantum processors, where the first closed-loop demonstration showed only a 0.19% gate fidelity penalty.

## Prediction

By June 2028 a peer-reviewed demonstration will report a fully integrated optical transmitter, including its on-chip or bonded laser, at aggregate rates above 1 Tb/s per chip with total energy below 1 pJ/b; if published transmitter-side energy including the laser remains above 1 pJ/b, the co-packaged optics thesis is materially behind schedule.

## Evidence base

- A monolithic 45 nm CMOS 32-channel WDM receiver ran 1.024 Tb/s aggregate at 71 fJ/b and 4 Tb/s/mm2 with BER below 1e-12 and no equalisation or error correction, reported 12 January 2026.
- A 3D micro-transfer-printed BiCMOS chiplet of 0.06 mm2 on a silicon photonic circuit achieved 224 Gb/s PAM-4 at 0.51 pJ/b and -5.2 dBm OMA sensitivity at BER 2.4e-4, reported 28 November 2025.
- A hybrid-integrated 1x8 TFLN modulator array with a bonded 1550 nm DFB laser reached over 40 GHz per channel and about 25 dB extinction ratio, but carried 15.19 to 16.55 dB bare-chip insertion loss plus bonding coupling loss, reported 20 May 2026.
- A March 2026 review argues co-packaged optics is an architectural commitment where packaging, thermal management and system robustness dominate scalability, and that standardisation and serviceability will decide the move from early deployment to widespread adoption.
- A CMOS-compatible centimetre-scale terahertz silicon link achieved 1.004 Tbps aggregate, positioned explicitly against optical interconnects on grounds of complexity and energy overhead at short reach, reported 16 May 2026.
- A fabricated 3D silicon nitride interposer cut crossings for a fully connected 12-node network from 495 to 150, below the planar theoretical bound of 153, and reduced average per-waveguide loss by 45.8%, reported 14 April 2026.

## Open questions

- Can transmit-side insertion loss be brought well below the 15.19 to 16.55 dB reported for the integrated TFLN modulator array, and what laser power and package heat load does the residual loss imply?
- Does terahertz silicon interconnect at 1.004 Tbps displace optics for on-package and chiplet-to-chiplet reach, or does it remain confined to centimetre-scale links?
- Which standardisation and serviceability model wins for co-packaged optics, given that the field identifies these rather than device performance as decisive for widespread adoption?
- Does multiplexed optical control and readout of superconducting qubits scale from two qubits to hundreds while preserving coherence times and gate fidelity?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
