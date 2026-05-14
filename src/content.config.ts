import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

// Concepts collection — filtered + emitted by scripts/publish_kb.py.
// Schema mirrors ~/kb/CLAUDE.md concept frontmatter, with publish-only additions
// (sources_7d, sources_30d).
const concepts = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./src/content/concepts",
    // Preserve the macro/meso path in the id so [macro]/[meso]/[slug] routing works
    generateId: ({ entry }) => entry.replace(/\.md$/, ""),
  }),
  schema: z
    .object({
      type: z.string().optional(),
      slug: z.string(),
      canonical_name: z.string(),
      aliases: z.array(z.string()).default([]),
      kind: z.string().optional(),
      domain: z.array(z.string()).default([]),
      parent_concepts: z.array(z.string()).default([]),
      related_concepts: z.array(z.string()).default([]),
      descendants: z.array(z.string()).default([]),
      companies_using: z.array(z.string()).default([]),
      ideas_referencing: z.array(z.string()).default([]),
      sources: z.array(z.string()).default([]),
      sources_7d: z.number().default(0),
      sources_30d: z.number().default(0),
      recent_mentions: z
        .array(z.object({
          slug: z.string(),
          title: z.string(),
          date: z.string(),
          kind: z.string(),
        }))
        .default([]),
      neighbors: z
        .array(z.object({
          slug: z.string(),
          name: z.string(),
          path: z.string(),
          macro: z.string(),
        }))
        .default([]),
      frontier: z.array(z.string()).default([]),
      last_updated: z.union([z.string(), z.date()]).optional(),
      last_reorg_date: z.union([z.string(), z.date()]).optional(),
      mention_count: z.number().optional(),
      tags: z.array(z.string()).default([]),
    })
    .passthrough(),
});

// Tours collection — Lawrence-authored narrative walkthroughs.
const tours = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/tours" }),
  schema: z.object({
    slug: z.string(),
    title: z.string(),
    subtitle: z.string().optional(),
    published_date: z.union([z.string(), z.date()]).optional(),
    duration_minutes: z.number().optional(),
    concepts_visited: z.array(z.string()).default([]),
    related_ideas: z.array(z.string()).default([]),
    last_updated: z.union([z.string(), z.date()]).optional(),
  }),
});

// Writing collection — Substack archive imports (later phase).
const writing = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/writing" }),
  schema: z.object({
    title: z.string(),
    published_date: z.union([z.string(), z.date()]).optional(),
    external_url: z.string().optional(),
    summary: z.string().optional(),
  }),
});

export const collections = { concepts, tours, writing };
