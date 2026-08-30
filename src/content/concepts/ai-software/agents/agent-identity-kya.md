---
type: concept
slug: agent-identity-kya
canonical_name: Agent Identity (KYA)
aliases:
- KYA
- know your agent
- agent identity
- agent authentication
- agent authorisation
- agent attestation
route: insig
parent_concepts:
- agentic-payments
related_concepts:
- agentic-payments
- payment-mandates
- x402
- stablecoin-clearing
sources:
- '[[2026-07-21-agent-identity-kya-landscape]]'
frontier:
- Does the Linux Foundation Agent Name Service ship, and does it end the case for a commercial registry?
- Does eIDAS 2.0's late-2027 private-sector acceptance obligation extend from human wallets to agent delegation?
- Is the real gap Know-Your-Merchant (underwriting agent-run businesses with no legal entity) rather than Know-Your-Agent?
- Does anyone build hardware-rooted TEE attestation for agents, the one primitive no foundation has claimed?
last_updated: 2026-07-21
tags:
- concept
mention_count: 8
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2026-07-26-ai-breach-frequency-autonomous-soc
  title: AI-enabled attack frequency and autonomous-SOC economics, 2026
  date: '2026-07-26'
  kind: web
- slug: 2026-07-21-x402-protocol-state
  title: x402 protocol state, governance and volume — commissioned research pass
  date: '2026-07-21'
  kind: web
- slug: 2026-07-21-applied-crypto-spinout-sourcing-map
  title: Applied-cryptography academic spinouts in financial infrastructure — sourcing map
  date: '2026-07-21'
  kind: web
- slug: 2026-07-21-agent-identity-kya-landscape
  title: Agent identity / KYA — landscape, demand and value capture, commissioned research pass
  date: '2026-07-21'
  kind: web
- slug: 2026-07-28-world-enterprise-pivot-and-layoffs
  title: World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags
  date: '2026-06-08'
  kind: web
- slug: 2026-07-28-zk-identity-primitives-commoditised
  title: Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages ZKP in the wallet
  date: '2026-04-15'
  kind: web
- slug: 2026-07-28-proof-of-personhood-competitive-landscape
  title: Proof-of-personhood competitive landscape — Humanity Protocol pivots out, Billions goes non-biometric
  date: '2026-02-01'
  kind: web
neighbors:
- slug: agentic-payments
  name: Agentic Payments
  path: /ai-software/agents/agentic-payments/
  macro: ai-software
- slug: payment-mandates
  name: Payment Mandates
  path: /ai-software/agents/payment-mandates/
  macro: ai-software
- slug: x402
  name: x402
  path: /ai-software/agents/x402/
  macro: ai-software
- slug: stablecoin-clearing
  name: Stablecoin Clearing & Netting
  path: /ai-software/agents/stablecoin-clearing/
  macro: ai-software
---
Authenticating and authorising an AI agent transacting on someone's behalf. The term is used as though it names one thing. It names at least six, and separating them is the whole analysis.

> Researched 21 July 2026 (agent identity kya landscape). The gate verdict this produced sits on the idea page **Agent Identity Value Capture**, which is a theme, not a thesis.

## Six problems wearing one label

| Problem | What it answers | Where it is solved today |
|---|---|---|
| Agent authentication | Is this request from the agent it claims to be? | HTTP Message Signatures (RFC 9421), Ed25519, `Signature-Agent` header. Cloudflare Web Bot Auth |
| Bot vs agent | Is this a scraper, or a human's delegate? | CDN and bot-mitigation layer: Cloudflare, Akamai, DataDome, HUMAN, Kasada |
| Delegated authority | Did a human authorise *this* purchase, at *this* limit? | Google AP2 verifiable mandates, Mastercard Verifiable Intent. See [Payment Mandates](/ai-software/agents/payment-mandates/) |
| Agent-to-merchant trust | Should this merchant serve and charge this agent? | Visa Trusted Agent Protocol, UCP `/.well-known/ucp`, ACP |
| Credential issuance | Give the agent a spendable instrument | Network tokens, virtual cards (Lithic, Marqeta), agent wallets (Crossmint, Skyfire) |
| Reputation and attestation | Has this agent behaved before? Is it running the code it claims? | Largely unbuilt. TEE attestation and trust-scoring are the frontier |

Authentication and bot-detection are the same business, and CDN incumbents own it. Delegated authority is a specification rather than a product. Merchant trust is network-owned. Credential issuance is a payments business wearing identity clothing, which is what Skyfire, Nekuda, Crossmint and Catena actually are. **Reputation and attestation is the only unclaimed slot, and it has close to no paying demand.**

## The structural fact: every monetisable primitive was given away

Inside twelve months:

- Google donated **AP2 to the FIDO Alliance on 28 April 2026**, with Mastercard co-donating a Verifiable Intent standard.
- Cloudflare put **Web Bot Auth** into the IETF as individual drafts, backed by Amazon, Akamai and OpenAI, and folded it into Verified Bots.
- Coinbase contributed **x402 to the Linux Foundation**, whose 40-member foundation launched 14 July 2026.
- The Linux Foundation has **announced an Agent Name Service**, free neutral trust infrastructure for agents.
- **ZeroID** was open-sourced by Highflame in April 2026: agent identity server, verifiable credentials, delegated-authority enforcement.

Google, Cloudflare and Coinbase each concluded that commoditising this layer protects their actual profit pools in ads and cloud, edge security, and exchange and stablecoin economics. When the three richest players in adjacent layers all decide the layer beneath them should be free, an independent vendor's pricing power is capped near zero.

## Identity is bundled at the point of enforcement

An identity assertion is worthless unless something checks it. The checkers are the CDN, the card network, the merchant platform and the enterprise identity provider. All four ship agent identity as a free feature defending an existing paid product. Skyfire's flagship 2026 announcement is a partnership in which **F5 does the enforcement**, which is the layer conceding where the value sits.

## What the funded companies actually are

| Company | Raised | Notes |
|---|---|---|
| Skyfire | $9.5M, 2024 | KYA protocol on standard JWTs, OAuth2/JWKS-compatible. F5 partnership Mar 2026 |
| Catena Labs | $18M seed, a16z crypto | AI-native regulated financial institution, founded by Circle co-founder Sean Neville |
| Basis Theory | $33M Series B, Oct 2025 | Tokenisation and vaulting; convenes the Agentic Commerce Consortium |
| Crossmint | $23.6M, Mar 2025 | Agent wallets, cards, payouts |
| Payman | $13.8M | Agent-initiated payments and transfers |
| Nekuda | $5M seed, May 2025 | Madrona, Amex Ventures, Visa Ventures |

Skyfire's KYA is JSON Web Tokens over existing OAuth2 plumbing. That is sound engineering and correct pragmatism, and it is not applied cryptography, so there is no research moat. Across the funded set the founder pattern is ex-security operators and ex-Israeli-unit engineers rather than academic spinouts, and the pre-seed geography skews Australia, London and San Francisco rather than the crypto-research corridor. For a deep-tech investor that should give pause: this layer is not behaving like a deep-tech problem.

## Real cryptography vs plumbing

Genuinely cryptographic and shipping: Cloudflare Web Bot Auth (RFC 9421, Ed25519, JWKS, standards-grade, publicly reviewed, free); Google AP2 verifiable mandates and Verifiable Intent, on the W3C Verifiable Credentials pattern, now a public good under FIDO; ZeroID. The architecturally correct design is the user's wallet issuing a credential delegating spend authority to the agent's DID, which is where the academic literature converges.

**TEE attestation, using the attestation document as the agent's credential bound to runtime characteristics, is the genuinely defensible primitive and the least built.** No company in the funded set is clearly shipping hardware-rooted agent attestation in production. That could mean nobody is, or that the search missed them.

Plumbing dressed as identity: most of the rest, plus the card networks' agent identity, which is EMV tokenisation from 2014 with an agent field added.

## Demand

There is essentially none, and the negative datapoints are strong.

**OpenAI killed Instant Checkout on 5 March 2026**, roughly five months after launch, with about a dozen Shopify merchants live and Walmart measuring in-ChatGPT checkout converting around three times worse than click-through to walmart.com. The best-distributed agentic checkout in the world was withdrawn, and identity was not the bottleneck. QED's read is that the roadblock is consumer trust rather than payments.

Bottom-up, x402 at ~$24M over 30 days annualises to ~$288M of GMV, and at a generous 1% identity take that is **~$3M a year of addressable revenue across the entire crypto-native agent-payments world**, against $120M+ of disclosed venture funding already sitting in the layer. No card network has published agentic volume. No credible independent estimate of agent-identity revenue exists, and that absence is itself the finding.

Every machine-identity market figure available is report-mill and they disagree by 5.5x for the same year, from $3.8B to $21.4B. None are usable as a TAM.

## The counter-argument worth taking seriously

Noah Levine at a16z crypto (4 March 2026) argues agents need no new identity mechanism at all: they behave like devices, receive payment tokens the way Apple Pay does, and require no separate KYC. Cards keep agentic commerce because they supply purchase protection, fraud detection and rewards. The gap he names is underwriting *merchants* with no legal entity or track record, because a processor that says yes to a merchant takes on that merchant's risk.

That relocates the problem from Know-Your-Agent to Know-Your-Merchant, which is a different and arguably better company.

The other place the bear case is weak: the **enforcement and audit** function, who checks the mandate, logs it, and carries liability when it is wrong, is not commoditised, not owned by a foundation, and is a recurring-revenue enterprise product.

## Pre-seed names found

Astrasync AI (seed undisclosed, Jan 2026, Australia, trust scoring, which is the unclaimed slot); Prefactor ($1M pre-seed, Jun 2026, Melbourne); Agentic Fabriq ($0.5M pre-seed, Dec 2025, San Francisco); Riptides ($3.3M pre-seed); Archestra ($10M seed, Jun 2026, London); Keycard ($30M Series A, Oct 2025).

Meanwhile the exits are already resolving as feature-tucks: Snowflake bought Natoma, Okta bought Axiom, Silverfort bought Fabrix at one year old, Palo Alto bid for CyberArk.
