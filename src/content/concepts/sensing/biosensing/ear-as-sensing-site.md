---
type: concept
slug: ear-as-sensing-site
canonical_name: The ear as a sensing site
aliases:
- ear sensing
- in-ear sensing
- hearables sensing
- ear biometrics
parent_concepts:
- sensing
related_concepts:
- hearing-aid-silicon-beachhead
- edge-ai
- low-power-edge-compute
- biometrics
sources: []
frontier:
- Does Apple hold ear-EEG or in-ear core-temperature patents/intent? This decides whether the regulated-medical niche is durably safe or merely next.
- Does any independent consumer in-ear sensing company reach >$50M standalone revenue by end-2028? (prior ~25% it does)
- Why did Bose shut its health division despite a dedicated Sleepbuds user base? Margin, regulatory, or churn?
last_updated: 2026-07-15
tags:
- concept
- sensing
- hearables
descendants:
- otoacoustic-emissions
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: hearing-aid-silicon-beachhead
  name: Hearing aids as an edge-AI silicon beachhead
  path: /compute/ai-edge/hearing-aid-silicon-beachhead/
  macro: compute
- slug: edge-ai
  name: Edge AI
  path: /compute/ai-edge/edge-ai/
  macro: compute
- slug: biometrics
  name: Biometrics
  path: /sensing/imaging/biometrics/
  macro: sensing
---
## The one-line read

The ear is genuinely the **best non-invasive site on the body for three things** — EEG, core temperature, and cephalic (head-directed) blood flow — and merely an *alternative* site for everything else, where the wrist and finger are already good enough and already own the user. **Every independent consumer in-ear sensing company to date has died, sold its hardware, been acqui-hired, or been shut down by its own parent. Zero survivors.** The survivors are component licensors and regulated-medical plays.

## What the ear is uniquely good for

Use this as the first screen. If a pitch's modality is not on this list, the ear is a form-factor choice, not an advantage.

- **Ear-EEG.** The only discreet, wear-all-day EEG site. The wrist cannot measure EEG at all. In-ear recordings showed >98% validity against 46–78% for frontal setups. Still inferior to scalp EEG, and single-channel in-ear sleep staging is **90.5% binary wake/asleep but only 65.1% four-class** — the accuracy gap is the product problem.
- **Cephalic blood flow.** Nothing at the wrist tells you about blood flow *to the head*. **Stat Health** optically senses a shallow ear artery as a cerebral-flow proxy; published in JACC (Mar 2023), tested at Johns Hopkins, predicts fainting minutes ahead. Cleanest "only the ear can do this" claim in the map.
- **Core body temperature.** The tympanic membrane reflects **carotid** temperature. But you cannot wear a sensor *on* the TM — you sit at the canal entrance and a thermal gradient from ambient air corrupts it. Right in principle, contested in practice.
- **Cochlear function (otoacoustic emissions).** Only observable from the ear. See the graveyard: this is what nura did, and it exited as an acqui-hire.
- **Ear-canal acoustic biometrics.** Only site with the geometry. Also a 30-year-old idea — see below.

Everything else — HR, HRV, SpO2, blood pressure — is an **alternative site, not a better one**. The real ear edge for PPG is *motion immunity* (the canal is mechanically shielded), not accuracy.

## The power inversion (matters for any silicon thesis)

Naive intuition says the amplifier is the constraint. It is not. **EEG front-ends are nearly free** (~200 µW for 8-channel acquisition ASICs; sub-µW/channel front-ends in 28nm). **PPG is the power hog** — you are pushing photons through tissue, and Apple pulses LEDs >100×/sec. The scarce resource in an earbud is the **optical budget**, not the compute or the amplifier. Any pitch claiming an inference-silicon power win should be asked what fraction of the earbud's budget its block actually addresses.

*(Confidence: directional. Sourced from academic ASIC figures; no shipping-product teardowns found.)*

## The graveyard — the load-bearing evidence

| Company | What happened |
|---|---|
| **Bose Health** | Division **shut down**. Sleepbuds discontinued 2019 (battery); Sleepbuds II launched Oct 2020, **discontinued Mar 2023 despite a dedicated user base**; health division closed to refocus on core audio. A $4B audio company with brand, distribution and engineering could not make in-ear health work. |
| **Nura** (AU) | **Acqui-hired by Masimo/Denon, Apr 2023.** Brand phased out, tech rebranded Masimo AAT. The otoacoustic-emission company — the most defensible ear-only modality — exited as an acqui-hire. |
| **Bragi** (DE) | **Sold hardware business Apr 2019**, pivoted to licensing. The Dash (2015) predated AirPods (2016) and lost anyway. Post-mortem is explicit: too early, hardware execution, "solved by the more simplistic AirPods." |
| **Doppler Labs** (US) | **Dead.** ~$50M raised, Here One discontinued. |
| **Ozlo** | Ex-Bose engineers rebuilt Sleepbuds. The corpse got reanimated by its own team — demand was real, the *business* wasn't. |

**The message: zero independent consumer in-ear sensing survivors.** Sample is small (~5) and pre-dates the current sensing generation, so hold at ~85% not 100%.

## The structural read — Apple absorbs

Apple's pattern is to absorb proven modalities as **free features**, not to compete on price:
- **Hearing aid:** Sept 2024 FDA De Novo, first OTC hearing-aid software. Not a hearing-aid business — a software toggle on a product it already sells 100M+ of.
- **Hearing test:** 5-minute pure-tone audiometry on hardware you own.
- **Heart rate:** Powerbeats Pro 2 (Feb 2025) → AirPods Pro 3 (Sept 2025) → iOS 26 Fitness integration.

The kill mechanism is **distribution, not capability**. IDC forecasts **407.6M hearable units in 2026 (+4.0%)**, explicitly citing biometric health monitoring as a driver. Apple gets biometric distribution free on an install base an independent cannot buy. **Bose Health is the clean control experiment.**

**Evidence against the absorption thesis** (thin, but real): Apple frames ear HR as *complementary* to the Watch, not a replacement. It has shipped **no ear-EEG and no core temperature**, with no signal it intends to. Note the shape of that counter-evidence — it says the niche is *currently un-absorbed*, not un-absorbable. Apple didn't ship a hearing aid until it did.

## Where the defensible positions are

1. **Regulated medical — the only one with a proof point.** **Naox Technologies** (French) received **FDA 510(k) clearance in Jan 2026 for Naox Link, the first-ever in-ear EEG clearance** (CEO Hugo Dinh; already in select neurology and sleep centres). This works precisely *because* Apple won't go there — Apple's regulatory posture is the lowest-risk path touching the most people. Epilepsy monitoring and Alzheimer's-risk epileptiform detection need trials, reimbursement codes, and a neurologist channel. **But this is a medical-device business, not a semiconductor one** — value accrues to the clinical dataset and the clearance, not the silicon, so the winner here is whoever can fund trials and a neurologist channel. Confidence it's durable: ~65%, one proof point and zero exits.
2. **Defence / industrial.** **Stat Health** holds a **US Air Force grant**. Core temp + cephalic blood flow under heat stress and G-load is a real military requirement with a buyer indifferent to consumer distribution economics. Small, non-commoditisable. One datapoint, not a market.
3. **Component / IP licensing — where the bodies are.** Valencell is the *successful* case and it's a modest licensing business, not a venture outcome. Bragi pivoted to licensing and disappeared. Nura's IP ended up inside Denon.
4. **Consumer device: no defensible position found.** Zero counter-evidence.

## Ear biometrics is a 30-year-old idea in a patent minefield

- **[US5787187A](https://patents.google.com/patent/US5787187A/en)** — "Systems and methods for biometric identification using the acoustic properties of the ear canal," **Sandia, filed 1 Apr 1996**, granted 1998, now **expired**. The core idea is public domain.
- **NEC** has pushed ear acoustic authentication since 2016 with a **live patent family**; **Apple** has an ear-canal biometrics filing. A pre-seed company selling an ear-print module to headphone OEMs walks into NEC plus Apple — and the OEMs it wants to sell to are the parties filing the patents.
- **The "99% accuracy / like Face ID" claim does not survive contact with the literature.** 99% accuracy is a meaningless metric; the operating point is what matters. Independent work reports **22% false-rejection at 0.1% false-accept** — one in five legitimate unlocks fails. Face ID's false-match rate is ~1 in 1,000,000, roughly 1000× tighter. **The Face ID comparison is not defensible.**
- **NEC did ship — via crowdfunding, in 2020, ten years after announcing, with no OEM design win.** Likely causes: reinsertion/fit variance (a physical property of the measurement, not a software bug), the FRR problem above, and no job-to-be-done (your phone already authenticated you and pairs by proximity).

## Attention decoding — read this before any "we read your focus" pitch

- **The established route is EEG, and it's crowded.** KU Leuven (Bertrand) reports 91.8%/81.1% at 0.1s windows; **Eriksholm (Oticon/Demant)** ran the EU COCOHA project and built a real-time prototype. ~15 years, EU consortium money, in-house research arms of the major OEMs — **and still no shipped neuro-steered hearing aid.** That is the base rate.
- **The otoacoustic-emission route is contested to the point of artifact.** Francis, Zhao & Guinan Jr, *Frontiers in Systems Neuroscience* 2018: **"Auditory Attention Reduced Ear-Canal Noise in Humans by Reducing Subject Motion, Not by Medial Olivocochlear Efferent Inhibition."** Across 8 subjects the apparent attention effect was subjects **holding still and breathing differently**; only 2 of 8 showed an efferent signature. A 2020 replication (n=20) split 9-of-20 — a coin flip. Guinan is the senior figure in efferent physiology.
- **Diligence screen:** any demo where a subject concentrates and the ear-canal signal changes is *exactly what Guinan 2018 predicts from postural stillness*, with zero cochlear physiology. **Ask whether subject motion was controlled.** If the answer is vague, that is the answer.
- **Framing correction:** "below the noise floor" is backwards. The clinical criterion for an OAE is **3–6 dB *above*** the noise floor, recovered by averaging over many repetitions. That averaging costs *time*, set by noise statistics — you cannot engineer it away with a better microphone. Fatal for a real-time interface.
- **Direction has no mechanism.** The efferent reflex is a cochlear **gain control** — a volume knob. Spatial direction is computed *centrally* from interaural timing/level differences. No literature suggests a per-ear gain signal carries azimuth.

## Market size — the right denominator

**Wrong denominators:** "hearables market $55–62B" is the *audio* market; sensing is a feature inside it. Any slide multiplying 400M earbuds by a health ARPU.

| Layer | Number | Source quality |
|---|---|---|
| Hearables, units | **407.6M (2026F, +4.0%)** | High — IDC, vendor-independent |
| **Hearing aids, units** | **23.16M (2025), +2.1% YoY** | **Highest in this page — EHIMA member actual sales, not a forecast** ([EHIMA](https://www.ehima.com/about-ehima/hearing-aid-sales/)) |
| Hearing aids, value | ~$9.1B (2025) → $9.7B (2026) | Low-med (analyst house) |
| Top-5 buyer concentration | **92.4% (2024)** | Med-high |

**The layers are three, and they are not the same business.**

- **Device layer (407.6M hearable units):** the biggest number and the most captive. Apple/Samsung/Chinese ODMs own it, and proven modalities arrive as free features. Independent consumer devices here: see the graveyard.
- **Medical-device layer (23.16M hearing aids + the un-absorbed clinical niches):** ~$9.7B in device value, growing ~2%/yr, 92.4% held by five vertically-integrated firms. The *growth* is not here; the *defensibility* is, in the regulated corners (Naox) those five and Apple don't enter.
- **Silicon / IP layer:** 23.16M units/year across ~5 buyers. At a plausible $5–20 sensing/SoC content, the entire addressable chip layer is **~$115M–$460M/year**, contested, against buyers who design in-house (Sonova, Demant, Starkey) and who bought from an incumbent (Starkey→Valencell) the one time they didn't. The device denominator is 17× larger and inaccessible — **nobody is selling a sensing ASIC into AirPods.**

**The size conclusion, vehicle-agnostic:** the ear is a **hundreds-of-millions** opportunity at the component layer and a **single-digit-billions, low-growth, highly concentrated** one at the device layer. Neither shape supports a venture-scale independent outcome on current evidence. The asymmetric money here, if any, is in regulated-medical clearances and in the listed incumbents' exposure to OTC commoditisation — not in the chip.

⚠️ **The $5–20 content figure is an estimate, not a sourced number** — no independent hearing-aid BOM teardown found. Treat $115M–$460M as an order-of-magnitude check that the answer is "hundreds of millions, not billions." That conclusion survives a 3× error either way. The unit count and concentration are solid; the BOM is not.

## So what

**This page confirms [Hearing aids as an edge-AI silicon beachhead](/compute/ai-edge/hearing-aid-silicon-beachhead/) arithmetically, at ~80%.** That page argued the beachhead is structurally thin; EHIMA's 23.16M units at +2.1% and 92.4% top-5 concentration are the numbers behind it. Attach them there rather than re-deriving.

Three screens for the next ear deal:
1. **Is the modality on the "uniquely good for" list?** If not, the ear is a form factor, not an edge.
2. **Which graveyard entry is this?** Bose had brand, distribution and engineering. What does this team have that Bose didn't?
3. **If it's attention decoding — was subject motion controlled?**

## All-routes read

## Suggested prediction to log

*"No independent consumer in-ear sensing company reaches >$50M standalone revenue by end-2028."* — prior **~75%** it holds. Resolvable, and it's the crux of this page.

## Connected

## Sources

Research sprint 15 Jul 2026, three parallel agents. Key primary sources verified directly by Lawrence's session (not agent-relayed): [EHIMA hearing aid sales](https://www.ehima.com/about-ehima/hearing-aid-sales/) (23.16M/2025, +2.1%); [Francis, Zhao & Guinan 2018](https://pubmed.ncbi.nlm.nih.gov/30271329/); [US5787187A Sandia 1996](https://patents.google.com/patent/US5787187A/en) (expired); [Naox FDA clearance Jan 2026](https://medcitynews.com/2026/01/fda-eeg-brain-healthcare/).
