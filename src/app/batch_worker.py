"""Asynchronous batch inference processor."""
from typing import List, Dict
import pandas as pd

def process_batch_scoring(model, records: List[Dict]):
    df = pd.DataFrame(records)
    preds = model.predict(df)
    return [round(float(p), 2) for p in preds]
