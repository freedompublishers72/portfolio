# Immutable Domain Primitives

## What this demonstrates

Defensive domain modeling with frozen dataclasses that enforce invariants
at construction time. Each value object rejects invalid inputs (NaN,
infinity, out-of-range, wrong types) in `__post_init__`, freezes its
mutable detail mapping via `MappingProxyType`, and implements value
equality with `NotImplemented` cross-type returns.

## The engineering problem

When domain invariants (e.g. "a probability is always in [0, 1]") are
enforced only at use sites, every consumer must repeat the same defensive
checks — or silently accept invalid data. By validating at the
constructor boundary and making the object immutable, the invariant
becomes a structural property of the type itself: once a `Probability(0.5)`
exists, it is guaranteed valid for its entire lifetime.

The `detail` / `derivation` mappings present a subtler problem: a plain
`dict` field on a frozen dataclass is mutable, breaking the immutability
contract. `MappingProxyType` wraps the dict at construction time so the
mapping becomes read-only.

## Important design decisions

- **`__post_init__` validation:** invariants are checked once, at the
  boundary, not at every consumption site.
- **`MappingProxyType` for detail fields:** the frozen dataclass prevents
  reassignment of fields, but `dict` values are still mutable.
  `MappingProxyType` closes that gap.
- **`NotImplemented` in `__eq__`:** cross-type comparisons return
  `NotImplemented` (letting Python fall back to identity), not `False` —
  this is the correct protocol for value equality.
- **Opaque identity:** `CanonicalIdentifier` wraps a UUID but exposes no
  structure to consumers — they use it for lookup without inspecting it.

## How it differs from the original production context

The original system used these primitives as the foundation of a larger
valuation pipeline (probability → confidence → edge → score). This
demonstration isolates the five value objects with no dependency on the
engine's domain layer, pipeline stages, or framework. Internal
architecture-decision references and provider-name examples in docstrings
were removed; the validation and immutability logic is preserved verbatim.

## Files

- `domain_primitives.py` — the value objects
- `test_domain_primitives.py` — tests for validation, immutability, equality, hashing

## Running the tests

```bash
cd examples/immutable-domain-primitives
python -m pytest test_domain_primitives.py -v
```
