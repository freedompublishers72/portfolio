"""Tests for resilient collector primitives — pagination, pacing, backoff, locking."""

import os
import tempfile
from pathlib import Path

import pytest

from pagination import iter_offset_pages
from interval_pacer import IntervalLimiter
from backoff import (
    BACKOFF_BASE_SECONDS,
    BACKOFF_CAP_SECONDS,
    RETRY_AFTER_MAX_SECONDS,
    TRANSIENT_HTTP_CODES,
    compute_backoff,
    retry_after_seconds,
)
from run_lock import RunLock


# ---------------------------------------------------------------------------
# Pagination
# ---------------------------------------------------------------------------

class TestPagination:
    def test_yields_all_pages(self):
        pages = [
            {"results": [1, 2, 3]},
            {"results": [4, 5]},
            {"results": []},
        ]
        calls = []

        def fetch(offset, size):
            calls.append((offset, size))
            return pages.pop(0)

        result = list(iter_offset_pages(fetch, page_size=3))
        assert len(result) == 3
        assert result[0] == (0, {"results": [1, 2, 3]})
        assert result[1] == (3, {"results": [4, 5]})
        assert result[2] == (6, {"results": []})
        assert calls == [(0, 3), (3, 3), (6, 3)]

    def test_stops_on_empty_results(self):
        pages = [{"results": [1]}, {"results": []}]
        result = list(iter_offset_pages(lambda o, s: pages.pop(0), page_size=1))
        assert len(result) == 2

    def test_stops_on_none_failure(self):
        pages = [{"results": [1]}, None]
        result = list(iter_offset_pages(lambda o, s: pages.pop(0), page_size=1))
        assert len(result) == 2
        assert result[1] == (1, None)

    def test_respects_total(self):
        pages = [{"results": [1]}, {"results": [2]}, {"results": [3]}]
        result = list(iter_offset_pages(
            lambda o, s: pages.pop(0), page_size=1, total=2
        ))
        assert len(result) == 2

    def test_respects_max_pages(self):
        pages = [{"results": [1]}, {"results": [2]}, {"results": [3]}]
        result = list(iter_offset_pages(
            lambda o, s: pages.pop(0), page_size=1, max_pages=2
        ))
        assert len(result) == 2

    def test_start_offset(self):
        pages = [{"results": [5, 6]}, {"results": []}]
        result = list(iter_offset_pages(
            lambda o, s: pages.pop(0), page_size=2, start_offset=4
        ))
        assert result[0][0] == 4

    def test_limiter_called_between_pages(self):
        waits = []

        class FakeLimiter:
            def wait(self):
                waits.append(True)

        pages = [{"results": [1]}, {"results": [2]}, {"results": []}]
        list(iter_offset_pages(
            lambda o, s: pages.pop(0), page_size=1, limiter=FakeLimiter()
        ))
        # limiter.wait() called after page 0 and page 1, but not after the
        # last (empty) page because iter returns before calling wait.
        assert len(waits) == 2


# ---------------------------------------------------------------------------
# Interval pacer
# ---------------------------------------------------------------------------

class TestIntervalLimiter:
    def test_rejects_negative_interval(self):
        with pytest.raises(ValueError):
            IntervalLimiter(-1)

    def test_first_wait_no_sleep(self):
        clock_values = [100.0]
        sleeps = []

        def clock():
            return clock_values[0]

        limiter = IntervalLimiter(5.0, sleep_fn=sleeps.append, clock_fn=clock)
        slept = limiter.wait()
        assert slept == 0.0
        assert sleeps == []

    def test_sleeps_remaining_interval(self):
        clock_values = [100.0, 102.0, 102.0]
        sleeps = []
        clock_iter = iter(clock_values)

        limiter = IntervalLimiter(5.0, sleep_fn=sleeps.append, clock_fn=lambda: next(clock_iter))
        limiter.wait()  # first call, no sleep
        slept = limiter.wait()  # 2s elapsed, 3s remaining
        assert slept == 3.0
        assert sleeps == [3.0]

    def test_no_sleep_if_interval_elapsed(self):
        clock_values = [100.0, 110.0]
        sleeps = []
        clock_iter = iter(clock_values)

        limiter = IntervalLimiter(5.0, sleep_fn=sleeps.append, clock_fn=lambda: next(clock_iter))
        limiter.wait()
        slept = limiter.wait()  # 10s elapsed > 5s interval
        assert slept == 0.0
        assert sleeps == []

    def test_last_permitted_at(self):
        clock_values = [100.0]
        clock_iter = iter(clock_values)
        limiter = IntervalLimiter(5.0, sleep_fn=lambda x: None, clock_fn=lambda: next(clock_iter))
        assert limiter.last_permitted_at is None
        limiter.wait()
        assert limiter.last_permitted_at is not None


# ---------------------------------------------------------------------------
# Backoff
# ---------------------------------------------------------------------------

class TestComputeBackoff:
    def test_base_at_attempt_zero(self):
        # With jitter, delay is in [base * 0.75, base * 1.25]
        for _ in range(100):
            delay = compute_backoff(0)
            assert BACKOFF_BASE_SECONDS * 0.75 <= delay <= BACKOFF_BASE_SECONDS * 1.25

    def test_exponential_growth(self):
        # attempt 3: base * 2^3 = 4.0, with jitter [3.0, 5.0]
        for _ in range(100):
            delay = compute_backoff(3)
            assert 3.0 <= delay <= 5.0

    def test_capped_at_max(self):
        for _ in range(100):
            delay = compute_backoff(100)
            assert delay <= BACKOFF_CAP_SECONDS * 1.25

    def test_min_delay_override(self):
        for _ in range(100):
            delay = compute_backoff(0, min_delay=10.0)
            assert delay >= 10.0

    def test_retry_after_honored(self):
        for _ in range(100):
            delay = compute_backoff(0, retry_after=20.0)
            assert delay >= 20.0

    def test_retry_after_capped(self):
        delay = compute_backoff(0, retry_after=999.0)
        assert delay >= RETRY_AFTER_MAX_SECONDS

    def test_jitter_is_nondeterministic(self):
        delays = {compute_backoff(5) for _ in range(50)}
        # With jitter, we should get many different values
        assert len(delays) > 10


class TestRetryAfterSeconds:
    def test_standard_header(self):
        assert retry_after_seconds({"Retry-After": "30"}) == 30.0

    def test_lowercase_header(self):
        assert retry_after_seconds({"retry-after": "15"}) == 15.0

    def test_none_headers(self):
        assert retry_after_seconds(None) is None

    def test_missing_header(self):
        assert retry_after_seconds({"Content-Type": "text/html"}) is None

    def test_invalid_value(self):
        assert retry_after_seconds({"Retry-After": "not-a-number"}) is None


class TestTransientCodes:
    def test_known_transient_codes(self):
        assert 429 in TRANSIENT_HTTP_CODES
        assert 503 in TRANSIENT_HTTP_CODES
        assert 500 in TRANSIENT_HTTP_CODES
        assert 502 in TRANSIENT_HTTP_CODES
        assert 504 in TRANSIENT_HTTP_CODES
        assert 408 in TRANSIENT_HTTP_CODES

    def test_non_transient_not_included(self):
        assert 200 not in TRANSIENT_HTTP_CODES
        assert 404 not in TRANSIENT_HTTP_CODES
        assert 401 not in TRANSIENT_HTTP_CODES


# ---------------------------------------------------------------------------
# Run lock
# ---------------------------------------------------------------------------

class TestRunLock:
    def test_acquire_and_release(self, tmp_path):
        lock_path = tmp_path / "test.lock"
        lock = RunLock(lock_path)
        assert not lock.is_held
        assert lock.try_acquire() is True
        assert lock.is_held
        lock.release()
        assert not lock.is_held

    def test_second_instance_cannot_acquire(self, tmp_path):
        lock_path = tmp_path / "test.lock"
        lock1 = RunLock(lock_path)
        lock2 = RunLock(lock_path)
        assert lock1.try_acquire() is True
        assert lock2.try_acquire() is False
        lock1.release()
        # After release, lock2 can acquire
        assert lock2.try_acquire() is True
        lock2.release()

    def test_re_acquire_same_instance(self, tmp_path):
        lock_path = tmp_path / "test.lock"
        lock = RunLock(lock_path)
        assert lock.try_acquire() is True
        # Already held by this instance
        assert lock.try_acquire() is True
        lock.release()

    def test_context_manager_acquires(self, tmp_path):
        lock_path = tmp_path / "test.lock"
        with RunLock(lock_path) as lock:
            assert lock.is_held
        assert not lock.is_held

    def test_context_manager_raises_if_locked(self, tmp_path):
        lock_path = tmp_path / "test.lock"
        lock1 = RunLock(lock_path)
        lock1.try_acquire()
        with pytest.raises(BlockingIOError):
            with RunLock(lock_path):
                pass
        lock1.release()

    def test_creates_parent_directory(self, tmp_path):
        lock_path = tmp_path / "subdir" / "nested" / "test.lock"
        lock = RunLock(lock_path)
        assert lock.try_acquire() is True
        assert lock_path.parent.exists()
        lock.release()

    def test_release_idempotent(self, tmp_path):
        lock_path = tmp_path / "test.lock"
        lock = RunLock(lock_path)
        lock.try_acquire()
        lock.release()
        lock.release()  # should not raise
