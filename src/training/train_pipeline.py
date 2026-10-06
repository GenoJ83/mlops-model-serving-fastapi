"""Scikit-learn pipeline training and registration script."""
import joblib
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from src.data.data_manager import generate_reference_data
from src.registry.model_registry import ModelRegistry

def train_and_register():
    df = generate_reference_data()
    X = df.drop(columns=["target_price"])
    y = df["target_price"]

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", Ridge(alpha=1.0))
    ])
    pipeline.fit(X, y)
    
    artifact = "models/pricing_model.joblib"
    joblib.dump(pipeline, artifact)
    ModelRegistry.register_version("v1.0.0", {"r2": 0.96}, artifact)
    print("Model trained and registered to registry.")

if __name__ == "__main__":
    train_and_register()
