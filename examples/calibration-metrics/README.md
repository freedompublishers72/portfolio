# Calibration Metrics

## What this demonstrates

Defensive numerical evaluation of probabilistic forecasts. The module
computes standard, published calibration metrics — Brier score, hit rate,
log loss, reliability diagram (calibration curve), Expected Calibration
Error (ECE), and Maximum Calibration Error (MCE) — with strict input
validation that rejects `NaN`, `inf`, booleans, `None`, and out-of-range
values before any computation.

## The engineering problem

Probabilistic forecast evaluation requires correct handling of edge-case
inputs. A naive `max(0, min(1, value))` clamp silently maps `NaN` to `1.0`
and `inf` to the bounds, corrupting every downstream metric. The
`is_valid_probability` / `clamp_probability` guards reject those values
explicitly so Brier scoring never receives an out-of-domain probability.

The calibration curve (reliability diagram) bins predictions into
equal-width intervals and compares the mean predicted probability against
the observed outcome frequency in each bin. A well-calibrated model has
`predicted_mean ≈ observed_frequency` in every bin.

## Important design decisions

- **Input validation at the boundary:** `filter_valid_predictions` strips
  invalid (prediction, outcome) pairs once, so every metric function
  operates on clean data without repeating validation.
- **Immutable result objects:** `CalibrationBin` is frozen;
  `CalibrationMetrics` carries the full evaluation as a serializable DTO.
- **Last-bin inclusivity:** the final bin includes `1.0` (closed interval)
  while all other bins are half-open `[lower, upper)` — preventing a
  prediction of exactly `1.0` from falling into no bin.

## How it differs from the original production context

The original module served a larger research engine that evaluated
forecasts against resolved outcomes. This demonstration isolates the
metrics and validation logic with no dependency on the engine's domain
objects, storage, or scheduling. The numerical code is preserved verbatim;
only internal architecture-document references in the module docstring were
removed.

## Files

- `metrics.py` — the metrics module
- `test_metrics.py` — focused tests for validation, correctness, and edge cases

## Running the tests

```bash
cd examples/calibration-metrics
python -m pytest test_metrics.py -v
```
