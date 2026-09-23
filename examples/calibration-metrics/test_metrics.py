"""Tests for calibration metrics — defensive input handling and correctness."""

import math

import pytest

from metrics import (
    CalibrationBin,
    CalibrationMetrics,
    clamp_probability,
    compute_all_metrics,
    compute_brier_score,
    compute_calibration_curve,
    compute_hit_rate,
    compute_log_loss,
    compute_reliability,
    filter_valid_predictions,
    is_valid_probability,
)


# ---------------------------------------------------------------------------
# Probability validation
# ---------------------------------------------------------------------------

class TestIsValidProbability:
    def test_valid_integers(self):
        assert is_valid_probability(0) is True
        assert is_valid_probability(1) is True

    def test_valid_floats(self):
        assert is_valid_probability(0.0) is True
        assert is_valid_probability(1.0) is True
        assert is_valid_probability(0.5) is True
        assert is_valid_probability(0.999) is True

    def test_rejects_none(self):
        assert is_valid_probability(None) is False

    def test_rejects_booleans(self):
        assert is_valid_probability(True) is False
        assert is_valid_probability(False) is False

    def test_rejects_nan(self):
        assert is_valid_probability(float("nan")) is False

    def test_rejects_inf(self):
        assert is_valid_probability(float("inf")) is False
        assert is_valid_probability(float("-inf")) is False

    def test_rejects_out_of_range(self):
        assert is_valid_probability(-0.01) is False
        assert is_valid_probability(1.01) is False
        assert is_valid_probability(-1.0) is False
        assert is_valid_probability(2.0) is False

    def test_rejects_non_numeric(self):
        assert is_valid_probability("0.5") is False
        assert is_valid_probability([0.5]) is False


class TestClampProbability:
    def test_clamps_high(self):
        assert clamp_probability(1.5) == 1.0

    def test_clamps_low(self):
        assert clamp_probability(-0.5) == 0.0

    def test_in_range_unchanged(self):
        assert clamp_probability(0.3) == 0.3

    def test_rejects_nan(self):
        assert clamp_probability(float("nan")) is None

    def test_rejects_inf(self):
        assert clamp_probability(float("inf")) is None

    def test_rejects_bool(self):
        assert clamp_probability(True) is None


class TestFilterValidPredictions:
    def test_filters_invalid(self):
        preds = [0.5, float("nan"), 0.8, None, True, 1.2, 0.3]
        outs = [1, 1, 0, 0, 1, 1, 0]
        fp, fo = filter_valid_predictions(preds, outs)
        assert fp == [0.5, 0.8, 0.3]
        assert fo == [1, 0, 0]

    def test_filters_invalid_outcomes(self):
        preds = [0.5, 0.8, 0.3]
        outs = [1, 2, 0]
        fp, fo = filter_valid_predictions(preds, outs)
        assert fp == [0.5, 0.3]
        assert fo == [1, 0]

    def test_empty_input(self):
        fp, fo = filter_valid_predictions([], [])
        assert fp == []
        assert fo == []


# ---------------------------------------------------------------------------
# Brier score
# ---------------------------------------------------------------------------

class TestBrierScore:
    def test_perfect_predictions(self):
        assert compute_brier_score([1.0, 0.0], [1, 0]) == 0.0

    def test_worst_predictions(self):
        assert compute_brier_score([0.0, 1.0], [1, 0]) == 1.0

    def test_known_value(self):
        # (0.8 - 1)^2 + (0.3 - 0)^2 = 0.04 + 0.09 = 0.13 / 2 = 0.065
        assert compute_brier_score([0.8, 0.3], [1, 0]) == pytest.approx(0.065)

    def test_filters_nan(self):
        result = compute_brier_score([0.5, float("nan")], [1, 0])
        assert result == pytest.approx(0.25)

    def test_empty_returns_nan(self):
        assert math.isnan(compute_brier_score([], []))


# ---------------------------------------------------------------------------
# Hit rate
# ---------------------------------------------------------------------------

class TestHitRate:
    def test_all_correct(self):
        assert compute_hit_rate([0.9, 0.1], [1, 0]) == 1.0

    def test_all_wrong(self):
        assert compute_hit_rate([0.1, 0.9], [1, 0]) == 0.0

    def test_half_correct(self):
        assert compute_hit_rate([0.6, 0.4], [0, 1]) == 0.0
        assert compute_hit_rate([0.6, 0.6], [1, 0]) == 0.5

    def test_empty_returns_nan(self):
        assert math.isnan(compute_hit_rate([], []))


# ---------------------------------------------------------------------------
# Log loss
# ---------------------------------------------------------------------------

class TestLogLoss:
    def test_perfect_predictions_near_zero(self):
        # log loss for perfect predictions is very small but not exactly 0
        # due to the epsilon clamp
        result = compute_log_loss([1.0 - 1e-15, 1e-15], [1, 0])
        assert result < 1e-10

    def test_known_value(self):
        # -ln(0.5) ≈ 0.6931
        result = compute_log_loss([0.5, 0.5], [1, 0])
        assert result == pytest.approx(math.log(2), abs=1e-6)

    def test_empty_returns_nan(self):
        assert math.isnan(compute_log_loss([], []))


# ---------------------------------------------------------------------------
# Calibration curve
# ---------------------------------------------------------------------------

class TestCalibrationCurve:
    def test_empty_returns_empty(self):
        assert compute_calibration_curve([], []) == []

    def test_single_bin(self):
        curve = compute_calibration_curve([0.5, 0.5, 0.5], [1, 0, 1], n_bins=10)
        assert len(curve) == 1
        assert curve[0].bin_lower == 0.5
        assert curve[0].count == 3
        assert curve[0].predicted_mean == pytest.approx(0.5)
        assert curve[0].observed_frequency == pytest.approx(2 / 3)

    def test_bin_gap_property(self):
        b = CalibrationBin(0.0, 0.1, 0.05, 0.08, 10)
        assert b.gap == pytest.approx(0.03)

    def test_last_bin_includes_one(self):
        curve = compute_calibration_curve([1.0], [1], n_bins=10)
        assert len(curve) == 1
        assert curve[0].bin_lower == 0.9
        assert curve[0].bin_upper == 1.0


# ---------------------------------------------------------------------------
# Reliability (ECE / MCE)
# ---------------------------------------------------------------------------

class TestReliability:
    def test_perfect_calibration_zero_ece(self):
        # predictions exactly match outcomes → ECE = 0
        preds = [0.0, 0.0, 1.0, 1.0]
        outs = [0, 0, 1, 1]
        ece, mce = compute_reliability(preds, outs, n_bins=10)
        assert ece == pytest.approx(0.0)
        assert mce == pytest.approx(0.0)

    def test_empty_returns_nan(self):
        ece, mce = compute_reliability([], [])
        assert math.isnan(ece)
        assert math.isnan(mce)


# ---------------------------------------------------------------------------
# compute_all_metrics
# ---------------------------------------------------------------------------

class TestComputeAllMetrics:
    def test_returns_all_fields(self):
        preds = [0.9, 0.1, 0.8, 0.2]
        outs = [1, 0, 1, 0]
        m = compute_all_metrics(preds, outs)
        assert isinstance(m, CalibrationMetrics)
        assert m.sample_count == 4
        assert m.brier_score == pytest.approx(0.025)
        assert m.hit_rate == 1.0
        assert m.prediction_mean == pytest.approx(0.5)
        assert m.outcome_mean == 0.5
        assert len(m.calibration_curve) >= 1

    def test_filters_invalid(self):
        preds = [0.5, float("nan"), 0.8, None]
        outs = [1, 1, 0, 0]
        m = compute_all_metrics(preds, outs)
        assert m.sample_count == 2

    def test_all_invalid_returns_nan(self):
        preds = [float("nan"), None, True]
        outs = [1, 0, 1]
        m = compute_all_metrics(preds, outs)
        assert m.sample_count == 0
        assert math.isnan(m.brier_score)
        assert math.isnan(m.hit_rate)
        assert math.isnan(m.log_loss)

    def test_to_dict_serialization(self):
        preds = [0.9, 0.1]
        outs = [1, 0]
        m = compute_all_metrics(preds, outs)
        d = m.to_dict()
        assert "brier_score" in d
        assert "calibration_curve" in d
        assert isinstance(d["calibration_curve"], list)
