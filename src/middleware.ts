/**
 * The paywall. Public pages are prerendered and never reach this at request time;
 * only the on-demand routes (/members, /signin, /auth, /api) do.
 *
 *  - reads + verifies the session cookie
 *  - once a day, re-checks the subscription with Stripe and either refreshes the
 *    cookie or drops it (lapsed subscriber → back to the sign-in page)
 *  - redirects anonymous requests for member content to /signin
 *  - marks every one of these responses private/no-store so no CDN or browser
 *    cache can hand a paid page to the next visitor
 */
import { defineMiddleware } from "astro:middleware";
import { getEnv } from "./env";
import { REVERIFY_AFTER_S, SESSION_COOKIE, clearSessionCookie, readSession, setSessionCookie } from "./lib/auth";
import { checkEntitlement } from "./lib/stripe";

const PRIVATE_ROUTE = /^\/(members|signin|auth|api)(\/|$)/;
// /members/ itself is the landing page (sign in / what's inside); anything deeper is paid.
const GATED_ROUTE = /^\/members\/.+/;

export const onRequest = defineMiddleware(async (context, next) => {
  const path = context.url.pathname;
  if (!PRIVATE_ROUTE.test(path)) return next();

  const env = getEnv();
  let session = await readSession(context.cookies.get(SESSION_COOKIE)?.value, env.SESSION_SECRET);

  if (session && Date.now() / 1000 - session.verified > REVERIFY_AFTER_S) {
    const ent = await checkEntitlement(session.email, env);
    if (ent.active) {
      await setSessionCookie(context.cookies, session.email, env.SESSION_SECRET);
    } else if (ent.reason !== "error") {
      // Confirmed lapsed. (A Stripe outage keeps the existing cookie for now.)
      clearSessionCookie(context.cookies);
      session = null;
    }
  }

  context.locals.member = session ? { email: session.email } : null;

  if (GATED_ROUTE.test(path) && !session) {
    return context.redirect(`/signin/?next=${encodeURIComponent(path)}`, 302);
  }

  const response = await next();
  response.headers.set("Cache-Control", "private, no-store");
  response.headers.set("X-Robots-Tag", "noindex");
  return response;
});
