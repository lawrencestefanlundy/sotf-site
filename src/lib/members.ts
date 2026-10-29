/**
 * Members' content lives in a private R2 bucket, written by scripts/publish_kb.py
 * + upload_members.py. Nothing here is in the repo, the build or the static assets:
 * the Worker fetches an object per request, only after middleware has let the
 * request through.
 */
import { marked } from "marked";
import type { Env } from "../env";

export type Dim = "viability" | "drivers" | "novelty" | "diffusion" | "impact";
export const DIMS: Dim[] = ["viability", "drivers", "novelty", "diffusion", "impact"];
export type Scores = Record<Dim, number | null>;

export type Status = "scored" | "draft" | "unscored" | "stub";

export type MemberEntry = {
  slug: string;
  name: string;
  macro: string;
  meso: string;
  path: string;              // "macro/meso/slug"
  last_updated: string;
  summary: string;           // one sentence: what the page says
  extra_sections: string[];  // members-only sections, for the teaser
  members: boolean;          // has an edition of its own
  status: Status;
  scores: Scores;
  verdict: string;
  timing: string;
  words: number;
  sources_7d: number;
  sources_30d: number;
};

export type MemberIndex = { generated: string; count: number; total: number; concepts: MemberEntry[] };

export type SourceRef = { slug: string; title: string; url: string; date: string; kind: string; blurb: string };
export type CompanyCard = { slug: string; name: string; website?: string; hq?: string; founded?: string; stage?: string; blurb?: string };

export type ChangeEvent = {
  date: string;
  slug: string;
  name: string;
  path: string;
  summary: string;
  members?: boolean;         // has a members' edition to link to; else link the public page
  kind: "score" | "verdict" | "timing" | "status" | "new";
  field?: string;
  old?: string | number | null;
  new?: string | number | null;
};

export type ActiveConcept = {
  slug: string; name: string; path: string; summary: string; members?: boolean; sources_7d: number;
  mentions: { title: string; url: string; date: string; kind: string; blurb: string }[];
};

/** Where a concept link goes: its members' edition when it has one, else the public page. */
export function conceptHref(c: { path: string; members?: boolean }, base = ""): string {
  return c.members ? `${base}/members/${c.path}/` : `${base}/${c.path}/`;
}

export type Changes = { generated: string; bootstrapped: string | null; events: ChangeEvent[]; active: ActiveConcept[] };

export type MemberConcept = MemberEntry & {
  scorecard?: Record<string, unknown> | null;
  scorecard_status?: string | null;
  body_md: string;
  sources: SourceRef[];
  essays: SourceRef[];
  companies: CompanyCard[];
  recent_mentions: { slug: string; title: string; date: string; kind: string }[];
  history?: ChangeEvent[];
};

const SEGMENT = /^[a-z0-9][a-z0-9-]{0,120}$/;

export function validSegments(...parts: (string | undefined)[]): parts is string[] {
  return parts.every((p) => typeof p === "string" && SEGMENT.test(p));
}

async function getJson<T>(env: Env, key: string): Promise<T | null> {
  const bucket = env.MEMBERS_BUCKET;
  if (!bucket) return null;                    // binding missing: wrangler.jsonc misconfig
  const obj = await bucket.get(key);
  if (!obj) return null;
  return (await obj.json()) as T;
}

export const getMemberIndex = (env: Env) => getJson<MemberIndex>(env, "index.json");
export const getChanges = (env: Env) => getJson<Changes>(env, "changes.json");

export function getMemberConcept(env: Env, macro: string, meso: string, slug: string) {
  return getJson<MemberConcept>(env, `${macro}/${meso}/${slug}.json`);
}

marked.setOptions({ gfm: true, breaks: false });

/** Author-controlled markdown → HTML. No sanitiser: the only writer is publish_kb.py. */
export function renderMarkdown(md: string): string {
  // Dataview placeholders from the publisher are HTML comments; drop them and
  // the headings they leave empty rather than render blank sections.
  const cleaned = md
    .replace(/^##+\s+[^\n]+\n+<!--[^>]*-->\s*(?=\n##+\s|\n*$)/gm, "")
    .replace(/<!--[^>]*-->/g, "");
  return marked.parse(cleaned, { async: false }) as string;
}

const DIM_LABEL: Record<string, string> = {
  viability: "Viability", drivers: "Drivers", novelty: "Novelty", diffusion: "Diffusion", impact: "Impact",
};

/** One short clause per event, the same in the feed, the page history and the email. */
export function describeEvent(e: ChangeEvent): string {
  switch (e.kind) {
    case "score": {
      const dim = DIM_LABEL[e.field ?? ""] ?? e.field;
      return e.old == null ? `${dim} first scored ${e.new}/5` : `${dim} ${e.old} → ${e.new}`;
    }
    case "verdict":
      return e.old ? `Call changed: ${e.old} → ${e.new}` : `Called: ${e.new}`;
    case "timing":
      return e.old ? `Timing ${e.old} → ${e.new}` : `Timing set: ${e.new}`;
    case "status":
      return e.new === "scored" ? "Scorecard finalised" : "Scorecard drafted";
    case "new":
      return "New concept";
  }
}

export const STATUS_LABEL: Record<Status, string> = {
  scored: "scored", draft: "draft", unscored: "unscored", stub: "stub",
};
