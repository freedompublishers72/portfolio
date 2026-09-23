<?php
/**
 * Tests for the Accept-Language Locale Matcher.
 *
 * Run: php test_accept_language.php
 */

require_once __DIR__ . '/accept_language.php';

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
        echo "FAIL: $message (expected '" . var_export( $expected, true ) . "', got '" . var_export( $actual, true ) . "')\n";
    }
}

function assert_false( $condition, $message ) {
    assert_true( ! $condition, $message );
}

// Test deployed languages: French, German, Spanish, Thai, Khmer.
// Default (excluded): English.
$DEPLOYED = array( 'en', 'fr', 'de', 'es', 'th', 'km' );

// ---------------------------------------------------------------------------
// Basic matching
// ---------------------------------------------------------------------------

function test_single_language_match() {
    global $DEPLOYED;
    $result = parse_accept_language( 'fr', $DEPLOYED );
    assert_equals( 'fr', $result, 'Single language should match' );
}

function test_simple_preference() {
    global $DEPLOYED;
    $result = parse_accept_language( 'fr,en;q=0.5', $DEPLOYED );
    assert_equals( 'fr', $result, 'Higher q-value should win' );
}

function test_q_value_ordering() {
    global $DEPLOYED;
    // de has higher q than fr
    $result = parse_accept_language( 'fr;q=0.3,de;q=0.9', $DEPLOYED );
    assert_equals( 'de', $result, 'Higher q-value should win' );
}

// ---------------------------------------------------------------------------
// q-value handling
// ---------------------------------------------------------------------------

function test_default_q_is_one() {
    global $DEPLOYED;
    // No q-value means q=1.0 (highest)
    $result = parse_accept_language( 'fr;q=0.9,de', $DEPLOYED );
    assert_equals( 'de', $result, 'Missing q defaults to 1.0' );
}

function test_q_zero_rejected() {
    global $DEPLOYED;
    // fr with q=0 should be rejected; de should match
    $result = parse_accept_language( 'fr;q=0,de;q=0.8', $DEPLOYED );
    assert_equals( 'de', $result, 'q=0 language should be rejected' );
}

function test_all_q_zero_returns_false() {
    global $DEPLOYED;
    $result = parse_accept_language( 'fr;q=0,de;q=0', $DEPLOYED );
    assert_false( $result, 'All q=0 should return false' );
}

// ---------------------------------------------------------------------------
// Case normalization
// ---------------------------------------------------------------------------

function test_uppercase_normalized() {
    global $DEPLOYED;
    $result = parse_accept_language( 'FR', $DEPLOYED );
    assert_equals( 'fr', $result, 'Uppercase should be normalized to lowercase' );
}

function test_mixed_case_normalized() {
    global $DEPLOYED;
    $result = parse_accept_language( 'De', $DEPLOYED );
    assert_equals( 'de', $result, 'Mixed case should be normalized' );
}

// ---------------------------------------------------------------------------
// ISO 639-1 truncation
// ---------------------------------------------------------------------------

function test_region_subtag_truncated() {
    global $DEPLOYED;
    // fr-CA should match fr
    $result = parse_accept_language( 'fr-CA', $DEPLOYED );
    assert_equals( 'fr', $result, 'Region subtag should be truncated to 2 chars' );
}

function test_complex_header_with_regions() {
    global $DEPLOYED;
    $result = parse_accept_language( 'en-US,en;q=0.9,fr-FR;q=0.8,de;q=0.7', $DEPLOYED );
    // en is excluded (default), fr-FR → fr (q=0.8), de (q=0.7) → fr wins
    assert_equals( 'fr', $result, 'Should match highest-q deployed non-default language' );
}

// ---------------------------------------------------------------------------
// Default language exclusion
// ---------------------------------------------------------------------------

function test_default_language_excluded() {
    global $DEPLOYED;
    // en is the default — should be excluded from matching
    $result = parse_accept_language( 'en', $DEPLOYED );
    assert_false( $result, 'Default language alone should not match' );
}

function test_default_excluded_but_fallback_matches() {
    global $DEPLOYED;
    $result = parse_accept_language( 'en;q=0.9,fr;q=0.8', $DEPLOYED );
    // en excluded, fr is next
    assert_equals( 'fr', $result, 'Should skip default and match next deployed language' );
}

// ---------------------------------------------------------------------------
// No match
// ---------------------------------------------------------------------------

function test_no_deployed_match() {
    global $DEPLOYED;
    $result = parse_accept_language( 'ja,ko,zh', $DEPLOYED );
    assert_false( $result, 'Undeployed languages should return false' );
}

function test_empty_header() {
    global $DEPLOYED;
    $result = parse_accept_language( '', $DEPLOYED );
    assert_false( $result, 'Empty header should return false' );
}

// ---------------------------------------------------------------------------
// Edge cases
// ---------------------------------------------------------------------------

function test_whitespace_handling() {
    global $DEPLOYED;
    $result = parse_accept_language( 'fr ; q=0.9 , de ; q=0.8', $DEPLOYED );
    assert_equals( 'fr', $result, 'Should handle whitespace around tokens' );
}

function test_duplicate_language_highest_q_wins() {
    global $DEPLOYED;
    // Same language appears twice with different q-values
    $result = parse_accept_language( 'fr;q=0.3,fr;q=0.9', $DEPLOYED );
    assert_equals( 'fr', $result, 'Duplicate language: highest q should win' );
}

function test_first_declared_wins_tie() {
    global $DEPLOYED;
    // Both fr and de have q=0.5; fr is declared first
    $result = parse_accept_language( 'fr;q=0.5,de;q=0.5', $DEPLOYED );
    assert_equals( 'fr', $result, 'Tie should be broken by declaration order' );
}

function test_custom_default_language() {
    $deployed = array( 'en', 'fr', 'de' );
    // With 'fr' as default, fr should be excluded
    $result = parse_accept_language( 'fr,de;q=0.5', $deployed, 'fr' );
    assert_equals( 'de', $result, 'Custom default language should be excluded' );
}

function test_empty_parts_skipped() {
    global $DEPLOYED;
    $result = parse_accept_language( ',fr,,de;q=0.5,', $DEPLOYED );
    assert_equals( 'fr', $result, 'Empty parts should be skipped' );
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
