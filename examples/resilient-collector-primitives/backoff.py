"""
Bounded exponential backoff with jitter and Retry-After honoring.

Centralizes the backoff computation so every collector shares one policy.
Callers still own their request/retry loops.

Policy:
  * bounded exponential backoff beginning at 0.5s, capped at 30s, with
    ±25% jitter;
  * honor provider ``Retry-After`` headers up to a configurable maximum;
  * a ``min_delay`` hook for documented source-specific overrides;
  * transient HTTP status codes are eligible for retry; everything else
    fails fast (the caller decides which statuses are transient).
"""

from __future__ import annotations

import random
from typing import Optional

BACKOFF_BASE_SECONDS = 0.5
BACKOFF_CAP_SECONDS = 30.0
# Provider Retry-After is honored up to this bound; larger values abort the
# run so the failure is recorded and the next scheduled cycle retries.
RETRY_AFTER_MAX_SECONDS = 120.0

# Transient HTTP statuses eligible for retry (everything else fails fast).
TRANSIENT_HTTP_CODES = frozenset({408, 425, 429, 500, 502, 503, 504})


def compute_backoff(attempt: int,
                    base: float = BACKOFF_BASE_SECONDS,
                    cap: float = BACKOFF_CAP_SECONDS,
                    retry_after: Optional[float] = None,
                    min_delay: Optional[float] = None) -> float:
    """Backoff seconds before the next attempt (``attempt`` is 0-based).

    ``min_delay`` is the documented source-specific override hook.
    ``retry_after`` sets a provider-directed floor, honored up to
    ``RETRY_AFTER_MAX_SECONDS``.
    """
    delay = min(base * (2 ** attempt), cap)
    delay *= 0.75 + random.random() * 0.5  # jitter ±25%
    if min_delay is not None:
        delay = max(delay, min_delay)
    if retry_after:
        delay = max(delay, min(retry_after, RETRY_AFTER_MAX_SECONDS))
    return delay


def retry_after_seconds(headers) -> Optional[float]:
    """Extract ``Retry-After`` seconds from an HTTP response header map."""
    if headers is None:
        return None
    raw = headers.get("Retry-After") or headers.get("retry-after")
    if raw is None:
        return None
    try:
        return float(str(raw).strip())
    except (TypeError, ValueError):
        return None
