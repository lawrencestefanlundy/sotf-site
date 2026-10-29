/**
 * Email via Resend's REST API (no SDK in the Worker bundle).
 * MAIL_FROM must be on a domain verified in Resend, e.g. members@stateofthefuture.io.
 */
import type { Env } from "../env";

export type Mail = { to: string; subject: string; text: string; html: string; headers?: Record<string, string> };

export async function sendEmail(env: Env, mail: Mail): Promise<boolean> {
  if (!env.RESEND_API_KEY) {
    console.error("RESEND_API_KEY not set; email not sent");
    return false;
  }
  const from = env.MAIL_FROM ?? "State of the Future <members@stateofthefuture.io>";
  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({ from, ...mail }),
    signal: AbortSignal.timeout(10000),
  });
  if (!res.ok) console.error("Resend", res.status, await res.text().catch(() => ""));
  return res.ok;
}

export async function sendMagicLink(env: Env, to: string, link: string): Promise<boolean> {
  const text = [
    "Your sign-in link for State of the Future:",
    "",
    link,
    "",
    "It works once and expires in 15 minutes. If you did not ask for it, ignore this email — nobody can sign in without it.",
    "",
    "— Lawrence",
  ].join("\n");
  const html = `<!doctype html><html><body style="font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;color:#1E1B18;background:#F5F1E6;padding:32px">
  <div style="max-width:520px;margin:0 auto;background:#FAF7F1;border:1px solid #1E1B18;padding:28px 28px 24px">
    <p style="font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#1E1B1899;margin:0 0 18px">State of the Future · Members</p>
    <p style="font-size:17px;line-height:1.5;margin:0 0 20px">Here is your sign-in link. It works once and expires in 15 minutes.</p>
    <p style="margin:0 0 22px"><a href="${link}" style="display:inline-block;background:#2F5D73;color:#FAF7F1;text-decoration:none;padding:12px 18px;font-size:13px;letter-spacing:.08em;text-transform:uppercase;border-radius:2px">Sign in</a></p>
    <p style="font-size:13px;line-height:1.5;color:#1E1B1899;margin:0 0 6px">Or paste this into your browser:</p>
    <p style="font-size:13px;line-height:1.5;word-break:break-all;margin:0 0 22px"><a href="${link}" style="color:#1E1B18">${link}</a></p>
    <p style="font-size:13px;line-height:1.5;color:#1E1B1899;margin:0">If you did not ask for this, ignore it — nobody can sign in without the link.</p>
  </div></body></html>`;
  return sendEmail(env, { to, subject: "Your sign-in link — State of the Future", text, html });
}
