"""Kolmogorov-Smirnov statistical data drift detector."""
from scipy.stats import ks_2samp
import numpy as np

def detect_drift(reference_col, production_col, p_threshold: float = 0.05):
    stat, p_value = ks_2samp(reference_col, production_col)
    drift_detected = p_value < p_threshold
    return {
        "ks_statistic": round(float(stat), 4),
        "p_value": round(float(p_value), 5),
        "drift_detected": bool(drift_detected)
    }
