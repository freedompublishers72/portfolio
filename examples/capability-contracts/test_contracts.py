"""Tests for capability contracts — structural typing, validation, error model."""

import pytest

from contracts import (
    AuthenticationError,
    Capabilities,
    CanonicalIdentifier,
    CapabilityNotSupportedError,
    ConfigurationError,
    DiscoveryProvider,
    DiscoveryQuery,
    HistoricalMarketsProvider,
    LookupProvider,
    Market,
    MarketMetadata,
    MarketNotFoundError,
    MarketProvider,
    MetadataProvider,
    NormalizationError,
    Provider,
    ProviderError,
    ProviderIdentity,
    ProviderUnavailableError,
    RateLimitError,
    TransportError,
)


# ---------------------------------------------------------------------------
# Domain value objects
# ---------------------------------------------------------------------------

class TestProviderIdentity:
    def test_valid(self):
        ident = ProviderIdentity("alpha")
        assert ident.name == "alpha"

    def test_rejects_empty(self):
        with pytest.raises(ValueError):
            ProviderIdentity("")

    def test_rejects_whitespace(self):
        with pytest.raises(ValueError):
            ProviderIdentity("   ")

    def test_equality(self):
        assert ProviderIdentity("alpha") == ProviderIdentity("alpha")
        assert ProviderIdentity("alpha") != ProviderIdentity("beta")

    def test_hashable(self):
        assert hash(ProviderIdentity("alpha")) == hash(ProviderIdentity("alpha"))


class TestCanonicalIdentifier:
    def test_auto_generated(self):
        a = CanonicalIdentifier()
        b = CanonicalIdentifier()
        assert a != b

    def test_explicit(self):
        from uuid import uuid4
        u = uuid4()
        assert CanonicalIdentifier(u).value == u

    def test_rejects_non_uuid(self):
        with pytest.raises(TypeError):
            CanonicalIdentifier("not-uuid")


class TestMarket:
    def test_valid(self):
        m = Market(CanonicalIdentifier(), "Will event X occur?")
        assert m.question == "Will event X occur?"

    def test_rejects_empty_question(self):
        with pytest.raises(ValueError):
            Market(CanonicalIdentifier(), "")

    def test_rejects_non_identifier(self):
        with pytest.raises(TypeError):
            Market("not-an-id", "question")


class TestMarketMetadata:
    def test_valid(self):
        md = MarketMetadata(CanonicalIdentifier(), category="politics")
        assert md.category == "politics"

    def test_tags_must_be_tuple(self):
        with pytest.raises(TypeError):
            MarketMetadata(CanonicalIdentifier(), tags=["a", "b"])


# ---------------------------------------------------------------------------
# DiscoveryQuery validation
# ---------------------------------------------------------------------------

class TestDiscoveryQuery:
    def test_defaults(self):
        q = DiscoveryQuery()
        assert q.category is None
        assert q.tags == ()
        assert q.max_results is None

    def test_max_results_must_be_positive(self):
        with pytest.raises(ValueError):
            DiscoveryQuery(max_results=0)
        with pytest.raises(ValueError):
            DiscoveryQuery(max_results=-1)

    def test_tags_must_be_tuple_of_strings(self):
        with pytest.raises(TypeError):
            DiscoveryQuery(tags=["a"])
        with pytest.raises(ValueError):
            DiscoveryQuery(tags=("",))

    def test_category_must_be_non_empty(self):
        with pytest.raises(ValueError):
            DiscoveryQuery(category="")

    def test_extra_filters_immutable(self):
        from types import MappingProxyType
        q = DiscoveryQuery(extra_filters={"region": "us"})
        assert isinstance(q.extra_filters, MappingProxyType)

    def test_is_frozen(self):
        q = DiscoveryQuery(category="test")
        with pytest.raises(Exception):
            q.category = "other"


# ---------------------------------------------------------------------------
# Structural Protocol contracts
# ---------------------------------------------------------------------------

class FakeDiscoveryProvider:
    """A provider that satisfies DiscoveryProvider structurally."""

    @property
    def identity(self) -> ProviderIdentity:
        return ProviderIdentity("fake")

    @property
    def capabilities(self) -> Capabilities:
        return Capabilities.DISCOVERY

    def discover_markets(self, query: DiscoveryQuery) -> tuple[Market, ...]:
        return (Market(CanonicalIdentifier(), "test question"),)


class FakePartialProvider:
    """A provider that only satisfies the base Provider contract."""

    @property
    def identity(self) -> ProviderIdentity:
        return ProviderIdentity("partial")

    @property
    def capabilities(self) -> Capabilities:
        return Capabilities.LOOKUP


class TestStructuralContracts:
    def test_discovery_provider_is_runtime_checkable(self):
        provider = FakeDiscoveryProvider()
        assert isinstance(provider, DiscoveryProvider)

    def test_base_provider_is_runtime_checkable(self):
        provider = FakeDiscoveryProvider()
        assert isinstance(provider, Provider)

    def test_partial_provider_satisfies_base(self):
        provider = FakePartialProvider()
        assert isinstance(provider, Provider)

    def test_partial_provider_does_not_satisfy_discovery(self):
        provider = FakePartialProvider()
        assert not isinstance(provider, DiscoveryProvider)

    def test_market_provider_satisfied_by_full_provider(self):
        provider = FakeDiscoveryProvider()
        assert isinstance(provider, MarketProvider)

    def test_non_provider_not_recognized(self):
        assert not isinstance("string", Provider)
        assert not isinstance(42, Provider)


# ---------------------------------------------------------------------------
# Error model
# ---------------------------------------------------------------------------

class TestProviderError:
    def test_base_error(self):
        err = ProviderError("something failed", provider_identity="alpha")
        assert err.message == "something failed"
        assert err.provider_identity == "alpha"

    def test_rejects_empty_message(self):
        with pytest.raises(ValueError):
            ProviderError("")

    def test_rejects_empty_identity(self):
        with pytest.raises(ValueError):
            ProviderError("msg", provider_identity="")

    def test_identity_optional(self):
        err = ProviderError("config error")
        assert err.provider_identity is None

    def test_value_equality(self):
        assert RateLimitError("too fast", "alpha") == RateLimitError("too fast", "alpha")

    def test_cross_type_inequality(self):
        assert RateLimitError("too fast", "alpha") != TransportError("too fast", "alpha")

    def test_different_message_inequality(self):
        assert RateLimitError("a", "alpha") != RateLimitError("b", "alpha")

    def test_hashable(self):
        err = RateLimitError("too fast", "alpha")
        assert hash(err) == hash(RateLimitError("too fast", "alpha"))

    def test_repr(self):
        err = TransportError("timeout", "alpha")
        r = repr(err)
        assert "TransportError" in r
        assert "timeout" in r

    def test_all_subclasses_inherit_base(self):
        for cls in [
            TransportError, AuthenticationError, RateLimitError,
            ProviderUnavailableError, NormalizationError,
            CapabilityNotSupportedError, MarketNotFoundError,
            ConfigurationError,
        ]:
            assert issubclass(cls, ProviderError)
            err = cls("test")
            assert isinstance(err, ProviderError)

    def test_market_not_found(self):
        err = MarketNotFoundError("not found", "alpha")
        assert isinstance(err, ProviderError)
        assert err.provider_identity == "alpha"
