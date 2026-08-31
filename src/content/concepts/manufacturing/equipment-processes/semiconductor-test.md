---
type: concept
slug: semiconductor-test
canonical_name: Semiconductor Test
aliases: []
parent_concepts: []
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 1
frontier:
- What pre-assembly telemetry channels (parametric probe data, on-die monitors, stress-test response) actually carry predictive signal for post-assembly failure, and what is the measured observability bias bound for each?
- Has the KGRD safety-gated architecture been validated against field-return or accelerated-life data from real chiplet assemblies, and what escape rate does it achieve versus conventional KGD?
- What is the yield loss and test-time cost of enforcing a given post-assembly failure probability guarantee, expressed per die or per package?
- Does KGRD screening displace or complement burn-in and system-level test in a production multi-die flow?
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Semiconductor test covers the electrical screening steps that separate functional die from defective ones before and after packaging. In chiplet-based assemblies the conventional gate is Known Good Die (KGD) screening, which establishes pre-assembly functional correctness for each die prior to integration formal foundations for known good reliable die screening in . KGD is a pass/fail functional statement: a die that meets specification at probe is admitted to assembly.

The limitation exposed by chiplet-based artificial intelligence systems-on-chip is that functional correctness at probe carries no probabilistic assurance about reliability lifetime after assembly formal foundations for known good reliable die screening in . Once dies are bonded into a multi-die package, a single latent-defect die can compromise the whole assembly, and the cost of an escape scales with the number and value of the co-packaged dies.

The proposed reformulation, Known Good Reliable Die (KGRD) screening, treats the pre- to post-assembly transition as a constrained inference problem under incomplete pre-assembly observability: the test system must infer a post-assembly reliability property from measurements that only partially observe the mechanisms that will drive field failure formal foundations for known good reliable die screening in . The stated contributions are a Bayesian probabilistic risk model mapping pre-assembly telemetry to post-assembly failure likelihood with a quantified observability bias bound, and a safety-gated decision architecture that yields a provable post-assembly failure probability guarantee formal foundations for known good reliable die screening in . Key parameters in this framing are the observability bias bound (how far the inferred risk can deviate given unobserved mechanisms) and the guaranteed post-assembly failure probability at the gate.

## Competitive landscape

The sources support only one comparison: KGD versus KGRD screening. KGD is the incumbent methodology and provides a deterministic functional guarantee before assembly; KGRD is proposed as a probabilistic extension that adds a bounded lifetime-reliability guarantee on top of the functional screen formal foundations for known good reliable die screening in . No data in the supplied source compares KGRD against burn-in, system-level test, or in-field telemetry-based reliability monitoring, and no cost, throughput, or yield figures are given.

## Evidence base

- A July 2026 arXiv preprint (arXiv:2607.20141v1, cs.AR) argues that growth in chiplet-based AI SoCs has exposed a fundamental gap in semiconductor test methodology formal foundations for known good reliable die screening in .
- The same work states that existing KGD screening guarantees pre-assembly functional correctness but offers no probabilistic assurance of post-assembly reliability lifetime formal foundations for known good reliable die screening in .
- The authors formalise the KGD-to-KGRD transition as a constrained inference problem over incomplete pre-assembly observability formal foundations for known good reliable die screening in .
- Contribution (i) is a Bayesian probabilistic risk model mapping pre-assembly telemetry to post-assembly failure likelihood with a quantified observability bias bound formal foundations for known good reliable die screening in .
- Contribution (ii) is a safety-gated decision architecture claimed to provide a provable post-assembly failure probability guarantee formal foundations for known good reliable die screening in .
- The work is authored by Prashanthi Metku and Chandra Gandu and announced as a new submission on 23 July 2026 formal foundations for known good reliable die screening in .

## Frontier (open questions)

- What pre-assembly telemetry channels (parametric probe data, on-die monitors, stress-test response) actually carry predictive signal for post-assembly failure, and what is the measured observability bias bound for each?
- Has the KGRD safety-gated architecture been validated against field-return or accelerated-life data from real chiplet assemblies, and what escape rate does it achieve versus conventional KGD?
- What is the yield loss and test-time cost of enforcing a given post-assembly failure probability guarantee, expressed per die or per package?
- Does KGRD screening displace or complement burn-in and system-level test in a production multi-die flow?

*Synthesised 2026-08-31 from 1 KB sources by the resynth pipeline; citations are KB source slugs.*
