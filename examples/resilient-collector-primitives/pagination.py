"""
Resumable offset/limit pagination.

``iter_offset_pages`` yields ``(offset, page)`` tuples. Iteration stops when
the endpoint reports the result set is exhausted, a page returns no
results, the page cap is reached, or ``fetch_page`` fails — in which case
the failure is yielded as ``(offset, None)`` so the caller decides whether
to keep partial results. A ``limiter`` (any object with ``wait()``) paces
requests between pages.
"""

from __future__ import annotations

from typing import Any, Callable, Iterator, Optional


def iter_offset_pages(fetch_page: Callable[[int, int], Optional[dict]],
                      page_size: int,
                      *,
                      max_pages: Optional[int] = None,
                      total: Optional[int] = None,
                      limiter: Any = None,
                      start_offset: int = 0,
                      ) -> Iterator[tuple[int, Optional[dict]]]:
    """Yield ``(offset, page)`` for an offset/limit-paginated endpoint.

    ``fetch_page(offset, page_size)`` returns the parsed page dict or
    ``None`` on failure. ``total`` may be supplied by the caller (e.g.
    from a first response's ``count``); when omitted, iteration relies on
    empty-page termination. ``start_offset`` supports resuming after a
    caller-fetched first page. Pages after the first are paced by
    ``limiter.wait()`` when a limiter is provided.
    """
    offset = start_offset
    pages = 0
    while True:
        if max_pages is not None and pages >= max_pages:
            return
        if total is not None and offset >= total:
            return
        page = fetch_page(offset, page_size)
        yield offset, page
        if page is None:
            return
        results = page.get("results") if isinstance(page, dict) else None
        if results is not None and not results:
            return
        offset += page_size
        pages += 1
        if limiter is not None:
            limiter.wait()
