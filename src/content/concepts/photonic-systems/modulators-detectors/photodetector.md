---
type: concept
slug: photodetector
canonical_name: Photodetector & Optical Receiver Front-End
aliases:
- photodiode
- Ge-on-Si photodiode
- optical receiver
- APD
- TIA
parent_concepts:
- photonic-integrated-circuits
related_concepts:
- germanium-photodiodes
- ingaas-photodiodes
- avalanche-photodiode
- co-packaged-optics
- optical-interconnect
- silicon-photonics
- external-laser-source
- uni-traveling-carrier-photodiode
sources:
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
frontier:
- Does any merchant/discrete datacom receiver supply chain de-integrate from the SiPh die (the laser precedent) — or does Ge-on-Si keep detection monolithic and commoditised?
- Does a single-photon detector (SPAD array / SNSPD) cross from niche into a system play big enough to escape the commodity-detector ceiling, outside incumbent capture?
last_updated: 2026-06-17
tags:
- concept
- photonics
- orientation
descendants:
- avalanche-photodiode
- uni-traveling-carrier-photodiode
mention_count: 19
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
neighbors:
- slug: germanium-photodiodes
  name: Germanium Photodiodes
  path: /photonic-systems/modulators-detectors/germanium-photodiodes/
  macro: photonic-systems
- slug: ingaas-photodiodes
  name: InGaAs Photodiodes
  path: /photonic-systems/modulators-detectors/ingaas-photodiodes/
  macro: photonic-systems
- slug: avalanche-photodiode
  name: Avalanche Photodiode (APD / SPAD)
  path: /photonic-systems/modulators-detectors/avalanche-photodiode/
  macro: photonic-systems
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: optical-interconnect
  name: Optical Interconnect
  path: /communications/optical-interconnect/optical-interconnect/
  macro: communications
- slug: silicon-photonics
  name: Silicon Photonics
  path: /photonic-systems/pic-platforms/silicon-photonics/
  macro: photonic-systems
- slug: external-laser-source
  name: External Laser Source (ELS) for Co-Packaged Optics
  path: /photonic-systems/light-sources/external-laser-source/
  macro: photonic-systems
- slug: uni-traveling-carrier-photodiode
  name: Uni-Traveling-Carrier Photodiode (UTC-PD)
  path: /photonic-systems/modulators-detectors/uni-traveling-carrier-photodiode/
  macro: photonic-systems
---
> **Orientation page** (built 2026-06-17). The receive end of an optical link: the chip that turns light back into electrical current after a laser/modulator has sent bits down a fibre or waveguide. Every optical interconnect, LiDAR, quantum-comms and optical-sensing system needs one. Investment view is the **Photonic Photodetection Layer** non-area call; this page is the device primer that sits under it.

## How to read any detector pitch — the six axes

| Axis | What it is | Good = | Watch for |
|---|---|---|---|
| **Bandwidth / speed** | How fast it switches (GHz, or rise time in ps) | Higher; datacom wants >100 GHz/lane | Hero numbers from one lab device or old data |
| **Responsivity** | Current out per watt of light in (A/W) | Higher = weaker, lower-power lasers | Quoted at an unrealistic wavelength/power |
| **Dark current / noise** | Leakage with no light; sets the faintest readable signal | Lower (nA range) | Omitted entirely |
| **Capacitance** | Large C is itself a speed limit | Lower | Large *device area* hides high total C |
| **Bias voltage** | Most need an applied voltage; "zero-bias/self-powered" is a real efficiency win **if** real | Lower / zero | "Self-powered" claims without a responsivity tradeoff shown |
| **Integration & wavelength** | Built *on* the silicon photonic die, or bonded separately? Works at 1310/1550 nm? | CMOS/SiPh-native | III-V that must be bonded; wrong wavelength |

Rule of thumb: a 2026 university Ge-on-Si waveguide detector already does **>110 GHz, 112–336 Gbps/λ, ~7 nA dark current, ~1 A/W** (sjtu ge si photodetector 110ghz fowlp). So raw speed is *table stakes*, not a moat — the value is in packaging/integration.

## The families (mapped to the KB)

## The investment throughline (why it's a non-area)

The datacenter interconnect *is* moving to optics (**Optical Interconnect Cpo Transition**, conviction 84), and detection is necessary. But as a **discrete datacom component the detector is a commodity** — the profit accrues to the silicon-photonics receiver/transceiver that swallows it (**Broadcom**, **Coherent**, **Lumentum**), or to the foundry (GF SiPh) that fabs it. A standalone detector startup caps at strategic acquisition or sub-scale. This is the recorded **Photonic Photodetection Layer** non-area, with two live predictions (no pure-play datacom-detector startup reaches >$500M independent valuation by 2030; none raises ≥$200M by end-2027). Public exposure to the layer is the SiPh primes (COHR, LITE).

A detector only escapes that ceiling **two** ways — the page's re-open triggers:
1. **Become a *system* in another market** — SPAD array / SNSPD into LiDAR / quantum / imaging (single photon detector market spad snspd). Bigger and faster-growing, but SPAD/SiPM volume is incumbent-captured (Sony/STM/**Onsemi On Semiconductor**) and SNSPD is a cryogenic niche. Routes into **Mid Ir Photonic Sensing** / **Image Sensor Silicon** / the quantum cluster, not a standalone "detector" thesis. KB pass-case: **Moon Photonics**.
2. **De-integrate into a merchant, separately-sourced supply layer** — the way *external lasers* did under CPO (sivers onet enablence external light source cpo, captured by **Photonic Light Source Supply**). **Detection does the opposite of lasers:** lasers are III-V, heat-sensitive and wavelength-critical, so they get isolated and separately sourced; Ge-on-Si detectors are CMOS-native and grow monolithically on the die, so they stay *inside* the receiver. That asymmetry is the core reason "light source = supply thesis" but "detector = non-area".

The genuine open question (the bottleneck): there is a real **device-physics** limit — the space-charge effect throttles high-speed response under high optical power (PAM4 / high-power CPO), pushing research into GeSn, plasmonic Ge and UTC structures. But that frontier is being solved *by the foundries and primes, integrated* — it is an R&D problem inside the receiver, not a sourced merchant layer. A bottleneck only becomes an investable thesis when it de-integrates (re-open trigger #2) or becomes a system (#1).

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Further reading
- [Germanium Photodiodes](/photonic-systems/modulators-detectors/germanium-photodiodes/) · [InGaAs Photodiodes](/photonic-systems/modulators-detectors/ingaas-photodiodes/) · [Avalanche Photodiode (APD / SPAD)](/photonic-systems/modulators-detectors/avalanche-photodiode/) — the material sub-pages
- **Photonic Photodetection Layer** — the non-area investment position (read first for the "should we ever back a detector" answer)
- **Photonic Light Source Supply** — the contrast case: the layer that *does* capture value
- SJTU >110 GHz Ge-Si FOWLP detector (sjtu ge si photodetector 110ghz fowlp)
- External light source / CPO supply asymmetry (sivers onet enablence external light source cpo)
- Single-photon detector market (SPAD/SiPM/SNSPD) (single photon detector market spad snspd)
