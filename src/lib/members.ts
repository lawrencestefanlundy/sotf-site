/**
 * Members' content lives in a private R2 bucket, written by scripts/publish_kb.py
 * + upload_members.py. Nothing here is in the repo, the build or the static assets:
 * the Worker fetches an object per request, only after middleware has let the
 * request through.
 */
import { marked } from "marked";
import type { Env } from "../env";

export type MemberEntry = {
  slug: string;
  name: string;
  macro: string;
  meso: string;
  path: string;          // "macro/meso/slug"
  last_updated: string;
  extra_sections: string[];
};

export type MemberIndex = { generated: string; count: number; concepts: MemberEntry[] };

export type MemberConcept = MemberEntry & {
  scorecard?: Record<string, unknown> | null;
  scorecard_status?: string | null;
  sources_30d?: number;
  body_md: string;
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
