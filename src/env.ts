/**
 * Worker bindings and secrets, as declared in wrangler.jsonc and set with
 * `wrangler secret put`. Astro 6 + @astrojs/cloudflare 13 expose them through
 * the `cloudflare:workers` module (Astro.locals.runtime.env is gone).
 */
import { env as cfEnv } from "cloudflare:workers";

export type Env = {
  // Bindings
  AUTH_KV: KVNamespace;          // magic-link tokens + rate limits (TTL'd)
  MEMBERS_BUCKET: R2Bucket;      // members' edition JSON, synced by upload_members.py
  ASSETS: Fetcher;
  // Secrets
  SESSION_SECRET: string;        // HMAC key for the session cookie (openssl rand -hex 32)
  STRIPE_SECRET_KEY: string;     // restricted key: Customers + Subscriptions, read
  RESEND_API_KEY: string;
  MEMBER_ALLOWLIST?: string;     // comma-separated emails that bypass Stripe (comps, author)
  DIGEST_SECRET?: string;        // bearer token the nightly script uses to trigger the weekly digest
  // Vars
  MAIL_FROM?: string;
  SITE_URL?: string;
};

export function getEnv(): Env {
  return cfEnv as unknown as Env;
}
