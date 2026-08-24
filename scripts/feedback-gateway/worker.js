/**
 * Cloudflare Worker: receive digest feedback from GitHub Pages and
 * trigger repository_dispatch on the Horizon repo.
 *
 * Required secrets (wrangler secret put):
 *   GITHUB_TOKEN  — fine-grained PAT with Contents + Actions dispatch
 *   GITHUB_REPO   — e.g. Yancy-gate/Horizon
 *   ALLOWED_ORIGINS — comma-separated, e.g. https://thysrael.github.io,http://localhost:4000
 */

const CORS_HEADERS = {
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const allowed = (env.ALLOWED_ORIGINS || "")
      .split(",")
      .map((value) => value.trim())
      .filter(Boolean);

    if (request.method === "OPTIONS") {
      if (origin && allowed.includes(origin)) {
        return new Response(null, {
          status: 204,
          headers: { ...CORS_HEADERS, "Access-Control-Allow-Origin": origin },
        });
      }
      return new Response(null, { status: 403 });
    }

    if (request.method !== "POST") {
      return new Response("Horizon feedback gateway", { status: 200 });
    }

    if (!origin || !allowed.includes(origin)) {
      return new Response(JSON.stringify({ error: "forbidden origin" }), {
        status: 403,
        headers: { "Content-Type": "application/json" },
      });
    }

    let entry;
    try {
      entry = await request.json();
    } catch {
      return new Response(JSON.stringify({ error: "invalid json" }), {
        status: 400,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": origin },
      });
    }

    if (!entry || !entry.url || !entry.rating) {
      return new Response(JSON.stringify({ error: "missing url or rating" }), {
        status: 400,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": origin },
      });
    }

    const dispatch = await fetch(
      `https://api.github.com/repos/${env.GITHUB_REPO}/dispatches`,
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${env.GITHUB_TOKEN}`,
          Accept: "application/vnd.github+json",
          "Content-Type": "application/json",
          "User-Agent": "horizon-feedback-gateway",
        },
        body: JSON.stringify({
          event_type: "horizon-feedback",
          client_payload: { entry },
        }),
      }
    );

    if (!dispatch.ok) {
      const detail = await dispatch.text();
      return new Response(JSON.stringify({ error: "dispatch failed", detail }), {
        status: 502,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": origin },
      });
    }

    return new Response(JSON.stringify({ ok: true }), {
      status: 200,
      headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": origin },
    });
  },
};
