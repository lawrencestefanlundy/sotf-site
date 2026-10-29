// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import cloudflare from '@astrojs/cloudflare';

// MEMBERS_ENABLED=1 at build time turns on the members' nav link and the teasers
// on concept pages. Off by default so a build for the old GitHub Pages host (no
// Worker, so no /members routes) carries no dead links. The Cloudflare deploy
// workflow sets it.
const membersEnabled = process.env.MEMBERS_ENABLED === '1';

// Routes that must never appear in the sitemap: paywalled, auth, API.
const PRIVATE_ROUTE = /\/(members|signin|auth|api)(\/|$)/;

// https://astro.build/config
export default defineConfig({
  // Live at the custom domain. public/CNAME pins stateofthefuture.io; internal
  // links resolve from root (no `base`). To revert to the github.io preview:
  // set `site` back to https://lawrencestefanlundy.github.io, add base:'/sotf-site',
  // and remove public/CNAME.
  site: 'https://stateofthefuture.io',

  // Static by default: every public page is prerendered and served as an asset.
  // Only routes that opt out (`export const prerender = false`: /members, /signin,
  // /auth, /api) run in the Worker, where middleware.ts gates them.
  adapter: cloudflare({
    imageService: 'compile',
  }),

  integrations: [
    sitemap({
      filter: (page) => !PRIVATE_ROUTE.test(new URL(page).pathname) || /\/members\/$/.test(new URL(page).pathname),
    }),
  ],

  // Prefetch every link on hover or tap (nav links on sight, see Base.astro). 'viewport' for
  // all links fetched dozens of pages at once on link-dense pages and competed with the page.
  prefetch: {
    prefetchAll: true,
    defaultStrategy: 'hover',
  },
  // Chromium prerenders the hovered page in full (Speculation Rules); other browsers prefetch.
  experimental: {
    clientPrerender: true,
  },
  compressHTML: true,
  build: {
    inlineStylesheets: 'always',   // one HTML response paints the page: no render-blocking CSS request
  },
  vite: {
    define: {
      __MEMBERS_ENABLED__: JSON.stringify(membersEnabled),
    },
  },
});
