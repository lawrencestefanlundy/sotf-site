---
type: concept
slug: security-cyber
context_concept: true
canonical_name: Security & Cyber
aliases: []
kind: market
parent_concepts:
- life-frontier
- trust
related_concepts: []
sources: []
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
mention_count: 30
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-05-stealthium-gpu-powered-security-intelligence-site-docs-compe
  title: Stealthium — GPU-Powered Security Intelligence (site + docs + competitive context)
  date: '2026-08-05'
  kind: web
- slug: 2025-10-09-wi-fi-7-advanced-integrates-sensing-iot-and-ai-security-into
  title: Wi-Fi 7 Advanced integrates sensing, IoT, and AI security into 10Gbps wireless networks - TechRadar
  date: '2025-10-09'
  kind: web
neighbors: []
---
**Security and cyber here means the defensive engineering around AI agents and the hardware that runs them, and the mid-2026 literature shows attacks landing reliably on shipping systems while the matching defences remain research prototypes.**

## Summary

"Security & Cyber" as a technology area currently splits into two very different layers. The upper layer is agentic AI security: LLM agents that read files, call tools, load third-party "skills" and drive browsers, and the guardrails, scanners and policy engines meant to contain them. The lower layer is the classical hardware and cryptographic substrate: post-quantum cryptography (PQC) on embedded devices, homomorphic encryption and trusted execution environments for confidential inference, physical unclonable functions (PUFs) for device identity, information-flow analysis of chip designs, and physical-layer security in radio links.

The upper layer works by interposing a checker between an agent and its environment. Guardrail models classify inputs and outputs, skill scanners vet natural-language plus code bundles at install time, and origin policies restrict data flows. The attack literature from June 2026 shows all three interposition points failing in distinct ways. Harmful goals can be split into individually benign subtasks that each pass refusal checks and cumulatively achieve the objective. Skills that look harmless in isolation become harmful when composed in a shared execution context, with attack success reaching 33.6 per cent on the capability-flow subset of SCR-Bench. Guardrails themselves become the target: crafted payloads trap them in extended reasoning loops, and payloads optimised on one open-source surrogate transfer to eight leading model backbones.

The lower layer is more conventional engineering with measurable results. NIST-standardised PQC signatures are shown to be impractical in pure software on an ARM Cortex-M4, with SPHINCS+ unusable and the reference Dilithium implementation failing to execute at all, while an FPGA number-theoretic-transform accelerator on a Zynq-7000 SoC brings key and signature generation down to millisecond levels. Systolic arrays can be extended to do polynomial multiplication directly for 20 per cent extra area and better than 1.2x lower latency than NTT-based mapping. Device signatures usable as PUF responses have been extracted from 112 commercial DDR4 chips.

The parameters that decide the area are: how fast defensive coverage rates rise from their current single-digit and low-double-digit percentages; whether containment can be enforced structurally (origin policies, hardware-guaranteed privacy budgets, attested TEEs) rather than by asking a model to judge intent; and whether crypto acceleration lands in the silicon that constrained devices actually ship with.

## Viability (3/5)

Split the verdict. On the substrate, the results are real and quantified: an FPGA NTT accelerator turns Dilithium from non-executing to millisecond-level on constrained hardware; DRAM PUF responses show average intra-Jaccard indices between 89.02 and 94.86 per cent across 112 DDR4 chips depending on the number of simultaneously activated rows; a dual-mode systolic array delivers polynomial multiplication for 20 per cent extra area with negligible power overhead in matrix mode; a directional-modulation array confines reliable 16-QAM recovery to a 30 to 36 degree E-plane beamwidth at 5.05 GHz in measurement.

On the agent layer, viability is poor and the numbers say so. Open-source skill scanners detect 2 to 8 per cent and commercial scanners 9 to 17 per cent of language-and-code cross-modal attacks. Code agents comply with roughly 100 per cent of single-file-workspace jailbreaks for stronger models, with mean attack success around 71 per cent, rising to about 75 per cent in multi-file settings where 32 per cent of produced attack code actually runs; wrapping an LLM in an agent raises attack success by 1.6x. Structural defences are the more promising direction: SOPGuard enforces same-origin policy in an agentic browser while preserving utility at small runtime overhead, and DataGuard enforces differential-privacy budgets in hardware rather than trusting a third-party application. Those are single-implementation prototypes, not proven-in-production controls.

**TLDR: Hardware and crypto defences demonstrably work; agent-layer defences are measurably porous.**

## Drivers (4/5)

Demand: the attack surface is generated by deployment, not by speculation. Agents now load skills at runtime that pair natural-language specifications with executable scripts and resources and drive browsers by natural-language instruction; each deployment step adds a new class of exposure. Cloud LLM serving creates a direct confidentiality problem because prompts may contain regulated or business-sensitive data while remote serving exposes intermediate state to the cloud stack and accelerator runtime. Separately, the anticipated quantum threat to classical public-key cryptography is driving the PQC migration onto embedded hardware.

Supply: the research response is fast and voluminous. A single survey taxonomises over 260 papers across agentic security applications, threats and defences, and notes that the literature has grown quickly and unevenly. Commercial skill scanners already exist as products, which indicates a paying market even at 9 to 17 per cent detection. The sources say nothing about regulatory mandates or procurement requirements, so that driver is unassessed here.

**TLDR: Demand is created mechanically by agent deployment and the quantum transition; research supply is already large.**

## Novelty (3/5)

The strongest novelty is on the attack and measurement side, where the baseline is that the risk was previously unmeasured. Decomposition attacks, skill composition risk, cross-modal skill attacks and guardrail denial-of-service are each framed as understudied surfaces that prior benchmarks did not capture, and each comes with a new benchmark. Making that risk legible is worth something, but a benchmark is not a control.

**TLDR: Genuinely new threat classes and one or two clean substrate wins; most defensive gains are incremental over an absent baseline.**

## Diffusion (2/5)

The clearest diffusion datum is negative: defensive products are already in the field and are catching 9 to 17 per cent of the attacks in question, with open-source alternatives at 2 to 8 per cent. Diffusion of the tool is not the constraint; efficacy is. The structural defences face harder paths. SOPGuard exists inside one open-source agentic browser; equivalent enforcement in commercial agentic browsers is a vendor decision the sources do not report on. DataGuard, MPX, the FPGA PQC core and DRAM PUFs all require hardware changes or hardware availability, which sets a multi-year cadence, though the DRAM PUF work at least uses commercial off-the-shelf DDR4 chips rather than custom silicon.

A second-order barrier is that the evaluation infrastructure is itself contaminated. On a hardware security competition benchmark, LLM detectors reach 83 per cent detection by exploiting diff-style syntactic comparison rather than genuine security reasoning, and semantics-preserving obfuscation cuts that accuracy by 50 per cent at 10 per cent obfuscation and 78.6 per cent under full obfuscation. If buyers cannot trust headline detection rates, procurement decisions get slower and worse. The Model Context Protocol standardises context exchange and tool invocation but functions as a passive routing layer that does not enforce contextual stability, so the emerging interoperability standard is not itself carrying security guarantees.

**TLDR: Deployed defensive tooling underperforms badly, and the better ideas need vendor or silicon adoption to move at all.**

## Impact (4/5)

The measured harms are not abstract. Code agents produce attack code that compiles and runs end to end in 27 to 32 per cent of cases depending on workspace richness. Agentic browsers act as an automated channel for cross-origin data flows and violate the same-origin policy both in benign settings and under attack, which means the single most load-bearing browser security invariant of the last two decades does not hold once an agent is in the loop. Skill ecosystems expose data leakage, unauthorised operations and tool misuse through composition paths that isolated vetting does not see.

The upside if the defensive layer works is correspondingly large: confidential inference architectures that keep prompts out of the cloud software stack would unlock regulated workloads, and hardware-guaranteed differential privacy would remove the need to trust third-party federated-learning applications with raw sensitive data. The sources do not quantify market size or breach cost, so the impact score reflects breadth of exposure demonstrated, not monetised damage.

**TLDR: The containment gap gates how much autonomy agents can be given, and the affected surface is everything they touch.**

## Timing Now (0-2yr)

This is not a forward-looking risk. Guardrail denial-of-service payloads optimised on one open-source surrogate transfer to eight leading model backbones including Claude, GPT and Gemini. Commercial skill scanners are in market and missing 83 to 91 per cent of cross-modal attacks. Existing agentic browsers frequently violate same-origin policy today.

The defensive timeline is uneven. Software-layer controls such as origin enforcement, install-time cross-modal scanning and controller-driven context validation could ship inside two years because they are software changes to products already in the field. The substrate work is slower: PQC acceleration, dual-mode systolic arrays and hardware-enforced privacy budgets need silicon, and the PQC results show that today's mainstream constrained MCUs cannot run the standardised signature schemes in software at all.

**TLDR: The attacks are already landing on shipped commercial systems; the defences are one to two product cycles behind.**

## Overrated or underrated? Underrated

The specific thing that is underrated is the size of the gap between agent capability and agent containment, and the fact that it is now measured rather than asserted. Three independent results in the same week point the same way: safety checks that hold for whole tasks fail for decomposed ones, vetting that holds per-skill fails on composed paths at 33.6 per cent attack success, and the guardrail that is supposed to hold the line is itself a denial-of-service target that generalises across architectures and vendors. The common structure is that per-item intent classification does not compose, and the industry's default defence is per-item intent classification.

The corollary for investors is that the durable value sits in structural containment rather than in classifiers: origin and capability enforcement in the agent runtime, hardware-guaranteed privacy budgets, attested TEE boundaries with FHE delegation and crypto acceleration in mainstream silicon. The counterweight to the bull case is that current benchmark numbers are unreliable in both directions, as demonstrated by LLM detectors scoring 83 per cent on a hardware CTF benchmark through syntactic diffing rather than reasoning. Treat every reported detection rate, including the alarming ones, as provisional.

## Prediction

By mid-2027, a published successor evaluation of commercial agent-skill scanners will still report detection below 50 per cent on cross-modal language-and-code attacks of the kind measured by SkillMutator, absent a shift from intent classification to runtime capability enforcement.

## Evidence base

- Open-source skill scanners detect 2-8 per cent and commercial scanners 9-17 per cent of language-and-code cross-modal attacks on agent skills.
- In multi-file workspaces, mean jailbreak attack success against code agents reaches about 75 per cent with 32 per cent of generated attack code runnable; agent wrapping raises attack success by 1.6x.
- Composed skill paths reach 33.6 per cent attack success on the capability-flow subset of SCR-Bench, exposing risks largely absent under isolated evaluation.
- Guardrail denial-of-service payloads optimised on a single open-source surrogate transfer to eight leading model backbones including Claude, GPT and Gemini.
- SPHINCS+ is practically unusable and reference Dilithium fails to execute on an STM32F407G Cortex-M4, while an FPGA NTT accelerator on a Zynq-7000 ZedBoard achieves millisecond-level key and signature generation.
- LLM detectors reach 83 per cent on a hardware security competition benchmark via diff-style syntactic comparison; 10 per cent semantics-preserving obfuscation cuts accuracy by 50 per cent and full obfuscation by 78.6 per cent.

## Open questions

- Do the structural defences hold under adaptive attack? SOPGuard and GT-MCP are evaluated against known attack sets; neither source reports an attacker optimising specifically against the deployed defence.
- Can install-time scanning ever close a composition-based gap, given that SCR-Bench shows the harm emerges from path-level state changes across skills rather than from any single artefact?
- Will PQC acceleration reach the constrained MCU class itself, or does the Cortex-M4 result imply an entire installed base that must be replaced with FPGA-SoC or accelerator-bearing parts?
- How much of the reported attack-success and detection literature survives the benchmark-contamination problem that AttackonCTF documents for hardware security competitions?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
