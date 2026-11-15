"""Test suite for data schemas, drift detector, and FastAPI endpoints."""
from fastapi.testclient import TestClient
from src.app.main import app, get_model
from src.monitoring.drift_detector import detect_drift
import numpy as np

get_model()
client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_prediction_endpoint():
    payload = {
        "square_footage": 1800,
        "bedrooms": 3,
        "bathrooms": 2.0,
        "location_score": 7.5
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "predicted_price" in data
    assert data["predicted_price"] > 100000

def test_drift_detection():
    ref = np.random.normal(0, 1, 500)
    curr_same = np.random.normal(0, 1, 500)
    curr_drift = np.random.normal(3, 1, 500)

    assert not detect_drift(ref, curr_same)["drift_detected"]
    assert detect_drift(ref, curr_drift)["drift_detected"]
