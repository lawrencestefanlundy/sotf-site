---
type: concept
slug: state-space-models
canonical_name: State Space Models (SSMs)
aliases:
- SSM
- selective state space models
- Mamba
- linear-time sequence models
parent_concepts: []
related_concepts:
- neuromorphic-computing
- in-memory-computing
- edge-ai
sources:
- '[[2025-cartesia-on-device-ssm]]'
- '[[2026-06-18-sensifai-hybrids-deck]]'
- '[[2026-07-31-etched-research-sprint]]'
- '[[2025-06-wisconsin-mamba-chiplet-gf22]]'
- '[[2025-08-emamba-edge-acceleration]]'
- '[[2026-07-01-sensifai-memo-streaming-physical-ai]]'
- '[[2026-03-mamba-3-iclr]]'
- '[[2026-06-23-on-device-llms-state-of-union-2026]]'
frontier:
- Do Mamba-3's smaller states and MIMO decoding hold their parameter-efficiency gains at frontier scale, or does the gap with attention re-open above the sizes reported at ICLR 2026?
- Have the core SSM primitives stabilised enough after Mamba-2 to Mamba-3 that a fixed-function accelerator taped out in 2026 is still relevant in 2029?
- Does the hybrid attention-to-SSM layer ratio converge to a stable value across labs, which is what determines whether disaggregated designs like DUET are worth building?
- Can any commercial vendor reproduce eMamba's ~48× energy advantage on its own silicon against a like-for-like accuracy baseline, rather than citing the academic 22nm ViT comparison?
- Does the energy advantage of dedicated SSM silicon over optimised kernels on existing NPUs stay large (>5x) and durable, or does software close it to ~2x?
- Does a sub-watt always-on streaming socket (hearing aids, AR perception) reach volume general silicon cannot serve, giving a dedicated SSM ASIC a why-now?
- Does the architecture stabilise (Mamba-3 onwards) enough to tape out fixed-function silicon, or does it keep moving fast enough to favour programmable / kernel approaches?
last_updated: '2026-08-31'
tags:
- concept
mention_count: 22
scorecard:
  viability: 4
  drivers: 4
  novelty: 4
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-07-31-etched-research-sprint
  title: Etched research sprint — tape-out speed, HBM supply, customer orders (4-lane web sweep)
  date: '2026-07-31'
  kind: web
- slug: 2026-07-01-sensifai-memo-streaming-physical-ai
  title: SensifAI — Purpose-Built Silicon for Streaming Physical AI (funding memo)
  date: '2026-07-01'
  kind: web
- slug: 2026-06-23-on-device-llms-state-of-union-2026
  title: On-device LLMs, the small-model frontier, and NPU throughput (2025-26 update)
  date: '2026-06-23'
  kind: web
- slug: 2026-06-18-sensifai-hybrids-deck
  title: SensifAI — Funding Round deck (sensifai.vercel.app/hybrids)
  date: '2026-06-18'
  kind: web
- slug: 2026-03-mamba-3-iclr
  title: Mamba-3 (ICLR 2026)
  date: '2026-03-01'
  kind: web
- slug: 2025-08-emamba-edge-acceleration
  title: 'eMamba: Efficient Acceleration Framework for Mamba Models in Edge Computing'
  date: '2025-08-14'
  kind: web
- slug: 2025-cartesia-on-device-ssm
  title: Cartesia — The on-device intelligence update
  date: '2025-08-01'
  kind: web
- slug: 2025-06-wisconsin-mamba-chiplet-gf22
  title: First Mamba Chiplet in GF 22nm — UW–Madison CHIPS
  date: '2025-06-12'
  kind: web
neighbors:
- slug: neuromorphic-computing
  name: Neuromorphic Computing
  path: /compute/non-conventional/neuromorphic-computing/
  macro: compute
- slug: in-memory-computing
  name: In-Memory Computing
  path: /memory/emerging-memory/in-memory-computing/
  macro: memory
- slug: edge-ai
  name: Edge AI
  path: /compute/ai-edge/edge-ai/
  macro: compute
---
**State space models replace the quadratic attention of transformers with a linear-time recurrence carrying a fixed-size state, and as of 2026 they are shipping inside mainstream hybrid checkpoints such as Qwen3-Next and NVIDIA Nemotron rather than displacing transformers outright <sup class="ref"><a href="https://v-chandra.github.io/on-device-llms/" title="On-device LLMs, the small-model frontier, and NPU throughput (2025-26 update)" rel="noopener">ref</a></sup>.**

## Summary

The architecture is still moving. Mamba-3, published at ICLR 2026 by authors at CMU, Princeton, Cartesia AI and Together AI, claims 2× smaller states, enhanced multi-input multi-output decoding aimed explicitly at hardware efficiency, improved scaling laws that narrow the gap with transformers at equal parameter counts, and cleaner integration with attention layers in hybrid stacks **2026 03 Mamba 3 Iclr**. That last point matters more than the others: the dominant deployment pattern is not pure SSM but Mamba-plus-attention hybrids, which is how Qwen3-Next and NVIDIA Nemotron-3 handle long context <sup class="ref"><a href="https://v-chandra.github.io/on-device-llms/" title="On-device LLMs, the small-model frontier, and NPU throughput (2025-26 update)" rel="noopener">ref</a></sup>.

## Viability (4/5)

The evidence for basic viability is no longer benchmark-only. Mamba-2 and related linear mixers appear as production sequence-mixer designs in checkpoints instrumented by third parties, alongside MLA, MHA and GQA variants, in a study spanning DeepSeek, Qwen and Nemotron models. Accelerator work is evaluated against real hybrid models including Nemotron-H-56B and Zamba2-7B. Mamba-3 reports narrowing the parameter-efficiency gap with transformers rather than closing it **2026 03 Mamba 3 Iclr**, which is the honest reading: SSMs are viable as a component, and the mainstream answer is a hybrid.

The unresolved half is execution. Multiple independent 2026 architecture papers converge on the same diagnosis: Mamba workloads cannot run at near-peak speed on current hardware because of irregular data movement, prefix dependencies and unfusable operator cascades. That is a solvable engineering problem with visible progress, not an existence question, which is why this scores 4 rather than 5.

**TLDR: Trained, published and shipping inside production hybrid checkpoints; the residual doubt is hardware efficiency, not learnability.**

## Drivers (4/5)

Supply: the research pipeline is unusually thick for a single architecture family. Between August 2025 and August 2026 the sources show eMamba (edge framework, up to 10× speedup and 48.6× lower energy on FPGA/ASIC) **2025 08 Emamba Edge Acceleration**, a first Mamba chiplet tape-out in GlobalFoundries 22nm **2025 06 Wisconsin Mamba Chiplet Gf22**, Mambalaya, HEMERA, LowRank-SSM and DUET, plus two NSF awards of $400,000 each on rethinking spiking networks as SSMs. Note also a counter-driver on the supply side: mobile NPUs already deliver over 100 tokens/sec decode and around 11,000 tokens/sec prefill on optimised small models <sup class="ref"><a href="https://v-chandra.github.io/on-device-llms/" title="On-device LLMs, the small-model frontier, and NPU throughput (2025-26 update)" rel="noopener">ref</a></sup>, which reduces the urgency of SSM-specific silicon for phone-class devices.

**TLDR: Demand from long-context and battery-powered streaming inference; supply from a dense 2025-26 wave of kernel, accelerator and architecture work.**

## Novelty (4/5)

The comparison class is transformer attention. The structural claim is that SSMs remove both the O(n²) sequence scaling and the growing KV cache, giving a fixed inference memory footprint **2025 Cartesia On Device Ssm**. The measured margins split by axis. On energy in dedicated silicon the gap is order-of-magnitude: eMamba reports up to 10× speedup and 48.6× lower energy on FPGAs and ASICs, and explicitly notes that no hardware-acceleration framework had previously been optimised for Mamba at the edge **2025 08 Emamba Edge Acceleration**. On end-user latency on commodity silicon the margins are smaller: roughly 1.5× lower time-to-first-audio and 2× lower real-time factor for Cartesia's Sonic against transformers **2025 Cartesia On Device Ssm**. On model quality per parameter, Mamba-3 narrows rather than reverses the transformer advantage **2026 03 Mamba 3 Iclr**.

**TLDR: Linear-time inference with no KV cache is a genuine asymptotic change from attention; the measured margins are large on energy and moderate on latency.**

## Diffusion (4/5)

The adoption question has largely resolved in one specific form. Qwen3-Next and NVIDIA Nemotron-3 use Mamba-attention hybrids for efficient long context, which the sources read as confirmation that the SSM line is mainstream rather than speculative <sup class="ref"><a href="https://v-chandra.github.io/on-device-llms/" title="On-device LLMs, the small-model frontier, and NPU throughput (2025-26 update)" rel="noopener">ref</a></sup>. Independent systems research now treats Mamba-2 as one of five standard sequence-mixer designs when sampling production MoE checkpoints. That is diffusion into the frontier stack, achieved in roughly two years.

The barriers apply to the remaining forms. Kernel and hardware support is the first: SSM recurrences map poorly to matmul-centric accelerators, so vendors must either co-design (DUET reports 4× faster time to first token, 1.4× higher throughput and 1.5× lower time between tokens versus a B200 GPU by disaggregating prefill and decode packages) or accept sub-peak utilisation. The second is architectural churn: Mamba-2 to Mamba-3 changed the core primitives, which is a direct risk to anyone taping out fixed-function SSM silicon **2026 03 Mamba 3 Iclr**. The only dedicated SSM ASIC in the sources is an academic chiplet, first taped out in early May 2025 **2025 06 Wisconsin Mamba Chiplet Gf22**; the commercial leader competes on software and custom kernels on commodity Apple silicon instead **2025 Cartesia On Device Ssm**.

**TLDR: Already diffused as a hybrid component in frontier checkpoints; diffusion as a full transformer replacement, or as dedicated silicon, has not happened.**

## Impact (4/5)

The deduction is that the hybrid architecture caps the upside. Because attention layers remain, DUET still has to build a runtime-configurable accelerator that handles both mixed Mamba and attention layers, and the asymmetric prefill/decode problem does not disappear, it inherits. Real cost reductions, not a new cost curve.

**TLDR: Changes the cost structure of long-context and streaming inference, and opens battery-powered continuous perception, but mostly as a component rather than a regime change.**

## Timing Now (0-2yr)

The software side has already arrived. Hybrid Mamba-attention models are shipping from major labs <sup class="ref"><a href="https://v-chandra.github.io/on-device-llms/" title="On-device LLMs, the small-model frontier, and NPU throughput (2025-26 update)" rel="noopener">ref</a></sup>, the frontier architecture was published in March 2026 **2026 03 Mamba 3 Iclr**, and third-party systems papers benchmark against real hybrid checkpoints as a matter of routine. Anyone building inference infrastructure needs an answer to SSM layers now, not later.

The hardware side is two to five years behind. The accelerator literature dated mid-2026 is still FPGA prototypes, simulator evaluations and academic ASIC chiplets **2025 06 Wisconsin Mamba Chiplet Gf22**, and NSF's foundational SSM-at-the-edge programme only started on 1 July 2026. Until the primitives stabilise, the near-term efficiency gains will come from kernels and dataflow on general hardware rather than fixed-function chips.

**TLDR: Hybrid SSM models are in production today; the hardware efficiency layer lands over the next two to five years.**

## Overrated or underrated? Fairly rated

The claim that SSMs replace transformers is overrated, and the sources do not support it: Mamba-3 narrows the gap at equal parameter counts, and the deployed form is hybrid with attention retained **2026 03 Mamba 3 Iclr** <sup class="ref"><a href="https://v-chandra.github.io/on-device-llms/" title="On-device LLMs, the small-model frontier, and NPU throughput (2025-26 update)" rel="noopener">ref</a></sup>. The claim that SSMs are a lab curiosity is also wrong, and has been for at least a year. What is fairly rated is the middle position: linear-time state-space mixers are now a standard component of frontier sequence models, they measurably cut memory traffic and energy for long sequences, and they will be a permanent part of the inference stack.

## Prediction

By 31 July 2027, at least one further frontier checkpoint from a major lab will ship with a Mamba-family linear mixer in a hybrid attention configuration, while no commercial fixed-function SSM-only ASIC will be in volume production.

## Evidence base

- Aug 2025: eMamba reports up to 10× speedup and 48.6× lower energy for Mamba on FPGAs and ASICs, and states no prior hardware-acceleration framework was optimised for edge Mamba deployment **2025 08 Emamba Edge Acceleration**.
- Early May 2025: the first dedicated Mamba accelerator chiplet (e-chip-V1) taped out in GlobalFoundries 22nm, from an academic lab rather than a startup **2025 06 Wisconsin Mamba Chiplet Gf22**.
- March 2026: Mamba-3 published at ICLR 2026 by CMU, Princeton, Cartesia AI and Together AI, claiming 2× smaller states, MIMO decoding for hardware efficiency, and improved scaling that narrows the gap with transformers at equal parameter counts **2026 03 Mamba 3 Iclr**.
- June 2026: Qwen3-Next and NVIDIA Nemotron-3 confirmed as shipping Mamba-attention hybrids for efficient long context; mobile NPUs meanwhile exceed 100 tokens/sec decode and ~11,000 tokens/sec prefill on optimised small models <sup class="ref"><a href="https://v-chandra.github.io/on-device-llms/" title="On-device LLMs, the small-model frontier, and NPU throughput (2025-26 update)" rel="noopener">ref</a></sup>.
- June 2026: DUET, a disaggregated prefill/decode accelerator for hybrid Mamba-Transformer models, reports 4× faster time to first token, 1.4× higher throughput and 1.5× lower time between tokens versus a B200 GPU on Nemotron-H-56B, Zamba2-7B and Llama3-8B, on the grounds that SSM recurrences map poorly to matmul-centric accelerators.
- Aug 2026: LowRank-SSM finds Mamba input and output projection layers account for over 60% of per-token runtime at sequence lengths of 1,024 and beyond on FPGA, identifying projection rank as an unexplored hardware design variable.

## Open questions

- Do Mamba-3's smaller states and MIMO decoding hold their parameter-efficiency gains at frontier scale, or does the gap with attention re-open above the sizes reported at ICLR 2026?
- Have the core SSM primitives stabilised enough after Mamba-2 to Mamba-3 that a fixed-function accelerator taped out in 2026 is still relevant in 2029?
- Does the hybrid attention-to-SSM layer ratio converge to a stable value across labs, which is what determines whether disaggregated designs like DUET are worth building?
- Can any commercial vendor reproduce eMamba's ~48× energy advantage on its own silicon against a like-for-like accuracy baseline, rather than citing the academic 22nm ViT comparison?

---
*Assessment drafted 2026-08-31 from up to 16 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
