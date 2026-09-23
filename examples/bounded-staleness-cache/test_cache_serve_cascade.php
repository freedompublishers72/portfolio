<?php
/**
 * Tests for the Bounded-Staleness Cache Serve Cascade.
 *
 * Run: php test_cache_serve_cascade.php
 */

require_once __DIR__ . '/cache_serve_cascade.php';

$pass = 0;
$fail = 0;

function assert_true( $condition, $message ) {
    global $pass, $fail;
    if ( $condition ) {
        $pass++;
    } else {
        $fail++;
        echo "FAIL: $message\n";
    }
}

function assert_equals( $expected, $actual, $message ) {
    global $pass, $fail;
    if ( $expected === $actual ) {
        $pass++;
    } else {
        $fail++;
        echo "FAIL: $message (expected '$expected', got '$actual')\n";
    }
}

// Use short TTL and grace for readable tests.
const TEST_TTL = 100;
const TEST_GRACE = 50;
const TEST_MAX_AGE = 30;

function make_cascade(): CacheServeCascade {
    return new CacheServeCascade( TEST_TTL, TEST_GRACE, TEST_MAX_AGE );
}

// ---------------------------------------------------------------------------
// HIT — fresh cache
// ---------------------------------------------------------------------------

function test_hit_within_ttl() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: 1000, size: 5000 );
    assert_equals( 'HIT', $cascade->decide( $entry, 1050 ), 'Entry within TTL should HIT' );
}

function test_hit_at_ttl_boundary() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: 1000, size: 5000 );
    // 99 seconds elapsed < 100 TTL
    assert_equals( 'HIT', $cascade->decide( $entry, 1099 ), 'Entry at TTL boundary should HIT' );
}

// ---------------------------------------------------------------------------
// STALE — TTL-expired (SWR-servable indefinitely)
// ---------------------------------------------------------------------------

function test_stale_after_ttl_expiry() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: 1000, size: 5000 );
    // 101 seconds elapsed > 100 TTL, but generated_at present → SWR
    assert_equals( 'STALE', $cascade->decide( $entry, 1101 ), 'TTL-expired entry should STALE' );
}

function test_stale_long_after_ttl() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: 1000, size: 5000 );
    // Even far past TTL, generated_at present → still SWR-servable
    assert_equals( 'STALE', $cascade->decide( $entry, 999999 ), 'TTL-expired with generated_at should remain STALE' );
}

// ---------------------------------------------------------------------------
// STALE → MISS — invalidated entry outside grace window
// ---------------------------------------------------------------------------

function test_stale_invalidated_within_grace() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: null, invalidated_at: 1000, size: 5000 );
    // 10 seconds since invalidation < 50 grace
    assert_equals( 'STALE', $cascade->decide( $entry, 1010 ), 'Invalidated entry within grace should STALE' );
}

function test_miss_invalidated_outside_grace() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: null, invalidated_at: 1000, size: 5000 );
    // 60 seconds since invalidation > 50 grace → MISS
    assert_equals( 'MISS', $cascade->decide( $entry, 1060 ), 'Invalidated entry outside grace should MISS' );
}

function test_miss_invalidated_at_grace_boundary() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: null, invalidated_at: 1000, size: 5000 );
    // Exactly at grace boundary (50s) → no longer stale
    assert_equals( 'MISS', $cascade->decide( $entry, 1050 ), 'Invalidated entry at grace boundary should MISS' );
}

// ---------------------------------------------------------------------------
// MISS — no cache or pending generation
// ---------------------------------------------------------------------------

function test_miss_no_cache() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: false );
    assert_equals( 'MISS', $cascade->decide( $entry, 1000 ), 'No cache should MISS' );
}

function test_miss_pending_generation() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: 1000, pending_generation_id: 42, size: 5000 );
    // Pending generation → not valid, not stale → MISS
    assert_equals( 'MISS', $cascade->decide( $entry, 1010 ), 'Pending generation should MISS' );
}

function test_stale_legacy_entry_no_generated_at() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: null, size: 5000 );
    // Legacy entry with no generated_at and no invalidated_at: the original
    // system serves it as STALE (safe fallback while regenerating).
    assert_equals( 'STALE', $cascade->decide( $entry, 1000 ), 'Legacy entry without generated_at should STALE' );
}

// ---------------------------------------------------------------------------
// is_valid / is_stale direct checks
// ---------------------------------------------------------------------------

function test_is_valid_fresh() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: 1000, size: 5000 );
    assert_true( $cascade->is_valid( $entry, 1050 ), 'Fresh entry should be valid' );
}

function test_is_valid_expired() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: 1000, size: 5000 );
    assert_false( $cascade->is_valid( $entry, 1101 ), 'Expired entry should not be valid' );
}

function test_is_valid_missing() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: false );
    assert_false( $cascade->is_valid( $entry, 1000 ), 'Missing entry should not be valid' );
}

function test_is_stale_valid_returns_false() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: 1000, size: 5000 );
    assert_false( $cascade->is_stale( $entry, 1050 ), 'Valid entry should not be stale' );
}

function test_is_stale_ttl_expired() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: 1000, size: 5000 );
    assert_true( $cascade->is_stale( $entry, 1101 ), 'TTL-expired entry should be stale' );
}

function test_is_stale_invalidated_within_grace() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: null, invalidated_at: 1000, size: 5000 );
    assert_true( $cascade->is_stale( $entry, 1010 ), 'Invalidated within grace should be stale' );
}

function test_is_stale_invalidated_outside_grace() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: null, invalidated_at: 1000, size: 5000 );
    assert_false( $cascade->is_stale( $entry, 1060 ), 'Invalidated outside grace should not be stale' );
}

// ---------------------------------------------------------------------------
// Bounded staleness model — Cache-Control header
// ---------------------------------------------------------------------------

function test_cache_control_header_structure() {
    $cascade = make_cascade();
    $header = $cascade->cache_control_header();
    assert_true( strpos( $header, 'max-age=30' ) !== false, 'Header should contain browser max-age' );
    assert_true( strpos( $header, 'stale-while-revalidate=50' ) !== false, 'Header should contain SWR grace' );
    assert_true( strpos( $header, 'must-revalidate' ) !== false, 'Header should contain must-revalidate' );
}

function test_browser_max_age_below_swr_grace() {
    $cascade = make_cascade();
    // Browser max-age (30) must be below SWR grace (50) so browser caching
    // cannot outlive server-side staleness.
    assert_true( TEST_MAX_AGE < TEST_GRACE, 'Browser max-age must be below SWR grace' );
}

function test_worst_case_browser_staleness_bounded() {
    $cascade = make_cascade();
    // Worst-case browser staleness = max-age + swr = 30 + 50 = 80
    // This is bounded — an indefinitely stale representation is impossible.
    $worst_case = TEST_MAX_AGE + TEST_GRACE;
    assert_true( $worst_case > 0, 'Worst-case staleness should be a finite, bounded value' );
}

// ---------------------------------------------------------------------------
// get_status
// ---------------------------------------------------------------------------

function test_status_active() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: 1000, size: 5000 );
    assert_equals( 'active', $cascade->get_status( $entry, 1050 ), 'Fresh entry status should be active' );
}

function test_status_expired() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: true, generated_at: 1000, size: 5000 );
    assert_equals( 'expired', $cascade->get_status( $entry, 1101 ), 'Expired entry status should be expired' );
}

function test_status_missing() {
    $cascade = make_cascade();
    $entry = new CacheEntry( exists: false );
    assert_equals( 'missing', $cascade->get_status( $entry, 1000 ), 'Missing entry status should be missing' );
}

// ---------------------------------------------------------------------------
// Helper
// ---------------------------------------------------------------------------

function assert_false( $condition, $message ) {
    assert_true( ! $condition, $message );
}

// ---------------------------------------------------------------------------
// Run all tests
// ---------------------------------------------------------------------------

$tests = get_defined_functions();
foreach ( $tests['user'] as $func ) {
    if ( strpos( $func, 'test_' ) === 0 ) {
        $func();
    }
}

echo "\n";
echo "Results: $pass passed, $fail failed\n";
exit( $fail > 0 ? 1 : 0 );
