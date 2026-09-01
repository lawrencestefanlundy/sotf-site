---
type: concept
slug: agentic-ai
canonical_name: Agentic AI
aliases: []
parent_concepts:
- ai-agents
related_concepts: []
sources:
- '[[2026-06-23-semidoped-daily-update]]'
- '[[2026-03-17-compute-specialisation-equilibrium-aws-rises-to-the-agentic]]'
- '[[2025-06-slm-future-agentic-ai-nvidia]]'
- '[[2026-07-26-postgres-absorption-vector-layer]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2026-05-01-semianalysis-ai-value-capture-model-labs]]'
- '[[2026-03-25-fog-computing-middleware-agentic-ai-rewriting-the-rules-of]]'
- '[[2026-03-23-data-value-migrates-to-retrieval-layer-memory-is-the-new]]'
- '[[2026-04-15-agentic-ai-foundation-linux]]'
- '[[2026-02-05-semianalysis-claude-code-inflection]]'
- '[[2026-06-02-agentic-runtime-silicon-necessity]]'
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 72
sources_7d: 0
sources_30d: 15
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-29-chipagents-series-a2-134m
  title: ChipAgents Expands Series A Funding to $134 Million as Demand Grows for Agentic AI in Semiconductor Design
  date: '2026-07-29'
  kind: web
- slug: 2026-07-26-postgres-absorption-vector-layer
  title: 'Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-02-agentic-runtime-silicon-necessity
  title: Deep-research dossier — does the stateful agent runtime / control-plane layer need a novel silicon primitive?
  date: '2026-06-02'
  kind: web
- slug: 2026-05-01-semianalysis-ai-value-capture-model-labs
  title: AI Value Capture - The Shift To Model Labs
  date: '2026-05-01'
  kind: web
- slug: 2026-04-15-agentic-ai-foundation-linux
  title: The Agentic AI Foundation (under the Linux Foundation)
  date: '2026-04-15'
  kind: web
neighbors: []
---
**Agentic AI is the pattern where one user goal triggers multi-step LLM orchestration with tool calls, retries and failure recovery; it now works well enough to run instrumented laboratories and chip-design loops unattended, but its cost profile, energy accounting and security model are all measurably unresolved.**

## Summary

Agentic AI describes systems in which a language model is not asked to produce a single answer but to pursue a goal over many steps: planning, calling external tools, reading results, retrying on failure and maintaining state between steps. The definition used in the systems literature is operational rather than philosophical, namely "a single user goal triggers multi-step orchestration, tool calls, retries, and failure recovery". The step from stateless generation to stateful autonomy is the whole point and also the source of most of the difficulty.

The engineering reality is that the model is often not the expensive part. Measurement of tool-heavy agentic workloads finds tool execution dominating end-to-end latency: 81-89% for retrieval in Haystack, up to 65% for Bash/Python in SWE-Agent, 85-88% for conformer generation in ChemCrow, while a tool-light workload such as Toolformer stays roughly 88% GPU-bound, so the split is workload-dependent **2511.00739 Cpu Centric Agentic Execution**. A separate audit reports CPU-side processing accounting for up to 90.6% of latency and 44% of dynamic energy, and orchestration structure dominating energy cost, with workflows consuming 4.33x more energy per successful goal than linear baselines and up to 7.63x for multi-step reasoning. The proposed remedies so far are software scheduling, not new silicon: CPU-aware overlapped micro-batching and mixed agentic scheduling deliver up to 1.7-3.9x lower latency from existing CPU-GPU resources **2511.00739 Cpu Centric Agentic Execution**.

The second parameter that decides economics is model size. NVIDIA Research argues that agents need narrow task competence rather than broad conversation, that small language models are "sufficiently powerful, inherently more suitable, and necessarily more economical" for most agentic invocations, that 40-70% of LLM calls in existing agentic systems could be served by specialised SLMs, and that paying 10-30x for unneeded capability is unsustainable at scale **2025 06 Slm Future Agentic Ai Nvidia**.

The third parameter is trust. Agents that hold state, credentials and tool access break the assumptions of conventional access control. Role-based access control is described as insufficient for stochastic agents in critical cloud infrastructure; memory-based attacks such as memory injection decouple the compromise from the eventual harmful action, defeating endpoint content filters; and a survey of 21 proposed agent permission systems finds no settled way to express, derive or enforce user-level policy. Where these three parameters land, cost per successful goal, model size mix, and enforceable permissions, decides whether agentic AI is a laboratory technique or an enterprise substrate.

## Viability (3/5)

The strongest evidence is closed-loop scientific and design work where an evaluator exists. CascadeMAP ran without human intervention for seven days, processing about 220,000 reactions across about 7,400 conditions, with the multi-agent layer handling hypothesis generation and synthesis over 11 GB of experimental data and Bayesian optimisation reaching optima three times faster than design of experiments. An LLM agent autonomously selected an NV centre, calibrated its resonant frequency, measured T2* by Ramsey and added a CPMG measurement to probe a weak feature. HORIZON reports 100% benchmark completion across ChipBench, RTLLM, Verilog-Eval and nine CVDP categories with a hands-free agent loop, while its authors explicitly decline to claim that agentic AI for hardware design is solved and call the benchmarks controlled proxies.

The common factor in every success is a machine-checkable acceptance predicate: an executable evaluator, a simulator, a spectrometer reading. Where that is absent, the field cannot yet answer whether an agent should be trusted, and the Open Security Benchmark authors name the missing ingredient directly as an environment data gap, since real enterprise environments are private and cross-vendor and none is exposed as a shared queryable evaluation target. A 3 is the honest score: the mechanism works, the verifiable half of the problem space is being taken, and the unverifiable half remains unproven.

**TLDR: Unattended multi-day autonomy is demonstrated in instrumented, verifiable domains; open-ended enterprise autonomy is not.**

## Drivers (4/5)

Supply side: an edge platform wave is already in market, with NVIDIA, Dell, HP, ASUS, MSI, Acer and Gigabyte all shipping GB10-based desktop AI systems in 2026 explicitly targeted at agentic workloads. The model supply is also in place, with a 2025-26 small-model lineup spanning Phi-4 and Phi-3.5-mini, Llama 3.2 1B/3B, Ministral 3B/8B, Gemma 2 2B/9B and Qwen 2.5 0.5-3B, and a case that these run locally on consumer hardware for real-time offline inference **2025 06 Slm Future Agentic Ai Nvidia**. Software-side headroom is documented too, at up to 1.7-3.9x latency reduction from better CPU-GPU orchestration alone **2511.00739 Cpu Centric Agentic Execution**.

Demand side: the pull appears independently across unrelated fields in the same window, self-driving materials characterisation, hardware/software co-design frameworks, 6G radio access networks reframed around memory-centric agent architectures, autonomous protocol and traffic-engineering design, and autonomous enterprise cyber defence. That breadth of independent adoption intent, combined with a hard cost argument, is what earns a 4. It is not a 5 because none of the sources supplies revenue, deployment counts or procurement evidence.

**TLDR: Hardware vendors are already shipping for it and the cost argument for cheap narrow models is explicit; the pull is broad across science, networking and security.**

## Novelty (3/5)

Two qualifications hold the score at 3. First, in the strongest results the agent is the search and synthesis wrapper while a Bayesian optimiser or a fast simulator does the discriminating work. Second, the novelty carries a measured penalty: orchestration structure raises energy per successful goal by 4.33x over linear baselines and up to 7.63x for multi-step reasoning. Better than the alternative, then, but at a cost that the same literature says cannot currently be measured on the hardware people are buying.

**TLDR: Real, measured gains over scripted automation and human-driven search, but usually as an orchestration layer over classical optimisers and evaluators.**

## Diffusion (3/5)

The barriers are unusually well characterised for so young a field. There is no agreed way to express or enforce user-level permissions: a survey of 21 agent permission proposals finds the work concentrated at product level, applying one policy to all users, while the risks include prompt injection, leakage of private data to third parties and the active danger of an agent executing sensitive transactions without authorisation. Statefulness creates attack classes that endpoint content filters do not catch, since memory injection and sleeper-agent patterns separate compromise from the eventual harmful action, and long-horizon systems need their own threat taxonomy and attack-propagation model. Thirty international experts convened for a horizon-scanning exercise on exactly these risks, and a separate cross-sector agenda records the gap between AI adoption and AI security readiness as continuing to widen, with governing agentic AI under adversarial pressure as one of four named themes.

Two further frictions are practical rather than adversarial. Enterprises cannot benchmark agents end to end because no realistic cross-vendor environment is publicly queryable, and on flagship edge hardware operators cannot attribute energy to processes at all: the audited GB10 platform exposes no CPU energy counter, no INA power-rail monitor, no IPMI/BMC and no SCMI powercap, with instantaneous GPU power via NVML the only telemetry, even though firmware computes per-rail energy internally through an undocumented ACPI interface. Adoption proceeds anyway, which is why this is a 3 and not a 2, but unit economics and assurance are both currently unmeasurable in production.

**TLDR: Deployment is already happening, but permissions, memory-persistence attacks, benchmark environments and energy observability are all documented as unsolved.**

## Impact (4/5)

The value case is that agentic loops convert bandwidth-limited expert work into machine-limited throughput. Materials characterisation has historically been split between high-throughput inflexible industrial inspection and flexible but bandwidth-limited operator-driven research systems; self-driving platforms aim to bridge the two. A week of unattended operation covering roughly 220,000 reactions and 7,400 conditions is a direct quantification of that shift in one biocatalysis workflow. In hardware, an agentic loop found a first-order design knob for inter-chiplet traffic that expert tuning had not surfaced, and co-design frameworks are being built specifically so such loops can be deployed at scale rather than in isolated small-scale demonstrations.

The upper bound proposed in the networking literature is larger still: protocols, services and traffic engineering designed, deployed and managed by AI, and 6G RANs restructured around a shared memory continuum spanning microsecond reflexes to long-horizon evolution. Those are visions, not results, so they do not lift this to a 5. The demonstrated results in science and chip design alone justify a 4.

**TLDR: If the trust and cost problems are solved, it changes throughput in laboratory science, chip design, network operations and security operations simultaneously.**

## Timing Now (0-2yr)

The 2026 sources describe deployment, not anticipation: hardware vendors shipping GB10-based agentic desktop systems in 2026, multi-day unattended laboratory campaigns, and hands-free hardware-design agent loops clearing benchmark suites. The near-term engineering agenda is also clear and executable: scheduling wins of 1.7-3.9x are available in software now **2511.00739 Cpu Centric Agentic Execution**, and substituting specialised small models for 40-70% of calls is a today decision **2025 06 Slm Future Agentic Ai Nvidia**.

What is not on a two-year clock is the governance layer. Permission specification and enforcement remain fragmented across 21 competing proposals, the evaluation environments needed to judge enterprise agents do not exist publicly, and expert consensus records the security readiness gap as widening rather than closing. Expect the split to persist: verifiable-domain autonomy now, credentialed enterprise autonomy later.

**TLDR: Narrow, evaluator-bounded agentic loops are running in production laboratories and design flows today; trustworthy open-ended autonomy is not.**

## Overrated or underrated? Fairly rated

Split the claim in two. The narrow claim, that goal-directed loops over tools and evaluators beat scripted automation and expert-driven search in domains with a machine-checkable success signal, is supported by measured results: three times faster than design of experiments, 5.1x less remote traffic than the best hand-chosen alternative, full benchmark completion hands-free in hardware design. That is not hype. The broad claim, that stateful agents will shortly hold credentials and run enterprise workflows autonomously, is contradicted by the same literature: role-based access control does not fit stochastic agents, memory persistence creates attacks that content filters do not see, and there is no shared environment on which to test whether an agent should be trusted.

The most useful correction for investors is about where the cost sits. The narrative treats agents as a GPU demand story; the measurements say tool execution and CPU-side work dominate latency in retrieval and code-heavy agents, 81-89% and up to 65% respectively **2511.00739 Cpu Centric Agentic Execution**, with CPU-side processing up to 90.6% of latency and 44% of dynamic energy in one audit, and the fixes proposed are scheduling software rather than new silicon. Anyone underwriting a control-plane accelerator on the agentic thesis should read that paper first.

## Prediction

By 31 December 2027, at least one shipping GB10-class edge AI system will expose per-process or per-rail CPU energy telemetry through a documented, supported software interface; if none does, the energy-attribution blind spot reported for the ASUS Ascent GX10 in will still prevent cost-per-successful-goal accounting for edge agents.

## Evidence base

- Jun 2025: NVIDIA Research argues small language models are sufficient for most agentic calls, estimates 40-70% of LLM queries in existing agentic systems could be served by specialised SLMs, and calls paying 10-30x for unneeded capability unsustainable at scale **2025 06 Slm Future Agentic Ai Nvidia**.
- Nov 2025: measurement of agentic workloads finds tool execution dominating end-to-end latency at 81-89% for retrieval, up to 65% for Bash/Python and 85-88% for conformer generation, with software scheduling (COMB, MAS) giving up to 1.7-3.9x lower latency and no new silicon proposed **2511.00739 Cpu Centric Agentic Execution**.
- Jun 2026: an energy audit of the ASUS Ascent GX10 (GB10 SoC) finds no CPU energy counter, no INA rail monitor, no IPMI/BMC and no SCMI powercap exposed, while agentic workflows consume 4.33x more energy per successful goal than linear baselines and CPU-side processing reaches 90.6% of latency and 44% of dynamic energy.
- Jun 2026: CascadeMAP ran unattended for seven days, processing about 220,000 reactions across about 7,400 conditions with a multi-agent layer over 11 GB of data, with Bayesian optimisation three times faster than design of experiments.
- Jun 2026: an agentic loop guided by a GEMM locality simulator found a 2D block-swizzle CTA traversal reducing remote inter-chiplet traffic by up to 5.1x over the best 1D traversal, in a space where remote traffic varies by up to 58x; separately HORIZON reached 100% completion on ChipBench, RTLLM, Verilog-Eval and nine CVDP categories hands-free while declining to claim the problem is solved.
- Jul 2026: a survey of 21 agent permission proposals finds no settled approach to user-level policy specification or enforcement, and a cross-sector expert agenda records the gap between AI adoption and AI security readiness as continuing to widen, naming governance of agentic AI under adversarial pressure as a priority theme.

## Open questions

- Does the 40-70% SLM substitution estimate from **2025 06 Slm Future Agentic Ai Nvidia** hold in a deployed production agent, and what is the measured effect on task success rate rather than on cost alone?
- Do the CPU-side latency shares of 81-89% for retrieval and up to 65% for code execution **2511.00739 Cpu Centric Agentic Execution** persist once the scheduling fixes are applied, or does the bottleneck move back to the model?
- Will any of the 21 surveyed permission approaches converge into an enforceable cross-vendor standard, or will each agent platform keep its own product-level policy?
- Can agentic performance be shown outside domains with an executable acceptance predicate, given that HORIZON's authors call their 100% completion result a controlled proxy?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
