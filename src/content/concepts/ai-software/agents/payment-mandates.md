---
type: concept
slug: payment-mandates
canonical_name: Payment Mandates
aliases:
- AP2
- Agent Payments Protocol
- ACP
- Agentic Commerce Protocol
- UCP
- verifiable intent
- agent mandate
route: insig
parent_concepts:
- agentic-payments
related_concepts:
- agentic-payments
- agent-identity-kya
- x402
- stablecoins
sources:
- '[[2026-07-21-agent-identity-kya-landscape]]'
frontier:
- Does ACP recover after OpenAI withdrew Instant Checkout, or does UCP take the merchant journey outright?
- Does a mandate standard ever carry a fee, now that AP2 sits with FIDO?
- Who takes liability when a mandate is honoured wrongly? Nobody currently holds that risk.
last_updated: 2026-07-21
tags:
- concept
mention_count: 1
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-21-agent-identity-kya-landscape
  title: Agent identity / KYA — landscape, demand and value capture, commissioned research pass
  date: '2026-07-21'
  kind: web
neighbors:
- slug: agentic-payments
  name: Agentic Payments
  path: /ai-software/agents/agentic-payments/
  macro: ai-software
- slug: agent-identity-kya
  name: Agent Identity (KYA)
  path: /ai-software/agents/agent-identity-kya/
  macro: ai-software
- slug: x402
  name: x402
  path: /ai-software/agents/x402/
  macro: ai-software
- slug: stablecoins
  name: Stablecoins
  path: /ai-software/agents/stablecoins/
  macro: ai-software
---
The cryptographic record that a human authorised an agent to spend: what, how much, with whom, for how long. Distinct from moving the money, and distinct from proving which agent is calling. Mandates sit above the rail ([x402](/ai-software/agents/x402/), cards) and beside identity ([Agent Identity (KYA)](/ai-software/agents/agent-identity-kya/)).

> Researched 21 July 2026 (, <sup class="ref"><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications" title="x402 protocol state, governance and volume — commissioned research pass" rel="noopener">ref</a></sup>).

## The standards, and who owns them

| Standard | Origin | Status |
|---|---|---|
| **AP2** (Agent Payments Protocol) | Google, Sept 2025 | **Donated to the FIDO Alliance 28 Apr 2026**, v0.2 released alongside, adding "Human Not Present" autonomous payments against pre-authorised mandates. Governance now sits with FIDO |
| **Verifiable Intent** | Google + Mastercard, co-donated Apr 2026 | Tamper-proof log of user-authorised agent actions |
| **ACP** (Agentic Commerce Protocol) | OpenAI + Stripe, Apache 2.0, Sept 2025 | Powers ChatGPT commerce. **OpenAI withdrew Instant Checkout 5 Mar 2026** |
| **UCP** (Universal Commerce Protocol) | Google + Shopify, launched 11 Jan 2026 at NRF | Merchants host JSON profiles at `/.well-known/ucp`. Checkout, Identity Linking and Order Management live at launch; Cart and Product Discovery added 19 Mar 2026 |
| **Visa Trusted Agent Protocol** | Visa, Oct 2025 | Layered on EMV tokenisation. Described by a16z as still in pilot in March 2026 |
| **Mastercard Agent Pay / AP4M** | Mastercard | Agentic Tokens extending MDES. Agent Pay for Machines launched June 2026 |

Two things follow from the table.

**The mandate primitive has been made a public good by the party best placed to charge for it.** Google built AP2 and gave it to FIDO. That removes the most obvious place a startup would have monetised delegated authority.

**Google now runs two overlapping stacks.** AP2 handles payment mandates, UCP handles the merchant journey including Identity Linking. UCP versus ACP is the one genuine head-to-head in agentic commerce, and OpenAI pulling Instant Checkout in March 2026 leaves ACP looking weaker than the specification suggests.

## What a mandate is technically

The W3C Verifiable Credentials pattern applied to spending authority. The user's wallet issues a credential delegating a bounded authority to the agent's decentralised identifier; the agent attaches it to the payment; the merchant or rail verifies the signature chain. AP2 v0.2's "Human Not Present" mode is the interesting extension, since it permits autonomous spend against a mandate signed earlier, which is what makes revocation and expiry load-bearing rather than cosmetic.

## The liability hole

Nobody currently carries the risk when a mandate is honoured wrongly.

Mastercard has closed the gap rather than opened one: agent identity and mandates layer on existing tokenisation, liability follows tokenised-transaction rules, the issuer carries fraud where the token was validly issued, and consumer chargeback rights are intact. [x402](/ai-software/agents/x402/) has no chargebacks, no dispute resolution and no refunds; escrow and refunds are on the roadmap, unbuilt.

That matters for two reasons. It removes the forcing function that would otherwise make somebody buy a mandate-enforcement product by a date. And it leaves **enforcement and audit** (who checks the mandate, logs it, and takes liability when it is wrong) as the one part of this layer that is not commoditised, not owned by a foundation, and plausibly a recurring-revenue enterprise product.

## Why this page is short on companies

`companies_using` is empty on purpose. The mandate layer is currently specification rather than product, and the companies adjacent to it are doing credential issuance and wallets, which is a payments business. See [Agent Identity (KYA)](/ai-software/agents/agent-identity-kya/) for the funded set, and **Agent Identity Value Capture** for why it does not clear the investment gate.
