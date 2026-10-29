/**
 * POST /api/digest/send — build this week's digest and email it to every paying
 * subscriber (Stripe) and allowlisted reader, minus anyone who opted out.
 * Triggered by nightly_publish.sh on Mondays with `Authorization: Bearer $DIGEST_SECRET`.
 * `?dry=1` returns the recipient count and the rendered subject without sending.
 */
export const prerender = false;

import type { APIRoute } from "astro";
import { getEnv } from "../../../env";
import { signValue } from "../../../lib/auth";
import { buildDigest } from "../../../lib/digest";
import { sendEmail } from "../../../lib/mail";
import { getChanges, getMemberIndex } from "../../../lib/members";
import { listSubscriberEmails } from "../../../lib/stripe";

const json = (body: unknown, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json" } });

export const POST: APIRoute = async ({ request, url }) => {
  const env = getEnv();
  const auth = request.headers.get("authorization") ?? "";
  if (!env.DIGEST_SECRET || auth !== `Bearer ${env.DIGEST_SECRET}`) return json({ error: "unauthorised" }, 401);
  if (!env.SESSION_SECRET) return json({ error: "SESSION_SECRET not set" }, 500);

  const dry = url.searchParams.get("dry") === "1";
  const site = (env.SITE_URL ?? url.origin).replace(/\/$/, "");
  const [changes, index, all] = await Promise.all([getChanges(env), getMemberIndex(env), listSubscriberEmails(env)]);

  const recipients: string[] = [];
  for (const email of all) {
    if (env.AUTH_KV && (await env.AUTH_KV.get(`nodigest:${email}`))) continue;
    recipients.push(email);
  }
  const preview = buildDigest(changes, index, site);
  if (dry) return json({ recipients: recipients.length, items: preview.items, subject: preview.subject });
  if (preview.items === 0 && url.searchParams.get("force") !== "1") {
    return json({ recipients: recipients.length, sent: 0, skipped: "quiet week — nothing changed; pass ?force=1 to send anyway" });
  }

  let sent = 0, failed = 0;
  for (const email of recipients) {
    const sig = await signValue(`digest:${email}`, env.SESSION_SECRET);
    const unsub = `${site}/api/digest/unsubscribe/?e=${encodeURIComponent(email)}&s=${sig}`;
    const d = buildDigest(changes, index, site, unsub);
    const ok = await sendEmail(env, {
      to: email, subject: d.subject, text: d.text, html: d.html,
      headers: { "List-Unsubscribe": `<${unsub}>` },
    });
    ok ? sent++ : failed++;
  }
  return json({ recipients: recipients.length, sent, failed, items: preview.items });
};
