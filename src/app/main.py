"""Production FastAPI application with health checks and predictions."""
from fastapi import FastAPI
import joblib
import pandas as pd
from src.schemas.prediction_schema import PropertyPredictionInput, PropertyPredictionOutput
from src.registry.model_registry import ModelRegistry
from src.training.train_pipeline import train_and_register
import os

app = FastAPI(title="MLOps Property Valuation Service", version="1.0.0")
model = None

def get_model():
    global model
    if model is None:
        path = "models/pricing_model.joblib"
        if not os.path.exists(path):
            train_and_register()
        model = joblib.load(path)
    return model

@app.on_event("startup")
def startup():
    get_model()

@app.get("/health")
def health():
    meta = ModelRegistry.get_latest_metadata()
    return {"status": "healthy", "model_version": meta.get("version")}

@app.post("/predict", response_model=PropertyPredictionOutput)
def predict(payload: PropertyPredictionInput):
    m = get_model()
    df = pd.DataFrame([payload.model_dump()])
    price = float(m.predict(df)[0])
    return PropertyPredictionOutput(
        predicted_price=round(price, 2),
        model_version=ModelRegistry.get_latest_metadata().get("version", "v1.0.0")
    )
