/**
 * GET /api/digest/unsubscribe?e=<email>&s=<hmac> — one click from the email footer.
 * Stops the weekly digest for that address; membership access is untouched.
 */
export const prerender = false;

import type { APIRoute } from "astro";
import { getEnv } from "../../../env";
import { normaliseEmail, verifyValue } from "../../../lib/auth";

export const GET: APIRoute = async ({ url, redirect }) => {
  const env = getEnv();
  const email = normaliseEmail(url.searchParams.get("e"));
  const sig = url.searchParams.get("s") ?? "";
  if (!email || !env.SESSION_SECRET || !(await verifyValue(`digest:${email}`, sig, env.SESSION_SECRET))) {
    return redirect("/members/?digest=invalid", 303);
  }
  if (env.AUTH_KV) await env.AUTH_KV.put(`nodigest:${email}`, new Date().toISOString());
  return redirect("/members/?digest=off", 303);
};
