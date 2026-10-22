"""Tests for real-time explainer."""
from src.app.explainer import RealTimeExplainer

def test_explainer():
    exp = RealTimeExplainer()
    inst = {"square_footage": 2000, "bedrooms": 3}
    att = exp.explain_instance(inst)
    assert att["square_footage"] == 360000.0
    assert att["bedrooms"] == 75000.0
