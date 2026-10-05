"""Strict Pydantic input/output contracts with runtime type validation."""
from pydantic import BaseModel, Field

class PropertyPredictionInput(BaseModel):
    square_footage: int = Field(..., gt=100, lt=20000, description="Square footage of the property")
    bedrooms: int = Field(..., ge=1, le=12, description="Number of bedrooms")
    bathrooms: float = Field(..., ge=0.5, le=10.0, description="Number of bathrooms")
    location_score: float = Field(..., ge=0.0, le=10.0, description="School and neighborhood rating")

class PropertyPredictionOutput(BaseModel):
    predicted_price: float
    model_version: str
    currency: str = "USD"
