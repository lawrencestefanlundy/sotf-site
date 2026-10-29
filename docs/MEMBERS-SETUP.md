# Members' edition — setup and operations

The paywall for the deeper KB content. Public pages stay exactly as they are
(prerendered, free, indexed). Paid newsletter subscribers sign in with the email
they use on Substack and get the members' edition of each concept: the investor
view the public page strips.

## How it fits together

| Piece | Service | Why this one |
|---|---|---|
| Hosting | **Cloudflare Workers** (static assets + Worker) | Public pages are still static files on a CDN; only `/members`, `/signin`, `/auth`, `/api` run code. Free tier covers this traffic comfortably. |
| Members' content | **Cloudflare R2** bucket `sotf-members` | Private object store the Worker reads per request. The content never enters this public repo or the build. A nightly sync is the members' deploy — no rebuild. |
| Sign-in tokens | **Cloudflare KV** `AUTH_KV` | 15-minute one-time magic-link tokens and a per-email rate limit. Nothing else is stored. |
| Who is a subscriber | **Stripe** (your existing account) | Substack bills through *your* Stripe account, so every paid subscriber is already a Customer with a Subscription there. The site asks Stripe directly: one subscriber list, one bill, nothing to migrate. |
| Email | **Resend** | Sends the sign-in link from `members@stateofthefuture.io`. Free tier: 3,000/month. |
| Billing, essays | **Substack** | Unchanged. Readers subscribe and cancel there; access here follows within a day. |

Session = signed cookie (HMAC, 30 days), re-checked against Stripe once a day so a
lapsed subscriber loses access without anyone doing anything.

Code: `src/middleware.ts` (the gate), `src/lib/{auth,stripe,mail,members}.ts`,
`src/pages/{signin.astro,api/auth/request.ts,auth/verify.astro,auth/signout.ts,members/**}`,
`scripts/publish_kb.py` (members' tier), `scripts/upload_members.py` (R2 sync).

## What is paywalled

`publish_kb.py` now emits two editions of every concept:

- **public** — as before: Cloudberry sections removed, Attio-tracked companies removed, private sources removed.
- **members** — the same note with the `## Cloudberry …` sections and any paragraph mentioning Cloudberry kept. Attio-tracked companies, private source kinds (granola/memo/email/note) and deal fields stay stripped: subscribers get the investor view of a technology, never the pipeline.

A concept gets a members' edition only when the two differ. Its public frontmatter
then carries `members: true` and the section names, which the concept page uses for
the teaser. To change what counts as members-only, edit `member_body()` in
`scripts/publish_kb.py` — it is the public pipeline minus one strip pass.

## One-time setup (about an hour)

### 1. Stripe — confirm and make a restricted key
1. dashboard.stripe.com → **Customers**. You should see your Substack subscribers (Substack creates them in your account). If you don't, stop and tell me — we'd switch to a Substack-export allowlist instead.
2. **Developers → API keys → Create restricted key**. Name `sotf-site members check`. Permissions: **Customers: Read**, **Subscriptions: Read**. Everything else None. Copy the `rk_live_…` key.

### 2. Resend — sending domain
1. resend.com → **Domains → Add** `stateofthefuture.io`. Add the DNS records it shows (at your DNS provider; after step 4 that is Cloudflare).
2. **API Keys → Create** with *Sending access* only. Copy `re_…`.

### 3. Cloudflare — account, bucket, token
1. Create a Cloudflare account (free) if you don't have one. Note the **Account ID** (right-hand side of the Workers & Pages overview).
2. **R2 → Create bucket** `sotf-members` (location: automatic). Then **R2 → Manage API tokens → Create**: *Object Read & Write*, scoped to this bucket. Copy the Access Key ID and Secret Access Key — these go on your Mac (step 6), not GitHub.
3. **Manage account → Account API Tokens → Create Token → Edit Cloudflare Workers template**. Add permissions *Workers KV Storage: Edit* and *Workers R2 Storage: Edit* if the template lacks them. Copy the token.

### 4. GitHub — turn the deploy on
In the repo: **Settings → Secrets and variables → Actions**.
- Secrets: `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`.
- Variables: `CLOUDFLARE_DEPLOY` = `true`.

Then **Actions → Deploy to Cloudflare → Run workflow**. First run provisions the KV
namespaces and deploys the Worker at `sotf-site.<your-subdomain>.workers.dev`.
(If it fails on a KV namespace without an `id`, run `npx wrangler kv namespace create AUTH_KV`
locally and paste the id into `wrangler.jsonc`.)

### 5. Secrets on the Worker
From the repo, logged in with `npx wrangler login`:
```sh
openssl rand -hex 32 | npx wrangler secret put SESSION_SECRET
npx wrangler secret put STRIPE_SECRET_KEY      # rk_live_… from step 1
npx wrangler secret put RESEND_API_KEY         # re_… from step 2
npx wrangler secret put MEMBER_ALLOWLIST       # your own email, comped readers; comma-separated
```

### 6. Your Mac — the nightly sync
Add to `~/.config/kb/env` (sourced by `nightly_publish.sh`):
```sh
export R2_ACCOUNT_ID=…
export R2_ACCESS_KEY_ID=…
export R2_SECRET_ACCESS_KEY=…
```
and `pip install boto3` in `~/kb/scripts/.venv`. Then run once by hand:
```sh
python3 scripts/publish_kb.py          # now also writes .members-out/
python3 scripts/upload_members.py --dry-run
python3 scripts/upload_members.py
```

### 7. Test on workers.dev before touching DNS
- `https://sotf-site.<sub>.workers.dev/members/` → landing page.
- Sign in with your own (allowlisted) email → link arrives → members' index.
- Sign in with a paying subscriber's email in a private window → should pass the Stripe check (the link goes to their inbox, so stop at the "sent" page).
- Sign in with a random email → "No active paid subscription".

### 8. Cut over
1. Cloudflare → **Workers & Pages → sotf-site → Settings → Domains & Routes → Add → Custom domain** `stateofthefuture.io` (and `www`). If the domain's DNS isn't on Cloudflare yet, it walks you through moving nameservers; Resend's records come with it.
2. Once `https://stateofthefuture.io/members/` serves from the Worker: delete `.github/workflows/deploy.yml` and `public/CNAME`, and turn GitHub Pages off in repo settings.

## Day to day

- **Nothing.** Nightly publish updates both editions; the public one via the git push + Actions build, the members' one via the R2 sync (`logs/nightly-publish.log` says `synced N members' concepts`).
- A new paid subscriber on Substack can sign in immediately. A lapsed one is locked out within 24 h.
- Comp someone: add their email to `MEMBER_ALLOWLIST` (`npx wrangler secret put MEMBER_ALLOWLIST`).
- Local dev with the members' routes: `cp .dev.vars.example .dev.vars`, fill it in, `npm run dev:members`. KV and R2 are emulated locally (empty R2 → members' pages 404 until you `wrangler r2 object put` a few files, or just test the sign-in flow).

## Known sharp edge

`wrangler.jsonc` sets `disable_nodejs_process_v2`. Without it, Astro 6 on a 2026
compatibility date detects workerd as Node and every on-demand page (sign-in,
members) comes back as the literal text `[object Object]` with a 200. Static pages
are unaffected. If a future Astro release fixes the detection, the flag can go;
until then, don't remove it, and re-test `/signin/` after any Astro or adapter upgrade.

## Security notes

- The Stripe key is restricted and read-only; the Worker never charges anyone.
- The session cookie is HttpOnly, Secure, SameSite=Lax, HMAC-signed; tampering fails verification. Rotating `SESSION_SECRET` signs everyone out.
- Magic links are single-use, 15 minutes, 256-bit; the GET only renders a page that POSTs the token, so mail-scanner prefetches don't burn it.
- Every `/members`, `/signin`, `/auth`, `/api` response is `Cache-Control: private, no-store` + `X-Robots-Tag: noindex`; `robots.txt` disallows them; they are excluded from the sitemap and the Pagefind index. Members' content is never in the repo, the build output or `llms.txt`.
