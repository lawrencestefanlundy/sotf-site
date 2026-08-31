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
- Does any buyer emerge with a budget line for agent identity itself, as opposed to agent security operations or key custody, where an existing budget line demonstrably converts to acquisitions?
- Does a card network, regulator or large platform ever open a liability gap that only agent attestation can close, reversing Mastercard's decision to route agent transactions through existing EMV tokenisation liability rules?
- Can any implementation carry the full InterSAGE-style stack (identity cards, DID-bound capability manifests, attenuated delegation, kernel-mediated audit) in production across organisational boundaries, with published overhead and failure data?
- Does the ~20x measurement discrepancy in agentic payment volume resolve upward, which would be the first credible evidence of transaction scale large enough to need paid identity infrastructure?
- Does the Linux Foundation Agent Name Service ship, and does it end the case for a commercial registry?
- Does eIDAS 2.0's late-2027 private-sector acceptance obligation extend from human wallets to agent delegation?
- Is the real gap Know-Your-Merchant (underwriting agent-run businesses with no legal entity) rather than Know-Your-Agent?
- Does anyone build hardware-rooted TEE attestation for agents, the one primitive no foundation has claimed?
last_updated: '2026-08-31'
tags:
- concept
mention_count: 8
scorecard:
  viability: 3
  drivers: 2
  novelty: 3
  diffusion: 3
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Overrated
scorecard_status: draft
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
**Agent identity, or "know your agent", is the layer of cryptographic identifiers, credentials and audit trails that lets one autonomous agent prove who it is, what it is allowed to do and on whose behalf it acts; the primitives are real and arriving fast, but almost every monetisable piece has already been donated to a standards body, so the layer is likely to be ubiquitous and unownable.**

## Summary

Agent-to-agent protocols such as MCP, A2A, ANP and AG-UI define how LLM-powered agents exchange messages, discover peers and delegate work. They largely do not define how an agent proves its identity, its authorisation, its advertised capabilities, or who is accountable once a task has been delegated onward. Agent identity is the attempt to fill that gap. The reference architecture in the literature is a four-layer stack: persistent identity, discovery, trust negotiation and accountability, with primitives that include "Agent Identity Cards" binding developer, code package, operator and deployment context; capability-aware discovery using DID-bound verifiable-credential manifests; monotonic capability attenuation on delegation combined with two-tier access control; and kernel-mediated cryptographic audit trails that bind usage, delegation and execution traces to an identity without needing a consensus ledger.

The hard technical question underneath is what the identity is actually bound *to*. Binding a key to an operator or a wrapper means trusting that operator. One line of work pushes the trust root down to cryptography by making an agent's neural-network weights a deterministic function of its private key, committing that binding in zero knowledge at genesis, re-checking it at every state transition, and signing the result into an unforkable on-chain history; a deployed proof of concept on Solana devnet completed a 2.36-day run with two host-side resumptions and no rejected transition, at bounded per-transition verification cost, while explicitly leaving liveness, key custody, oracle trust and the software stack outside the trust boundary. That is the shape of the research frontier: strong binding of key to behaviour, with most operational trust still external.

The parameters that decide the outcome are commercial rather than cryptographic. A commissioned research pass found that "KYA" collapses six distinct problems (agent authentication, bot-versus-agent distinction, delegated authority and mandates, agent-to-merchant trust, credential issuance, and reputation or attestation), of which only the last is genuinely unclaimed, and it has essentially no paying demand. Every monetisable primitive in the layer was donated to a standards body inside twelve months: Google donated AP2 to the FIDO Alliance on 28 April 2026 with Mastercard co-donating "Verifiable Intent", Cloudflare put Web Bot Auth into the IETF using RFC 9421 signatures and Ed25519, Coinbase gave x402 to the Linux Foundation, the Linux Foundation announced an Agent Name Service as free neutral trust infrastructure, and ZeroID was open-sourced in April 2026. A dedicated search for a regulatory, liability or network mandate with a date found none; Mastercard has closed the liability gap by layering agent identity onto existing EMV tokenisation, so liability follows tokenised-transaction rules and the issuer carries fraud.

One terminology note: the same acronym is used in the security literature for "Know Your Agent", a framework for reconnaissance-driven black-box pentesting of agents, which builds target profiles of an agent and uses them to craft stronger indirect prompt-injection attacks. That is an attacker-side discipline, not an identity layer, but it is evidence that agent metadata and profiles are adversarially useful in both directions.

## Viability (3/5)

The building blocks are conventional and shipped: HTTP message signatures under RFC 9421 with Ed25519 keys are already in the IETF via Web Bot Auth, DIDs and verifiable credentials are in use, and neutral naming infrastructure has been announced by the Linux Foundation. The full trust-native stack, however, exists in the literature as a design: InterSAGE is presented as a protocol suite complementing MCP, A2A, ANP and AG-UI, with the sources describing its architecture and primitives rather than production deployments at scale.

The strongest end of the binding problem is demonstrably immature. The key-to-weights binding proof of concept ran for 2.36 days on a devnet, needed two host-side resumptions, and its authors are explicit that liveness, key custody, oracle trust and the underlying software stack remain outside the cryptographic guarantee. That is honest engineering, but it means "the agent is provably this agent" is not yet a property you can buy. A 3 reflects working components, credible architecture, and no demonstrated end-to-end system carrying real authority.

**TLDR: The primitives work and some are already in standards bodies, but the full trust stack is research-stage and leaves most operational trust external.**

## Drivers (2/5)

Supply side: the layer is being pushed out by the largest adjacent players at zero price. AP2 went to FIDO on 28 April 2026, Web Bot Auth to the IETF, x402 to the Linux Foundation, and the x402 Foundation reached operational launch with 40 members on 14 July 2026, including Visa, Mastercard, Amex, Stripe, Adyen, Fiserv, Google, AWS, Cloudflare, Circle, Shopify and Ripple, with zero protocol fees and no native token <sup class="ref"><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications" title="x402 protocol state, governance and volume — commissioned research pass" rel="noopener">ref</a></sup>. When the richest players in adjacent layers all decide the layer beneath them should be free, pricing power is capped near zero.

Demand side: a specific search for a regulatory, liability or network mandate with a date found none, and Mastercard has layered agent identity onto existing EMV tokenisation so that liability follows tokenised-transaction rules with the issuer carrying fraud. The nearest thing to a real pull is security pressure: AI-enabled attacks rose 89% year on year, 16% of breaches now involve attacker-used AI, and autonomous agents are involved in roughly one in eight AI breaches, with AI-driven attacks costing $4.49M on average <sup class="ref"><a href="https://www.kiteworks.com/cybersecurity-risk-management/ai-cybersecurity-2026-trends-report/" title="AI-enabled attack frequency and autonomous-SOC economics, 2026" rel="noopener">ref</a></sup>. That is a driver for agent security spend generally, not evidence of budget lines for agent identity specifically. Meanwhile agentic payment volume, the obvious demand proxy, fell from a $5.15M peak in November 2025 by roughly 77% to $1.19M by May 2026, with a ~20x unresolved measurement discrepancy against x402.org's own panel reading 75.41M transactions and $24.24M over 30 days <sup class="ref"><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications" title="x402 protocol state, governance and volume — commissioned research pass" rel="noopener">ref</a></sup>.

**TLDR: Supply is abundant and free; demand has no dated forcing function and the main liability gap has been closed rather than opened.**

## Novelty (3/5)

The claimed advance is relative to the agent communication protocols themselves: they increasingly specify message exchange but not identity proof, authorisation, capability attestation or post-delegation accountability, and InterSAGE positions itself as the missing security substrate alongside rather than instead of them. Two elements look genuinely new in kind rather than degree: binding developer, code package, operator and deployment context into a single identity card, and monotonic capability attenuation so that delegated authority can only narrow as a task is passed on. Kernel-mediated audit trails that avoid a consensus ledger are a meaningful engineering choice against the blockchain-anchored alternative.

Against that, most of the stack is inherited: DIDs, verifiable credentials, HTTP message signatures under RFC 9421, Ed25519. The one strongly novel research result, making weights a deterministic function of the private key and committing that binding in zero knowledge, shifts the trust root from hardware, operator or wrapper trust to cryptographic assumptions, which is a real conceptual move, but it is demonstrated at devnet scale over 2.36 days. The sources do not quantify how much better any of this is than the status quo in security or fraud terms, so the score stops at credible-and-contested.

**TLDR: Genuinely fills a gap the message protocols leave open, but does so by recomposing existing human-identity plumbing.**

## Diffusion (3/5)

Distribution is the strong part of the story. Governance is settled and institutional at the payments-adjacent layer, with premier members spanning card networks, PSPs and hyperscalers <sup class="ref"><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications" title="x402 protocol state, governance and volume — commissioned research pass" rel="noopener">ref</a></sup>, and the Linux Foundation's announced Agent Name Service provides free neutral naming. Free, standards-body infrastructure with that membership list tends to diffuse. Fragmentation is the practical barrier: identity primitives are landing in at least three separate homes (FIDO, IETF, Linux Foundation) plus open-source releases such as ZeroID in April 2026, and the security substrate work explicitly has to interoperate with four different communication protocols.

The cautionary analogue is the human identity layer, which has run this experiment further. The same commoditisation pattern is more complete there: Google open-sourced its ZKP libraries under Apache 2.0, the EU shipped an open-source age-verification blueprint behind the app announced 15 April 2026, and eIDAS 2.0 encourages ZKPs in the wallet so privacy is a regulatory expectation rather than a differentiator <sup class="ref"><a href="https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/" title="Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages " rel="noopener">ref</a></sup>. Adoption of the primitive was not the problem; monetisation was. The best-funded proof-of-personhood player reached 18M+ Orb-verified humans, 475M+ proofs and a $2.5bn valuation, and was still cutting staff from a ~500-person team on 8 June 2026 because revenue had not kept pace, having only just introduced per-verification application fees <sup class="ref"><a href="https://www.biometricupdate.com/202606/world-shifts-from-crypto-identity-experiment-to-enterprise-proof-of-humanity" title="World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags" rel="noopener">ref</a></sup>.

**TLDR: The standards will probably diffuse widely and quickly precisely because they are free; products built on them face near-zero pricing power.**

## Impact (3/5)

Functionally the layer is close to necessary. Without identity, authorisation, capability attestation and accountability after delegation, an internet of agents crossing organisational boundaries has no basis for trust, and agents accumulating authority and economic stakes on public infrastructure make the individuation question an engineering problem rather than a philosophical one. The security case is adjacent and real: reconnaissance-driven pentesting shows that profiling an agent materially strengthens indirect prompt-injection attacks against it, including against a real-world coding agent, and autonomous agents already feature in roughly one in eight AI-involved breaches <sup class="ref"><a href="https://www.kiteworks.com/cybersecurity-risk-management/ai-cybersecurity-2026-trends-report/" title="AI-enabled attack frequency and autonomous-SOC economics, 2026" rel="noopener">ref</a></sup>.

Economic impact captured *within* the layer looks small. "KYA" collapses six problems, five of which are already claimed by incumbents or standards bodies, and the one unclaimed problem, reputation and attestation, has essentially no paying demand. The protocol layer beneath it charges zero fees and has no token, so there is nothing to own there either <sup class="ref"><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications" title="x402 protocol state, governance and volume — commissioned research pass" rel="noopener">ref</a></sup>. A 3 is the honest reading: high systemic importance, low appropriable value on current evidence.

**TLDR: Load-bearing for cross-organisational agent commerce if it works, but the sources suggest the value lands in adjacent layers, not here.**

## Timing Now (0-2yr)

The standards timeline is already in motion: AP2 to FIDO on 28 April 2026, Web Bot Auth in the IETF, x402 contributed to the Linux Foundation on 2 April 2026 with a 40-member operational launch on 14 July 2026, an announced Agent Name Service, and ZeroID open-sourced in April 2026 <sup class="ref"><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications" title="x402 protocol state, governance and volume — commissioned research pass" rel="noopener">ref</a></sup>. Anyone building agents that cross organisational boundaries will be making identity decisions inside the next two years, whether or not they buy anything.

The revenue timing is a different question and the sources do not support a band for it. No dated regulatory, liability or network mandate exists, and the closest comparable category took three years past launch to start charging at all <sup class="ref"><a href="https://www.biometricupdate.com/202606/world-shifts-from-crypto-identity-experiment-to-enterprise-proof-of-humanity" title="World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags" rel="noopener">ref</a></sup>. Treat "Now" as applying to the technology and the standards, not to a market.

**TLDR: The substrate is being standardised and shipped right now; the paying market is not visible on any dated evidence.**

## Overrated or underrated? Overrated

As an engineering requirement, agent identity is real and the research is respectable: the gap in existing agent protocols is precisely identified, the four-layer architecture is coherent, and the key-to-weights binding work is a genuine attempt to move the trust root somewhere defensible. As a standalone technology category or investment thesis it is overrated, and the commissioned pass that tested exactly that question concluded it does not clear the bar: the term bundles six unrelated problems, five are claimed, the sixth has no paying demand, every monetisable primitive was given away inside twelve months, and no forcing function with a date exists.

The structural argument is the one to hold onto. Google, Cloudflare and Coinbase each commoditised this layer to protect a profit pool above or beside it, and the identical mechanism has already played out one level down at the human identity layer, where the platforms and the regulator both gave the primitives away <sup class="ref"><a href="https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/" title="Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages " rel="noopener">ref</a></sup>. The result there was wide adoption and unconvincing economics, illustrated by a category leader with 475M+ proofs issued doing layoffs <sup class="ref"><a href="https://www.biometricupdate.com/202606/world-shifts-from-crypto-identity-experiment-to-enterprise-proof-of-humanity" title="World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags" rel="noopener">ref</a></sup>. Expect agent identity to become universal plumbing that almost nobody pays for directly. Where money is plausible, on current sources, is adjacent: agent security operations, where AI-enabled attacks rose 89% year on year and 85% of security professionals prefer new SOC capability delivered as a managed service <sup class="ref"><a href="https://www.kiteworks.com/cybersecurity-risk-management/ai-cybersecurity-2026-trends-report/" title="AI-enabled attack frequency and autonomous-SOC economics, 2026" rel="noopener">ref</a></sup>.

## Prediction

By 31 December 2027, no dated regulatory, liability or network mandate requiring cryptographic agent identity will be in force, and the core primitives (AP2 at FIDO, Web Bot Auth at the IETF, x402 and the Agent Name Service at the Linux Foundation) will still be available at zero licence cost.

## Evidence base

- Existing agent protocols specify message exchange but not identity, authorisation, capability attestation or post-delegation accountability; InterSAGE proposes a four-layer trust substrate with agent identity cards, DID-bound verifiable-credential discovery, monotonic capability attenuation and kernel-mediated audit trails, published 14 Aug 2026 
- An agent whose neural-network weights are a deterministic function of its private key, committed in zero knowledge at genesis and re-checked each state transition, completed a 2.36-day Solana devnet run with two host-side resumptions and no rejected transition, with liveness, key custody and oracle trust left external, published 5 Aug 2026 
- Every monetisable primitive in the layer was donated to a standards body within twelve months: AP2 to FIDO on 28 Apr 2026 with Mastercard co-donating Verifiable Intent, Web Bot Auth to the IETF, x402 to the Linux Foundation, an announced Agent Name Service, and ZeroID open-sourced in Apr 2026; a search for a dated regulatory or liability forcing function found none 
- The x402 Foundation reached operational launch with 40 members on 14 Jul 2026 including Visa, Mastercard, Stripe, Google, AWS and Cloudflare, with zero protocol fees and no native token, while measured volume fell from a $5.15M peak in Nov 2025 to $1.19M by May 2026 <sup class="ref"><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications" title="x402 protocol state, governance and volume — commissioned research pass" rel="noopener">ref</a></sup>
- The same commoditisation pattern is further advanced at the human identity layer: Google open-sourced its ZKP libraries under Apache 2.0, the EU shipped an open-source age-verification blueprint behind the app announced 15 Apr 2026, and eIDAS 2.0 encourages ZKPs in the wallet <sup class="ref"><a href="https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/" title="Google open-sources its ZKP libraries, the EU ships an open-source age-verification blueprint, and eIDAS 2.0 encourages " rel="noopener">ref</a></sup>
- The best-funded identity-verification comparable, with 18M+ verified humans, 475M+ proofs and a $2.5bn valuation, restructured a ~500-person team on 8 Jun 2026 because revenue lagged costs, and only then introduced per-verification application fees <sup class="ref"><a href="https://www.biometricupdate.com/202606/world-shifts-from-crypto-identity-experiment-to-enterprise-proof-of-humanity" title="World (Tools for Humanity) pivots to enterprise fees and cuts staff as revenue lags" rel="noopener">ref</a></sup>
- AI-enabled attacks rose 89% year on year, 16% of breaches involve attacker-used AI, autonomous agents feature in roughly one in eight AI breaches, and AI-driven attacks cost $4.49M on average <sup class="ref"><a href="https://www.kiteworks.com/cybersecurity-risk-management/ai-cybersecurity-2026-trends-report/" title="AI-enabled attack frequency and autonomous-SOC economics, 2026" rel="noopener">ref</a></sup>

## Open questions

- Does any buyer emerge with a budget line for agent identity itself, as opposed to agent security operations or key custody, where an existing budget line demonstrably converts to acquisitions?
- Does a card network, regulator or large platform ever open a liability gap that only agent attestation can close, reversing Mastercard's decision to route agent transactions through existing EMV tokenisation liability rules?
- Can any implementation carry the full InterSAGE-style stack (identity cards, DID-bound capability manifests, attenuated delegation, kernel-mediated audit) in production across organisational boundaries, with published overhead and failure data?
- Does the ~20x measurement discrepancy in agentic payment volume resolve upward, which would be the first credible evidence of transaction scale large enough to need paid identity infrastructure?

---
*Assessment drafted 2026-08-31 from up to 10 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
