---
type: concept
slug: eda-design-tools
canonical_name: EDA & Design Tools
aliases: []
kind: technology
parent_concepts:
- manufacturing
- foundry-design
related_concepts: []
sources: []
frontier:
- Do LLM-generated assertion sets close the gap between proving non-vacuously (82.1%) and covering the formal core (36.2%), or is the missing coverage a structural limit of generating properties without a specification the model can be held to?
- Does PANDA's reported reduction of analog turnaround from days or weeks to hours reproduce independently, on production process design kits rather than research flows?
- How far do surrogate power models such as BigPower degrade outside their training configurations and workloads, and is the residual error small enough to make architectural decisions on?
- Will the small synthesised datasets now being published (342 modules in HierSVA-DS, Verilog-to-VHDL conversions in VHDLSuite) scale to the volume needed for fine-tuning, or does the field remain data-limited?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 25
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
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-25-why-ramp-built-its-own-in-house-coding-agent-inspect
  title: Why Ramp built its own in-house coding agent, Inspect
  date: '2026-08-25'
  kind: web
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-29-chipagents-series-a2-134m
  title: ChipAgents Expands Series A Funding to $134 Million as Demand Grows for Agentic AI in Semiconductor Design
  date: '2026-07-29'
  kind: web
- slug: 2026-06-11-southampton-to-help-expand-uk-chip-design-capabilities---mir
  title: Southampton To Help Expand UK Chip Design Capabilities - Mirage News
  date: '2026-06-11'
  kind: web
neighbors: []
---
**EDA is the software layer that turns design intent into manufacturable silicon, and the 2026 research front is rebuilding it around large language models, differentiable optimisation and surrogate models, with benchmark results showing real gains in design turnaround but verification quality still well short of sign-off.**

## Summary

Electronic design automation (EDA) covers the tool chain between a designer's intent and a manufacturable chip: writing register transfer level (RTL) code in Verilog, SystemVerilog or VHDL, verifying it, synthesising it, placing and routing it, estimating power and timing, laying out analog blocks, and exploring architectures before any of that is committed. Each of those stages is currently a mix of solver-based algorithms, hand-tuned heuristics, slow simulators and large amounts of manual engineering judgement.

The current wave of work attacks this from three directions. First, LLMs as code and property generators: RTL generation with tool assistance and curated datasets, VHDL generation and evaluation infrastructure built by automatically converting Verilog designs and testbenches into executable VHDL benchmarks validated with VUnit/GHDL, hierarchical formal verification via generated SystemVerilog Assertions, and full analog flows that carry design intent through topology synthesis, sizing and constraint-driven layout. Second, learned or differentiable replacements for expensive inner loops: source-level module power estimation without simulation at inference time, Gaussian-reparameterised differentiable operator scheduling for compilation and high-level synthesis, and neural surrogates plus a decision-tree quality gate for signal-integrity-compliant PCB interconnect design. Third, modelling tools for physical realities the existing tools were never built for: inter-die routing in 2.5D and 3D FPGAs, modelled by extending the open-source VTR/VPR flow with HSPICE circuit models of a 7 nm die on a 45 nm interposer, and embodied plus operational carbon as a first-class architectural metric.

The parameters that decide whether any of this matters are unglamorous. For generative tools, everything hinges on whether the output is checked by a real tool rather than scored by string similarity: compile rate, proof success, vacuity, mutation coverage and formal core coverage are the numbers that separate a demo from usable automation. For surrogate tools, it is whether accuracy holds across configurations and workloads outside the training distribution. For both, the binding constraint is training and evaluation data, which is why several of these papers are data synthesis pipelines rather than models. And for anything touching a real tape-out, the question is whether the result can be signed off, which none of the supplied sources demonstrates.

## Viability (3/5)

The deterministic side of this field is already functional. Extending VTR/VPR to model multi-die routing architectures, backed by HSPICE modelling of inter-die connections on a 7 nm process over a 45 nm interposer, is a working design space exploration capability rather than a promise. GauS produces Pareto-optimal schedules on benchmarks and gives the first differentiable formulation of pipelined scheduling. ACT3 is a shipped modelling platform with case studies.

The generative side is where the honest numbers are, and they are middling. Across twelve recent LLMs, HierSVA reports a module-level compile rate of 67.1%; of assertions in evaluable runs 82.1% prove non-vacuously, but the assertion sets detect only 70.2% of eligible injected faults and cover 36.2% of the formal core. That is a tool which finds some bugs and misses most of the design's proof surface, which is not the same thing as verification. The VHDL work exists precisely because coverage of anything other than Verilog was untested, and stricter semantics make generalisation harder. LLM4RTL further reports common LLM weaknesses in rule-based reasoning and logic and has to add pre-processing tools to compensate. A 3 reflects a split field: credible and working in modelling and optimisation, early and contested in generation.

**TLDR: The non-generative tools work now; LLM-generated verification collateral is measurably incomplete.**

## Drivers (3/5)

Demand is stated explicitly in several sources. Die stacking has produced 2.5D FPGAs and is pushing towards 3D, and the absence of accurate modelling tools has left most inter-die routing architecture questions unanswered. Sustainability has emerged as a system architecture design metric and will require a new generation of EDA and architectural modelling tools. Analog design still depends on manual intervention across topology, sizing and layout, with prior automation addressing stages in isolation. Security validation requires engineers to define threat models and properties by hand, which is manually intensive and error-prone. Power estimation workflows still rely on simulation or post-silicon analysis. Each of these is a specific, named bottleneck rather than a general appeal to complexity.

Supply is the weaker half. The rate limiter on LLM-based EDA is high-quality training and evaluation data, which is why the work takes the shape of synthesis pipelines: Verilog-to-VHDL conversion with executable validation, a judge-renew-check-renew-check pipeline that uses a cost-tiered hierarchy of commercial LLMs to refine an existing public dataset, and a 342-module hierarchical dataset with a 28 module-bug deep subset derived from BaseJump STL. Datasets of that scale are small relative to the design spaces involved. The sources give no evidence on commercial R&D spend, tool licensing or foundry co-development, so the supply picture is partial.

**TLDR: Demand pull is clear and named in the sources; supply is improving mainly because people are building the missing datasets and benchmarks.**

## Novelty (3/5)

The comparisons that carry numbers are respectable rather than transformative. An LLM-based shuttling compiler for trapped-ion machines, fine-tuned on linear and branched 1D architectures, generates valid schedules for benchmark circuits up to 16 qubits, generalises to a previously unseen four-way junction layout, and reduces shuttling effort by up to 15% against state-of-the-art baseline compilers. GauS beats categorical differentiable formulations by capturing the ordinal nature of time and reducing the optimisation space by orders of magnitude, reaching Pareto-optimal results. QALM's contribution is structural, interleaving search-based exploration with rule-based exploitation so that escaping a local minimum does not require exponentially many blind steps. The surrogate PCB framework is deliberately positioned against iterative black-box surrogate optimisation, replacing stochastic search with an interpretable sequential gate plus an Earth Mover's Distance ranking.

The headline claim is PANDA's, which reports analog design turnaround falling from days or weeks to hours while improving design performance, by managing cross-stage dependencies instead of automating stages in isolation. If that generalises it is a step change; as supplied it is one framework's self-reported result with no independent replication. Against that, HierSVA is evidence that on verification quality the new methods are not yet better than what they would replace. Genuine but uneven improvement over the incumbent, hence 3.

**TLDR: Real margins over solvers, heuristics and manual flows, but the largest claimed gain is a single-paper turnaround figure.**

## Diffusion (2/5)

The evaluation substrates give the position away. HierSVA is built on BaseJump STL, BigPower on the open-source XiangShan processor family, the multi-die work on open-source VTR/VPR, the VHDL benchmarks on GHDL and VUnit. Open tooling is what makes the research possible, and it is also a sign that none of this has yet been tested inside a production flow tied to a foundry process design kit. ACT3 is explicitly framed as a platform for research and advanced development.

The barriers follow from that. Verification and sign-off are liability functions, and a flow whose generated assertions cover 36.2% of the formal core cannot be trusted to replace an existing methodology without a human doing the same work again. Surrogate power and signal-integrity models need demonstrated accuracy outside their training distributions before anyone commits mask cost to them. The path of least resistance is therefore assistive: pre-silicon exploration, early power and carbon estimates, first-pass analog layout, all reviewed downstream. That path is real but slow, and the supplied sources contain no adoption, licensing or industrial pilot data to support a higher score.

**TLDR: Everything in the sources is a research prototype evaluated on open designs; no deployment evidence at all.**

## Impact (4/5)

If the analog claim holds, compressing topology-to-layout turnaround from days or weeks to hours changes the economics of mixed-signal design, which has resisted automation longest and is described in the sources as still heavily manual across every stage. Removing simulation from the inner loop of module-level power estimation moves a decision that currently waits for simulation or post-silicon data into the source-level design phase. Automating property generation and information flow path reconstruction from RTL traces attacks a security validation process that today depends on manual threat modelling and is prone to human error. The multi-die modelling work determines how an entire generation of 2.5D and 3D devices is architected, a question the sources say was previously unanswerable for lack of tools. Adding carbon as a design axis alongside power and performance changes what gets optimised, not just how fast.

The same machinery also transfers to adjacent design domains: hardware-aware neural architecture search that fits within 512 MB of RAM so it can run on the target class of device, quantum circuit synthesis and compilation, and physics-informed inverse design of devices whose forward models are non-differentiable Monte Carlo simulations. The score is a judgement about magnitude if the methods land; no source in this set quantifies the economic value, and that is the reason it is not a 5.

**TLDR: The bottlenecks these tools target are the ones that set chip design cost and schedule.**

## Timing Soon (2-5yr)

Two clocks are running. The architectural modelling and optimisation tools are available immediately: ACT3 is released with case studies, the enhanced VTR flow is in use for design space exploration today, and differentiable scheduling is a drop-in replacement for solvers and heuristics in compilation and synthesis. Anyone doing pre-silicon exploration can pick these up now.

The generative side is at the stage where the field has just finished building its measuring instruments. VHDLSuite and HierSVA are both benchmark infrastructure published in June 2026, and the numbers those instruments return, notably 67.1% module compile rate and 36.2% formal core coverage, are the baseline against which progress will be measured. Historically, benchmarks of this kind precede rapid improvement, but closing a gap of that size and then earning sign-off trust is a multi-year process. Two to five years is the reasonable window for LLM-assisted RTL and assertion generation to appear as a standard assistive stage in production flows; full autonomy is not in view in these sources.

**TLDR: Modelling and surrogate tools are usable now; LLM-generated RTL and verification collateral need another cycle of benchmark-driven improvement before they enter real flows.**

## Overrated or underrated? Fairly rated

The field is being valued roughly correctly, but for the wrong reasons, and the attention is pointed at the weakest part. The loud story is LLMs writing RTL and verification properties, and that is exactly where the June 2026 evidence is thinnest: 67.1% compile rate, 70.2% of injected faults caught, 36.2% formal core coverage across twelve models, plus documented weaknesses in rule-based logical reasoning that require external tools to patch. Anyone underwriting a near-term replacement of verification engineers is reading a demo, not a result.

The quieter half is undervalued and offsets it. Surrogate models that remove simulation from power and signal-integrity loops, differentiable reformulations of scheduling that exploit GPUs, hybrid search plus rule-based optimisers, and new modelling capability for die stacking and carbon are less exciting and more likely to be in someone's flow within two years. The credible read is a decade of steady, tool-checked assistance rather than a discontinuity, with cross-stage analog automation the single most interesting result to watch.

## Prediction

By June 2028, a published benchmark applying the HierSVA metric axes to then-current LLMs will report formal core coverage above 60%, more than doubling the 36.2% measured in June 2026, while module-level compile rates remain below 95%.

## Evidence base

- Across twelve recent LLMs, generated SystemVerilog Assertions achieved a 67.1% module-level compile rate, 82.1% non-vacuous proof rate, detection of only 70.2% of eligible injected faults and 36.2% formal core coverage on a 342-module hierarchical dataset.
- An LLM-enhanced analog framework spanning topology synthesis, sizing and layout reports turnaround falling from days or weeks to hours while improving design performance.
- Fine-tuned LLM shuttling compilers for trapped-ion machines generated valid schedules for circuits up to 16 qubits, generalised to an unseen four-way junction layout, and cut shuttling effort by up to 15% versus state-of-the-art baseline compilers.
- The open-source VTR flow was extended with HSPICE models of inter-die connections on a 7 nm process and a 45 nm silicon interposer, because the absence of accurate modelling tools had left most 2.5D and 3D routing architecture questions unanswered.
- Architecture Carbon Tool v3, published June 2026, frames sustainability as a system architecture design metric requiring a new generation of EDA and architectural modelling tools, and adds first-order design space exploration.
- A differentiable scheduling framework using Gaussian reparameterisation reduced the optimisation space by orders of magnitude versus categorical formulations and gave the first differentiable formulation of pipelined scheduling, reaching Pareto-optimal results.

## Open questions

- Do LLM-generated assertion sets close the gap between proving non-vacuously (82.1%) and covering the formal core (36.2%), or is the missing coverage a structural limit of generating properties without a specification the model can be held to?
- Does PANDA's reported reduction of analog turnaround from days or weeks to hours reproduce independently, on production process design kits rather than research flows?
- How far do surrogate power models such as BigPower degrade outside their training configurations and workloads, and is the residual error small enough to make architectural decisions on?
- Will the small synthesised datasets now being published (342 modules in HierSVA-DS, Verilog-to-VHDL conversions in VHDLSuite) scale to the volume needed for fine-tuning, or does the field remain data-limited?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
