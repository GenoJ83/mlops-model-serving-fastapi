"""Real-time linear feature attribution generator."""
from typing import Dict, Any

class RealTimeExplainer:
    def __init__(self, coefficients: Dict[str, float] = None):
        self.coefficients = coefficients or {
            "square_footage": 180.0,
            "bedrooms": 25000.0,
            "bathrooms": 15000.0,
            "location_score": 35000.0
        }

    def explain_instance(self, features: Dict[str, Any]) -> Dict[str, float]:
        attributions = {}
        for k, v in features.items():
            if k in self.coefficients:
                attributions[k] = round(float(v) * self.coefficients[k], 2)
        return attributions
