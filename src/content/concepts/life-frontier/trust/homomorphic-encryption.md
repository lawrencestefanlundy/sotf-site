---
type: concept
slug: homomorphic-encryption
canonical_name: Homomorphic Encryption
aliases: []
kind: technology
parent_concepts:
- life-frontier
- trust
related_concepts: []
sources:
- '[[2024-11-05-confidential-ai-the-dog-that-didnt]]'
- '[[2023-06-08-three-overrated-technologies-from]]'
- '[[2023-10-19-e20-the-state-of-privacy-enhancing]]'
- '[[2023-02-05-interview-flavio-bergamaschi-private]]'
- '[[2021-07-21-why-privacy-tech-is-actually-collaborative]]'
- '[[2023-05-24-launching-state-of-the-future]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2023-10-13-e19-trusted-execution-environments]]'
- '[[2023-07-06-e07-decentralised-ai]]'
- '[[2023-03-05-interview-dr-hyoduk-shin-professor]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2026-07-10-the-next-vc-meme-is]]'
- '[[2023-04-05-interview-stijn-christiaens-ceo-of]]'
- '[[2023-05-05-interview-rick-hao-partner-at-speedinvest]]'
frontier:
- Does modified AI silicon actually close the gap? MPX reports 20% extra area for dual-mode operation and more than 1.2x lower polynomial-multiplication latency 2026 06 16 mpx a unified systolic array for matrix and polynomial multi; what total end-to-end speedup do such changes deliver on a full CKKS inference, and would a GPU or TPU vendor accept the area and precision changes proposed in FHECore-style designs 2026 07 29 fhecore rethinking gpu microarchitecture for fully homomorph?
- How much of the current gap is scheme-inherent versus tooling? With CKKS a decade old and no fifth generation indicated 2026 07 08 libfhe a numba based cuda python library for non rns ckks bg, is there a remaining algorithmic step change, or only compounding engineering at 1.2x-3.9x per layer?
- Do the polynomial approximations required for non-linear operators hold accuracy on frontier-scale models, given that automated per-layer search already faces roughly 10^225 configurations for a 32-layer model 2026 07 28 atlas automated approximation of transformers for efficient ?
- Is the reliability envelope compatible with commodity infrastructure? Encrypted fault injection indicates a safe boundary near a bit-error rate of 10^-5 2026 07 22 prism sensitivity aware polynomial pruning for efficient neu; what does mandatory checksum protection 2026 07 22 an efficient fault tolerance scheme for ckks computation on  add to the already large overhead in production?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 48
last_reorg_date: '2026-05-13'
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 1
sources_30d: 2
recent_mentions:
- slug: 2026-07-10-the-next-vc-meme-is
  title: The Next VC Meme Is...
  date: '2026-07-10'
  kind: substack
- slug: 2025-10-09-a-specific-theory-of-sovereign-ai
  title: A Specific Theory of Sovereign AI
  date: '2025-10-09'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2024-11-05-confidential-ai-the-dog-that-didnt
  title: Confidential AI
  date: '2024-11-05'
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
neighbors: []
---
**Homomorphic encryption lets a server compute on data it cannot read, and after a decade of work on the CKKS family the remaining problem is not security but cost: overheads still run orders of magnitude above plaintext, so most 2026 systems papers either accelerate the arithmetic in hardware or route around full FHE with hybrids and restricted operation sets.**

## Summary

Homomorphic encryption (HE) is a class of encryption schemes in which arithmetic on ciphertexts corresponds to arithmetic on the underlying plaintexts. A client encrypts, an untrusted server computes, the client decrypts and gets the answer it would have got in the clear. Fully homomorphic encryption (FHE) is the general case: arbitrary computation on encrypted data with no decryption key on the server side. The dominant modern constructions rest on Ring Learning with Errors (RLWE) lattice problems and split into approximate-arithmetic schemes (CKKS, and the related BGV) used for neural network and vector workloads, and Boolean/gate-level schemes (TFHE) used for general-purpose integer and control-flow code. Simpler additive-only schemes such as Paillier sit at the cheap end.

A second, quieter theme in the same literature is avoidance. Bifrost keeps only linear layers in CKKS on the accelerator and runs non-linear and cache-state operators inside a CPU trusted execution environment. A music retrieval paper observes that if only one operand is encrypted, similarity search collapses to additions and ciphertext-plaintext multiplications, removing bootstrapping entirely. PrivDNN pushes work to the client with partial model encryption specifically to avoid the server carrying the ciphertext-domain load. Where systems designers reach for these, they are telling you what full FHE still costs.

## Viability (3/5)

The improvement increments reported are honest but small relative to the gap: 1.25x from polynomial-level compiler optimisation over ciphertext-level-only, up to 3.9x on selected TFHE operations from bootstrap reduction, more than 1.2x on polynomial multiplication latency from a dual-mode systolic array. Only workload-specific restructuring produces large numbers, such as 56x on embedding compression. There is also a new reliability question: long ciphertext dataflows are vulnerable to silent data corruption from transient hardware faults, requiring dedicated checksum schemes on CPUs and showing a safe operating boundary near a bit-error rate of 10^-5 in encrypted fault injection. A 3 rather than a 4: it demonstrably works, nothing here shows it working at competitive cost.

**TLDR: Cryptographically settled and demonstrated end to end on real models, but the overhead gap to plaintext is still measured in orders of magnitude.**

## Drivers (3/5)

On supply, the sources show a broad and coordinated push across every layer of the stack in mid-2026: ASIC and FPGA NTT accelerators, reuse and modification of AI silicon including 7nm systolic array designs and GPU microarchitecture proposals, compilers, libraries in C++, CUDA-Python and OpenFHE, and even a quantum-side analogue in blind quantum computation tooling. A notable supply constraint is scheme stability: it is a decade since CKKS was proposed with no indicator of a fifth-generation successor, which is good for hardware investment but implies no algorithmic step change is queued.

On demand, the sources describe pull rather than evidencing it. Cloud LLM serving is framed as a direct confidentiality problem because prompts may contain regulated documents, code or business data; multi-vendor autonomous vehicle fusion is framed as exposing proprietary model behaviour; music embeddings are framed as copyable and usable for training generative models. Interest in ciphertext copyright, source authentication and supervision, addressed by ciphertext watermarking, suggests governance-driven requirements are appearing. None of this is procurement data, revenue or deployment counts, so the demand half of the score is held at credible but unproven.

**TLDR: Supply-side activity is dense and multi-disciplinary; demand is asserted by researchers rather than measured in these sources.**

## Novelty (3/5)

The thing HE is better than is trust. Bifrost states the distinction cleanly: FHE keeps accelerator-side execution ciphertext-only, so device memory, driver, runtime and host software sit outside the trusted computing base, which a hardware TEE alone does not achieve. That is a categorical improvement over enclave-based confidentiality, not an incremental one, and it is why the field persists despite the cost.

But the same paper is the strongest evidence that HE does not yet win alone: it provisions secrets to an attested CPU TEE and uses FHE only as a delegation mechanism for projection and feed-forward linear layers. Similarly, additive-only HE preserves nearest-neighbour rankings exactly for music retrieval while avoiding the ciphertext-ciphertext multiplication and bootstrapping of full-depth FHE, and scales better in embedding dimension; PrivDNN explicitly frames conventional HE-based private inference as making the model owner "handle the heavy lifting" and proposes partial encryption instead. So the honest reading is: unmatched guarantee, currently affordable only in reduced form.

**TLDR: Qualitatively unique guarantee (no plaintext ever on the server) but the sources show it being blended with, not beating, trusted hardware and lighter cryptography.**

## Diffusion (2/5)

What is improving is the abstraction layer, which is the usual precondition for diffusion. ComputeFHE offers encrypted integer and fixed-point types with familiar imperative constructs plus a simulation mode for debugging without running the cryptography. LibFHE argues CUDA-Python can match highly optimised C++ libraries while cutting implementation complexity. Compilers now insert ciphertext management automatically from non-FHE input programs. That is genuine progress on the skills bottleneck, but nothing in these sources indicates production adoption at scale, hence 2.

**TLDR: Cost, developer complexity, depth budgeting and new reliability failure modes all block adoption outside specialist teams.**

## Impact (4/5)

The application breadth in a two-month window of preprints is the argument for high impact: cloud LLM and transformer serving, recommendation systems with private lookups into large embedding tables, cooperative autonomous-vehicle perception across competing vendors, privacy-preserving database queries and deep learning inference generally, and music/vector retrieval. The unlock in each case is the same: parties that cannot legally or commercially share data can still compute jointly, and the compute host does not need to be trusted.

The sources also hint at second-order infrastructure value: shared cryptographic and AI silicon, where adding polynomial-multiplication capability to a systolic array costs only 20% additional area with negligible power overhead in matrix mode, and where the same NTT hardware serves post-quantum cryptography as well as FHE. That makes partial success cheap to capture. The score is 4 rather than 5 because no source quantifies economic value, market size or displaced spend; the impact case here is inferred from technical scope only.

**TLDR: If the cost curve closes, it removes the need to trust cloud operators and hardware vendors across a very wide set of workloads.**

## Timing Soon (2-5yr)

Two clocks run at different speeds. Additive-only HE for similarity search is already practical, preserving rankings exactly without bootstrapping, and hybrid TEE-FHE architectures for LLM serving are being specified now. Those can ship in the near term because they deliberately avoid the expensive primitives.

General-purpose FHE is further out. The published gains are multiplicative in the 1.2x to 3.9x range at the arithmetic, compiler and library layers, set against a gap of several orders of magnitude, and the hardware route most likely to close it, purpose-built or modified AI silicon, carries multi-year design and fabrication lead times. With no fifth-generation scheme in sight to change the arithmetic, the credible window for broad encrypted inference is the back half of a 2-5 year band at the earliest.

**TLDR: Restricted and hybrid HE is deployable on narrow workloads now; general-purpose FHE at competitive cost is not on a 2-year clock.**

## Overrated or underrated? Fairly rated

The position worth holding is that the label is doing too much work. Anyone pricing "homomorphic encryption" as a single asset should split it. The restricted forms, additive-only HE and TEE-FHE hybrids, are underrated and near-term, and are the ones system builders actually choose when they have a workload to ship. General-purpose full-depth FHE as a drop-in replacement for plaintext cloud compute is still gated on orders of magnitude that these papers close in single-digit multiples. On balance, fairly rated, with the caveat that the interesting near-term value sits in the compromises rather than the pure form.

## Prediction

Through the end of 2027, published privacy-preserving transformer or LLM serving systems that report practical end-to-end latency will predominantly be hybrids (HE plus a trusted execution environment, client-side offload, or additive-only HE) rather than end-to-end full-depth FHE.

## Evidence base

## Open questions

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
