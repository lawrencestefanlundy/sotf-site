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
- Does a unified abstraction layer over cryptographic and hardware-based secure computation achieve measurable throughput or latency gains over hand-tuned single-primitive deployments, and on which workload classes?
- 'If ZKP identity primitives are commoditised and mandated by eIDAS 2.0, where does defensible value accrue: wallet distribution, credential issuance, or verification networks?'
- Has any PET vendor demonstrated repeatable revenue from cross-organisational data collaboration, as opposed to intra-organisational deployment, and in which verticals?
- Do the cultural barriers to data sharing identified in 2023 interviews persist in 2026 deployments, or has regulatory mandate substituted for voluntary trust-building?
last_updated: '2026-08-31'
tags:
- concept
- seeded-stub
mention_count: 19
sources_7d: 0
sources_30d: 0
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
## Physics / mechanism

Privacy technology, often labelled privacy-enhancing technologies (PETs), addresses the gap in the standard communication chain: data can be encrypted at rest on a device, and transport layer security protects data in motion, but the processing step has historically required plaintext why privacy tech is actually collaborative. PETs close that gap by allowing computation over data that the computing party cannot read, which in turn allows parties who do not trust each other to pool inputs. The thesis framing from this body of work is that securing data during processing creates confidential data collaboration opportunities and a market described as collaborative computing why privacy tech is actually collaborative.

The field spans several families of technique with distinct cost profiles: cryptographic approaches such as secure multiparty computation, homomorphic encryption and zero-knowledge proofs, and hardware-based approaches such as trusted execution environments. An NSF CAREER award to Boston University treats these as complementary rather than competing, proposing a unified software stack with shared abstractions and intermediate representations so functionality can be reused across technologies and workloads, a distributed and fault-tolerant runtime for secure analysis pipelines, and a performance modelling and optimisation framework integrating diverse cost metrics for deployment in heterogeneous environments nsf 2541869 career a unified analytics stack for sec. The framing implies that the binding constraint is no longer whether a given primitive works but how to select and schedule primitives against performance budgets.

Confidentiality is only half the requirement. Intel's private AI and analytics work argues that integrity matters as much as confidentiality, and that crypto-agility, the ability to swap cryptographic primitives as they age or break, is systematically underrated interview flavio bergamaschi private. On the identity side, zero-knowledge proofs have moved into deployed infrastructure: the EU Age Verification Blueprint presents credentials over the W3C Digital Credentials API and OpenID4VP with ZKP support incoming, and eIDAS 2.0 encourages privacy-enhancing technologies including ZKPs in the wallet zk identity primitives commoditised.

Adoption barriers in the sources are as much organisational as technical. Data sharing is described as cultural, requiring communication, collaboration and transparency rather than only tooling interview christine huang data privacy, and vendors compete largely against non-consumption, where even a technology that is five times better carries higher perceived risk than the status quo interview stijn christiaens ceo of.

## Competitive landscape

The main axis of comparison is cryptographic versus hardware-based secure computation. The NSF stack work characterises each as having its own strengths, challenges and performance characteristics, and its design premise is that neither dominates, so a deployment layer must model costs and choose per workload nsf 2541869 career a unified analytics stack for sec. A second axis is architectural: edge versus cloud, where one practitioner view is that the future stack will not resolve to one or the other interview christine huang data privacy. A related unbundling thesis places secure databases alongside serverless and edge databases as the three directions in which database value migrates from commodity hosting towards differentiated query and analysis unbundling the database.

## Evidence base

- The collaborative computing thesis, published 21 Jul 2021 with Lunar Ventures, argues PETs will secure data during processing, closing the gap left by device encryption and TLS, and create a new market why privacy tech is actually collaborative.
- NSF award 2541869, dated 13 May 2026, granted $422,683 to PI Ioannis Liagouris at Boston University under the Secure and Trustworthy Cyberspace programme for a unified analytics stack integrating cryptographic and hardware-based secure computation nsf 2541869 career a unified analytics stack for sec.
- The European age-verification app was announced 15 Apr 2026, with the EU Age Verification Blueprint as its open-source reference implementation over the W3C Digital Credentials API and OpenID4VP zk identity primitives commoditised.
- As of 28 Jul 2026, Google had open-sourced its ZKP libraries under Apache 2.0, and ZKPassport was live on both app stores covering 120+ countries zk identity primitives commoditised.
- Intel's Flavio Bergamaschi, interviewed 5 Feb 2023, identified integrity as equally important to confidentiality and named five stakeholder groups that must be convinced to sell data collaboration software interview flavio bergamaschi private.
- Collibra's Stijn Christiaens, interviewed 5 Apr 2023, described the sale as competing against non-consumption, with a 5x better technology still carrying much higher perceived risk interview stijn christiaens ceo of.
- Speedinvest's Rick Hao, interviewed 5 May 2023, argued machine learning is likely to catalyse PET adoption and that healthcare needs dedicated infrastructure interview rick hao partner at speedinvest.

## Frontier (open questions)

- Does a unified abstraction layer over cryptographic and hardware-based secure computation achieve measurable throughput or latency gains over hand-tuned single-primitive deployments, and on which workload classes?
- If ZKP identity primitives are commoditised and mandated by eIDAS 2.0, where does defensible value accrue: wallet distribution, credential issuance, or verification networks?
- Has any PET vendor demonstrated repeatable revenue from cross-organisational data collaboration, as opposed to intra-organisational deployment, and in which verticals?
- Do the cultural barriers to data sharing identified in 2023 interviews persist in 2026 deployments, or has regulatory mandate substituted for voluntary trust-building?

*Synthesised 2026-08-31 from 12 KB sources by the resynth pipeline; citations are KB source slugs.*
