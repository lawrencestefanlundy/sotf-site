---
type: concept
slug: qkd
canonical_name: QKD (Quantum Key Distribution)
aliases: []
kind: technology
parent_concepts:
- communications
- quantum-comms
related_concepts: []
sources: []
frontier:
- Do the new numerical finite-key frameworks that admit non-IID signals and partially characterised devices still yield commercially useful key rates once real modulator bandwidth limits, intensity correlations and detector timing effects are all included 2026 05 14 numerical security analysis for practical quantum key distri?
- 'Which family wins on cost per certified bit at metropolitan distance: DV with integrated photonics and single-photon detectors 2026 05 29 quantum key distribution over a metropolitan network using a, or CV reusing standard telecom optics and squeezed or coherent states 2026 05 29 practical continuous variable quantum key distribution with ?'
- Can the detector energy-time superlinearity be closed by countermeasure or must it be absorbed into the security proof, and at what key-rate cost 2026 05 14 energy time attack on detectors in quantum key distribution?
- Do the sub-quadratic authentication and adaptive routing results hold under real metropolitan traffic and real loss, or only under the sparse-mixing assumptions used to derive them 2026 05 28 emergent operational entanglement graphs and sub quadratic a?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 65
last_reorg_date: '2026-05-14'
scorecard:
  viability: 4
  drivers: 2
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Overrated
scorecard_status: draft
sources_7d: 0
sources_30d: 7
recent_mentions: []
neighbors: []
---
**Quantum key distribution uses single photons or weak optical signals to let two parties agree a shared secret key whose security rests on physics rather than computational hardness, and the 2026 literature shows the hardware is now rack-mountable and field-stable while the security proofs are still catching up with real devices.**

## Summary

QKD is a protocol family, not a single device. Alice encodes random bits in properties of very weak light (polarisation, time bins, phase, or the quadratures of a laser field), Bob measures them, and the two then run a classical exchange over an authenticated public channel to sift, error-correct and privacy-amplify what remains into a shared key. Any eavesdropper measuring the quantum signal disturbs it, which shows up as excess error or noise, so the parties can bound how much an adversary could know and hash the key down until that knowledge is negligible. The output is key material, typically consumed by symmetric encryption or, in the limit, a one-time pad.

Two hardware families dominate. Discrete-variable (DV) systems use single-photon detectors and decoy-state BB84 with attenuated lasers; continuous-variable (CV) systems use coherent or squeezed states with homodyne detection and reuse standard telecom optics. Variants proliferate: entanglement-based schemes such as BBM92 and E91, measurement-device-independent and twin-field protocols, mode-pairing protocols that beat the repeaterless rate-loss bound without global phase locking, and high-dimensional encodings using orbital angular momentum to raise bits per photon.

The parameters that decide QKD are channel loss, background noise, clock rate and the fidelity of the device model. Loss sets reach: metropolitan fibre links of tens of kilometres sit at roughly 10 dB, free-space CV work is being pushed to 23.5 dB, and geostationary satellite downlinks are an extreme-loss, high-background regime. Rate is chased by raising the repetition rate, which is exactly what creates the practical security problems: pulses at GHz clocks correlate with their neighbours and leak encoding settings, breaking a founding assumption of the decoy-state method.

The decisive variable is therefore not physics but characterisation. The security is information-theoretic only relative to a model of the boxes; when the boxes deviate, the proof does not apply. Much of the current work is closing that gap, either with numerical finite-key frameworks that admit non-IID signals and partially characterised hardware or by finding the next side channel in deployed components.

## Viability (4/5)

The engineering is demonstrably real. An integrated-photonics prototype running at 1.25 GHz in standard 19-inch rack units exchanged keys continuously over metropolitan fibre across more than 12 day-night cycles without manual intervention, and needed no chromatic dispersion compensation below 100 km. Free-space CV-QKD with self-referenced passive state preparation reported an asymptotic secret key rate of 10.34 Mbps at up to 23.5 dB loss under turbulence. Entangled time-bin distribution over about 30 km and 9.5 dB of the Vienna fibre network was done with off-the-shelf components. Squeezed-state CV-QKD has moved from theory to measured advantage over coherent states under finite-size security against collective attacks.

The deduction is that the security claim, which is the entire point, is still conditional. Existing proofs are described as falling short of capturing real systems; measured intensity correlations in two industrial decoy-state BB84 prototypes significantly reduce the asymptotic key rate, and higher-order correlations turn out to matter more than nearest-neighbour ones; a sinusoidally-gated avalanche detector at 312.5 MHz shifts its click timing by more than 2 ns across a 50 dB energy range, which an attacker could use to move a click between adjacent bit slots and render the security proofs inapplicable. A system that works and a system that is proven secure as built are not yet the same object.

**TLDR: Working field hardware and real key rates, but proofs that cover the actual devices are still being written.**

## Drivers (2/5)

On supply, the ingredients are converging: industrial prototypes exist in at least two independent product lines, integrated photonics is consolidating transmitters and receivers into rack units aimed explicitly at large-scale manufacturability, and protocol work is deliberately targeting cheap commercial parts, for example differential phase shift keying framed as a route to practical QKD using affordable commercial technology and CV schemes that reuse existing optical communication infrastructure. Reducing randomness demand from an unbounded stream to roughly four bits per pulse is the same kind of cost-driven engineering.

On demand, these sources say almost nothing. They assert that industrial-scale adoption requires cheaper and more stable hardware and that applications such as multiparty computation and the future quantum internet are rising, but contain no procurement, market, regulatory or standards evidence. The score reflects supply-side progress only; anyone underwriting a demand thesis will have to look outside this evidence base.

**TLDR: Supply-side momentum is visible in the sources; demand pull is essentially absent from them.**

## Novelty (3/5)

The claim to novelty is the security model itself: key agreement whose secrecy follows from quantum mechanics rather than from an assumption about an adversary's computing power. The sources do not benchmark that against any classical key-exchange alternative, so the headline advantage cannot be sized here. What they do quantify is progress inside the field. Squeezed states beat coherent states on key rate, excess-noise tolerance and reconciliation-efficiency requirements, now experimentally rather than only in theory. Mode-pairing protocols exceed the repeaterless rate-transmittance bound without global phase locking. Entanglement-based schemes supply intrinsic randomness and, per one source, generally higher security than prepare-and-measure. High-dimensional OAM encoding raises information efficiency and noise tolerance but remains constrained by state generation, transmission and detection.

There is also competition from within quantum communications. Quantum-memory-free quantum secure direct communication is being developed explicitly as an alternative to running QKD plus a one-time pad, using privacy amplification of coded sequences and universal hashing without wiretap coding. That matters because it suggests QKD is one architecture for physics-based confidentiality rather than the only one.

**TLDR: Qualitatively distinct security model, but the sources quantify improvements only against other QKD variants, not against the classical alternative.**

## Diffusion (2/5)

Reach is the first barrier. The flagship integrated prototype demonstrated continuous key exchange over more than 4 km of metropolitan fibre, with the architecture simplification justified for distances below 100 km; entangled distribution reached about 30 km at 9.5 dB. Longer spans need repeaters, trusted nodes, or satellites, and the geostationary route faces extreme channel loss plus daylight background, with feasibility depending on receiver architecture, wavelength choice including Fraunhofer minima, site environment and even historical cloud cover. Exotic channels such as seawater remain simulation-stage, with QBER sensitive to water type and turbulence.

The second barrier is certification. A survey organises practical QKD exposure into nine problem classes spanning device, channel, protocol, machine-learning and network layers, and proposes a benchmarking framework precisely because no unified one exists. Until security proofs routinely cover as-built hardware, each deployment is a bespoke assurance exercise, which is expensive. The third barrier is network operation: multi-user QKD needs routing that jointly optimises latency, key rate, congestion, capacity and risk, which is being attacked with Hamiltonian and tensor-network heuristics rather than settled practice, and authentication scaling is only now being argued down from quadratic to Theta(N log N) under sparse-mixing assumptions.

**TLDR: Distance, cost, certification and network-scale key management all bind before wide deployment.**

## Impact (3/5)

If the assurance problem is closed, QKD delivers something no computational scheme claims: key material whose secrecy does not degrade if an adversary's compute or cryptanalysis improves later. The sources point at continental-scale continuous secure communication via geostationary satellites and at entanglement distribution as the substrate for securely connecting quantum computers in a future quantum internet. Rates of order 10 Mbps over lossy free-space channels are enough for symmetric-key refresh on serious traffic volumes.

The bounds on impact are structural. QKD produces keys and still requires an authenticated classical channel, so it does not remove classical cryptographic dependencies; the authentication cost is itself an active scaling question at network scale. Point-to-point reach is limited without trusted or repeater nodes, and machine-learning components introduced for adaptation and monitoring create their own attack surface, with adversarial robustness recovery reported only up to 79.5%. The realistic value pool is government, financial and inter-datacentre links inside metropolitan distance, plus whatever satellite economics eventually allow.

**TLDR: High value in a narrow slot: long-lived confidentiality on fixed high-value links, not a general replacement for cryptographic infrastructure.**

## Timing Soon (2-5yr)

The hardware milestone has effectively landed: a rack-format, 1.25 GHz integrated-photonics system ran unattended over metropolitan fibre across more than 12 day-night cycles, and finite-key security for industrially relevant protocols is now being demonstrated at practical signal counts, with DPSK key rates at 10^5 signals beyond 12 dB. That combination is what a procurable metro product looks like.

What is not ready is the assurance chain. As of May 2026 the community is still publishing the first numerical finite-key frameworks that admit non-IID signals from bandwidth-limited modulators and only partial device characterisation, and simultaneously discovering new detector side channels in commercially typical components. Expect a two-to-five year window in which certified metro links become routine for high-value users. Satellite QKD, particularly geostationary, sits later: the current state of the art there is an end-to-end feasibility study rather than a link.

**TLDR: Metro-scale hardware is deployable now; security certification of that hardware is the thing that gates the next few years.**

## Overrated or underrated? Overrated

The engineering deserves respect and the marketing does not. On the evidence here, QKD hardware has crossed into product territory, and the rate and stability numbers are good. But the reason to buy QKD rather than a cheaper classical scheme is the security guarantee, and in 2026 that guarantee is still being repaired in public. Two industrial decoy-state BB84 prototypes were measured to leak encoding settings through pulse-to-pulse intensity correlations, with a significant hit to asymptotic key rate and with higher-order correlations worse than expected. A standard gated detector was shown to shift click timing by over 2 ns across a 50 dB range, enabling attacks that make existing proofs inapplicable. A survey of the field organises the practical failure modes into nine distinct classes and has to propose a benchmarking framework because none is agreed.

That pattern is characteristic of a technology whose theoretical claim is strong and whose implementation claim is not yet auditable. The rational position is that QKD will be genuinely valuable on specific links for specific threat models, that the interesting near-term work is certification and side-channel closure rather than record key rates, and that the phrase 'unconditional security' should be treated as a statement about a device model, not about a box in a rack. Note also that the sources contain no demand-side evidence at all, so anyone rating QKD highly on adoption grounds is doing so on faith.

## Prediction

By May 2028, at least one further published, experimentally characterised side channel in commercially representative QKD transmitters or single-photon detectors will be shown to invalidate security proofs used for deployed systems, in the same manner as the 312.5 MHz detector energy-time effect reported in 2026.

## Evidence base

- A 1.25 GHz integrated-photonics QKD prototype in 19-inch rack units held continuous key exchange over more than 4 km of metropolitan fibre across more than 12 day-night cycles without manual intervention, with no chromatic dispersion compensation needed below 100 km, reported 29 May 2026.
- Free-space CV-QKD with self-referenced passive state preparation and a local local oscillator reached an asymptotic secret key rate of 10.34 Mbps at up to 23.5 dB channel loss under turbulence, 8 May 2026.
- Intensity correlations measured in two industrial decoy-state BB84 prototypes leak encoding settings and significantly reduce the asymptotic key rate, with higher-order correlations having greater impact than nearest-neighbour ones, contrary to prior conjecture, 4 May 2026.
- An avalanche single-photon detector sinusoidally gated at 312.5 MHz showed click timing shifting by more than 2 ns as pulse energy varied over 50 dB, enabling two proposed attacks that violate an implicit assumption in security proofs, 14 May 2026.
- Sequential time-bin entangled photon pairs generated from GHz modulated laser pulses were distributed over about 30 km and 9.5 dB of the Vienna fibre network using off-the-shelf components, 14 May 2026.
- A survey published 28 May 2026 catalogues nine practical QKD problem classes across device, channel, protocol, machine-learning and network layers, reporting DBSCAN-based CV attack detection at precision 99.7% and recall 99.8% but adversarial robustness recovery only up to 79.5%.
- A geostationary decoy-state BB84 downlink feasibility study using variable-length finite-key security forecast annual secret-key yield across Europe from historical cloud data, establishing trade-offs rather than a demonstrated link, 29 May 2026.

## Open questions

- Do the new numerical finite-key frameworks that admit non-IID signals and partially characterised devices still yield commercially useful key rates once real modulator bandwidth limits, intensity correlations and detector timing effects are all included?
- Which family wins on cost per certified bit at metropolitan distance: DV with integrated photonics and single-photon detectors, or CV reusing standard telecom optics and squeezed or coherent states?
- Can the detector energy-time superlinearity be closed by countermeasure or must it be absorbed into the security proof, and at what key-rate cost?
- Do the sub-quadratic authentication and adaptive routing results hold under real metropolitan traffic and real loss, or only under the sparse-mixing assumptions used to derive them?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
