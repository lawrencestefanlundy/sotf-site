---
type: concept
slug: agentic-payments
canonical_name: Agentic Payments
aliases:
- agent payments
- agent commerce payments
- machine-to-machine payments
- M2M payments
- agentic commerce
- agent-native payments
route: insig
parent_concepts:
- stablecoins
- ai-agents
related_concepts:
- stablecoin-clearing
- x402
- payment-mandates
- agent-identity-kya
sources:
- '[[2026-06-13-agentic-payments-value-capture]]'
- '[[2026-06-14-frontier-ai-value-capture]]'
- '[[2026-06-19-onchain-agent-volume-tracking]]'
- '[[2026-06-13-mckinsey-agentic-commerce]]'
- '[[2026-07-21-stablecoin-market-structure]]'
- '[[2026-07-31-4mica-update-verification]]'
frontier:
- Does clearing/netting stay a separate layer, or get absorbed by stablecoin issuers + the protocol owners?
- When does agent-initiated transaction volume cross the threshold that makes a dedicated clearing layer necessary (Akash's 6-vs-18-month question)?
- 'Which authorization standard wins, or does it fragment: Google AP2 mandates, Coinbase x402, OpenAI/Stripe ACP, ERC-8183?'
- Are clearing + credit-backing regulated activities (clearing house / EMI / credit institution) under MiCA / PSD?
last_updated: 2026-06-11
tags:
- concept
descendants:
- agent-identity-kya
- payment-mandates
- stablecoin-clearing
- x402
mention_count: 18
sources_7d: 0
sources_30d: 3
recent_mentions:
- slug: 2026-08-06-4mica-base-mainnet-onchain-verification
  title: 4Mica's Base mainnet contract, verified on-chain
  date: '2026-08-06'
  kind: web
- slug: 2026-07-31-4mica-update-verification
  title: Verifying 4Mica's Q2 investor update against primary sources
  date: '2026-07-31'
  kind: web
- slug: 2026-07-30-arxiv-before-agents-speak-pre-hoc-failure-risk-inference-in-multi-
  title: 'Before Agents Speak: Pre-hoc Failure Risk Inference in Multi-Agent Systems'
  date: '2026-07-30'
  kind: paper
- slug: 2026-07-21-stablecoin-market-structure
  title: Stablecoin market structure and value capture — commissioned research pass
  date: '2026-07-21'
  kind: web
- slug: 2026-07-21-x402-protocol-state
  title: x402 protocol state, governance and volume — commissioned research pass
  date: '2026-07-21'
  kind: web
- slug: 2026-07-21-agent-identity-kya-landscape
  title: Agent identity / KYA — landscape, demand and value capture, commissioned research pass
  date: '2026-07-21'
  kind: web
- slug: 2026-06-19-onchain-agent-volume-tracking
  title: How to track on-chain agent-transaction volume (x402) — sources, method, baseline
  date: '2026-06-19'
  kind: web
- slug: 2026-06-14-frontier-ai-value-capture
  title: 'Frontier AI value capture: where the $4T accrues (research synthesis)'
  date: '2026-06-14'
  kind: web
neighbors:
- slug: stablecoin-clearing
  name: Stablecoin Clearing & Netting
  path: /ai-software/agents/stablecoin-clearing/
  macro: ai-software
- slug: x402
  name: x402
  path: /ai-software/agents/x402/
  macro: ai-software
- slug: payment-mandates
  name: Payment Mandates
  path: /ai-software/agents/payment-mandates/
  macro: ai-software
- slug: agent-identity-kya
  name: Agent Identity (KYA)
  path: /ai-software/agents/agent-identity-kya/
  macro: ai-software
---
**What it is.** Payment infrastructure built for *AI agents* transacting autonomously, rather than for a human present at checkout. The defining shift: the payer is software acting on a delegated mandate, transactions are high-frequency and often low-value (micro), and authorization/identity/dispute handling must be machine-native.

> Provenance note: this page is synthesised from the 4Mica call substrate in the KB plus general knowledge (assistant cutoff Jan 2026). Specific competitor facts (funding, dates) are flagged `[verify]` and should be hardened with a `/kb-research agentic payments` pass before being cited in any artefact.

## Why the existing rails break

Card networks (Visa/Mastercard) assume a human present, ~2–3% interchange, chargeback/dispute machinery, and KYC on a person. For agents this fails three ways:
1. **Economics** — 2–3% + fixed fees make sub-dollar, high-frequency agent payments uneconomic.
2. **Authorization** — there is no human to tap/approve; you need a *verifiable delegated mandate* (what the agent is allowed to spend, on what, for whom).
3. **Identity & dispute** — "who is this agent, on whose behalf" (know-your-agent / KYA) and machine-speed dispute/refund have no native primitive on card rails.

Stablecoins (USDC, USDT, PYUSD) supply the missing rail: programmable, instant, ~zero marginal cost, global. Regulatory clarity (US GENIUS Act; EU MiCA) de-risked them through 2024–2026.

## The stack (2025–2026)

| Layer | What it does | Players / standards |
|---|---|---|
| **Authorization / protocol** | How an agent proves it may pay, and how a merchant accepts | Google **AP2** (intent + cart *mandates*; 60+→100+ partners) · Coinbase **x402** (HTTP 402, pay-per-request in USDC; → **Linux Foundation** Apr 2026) · OpenAI+Stripe **ACP** (Instant Checkout) · Google+Shopify **UCP** (Jan 2026) · Visa **Intelligent Commerce** / Mastercard **Agent Pay / AP4M** · **ERC-8183 "Agentic Commerce"** (EF + Virtuals; primitive is a "Job", Draft Feb 2026) · Anthropic **MCP** (discovery layer payments compose against) |
| **Identity (KYA)** | Know-your-agent, attribution to a principal | Skyfire, Catena, emerging standards |
| **Settlement rail** | Moves the value | Stablecoins: Circle (USDC), Tether (USDT), PayPal (PYUSD); the Stripe–Visa–Mastercard–Coinbase stablecoin consortium `[verify, ~Jun 2026]` |
| **Clearing / netting** | Aggregates and nets many agent micro-payments so they don't each settle on-chain; capital efficiency, dispute resolution, credit | **[Stablecoin Clearing & Netting](/ai-software/agents/stablecoin-clearing/)** — 4Mica's wedge; least-built layer |

## The key technical primitive: authorization/settlement separation

4Mica's founder (**Akash Madhusudan**, PhD cryptography, COSIC/Bart Preneel) frames the core as **separating payment authorization from settlement** — the agent authorizes intent in the critical path (instant, low-latency), while settlement/netting happens off the critical path with capital-efficient (non-idle) collateral and a dispute/default-remediation flow. This is the clearing-house pattern applied to agent micro-payments. See [Stablecoin Clearing & Netting](/ai-software/agents/stablecoin-clearing/).

## Frontier

The open questions are in the frontmatter `frontier`. The load-bearing one is **whether clearing stays a distinct, capturable layer** or is absorbed by the rail owners (Circle / the card-network consortium) and protocol owners (Google / OpenAI / Coinbase). That is the crux of the investment thesis in **Agentic Payment Rails**.
