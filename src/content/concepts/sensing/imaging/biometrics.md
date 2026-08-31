---
type: concept
slug: biometrics
canonical_name: Biometrics
aliases:
- biometric authentication
- ear biometrics
- liveness detection
- presentation attack detection
- PAD
- injection attack detection
- proof of liveness
parent_concepts:
- imaging
- sensing
related_concepts:
- otoacoustic-emissions
- ear-as-sensing-site
- agent-identity-kya
- edge-ai
sources:
- '[[2023-10-13-e19-trusted-execution-environments]]'
- '[[2026-07-28-proof-of-personhood-competitive-landscape]]'
- '[[2026-07-28-eab-injection-attack-standardisation]]'
- '[[2026-07-28-cen-ts-18099-injection-attack-detection]]'
- '[[2026-07-28-world-enterprise-pivot-and-layoffs]]'
frontier:
- Does proof-of-humanity spend ever reach a sensing modality, or does it stay in remote verification and platform-owned attestation?
- Is there a durable channel where the platform does not own the endpoint (defence comms, contact centres), and can it be priced per seat rather than per device?
- Does passkeys/FIDO2 absorb the "authentication is broken by genAI" thesis before any new modality gets a hearing?
- Does capture-time attestation (C2PA, platform integrity APIs) displace detection outright, and on what timeline? This decides whether deepfake detection is a decade-long market or a transitional one.
- Is there any certification path for a novel modality, or does its absence cap every new sensor at consumer convenience regardless of how good the physics is?
- Does the EAB explainability mandate advantage physics-grounded sensing over black-box classifiers, and is that the one entry point a novel modality has?
last_updated: 2026-07-28
tags:
- concept
mention_count: 17
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-07-28-eab-injection-attack-standardisation
  title: EAB previews biometric injection attack detection standardization developments
  date: '2026-07-01'
  kind: web
- slug: 2026-07-28-world-enterprise-pivot-and-layoffs
  title: World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags
  date: '2026-06-08'
  kind: web
- slug: 2026-07-28-zk-identity-primitives-commoditised
  title: Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages ZKP in the wallet
  date: '2026-04-15'
  kind: web
- slug: 2026-07-28-rivr-phase3-liveness-results
  title: RIVR results show biometric liveness detection effectiveness highly variable
  date: '2026-03-01'
  kind: web
- slug: 2026-07-28-cen-ts-18099-injection-attack-detection
  title: 'CEN/TS 18099: the standard that proves injection attack resilience'
  date: '2026-02-16'
  kind: web
- slug: 2026-07-28-proof-of-personhood-competitive-landscape
  title: Proof-of-personhood competitive landscape — Humanity Protocol pivots out, Billions goes non-biometric
  date: '2026-02-01'
  kind: web
- slug: 2023-10-13-e19-trusted-execution-environments
  title: Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)
  date: '2023-10-13'
  kind: substack
neighbors:
- slug: otoacoustic-emissions
  name: Otoacoustic Emissions
  path: /life-frontier/diagnostics-health/otoacoustic-emissions/
  macro: life-frontier
- slug: ear-as-sensing-site
  name: The ear as a sensing site
  path: /sensing/biosensing/ear-as-sensing-site/
  macro: sensing
- slug: agent-identity-kya
  name: Agent Identity (KYA)
  path: /ai-software/agents/agent-identity-kya/
  macro: ai-software
- slug: edge-ai
  name: Edge AI
  path: /compute/ai-edge/edge-ai/
  macro: compute
---
## The structural fact: the modality is never the business

The biometrics market is not small. Roughly $60–70bn, growing mid-teens. Almost none of that money
has ever gone to whoever owned the modality.

The evidence is company revenue, not market reports:

- **Fingerprint Cards** is the pure-play in the largest modality in biometrics, around a third of the
  market. Revenue SEK 78m in 2025 and a market capitalisation of about **$11m**. Precise Biometrics,
  IDEX and Aware sit in the same microcap band.
- **Face recognition** made zero dollars for any licensor. Apple built Face ID in-house.
- **Voice** is the partial exception at roughly $3bn in 2026, and only because 45% of it is contact
  centres — a channel Apple and Google do not own.
- **Clear Secure** owns no modality at all and does around $880m of revenue, profitably, at a
  multi-billion valuation. It owns enrolled users, airport lanes and a subscription.

**The rule that generalises: a biometric modality only earns money where the platform does not
already own the device.** Fingerprint failed as a business because Apple owned the phone. That places
ear authentication in the fingerprint pattern rather than the voice pattern, because earbuds are
owned by Apple, Samsung, Google and Xiaomi.

## Per-device royalties cap the outcome arithmetically

A licensor charging per device earns units × price, whatever the market is. Global true wireless
earbud shipments were about 332m units in 2024 inside a ~455m personal-audio category. At €1/device,
**one hundred percent of every earbud shipped on earth is €350–400m of revenue.** No licensor has
ever held a whole category, so a realistic ten percent is €35–40m.

## Report-mill sizing is unusable at modality level

Do not put a per-modality TAM in any artefact. In one search on 28 Jul 2026 the same segment (voice)
appeared at $49.8bn by 2029 and at $3.06bn in 2026 — a sixteen-fold disagreement. The quoted "ear
biometrics market" of ~$1.07bn in 2025 almost certainly counts **ear-shape recognition from
photographs**, a forensic and surveillance technique, and not in-ear acoustic authentication, which
has no meaningful commercial revenue anywhere after ten years of NEC pursuing it. Same failure mode
already documented on machine identity at **Agent Identity Value Capture**, where four firms
disagreed 5.5x for the same year.

## Proof of liveness is real growth that lands somewhere else

The deepfake why-now is genuine. Identity verification runs from ~$14bn in 2026 to ~$43bn by 2036 at
13%; deepfake detection specifically from ~$0.85bn in 2025 to ~$7.3bn by 2031, about 43% a year.

But that spend buys **remote** verification: onboarding over video, document-plus-selfie checks,
contact-centre screening. Priced per check, sold to banks and platforms, and the entire premise is
that the channel cannot be trusted. An on-device biometric authenticates you to hardware already in
your hand, which was never the deepfake problem.

Bridging a device biometric to a remote counterparty needs **attestation** — the device signs a claim
the far end trusts — and that is a PKI problem owned by whoever owns the operating system.
[Agent Identity (KYA)](/ai-software/agents/agent-identity-kya/) records how that layer resolves: Google donated AP2 to FIDO, Cloudflare put
Web Bot Auth into the IETF, Coinbase gave x402 to the Linux Foundation. The platforms are
deliberately commoditising attestation to protect the profit pools above it.

So the growth accrues to remote-verification vendors and to platform-owned attestation roots. A new
sensing modality sits outside both.

## Routing

**Public markets is where this is investable.** Screening list, not a recommendation: Mitek (owns
ID R&D), NICE and Verint on contact-centre fraud, Clear Secure on consumer enrolment, Thales on
government ID. Onfido sits inside Entrust; Socure, Persona and iProov are private.

**Insig:** no. Proof-of-humanity in the crypto framing is World, which is token-funded rather than a
revenue business.

**Angel:** the vehicle for anything here, because the outcomes are €250–500m.

---

# State of the art, technical (research pass 28 Jul 2026)

*Added the same day, from an independent literature and standards sweep. The sections above
answer "who captures the value". These answer "what actually works, and what would a new
modality have to clear". They reinforce the same conclusion from a different direction, with
one figure correction flagged below.*

## Which layer of the stack is actually unsolved

Three layers, in very different states. **Matching** (is this the right person, given a genuine
sample) is close to solved for face. **Document validation** is bad. **Liveness** is the
contested middle, and it is where the spend is going.

That ranking is measured rather than asserted. The **Remote Identity Validation Rally**, run by
the Maryland Test Facility for DHS Science & Technology, placed presentation attack detection
between document validation (soberingly poor) and face matching (substantially better)
(rivr phase3 liveness results). The corollary for sizing: the growth is not in
recognising people, it is in proving they exist.

## Two threat models, and the industry's main error

A sample can be faked in two structurally different places, and almost every "liveness
certified" claim in market addresses only the first.

| | Presentation attack | Injection attack |
|---|---|---|
| Where | At the sensor: photo, screen replay, 3D mask | Downstream of it: virtual camera, hooked system calls, manipulated traffic |
| What is faked | A physical artefact | The data stream itself |
| Attacker economics | Physical presence, linear effort | Software, scales to thousands of simultaneous attempts |
| Standard | **ISO/IEC 30107-3:2023** | **CEN/TS 18099:2024** |
| Certification in market | iBeta Level 1/2, widely held | Almost nobody, and only since 2024 |

**Deepfakes mostly arrive by injection.** They are not held up to a camera, so the entire
installed base of iBeta-certified PAD says nothing about them: a product can hold PAD
certification and have zero injection resilience
(cen ts 18099 injection attack detection).

This sharpens the why-now on the section above. The usual claim is that deepfakes got good. The
structural claim is better: **the attack moved from a physical channel that scales linearly to a
software channel that scales freely, while the certification regime stayed pointed at the
physical one.** The standards only started closing that gap in 2024, which dates the window.

### Where the standards stand, July 2026

| Instrument | Body | Status | Covers |
|---|---|---|---|
| ISO/IEC 30107-3:2023 | ISO/IEC | Published, mature, iBeta-tested | Presentation only |
| CEN/TS 18099:2024 | CEN | Published; the only operational injection specification | Injection |
| ISO/IEC 25456 | ISO/IEC | **In development**, based on the CEN work | Injection, internationally |
| ETSI EN 119 461 | ETSI | In force; mandates injection testing with evidence | Remote identity proofing under eIDAS |
| NIST SP 800-63-4 | NIST | Published | Requires resistance to both |

Source: eab injection attack standardisation. Europe leads, and the pull-through
is **regulatory rather than demand-led**: ETSI EN 119 461 sits under eIDAS and the EUDI wallet,
forcing certified remote verification into banking and qualified signatures on a legislated
timetable. This corroborates the routing section above from the other end. The demand is
compliance demand, arriving through remote-verification vendors, and it never reaches a sensor.

### What deployed systems actually score

RIVR Phase 3 tested 6 active and 12 passive liveness systems. Of the twelve passive systems,
three met the false-reject goal and **exactly one** met the attack-rejection threshold (best:
Paravision, 0.5% BPCER / 1.7% APCER in 2.3 s). Discount vendor accuracy claims accordingly.

## The rival paradigm: provenance, not detection

Detection is a classifier arms race in which the side holding the generator iterates against the
detector. The structural alternative is signing content at capture: **C2PA / Content
Credentials**, and on mobile the platform integrity APIs (Play Integrity, App Attest) attesting
that a real sensor produced the frames.

**If attested capture wins, detection becomes the fallback rather than the product**, and the
durable position sits with whoever owns attestation, meaning Apple and Google. This is the same
mechanism [Agent Identity (KYA)](/ai-software/agents/agent-identity-kya/) documents one layer up, and the ~43%/yr deepfake-detection
growth is, read structurally, a bet that injection attacks scale faster than attested capture
rolls out.

## The certification ceiling on any novel modality

Every standard, accredited lab, certification tier and regulatory instrument above is written
for **face, fingerprint and iris**. A new sensing modality has **no certification path at all**.
It cannot be iBeta Level 2 certified because no test protocol exists for it, and it cannot
satisfy ETSI EN 119 461 for the same reason.

This is a second, independent reason for the "modality is never the business" rule above, and a
harder one: it is not a value-chain argument that a clever go-to-market might route around, it
is a gate. A novel modality is **structurally barred from the regulated identity-proofing market
where the growth is**, and confined to device convenience unlocking, where the buyer is an OEM
and the comparison is Face ID. Writing the protocol takes years and is done by committees the
incumbents sit on.

Modality benchmarks for context: voice has **ASVspoof 5**, whose key finding travels well —
zero-shot neural TTS is detected fairly reliably yet remains highly effective as an attack on
speaker verification, so a good detector does not imply a secure system. Fingerprint has
**LivDet**, running since 2009.

## Ear and in-ear acoustic biometrics: the published record

Denser than pitch-deck framing suggests. Mechanism matters and the two get conflated; see
[Otoacoustic Emissions](/life-frontier/diagnostics-health/otoacoustic-emissions/) for why the passive canal transfer function and an active cochlear
emission are different physics selecting different prior art.

| Work | Year | Mechanism | Reported | The catch |
|---|---|---|---|---|
| **EarNet** **2021 Earnet Teoae Biometric Embeddings** | 2021 | TEOAE (true cochlear emission) | EER **0.581% / 0.057%** L/R, fused ID 99.92%, open-set generalisation | Subject count unverified, paywalled |
| **Bilateral ear acoustic** **2022 Bilateral Ear Acoustic Authentication** | 2022 | Canal acoustic, both ears | EER **0.39%**, AUC 0.9995 (vs 1.31% one ear) | Requires a special earphone |
| **Between-class features** **2022 Ear Acoustic Between Class Features** | 2022 | Canal acoustic | FRR **14% at FAR 0.1%**, improved from ~22% | The deployable operating point, and it is bad |
| **EarID** **2025 Earid Ear Canal Biometric Key Extraction** | 2025 | Canal scanning | 98.7% acc, FAR <1%, **226 ms on-earbud**, no classifier | Fuzzy commitment, so no template to steal |
| **EarDynamic** | 2021 | Canal deformation while speaking | Recall 97.38%, F1 96.84% | Needs the user to speak |
| **EarCapAuth** | 2024 | Capacitive eartips | EER 7.62%; FRR 16.14% at FAR 1% | Different sensing entirely |

Three conclusions to carry into any ear-biometrics diligence.

**EER flatters this field badly.** Sub-1% EER and 14% FRR at 0.1% FAR are both true of canal
response, because EER is the crossover point and not where a security product runs. Face ID
operates near a one-in-a-million false accept. Quoting EER alone is how this modality reads
better than it deploys, so **asking for FRR at a fixed security-grade FAR is the single most
useful question in the room**.

**The liveness argument is prior art, not a novelty.** EarNet's authors wrote in 2021 that TEOAE
is immune to replay and falsification because the cochlea must actively generate the signal.
Cochlear-emission liveness pitched as a 2026 insight is five years behind a published paper, and
"Earprint" is already a term of art here (a University of Toronto thesis carries that exact
title).

**The edge-compute layer is not the moat.** EarID enrols in 226 ms on the earbud with no
classifier at all. Differentiation resting on an on-device runtime plus edge inference claims a
layer a 2025 academic paper reached on commodity hardware.

On incumbency, reinforcing the fingerprint-pattern read above: **NEC** has published on ear
acoustic authentication since 2017, shipped a crowdfunded hearable in 2022, and has no OEM
design win a decade on. **Apple** holds a granted 2022 patent on ultrasonic ear-canal echo
identification in AirPods. A specialist that shipped and could not sell it, plus a platform
owner with granted IP and the sockets.

## Unresolved conflict: the deepfake-detection series

The section above quotes deepfake detection at **~$0.85bn in 2025 to ~$7.3bn by 2031, about 43%
a year**. An independent sweep on 28 Jul 2026 could not reproduce that series and found
published estimates for overlapping years differing by an order of magnitude: **$635.7M (2025)
growing to $712.3M (2026)** from one house, against **"$5.5bn in 2023 to $15.7bn by 2026 at
42%"** from another. Those cannot both be true.

**Not a correction to apply, a conflict to resolve** — the $0.85bn/$7.3bn pair may well come
from a specific house's series this sweep did not surface. Until one house's series is quoted
end to end, the 43% CAGR should not go into a memo, an artefact or the newsletter. This is the
same failure mode already logged on **Agent Identity Value Capture** (four firms, 5.5x apart)
and on the voice segment above (16x apart).

The identity-verification headline is firmer: four houses put 2026 at **$14–16bn**, then diverge
from 11.2% to 18.2% CAGR (identity verification market forecasts). The $14bn to
$43bn at 13% figure is Future Market Insights specifically, and it sits at the **conservative**
end of the range.

## Connected