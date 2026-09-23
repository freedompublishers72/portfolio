# Bounded-Staleness Cache Serve Cascade

## What this demonstrates

The serving decision table of a production full-page cache: the cascade
that decides whether a request receives a **HIT** (fresh cache), **STALE**
(stale-while-revalidate), or **MISS** (no usable cache). It also encodes
the bounded staleness model that makes an indefinitely stale representation
impossible.

## The engineering problem

A full-page cache must answer one question per request: serve cached, serve
stale, or render live? The answer depends on multiple factors:

- Does a cache file exist?
- Is it still within its TTL?
- Was it invalidated (content changed) and if so, how long ago?
- Is a background regeneration already pending?

The subtlety is in the **stale-while-revalidate** path. An invalidated cache
entry should serve stale content *temporarily* while a background warm
regenerates it — but if the warm fails or never executes, the route must
not serve stale content forever. The bounded SWR grace window solves this:
after the grace window expires, `is_stale()` returns false and the next
request falls through to MISS, forcing a live render.

The `Cache-Control` header must also be bounded by construction:
`max-age` + `stale-while-revalidate` must not exceed a finite, known bound
so a browser can never hold an indefinitely stale representation.

## Important design decisions

- **TTL-expired vs. invalidated distinction:** a TTL-expired entry
  (generated_at present) is SWR-servable indefinitely — the content is
  still correct, just not freshly generated. An invalidated entry
  (generated_at removed, invalidated_at set) is SWR-servable only inside
  the bounded grace window. This asymmetry prevents a failed warm from
  leaving a route stale forever while still allowing TTL-expired content
  to serve during background regeneration.
- **Pending generation → MISS:** if a background generation is already
  pending, the entry is neither valid nor stale — it is MISS, so the
  request renders live rather than serving content that is about to be
  replaced.
- **Browser max-age < server SWR grace:** the browser's `max-age` is
  deliberately shorter than the server's SWR grace so browser caching
  cannot outlive server-side staleness. Combined with `must-revalidate`,
  the worst-case browser staleness is `max-age + swr` — a finite, bounded
  value.
- **Injected time:** the `decide()` method accepts `$now` as a parameter,
  making the entire cascade deterministic and testable without real time.

## How it differs from the original production context

The original cache engine was a WordPress plugin class with ~2000 lines
handling cache storage, atomic writes, capture locking, invalidation
hooks, asset fingerprinting, domain-mismatch detection, and WordPress
conditional exclusions. This demonstration isolates the serving decision
logic and the bounded staleness model into a ~200-line miniature with
injected dependencies (time, TTL, grace window). WordPress-specific calls,
private domain references, plugin headers, and operational identifiers
were removed. The decision table — HIT / STALE / MISS — and the freshness
model derivation are preserved faithfully.

## Files

- `cache_serve_cascade.php` — the decision cascade and freshness model
- `test_cache_serve_cascade.php` — tests for HIT/STALE/MISS decisions and bounded staleness

## Running the tests

```bash
cd examples/bounded-staleness-cache
php test_cache_serve_cascade.php
```
