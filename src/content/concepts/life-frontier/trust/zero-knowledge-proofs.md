---
type: concept
slug: zero-knowledge-proofs
canonical_name: Zero-Knowledge Proofs
aliases: []
kind: technology
parent_concepts:
- life-frontier
- trust
related_concepts: []
sources:
- '[[2023-06-08-three-overrated-technologies-from]]'
- '[[2023-10-19-e20-the-state-of-privacy-enhancing]]'
- '[[2021-07-21-why-privacy-tech-is-actually-collaborative]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2023-10-13-e19-trusted-execution-environments]]'
- '[[2023-07-06-e07-decentralised-ai]]'
- '[[2023-05-05-interview-rick-hao-partner-at-speedinvest]]'
frontier:
- How does NanoZK's roughly 6.3 second per-MLP-sub-circuit CPU prove time change on GPU or dedicated proving hardware, and does the layerwise parallelism deliver near-linear speedup in practice 2026 07 21 nanozk privacy preserving verifiable inference for large lan?
- Will any regulator or large buyer actually require cryptographic proof of model execution, rather than accepting hardware attestation from a trusted execution environment 2023 10 13 e19 trusted execution environments?
- How much soundness is lost in practice under Fisher-information-guided audit-budget triage compared with verifying every layer, and would a court or auditor accept sampled verification 2026 07 21 nanozk privacy preserving verifiable inference for large lan?
- Do post-quantum proof systems with advanced functionalities, built on lattices or codes, reach comparable proof sizes and prover costs, or does quantum resistance cost an order of magnitude 2026 05 07 nsf 2528909 collaborative research satc 20 res post ?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 11
last_reorg_date: '2026-05-13'
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2025-10-09-a-specific-theory-of-sovereign-ai
  title: A Specific Theory of Sovereign AI
  date: '2025-10-09'
  kind: substack
- slug: 2023-10-19-e20-the-state-of-privacy-enhancing
  title: Understanding Privacy Enhancing Technology (Feat. Karim Eldefrawy, Confidencial.io)
  date: '2023-10-19'
  kind: substack
- slug: 2023-10-13-e19-trusted-execution-environments
  title: Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)
  date: '2023-10-13'
  kind: substack
- slug: 2023-07-06-e07-decentralised-ai
  title: '🔮E07: Decentralised AI'
  date: '2023-07-06'
  kind: substack
- slug: 2023-06-08-three-overrated-technologies-from
  title: '💡E03: Three Overrated Technologies from the Future Fusion, Bitcoin & LEO Internet + Ultrasound for Hibernation; Wind Power; Skeletal Editing; Carbon Pricing; & Psychedelics++'
  date: '2023-06-08'
  kind: substack
- slug: 2023-05-05-interview-rick-hao-partner-at-speedinvest
  title: '☎️ Interview: Rick Hao, Partner at SpeedInvest on the State of Privacy-Enhancing Technologies #005'
  date: '2023-05-05'
  kind: substack
- slug: 2021-07-21-why-privacy-tech-is-actually-collaborative
  title: 💡Collaborative Computing
  date: '2021-07-21'
  kind: substack
neighbors: []
---
**Zero-knowledge proofs let one party prove a computation was carried out correctly without revealing the data or model behind it, and the 2026 state of the art shows this is now cheap to verify but still expensive to prove, which is why the technology keeps finding niches rather than becoming default infrastructure.**

## Summary

A zero-knowledge proof (ZKP) is a cryptographic protocol in which a prover convinces a verifier that a statement about some hidden data is true, while revealing nothing beyond the truth of the statement. The practical version used today compiles a computation into an arithmetic circuit, then produces a short proof that the circuit was executed on committed inputs. The verifier checks the proof rather than re-running the work. That gives two distinct products from one primitive: privacy (the inputs stay hidden) and verifiability (the computation is auditable by someone who never sees it).

ZKPs sit inside the broader family of privacy-enhancing technologies alongside secure multi-party computation, homomorphic encryption, verifiable computation and trusted execution environments. The framing used across the State of the Future material is that data is already encrypted at rest and in transit, but not during processing, and PETs are the set of techniques attacking that third gap, opening up confidential data collaboration as a market <sup class="ref"><a href="https://stateofthefuture.substack.com/p/why-privacy-tech-is-actually-collaborative" title="💡Collaborative Computing" rel="noopener">ref</a></sup>. The same body of work is candid that MPC, ZKP and FHE have all struggled for adoption in practice <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e20-the-state-of-privacy-enhancing" title="Understanding Privacy Enhancing Technology (Feat. Karim Eldefrawy, Confidencial.io)" rel="noopener">ref</a></sup>, with hardware-based trusted execution environments treated as the more likely near-term route to confidential cloud computing <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e19-trusted-execution-environments" title="Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)" rel="noopener">ref</a></sup>.

The parameters that decide whether a ZKP deployment is worth it are prover time, proof size, verification time, setup cost, and how awkward the target computation is to express as a circuit. The clearest recent datapoint is NanoZK, a system for verifiable large language model inference in which clients or third-party auditors check that a provider ran the advertised model on a committed input without learning weights or activations. It decomposes transformer inference into independently provable layers linked by a SHA-256 commitment chain, giving constant-size sub-circuit proofs of 3.5 to 3.7 KB and about 83 KB in total at twelve layers, against 101 to 126 KB for prior monolithic ZKML proofs, with the layerwise structure being substantially more parallelisable. Non-linear operations that circuits handle badly (softmax, GELU, normalisation) are replaced with 16-bit lookup-table approximations, with measured perplexity degradation below 1e-4 across six model and dataset combinations. On CPU the MLP sub-circuit proves in about 6.3 seconds prove-only, about 43 seconds including setup, with about 22 ms verification at any width, and attention proving starts from about 0.9 seconds. Verification is trivially cheap; proving is seconds per layer per token-batch, which is the whole economic story.

A second parameter is the assumption base. Most deployed proof systems rest on hardness assumptions that a large quantum computer would break, and standardisation to date has concentrated on basic encryption and signatures rather than advanced functionalities. NSF is funding work explicitly on post-quantum protocols with advanced features for decentralised and privacy-preserving applications, built on lattices and error-correcting codes.

## Viability (3/5)

The soundness and zero-knowledge properties are proved under standard assumptions in the strongest source here, including compositional soundness for the layerwise construction, and the numerical fidelity cost of making transformer non-linearities circuit-friendly is measured rather than asserted, at below 1e-4 perplexity degradation across six model and dataset combinations. Verification at about 22 ms and proofs at tens of kilobytes mean the verifier side is essentially solved for this workload.

The prover side is not. Roughly 6.3 seconds prove-only for one MLP sub-circuit on CPU, plus setup, against inference that would otherwise take milliseconds, is a large multiple, and the authors themselves introduce a Fisher-information-guided audit-budget triage as an efficiency tool while conceding that full soundness still requires verifying every layer. That concession is the honest summary of the field: you either pay the full cost or you accept sampled assurance. A further open exposure is the assumption base, since the primitives underpinning many proof systems fall to Shor's algorithm and post-quantum equivalents with advanced functionality are still a research programme rather than a standard. Three, not higher: it demonstrably works, at a cost most workloads will not pay yet.

**TLDR: The mathematics works and verification is near-free; proving cost remains the binding constraint.**

## Drivers (3/5)

On supply, the evidence here is thin and mostly public-sector. The NSF awards for post-quantum protocols with advanced functionalities are $399,964 and $200,002 respectively, dated 1 May 2026. Those are foundational grants, not industrialisation money. The sources give no figures on private investment, proving hardware, or commercial ZKP volumes, so the supply picture cannot be scored more confidently than the middle.

**TLDR: Demand is being pulled by AI trust and data acquisition; supply-side funding visible here is small and academic.**

## Novelty (3/5)

The comparison that matters is against trusted execution environments, which achieve confidential processing by trusting silicon vendors and are treated in this material as the significant near-term component of confidential cloud <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e19-trusted-execution-environments" title="Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)" rel="noopener">ref</a></sup>. ZKPs need no such hardware trust and produce a transferable artefact: a third-party auditor can check the proof later, which a TEE attestation does not equal. Against MPC and FHE, ZKPs address a different shape of problem, proof of correct execution rather than joint or encrypted computation, and all three are described as sharing the same adoption difficulty <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e20-the-state-of-privacy-enhancing" title="Understanding Privacy Enhancing Technology (Feat. Karim Eldefrawy, Confidencial.io)" rel="noopener">ref</a></sup>.

Within ZKP itself the 2026 improvement is real but modest in headline terms: total proof size of about 83 KB at twelve layers is comparable to prior monolithic ZKML proofs of 101 to 126 KB, and the actual gain claimed is parallelisability and constant-size 3.5 to 3.7 KB sub-circuits from layerwise decomposition, plus lookup-table handling of non-linearities with negligible accuracy loss. That is an engineering restructuring that makes distribution across machines feasible, not a step change in total cost. Score three: genuinely differentiated capability, incremental measured advance.

**TLDR: Uniquely offers verifiability without hardware trust; the measured gains over prior ZKML are structural rather than order-of-magnitude.**

## Diffusion (2/5)

The most direct statement in the material is that MPC, ZKP and FHE struggle for adoption, with the discussion pointing towards selective encryption and a shift in data security practice rather than wholesale substitution of computation with cryptography <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e20-the-state-of-privacy-enhancing" title="Understanding Privacy Enhancing Technology (Feat. Karim Eldefrawy, Confidencial.io)" rel="noopener">ref</a></sup>. The same body of work notes that technologies do not solve problems, solutions do, and that framing exploration around zero-knowledge proofs rather than around the problem of protecting data during processing yields worse answers <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e20-the-state-of-privacy-enhancing" title="Understanding Privacy Enhancing Technology (Feat. Karim Eldefrawy, Confidencial.io)" rel="noopener">ref</a></sup>. That is a diffusion diagnosis: ZKP is a capability in search of procurement categories.

**TLDR: The sources are explicit that ZKP and its PET siblings have struggled for adoption, and the hardware alternative is easier to buy.**

## Impact (3/5)

The upside case in this material is that securing data during processing unlocks confidential data collaboration and creates a new market described as collaborative computing <sup class="ref"><a href="https://stateofthefuture.substack.com/p/why-privacy-tech-is-actually-collaborative" title="💡Collaborative Computing" rel="noopener">ref</a></sup>. Layered onto the 2026 use case, the value is that a buyer of model inference can prove which model ran, which matters for regulated decisions, model substitution disputes and any claim of provenance in AI output. It also sits under decentralised AI arguments, where compute and models are distributed across parties who do not trust each other and therefore need verification rather than reputation <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e07-decentralised-ai" title="🔮E07: Decentralised AI" rel="noopener">ref</a></sup>.

What the sources do not contain is any market sizing, revenue figure, or measured cost of the harm ZKPs would prevent. The NSF abstracts note that emerging decentralised and privacy-preserving applications need advanced cryptographic functionality that current standards do not cover, which supports importance but not magnitude. Three reflects a credible and specific value mechanism with no quantified prize behind it.

**TLDR: Large if it becomes the audit layer for outsourced AI; the sources support the mechanism but not the size of the prize.**

## Timing Soon (2-5yr)

The verification side is already practical at about 22 ms per sub-circuit proof and tens of kilobytes on the wire, which means the client-side and auditor-side integration cost is low today. What stands between that and use is prover economics and the absence of anyone contractually obliged to demand proofs. Both are solvable in the two to five year window for high-value, low-volume workloads: regulated model decisions, audit sampling of a provider, or disputes where the cost of proving is trivial against the cost of being wrong.

The wider ambition, cryptographically protected processing as a default, has been forecast for years in this material and has repeatedly lost to easier options, with hardware trusted execution treated as the practical route to confidential cloud <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e19-trusted-execution-environments" title="Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)" rel="noopener">ref</a></sup> and PET adoption described as a struggle <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e20-the-state-of-privacy-enhancing" title="Understanding Privacy Enhancing Technology (Feat. Karim Eldefrawy, Confidencial.io)" rel="noopener">ref</a></sup>. The post-quantum question adds a second, longer clock, since advanced functionalities on quantum-resistant assumptions were still being funded as foundational research in May 2026.

**TLDR: Narrow verifiable-inference and audit deployments are plausible within a few years; general privacy-preserving computation is not on that clock.**

## Overrated or underrated? Fairly rated

Zero-knowledge proofs are overrated as a privacy technology and underrated as an audit technology, which nets out to fairly rated. The privacy pitch has been made for at least five years across this material and has not converted, losing to trusted execution environments and to selective encryption because those can be bought rather than engineered <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e19-trusted-execution-environments" title="Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e20-the-state-of-privacy-enhancing" title="Understanding Privacy Enhancing Technology (Feat. Karim Eldefrawy, Confidencial.io)" rel="noopener">ref</a></sup>. Anyone modelling ZKP as the substrate of a general confidential cloud should discount heavily.

The verifiability pitch is different and stronger. The 2026 result shows that proving a transformer ran as advertised is now a matter of tens of kilobytes and milliseconds to check, with under 1e-4 perplexity cost to make the model circuit-friendly, and seconds of prover time per layer on CPU. That is the profile of a technology that gets deployed when a regulator or a contract asks for it, not when engineers find it elegant. The honest caveat, and the one the authors make themselves, is that the affordable version relies on sampled auditing and therefore does not give full soundness. Until proving cost drops far enough that every layer is verified by default, ZKP-based AI auditing will be assurance with an asterisk.

## Prediction

By 31 December 2028, no major commercial LLM API will offer per-request zero-knowledge proofs of model execution as a generally available, full-soundness (every-layer-verified) product feature.

## Evidence base

- 21 July 2026: NanoZK decomposes transformer inference into independently provable layers linked by a SHA-256 commitment chain, giving constant-size 3.5 to 3.7 KB sub-circuit proofs and about 83 KB total at twelve layers, against 101 to 126 KB for prior monolithic ZKML proofs.
- 21 July 2026: 16-bit lookup-table approximations for softmax, GELU and normalisation show measured perplexity degradation below 1e-4 across six model and dataset combinations.
- 21 July 2026: on CPU the MLP sub-circuit proves in about 6.3 seconds prove-only (about 43 seconds with setup) with about 22 ms verification at any width, and attention proving starts from about 0.9 seconds; the authors state that full soundness still requires verifying every layer.
- 1 May 2026: NSF awarded $399,964 and $200,002 to two collaborative projects on post-quantum cryptographic protocols with advanced functionalities, noting that standardisation so far has focused on basic encryption and signatures while decentralised and privacy-preserving applications need more.
- 19 October 2023: MPC, ZKP and FHE are described as struggling for adoption, with selective encryption offered as the more tractable path <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e20-the-state-of-privacy-enhancing" title="Understanding Privacy Enhancing Technology (Feat. Karim Eldefrawy, Confidencial.io)" rel="noopener">ref</a></sup>.
- 13 October 2023: trusted execution environments are argued to be a significant part of the future confidential cloud, positioning hardware trust as ZKP's main competitor for processing-time protection <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e19-trusted-execution-environments" title="Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)" rel="noopener">ref</a></sup>.
- 5 May 2023: machine learning is identified as the main driver of data-sharing tool adoption, with healthcare likely to need its own data infrastructure <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-rick-hao-partner-at-speedinvest" title="☎️ Interview: Rick Hao, Partner at SpeedInvest on the State of Privacy-Enhancing Technologies #005" rel="noopener">ref</a></sup>.

## Open questions

- How does NanoZK's roughly 6.3 second per-MLP-sub-circuit CPU prove time change on GPU or dedicated proving hardware, and does the layerwise parallelism deliver near-linear speedup in practice?
- Will any regulator or large buyer actually require cryptographic proof of model execution, rather than accepting hardware attestation from a trusted execution environment <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e19-trusted-execution-environments" title="Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)" rel="noopener">ref</a></sup>?
- How much soundness is lost in practice under Fisher-information-guided audit-budget triage compared with verifying every layer, and would a court or auditor accept sampled verification?
- Do post-quantum proof systems with advanced functionalities, built on lattices or codes, reach comparable proof sizes and prover costs, or does quantum resistance cost an order of magnitude?

---
*Assessment drafted 2026-08-31 from up to 10 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
