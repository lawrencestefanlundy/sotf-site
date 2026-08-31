---
type: concept
slug: post-training
canonical_name: Post Training
aliases: []
parent_concepts: []
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
frontier:
- What benchmark deltas, on which medical evaluation sets, are attributable to each stage (SFT vs DPO vs GRPO reward modelling) when stages are ablated independently?
- Do the eight sequential DPO iterations (v0 to v7) yield monotonic gains, or does performance saturate or regress after a specific iteration count?
- How does LoRA at r = 8 compare with full-parameter post-training on the same 27B base, in both task accuracy and compute cost?
- Does a 6,283-pair preference set generalise beyond the curating institution's data distribution, and how does performance scale with preference-pair count?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-20-ai-inference-economics-column
  title: Money Stuff-style column on AI model pricing, open weights and datacentre monetisation
  date: '2026-07-20'
  kind: web
neighbors: []
---
## Physics / mechanism

Post-training is the set of procedures applied to a pretrained language model to adapt its behaviour to a task, domain or preference specification, without repeating the base pretraining run. The single supplied source treats it as a staged pipeline rather than a single operation: data synthesis and curation, supervised instruction fine-tuning, preference optimisation, and reinforcement-learning-based reward model training.

In the documented case, a medical foundation model was built on the Qwen3.5-27B base. The instruction supervised fine-tuning stage used LoRA (low-rank adaptation) with rank r = 8 and scaling factor 32, executed with the MS-Swift framework, and produced successive model iterations labelled 2.0.0, 2.0.2 and 2.0.4. LoRA restricts updates to a small set of injected low-rank matrices, so the parameter count touched during adaptation is a small fraction of the 27B base.

The preference alignment stage applied Direct Preference Optimization (DPO) to 6,283 curated medical preference pairs, using a DPO-RPO combined loss with beta = 0.3 and an RPO term weighted at 0.1, run across eight progressive training iterations (v0 to v7). A parallel branch used Group Relative Policy Optimization (GRPO) for reward model training. Key controllable parameters visible here are the LoRA rank and scaling, the DPO temperature-like beta, the auxiliary loss weight, and the number of sequential alignment iterations.

Data preparation is treated as part of post-training rather than a precondition. The pipeline drew from a proprietary MySQL database organised by a MedicalCategoryTree, with validation by a medical PhD team, semantic deduplication using a Chinese RoBERTa encoder, and API-assisted language refinement.

## Competitive landscape

The source supports a comparison only between the stages inside one pipeline, not between competing vendors. Supervised instruction tuning fixes the output format and domain vocabulary; DPO adjusts relative ranking of candidate responses using paired preference data and avoids training an explicit reward model; GRPO is used in a separate branch to train a reward model, implying that the group-relative and pairwise-preference routes were treated as complementary rather than substitutes. The broader positioning is that post-training is the cheap-adaptation layer above a general base model: a 27B open base was specialised for medicine using LoRA adapters and a few thousand preference pairs, rather than by pretraining a medical model from scratch.

## Evidence base

- A multi-stage post-training pipeline (data synthesis, instruction SFT, DPO, GRPO reward modelling) was used to build a medical foundation model on Qwen3.5-27B, reported 30 June 2026.
- Instruction supervised fine-tuning used LoRA with r = 8 and scaling 32 via MS-Swift, producing iterations 2.0.0, 2.0.2 and 2.0.4.
- DPO was applied to 6,283 curated medical preference pairs with a DPO-RPO loss (beta = 0.3, RPO = 0.1) over eight iterations, v0 to v7.
- GRPO was run in a parallel branch for reward model training.
- Training data came from a proprietary MySQL corpus organised by a MedicalCategoryTree, validated by a medical PhD team and deduplicated semantically with Chinese RoBERTa.

## Frontier (open questions)

- What benchmark deltas, on which medical evaluation sets, are attributable to each stage (SFT vs DPO vs GRPO reward modelling) when stages are ablated independently?
- Do the eight sequential DPO iterations (v0 to v7) yield monotonic gains, or does performance saturate or regress after a specific iteration count?
- How does LoRA at r = 8 compare with full-parameter post-training on the same 27B base, in both task accuracy and compute cost?
- Does a 6,283-pair preference set generalise beyond the curating institution's data distribution, and how does performance scale with preference-pair count?

*Synthesised 2026-08-31 from 1 KB sources by the resynth pipeline; citations are KB source slugs.*
