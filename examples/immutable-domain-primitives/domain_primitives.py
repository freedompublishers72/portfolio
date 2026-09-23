"""
Immutable domain value objects with construction-time validation.

Each value object is a frozen dataclass that rejects invalid inputs
(NaN, infinity, out-of-range, wrong types) at construction time and
freezes its mutable detail mapping via ``MappingProxyType`` so the
object cannot be mutated after creation.

These primitives demonstrate defensive domain modeling: invariants are
enforced at the boundary (the constructor), not scattered across
consumers. Once constructed, the object is a trustworthy value that can
be passed freely without defensive copying.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any, Mapping
from uuid import UUID, uuid4


# ---------------------------------------------------------------------------
# Normalized [0, 1] value objects
# ---------------------------------------------------------------------------

@dataclass(frozen=True, slots=True)
class Probability:
    """Assessed likelihood of an outcome.

    Immutable. ``value`` is normalized to ``[0, 1]``. The optional
    ``detail`` mapping is frozen at construction time.
    """

    value: float
    detail: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.value, (int, float)):
            raise TypeError("Probability.value must be a number")
        if isinstance(self.value, float) and (math.isnan(self.value) or math.isinf(self.value)):
            raise ValueError("Probability.value must be finite")
        if not (0.0 <= self.value <= 1.0):
            raise ValueError("Probability.value must be in [0, 1]")
        if self.detail:
            object.__setattr__(self, "detail", MappingProxyType(dict(self.detail)))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Probability):
            return NotImplemented
        return self.value == other.value and self.detail == other.detail

    def __hash__(self) -> int:
        return hash(self.value)


@dataclass(frozen=True, slots=True)
class Confidence:
    """Assessed reliability of a valuation given its evidence.

    Immutable. ``level`` is normalized to ``[0, 1]`` (higher = more
    confident). A snapshot tied to a specific evidence set at a specific
    point in time — re-valuation with new evidence produces a new object,
    not a mutation.
    """

    level: float
    detail: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.level, (int, float)):
            raise TypeError("Confidence.level must be a number")
        if isinstance(self.level, float) and (math.isnan(self.level) or math.isinf(self.level)):
            raise ValueError("Confidence.level must be finite")
        if not (0.0 <= self.level <= 1.0):
            raise ValueError("Confidence.level must be in [0, 1]")
        if self.detail:
            object.__setattr__(self, "detail", MappingProxyType(dict(self.detail)))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Confidence):
            return NotImplemented
        return self.level == other.level and self.detail == other.detail

    def __hash__(self) -> int:
        return hash(self.level)


@dataclass(frozen=True, slots=True)
class Score:
    """Generic normalized numeric assessment with derivation context.

    Immutable. ``value`` is normalized to ``[0, 1]``. The optional
    ``derivation`` mapping records how the score was produced.
    """

    value: float
    derivation: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.value, (int, float)):
            raise TypeError("Score.value must be a number")
        if isinstance(self.value, float) and (math.isnan(self.value) or math.isinf(self.value)):
            raise ValueError("Score.value must be finite")
        if not (0.0 <= self.value <= 1.0):
            raise ValueError("Score.value must be in [0, 1]")
        if self.derivation:
            object.__setattr__(self, "derivation", MappingProxyType(dict(self.derivation)))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Score):
            return NotImplemented
        return self.value == other.value and self.derivation == other.derivation

    def __hash__(self) -> int:
        return hash(self.value)


# ---------------------------------------------------------------------------
# Signed divergence (unbounded range)
# ---------------------------------------------------------------------------

@dataclass(frozen=True, slots=True)
class Edge:
    """Signed divergence between a probability and a caller-supplied reference.

    Immutable. ``magnitude`` is the signed divergence (positive means the
    assessed probability is above the reference; negative means below).
    The range is unbounded — the divergence can be any real number.
    ``reference_value`` is stored for auditability.
    """

    magnitude: float
    reference_value: float
    detail: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.magnitude, (int, float)):
            raise TypeError("Edge.magnitude must be a number")
        if isinstance(self.magnitude, float) and (math.isnan(self.magnitude) or math.isinf(self.magnitude)):
            raise ValueError("Edge.magnitude must be finite")

        if not isinstance(self.reference_value, (int, float)):
            raise TypeError("Edge.reference_value must be a number")
        if isinstance(self.reference_value, float) and (math.isnan(self.reference_value) or math.isinf(self.reference_value)):
            raise ValueError("Edge.reference_value must be finite")

        if self.detail:
            object.__setattr__(self, "detail", MappingProxyType(dict(self.detail)))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Edge):
            return NotImplemented
        return (
            self.magnitude == other.magnitude
            and self.reference_value == other.reference_value
            and self.detail == other.detail
        )

    def __hash__(self) -> int:
        return hash((self.magnitude, self.reference_value))


# ---------------------------------------------------------------------------
# Opaque canonical identifier
# ---------------------------------------------------------------------------

@dataclass(frozen=True, slots=True)
class CanonicalIdentifier:
    """An opaque, canonical identifier for an entity.

    Immutable. The identifier is opaque to consumers — they use it for
    lookup but never inspect its structure. A UUID is auto-generated by
    default; callers may supply a specific UUID for deterministic
    construction (e.g., mapping a known external ID to a stable canonical ID).
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
