// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  // Live at the custom domain. public/CNAME pins stateofthefuture.io; internal
  // links resolve from root (no `base`). To revert to the github.io preview:
  // set `site` back to https://lawrencestefanlundy.github.io, add base:'/sotf-site',
  // and remove public/CNAME.
  site: 'https://stateofthefuture.io',

  prefetch: {
    prefetchAll: true,
    defaultStrategy: 'viewport',
  },
  compressHTML: true,
  build: {
    inlineStylesheets: 'auto',
  },
});
