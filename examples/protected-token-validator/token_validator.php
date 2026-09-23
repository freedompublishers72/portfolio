<?php
/**
 * Protected-Token Translation Validator
 *
 * Validates machine-translated text against a protected-token map before
 * reconstruction, then validates the reconstructed content.
 *
 * Checks performed on translated text:
 * - Token count match (expected vs. found)
 * - No missing tokens
 * - No extra tokens
 * - No duplicate tokens
 * - No unexpected injected HTML tags
 *
 * Checks performed on reconstructed content:
 * - No unreplaced tokens remaining
 * - No unreplaced segment markers
 * - URL preservation (href/src attributes)
 * - Shortcode-tag preservation
 *
 * The token scheme uses %%TOKEN%%-style markers that protect inline
 * content (URLs, shortcodes, HTML entities) from being altered by the
 * translation service. This validator verifies the round-trip integrity
 * of that protection scheme.
 */

// Token regex patterns. Primary format: %%KEY%%. Alternate format: [[KEY]].
const TOKEN_REGEX     = '/%%[A-Z0-9_]+%%/';
const ALT_TOKEN_REGEX = '/\[\[[A-Z0-9_]+\]\]/';
const SEGMENT_MARKER_REGEX = '/%%SHORTCODE_SEGMENT:[^%]+%%/';

/**
 * Validate translated text against the original token set.
 *
 * @param string $translated_text  The text returned by the translation service.
 * @param array  $original_tokens   The original token map (token => content).
 * @param bool   $use_alt           Whether the alternate token format was used.
 * @return array {
 *     @type bool   $valid         Whether validation passed.
 *     @type array  $errors        List of validation error messages.
 *     @type array  $found_tokens  Tokens found in translated text.
 * }
 */
function validate_tokens( $translated_text, $original_tokens, $use_alt = false ) {
    $errors = array();
    $regex = $use_alt ? ALT_TOKEN_REGEX : TOKEN_REGEX;

    // Extract tokens from translated text.
    $found_tokens = array();
    preg_match_all( $regex, $translated_text, $matches );
    if ( ! empty( $matches[0] ) ) {
        $found_tokens = $matches[0];
    }

    $original_token_keys = array_keys( $original_tokens );
    $original_count = count( $original_token_keys );
    $found_count = count( $found_tokens );

    // Check 1: Token count match.
    if ( $found_count !== $original_count ) {
        $errors[] = sprintf(
            'Token count mismatch: expected %d, found %d',
            $original_count,
            $found_count
        );
    }

    // Check 2: No missing tokens.
    $missing = array_diff( $original_token_keys, $found_tokens );
    if ( ! empty( $missing ) ) {
        $errors[] = 'Missing tokens: ' . implode( ', ', array_slice( $missing, 0, 10 ) );
    }

    // Check 3: No extra tokens.
    $extra = array_diff( $found_tokens, $original_token_keys );
    if ( ! empty( $extra ) ) {
        $errors[] = 'Extra tokens: ' . implode( ', ', array_slice( $extra, 0, 10 ) );
    }

    // Check 4: No duplicate tokens.
    $counts = array_count_values( $found_tokens );
    $duplicates = array();
    foreach ( $counts as $token => $count ) {
        if ( $count > 1 ) {
            $duplicates[] = $token . ' (x' . $count . ')';
        }
    }
    if ( ! empty( $duplicates ) ) {
        $errors[] = 'Duplicate tokens: ' . implode( ', ', array_slice( $duplicates, 0, 10 ) );
    }

    // Check 5: No unexpected HTML tags in translated text (outside of tokens).
    $stripped = preg_replace( $regex, '', $translated_text );
    $stripped = preg_replace( SEGMENT_MARKER_REGEX, '', $stripped );
    if ( preg_match( '/<[a-z][a-z0-9]*\b[^>]*>/i', $stripped ) ) {
        $errors[] = 'Unexpected HTML tags found in translated text';
    }

    if ( empty( $errors ) ) {
        return array(
            'valid' => true,
            'errors' => array(),
            'found_tokens' => $found_tokens,
        );
    }

    return array(
        'valid' => false,
        'errors' => $errors,
        'found_tokens' => $found_tokens,
    );
}

/**
 * Post-reconstruction validation.
 *
 * @param string $reconstructed     The reconstructed content.
 * @param string $original_content  The original source content.
 * @return array {
 *     @type bool   $valid   Whether validation passed.
 *     @type array  $errors  List of validation error messages.
 * }
 */
function validate_reconstruction( $reconstructed, $original_content ) {
    $errors = array();

    // Check: No remaining tokens in reconstructed content.
    $primary_tokens = preg_match_all( TOKEN_REGEX, $reconstructed );
    $alt_tokens = preg_match_all( ALT_TOKEN_REGEX, $reconstructed );
    if ( $primary_tokens > 0 || $alt_tokens > 0 ) {
        $errors[] = 'Unreplaced tokens remaining in reconstructed content';
    }

    // Check: No remaining segment markers.
    if ( strpos( $reconstructed, '%%SHORTCODE_SEGMENT:' ) !== false ) {
        $errors[] = 'Unreplaced segment markers in reconstructed content';
    }

    // Check: URL preservation — extract URLs from both and compare.
    $original_urls = extract_urls( $original_content );
    $reconstructed_urls = extract_urls( $reconstructed );
    if ( ! empty( $original_urls ) ) {
        $missing_urls = array_diff( $original_urls, $reconstructed_urls );
        if ( ! empty( $missing_urls ) ) {
            $errors[] = 'URLs missing from reconstructed content: ' . implode( ', ', array_slice( $missing_urls, 0, 5 ) );
        }
    }

    // Check: Shortcode preservation.
    $original_shortcodes = extract_shortcode_tags( $original_content );
    $reconstructed_shortcodes = extract_shortcode_tags( $reconstructed );
    if ( ! empty( $original_shortcodes ) ) {
        $missing_shortcodes = array_diff( $original_shortcodes, $reconstructed_shortcodes );
        if ( ! empty( $missing_shortcodes ) ) {
            $errors[] = 'Shortcodes missing from reconstructed content: ' . implode( ', ', array_slice( $missing_shortcodes, 0, 5 ) );
        }
    }

    if ( empty( $errors ) ) {
        return array(
            'valid' => true,
            'errors' => array(),
        );
    }

    return array(
        'valid' => false,
        'errors' => $errors,
    );
}

/**
 * Extract URLs from HTML content (href and src attributes).
 *
 * @param string $content HTML content.
 * @return array Unique URLs found in href/src attributes.
 */
function extract_urls( $content ) {
    $urls = array();
    preg_match_all( '/href=["\']([^"\']+)["\']/i', $content, $matches );
    if ( ! empty( $matches[1] ) ) {
        $urls = $matches[1];
    }
    preg_match_all( '/src=["\']([^"\']+)["\']/i', $content, $matches2 );
    if ( ! empty( $matches2[1] ) ) {
        $urls = array_merge( $urls, $matches2[1] );
    }
    return array_unique( $urls );
}

/**
 * Extract shortcode tag names from content.
 *
 * @param string $content Content containing shortcode tags.
 * @return array Unique shortcode tag names.
 */
function extract_shortcode_tags( $content ) {
    $tags = array();
    preg_match_all( '/\[([a-z][a-z0-9_-]*)[^\]]*\]/', $content, $matches );
    if ( ! empty( $matches[1] ) ) {
        $tags = $matches[1];
    }
    return array_unique( $tags );
}
