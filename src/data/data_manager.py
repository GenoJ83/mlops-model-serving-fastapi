"""Tabular real estate dataset simulator for production MLOps pipeline."""
import pandas as pd
import numpy as np

def generate_reference_data(n_samples: int = 2000) -> pd.DataFrame:
    rng = np.random.default_rng(42)
    square_footage = rng.integers(500, 4500, size=n_samples)
    bedrooms = rng.integers(1, 6, size=n_samples)
    bathrooms = np.round(bedrooms * 0.75 + rng.uniform(0, 1, size=n_samples), 1)
    location_score = rng.uniform(1.0, 10.0, size=n_samples)

    price = 50000 + (square_footage * 180) + (bedrooms * 25000) + (location_score * 35000) + rng.normal(0, 15000, n_samples)

    return pd.DataFrame({
        "square_footage": square_footage,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "location_score": np.round(location_score, 2),
        "target_price": np.round(price, 2)
    })
