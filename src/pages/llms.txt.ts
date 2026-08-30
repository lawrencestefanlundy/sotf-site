import type { APIRoute } from "astro";
import { getCollection } from "astro:content";

// llms.txt — a plain-text map of the site for AI search engines / LLM crawlers.
// Spec convention: https://llmstxt.org/
export const GET: APIRoute = async ({ site }) => {
  const base = (site?.toString() ?? "https://stateofthefuture.io/").replace(/\/$/, "");
  const concepts = await getCollection("concepts");

  const byMacro = new Map<string, { name: string; url: string }[]>();
  for (const c of concepts) {
    const parts = c.id.split("/");
    if (parts.length !== 3) continue;
    const [macro, meso, slug] = parts;
    const list = byMacro.get(macro) ?? [];
    list.push({ name: c.data.canonical_name, url: `${base}/${macro}/${meso}/${slug}/` });
    byMacro.set(macro, list);
  }

  const lines: string[] = [
    "# State of the Future",
    "",
    "> Lawrence Lundy-Bryan's public deep-tech reference: concept pages on semiconductors,",
    "> photonics, advanced materials, compute, sensing and energy, rebuilt nightly from the",
    "> research base behind his investing. Analysis and essays: https://stateofthefuture.substack.com",
    "",
    `- [Atlas (full graph)](${base}/atlas/)`,
    `- [Tours (curated paths)](${base}/tours/)`,
    `- [Writing](${base}/writing/)`,
    `- [About](${base}/about/)`,
    "",
  ];

  for (const [macro, items] of [...byMacro.entries()].sort()) {
    lines.push(`## ${macro.replace(/-/g, " ")}`);
    lines.push("");
    for (const item of items.sort((a, b) => a.name.localeCompare(b.name))) {
      lines.push(`- [${item.name}](${item.url})`);
    }
    lines.push("");
  }

  return new Response(lines.join("\n"), {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
};
