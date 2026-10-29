/**
 * POST /api/auth/request — form from /signin. Checks the email has a live
 * subscription, mints a one-time token in KV and emails the link.
 *
 * The subscription is checked *before* sending so a reader who is not (or no
 * longer) paying gets told immediately, with the subscribe link, instead of
 * waiting for an email that never comes.
 */
export const prerender = false;

import type { APIRoute } from "astro";
import { getEnv } from "../../../env";
import { MAGIC_LINK_TTL_S, normaliseEmail, randomToken, safeNext } from "../../../lib/auth";
import { sendMagicLink } from "../../../lib/mail";
import { checkEntitlement } from "../../../lib/stripe";

export const POST: APIRoute = async ({ request, redirect, url }) => {
  const env = getEnv();
  const form = await request.formData();
  const email = normaliseEmail(form.get("email"));
  const next = safeNext(String(form.get("next") ?? ""));
  const back = (q: Record<string, string>) => redirect(`/signin/?${new URLSearchParams({ next, ...q })}`, 303);

  if (!email) return back({ error: "invalid" });
  if (!env.SESSION_SECRET || !env.AUTH_KV) return back({ error: "config", email });

  // One link per address per minute, whatever the outcome.
  const rlKey = `rl:${email}`;
  if (await env.AUTH_KV.get(rlKey)) return back({ error: "ratelimit", email });
  await env.AUTH_KV.put(rlKey, "1", { expirationTtl: 60 });

  const ent = await checkEntitlement(email, env);
  if (!ent.active) return back({ error: ent.reason === "error" ? "stripe" : "nosub", email });

  const token = randomToken();
  await env.AUTH_KV.put(`ml:${token}`, JSON.stringify({ email, next }), { expirationTtl: MAGIC_LINK_TTL_S });

  // Links point at the canonical host in production; at whatever host served
  // the form in local dev.
  const local = url.hostname === "localhost" || url.hostname === "127.0.0.1";
  const origin = (!local && env.SITE_URL?.replace(/\/$/, "")) || url.origin;
  const sent = await sendMagicLink(env, email, `${origin}/auth/verify/?t=${token}`);
  if (!sent) return back({ error: "mail", email });

  return back({ sent: "1", email });
};
