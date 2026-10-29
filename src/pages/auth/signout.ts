export const prerender = false;

import type { APIRoute } from "astro";
import { clearSessionCookie } from "../../lib/auth";

const signout: APIRoute = ({ cookies, redirect }) => {
  clearSessionCookie(cookies);
  return redirect("/", 303);
};

export const GET = signout;
export const POST = signout;
