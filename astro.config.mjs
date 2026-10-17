// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  // Live at the custom domain. public/CNAME pins stateofthefuture.io; internal
  // links resolve from root (no `base`). To revert to the github.io preview:
  // set `site` back to https://lawrencestefanlundy.github.io, add base:'/sotf-site',
  // and remove public/CNAME.
  site: 'https://stateofthefuture.io',

  integrations: [sitemap()],

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
});
