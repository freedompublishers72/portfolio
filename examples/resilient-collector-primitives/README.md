# Resilient Collector Primitives

## What this demonstrates

Four small, production-grade reliability primitives for scheduled data
collection:

1. **Resumable offset pagination** — yields failures instead of throwing,
   so the caller decides whether to keep partial results.
2. **Interval pacing** — enforces a minimum wall-clock interval between
   operations with an injectable clock for testability.
3. **Bounded exponential backoff** — jittered backoff with `Retry-After`
   honoring and a documented override hook.
4. **Advisory run lock** — non-blocking `flock`-based single-instance lock
   that is kernel-released on crash (no stale locks, no permanent deadlock).

## The engineering problem

Scheduled collectors face several reliability challenges: paginated
endpoints that may fail mid-stream, rate limits that require pacing,
transient failures that warrant retry with backoff, and the risk of
overlapping runs when a scheduler fires before the previous run completes.

Each primitive addresses one concern in isolation, with minimal
dependencies and injectable seams for testing:

- The pacer accepts `sleep_fn` and `clock_fn` so tests run instantly.
- The backoff function accepts `retry_after` and `min_delay` parameters
  so the policy is testable without real HTTP responses.
- The run lock uses `flock` (kernel-managed) rather than a sentinel file,
  so a crashed process automatically releases the lock — no cleanup
  script needed.

## Important design decisions

- **Pagination yields failures, doesn't throw:** `iter_offset_pages` yields
  `(offset, None)` on failure, letting the caller decide whether to keep
  partial results or abort. This avoids losing already-collected data.
- **Pacer sleeps only the remaining interval:** if the caller's work took
  longer than the interval, `wait()` returns immediately — no unnecessary
  delay.
- **Backoff jitter ±25%:** `delay *= 0.75 + random() * 0.5` prevents
  thundering-herd retries when multiple collectors back off simultaneously.
- **Retry-After is capped:** a provider directing an unreasonably long
  `Retry-After` (e.g. 3600s) is capped at `RETRY_AFTER_MAX_SECONDS` so the
  run fails and the next scheduled cycle retries, rather than blocking
  indefinitely.
- **Non-blocking lock:** `try_acquire()` returns `False` instead of
  blocking, so a second run exits cleanly with a "skipped" result.

## How it differs from the original production context

The original primitives served a multi-source collection framework with
provider-specific rate-limit overrides and a collection specification
registry. This demonstration isolates the four primitives with no
dependency on the framework's specification registry, provider adapters,
or lifecycle manager. Internal work-package references, provider names,
and specific file paths in docstrings were removed. The engineering
behavior — pagination termination, pacing, backoff computation, and lock
semantics — is preserved verbatim.

Note: `run_lock.py` uses `fcntl.flock`, which is Unix-specific.

## Files

- `pagination.py` — resumable offset/limit pagination iterator
- `interval_pacer.py` — minimum-interval request pacer
- `backoff.py` — bounded exponential backoff with jitter
- `run_lock.py` — advisory `flock`-based single-instance lock
- `test_primitives.py` — tests for all four primitives

## Running the tests

```bash
cd examples/resilient-collector-primitives
python -m pytest test_primitives.py -v
```
