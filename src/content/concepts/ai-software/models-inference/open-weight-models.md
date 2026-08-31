---
type: concept
slug: open-weight-models
canonical_name: Open Weight Models
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2026-07-18-post-training-inference-loop-open-weight-models-are-turning]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 1
frontier:
- Did independent benchmarking after the 27 July 2026 weight release reproduce Moonshot's claimed K3 parameter activation, 1M context behaviour and 2.5x scaling-efficiency figure 2026 07 15 kimi k3 launch moonshot?
- What is the measured cost per million tokens of self-serving K3 on a 64-plus accelerator supernode, and does it beat the $3/$15 hosted price at realistic utilisation 2026 07 17 the once and future kimi?
- Does the 95% specialised-token share reported by one serving vendor hold across other serving providers, and does the resulting data flywheel accrue to the serving vendor, the application owner or the model lab 2026 07 18 post training inference loop open weight models are turning?
- Do open weight releases measurably compress closed-lab pricing or gross margins, which would test the contestability and mediocre-return thesis 2026 07 21 minack dud competition mediocre ai returns?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-20-ai-inference-economics-column
  title: Money Stuff-style column on AI model pricing, open weights and datacentre monetisation
  date: '2026-07-20'
  kind: web
- slug: 2026-07-18-post-training-inference-loop-open-weight-models-are-turning
  title: Open Weight Models Are Turning Inference Into A Control Point
  date: '2026-07-18'
  kind: web
- slug: 2026-07-17-the-once-and-future-kimi
  title: The Once and Future Kimi
  date: '2026-07-17'
  kind: substack
- slug: 2026-07-16-china-open-weight-strategy-loeber-teortaxes
  title: Why does China keep releasing open-weight models? — Loeber + Teortaxes threads (K3 week)
  date: '2026-07-16'
  kind: web
- slug: 2026-07-15-kimi-k3-launch-moonshot
  title: Kimi K3 — Moonshot launch post (architecture, quantisation, serving requirements)
  date: '2026-07-15'
  kind: web
neighbors: []
---
## Physics / mechanism

Open weight models are models whose trained parameters are published for download, so that any party can serve, fine-tune, quantise or distil them on their own hardware rather than calling a hosted API. The distinguishing technical property is not the architecture but the point of control: once weights are downloadable, the serving stack and the post-training stack become separable from the lab that trained the model.

Recent frontier-scale open weight releases are extremely sparse mixture-of-experts systems, which shifts the cost structure of self-serving. Kimi K3 was published with 2.8T total parameters and "effectively activating 16 out of 896 experts" per token under a scheme Moonshot calls Stable LatentMoE, with 1M context and native vision kimi k3 launch moonshot. Sparsity of that degree means the whole model is never woken for a single token, but it also distributes the router's 16 selected experts across 16 different chips, which is why Moonshot recommend a 64-plus accelerator supernode to serve it the once and future kimi. Serving requirements, not licence terms, therefore set who can actually run a frontier open weight model.

The second parameter set is memory per token. K3 stacks DeepSeek-lineage Gated MLA, which compresses the KV cache, with Kimi Delta Attention, a linear attention variant with per-channel forgetting that replaces the KV cache with a fixed-size compressed running state, interleaved with regular attention layers; Attention Residuals selectively retrieve representations across depth rather than accumulating them uniformly kimi k3 launch moonshot. Moonshot claim 2.5x scaling efficiency from this chain, a vendor number the once and future kimi. Pricing was set at $3 in / $15 out per million tokens, parity with Claude Sonnet rather than the historic Chinese discount, with the model positioned by its own vendor as trailing Fable 5 and GPT-5.6 Sol overall while winning on game-dev and UI tasks kimi k3 launch moonshot.

Downstream, open weights are mostly consumed as substrates for specialisation rather than as drop-in replacements. Fireworks reported that 95% of tokens it serves come from customer-specialised models, that is fine-tuned open weights, adapters and distillations, rather than downloadable third-party models served as-is post training inference loop open weight models are turning.

## Competitive landscape

The competitive question is whether openness commoditises the closed frontier. One reading holds that releasing frontier open weight models commoditises closed models, challenges the closed labs' businesses and splinters their most valuable asset, their teams, since staff leave to build on open weights when the labs' primacy looks uncertain; on that reading Chinese labs stay ahead and could switch to closed once the lead is large enough, with usage-driven dependence as the strategic payoff china open weight strategy loeber teortaxes. The macro corollary is that AI provision looks like a competitive, mediocre-return industry, partly because of intense and cheap Chinese competition, which would force providers to invest less and hit the "shovel sellers" that led equities for three years minack dud competition mediocre ai returns.

Against a full commoditisation reading, serving vendors compete on the same fine-tune plus RL plus serve stack, so differentiation may collapse to execution rather than structure, and closed frontier models may stay far enough ahead that "own your intelligence on open weights" remains a minority of workloads post training inference loop open weight models are turning. Vendor self-positioning is consistent with a residual gap: K3 was framed by Moonshot as trailing the leading closed models overall while priced at parity with a closed mid-tier model kimi k3 launch moonshot.

## Evidence base

- Kimi K3 launched 15 July 2026 with 2.8T total parameters, 16 of 896 experts activated per token, 1M context and native vision, all vendor numbers unverified at capture, with weights promised for 27 July 2026 as the first opportunity for independent benchmarking kimi k3 launch moonshot.
- K3 was priced at $3 in / $15 out per million tokens, parity with Claude Sonnet rather than a Chinese discount, and positioned as trailing Fable 5 and GPT-5.6 Sol overall while winning game-dev and UI tasks kimi k3 launch moonshot.
- Serving K3 is recommended on a 64-plus accelerator supernode because the router sends each token to 16 experts living on 16 different chips; the vendor claims 2.5x scaling efficiency from the MLA plus sparsity plus KDA chain the once and future kimi.
- Fireworks reported on 18 July 2026 that 95% of tokens it serves come from customer-specialised models, evidence of demand for specialisation of open weights over serving third-party downloads unchanged post training inference loop open weight models are turning.
- Two strategic readings circulated on 16 July 2026 arguing Chinese open weight releases are deliberate strategy; Loeber's is a commoditise-to-splinter thesis aimed at the closed labs' teams and business models china open weight strategy loeber teortaxes.
- A 21 July 2026 macro note argued the contestability case for AI provision has firmed up, implying mediocre returns on invested capital for AI providers, partly because of cheap Chinese competition minack dud competition mediocre ai returns.
- A medRxiv preprint dated 22 July 2026 evaluated five leading LLMs, including o3, GPT-4.1 and GPT-5.1, generating synthetic colonoscopy-preparation dialogues as both AI coach and simulated patient, scoring correctness, harmfulness and diversity medrxiv evaluating large language models for colonosco.

## Frontier (open questions)

- Did independent benchmarking after the 27 July 2026 weight release reproduce Moonshot's claimed K3 parameter activation, 1M context behaviour and 2.5x scaling-efficiency figure kimi k3 launch moonshot?
- What is the measured cost per million tokens of self-serving K3 on a 64-plus accelerator supernode, and does it beat the $3/$15 hosted price at realistic utilisation the once and future kimi?
- Does the 95% specialised-token share reported by one serving vendor hold across other serving providers, and does the resulting data flywheel accrue to the serving vendor, the application owner or the model lab post training inference loop open weight models are turning?
- Do open weight releases measurably compress closed-lab pricing or gross margins, which would test the contestability and mediocre-return thesis minack dud competition mediocre ai returns?

*Synthesised 2026-08-31 from 6 KB sources by the resynth pipeline; citations are KB source slugs.*
