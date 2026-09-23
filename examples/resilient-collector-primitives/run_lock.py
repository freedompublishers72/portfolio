"""
Advisory single-instance run lock using ``flock``.

Prevents overlapping scheduled runs using an advisory file lock. This
protects long-running cleanup or collection tasks from concurrent
execution.

Design properties:

- **Non-blocking:** A second process does not wait; it exits with a
  "skipped" result instead of running concurrently.
- **No permanent deadlock:** ``flock`` locks are kernel-managed and are
  automatically released when the holding process exits — including
  crashes and SIGKILL. A lock file left on disk is therefore never
  "stale" in the blocking sense: an orphaned file without a live holder
  does not block.
- **Deterministic:** Same lock path for the same task, regardless of which
  entry point (CLI, cron, tests) starts the run.

Note: ``fcntl.flock`` is Unix-specific; on other platforms this primitive
is not available.
"""

from __future__ import annotations

import fcntl
import os
from pathlib import Path
from typing import Optional


class RunLock:
    """Advisory ``flock``-based lock for single-instance scheduled runs.

    Usage::

        lock = RunLock(path)
        if lock.try_acquire():
            try:
                ... run task ...
            finally:
                lock.release()
        else:
            ... report skipped ...
    """

    def __init__(self, lock_path: str | Path) -> None:
        self.lock_path = Path(lock_path)
        self._fd: Optional[int] = None

    @property
    def is_held(self) -> bool:
        return self._fd is not None

    def try_acquire(self) -> bool:
        """Try to acquire the lock without blocking.

        Returns True if the lock was acquired, False if another process
        currently holds it.
        """
        if self._fd is not None:
            # Already held by this instance.
            return True

        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(str(self.lock_path), os.O_CREAT | os.O_RDWR, 0o644)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except (BlockingIOError, OSError):
            os.close(fd)
            return False
        self._fd = fd
        return True

    def release(self) -> None:
        """Release the lock if held."""
        if self._fd is None:
            return
        fd, self._fd = self._fd, None
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        except OSError:
            pass
        try:
            os.close(fd)
        except OSError:
            pass

    def __enter__(self) -> "RunLock":
        if not self.try_acquire():
            raise BlockingIOError(
                f"run lock already held: {self.lock_path}"
            )
        return self

    def __exit__(self, *exc: object) -> None:
        self.release()

    def __del__(self) -> None:  # pragma: no cover - best-effort safety
        self.release()
