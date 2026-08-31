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
- Once ISO/IEC 25456 publishes, do any of the liveness vendors that passed RIVR Phase 3 on presentation attacks also pass injection-resilience testing, or is the passing set disjoint?
- Does World's per-verification application fee model, introduced June 2026, produce disclosed revenue that justifies Orb manufacturing and per-jurisdiction compliance cost?
- Have any ear-based results been reproduced cross-session and open-set on a verified subject count, given that the EarNet subject count could not be confirmed and the MDPI and arXiv figures were taken from indexed abstracts?
- 'With Google''s ZKP libraries and the EU age-verification blueprint free and open source, what layer of the human identity stack retains pricing power: capture hardware, liveness and injection detection, or nothing?'
- Does proof-of-humanity spend ever reach a sensing modality, or does it stay in remote verification and platform-owned attestation?
- Is there a durable channel where the platform does not own the endpoint (defence comms, contact centres), and can it be priced per seat rather than per device?
- Does passkeys/FIDO2 absorb the "authentication is broken by genAI" thesis before any new modality gets a hearing?
- Does capture-time attestation (C2PA, platform integrity APIs) displace detection outright, and on what timeline? This decides whether deepfake detection is a decade-long market or a transitional one.
- Is there any certification path for a novel modality, or does its absence cap every new sensor at consumer convenience regardless of how good the physics is?
- Does the EAB explainability mandate advantage physics-grounded sensing over black-box classifiers, and is that the one entry point a novel modality has?
last_updated: '2026-08-31'
tags:
- concept
mention_count: 17
scorecard:
  viability: 4
  drivers: 3
  novelty: 2
  diffusion: 3
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
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
**Biometrics is the recognition of people from physical or behavioural traits, and the deployed reality in 2026 is that matching largely works while liveness, injection resilience and commercial capture do not.**

## Summary

Biometrics covers the recognition of individuals from physical and behavioural traits such as fingerprints, face, iris, voice and gait, and is increasingly the default replacement for passwords in device unlock, border control, national ID and financial account protection. A system has three layers that are usually confused with each other: a sensor and feature extractor that turns a body into a template or embedding; a comparison step that produces a match score; and a defence layer that decides whether the thing in front of the sensor is a live human at all, and whether the data reaching the comparison step actually came from that sensor.

The numbers that decide a biometric are operating-point numbers, not accuracy numbers. False accept rate (FAR) and false reject rate (FRR) trade against each other, and equal error rate (EER) is the point where they cross, which is almost never where a security product runs. The ear-acoustic literature is the clearest illustration: sub-1% EER coexists with roughly 22% FRR at a security-grade FAR of 0.1%, improved to about 14% by a dedicated methods paper, against a Face ID FAR of around one in a million **2022 Ear Acoustic Between Class Features**. For the defence layer the equivalent metrics are BPCER (rejecting genuine users) and APCER (accepting attacks), plus a separate question of injection resilience, meaning whether an attacker can bypass the sensor entirely with a virtual camera, hooked system call or manipulated network traffic <sup class="ref"><a href="https://www.iproov.com/blog/cen-ts-18099-standard-proves-injection-attack-resilience" title="CEN/TS 18099: the standard that proves injection attack resilience" rel="noopener">ref</a></sup>.

The live frontier is therefore not new sensing modalities but that defence layer. A US government evaluation run by the Maryland Test Facility for DHS Science and Technology tested six active and twelve passive liveness systems, and of the twelve passive systems exactly one met the APCER threshold; the report places presentation attack detection between document validation (poor) and face matching (substantially better) in the identity stack <sup class="ref"><a href="https://www.biometricupdate.com/202603/rivr-results-show-biometric-liveness-detection-effectiveness-highly-variable" title="RIVR results show biometric liveness detection effectiveness highly variable" rel="noopener">ref</a></sup>. Standards are following: ISO/IEC 30107-3:2023 covers presentation attacks only, CEN/TS 18099:2024 is the only published specification that proves injection resilience, ISO/IEC 25456 is in development, and ETSI EN 119 461 already mandates injection-attack testing with documented evidence <sup class="ref"><a href="https://www.biometricupdate.com/202607/eab-previews-biometric-injection-attack-detection-standardization-developments" title="EAB previews biometric injection attack detection standardization developments" rel="noopener">ref</a></sup>.

Alongside this, exotic modalities keep being reintroduced as novel. Transient evoked otoacoustic emission identity, including the liveness-by-construction argument that you cannot replay a signal the cochlea must actively generate, was published as a University of Toronto thesis in 2014 with 99.44% identification and 0.02% EER on both-ear fusion **2014 Liu Earprint Teoae Biometrics Thesis**, and again with proper verification metrics in 2021 **2021 Earnet Teoae Biometric Embeddings**. Anyone assessing a biometrics pitch should check the prior art, the operating point rather than the EER, and whether the claim covers injection as well as presentation attacks.

## Viability (4/5)

The core recognition function works. The RIVR Phase 3 evaluation explicitly ranks face matching as substantially better than liveness detection, which in turn is better than document validation <sup class="ref"><a href="https://www.biometricupdate.com/202603/rivr-results-show-biometric-liveness-detection-effectiveness-highly-variable" title="RIVR results show biometric liveness detection effectiveness highly variable" rel="noopener">ref</a></sup>, and one vendor has issued over 475 million iris-based identity proofs to more than 18 million verified people across 160 countries <sup class="ref"><a href="https://www.biometricupdate.com/202606/world-shifts-from-crypto-identity-experiment-to-enterprise-proof-of-humanity" title="World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags" rel="noopener">ref</a></sup>. That is demonstrated field performance, not a lab result.

The defence layer is where viability breaks. Only one of twelve passive liveness systems met the APCER threshold in the only independent benchmark of deployed systems, and the best reported combination was 0.5% BPCER with 1.7% APCER at 2.3 seconds <sup class="ref"><a href="https://www.biometricupdate.com/202603/rivr-results-show-biometric-liveness-detection-effectiveness-highly-variable" title="RIVR results show biometric liveness detection effectiveness highly variable" rel="noopener">ref</a></sup>; that benchmark covers presentation attacks only and tests nothing about injection <sup class="ref"><a href="https://www.biometricupdate.com/202607/eab-previews-biometric-injection-attack-detection-standardization-developments" title="EAB previews biometric injection attack detection standardization developments" rel="noopener">ref</a></sup>. A vendor can hold PAD certification and have zero injection resilience <sup class="ref"><a href="https://www.iproov.com/blog/cen-ts-18099-standard-proves-injection-attack-resilience" title="CEN/TS 18099: the standard that proves injection attack resilience" rel="noopener">ref</a></sup>. Novel modalities are further back still: ear-canal acoustic authentication still rejects roughly one in seven legitimate users at FAR 0.1% after a paper written specifically to fix that **2022 Ear Acoustic Between Class Features**. Score reflects a mature core with a measured, unsolved perimeter.

**TLDR: Matching is close to solved and deployed at scale; the liveness and injection layers demonstrably are not.**

## Drivers (3/5)

Demand side: biometrics is displacing passwords as the preferred authentication approach across smartphones, border security, national ID and financial accounts, with the skills shortage explicit enough for NSF to fund a dedicated undergraduate research site at $450,000. Regulation is a harder driver than fraud narratives: ETSI EN 119 461 already mandates injection-attack testing across face-to-face, remote-assisted and unattended remote identification, and eIDAS 2.0 encourages privacy-enhancing technologies in the wallet <sup class="ref"><a href="https://www.biometricupdate.com/202607/eab-previews-biometric-injection-attack-detection-standardization-developments" title="EAB previews biometric injection attack detection standardization developments" rel="noopener">ref</a></sup>, <sup class="ref"><a href="https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/" title="Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages " rel="noopener">ref</a></sup>. The structural why-now on the attack side is that injection attacks are software and scale to thousands of simultaneous attempts, whereas presentation attacks require physical presence <sup class="ref"><a href="https://www.iproov.com/blog/cen-ts-18099-standard-proves-injection-attack-resilience" title="CEN/TS 18099: the standard that proves injection attack resilience" rel="noopener">ref</a></sup>.

Supply and monetisation are the weak half. The best-capitalised, best-distributed proof-of-personhood vendor, valued at $2.5bn with Zoom, Tinder, DocuSign and Okta as named partners, restructured a roughly 500-person team on 8 June 2026 because revenue had not kept pace with hardware and compliance costs, and only introduced per-verification application fees in June 2026 <sup class="ref"><a href="https://www.biometricupdate.com/202606/world-shifts-from-crypto-identity-experiment-to-enterprise-proof-of-humanity" title="World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags" rel="noopener">ref</a></sup>. Fraud-side growth numbers driving the demand story are largely vendor-published and uncheckable, including a claimed 495% increase in deepfake identity fraud in 2026 and 740% growth in iOS injection attacks during 2025, <sup class="ref"><a href="https://www.iproov.com/blog/cen-ts-18099-standard-proves-injection-attack-resilience" title="CEN/TS 18099: the standard that proves injection attack resilience" rel="noopener">ref</a></sup>.

**TLDR: Regulatory mandates and software-scale fraud pull hard on demand; the leading vendor still cannot convert it into revenue.**

## Novelty (2/5)

Very little in these sources is new. Otoacoustic-emission identity and its entire security framing, including the liveness and anti-replay argument and the term 'earprint' itself, were published in 2014 with 0.02% EER on both-ear fusion **2014 Liu Earprint Teoae Biometrics Thesis**, and restated with authentication metrics and an open-set claim in 2021 at 0.057% EER for the right ear and 99.92% fused identification accuracy **2021 Earnet Teoae Biometric Embeddings**. The edge-compute story is also already met: an October 2025 system extracts a stable binary key from the ear canal on the earbud itself in 226 ms with no classifier, reporting 98.7% accuracy and FAR below 1% **2025 Earid Ear Canal Biometric Key Extraction**. That fuzzy-commitment architecture is strictly better than storing embeddings, because there is no template to leak.

Where something is genuinely better than what came before, the margins are modest and well characterised. Bilateral ear fusion buys roughly a 3x error reduction over one ear, 0.39% EER against 1.31% **2022 Bilateral Ear Acoustic Authentication**. Between-class features improve the security-grade operating point by 7.95 points of FRR **2022 Ear Acoustic Between Class Features**. Meanwhile the privacy primitives that would differentiate a product have been commoditised by the platforms and the regulator: Google open-sourced its zero-knowledge-proof libraries under Apache 2.0, the EU shipped an open-source age-verification blueprint behind the app announced 15 April 2026, and ZKPassport covers over 120 countries free and open source <sup class="ref"><a href="https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/" title="Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages " rel="noopener">ref</a></sup>. The defensible novelty left is injection-attack detection and its test methodology, which is early enough that the standard is still in development <sup class="ref"><a href="https://www.biometricupdate.com/202607/eab-previews-biometric-injection-attack-detection-standardization-developments" title="EAB previews biometric injection attack detection standardization developments" rel="noopener">ref</a></sup>.

**TLDR: The category is old, the exotic modalities are older than their pitches, and the privacy layer is being given away free.**

## Diffusion (3/5)

Diffusion is already deep in some segments and reversing in others. Identity verification is an observable $14-16bn market in 2026 across four independent houses, roughly 56% cloud-deployed and 32.7% BFSI by vertical, and iris-based proof-of-personhood reached 1,500 Orbs live in 23 countries with a US launch on 1 May 2026 <sup class="ref"><a href="https://www.biometricupdate.com/202606/world-shifts-from-crypto-identity-experiment-to-enterprise-proof-of-humanity" title="World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags" rel="noopener">ref</a></sup>. That is real distribution.

The adoption barriers are consent, cost and error rates. The number-two proof-of-personhood vendor, with over 8 million palm-based Human IDs, abandoned the category in February 2026 for a verifiable-credential network, while a $30m-funded competitor positions explicitly against 'invasive biometric scans' using passport NFC and zero-knowledge proofs instead <sup class="ref"><a href="https://www.biometricupdate.com/202602/humanity-protocol-pivots-from-proof-of-personhood-but-sticks-with-palm-biometrics" title="Proof-of-personhood competitive landscape — Humanity Protocol pivots out, Billions goes non-biometric" rel="noopener">ref</a></sup>. Hardware-based capture carries manufacturing, deployment and per-jurisdiction compliance costs that outran revenue at the category leader <sup class="ref"><a href="https://www.biometricupdate.com/202606/world-shifts-from-crypto-identity-experiment-to-enterprise-proof-of-humanity" title="World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags" rel="noopener">ref</a></sup>. For new modalities the barrier is arithmetic: no consumer product ships an authenticator that rejects one user in seven at a usable FAR <sup class="ref"><a href="https://www.biometricupdate.com/202607/eab-previews-biometric-injection-attack-detection-standardization-developments" title="EAB previews biometric injection attack detection standardization developments" rel="noopener">ref</a></sup>, **2022 Ear Acoustic Between Class Features**. Fragmented certification, with PAD certification not covering injection, adds procurement friction on top <sup class="ref"><a href="https://www.iproov.com/blog/cen-ts-18099-standard-proves-injection-attack-resilience" title="CEN/TS 18099: the standard that proves injection attack resilience" rel="noopener">ref</a></sup>.

**TLDR: Ubiquitous in device unlock and identity verification, but the biometric-first identity vendors are retreating from biometrics.**

## Impact (3/5)

The stakes are substantive: biometrics gates devices, facilities, borders, national identification and financial accounts, and the observable base market for identity verification is $14-16bn in 2026 with houses disagreeing only on growth, between 11.2% and 18.2% CAGR. Because liveness sits in the middle of the stack as the weakest measured link, spend concentrating there is a structurally coherent expectation rather than an assertion <sup class="ref"><a href="https://www.biometricupdate.com/202603/rivr-results-show-biometric-liveness-detection-effectiveness-highly-variable" title="RIVR results show biometric liveness detection effectiveness highly variable" rel="noopener">ref</a></sup>. Bot farms using real human workers to defeat anti-bot protections, now the subject of a $471,822 NSF award, give an additional reason why proving a live, unique human has economic value.

Value capture is the constraint on the score. Adjacent decentralised-identity forecasts are unusable, disagreeing 6.5x on the same year with CAGRs between 51% and 80%, while the one layer-specific number is small: zero-knowledge KYC at $83.6m in 2025 rising to $903.5m by 2032. Regulators and platforms are donating the privacy layer, making it a compliance expectation rather than a differentiator <sup class="ref"><a href="https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/" title="Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages " rel="noopener">ref</a></sup>, and the leading biometric vendor's layoffs are harder evidence than any forecast that the value is not yet reaching the people building the sensors <sup class="ref"><a href="https://www.biometricupdate.com/202606/world-shifts-from-crypto-identity-experiment-to-enterprise-proof-of-humanity" title="World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags" rel="noopener">ref</a></sup>.

**TLDR: A real, measurable market with genuine security stakes, but the sources show value leaking to free primitives rather than accruing to vendors.**

## Timing Now (0-2yr)

There is nothing speculative about the timing of core biometrics. Face and iris matching are deployed at hundreds of millions of transactions, the US launch of the largest proof-of-personhood network was 1 May 2026, and the identity verification market is being measured rather than projected <sup class="ref"><a href="https://www.biometricupdate.com/202606/world-shifts-from-crypto-identity-experiment-to-enterprise-proof-of-humanity" title="World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags" rel="noopener">ref</a></sup>,. What is in motion over the next two years is the defence layer: CEN/TS 18099:2024 is published, ISO/IEC 25456 is in development with weighted attack-complexity levels expected, and the European Association for Biometrics is working on capture-environment vulnerability methodology and explainability requirements for deepfake and injection detection <sup class="ref"><a href="https://www.biometricupdate.com/202607/eab-previews-biometric-injection-attack-detection-standardization-developments" title="EAB previews biometric injection attack detection standardization developments" rel="noopener">ref</a></sup>.

The exception is exotic modalities. Ear-canal and otoacoustic authentication have been in the literature since at least 2014 and still sit at security-grade operating points no consumer product would tolerate **2014 Liu Earprint Teoae Biometrics Thesis**, **2022 Ear Acoustic Between Class Features**. On the evidence here their timing is unclear rather than soon, and twelve years of published prior art without a shipped product is itself the signal.

**TLDR: Deployment is already happening; the contested liveness and injection layer is being standardised and independently benchmarked right now.**

## Overrated or underrated? Fairly rated

Split the category and the picture is consistent. Biometric matching is fairly rated: it works, it is deployed, the independent benchmark says so, and the market for it is one of the few in this space where four forecasting houses agree on the base <sup class="ref"><a href="https://www.biometricupdate.com/202603/rivr-results-show-biometric-liveness-detection-effectiveness-highly-variable" title="RIVR results show biometric liveness detection effectiveness highly variable" rel="noopener">ref</a></sup>,. Injection attack detection is arguably underrated, because it is the only layer with a published operational standard, an ISO successor in development, an existing ETSI mandate and a structural argument for why attacks scale that does not depend on deepfake quality improving <sup class="ref"><a href="https://www.biometricupdate.com/202607/eab-previews-biometric-injection-attack-detection-standardization-developments" title="EAB previews biometric injection attack detection standardization developments" rel="noopener">ref</a></sup>, <sup class="ref"><a href="https://www.iproov.com/blog/cen-ts-18099-standard-proves-injection-attack-resilience" title="CEN/TS 18099: the standard that proves injection attack resilience" rel="noopener">ref</a></sup>.

Two things are clearly overrated. Biometric proof-of-personhood as a business: the leader has $2.5bn of valuation, 18 million verified humans and layoffs in the same year, and the number-two player left the category entirely <sup class="ref"><a href="https://www.biometricupdate.com/202606/world-shifts-from-crypto-identity-experiment-to-enterprise-proof-of-humanity" title="World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags" rel="noopener">ref</a></sup>, <sup class="ref"><a href="https://www.biometricupdate.com/202602/humanity-protocol-pivots-from-proof-of-personhood-but-sticks-with-palm-biometrics" title="Proof-of-personhood competitive landscape — Humanity Protocol pivots out, Billions goes non-biometric" rel="noopener">ref</a></sup>. And novel ear-based modalities: the liveness pitch, the name and the headline error rates are all prior art from 2014 and 2021, the edge-compute and template-privacy arguments were closed by an October 2025 paper, and the honest operating point is roughly 14% FRR at 0.1% FAR against Face ID's four-orders-of-magnitude better FAR **2014 Liu Earprint Teoae Biometrics Thesis**, **2025 Earid Ear Canal Biometric Key Extraction**, **2022 Ear Acoustic Between Class Features**. Treat any EER-only claim as a flattering operating point until FRR at FAR 0.1% is stated.

## Prediction

By 31 December 2028, no ear-acoustic or otoacoustic authentication system will have been independently benchmarked (by a body such as the Maryland Test Facility or an iBeta-equivalent lab) at an FRR below 5% at FAR 0.1%.

## Evidence base

- In the only independent benchmark of deployed liveness systems, run by the Maryland Test Facility for DHS S&T, only two of six active systems met the BPCER threshold and exactly one of twelve passive systems met APCER; the best result was 0.5% BPCER, 1.7% APCER, 2.3 s (Mar 2026 reporting) <sup class="ref"><a href="https://www.biometricupdate.com/202603/rivr-results-show-biometric-liveness-detection-effectiveness-highly-variable" title="RIVR results show biometric liveness detection effectiveness highly variable" rel="noopener">ref</a></sup>.
- CEN/TS 18099:2024 is the only published specification proving injection resilience, ISO/IEC 25456 is in development, ETSI EN 119 461 already mandates injection-attack testing, and a report-mill forecast puts injection attacks above 4 billion by 2028 (Jul 2026) <sup class="ref"><a href="https://www.biometricupdate.com/202607/eab-previews-biometric-injection-attack-detection-standardization-developments" title="EAB previews biometric injection attack detection standardization developments" rel="noopener">ref</a></sup>.
- World held a $2.5bn valuation, 18M+ Orb-verified humans, 475M+ proofs and 1,500+ Orbs in 23 countries, and restructured a ~500-person team on 8 June 2026 because revenue lagged Orb manufacturing and compliance costs <sup class="ref"><a href="https://www.biometricupdate.com/202606/world-shifts-from-crypto-identity-experiment-to-enterprise-proof-of-humanity" title="World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags" rel="noopener">ref</a></sup>.
- Humanity Protocol abandoned proof-of-personhood in February 2026 after 8M+ palm-based Human IDs, while Billions raised $30m positioning explicitly against invasive biometric scans using passport NFC plus zero-knowledge proofs <sup class="ref"><a href="https://www.biometricupdate.com/202602/humanity-protocol-pivots-from-proof-of-personhood-but-sticks-with-palm-biometrics" title="Proof-of-personhood competitive landscape — Humanity Protocol pivots out, Billions goes non-biometric" rel="noopener">ref</a></sup>.
- Ear-canal acoustic authentication's baseline is ~22% FRR at FAR 0.1%, improved to ~14% by a dedicated methods paper (arXiv 2205.08778, May 2022), against a Face ID FAR of roughly one in 1,000,000 **2022 Ear Acoustic Between Class Features**.
- Otoacoustic-emission identity with the liveness and anti-replay argument, 99.44% identification and 0.02% EER on both-ear fusion, was published in a 2014 University of Toronto thesis titled 'Earprint' **2014 Liu Earprint Teoae Biometrics Thesis**.
- Four houses put the 2026 identity verification market at $14-16bn but diverge from 11.2% to 18.2% CAGR, changing the 2033 answer by ~2.4x; cloud is ~56% of deployment and BFSI ~32.7% of verticals (accessed 28 Jul 2026).

## Open questions

- Once ISO/IEC 25456 publishes, do any of the liveness vendors that passed RIVR Phase 3 on presentation attacks also pass injection-resilience testing, or is the passing set disjoint?
- Does World's per-verification application fee model, introduced June 2026, produce disclosed revenue that justifies Orb manufacturing and per-jurisdiction compliance cost?
- Have any ear-based results been reproduced cross-session and open-set on a verified subject count, given that the EarNet subject count could not be confirmed and the MDPI and arXiv figures were taken from indexed abstracts?
- With Google's ZKP libraries and the EU age-verification blueprint free and open source, what layer of the human identity stack retains pricing power: capture hardware, liveness and injection detection, or nothing?

---
*Assessment drafted 2026-08-31 from up to 16 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
