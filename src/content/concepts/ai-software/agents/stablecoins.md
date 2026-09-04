---
type: concept
slug: stablecoins
canonical_name: Stablecoins
aliases:
- stablecoin
- USDC
- USDT
- PYUSD
- e-money token
- EMT
- payment stablecoin
route: insig
parent_concepts:
- ai-agents
related_concepts:
- stablecoin-clearing
- agentic-payments
- x402
- payment-mandates
descendants:
- agent-identity-kya
- agentic-payments
- payment-mandates
- stablecoin-clearing
- x402
sources:
- '[[2023-09-28-e16-in-conversation-with-shiv-malik]]'
- '[[2026-04-10-state-of-the-future-friday-four-551]]'
- '[[2023-04-04-learnings-from-a-deep-tech-horizon]]'
- '[[2023-07-06-e07-decentralised-ai]]'
- '[[2026-06-13-agentic-payments-value-capture]]'
- '[[2026-06-19-onchain-agent-volume-tracking]]'
- '[[2026-07-21-stablecoin-market-structure]]'
- '[[2026-06-18-aeon-verification]]'
- '[[2026-06-23-mastercard-ap4m-launch]]'
- '[[2026-07-31-4mica-update-verification]]'
- '[[2026-08-06-4mica-base-mainnet-onchain-verification]]'
frontier:
- Does Open USD accumulate real float, or is it a press release with 140 logos and no supply?
- Does the Circle/Coinbase agreement get repriced at the August 2026 decision point, and at what split?
- Do tokenised money-market funds displace non-yielding stablecoins as the default on-chain dollar?
- Does the affiliate yield loophole in the GENIUS Act survive the OCC's rebuttable presumption and the bank lobby?
last_updated: 2026-07-21
tags:
- concept
mention_count: 23
sources_7d: 1
sources_30d: 4
recent_mentions:
- slug: 2026-08-06-4mica-base-mainnet-onchain-verification
  title: 4Mica's Base mainnet contract, verified on-chain
  date: '2026-08-06'
  kind: web
- slug: 2026-07-31-4mica-update-verification
  title: Verifying 4Mica's Q2 investor update against primary sources
  date: '2026-07-31'
  kind: web
- slug: 2026-07-21-stablecoin-market-structure
  title: Stablecoin market structure and value capture — commissioned research pass
  date: '2026-07-21'
  kind: web
- slug: 2026-07-21-x402-protocol-state
  title: x402 protocol state, governance and volume — commissioned research pass
  date: '2026-07-21'
  kind: web
- slug: 2026-06-23-mastercard-ap4m-launch
  title: Mastercard Agent Pay for Machines (AP4M) launch — multi-rail guaranteed settlement, 30+ co-builders (10 Jun 2026)
  date: '2026-06-23'
  kind: web
- slug: 2026-06-19-onchain-agent-volume-tracking
  title: How to track on-chain agent-transaction volume (x402) — sources, method, baseline
  date: '2026-06-19'
  kind: web
- slug: 2026-06-18-aeon-verification
  title: AEON product verification — facilitator + merchant network + atomic settlement, not a netting competitor
  date: '2026-06-18'
  kind: web
- slug: 2026-06-13-agentic-payments-value-capture
  title: Where durable value sits in the agent-payments stack (research synthesis)
  date: '2026-06-13'
  kind: web
neighbors:
- slug: stablecoin-clearing
  name: Stablecoin Clearing & Netting
  path: /ai-software/agents/stablecoin-clearing/
  macro: ai-software
- slug: agentic-payments
  name: Agentic Payments
  path: /ai-software/agents/agentic-payments/
  macro: ai-software
- slug: x402
  name: x402
  path: /ai-software/agents/x402/
  macro: ai-software
- slug: payment-mandates
  name: Payment Mandates
  path: /ai-software/agents/payment-mandates/
  macro: ai-software
---
Dollar tokens redeemable 1:1 against reserves, used as an on-chain settlement instrument. The thing worth understanding about them in mid-2026 is not that they work but that the economics of issuing them are being taken apart, which changes who is worth backing anywhere in the stack.

> Researched 21 July 2026 (). Figures are point-in-time. Where sources disagree the spread is shown rather than averaged.

## Size and structure

Total float is roughly **$290-305B**, and sources disagree by about $30B depending on date and whether yield-bearing tokens are counted. DefiLlama showed ~$297B on 21 Jul 2026, Stablecoin Beat $303.2B on 12 Jul, **down 1.7% over the prior 90 days**.

That last figure matters more than the level. Float growth stalled and mildly reversed in the first half of 2026, which is not what the 2025 consensus expected.

| Token | Issuer | Float | Share |
|---|---|---|---|
| USDT | Tether | $184.0B | ~62% |
| USDC | Circle | $73.2B | ~25% |
| USDS | Sky | $6.67B | 2.2% |
| DAI | Sky/Maker | $4.85B | 1.6% |
| USD1 | World Liberty Financial | $4.20B | 1.4% |
| USDe | Ethena | $4.03B | 1.4% |
| USDG | Paxos consortium | $3.21B | 1.1% |
| PYUSD | PayPal | $2.82B | 0.9% |
| BUIDL | BlackRock | $2.53B | 0.9% |

USDT and USDC together are about 87% of float.

Three corrections to figures carried elsewhere in the KB: USDC is **$73.2B** not ~$77B, USDT is **$184.0B** not ~$186B, and PYUSD is **$2.82B** not ~$4B. PYUSD peaked around $4.2B in March 2026 and has fallen ~31% since. That peak was bought with a 4.5% rewards programme plus YouTube creator payouts and Visa Direct remittance rails, and the supply left when the incentive did. PYUSD is the clearest demonstration available that incentive-bought float does not stick.

## Float is not volume, and the two have decoupled

Headline on-chain volume runs about $35 trillion annualised. **Real payments are ~$390B, about 1%** (McKinsey/Artemis). The rest is DeFi (~$7.8T), exchange flow (~$4.3T), MEV (~$1.9T) and internal transfers. Any market sizing built on the $35T denominator is wrong by two orders of magnitude.

On Visa Onchain Analytics' adjusted series, which strips bots and exchange transfers: $5.8T in FY2024, $10.8T in FY2025, **$1.79T in June 2026 alone**, $8.82T across H1 2026.

Underneath that: **USDC is ~70% of adjusted volume in H1 2026 against USDT's ~25%, on 2.5x less float.** In 2020 the ratio was inverted. USDT is a store-of-value dollar for emerging markets and offshore liquidity, USDC is the transactional rail. Reading market share off float alone gets you the wrong company.

B2B stablecoin payments reached $226B annualised, up 733% year on year, about 60% of real payment activity.

## Where the money is made, and who is taking it

Reserve interest is still essentially the whole business.

Tether posted $1.04B net profit in Q1 2026 on $141B of Treasuries, with equity up ~30% quarter on quarter to $8.23B. That figure is attested by BDO Italia, not audited; KPMG's first full audit only began that quarter. Circle posted $694M of revenue and reserve income, up 20%, with net income of $55.3M and a reserve return rate down to 3.5%. **Circle's other revenue was $42M of $694M, about 6%.** After eleven years and an IPO it remains a levered position on the front end of the US curve.

Distribution is where it goes. Coinbase takes **100% of reserve income on USDC held on its own platform, and splits the residual 50/50 with Circle**. Circle's distribution cost went from $924.5M in 2024 to $1.4B in 2025, about 51% of revenue. Coinbase's Q1 2026 stablecoin revenue was $305M, roughly a fifth of its total, on a record $19B average USDC held, with over a quarter of all USDC sitting on Coinbase.

Three datapoints set the trend and they point one way:

1. Coinbase/Circle: about 50% of residual reserve income to the distributor.
2. Hyperliquid/Coinbase, June 2026: Hyperliquid sunset its own USDH, and Coinbase now treats USDC on Hyperliquid as on-platform, collecting the reserve income and paying **~90% of it back to Hyperliquid**, which holds ~$6B USDC, about 8% of the float.
3. Open USD, 30 June 2026: **partners keep nearly all reserve earnings**, issuer takes a small management fee.

Issuance is being commoditised into a fee-for-service utility and the value is moving to whoever owns the balance. Bridge's USDB already writes this into the product, with interest accruing to the developer rather than the issuer.

**Dated catalyst.** The Circle/Coinbase Collaboration Agreement took effect 18 Aug 2023 on a three-year initial term expiring **August 2026**, auto-renewing for three years absent agreement. Coinbase joined the Open USD consortium in June 2026, one month before that decision point. Read the two together.

## Open USD

Announced 30 June 2026, consortium-governed, operated by Open Standard, with 140+ partners including Visa, Mastercard, Amex, Stripe, BlackRock, BNY, Standard Chartered, Google, Shopify and Coinbase. Founding CEO is Zach Abrams, co-founder of Stripe-owned Bridge. Free minting and redemption with no volume caps, partners keep nearly all reserve earnings, governance by a partner board. CRCL fell more than 17% on the announcement.

**Caveat that travels with this section:** as of 21 July 2026 OUSD does not appear in DefiLlama's top 13 and its circulating float is unverified. The partner count and economics come from secondary coverage. If OUSD is a press release with no supply, the commoditisation argument above is materially weaker than stated. Verify float before leaning on it.

## Regulation

The pattern across every jurisdiction is the same: **the right to issue is being entrenched for licensed institutions while the economics of issuing are taken apart.**

**US, GENIUS Act.** Enacted July 2025, effective the earlier of 18 Jan 2027 or 120 days after final rules. The statutory rulemaking deadline was 18 July 2026 and implementation is incomplete. The Act bans issuers paying holders yield but is silent on affiliates and third parties, which is exactly how Circle pays Coinbase. The OCC's 25 Feb 2026 proposed rule adds a rebuttable presumption against coordinated issuer-affiliate yield arrangements, and 40+ banking associations led by the ABA are lobbying to close it properly. That fight has stalled the broader market-structure bill.

**EU, MiCAR.** Article 143 grandfathering expired **1 July 2026**. USDT, DAI, USDe, FDUSD, PYUSD and TUSD lack authorisation; Tether has said it will not seek it and has been delisted for EEA retail by Binance, Coinbase, Kraken and Crypto.com. A MiCA rewrite reportedly began in July 2026 on the view that the reserve rules handed Circle a European monopoly, though that rests on a single trade-press article.

**UK.** FCA final policy statements 30 June 2026, minimum capital £350,000, applications open 30 Sept 2026, full effect 25 Oct 2027. The Bank of England's June 2026 draft Code for systemic issuers includes a **temporary per-stablecoin issuance cap initially set at £40bn**, an explicit ceiling on any single winner.

**Hong Kong.** First two licences granted 10 April 2026, to HSBC and the Standard Chartered-led Anchorpoint Financial.

## Agent payments, sized honestly

[x402](/ai-software/agents/x402/) settled roughly **$24M over the 30 days to 15 July 2026** on protocol-reported figures. Against one month of adjusted stablecoin volume ($1.79T) that is **0.03%**; against the real-payments pool, about 0.15%. Circle Payments Network runs ~$10B annualised but is oriented to institutional payments rather than agents. Cloudflare's NET Dollar, announced September 2025 for the agentic web, still has no launch date and no circulating float.

Anyone citing agent payments as a driver of current stablecoin economics is citing a projection. See **Agentic Payment Rails** for what that means for the clearing layer, and [x402](/ai-software/agents/x402/) for a serious measurement problem in the underlying number.

## The case against

1. **Distribution eats the margin, and it ratchets.** 50% to Coinbase, ~90% to Hyperliquid, nearly all to OUSD partners. Distributors do not un-learn what the float is worth. Already in the tape: CRCL is down ~75% from its June 2025 IPO peak.
2. **Float has stopped growing.** Anything underwritten to continued float growth has to explain the stall first.
3. **Rate exposure, though not as usually framed.** Fed funds at 3.50-3.75% with the July futures market pricing a hold or a hike on 4.2% CPI, so near-term revenue risk is not from cuts. Structurally, -100bp costs Circle roughly $387M of net income against a ~$15B market cap, with no second revenue line ready.
4. **Tokenised money-market funds are the direct substitute and they pay yield.** Tokenised Treasuries ~$12.9B mid-May 2026, BUIDL $2.9B, Ondo USDY at 4.8% net APY. If you can hold a token paying 4.8% that settles on-chain, holding a non-yielding stablecoin is a donation to the issuer. GENIUS makes this worse by permitting tokenised MMF shares as reserve assets.
5. **Bank deposit tokens plus the bank lobby.** No yield anywhere in the stack, issuance restricted to regulated depositories, is live policy rather than a hypothetical.
6. **Regulatory ceilings are being installed on purpose.** The BoE's £40bn cap is explicit; MiCA already excluded USDT from EU venues and is being rewritten for concentrating the market too far.
7. **Volume is 99% not payments.** Every "stablecoins are eating payments" chart uses the wrong denominator.
8. **Tether's audit is unfinished.** A 62%-share issuer, attested not audited, holding $20B gold and $7B BTC, without MiCA authorisation, is a single point of failure for the asset class.

## Routing

For Insig, which invests fintech equity as principal, issuance is closed (licensed, capital-intensive, margin flowing to distributors) and orchestration is consolidating at $1-2B into Mastercard and Stripe. The seed tier is thin enough that the honest answer is we have no sourcing target here today, and the research pass found no 2026-vintage pre-seed rounds in the vertical from public sources. That absence should be tested against a private data source before it is accepted.