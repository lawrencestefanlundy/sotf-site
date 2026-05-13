// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  // Set to stateofthefuture.io once DNS is cut. For now the GH Pages default
  // works at https://lawrencestefanlundy.github.io/sotf-site/ — but we don't
  // want the /sotf-site/ base because we'll cut the domain straight to it.
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
