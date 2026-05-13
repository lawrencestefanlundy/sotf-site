// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  // Preview lives at https://lawrencestefanlundy.github.io/sotf-site/ until DNS
  // is cut to stateofthefuture.io. Toggling `base` so internal links resolve
  // under the /sotf-site/ subpath. After DNS cutover: remove `base`, change
  // `site` to https://stateofthefuture.io, restore public/CNAME, rebuild.
  site: 'https://lawrencestefanlundy.github.io',
  base: '/sotf-site',

  prefetch: {
    prefetchAll: true,
    defaultStrategy: 'viewport',
  },
  compressHTML: true,
  build: {
    inlineStylesheets: 'auto',
  },
});
