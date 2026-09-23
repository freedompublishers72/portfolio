"""
Calibration metrics for probabilistic forecast evaluation.

Implements standard, published calibration metrics:
- Brier score (mean squared error of probabilistic predictions)
- Hit rate (accuracy at 0.5 threshold)
- Log loss (cross-entropy)
- Calibration curve (reliability diagram: predicted vs. actual in bins)
- Reliability (calibration-in-the-large, calibration slope)

All probability inputs are validated to be finite numbers in ``[0, 1]``
before any metric is computed.  Invalid predictions (NaN, infinity,
out-of-range, or non-numeric) are filtered out so that Brier scoring
never receives an out-of-domain probability.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Probability validation helpers
# ---------------------------------------------------------------------------

def is_valid_probability(value) -> bool:
    """Return ``True`` iff *value* is a finite probability in ``[0, 1]``.

    Rejects ``None``, booleans, non-numeric types, ``NaN``, ``inf``, and
    values outside the closed interval ``[0, 1]``.
    """
    if value is None or isinstance(value, bool):
        return False
    if not isinstance(value, (int, float)):
        return False
    p = float(value)
    return math.isfinite(p) and 0.0 <= p <= 1.0


def clamp_probability(value) -> float | None:
    """Clamp *value* to ``[0, 1]`` and return the result, or ``None`` if
    *value* is not a finite numeric value.

    Finite out-of-range values are clamped to the nearest bound.
    ``NaN``, ``inf``, ``-inf``, ``None``, booleans, and non-numeric types
    are rejected (return ``None``).

    This is stricter than ``max(0, min(1, value))`` because that idiom
    silently maps ``NaN`` to ``1.0`` (or ``0.0`` depending on argument
    order) and maps ``inf``/``-inf`` to the bounds.  ``clamp_probability``
    rejects those values instead.
    """
    if value is None or isinstance(value, bool):
        return None
    if not isinstance(value, (int, float)):
        return None
    p = float(value)
    if not math.isfinite(p):
        return None
    return max(0.0, min(1.0, p))


def filter_valid_predictions(
    predictions: list[float],
    outcomes: list[int],
) -> tuple[list[float], list[int]]:
    """Filter (prediction, outcome) pairs to keep only valid probabilities.

    Returns a new ``(predictions, outcomes)`` pair where every prediction
    is a finite number in ``[0, 1]`` and every outcome is ``0`` or ``1``.
    """
    valid_preds: list[float] = []
    valid_outcomes: list[int] = []
    for p, o in zip(predictions, outcomes):
        if not is_valid_probability(p):
            continue
        if o not in (0, 1):
            continue
        valid_preds.append(float(p))
        valid_outcomes.append(int(o))
    return valid_preds, valid_outcomes


@dataclass(frozen=True)
class CalibrationBin:
    """A single bin in a calibration curve (reliability diagram)."""

    bin_lower: float
    bin_upper: float
    predicted_mean: float
    observed_frequency: float
    count: int

    @property
    def gap(self) -> float:
        """Absolute gap between predicted and observed (calibration error)."""
        return abs(self.predicted_mean - self.observed_frequency)


@dataclass
class CalibrationMetrics:
    """Full calibration metrics for a set of predictions vs. outcomes."""

    brier_score: float
    hit_rate: float
    log_loss: float
    sample_count: int
    calibration_curve: list[CalibrationBin] = field(default_factory=list)
    expected_calibration_error: float = 0.0
    maximum_calibration_error: float = 0.0
    prediction_mean: float = 0.0
    outcome_mean: float = 0.0

    def to_dict(self) -> dict:
        return {
            "brier_score": round(self.brier_score, 6),
            "hit_rate": round(self.hit_rate, 4),
            "log_loss": round(self.log_loss, 6),
            "sample_count": self.sample_count,
            "expected_calibration_error": round(self.expected_calibration_error, 6),
            "maximum_calibration_error": round(self.maximum_calibration_error, 6),
            "prediction_mean": round(self.prediction_mean, 4),
            "outcome_mean": round(self.outcome_mean, 4),
            "calibration_curve": [
                {
                    "bin_lower": round(b.bin_lower, 2),
                    "bin_upper": round(b.bin_upper, 2),
                    "predicted_mean": round(b.predicted_mean, 4),
                    "observed_frequency": round(b.observed_frequency, 4),
                    "count": b.count,
                }
                for b in self.calibration_curve
            ],
        }


def compute_brier_score(predictions: list[float], outcomes: list[int]) -> float:
    """Compute Brier score (lower is better, 0 = perfect, 1 = worst).

    Args:
        predictions: predicted probabilities in [0, 1]
        outcomes: actual outcomes (1 = YES, 0 = NO)

    Returns:
        Mean squared error of predictions.

    Invalid predictions (NaN, inf, out-of-range, non-numeric) are
    filtered out before computation so Brier never receives an
    out-of-domain probability.
    """
    preds, outs = filter_valid_predictions(predictions, outcomes)
    if not preds:
        return float("nan")
    return sum((p - o) ** 2 for p, o in zip(preds, outs)) / len(preds)


def compute_hit_rate(predictions: list[float], outcomes: list[int]) -> float:
    """Compute hit rate (accuracy at 0.5 threshold).

    Args:
        predictions: predicted probabilities in [0, 1]
        outcomes: actual outcomes (1 = YES, 0 = NO)

    Returns:
        Fraction of correct binary predictions.
    """
    if not predictions:
        return float("nan")
    correct = sum(1 for p, o in zip(predictions, outcomes) if (p >= 0.5) == (o == 1))
    return correct / len(predictions)


def compute_log_loss(predictions: list[float], outcomes: list[int]) -> float:
    """Compute log loss (cross-entropy, lower is better).

    Args:
        predictions: predicted probabilities in [0, 1]
        outcomes: actual outcomes (1 = YES, 0 = NO)

    Returns:
        Mean cross-entropy loss.
    """
    if not predictions:
        return float("nan")
    total = 0.0
    for p, o in zip(predictions, outcomes):
        p = max(min(p, 1 - 1e-15), 1e-15)
        if o == 1:
            total += -math.log(p)
        else:
            total += -math.log(1 - p)
    return total / len(predictions)


def compute_calibration_curve(
    predictions: list[float],
    outcomes: list[int],
    n_bins: int = 10,
) -> list[CalibrationBin]:
    """Compute calibration curve (reliability diagram).

    Divides predictions into n_bins equal-width bins from 0 to 1.
    For each bin, computes the mean predicted probability and the
    observed outcome frequency.

    A well-calibrated model has predicted_mean ≈ observed_frequency
    in each bin.

    Args:
        predictions: predicted probabilities in [0, 1]
        outcomes: actual outcomes (1 = YES, 0 = NO)
        n_bins: number of bins (default 10)

    Returns:
        List of CalibrationBin, one per non-empty bin.
    """
    if not predictions:
        return []

    bin_width = 1.0 / n_bins
    bins: list[CalibrationBin] = []

    for i in range(n_bins):
        lower = i * bin_width
        upper = (i + 1) * bin_width
        if i == n_bins - 1:
            # Include 1.0 in the last bin
            indices = [
                j for j, p in enumerate(predictions)
                if lower <= p <= upper
            ]
        else:
            indices = [
                j for j, p in enumerate(predictions)
                if lower <= p < upper
            ]

        if not indices:
            continue

        pred_mean = sum(predictions[j] for j in indices) / len(indices)
        obs_freq = sum(outcomes[j] for j in indices) / len(indices)
        bins.append(CalibrationBin(
            bin_lower=lower,
            bin_upper=upper,
            predicted_mean=pred_mean,
            observed_frequency=obs_freq,
            count=len(indices),
        ))

    return bins


def compute_reliability(
    predictions: list[float],
    outcomes: list[int],
    n_bins: int = 10,
) -> tuple[float, float]:
    """Compute Expected Calibration Error (ECE) and Maximum Calibration Error (MCE).

    ECE: weighted average of |predicted_mean - observed_frequency| per bin.
    MCE: maximum of |predicted_mean - observed_frequency| per bin.

    Args:
        predictions: predicted probabilities in [0, 1]
        outcomes: actual outcomes (1 = YES, 0 = NO)
        n_bins: number of bins

    Returns:
        (ECE, MCE)
    """
    curve = compute_calibration_curve(predictions, outcomes, n_bins)
    if not curve:
        return float("nan"), float("nan")

    total = sum(b.count for b in curve)
    if total == 0:
        return float("nan"), float("nan")

    ece = sum(b.gap * b.count for b in curve) / total
    mce = max(b.gap for b in curve)
    return ece, mce


def compute_all_metrics(
    predictions: list[float],
    outcomes: list[int],
    n_bins: int = 10,
) -> CalibrationMetrics:
    """Compute all calibration metrics for a set of predictions vs. outcomes.

    Args:
        predictions: predicted probabilities in [0, 1]
        outcomes: actual outcomes (1 = YES, 0 = NO)
        n_bins: number of calibration curve bins

    Returns:
        CalibrationMetrics with all computed metrics.

    Invalid predictions (NaN, infinity, out-of-range, or non-numeric) are
    filtered out before any metric is computed so that Brier scoring never
    receives an out-of-domain probability.
    """
    preds, outs = filter_valid_predictions(predictions, outcomes)
    if not preds:
        return CalibrationMetrics(
            brier_score=float("nan"),
            hit_rate=float("nan"),
            log_loss=float("nan"),
            sample_count=0,
        )

    brier = compute_brier_score(preds, outs)
    hit = compute_hit_rate(preds, outs)
    ll = compute_log_loss(preds, outs)
    curve = compute_calibration_curve(preds, outs, n_bins)
    ece, mce = compute_reliability(preds, outs, n_bins)
    pred_mean = sum(preds) / len(preds)
    outcome_mean = sum(outs) / len(outs)

    return CalibrationMetrics(
        brier_score=brier,
        hit_rate=hit,
        log_loss=ll,
        sample_count=len(preds),
        calibration_curve=curve,
        expected_calibration_error=ece,
        maximum_calibration_error=mce,
        prediction_mean=pred_mean,
        outcome_mean=outcome_mean,
    )
