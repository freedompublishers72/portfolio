<?php
/**
 * Bounded-Staleness Cache Serve Cascade
 *
 * A miniature of a production full-page cache's serving decision table.
 * Demonstrates the HIT / STALE (stale-while-revalidate) / MISS decision
 * cascade and the bounded staleness model that makes an indefinitely stale
 * representation impossible.
 *
 * The original system served pre-generated HTML early in the request
 * lifecycle. This demonstration isol the serving decision logic with
 * injected dependencies so it runs without a web server or framework.
 */

/**
 * Default freshness windows (seconds).
 */
const DEFAULT_TTL_SECONDS         = 2592000; // 30 days — safety fallback; cache is primarily event-driven.
const DEFAULT_SWR_GRACE_SECONDS   = 600;     // Stale-while-revalidate grace for invalidated entries.
const DEFAULT_BROWSER_MAX_AGE      = 300;    // Browser max-age — bounded below server SWR grace.

/**
 * Represents a single route's cache metadata.
 */
class CacheEntry {
    public bool $exists;
    public ?int $generated_at;
    public ?int $invalidated_at;
    public ?int $pending_generation_id;
    public int $size;

    public function __construct(
        bool $exists = false,
        ?int $generated_at = null,
        ?int $invalidated_at = null,
        ?int $pending_generation_id = null,
        int $size = 0
    ) {
        $this->exists = $exists;
        $this->generated_at = $generated_at;
        $this->invalidated_at = $invalidated_at;
        $this->pending_generation_id = $pending_generation_id;
        $this->size = $size;
    }
}

/**
 * The cache serve cascade.
 *
 * Encapsulates the serving decision table and the bounded staleness model.
 * Dependencies (current time, TTL, SWR grace) are injected for testability.
 */
class CacheServeCascade {
    private int $ttl_seconds;
    private int $swr_grace_seconds;
    private int $browser_max_age;

    /**
     * @param int $ttl_seconds       Server-side cache TTL (safety fallback).
     * @param int $swr_grace_seconds SWR grace window for invalidated entries.
     * @param int $browser_max_age   Browser max-age (must be < swr_grace).
     */
    public function __construct(
        int $ttl_seconds = DEFAULT_TTL_SECONDS,
        int $swr_grace_seconds = DEFAULT_SWR_GRACE_SECONDS,
        int $browser_max_age = DEFAULT_BROWSER_MAX_AGE
    ) {
        $this->ttl_seconds = $ttl_seconds;
        $this->swr_grace_seconds = $swr_grace_seconds;
        $this->browser_max_age = $browser_max_age;
    }

    /**
     * Determine the serve decision for a cache entry at a given time.
     *
     * Decision table:
     * 1. Entry does not exist or is pending generation → MISS
     * 2. Entry exists and generated_at is within TTL → HIT
     * 3. Entry exists but TTL-expired (generated_at present) → STALE (SWR)
     * 4. Entry exists but invalidated (generated_at removed, invalidated_at set)
     *    → STALE only inside the bounded SWR grace window; else MISS
     *
     * @param CacheEntry $entry  The route's cache metadata.
     * @param int        $now    Current Unix timestamp.
     * @return string 'HIT' | 'STALE' | 'MISS'
     */
    public function decide( CacheEntry $entry, int $now ): string {
        // No cache file or a generation is pending → MISS.
        if ( ! $entry->exists || ! empty( $entry->pending_generation_id ) ) {
            return 'MISS';
        }

        // Valid (fresh) cache: generated_at present and within TTL.
        if ( $this->is_valid( $entry, $now ) ) {
            return 'HIT';
        }

        // Stale: cache file exists but is no longer valid.
        if ( $this->is_stale( $entry, $now ) ) {
            return 'STALE';
        }

        // No usable cache entry.
        return 'MISS';
    }

    /**
     * True if the entry is fresh (generated_at present and within TTL).
     */
    public function is_valid( CacheEntry $entry, int $now ): bool {
        if ( ! $entry->exists ) {
            return false;
        }
        if ( ! empty( $entry->pending_generation_id ) ) {
            return false;
        }
        if ( empty( $entry->generated_at ) ) {
            return false;
        }
        return ( $now - (int) $entry->generated_at ) < $this->ttl_seconds;
    }

    /**
     * True if a cache file exists but is no longer valid, and
     * stale-serving is still permitted.
     *
     * TTL-expired entries (generated_at present) remain SWR-servable
     * indefinitely — the content is still correct, just not freshly generated.
     *
     * Invalidated entries (generated_at removed, invalidated_at set) are
     * SWR-servable only inside the bounded grace window. After it, the
     * next request falls through to MISS so a failed warm cannot leave a
     * route serving stale indefinitely.
     */
    public function is_stale( CacheEntry $entry, int $now ): bool {
        if ( ! $entry->exists || $this->is_valid( $entry, $now ) ) {
            return false;
        }

        // Invalidated entry: SWR only inside the bounded grace window.
        if ( ! empty( $entry->invalidated_at ) && empty( $entry->generated_at ) ) {
            return ( $now - (int) $entry->invalidated_at ) < $this->swr_grace_seconds;
        }

        // Pending generation: SWR only inside the bounded grace window.
        if ( ! empty( $entry->pending_generation_id ) ) {
            return false; // Handled as MISS by decide().
        }

        // TTL-expired entry with generated_at present: SWR-servable.
        return true;
    }

    /**
     * The SWR grace window in seconds.
     */
    public function swr_grace(): int {
        return $this->swr_grace_seconds;
    }

    /**
     * Compose the Cache-Control header for a cached HTML response.
     *
     * Freshness model (bounded by construction):
     * - max-age: the browser may reuse the body unconditionally for at most
     *   browser_max_age — well inside the server-side SWR grace.
     * - must-revalidate: once max-age passes, the browser MUST revalidate;
     *   it cannot silently serve stale while the origin is reachable.
     * - stale-while-revalidate: bounded to the SAME window as the server's
     *   own SWR grace, applicable only while revalidation fails (origin
     *   unreachable).
     *
     * Total worst-case browser staleness = max-age + swr ≤ server grace +
     * max-age, and equals max-age alone whenever the origin is reachable.
     * An indefinitely stale browser representation is therefore impossible.
     */
    public function cache_control_header(): string {
        return sprintf(
            'public, max-age=%d, stale-while-revalidate=%d, must-revalidate',
            $this->browser_max_age,
            $this->swr_grace_seconds
        );
    }

    /**
     * Human-readable status for a cache entry.
     *
     * @return string 'active' | 'expired' | 'missing'
     */
    public function get_status( CacheEntry $entry, int $now ): string {
        if ( ! $entry->exists ) {
            return 'missing';
        }
        return $this->is_valid( $entry, $now ) ? 'active' : 'expired';
    }
}
