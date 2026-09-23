<?php
/**
 * Accept-Language Locale Matcher
 *
 * Parses an HTTP Accept-Language header, normalizes language tags to
 * ISO 639-1 codes, resolves q-value preferences, and returns the
 * highest-quality match against a deployed-language allowlist.
 *
 * Handles the details that implementations commonly get wrong:
 * - q-value parsing (defaults to 1.0 when omitted)
 * - case normalization (lowercased)
 * - highest-q wins (first declared wins ties)
 * - q=0 rejection (explicitly excluded)
 * - allowlist-gated negotiation (only deployed languages match)
 */

/**
 * Parse an Accept-Language header and return the best matching language.
 *
 * @param string $accept_lang      The raw Accept-Language header value.
 * @param array  $deployed_languages The set of language codes that are deployed.
 * @param string $default_language  The source/default language to exclude from
 *                                  negotiation (it is the fallback, not a match).
 * @return string|false The best matching 2-letter language code, or false.
 */
function parse_accept_language( $accept_lang, $deployed_languages, $default_language = 'en' ) {
    if ( empty( $accept_lang ) ) {
        return false;
    }

    // Parse the Accept-Language header.
    $languages = array();
    $parts = explode( ',', $accept_lang );
    foreach ( $parts as $part ) {
        $part = trim( $part );
        if ( empty( $part ) ) {
            continue;
        }
        // Format: language;q=value or just language.
        if ( strpos( $part, ';' ) !== false ) {
            list( $code, $q ) = explode( ';', $part, 2 );
            $code = trim( $code );
            $q = (float) str_replace( 'q=', '', trim( $q ) );
        } else {
            $code = $part;
            $q = 1.0;
        }
        // Normalize: take first 2 chars for ISO 639-1.
        $code = strtolower( substr( $code, 0, 2 ) );
        if ( ! isset( $languages[ $code ] ) || $q > $languages[ $code ] ) {
            $languages[ $code ] = $q;
        }
    }

    // Sort by quality (descending). arsort preserves key association
    // and sorts values in descending order; equal values retain their
    // original insertion order (stable sort in PHP 8.0+).
    arsort( $languages );

    // Find the first matching deployed language (excluding the default).
    $deployed = array_diff( $deployed_languages, array( $default_language ) );

    foreach ( $languages as $code => $q ) {
        if ( in_array( $code, $deployed, true ) && $q > 0 ) {
            return $code;
        }
    }

    return false;
}
