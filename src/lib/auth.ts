/**
 * Member sessions and magic-link tokens.
 *
 * A session is a signed cookie, not a server-side record: `{email, exp, verified}`
 * as base64url JSON with an HMAC-SHA256 tag. The Worker can check it on every
 * request with one WebCrypto call and no KV read. `verified` is when the Stripe
 * subscription was last confirmed; middleware re-checks once a day so a lapsed
 * subscriber loses access within 24 h without anyone revoking anything.
 */
import type { AstroCookies } from "astro";

export const SESSION_COOKIE = "sotf_member";
export const SESSION_TTL_S = 30 * 24 * 3600;      // cookie lifetime
export const REVERIFY_AFTER_S = 24 * 3600;        // re-check Stripe after this
export const MAGIC_LINK_TTL_S = 15 * 60;

export type Session = { email: string; exp: number; verified: number };

const enc = new TextEncoder();

function b64url(bytes: ArrayBuffer | Uint8Array): string {
  const arr = bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes);
  let s = "";
  for (const b of arr) s += String.fromCharCode(b);
  return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

function unb64url(s: string): Uint8Array {
  const pad = s.length % 4 === 0 ? "" : "=".repeat(4 - (s.length % 4));
  const bin = atob(s.replace(/-/g, "+").replace(/_/g, "/") + pad);
  return Uint8Array.from(bin, (c) => c.charCodeAt(0));
}

async function hmacKey(secret: string): Promise<CryptoKey> {
  return crypto.subtle.importKey("raw", enc.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign", "verify"]);
}

export async function signSession(session: Session, secret: string): Promise<string> {
  const payload = b64url(enc.encode(JSON.stringify(session)));
  const sig = await crypto.subtle.sign("HMAC", await hmacKey(secret), enc.encode(payload));
  return `${payload}.${b64url(sig)}`;
}

/** Null when the cookie is missing, tampered with, malformed or expired. */
export async function readSession(value: string | undefined, secret: string | undefined): Promise<Session | null> {
  if (!value || !secret) return null;
  const dot = value.lastIndexOf(".");
  if (dot < 1) return null;
  const payload = value.slice(0, dot);
  const sig = value.slice(dot + 1);
  try {
    // subtle.verify is constant-time; never compare the tag as a string.
    const ok = await crypto.subtle.verify("HMAC", await hmacKey(secret), unb64url(sig), enc.encode(payload));
    if (!ok) return null;
    const s = JSON.parse(new TextDecoder().decode(unb64url(payload))) as Session;
    if (typeof s.email !== "string" || typeof s.exp !== "number" || typeof s.verified !== "number") return null;
    if (s.exp * 1000 < Date.now()) return null;
    return s;
  } catch {
    return null;
  }
}

export async function setSessionCookie(cookies: AstroCookies, email: string, secret: string): Promise<void> {
  const now = Math.floor(Date.now() / 1000);
  const value = await signSession({ email, exp: now + SESSION_TTL_S, verified: now }, secret);
  cookies.set(SESSION_COOKIE, value, {
    httpOnly: true,
    secure: true,
    sameSite: "lax",
    path: "/",
    maxAge: SESSION_TTL_S,
  });
}

export function clearSessionCookie(cookies: AstroCookies): void {
  cookies.delete(SESSION_COOKIE, { path: "/" });
}

/** 256 bits of randomness, URL-safe: the magic-link token and the KV key. */
export function randomToken(): string {
  const bytes = new Uint8Array(32);
  crypto.getRandomValues(bytes);
  return b64url(bytes);
}

export function normaliseEmail(raw: unknown): string | null {
  if (typeof raw !== "string") return null;
  const email = raw.trim().toLowerCase();
  // Deliberately loose: the real test is whether Stripe knows the address.
  if (email.length > 254 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return null;
  return email;
}

/** Only ever redirect within the site: a relative path, never a second host. */
export function safeNext(raw: string | null | undefined, fallback = "/members/"): string {
  if (!raw || !raw.startsWith("/") || raw.startsWith("//") || raw.includes("\\")) return fallback;
  return raw;
}
