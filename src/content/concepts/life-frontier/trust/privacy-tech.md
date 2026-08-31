---
type: concept
slug: privacy-tech
canonical_name: Privacy Technology
aliases:
- privacy-enhancing technologies
- PETs
- privacy tech
parent_concepts:
- trust
related_concepts: []
sources:
- '[[2023-06-08-three-overrated-technologies-from]]'
- '[[2023-05-20-interview-jordan-brandt-ceo-of-inpher]]'
- '[[2023-10-19-e20-the-state-of-privacy-enhancing]]'
- '[[2023-02-05-interview-flavio-bergamaschi-private]]'
- '[[2023-09-28-e16-in-conversation-with-shiv-malik]]'
- '[[2021-07-21-why-privacy-tech-is-actually-collaborative]]'
- '[[2025-02-05-you-like-ai-agents-you-are-gonna]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2022-12-15-im-doing-research-in-venture-capital]]'
- '[[2023-10-13-e19-trusted-execution-environments]]'
- '[[2023-01-05-interview-christine-huang-data-privacy]]'
- '[[2023-07-06-e07-decentralised-ai]]'
- '[[2022-12-15-unbundling-the-database]]'
- '[[2023-03-05-interview-dr-hyoduk-shin-professor]]'
- '[[2023-04-05-interview-stijn-christiaens-ceo-of]]'
- '[[2023-05-05-interview-rick-hao-partner-at-speedinvest]]'
- '[[2026-07-28-zk-identity-primitives-commoditised]]'
frontier:
- What are the actual performance overheads of FHE, MPC and TEE-based analytics versus plaintext computation, and does the unified stack under NSF development close them enough for production pipelines?
- Does eIDAS 2.0's encouragement of ZKPs harden into a requirement, and do member state wallets adopt the open-sourced Google or EU implementations rather than building their own?
- 'If the privacy primitives are free, where does the revenue sit: cloud infrastructure, governance and workflow software, or verticalised data collaboration networks?'
- Has any organisation publicly reported a data collaboration deployment that crossed an organisational boundary and produced measurable revenue, as opposed to a pilot?
- Does a unified abstraction layer over cryptographic and hardware-based secure computation achieve measurable throughput or latency gains over hand-tuned single-primitive deployments, and on which workload classes?
- 'If ZKP identity primitives are commoditised and mandated by eIDAS 2.0, where does defensible value accrue: wallet distribution, credential issuance, or verification networks?'
- Has any PET vendor demonstrated repeatable revenue from cross-organisational data collaboration, as opposed to intra-organisational deployment, and in which verticals?
- Do the cultural barriers to data sharing identified in 2023 interviews persist in 2026 deployments, or has regulatory mandate substituted for voluntary trust-building?
last_updated: '2026-08-31'
tags:
- concept
- seeded-stub
mention_count: 20
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Overrated
scorecard_status: draft
sources_7d: 1
sources_30d: 1
recent_mentions:
- slug: 2026-07-28-zk-identity-primitives-commoditised
  title: Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages ZKP in the wallet
  date: '2026-04-15'
  kind: web
- slug: 2025-10-09-a-specific-theory-of-sovereign-ai
  title: A Specific Theory of Sovereign AI
  date: '2025-10-09'
  kind: substack
- slug: 2025-02-05-you-like-ai-agents-you-are-gonna
  title: Decentralised AI (Feat. Richard Blythman of Naptha)
  date: '2025-02-05'
  kind: substack
- slug: 2023-10-19-e20-the-state-of-privacy-enhancing
  title: Understanding Privacy Enhancing Technology (Feat. Karim Eldefrawy, Confidencial.io)
  date: '2023-10-19'
  kind: substack
- slug: 2023-10-13-e19-trusted-execution-environments
  title: Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)
  date: '2023-10-13'
  kind: substack
- slug: 2023-09-28-e16-in-conversation-with-shiv-malik
  title: '☎️ E17: In Conversation with Shiv Malik, CEO of Pool.io on the State of Data Unions 🤝₿'
  date: '2023-09-28'
  kind: substack
- slug: 2023-07-06-e07-decentralised-ai
  title: '🔮E07: Decentralised AI'
  date: '2023-07-06'
  kind: substack
- slug: 2023-06-08-three-overrated-technologies-from
  title: '💡E03: Three Overrated Technologies from the Future Fusion, Bitcoin & LEO Internet + Ultrasound for Hibernation; Wind Power; Skeletal Editing; Carbon Pricing; & Psychedelics++'
  date: '2023-06-08'
  kind: substack
neighbors: []
---
**Privacy technology is the family of techniques that keep data confidential while it is being used rather than only at rest or in transit, and after a decade as a research category it is now shipping first at the identity layer, where the core primitives are being given away free by platforms and regulators.**

## Summary

Privacy technology, usually called privacy-enhancing technologies (PETs), covers secure multiparty computation (MPC), fully homomorphic encryption (FHE), zero-knowledge proofs (ZKPs), verifiable computing, trusted execution environments (TEEs) and private information retrieval (PIR). The framing that makes the category coherent is simple: in a normal online interaction, data on the device can be encrypted and data moving between device and server is protected by TLS, but data being processed on the server is not protected at all. PETs are the attempts to close that third gap, either cryptographically (MPC, FHE, ZKP) or in hardware (TEEs, marketed as confidential computing) <sup class="ref"><a href="https://stateofthefuture.substack.com/p/why-privacy-tech-is-actually-collaborative" title="💡Collaborative Computing" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e19-trusted-execution-environments" title="Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)" rel="noopener">ref</a></sup>.

The commercial thesis attached to this stack has been that securing processing unlocks data collaboration between organisations that today cannot legally or commercially share data, creating a new market variously called collaborative computing <sup class="ref"><a href="https://stateofthefuture.substack.com/p/why-privacy-tech-is-actually-collaborative" title="💡Collaborative Computing" rel="noopener">ref</a></sup>. A related line of argument extends the same primitives into database architecture, where secure enclaves and fast PIR would give a query engine that never sees the query or the data <sup class="ref"><a href="https://stateofthefuture.substack.com/p/unbundling-the-database" title="💡Thesis: Unbundling the Database: Serverless, Edge and Secure" rel="noopener">ref</a></sup>.

The parameters that decide it are three. First, performance and engineering integration: as of May 2026 the problem of making cryptographic and hardware PETs interoperable, distributable and cost-optimisable was still the subject of a fresh NSF CAREER award, which tells you the unified stack does not exist yet. Second, demand structure: practitioners interviewed across 2023 consistently located the blocker outside the technology, in culture, incentives, risk asymmetry and the number of internal stakeholders who must agree <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-christine-huang-data-privacy" title="☎️ Interview: Christine Huang, Data Privacy & Protection at SAP on the State of Privacy-Enhancing Technologies #001" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-flavio-bergamaschi-private" title="☎️ Interview: Flavio Bergamaschi, Private AI and Analytics at Intel on the State of Privacy-Enhancing Technologies #002" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-stijn-christiaens-ceo-of" title="☎️ Interview: Stijn Christiaens, CEO of Collibra on the State of Privacy-Enhancing Technologies #004" rel="noopener">ref</a></sup>. Third, value capture: in the one place where PETs have reached consumers, the primitives are being open-sourced by Google and by the European Commission itself, which makes privacy a compliance baseline rather than a product <sup class="ref"><a href="https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/" title="Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages " rel="noopener">ref</a></sup>.

The practical consequence is that "privacy technology" now needs splitting into two very different things: a shipping, regulator-driven ZK identity layer, and an enterprise secure-analytics market that has been three years away for at least five years.

## Viability (3/5)

The general-purpose side is weaker. An NSF CAREER award dated 13 May 2026 funds software abstractions, a distributed fault-tolerant runtime and a cost-based optimiser to make FHE, MPC and TEEs usable in one pipeline, worth $422,683. The existence of that project in 2026 is the clearest available signal that scalable, deployable secure analytics remains unsolved engineering rather than a productisation exercise, consistent with a 2023 practitioner account of why MPC, ZKP and FHE struggle for adoption and why selective rather than blanket encryption is the pragmatic route <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e20-the-state-of-privacy-enhancing" title="Understanding Privacy Enhancing Technology (Feat. Karim Eldefrawy, Confidencial.io)" rel="noopener">ref</a></sup>. Sources contain no benchmark numbers, so the size of the remaining performance gap cannot be assessed here.

**TLDR: ZK identity works and is in app stores; general secure analytics is still a funded research problem in 2026.**

## Drivers (3/5)

Demand: eIDAS 2.0 encourages privacy-enhancing technologies including ZKPs in the wallet, which converts the primitive from a differentiator into an expectation, and the EU shipped an age-verification blueprint and app in April 2026 <sup class="ref"><a href="https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/" title="Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages " rel="noopener">ref</a></sup>. Outside identity, the demand case in the sources is argued rather than demonstrated: more data continues to be a business driver and machine learning is expected to be the main catalyst for data-sharing tools <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-rick-hao-partner-at-speedinvest" title="☎️ Interview: Rick Hao, Partner at SpeedInvest on the State of Privacy-Enhancing Technologies #005" rel="noopener">ref</a></sup>; incumbents holding monolithic data estates are said to carry all the data risk, making federation inevitable <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-jordan-brandt-ceo-of-inpher" title=" ☎️ Interview: Jordan Brandt, CEO of Inpher on the State of Privacy-Enhancing Technologies" rel="noopener">ref</a></sup>. Counterweight: the same interview series repeatedly identifies data sharing as cultural rather than technical, and expects global data-sharing rules to remain unlikely because of differing values <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-christine-huang-data-privacy" title="☎️ Interview: Christine Huang, Data Privacy & Protection at SAP on the State of Privacy-Enhancing Technologies #001" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-dr-hyoduk-shin-professor" title="☎️ Interview: Dr Hyoduk Shin, Professor of Innovation at UC San Diego on the State of Privacy-Enhancing Technologies #00" rel="noopener">ref</a></sup>.

Supply: the constraint is loosening fast in identity, because the platforms and the regulator are both giving the code away, and the stated pattern is that commoditising a layer protects a profit pool above or below it, the same mechanism used when Google donated AP2 to FIDO, Cloudflare put Web Bot Auth into the IETF and Coinbase gave x402 to the Linux Foundation <sup class="ref"><a href="https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/" title="Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages " rel="noopener">ref</a></sup>. On the analytics side supply is still constrained by scarce cryptography and systems engineering, which is what public research money is being pointed at.

**TLDR: Regulation is the only hard demand driver in the sources, and it is concentrated in identity; supply is now free.**

## Novelty (3/5)

The thing PETs are better than is the status quo of encrypting storage and transport and leaving processing in the clear, which is the whole basis of the category <sup class="ref"><a href="https://stateofthefuture.substack.com/p/why-privacy-tech-is-actually-collaborative" title="💡Collaborative Computing" rel="noopener">ref</a></sup>. In identity the comparison is sharper: a ZKP-based age attestation replaces handing over a document or a full identity record, and no conventional alternative achieves that, which is why the regulator has written the primitive into its own reference implementation <sup class="ref"><a href="https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/" title="Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages " rel="noopener">ref</a></sup>. TEEs are a distinct claim again, offering confidentiality and integrity in mainstream cloud hardware rather than through cryptography <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e19-trusted-execution-environments" title="Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)" rel="noopener">ref</a></sup>, and one practitioner argues integrity matters as much as confidentiality and that crypto-agility is systematically underrated <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-flavio-bergamaschi-private" title="☎️ Interview: Flavio Bergamaschi, Private AI and Analytics at Intel on the State of Privacy-Enhancing Technologies #002" rel="noopener">ref</a></sup>.

What the sources do not provide is magnitude. There are no throughput, latency or cost figures for FHE, MPC or PIR against plaintext computation anywhere in this evidence base, and the fact that a 2026 research project is still building the cost-modelling framework needed to choose between these technologies implies the tradeoff space is not yet even well characterised. The relevant caution from an adjacent interview is that a 5x technical improvement can still lose to the risk and cost of acting on it <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-stijn-christiaens-ceo-of" title="☎️ Interview: Stijn Christiaens, CEO of Collibra on the State of Privacy-Enhancing Technologies #004" rel="noopener">ref</a></sup>. Novelty is real; the score is held at 3 because it is unquantified here.

**TLDR: A genuinely new capability against the encryption-at-rest plus TLS baseline, but the sources quantify none of the improvement.**

## Diffusion (2/5)

The barriers are unusually well specified in the sources and they are not technical. Selling data collaboration software means convincing five distinct groups inside the buyer <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-flavio-bergamaschi-private" title="☎️ Interview: Flavio Bergamaschi, Private AI and Analytics at Intel on the State of Privacy-Enhancing Technologies #002" rel="noopener">ref</a></sup>; the vendor is competing against non-consumption, and even a large performance gain can be refused because the downside risk of sharing data is larger <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-stijn-christiaens-ceo-of" title="☎️ Interview: Stijn Christiaens, CEO of Collibra on the State of Privacy-Enhancing Technologies #004" rel="noopener">ref</a></sup>; alignment must be reached across legal, compliance, technology and business before a single supplier is onboarded <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-christine-huang-data-privacy" title="☎️ Interview: Christine Huang, Data Privacy & Protection at SAP on the State of Privacy-Enhancing Technologies #001" rel="noopener">ref</a></sup>; culture is named as the most important driver ahead of technology, with a globally fragmented data economy the expected end state <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-dr-hyoduk-shin-professor" title="☎️ Interview: Dr Hyoduk Shin, Professor of Innovation at UC San Diego on the State of Privacy-Enhancing Technologies #00" rel="noopener">ref</a></sup>. A vertical go-to-market is also argued to be sub-optimal, which removes the usual beachhead strategy <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-jordan-brandt-ceo-of-inpher" title=" ☎️ Interview: Jordan Brandt, CEO of Inpher on the State of Privacy-Enhancing Technologies" rel="noopener">ref</a></sup>, while healthcare is expected to need its own infrastructure rather than the general one <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-rick-hao-partner-at-speedinvest" title="☎️ Interview: Rick Hao, Partner at SpeedInvest on the State of Privacy-Enhancing Technologies #005" rel="noopener">ref</a></sup>.

The identity path diffuses differently and better, because distribution is the wallet and the mandate comes from eIDAS 2.0 rather than a sales cycle, and because the implementation cost has been driven towards zero by Google's Apache 2.0 release and the EU's own blueprint <sup class="ref"><a href="https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/" title="Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages " rel="noopener">ref</a></sup>. Note that this is diffusion of a capability, not of a business. The score reflects the enterprise case, where five years of sources show diagnosis without resolution.

**TLDR: Free primitives will spread through wallets; enterprise adoption is blocked by culture, stakeholder count and risk asymmetry, all documented and none solved.**

## Impact (3/5)

The upside claim is that securing processing lets organisations combine data across boundaries, maximising the value of data assets for private and public benefit, described as the next trillion-dollar market <sup class="ref"><a href="https://stateofthefuture.substack.com/p/why-privacy-tech-is-actually-collaborative" title="💡Collaborative Computing" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-jordan-brandt-ceo-of-inpher" title=" ☎️ Interview: Jordan Brandt, CEO of Inpher on the State of Privacy-Enhancing Technologies" rel="noopener">ref</a></sup>. That number is advocacy from the publication's own thesis and should not be treated as evidence. The nearest independent-ish scale anchor in the sources is a data broker market put at $250bn against a machine-learning market of roughly $40bn, used to argue that data intermediation is the larger prize <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e16-in-conversation-with-shiv-malik" title="☎️ E17: In Conversation with Shiv Malik, CEO of Pool.io on the State of Data Unions 🤝₿" rel="noopener">ref</a></sup>.

**TLDR: Large if data collaboration actually unlocks, but the trillion-dollar figure in the sources is the authors' own thesis, not measured demand.**

## Timing Now (0-2yr)

Something is shipping now. The European age-verification app was announced on 15 April 2026, its blueprint is open source, Google's ZKP libraries were released under Apache 2.0, and ZKPassport is already in both app stores across 120-plus countries <sup class="ref"><a href="https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/" title="Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages " rel="noopener">ref</a></sup>. If you are asking when privacy technology first touches ordinary users at scale, the answer is the current cycle, driven by eIDAS 2.0 rather than by product demand.

The collaborative computing market is on a different and undated clock. It was declared ready for investment around 2022 <sup class="ref"><a href="https://stateofthefuture.substack.com/p/im-doing-research-in-venture-capital" title="🔮 I’m doing research in venture capital, AMA" rel="noopener">ref</a></sup>, the obstacles were catalogued through 2023 as cultural and organisational <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-christine-huang-data-privacy" title="☎️ Interview: Christine Huang, Data Privacy & Protection at SAP on the State of Privacy-Enhancing Technologies #001" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-stijn-christiaens-ceo-of" title="☎️ Interview: Stijn Christiaens, CEO of Collibra on the State of Privacy-Enhancing Technologies #004" rel="noopener">ref</a></sup>, and by May 2026 the integration layer was still receiving early-career research funding. The publication's own hype-cycle test is apposite: the hard part of any inevitable technology is the "now" <sup class="ref"><a href="https://stateofthefuture.substack.com/p/three-overrated-technologies-from" title="💡E03: Three Overrated Technologies from the Future Fusion, Bitcoin & LEO Internet + Ultrasound for Hibernation; Wind Pow" rel="noopener">ref</a></sup>. On this evidence the analytics half fails that test and no responsible date can be put on it.

**TLDR: The ZK identity layer is live in 2026; the enterprise secure-analytics market is not, and the sources do not date it.**

## Overrated or underrated? Overrated

As a capability, privacy technology is real and, in identity, already deployed. As the venture category described in these sources, a trillion-dollar collaborative computing market unlocked by PETs, it is overrated on the evidence available. Two things support that call. First, the timeline: the thesis was declared investment-ready in 2022, the blockers documented in 2023 were cultural, incentive-based and organisational rather than technical, and by 2026 the technical layer that would make the products deployable was still being built with a $422,683 research grant <sup class="ref"><a href="https://stateofthefuture.substack.com/p/im-doing-research-in-venture-capital" title="🔮 I’m doing research in venture capital, AMA" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-dr-hyoduk-shin-professor" title="☎️ Interview: Dr Hyoduk Shin, Professor of Innovation at UC San Diego on the State of Privacy-Enhancing Technologies #00" rel="noopener">ref</a></sup>. Nothing in the sources shows the cultural blockers being cleared.

Second, value capture. In the one segment where PETs reached scale, the primitives were immediately given away by Google, by Microsoft Research and by the European Commission, and the explicit reading is that privacy becomes a regulatory expectation rather than a product differentiator, following the same commoditise-the-layer-below pattern seen with AP2, Web Bot Auth and x402 <sup class="ref"><a href="https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/" title="Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages " rel="noopener">ref</a></sup>. A specialist selling the primitive into that environment has no moat. The defensible positions the sources point to are elsewhere: selective encryption and workflow-level products <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e20-the-state-of-privacy-enhancing" title="Understanding Privacy Enhancing Technology (Feat. Karim Eldefrawy, Confidencial.io)" rel="noopener">ref</a></sup>, confidential computing folded into cloud infrastructure <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e19-trusted-execution-environments" title="Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)" rel="noopener">ref</a></sup>, and data governance as a system of record <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-stijn-christiaens-ceo-of" title="☎️ Interview: Stijn Christiaens, CEO of Collibra on the State of Privacy-Enhancing Technologies #004" rel="noopener">ref</a></sup>. Underrated as infrastructure, overrated as a market.

## Prediction

By 31 December 2027, ZKP-based age or identity attestation will be in production in at least one EUDI Wallet deployment built on the EU Age Verification Blueprint or Google's Apache 2.0 ZKP libraries, while no general-purpose FHE or MPC analytics stack in these sources will have shipped as a mainstream cloud product.

## Evidence base

## Open questions

- What are the actual performance overheads of FHE, MPC and TEE-based analytics versus plaintext computation, and does the unified stack under NSF development close them enough for production pipelines?
- Does eIDAS 2.0's encouragement of ZKPs harden into a requirement, and do member state wallets adopt the open-sourced Google or EU implementations rather than building their own?
- If the privacy primitives are free, where does the revenue sit: cloud infrastructure, governance and workflow software, or verticalised data collaboration networks?
- Has any organisation publicly reported a data collaboration deployment that crossed an organisational boundary and produced measurable revenue, as opposed to a pilot?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
