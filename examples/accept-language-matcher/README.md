# Accept-Language Locale Matcher

## What this demonstrates

Correct parsing of the HTTP `Accept-Language` header with q-value
negotiation against a deployed-language allowlist. The implementation
handles the details that are commonly implemented incorrectly.

## The engineering problem

`Accept-Language` parsing has several subtleties that naive implementations
get wrong:

- **q-value defaults:** when `;q=` is omitted, the quality defaults to
  `1.0` (highest), not `0` or "unspecified".
- **q=0 rejection:** a language with `q=0` is *explicitly excluded* — it
  must not match even if it is the only deployed language present.
- **Region subtags:** `fr-CA` and `fr-FR` both match `fr`. The matcher
  truncates to the first 2 characters (ISO 639-1).
- **Tie-breaking:** when two languages have the same q-value, the first
  declared in the header should win. `arsort` in PHP 8.0+ is stable,
  preserving insertion order for equal values.
- **Allowlist gating:** only deployed languages match. The default/source
  language is excluded from negotiation — it is the fallback, not a match.

## Important design decisions

- **Parameterized language set:** the deployed languages and the default
  language are function parameters, not global constants. This makes the
  matcher reusable and testable with any language configuration.
- **Highest-q-wins with stable ordering:** `arsort` sorts by descending
  q-value while preserving key association and insertion order for ties.
  The first matching deployed language in the sorted list wins.
- **2-character truncation:** language tags are normalized to lowercase
  and truncated to 2 characters immediately, before deduplication. If
  the same base language appears multiple times (`fr;q=0.3,fr;q=0.9`),
  the highest q-value is kept.
- **Empty-header guard:** an empty or whitespace-only header returns
  `false` immediately, before any parsing.

## How it differs from the original production context

The original implementation was a static method inside a WordPress
multilingual plugin's language router class (~1500 lines) that depended on
plugin-specific constants for the deployed language set and source
language. This demonstration extracts the parsing function standalone,
parameterizes the language set, removes the WordPress and plugin
dependencies, and genericizes all terminology. The parsing logic —
q-value handling, case normalization, region truncation, allowlist
gating, q=0 rejection — is preserved verbatim.

## Files

- `accept_language.php` — the locale matcher function
- `test_accept_language.php` — tests for q-values, normalization, and edge cases

## Running the tests

```bash
cd examples/accept-language-matcher
php test_accept_language.php
```
