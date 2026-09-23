# Technical Code Demonstrations

Sanitized, standalone code examples extracted from larger private projects.
Each demonstration isolates one engineering concept with focused
implementation, tests, and documentation. No demonstration requires access
to the original production systems.

---

## Demonstrations

### Protected-Token Translation Validator (PHP)

Defensive verification of machine-translated text against a protected-token
map — token count match, missing/extra/duplicate detection, unexpected HTML
injection, and post-reconstruction integrity (URL/shortcode preservation).

→ [`protected-token-validator/`](protected-token-validator/)

### Bounded-Staleness Cache Serve Cascade (PHP)

The serving decision table of a production full-page cache: HIT / STALE
(stale-while-revalidate) / MISS cascade, plus the bounded staleness model
that makes an indefinitely stale representation impossible.

→ [`bounded-staleness-cache/`](bounded-staleness-cache/)

### Capability-Contract Provider Layer (Python)

Structural Protocol-based interface design for a provider framework —
capability contracts, immutable query objects, and a canonical
provider-agnostic error model.

→ [`capability-contracts/`](capability-contracts/)

### Calibration Metrics (Python)

Defensive numerical evaluation of probabilistic forecasts — Brier score,
hit rate, log loss, reliability diagram, ECE/MCE — with strict input
validation that rejects NaN, infinity, and out-of-range values.

→ [`calibration-metrics/`](calibration-metrics/)

### Resilient Collector Primitives (Python)

Four production reliability primitives: resumable offset pagination,
interval pacing, bounded exponential backoff with jitter, and advisory
flock-based single-instance run locking.

→ [`resilient-collector-primitives/`](resilient-collector-primitives/)

### Accept-Language Locale Matcher (PHP)

Correct Accept-Language header parsing with q-value negotiation, case
normalization, region-subtag truncation, q=0 rejection, and
allowlist-gated matching.

→ [`accept-language-matcher/`](accept-language-matcher/)

### Immutable Domain Primitives (Python)

Frozen dataclass value objects with construction-time validation,
MappingProxyType immutability for detail mappings, and value equality with
NotImplemented cross-type returns.

→ [`immutable-domain-primitives/`](immutable-domain-primitives/)

---

## Running the tests

Each demonstration has its own test suite:

```bash
# Python demonstrations
cd examples/calibration-metrics && python -m pytest test_metrics.py -v
cd examples/capability-contracts && python -m pytest test_contracts.py -v
cd examples/resilient-collector-primitives && python -m pytest test_primitives.py -v
cd examples/immutable-domain-primitives && python -m pytest test_domain_primitives.py -v

# PHP demonstrations
cd examples/protected-token-validator && php test_token_validator.php
cd examples/bounded-staleness-cache && php test_cache_serve_cascade.php
cd examples/accept-language-matcher && php test_accept_language.php
```
