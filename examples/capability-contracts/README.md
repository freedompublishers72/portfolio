# Capability-Contract Provider Layer

## What this demonstrates

Structural (Protocol-based) interface design for a provider framework.
Providers expose *capabilities* — not concrete implementations — and a
framework selects providers based on declared capabilities. Consumers
never instantiate provider classes directly.

A canonical error model translates all provider failures into a single
provider-agnostic hierarchy so consumers receive structured `ProviderError`
objects, never raw transport exceptions.

## The engineering problem

When a framework depends on concrete provider classes, adding or replacing
a provider requires modifying the framework itself. By defining
*capability contracts* as structural Protocols, any object implementing the
required methods satisfies the contract — no inheritance required. The
framework routes queries to providers that declared the matching
capability, and partial providers (implementing only a subset of
capabilities) are first-class citizens.

The error model solves a parallel problem: every external provider has its
own error vocabulary. Without translation, consumers must handle each
provider's errors differently. The canonical hierarchy (`TransportError`,
`RateLimitError`, `AuthenticationError`, …) gives consumers a single,
provider-agnostic vocabulary. A rate-limit failure from any provider
becomes a `RateLimitError`.

## Important design decisions

- **Structural Protocols (PEP 544):** providers do not inherit from the
  contracts; they implement the methods. `@runtime_checkable` allows
  `isinstance` capability checks without coupling.
- **Capability flags (`Capabilities`):** a `Flag` enum lets a provider
  declare exactly which capabilities it supports — and the framework can
  check support with bitwise operations.
- **Immutable query objects:** `DiscoveryQuery` is frozen and validates
  its fields in `__post_init__`. The `extra_filters` mapping is wrapped in
  `MappingProxyType` for immutability.
- **Error equality and hashing:** `ProviderError` implements value
  equality (same type + message + identity) so errors can be compared in
  tests and used in sets.
- **Dependency direction:** provider-specific knowledge lives only inside
  provider implementations. No provider-specific vocabulary escapes the
  contract layer.

## How it differs from the original production context

The original contracts served a market-data provider framework with
multiple live providers, a normalization boundary, and a provider registry.
This demonstration bundles the contracts, the canonical error model, and
the minimal domain value objects needed to make them compile standalone.
Internal architecture-decision references and provider-name examples in
docstrings were removed. The Protocol structure, capability flags, error
hierarchy, and validation logic are preserved.

## Files

- `contracts.py` — domain objects, query contract, capability Protocols, error model
- `test_contracts.py` — tests for structural typing, validation, and error model

## Running the tests

```bash
cd examples/capability-contracts
python -m pytest test_contracts.py -v
```
