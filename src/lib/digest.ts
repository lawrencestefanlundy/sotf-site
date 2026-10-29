/**
 * The weekly members' digest: what changed in the last seven days, as text and
 * HTML. Every link carries one sentence saying what is behind it. The same
 * builder renders the email and the /members/digest/ preview.
 */
import { conceptHref, describeEvent, type ChangeEvent, type Changes, type MemberIndex } from "./members";

export type Digest = { subject: string; text: string; html: string; inner: string; items: number };

const esc = (s: string) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]!));

type Item = { href: string; label: string; clause: string; sentence: string };

function section(title: string, items: Item[]): { text: string; html: string } {
  if (!items.length) return { text: "", html: "" };
  const text = [`${title.toUpperCase()}`, "", ...items.map((i) => `• ${i.label} — ${i.clause}\n  ${i.sentence}\n  ${i.href}`), ""].join("\n");
  const html = `<h2 style="font-family:Georgia,serif;font-size:17px;margin:26px 0 8px;padding-top:12px;border-top:1px solid #CFC5AF;color:#1E1B18">${esc(title)}</h2>` +
    items.map((i) =>
      `<p style="margin:0 0 12px;font-size:15px;line-height:1.5"><a href="${esc(i.href)}" style="color:#1E1B18;font-weight:600;text-decoration:underline;text-underline-offset:3px">${esc(i.label)}</a>` +
      ` <span style="color:#2F5D73">— ${esc(i.clause)}</span>` +
      (i.sentence ? `<br><span style="color:#1E1B1899">${esc(i.sentence)}</span>` : "") + `</p>`).join("");
  return { text, html };
}

export function buildDigest(changes: Changes | null, index: MemberIndex | null, siteUrl: string, unsubscribeUrl?: string): Digest {
  const base = siteUrl.replace(/\/$/, "");
  const week = new Date(Date.now() - 7 * 86400e3).toISOString().slice(0, 10);
  const events = (changes?.events ?? []).filter((e) => e.date >= week);
  const link = (e: ChangeEvent) => conceptHref(e, base);
  const item = (e: ChangeEvent): Item => ({ href: link(e), label: e.name, clause: describeEvent(e), sentence: e.summary });

  const calls = events.filter((e) => e.kind === "verdict").map(item);
  const scores = events.filter((e) => e.kind === "score" && e.old != null).map(item);
  const firstScored = events.filter((e) => (e.kind === "score" && e.old == null) || e.kind === "status");
  // One line per concept for "newly scored", not one per dimension.
  const seen = new Set<string>();
  const scored = firstScored.filter((e) => !seen.has(e.slug) && seen.add(e.slug))
    .map((e) => ({ href: link(e), label: e.name, clause: "Newly scored", sentence: e.summary }));
  const timing = events.filter((e) => e.kind === "timing").map(item);
  const fresh = events.filter((e) => e.kind === "new").map(item);
  const active: Item[] = (changes?.active ?? []).slice(0, 8).map((a) => ({
    href: conceptHref(a, base),
    label: a.name,
    clause: `${a.sources_7d} new source${a.sources_7d === 1 ? "" : "s"} this week`,
    sentence: a.mentions[0] ? `Latest: ${a.mentions[0].title}${a.mentions[0].blurb ? ` — ${a.mentions[0].blurb}` : ""}` : a.summary,
  }));

  const sections = [
    section("Calls that changed", calls),
    section("Scores that moved", scores),
    section("Newly scored", scored),
    section("Timing revised", timing),
    section("New concepts", fresh),
    section("Most active this week", active),
  ];
  const items = calls.length + scores.length + scored.length + timing.length + fresh.length + active.length;
  const dateLabel = new Date().toISOString().slice(0, 10);
  const subject = `State of the Future — what changed, week to ${dateLabel}`;
  const scoredCount = index ? index.concepts.filter((c) => c.status === "scored" || c.status === "draft").length : null;

  const intro = items
    ? `The research base behind State of the Future rebuilds nightly. This is what moved in the last seven days${scoredCount ? ` across ${scoredCount} scored technologies` : ""}.`
    : "A quiet week: no scores, calls or timing changed in the last seven days.";
  const text = [
    "STATE OF THE FUTURE · MEMBERS' DIGEST", "", intro, "",
    ...sections.map((s) => s.text).filter(Boolean),
    `Changes feed: ${base}/members/changes/ — every change in the last 90 days.`,
    `Screener: ${base}/members/screener/ — filter all scored technologies by verdict, timing and score.`,
    "",
    unsubscribeUrl ? `Stop the weekly digest (your access is unaffected): ${unsubscribeUrl}` : "",
  ].join("\n");

  const inner = `<div style="max-width:560px;margin:0 auto;background:#FAF7F1;border:1px solid #1E1B18;padding:28px 28px 22px">
  <p style="font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:#1E1B1899;margin:0 0 14px;font-family:Menlo,monospace">State of the Future · Members' digest</p>
  <p style="font-size:16px;line-height:1.55;margin:0 0 6px">${esc(intro)}</p>
  ${sections.map((s) => s.html).join("")}
  <p style="font-size:14px;line-height:1.55;margin:26px 0 0;padding-top:12px;border-top:1px solid #CFC5AF"><a href="${base}/members/changes/" style="color:#1E1B18">Changes feed</a> — every change in the last 90 days.<br><a href="${base}/members/screener/" style="color:#1E1B18">Screener</a> — filter all scored technologies by verdict, timing and score.</p>
  ${unsubscribeUrl ? `<p style="font-size:12px;color:#1E1B1899;margin:18px 0 0">You get this as a paid subscriber. <a href="${esc(unsubscribeUrl)}" style="color:#1E1B1899">Stop the weekly digest</a> — your access is unaffected.</p>` : ""}
</div>`;
  const html = `<!doctype html><html><body style="margin:0;padding:32px 16px;background:#F5F1E6;color:#1E1B18;font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif">${inner}</body></html>`;

  return { subject, text, html, inner, items };
}
