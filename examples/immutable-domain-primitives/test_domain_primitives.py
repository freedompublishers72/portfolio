"""Tests for immutable domain primitives — validation, immutability, equality."""

import math
from types import MappingProxyType
from uuid import uuid4

import pytest

from domain_primitives import (
    CanonicalIdentifier,
    Confidence,
    Edge,
    Probability,
    Score,
)


# ---------------------------------------------------------------------------
# Construction validation
# ---------------------------------------------------------------------------

class TestProbabilityValidation:
    def test_valid_construction(self):
        p = Probability(0.5)
        assert p.value == 0.5

    def test_accepts_int(self):
        p = Probability(0)
        assert p.value == 0.0

    def test_rejects_nan(self):
        with pytest.raises(ValueError, match="finite"):
            Probability(float("nan"))

    def test_rejects_inf(self):
        with pytest.raises(ValueError, match="finite"):
            Probability(float("inf"))

    def test_rejects_out_of_range_high(self):
        with pytest.raises(ValueError, match=r"\[0, 1\]"):
            Probability(1.01)

    def test_rejects_out_of_range_low(self):
        with pytest.raises(ValueError, match=r"\[0, 1\]"):
            Probability(-0.01)

    def test_rejects_string(self):
        with pytest.raises(TypeError):
            Probability("0.5")

    def test_boundary_values(self):
        Probability(0.0)
        Probability(1.0)


class TestConfidenceValidation:
    def test_valid_construction(self):
        c = Confidence(0.8)
        assert c.level == 0.8

    def test_rejects_nan(self):
        with pytest.raises(ValueError, match="finite"):
            Confidence(float("nan"))

    def test_rejects_out_of_range(self):
        with pytest.raises(ValueError, match=r"\[0, 1\]"):
            Confidence(1.5)


class TestScoreValidation:
    def test_valid_construction(self):
        s = Score(0.7)
        assert s.value == 0.7

    def test_rejects_nan(self):
        with pytest.raises(ValueError, match="finite"):
            Score(float("nan"))


class TestEdgeValidation:
    def test_valid_construction(self):
        e = Edge(magnitude=0.15, reference_value=0.5)
        assert e.magnitude == 0.15
        assert e.reference_value == 0.5

    def test_negative_magnitude_allowed(self):
        e = Edge(magnitude=-0.3, reference_value=0.6)
        assert e.magnitude == -0.3

    def test_rejects_nan_magnitude(self):
        with pytest.raises(ValueError, match="finite"):
            Edge(magnitude=float("nan"), reference_value=0.5)

    def test_rejects_nan_reference(self):
        with pytest.raises(ValueError, match="finite"):
            Edge(magnitude=0.1, reference_value=float("nan"))

    def test_rejects_string_magnitude(self):
        with pytest.raises(TypeError):
            Edge(magnitude="0.1", reference_value=0.5)


class TestCanonicalIdentifier:
    def test_auto_generated_uuid(self):
        ident = CanonicalIdentifier()
        assert ident.value is not None

    def test_two_auto_generated_are_different(self):
        a = CanonicalIdentifier()
        b = CanonicalIdentifier()
        assert a != b

    def test_explicit_uuid(self):
        u = uuid4()
        ident = CanonicalIdentifier(value=u)
        assert ident.value == u

    def test_str_representation(self):
        u = uuid4()
        ident = CanonicalIdentifier(value=u)
        assert str(ident) == str(u)

    def test_rejects_non_uuid(self):
        with pytest.raises(TypeError):
            CanonicalIdentifier(value="not-a-uuid")


# ---------------------------------------------------------------------------
# Immutability
# ---------------------------------------------------------------------------

class TestImmutability:
    def test_probability_is_frozen(self):
        p = Probability(0.5)
        with pytest.raises(Exception):
            p.value = 0.6

    def test_confidence_is_frozen(self):
        c = Confidence(0.8)
        with pytest.raises(Exception):
            c.level = 0.9

    def test_score_is_frozen(self):
        s = Score(0.7)
        with pytest.raises(Exception):
            s.value = 0.8

    def test_edge_is_frozen(self):
        e = Edge(0.1, 0.5)
        with pytest.raises(Exception):
            e.magnitude = 0.2

    def test_detail_is_mapping_proxy(self):
        p = Probability(0.5, detail={"source": "test"})
        assert isinstance(p.detail, MappingProxyType)

    def test_detail_is_immutable(self):
        p = Probability(0.5, detail={"source": "test"})
        with pytest.raises(TypeError):
            p.detail["source"] = "other"

    def test_derivation_is_mapping_proxy(self):
        s = Score(0.7, derivation={"method": "weighted"})
        assert isinstance(s.derivation, MappingProxyType)


# ---------------------------------------------------------------------------
# Equality and hashing
# ---------------------------------------------------------------------------

class TestEquality:
    def test_probability_value_equality(self):
        assert Probability(0.5) == Probability(0.5)

    def test_probability_value_inequality(self):
        assert Probability(0.5) != Probability(0.6)

    def test_probability_detail_equality(self):
        assert Probability(0.5, detail={"a": 1}) == Probability(0.5, detail={"a": 1})

    def test_probability_detail_inequality(self):
        assert Probability(0.5, detail={"a": 1}) != Probability(0.5, detail={"a": 2})

    def test_confidence_equality(self):
        assert Confidence(0.8) == Confidence(0.8)

    def test_score_equality(self):
        assert Score(0.7) == Score(0.7)

    def test_edge_equality(self):
        assert Edge(0.1, 0.5) == Edge(0.1, 0.5)

    def test_edge_inequality_different_magnitude(self):
        assert Edge(0.1, 0.5) != Edge(0.2, 0.5)

    def test_edge_inequality_different_reference(self):
        assert Edge(0.1, 0.5) != Edge(0.1, 0.6)

    def test_cross_type_inequality(self):
        assert Probability(0.5) != Confidence(0.5)
        assert Probability(0.5) != "0.5"

    def test_identifier_equality(self):
        u = uuid4()
        assert CanonicalIdentifier(u) == CanonicalIdentifier(u)

    def test_identifier_inequality(self):
        assert CanonicalIdentifier() != CanonicalIdentifier()


class TestHashing:
    def test_probability_hashable(self):
        p = Probability(0.5)
        assert hash(p) == hash(Probability(0.5))

    def test_edge_hashable(self):
        e = Edge(0.1, 0.5)
        assert hash(e) == hash(Edge(0.1, 0.5))

    def test_identifier_hashable(self):
        u = uuid4()
        ident = CanonicalIdentifier(u)
        assert hash(ident) == hash(CanonicalIdentifier(u))

    def test_usable_in_set(self):
        s = {Probability(0.5), Probability(0.5), Probability(0.6)}
        assert len(s) == 2
