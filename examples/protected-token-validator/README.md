# Protected-Token Translation Validator

## What this demonstrates

Defensive verification of machine-translated text against a protected-token
map. Before a translation service processes content, inline elements (URLs,
shortcodes, HTML entities) are replaced with opaque `%%TOKEN%%` markers. After
translation, this validator verifies the round-trip integrity of that
protection scheme before the markers are replaced with their original content.

## The engineering problem

Machine translation services alter text unpredictably: they may reorder
tokens, inject HTML, drop markers, or duplicate them. If these defects are
not caught *before* reconstruction, the final content may contain broken
URLs, missing shortcodes, or injected markup — and the error may not be
visible until the page is rendered.

This validator acts as a gate between translation and reconstruction. It
checks the translated text for token integrity (count match, no missing,
no extra, no duplicates, no unexpected HTML) and then checks the
reconstructed content for completeness (no unreplaced tokens, no segment
markers, URL preservation, shortcode preservation).

## Important design decisions

- **Six token checks before reconstruction:** count match, missing, extra,
  duplicate, and unexpected HTML injection. Each produces a specific error
  message so the operator knows exactly what went wrong.
- **HTML stripping before tag detection:** tokens and segment markers are
  stripped from the text before checking for unexpected HTML tags, so
  legitimate token content is not mistaken for injected markup.
- **URL and shortcode preservation:** after reconstruction, URLs (from
  `href`/`src` attributes) and shortcode tags are extracted from both the
  original and reconstructed content and compared — any missing element
  is a reconstruction failure.
- **Structured error reporting:** every check appends to an errors array
  rather than throwing, so all defects are reported in one pass rather
  than stopping at the first.

## How it differs from the original production context

The original validator was a static class method inside a WordPress
multilingual plugin that depended on a constants class for the token regex
patterns and used WordPress-specific terminology in its docstrings. This
demonstration inlines the regex constants, converts the class methods to
standalone functions, removes the WordPress dependency, and genericizes all
terminology. The validation logic — the six token checks, the four
reconstruction checks, the URL/shortcode extraction — is preserved verbatim.

## Files

- `token_validator.php` — the validator functions
- `test_token_validator.php` — focused tests for all validation checks

## Running the tests

```bash
cd examples/protected-token-validator
php test_token_validator.php
```
