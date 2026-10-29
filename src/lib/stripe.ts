/**
 * Entitlement = "does this email have a live paid subscription in my Stripe account?"
 *
 * Substack bills through the writer's own Stripe account, so every paid
 * newsletter subscriber already exists there as a Customer with a Subscription.
 * Checking Stripe directly means one subscriber list, one bill, and nothing to
 * migrate: a reader subscribes on Substack, then signs in here with the same
 * email. MEMBER_ALLOWLIST covers comped readers and the author.
 *
 * Uses the REST API over fetch — no SDK, nothing to bundle into the Worker.
 * The key should be a *restricted* key with read-only Customers + Subscriptions.
 */
import type { Env } from "../env";

export type Entitlement = {
  active: boolean;
  reason: "stripe" | "allowlist" | "none" | "error";
  status?: string;
};

// past_due keeps access while Stripe retries the card, matching Substack's behaviour.
const LIVE_STATUSES = new Set(["active", "trialing", "past_due"]);

function allowlisted(email: string, env: Env): boolean {
  return (env.MEMBER_ALLOWLIST ?? "")
    .split(/[,\s;]+/)
    .map((s) => s.trim().toLowerCase())
    .filter(Boolean)
    .includes(email);
}

async function stripeGet(path: string, key: string): Promise<any> {
  const res = await fetch(`https://api.stripe.com/v1${path}`, {
    headers: { Authorization: `Bearer ${key}` },
    signal: AbortSignal.timeout(8000),
  });
  if (!res.ok) throw new Error(`Stripe ${res.status} on ${path.split("?")[0]}`);
  return res.json();
}

/**
 * Every email with a live subscription, plus the allowlist: the digest's
 * recipient list. Paginates; a few hundred subscribers is a handful of calls.
 */
export async function listSubscriberEmails(env: Env): Promise<string[]> {
  const emails = new Set<string>(
    (env.MEMBER_ALLOWLIST ?? "").split(/[,\s;]+/).map((s) => s.trim().toLowerCase()).filter(Boolean),
  );
  if (!env.STRIPE_SECRET_KEY) return [...emails];
  for (const status of ["active", "trialing", "past_due"]) {
    let after: string | undefined;
    for (let page = 0; page < 20; page++) {
      const q = new URLSearchParams({ status, limit: "100" });
      q.append("expand[]", "data.customer");
      if (after) q.set("starting_after", after);
      const res = await stripeGet(`/subscriptions?${q}`, env.STRIPE_SECRET_KEY);
      for (const s of res.data ?? []) {
        const email = s.customer?.email;
        if (typeof email === "string" && email.includes("@")) emails.add(email.trim().toLowerCase());
        after = s.id;
      }
      if (!res.has_more) break;
    }
  }
  return [...emails];
}

export async function checkEntitlement(email: string, env: Env): Promise<Entitlement> {
  if (allowlisted(email, env)) return { active: true, reason: "allowlist" };
  if (!env.STRIPE_SECRET_KEY) return { active: false, reason: "none" };

  try {
    // One call: customers matching the email, each with its subscriptions expanded.
    const q = new URLSearchParams({ email, limit: "20" });
    q.append("expand[]", "data.subscriptions");
    const customers = await stripeGet(`/customers?${q}`, env.STRIPE_SECRET_KEY);

    let seen: string | undefined;
    for (const c of customers.data ?? []) {
      let subs: any[] = c.subscriptions?.data ?? [];
      // The embedded list is capped at 10; a long history needs the full list.
      if (c.subscriptions?.has_more) {
        const all = await stripeGet(`/subscriptions?customer=${c.id}&status=all&limit=100`, env.STRIPE_SECRET_KEY);
        subs = all.data ?? [];
      }
      for (const s of subs) {
        seen = s.status;
        if (LIVE_STATUSES.has(s.status)) return { active: true, reason: "stripe", status: s.status };
      }
    }
    return { active: false, reason: "none", status: seen };
  } catch (err) {
    console.error("entitlement check failed", err);
    return { active: false, reason: "error" };
  }
}
