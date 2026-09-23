"""
Capability-contract provider layer with a canonical error model.

Demonstrates structural (Protocol-based) interface design where providers
expose capabilities — not concrete implementations — and a framework
selects providers based on declared capabilities. Consumers never
instantiate provider classes directly.

The contracts are structural: any object implementing the required methods
satisfies the contract without inheriting from it. This keeps the contract
layer free of business logic and framework dependencies.

A canonical error model translates all provider failures into a single
provider-agnostic hierarchy so consumers receive structured errors, never
raw transport exceptions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Flag, auto
from types import MappingProxyType
from typing import Any, Mapping, Protocol, runtime_checkable
from uuid import UUID, uuid4


# ---------------------------------------------------------------------------
# Minimal domain value objects (standalone for this demonstration)
# ---------------------------------------------------------------------------

@dataclass(frozen=True, slots=True)
class CanonicalIdentifier:
    """Opaque, canonical identifier for an entity.

    Consumers use it for lookup but never inspect its structure.
    """

    value: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.value, UUID):
            raise TypeError("CanonicalIdentifier.value must be a UUID")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CanonicalIdentifier):
            return NotImplemented
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True, slots=True)
class ProviderIdentity:
    """Canonical, immutable identity of a provider.

    The framework uses this to route queries and attribute errors without
    exposing provider-specific vocabulary to consumers.
    """

    name: str

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("ProviderIdentity.name must be a non-empty string")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ProviderIdentity):
            return NotImplemented
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return self.name


class Capabilities(Flag):
    """Capability flags a provider may declare.

    A provider may implement any subset of these — partial providers are
    explicitly supported.
    """

    NONE = 0
    DISCOVERY = auto()
    LOOKUP = auto()
    HISTORICAL = auto()
    METADATA = auto()


@dataclass(frozen=True, slots=True)
class Market:
    """Canonical market object returned by providers.

    Providers return canonical objects — never raw provider responses.
    Normalization happens inside the provider before the response escapes.
    """

    identifier: CanonicalIdentifier
    question: str
    status: str = "active"

    def __post_init__(self) -> None:
        if not isinstance(self.identifier, CanonicalIdentifier):
            raise TypeError("Market.identifier must be a CanonicalIdentifier")
        if not isinstance(self.question, str) or not self.question.strip():
            raise ValueError("Market.question must be a non-empty string")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Market):
            return NotImplemented
        return self.identifier == other.identifier

    def __hash__(self) -> int:
        return hash(self.identifier)


@dataclass(frozen=True, slots=True)
class MarketMetadata:
    """Structured metadata for a market (resolution criteria, category, etc.)."""

    identifier: CanonicalIdentifier
    category: str | None = None
    tags: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if not isinstance(self.identifier, CanonicalIdentifier):
            raise TypeError("MarketMetadata.identifier must be a CanonicalIdentifier")
        if not isinstance(self.tags, tuple):
            raise TypeError("MarketMetadata.tags must be a tuple")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MarketMetadata):
            return NotImplemented
        return self.identifier == other.identifier

    def __hash__(self) -> int:
        return hash(self.identifier)


# ---------------------------------------------------------------------------
# Discovery query contract
# ---------------------------------------------------------------------------

@dataclass(frozen=True, slots=True)
class DiscoveryQuery:
    """Immutable discovery query — filters and constraints.

    Carries no provider-specific vocabulary. Providers interpret the
    canonical filters and map them to their native query parameters inside
    their own normalization boundary.
    """

    category: str | None = None
    tags: tuple[str, ...] = field(default_factory=tuple)
    max_results: int | None = None
    cursor: str | None = None
    sort_by: str | None = None
    extra_filters: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.max_results is not None:
            if not isinstance(self.max_results, int) or self.max_results <= 0:
                raise ValueError("DiscoveryQuery.max_results must be a positive integer or None")

        if not isinstance(self.tags, tuple):
            raise TypeError("DiscoveryQuery.tags must be a tuple")
        for tag in self.tags:
            if not isinstance(tag, str) or not tag.strip():
                raise ValueError("DiscoveryQuery.tags must contain only non-empty strings")

        if self.category is not None:
            if not isinstance(self.category, str) or not self.category.strip():
                raise ValueError("DiscoveryQuery.category must be a non-empty string or None")

        if self.cursor is not None:
            if not isinstance(self.cursor, str) or not self.cursor.strip():
                raise ValueError("DiscoveryQuery.cursor must be a non-empty string or None")

        if self.sort_by is not None:
            if not isinstance(self.sort_by, str) or not self.sort_by.strip():
                raise ValueError("DiscoveryQuery.sort_by must be a non-empty string or None")

        if not isinstance(self.extra_filters, Mapping):
            raise TypeError("DiscoveryQuery.extra_filters must be a mapping")
        if self.extra_filters:
            object.__setattr__(self, "extra_filters", MappingProxyType(dict(self.extra_filters)))


# ---------------------------------------------------------------------------
# Capability contracts (Protocol interfaces)
# ---------------------------------------------------------------------------

@runtime_checkable
class Provider(Protocol):
    """Base provider contract.

    Every provider must expose its identity and declared capabilities.
    This is the minimal contract; specific capability contracts extend it
    with the methods that deliver each capability.

    A provider is the only place where provider-specific knowledge lives:
    native API endpoints, authentication, response formats, identifiers,
    rate limits, and transport concerns. No provider-specific knowledge
    escapes the provider's implementation and its normalization boundary.
    """

    @property
    def identity(self) -> ProviderIdentity:
        """Return the canonical, immutable identity of this provider."""
        ...

    @property
    def capabilities(self) -> Capabilities:
        """Return the declared capabilities of this provider."""
        ...


@runtime_checkable
class DiscoveryProvider(Protocol):
    """Market Discovery capability contract.

    A provider that supports discovery can find markets based on filters
    and constraints. The discovery method returns canonical ``Market``
    objects — never raw provider responses. An empty tuple indicates a
    successful query with no matches; this is not an error.
    """

    def discover_markets(self, query: DiscoveryQuery) -> tuple[Market, ...]:
        """Discover markets matching the given query.

        Raises:
            ProviderError: If the provider could not respond or the
                response was invalid. Never raises raw transport exceptions.
        """
        ...


@runtime_checkable
class LookupProvider(Protocol):
    """Market Lookup capability contract.

    A provider that supports lookup can retrieve a single market by its
    canonical identifier.
    """

    def lookup_market(self, identifier: CanonicalIdentifier) -> Market:
        """Look up a single market by its canonical identifier.

        Raises:
            MarketNotFoundError: If no market corresponds to the identifier.
            ProviderError: If the provider could not respond.
        """
        ...


@runtime_checkable
class HistoricalMarketsProvider(Protocol):
    """Historical Markets capability contract.

    A provider that supports historical markets can return resolved markets
    for outcome tracking and evaluation.
    """

    def discover_historical_markets(self, query: DiscoveryQuery) -> tuple[Market, ...]:
        """Discover resolved/historical markets matching the given query.

        Raises:
            ProviderError: If the provider could not respond.
        """
        ...


@runtime_checkable
class MetadataProvider(Protocol):
    """Metadata capability contract.

    A provider that supports metadata can supply structured metadata for
    a market (resolution criteria, category, tags).
    """

    def fetch_metadata(self, identifier: CanonicalIdentifier) -> MarketMetadata:
        """Fetch structured metadata for the given market.

        Raises:
            MarketNotFoundError: If no market corresponds to the identifier.
            ProviderError: If the provider could not respond.
        """
        ...


@runtime_checkable
class MarketProvider(Protocol):
    """Composite provider contract — the union of capability contracts.

    A full provider may implement any subset of these capabilities (partial
    providers are explicitly supported).
    """

    @property
    def identity(self) -> ProviderIdentity:
        ...

    @property
    def capabilities(self) -> Capabilities:
        ...


# ---------------------------------------------------------------------------
# Canonical error model
# ---------------------------------------------------------------------------

class ProviderError(Exception):
    """Base class for all canonical provider errors.

    All provider errors inherit from this base class. Consumers catch
    ``ProviderError`` to handle any provider failure, or catch specific
    subclasses for granular handling.

    Provider errors carry the provider identity so consumers can know
    *which* provider failed without the error vocabulary being
    provider-specific.

    Attributes:
        message: A provider-agnostic description. Must not contain
            provider-specific error codes, response bodies, or vocabulary.
        provider_identity: The canonical identity of the provider that
            failed, or ``None`` if the error is not attributable to a
            specific provider.
    """

    def __init__(
        self,
        message: str,
        provider_identity: str | None = None,
    ) -> None:
        if not isinstance(message, str) or not message.strip():
            raise ValueError("ProviderError.message must be a non-empty string")
        if provider_identity is not None:
            if not isinstance(provider_identity, str) or not provider_identity.strip():
                raise ValueError("ProviderError.provider_identity must be a non-empty string or None")
        self.message = message
        self.provider_identity = provider_identity
        super().__init__(message)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ProviderError):
            return NotImplemented
        return (
            type(self) is type(other)
            and self.message == other.message
            and self.provider_identity == other.provider_identity
        )

    def __hash__(self) -> int:
        return hash((type(self).__name__, self.message, self.provider_identity))

    def __repr__(self) -> str:
        return f"{type(self).__name__}(message={self.message!r}, provider_identity={self.provider_identity!r})"


class TransportError(ProviderError):
    """The provider could not be reached or the connection was interrupted."""


class AuthenticationError(ProviderError):
    """The provider rejected the framework's credentials."""


class RateLimitError(ProviderError):
    """The provider rate-limited the request."""


class ProviderUnavailableError(ProviderError):
    """The provider is temporarily unavailable (e.g. 5xx, maintenance)."""


class NormalizationError(ProviderError):
    """The provider returned a response that could not be normalized."""


class CapabilityNotSupportedError(ProviderError):
    """The requested capability is not supported by any registered provider."""


class MarketNotFoundError(ProviderError):
    """The requested identifier does not correspond to any known market."""


class ConfigurationError(ProviderError):
    """The framework's configuration is invalid or incomplete."""


class DiscoveryError(ProviderError):
    """A discovery query could not be completed at the framework level."""
