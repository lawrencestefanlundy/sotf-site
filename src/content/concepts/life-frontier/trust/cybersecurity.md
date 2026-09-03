---
type: concept
slug: cybersecurity
canonical_name: Cybersecurity
aliases: []
kind: technology
parent_concepts:
- life-frontier
- trust
related_concepts: []
sources:
- '[[2026-07-24-the-huggingface-incident]]'
- '[[2023-10-19-e20-the-state-of-privacy-enhancing]]'
- '[[2026-04-10-state-of-the-future-friday-four-551]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2026-07-06-willdepue-stargate-for-data]]'
- '[[2025-12-16-draft-nist-guidelines-rethink-cybersecurity-for-the-ai-era]]'
- '[[2026-07-25-thoughts-on-ai-and-power]]'
- '[[2026-07-26-ai-breach-frequency-autonomous-soc]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-03-28-agentic-ai-security-funding-mna]]'
- '[[2026-05-29-silicon-shock-the-macro-of-tech-inflation]]'
- '[[2026-08-20-callosum-100m-seed-announcement]]'
scorecard:
  viability: null
  drivers: null
  novelty: null
  diffusion: null
  impact: null
  timing_band: Unclear
  verdict: ''
scorecard_status: draft
mention_count: 115
sources_7d: 5
sources_30d: 37
recent_mentions:
- slug: 2026-08-20-callosum-100m-seed-announcement
  title: Callosum announces $100M seed led by Atomico (round coverage + Companies House filings)
  date: '2026-08-20'
  kind: web
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-26-ai-breach-frequency-autonomous-soc
  title: AI-enabled attack frequency and autonomous-SOC economics, 2026
  date: '2026-07-26'
  kind: web
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-24-the-huggingface-incident
  title: The HuggingFace Incident
  date: '2026-07-24'
  kind: substack
- slug: 2026-07-06-willdepue-stargate-for-data
  title: A Stargate for Data — will depue (OpenAI) on >$100B/year data spend by 2030
  date: '2026-07-06'
  kind: web
- slug: 2026-05-29-silicon-shock-the-macro-of-tech-inflation
  title: 'Silicon Shock: The Macro of Tech Inflation'
  date: '2026-05-29'
  kind: web
- slug: 2026-04-10-state-of-the-future-friday-four-551
  title: 'State of the Future: Friday Four'
  date: '2026-04-10'
  kind: substack
neighbors: []
---
**Cybersecurity is being restructured around autonomous LLM agents that now perform triage, vulnerability discovery and incident response, while simultaneously becoming the largest new attack surface and lowering the skill floor for offence.**

## Summary

Cybersecurity here means the practice of defending computing systems, networks and the physical processes they control against deliberate attack. The traditional stack is human analysts in a Security Operations Centre (SOC) working through alerts from detection tools, plus periodic penetration testing by trained practitioners using deterministic, narrowly scoped tooling. The current body of research is dominated by one change: large language model agents that can plan, execute commands, read code and iterate are being inserted into every stage of that stack. A survey covering more than 260 papers finds LLM-based agents now used throughout cybersecurity, and organises the field into applications, threats to the agents themselves, and defences for them.

The mechanics differ by task. For alert triage, models are trained to reason about whether a detection is a genuine threat rather than emit a label directly, with a separate calibrator reading the reasoning trace because chain-of-thought degrades the label-token probabilities that automated triage depends on. For vulnerability work, compact models are fine-tuned on security reasoning and repository exploration data, then trained with reinforcement learning from verifiable rewards over real vulnerable repositories. For defence policy learning, deep reinforcement learning agents are trained in cyber ranges, though almost always against static heuristic attackers.

The parameters that decide outcomes are: whether source code is available (agents are much weaker on binaries, which is where malware, firmware and proprietary software live); whether evaluation is contamination-free and operationally representative; whether autonomy can be tiered against trust and human oversight rather than treated as binary; and the structural cost asymmetry between offence and defence, which the same technology amplifies on both sides but not symmetrically.

A second, quieter strand in the sources is the collision of cybersecurity with domains that were previously governed by safety or physical engineering: industrial control networks where draft standard prEN 50742 mandates cryptography inside safety-critical communication, satellite systems across space, ground, communication and user segments, and hardware-assisted run-time control-flow monitoring for embedded systems.

## Viability (unscored)

## Drivers (unscored)

## Novelty (unscored)

## Diffusion (unscored)

## Impact (unscored)

## Timing Unclear

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
