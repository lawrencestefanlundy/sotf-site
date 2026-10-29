/// <reference types="@cloudflare/workers-types" />

declare namespace App {
  interface Locals {
    /** Set by middleware on /members, /signin, /auth and /api routes. */
    member: { email: string } | null;
  }
}

/** Build-time flag from astro.config.mjs (MEMBERS_ENABLED=1): shows the nav link and teasers. */
declare const __MEMBERS_ENABLED__: boolean;
