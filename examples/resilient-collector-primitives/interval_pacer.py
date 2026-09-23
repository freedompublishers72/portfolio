"""
Minimum-interval request pacing.

``IntervalLimiter`` enforces a minimum wall-clock interval between
operations — the common pacing primitive for collectors that page through
an external API. It is intentionally simple: per-source token buckets,
daily budgets, and concurrency caps are higher-level concerns that layer
on top.

An injectable ``sleep_fn`` and ``clock_fn`` make the pacer fully testable
without real time delays.
"""

from __future__ import annotations

import time
from typing import Callable


class IntervalLimiter:
    """Minimum-interval pacer.

    ``wait()`` sleeps only the remaining time since the last permitted
    operation, so callers that already take longer than the interval are
    never delayed further.
    """

    def __init__(self, min_interval_seconds: float,
                 *,
                 sleep_fn: Callable[[float], None] = time.sleep,
                 clock_fn: Callable[[], float] = time.monotonic) -> None:
        if min_interval_seconds < 0:
            raise ValueError("min_interval_seconds must be >= 0")
        self.min_interval = float(min_interval_seconds)
        self._sleep = sleep_fn
        self._clock = clock_fn
        self._last: float | None = None

    def wait(self) -> float:
        """Block until the interval has elapsed; returns the slept seconds."""
        now = self._clock()
        slept = 0.0
        if self._last is not None:
            remaining = self.min_interval - (now - self._last)
            if remaining > 0:
                self._sleep(remaining)
                slept = remaining
                now = self._clock()
        self._last = now
        return slept

    @property
    def last_permitted_at(self) -> float | None:
        return self._last
