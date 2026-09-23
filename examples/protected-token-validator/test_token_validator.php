<?php
/**
 * Tests for the Protected-Token Translation Validator.
 *
 * Run: php test_token_validator.php
 */

require_once __DIR__ . '/token_validator.php';

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

function assert_false( $condition, $message ) {
    assert_true( ! $condition, $message );
}

// ---------------------------------------------------------------------------
// validate_tokens — valid cases
// ---------------------------------------------------------------------------

function test_valid_token_match() {
    $tokens = array( '%%URL_1%%' => 'https://example.com', '%%TOKEN_2%%' => 'protected' );
    $translated = 'Hello %%URL_1%% world %%TOKEN_2%% end';
    $result = validate_tokens( $translated, $tokens );
    assert_true( $result['valid'], 'Valid token match should pass' );
    assert_true( empty( $result['errors'] ), 'Valid token match should have no errors' );
    assert_true( count( $result['found_tokens'] ) === 2, 'Should find 2 tokens' );
}

function test_valid_alt_token_match() {
    $tokens = array( '[[URL_1]]' => 'https://example.com' );
    $translated = 'Hello [[URL_1]] world';
    $result = validate_tokens( $translated, $tokens, true );
    assert_true( $result['valid'], 'Valid alt token match should pass' );
}

// ---------------------------------------------------------------------------
// validate_tokens — error cases
// ---------------------------------------------------------------------------

function test_missing_token() {
    $tokens = array( '%%A%%' => 'a', '%%B%%' => 'b' );
    $translated = 'Only %%A%% here';
    $result = validate_tokens( $translated, $tokens );
    assert_false( $result['valid'], 'Missing token should fail' );
    assert_true( count( $result['errors'] ) >= 1, 'Missing token should report errors' );
}

function test_extra_token() {
    $tokens = array( '%%A%%' => 'a' );
    $translated = '%%A%% and %%B%%';
    $result = validate_tokens( $translated, $tokens );
    assert_false( $result['valid'], 'Extra token should fail' );
}

function test_duplicate_token() {
    $tokens = array( '%%A%%' => 'a' );
    $translated = '%%A%% and %%A%%';
    $result = validate_tokens( $translated, $tokens );
    assert_false( $result['valid'], 'Duplicate token should fail' );
}

function test_token_count_mismatch() {
    $tokens = array( '%%A%%' => 'a', '%%B%%' => 'b', '%%C%%' => 'c' );
    $translated = '%%A%% %%B%%';
    $result = validate_tokens( $translated, $tokens );
    assert_false( $result['valid'], 'Token count mismatch should fail' );
}

function test_unexpected_html_tags() {
    $tokens = array( '%%A%%' => 'a' );
    $translated = '%%A%% <script>alert(1)</script>';
    $result = validate_tokens( $translated, $tokens );
    assert_false( $result['valid'], 'Unexpected HTML should fail' );
}

function test_no_unexpected_html_for_valid_text() {
    $tokens = array( '%%A%%' => 'a' );
    $translated = 'Just text %%A%% more text';
    $result = validate_tokens( $translated, $tokens );
    assert_true( $result['valid'], 'Plain text with tokens should pass' );
}

// ---------------------------------------------------------------------------
// validate_reconstruction — valid cases
// ---------------------------------------------------------------------------

function test_valid_reconstruction() {
    $original = '<p>Hello world</p><a href="https://example.com">Link</a>';
    $reconstructed = '<p>Bonjour le monde</p><a href="https://example.com">Lien</a>';
    $result = validate_reconstruction( $reconstructed, $original );
    assert_true( $result['valid'], 'Valid reconstruction should pass' );
}

function test_reconstruction_no_urls() {
    $original = '<p>Simple text</p>';
    $reconstructed = '<p>Texto simple</p>';
    $result = validate_reconstruction( $reconstructed, $original );
    assert_true( $result['valid'], 'Reconstruction without URLs should pass' );
}

// ---------------------------------------------------------------------------
// validate_reconstruction — error cases
// ---------------------------------------------------------------------------

function test_unreplaced_tokens() {
    $original = '<p>Hello</p>';
    $reconstructed = '<p>%%TOKEN_1%% world</p>';
    $result = validate_reconstruction( $reconstructed, $original );
    assert_false( $result['valid'], 'Unreplaced tokens should fail' );
}

function test_unreplaced_alt_tokens() {
    $original = '<p>Hello</p>';
    $reconstructed = '<p>[[TOKEN_1]] world</p>';
    $result = validate_reconstruction( $reconstructed, $original );
    assert_false( $result['valid'], 'Unreplaced alt tokens should fail' );
}

function test_unreplaced_segment_markers() {
    $original = '<p>Hello</p>';
    $reconstructed = '<p>%%SHORTCODE_SEGMENT:abc%% world</p>';
    $result = validate_reconstruction( $reconstructed, $original );
    assert_false( $result['valid'], 'Unreplaced segment markers should fail' );
}

function test_missing_url() {
    $original = '<a href="https://example.com">Link</a>';
    $reconstructed = '<a href="https://different.com">Link</a>';
    $result = validate_reconstruction( $reconstructed, $original );
    assert_false( $result['valid'], 'Missing URL should fail' );
}

function test_url_preserved() {
    $original = '<a href="https://example.com">Link</a>';
    $reconstructed = '<a href="https://example.com">Lien</a>';
    $result = validate_reconstruction( $reconstructed, $original );
    assert_true( $result['valid'], 'Preserved URL should pass' );
}

function test_missing_shortcode() {
    $original = '<p>[gallery id="1"]</p>';
    $reconstructed = '<p>Text</p>';
    $result = validate_reconstruction( $reconstructed, $original );
    assert_false( $result['valid'], 'Missing shortcode should fail' );
}

function test_shortcode_preserved() {
    $original = '<p>[gallery id="1"]</p>';
    $reconstructed = '<p>[gallery id="1"] text</p>';
    $result = validate_reconstruction( $reconstructed, $original );
    assert_true( $result['valid'], 'Preserved shortcode should pass' );
}

// ---------------------------------------------------------------------------
// extract_urls / extract_shortcode_tags
// ---------------------------------------------------------------------------

function test_extract_urls() {
    $content = '<a href="https://a.com">A</a><img src="https://b.com/img.png">';
    $urls = extract_urls( $content );
    assert_true( in_array( 'https://a.com', $urls ), 'Should extract href URL' );
    assert_true( in_array( 'https://b.com/img.png', $urls ), 'Should extract src URL' );
}

function test_extract_shortcode_tags() {
    $content = '<p>[gallery id="1"] [caption text]</p>';
    $tags = extract_shortcode_tags( $content );
    assert_true( in_array( 'gallery', $tags ), 'Should extract gallery shortcode' );
    assert_true( in_array( 'caption', $tags ), 'Should extract caption shortcode' );
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
