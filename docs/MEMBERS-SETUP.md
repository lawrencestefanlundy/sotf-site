# Members' edition — what it is, how to set it up, how it runs

The paywall for the deeper content. Public pages stay exactly as they are: prerendered, free, indexed. Paid newsletter subscribers sign in with the email they use on Substack and get the members' edition: the reasoning and the calls behind every scored technology, a feed of what changed, a screener, reading lists and a weekly digest.

The product is **State of the Future**, on its own. Nothing in either edition names the fund; the publisher strips it twice (`strip_cloudberry_content`, then `scrub_fund_mentions`) and the smoke test checks for it.

## The pieces

| Piece | Service | Why this one |
|---|---|---|
| Hosting | [Cloudflare Workers](https://developers.cloudflare.com/workers/) — Cloudflare's serverless platform; static assets are served from its edge, code runs only on the routes that need it. | Public pages are still static files on a CDN; only `/members`, `/signin`, `/auth`, `/api` run code. The free tier covers this traffic. |
| Members' content | [Cloudflare R2](https://developers.cloudflare.com/r2/) — S3-compatible object storage with no egress fees. | A private bucket the Worker reads per request. The content never enters this public repo or the build; the nightly sync *is* the members' deploy. |
| Sign-in tokens | [Cloudflare KV](https://developers.cloudflare.com/kv/) — a key-value store with expiring keys. | 15-minute one-time tokens, a per-email rate limit, digest opt-outs. Nothing else is stored. |
| Who is a subscriber | [Stripe](https://dashboard.stripe.com/) — your existing account; Substack bills through it. | Every paid subscriber is already a Customer with a Subscription there. The site asks Stripe directly with a read-only key: one list, one bill, nothing to migrate. |
| Email | [Resend](https://resend.com/) — a transactional email API with a 3,000/month free tier. | Sends the sign-in link and the Monday digest from `members@stateofthefuture.io`. |
| Billing, essays | [Substack](https://stateofthefuture.substack.com/) — unchanged. | Readers subscribe and cancel there; access here follows within a day. |

Session = HMAC-signed cookie (30 days), re-checked against Stripe once a day so a lapsed subscriber loses access without anyone doing anything.

## What members get that the public page does not

`publish_kb.py` emits two editions of every concept from the same note:

- **Public** — Summary, Physics/mechanism, Competitive landscape, Evidence base, Frontier questions, the score dots and the verdict label.
- **Members** — all of that plus the sections matched by `MEMBER_SECTIONS`: `Prediction`, the per-dimension rationale (`Viability (3/5)`, `Impact (4/5)` …), `Overrated or underrated?`, `Timing`, `What would change my mind`, bull/bear cases.

Stripped from **both**: fund framing, Attio-tracked companies (pipeline), private source kinds (granola/memo/email/note), deal fields, Dataview blocks. To move a section across the line, edit the `MEMBER_SECTIONS` regex; that is the whole rule.

Beyond the note, each members' concept page carries:

- **Score history** — every change to its scores and calls, from the ledger.
- **Who is building it** — companies tracked against the concept that have no Attio id (public companies, well-known startups), each linked to its site with a one-line blurb.
- **Essays on this** — the newsletter pieces that discuss it, linked.
- **Reading list** — every public source behind it, newest first, each linked with one sentence on what it argues.

And four members' tools:

- [`/members/changes/`](https://stateofthefuture.io/members/changes/) — every score, call, timing and status change in the last 90 days, plus the concepts cited most this week.
- [`/members/screener/`](https://stateofthefuture.io/members/screener/) — all scored technologies in one sortable, filterable table.
- [`/members/coverage/`](https://stateofthefuture.io/members/coverage/) — scored / draft / unscored / stub per macro and meso, and the scoring queue (most-cited unscored concepts).
- [`/members/digest/`](https://stateofthefuture.io/members/digest/) — this week's email as it will be sent.

### The ledger

`publish_kb.py` keeps `~/kb/scripts/sotf_members_ledger.json` (override with `SOTF_MEMBERS_LEDGER`): last run's scorecards plus every change since. The first run only takes a snapshot, so the feed starts empty and fills from the next night. It lives in the KB because the KB is backed up and this repo is public. Lose it and history restarts; nothing else breaks.

### The digest

Mondays, after the R2 sync, `nightly_publish.sh` POSTs to `/api/digest/send` with `DIGEST_SECRET`. The Worker builds the week's digest from `changes.json`, lists recipients from Stripe (active, trialing, past-due subscriptions) plus the allowlist, skips anyone who opted out, and sends one email each through Resend with a one-click opt-out link. A week with nothing changed sends nothing. `?dry=1` returns the recipient count without sending.

## One-time setup (about an hour)

### 1. Stripe
1. Open [Customers](https://dashboard.stripe.com/customers) — the list of everyone Stripe has billed for you. You should see your Substack subscribers. If you don't, stop and tell me: we switch to a Substack-export allowlist instead.
2. Open [API keys](https://dashboard.stripe.com/apikeys) and **Create restricted key** — a key limited to the permissions you tick. Name it `sotf-site members`, set **Customers: Read** and **Subscriptions: Read**, everything else None. Copy the `rk_live_…` key.

### 2. Resend
1. Open [Domains](https://resend.com/domains) and add `stateofthefuture.io` — it shows the DNS records that let Resend send as you. Add them at your DNS provider (after step 8 that is Cloudflare).
2. Open [API keys](https://resend.com/api-keys) and create one with *Sending access* only. Copy `re_…`.

### 3. Cloudflare
1. [Sign up](https://dash.cloudflare.com/sign-up) if you have no account — the free plan is enough. The **Account ID** (right-hand column of the Workers & Pages overview) goes in `wrangler.jsonc` as `account_id`; it is not sensitive.
2. Open [R2](https://dash.cloudflare.com/?to=/:account/r2) and **Create bucket** `sotf-members`, location automatic. Then **Manage API tokens → Create**: *Object Read & Write*, scoped to this bucket. Copy the Access Key ID and Secret — these go on your Mac (step 6), not GitHub.
3. Open [Account API Tokens](https://dash.cloudflare.com/?to=/:account/api-tokens) — tokens that let tools act on your account — and **Create Token → Edit Cloudflare Workers** template. Add *Workers KV Storage: Edit* and *Workers R2 Storage: Edit* if missing. Copy it.

### 4. GitHub
Open the repo's [Actions secrets and variables](https://github.com/lawrencestefanlundy/sotf-site/settings/secrets/actions) — where workflows read credentials.
- Secret: `CLOUDFLARE_API_TOKEN`.
- Variable: `CLOUDFLARE_DEPLOY` = `true`.

Then open [Actions → Deploy to Cloudflare](https://github.com/lawrencestefanlundy/sotf-site/actions/workflows/deploy-cloudflare.yml) and **Run workflow**. The first run provisions the KV namespaces and deploys the Worker at `sotf-site.<your-subdomain>.workers.dev`. If it fails on a KV namespace without an `id`, run `npx wrangler kv namespace create AUTH_KV` locally and paste the id into `wrangler.jsonc`.

### 5. Secrets on the Worker
From the repo, after `npx wrangler login`:
```sh
openssl rand -hex 32 | npx wrangler secret put SESSION_SECRET
openssl rand -hex 32 | npx wrangler secret put DIGEST_SECRET
npx wrangler secret put STRIPE_SECRET_KEY      # rk_live_… from step 1
npx wrangler secret put RESEND_API_KEY         # re_… from step 2
npx wrangler secret put MEMBER_ALLOWLIST       # your email, comped readers; comma-separated
```

### 6. Your Mac — the nightly sync and the Monday digest
Add to `~/.config/kb/env` (sourced by `nightly_publish.sh`):
```sh
export R2_ACCOUNT_ID=…
export R2_ACCESS_KEY_ID=…
export R2_SECRET_ACCESS_KEY=…
export DIGEST_SECRET=…        # the same value as the Worker secret
export SITE_URL=https://stateofthefuture.io
```
and `pip install boto3` in `~/kb/scripts/.venv`. Then once by hand:
```sh
python3 scripts/publish_kb.py           # writes .members-out/ and starts the ledger
python3 scripts/upload_members.py --dry-run
python3 scripts/upload_members.py
```

### 7. Test on workers.dev before touching DNS
- `/members/` → landing page. `/members/screener/` → redirected to sign-in.
- Sign in with your own (allowlisted) email → link arrives → members' home with the four tools.
- Open a scored concept's members' edition: Prediction and rationale present; search the page for the fund's name — it must not appear.
- Sign in with a paying subscriber's email in a private window → passes the Stripe check (the link goes to *their* inbox, so stop at the "sent" page).
- A random email → "No active paid subscription".
- `curl -X POST -H "Authorization: Bearer $DIGEST_SECRET" "https://…workers.dev/api/digest/send?dry=1"` → recipient count.

### 8. Cut over
1. In [Workers & Pages](https://dash.cloudflare.com/?to=/:account/workers-and-pages) open `sotf-site` → **Settings → Domains & Routes → Add → Custom domain** `stateofthefuture.io` (and `www`). If the domain's DNS isn't on Cloudflare yet it walks you through moving nameservers; Resend's records come along.
2. Once `https://stateofthefuture.io/members/` serves from the Worker: delete `.github/workflows/deploy.yml` and `public/CNAME`, and turn GitHub Pages off in the repo settings.

## Day to day

- **Nothing.** Nightly publish updates both editions and the ledger; Mondays it sends the digest. `logs/nightly-publish.log` says `synced N members' concepts` and `ledger: N change events`.
- A new paid subscriber on Substack can sign in immediately. A lapsed one is locked out within 24 h.
- Comp someone: `npx wrangler secret put MEMBER_ALLOWLIST` with the new list.
- Local dev: `cp .dev.vars.example .dev.vars`, fill it in, `npm run dev:members`. KV and R2 are emulated locally and start empty.

## Style guide

The brand guide (`~/reference/system/design/BRAND.md`, `DESIGN.md`) is not in this repo, so the members' surfaces follow what the site already encodes: Loom palette (`--bg`, `--ink`, one `--accent`), Fraunces for headings, Plex Sans for reading, Plex Mono uppercase for labels, short declarative copy, no exclamation marks. Every list link carries a one-sentence `.link-blurb` saying what is behind it. Copy `BRAND.md` into `docs/` and future work can be checked against it directly.

## Known sharp edge

`wrangler.jsonc` sets `disable_nodejs_process_v2`. Without it, Astro 6 on a 2026 compatibility date detects workerd as Node and every on-demand page comes back as the literal text `[object Object]` with a 200. Static pages are unaffected. Re-test `/signin/` after any Astro or adapter upgrade before removing it.

## Security notes

- The Stripe key is restricted and read-only; the Worker never charges anyone.
- The session cookie is HttpOnly, Secure, SameSite=Lax, HMAC-signed; tampering fails verification. Rotating `SESSION_SECRET` signs everyone out and invalidates old digest opt-out links.
- Magic links are single-use, 15 minutes, 256-bit; the GET only renders a page that POSTs the token, so mail-scanner prefetches don't burn it.
- `/api/digest/send` needs the bearer secret; opt-out links are HMAC-signed per address.
- Every `/members`, `/signin`, `/auth`, `/api` response is `Cache-Control: private, no-store` + `X-Robots-Tag: noindex`; `robots.txt` disallows them; they are excluded from the sitemap and the Pagefind index. Members' content is never in the repo, the build output or `llms.txt`.
