"""Model artifact versioning and metadata management."""
import json
import os

class ModelRegistry:
    METADATA_FILE = "models/metadata.json"

    @classmethod
    def register_version(cls, version: str, metrics: dict, artifact_path: str):
        meta = {
            "version": version,
            "metrics": metrics,
            "artifact_path": artifact_path
        }
        os.makedirs("models", exist_ok=True)
        with open(cls.METADATA_FILE, "w") as f:
            json.dump(meta, f, indent=2)

    @classmethod
    def get_latest_metadata(cls):
        if not os.path.exists(cls.METADATA_FILE):
            return {"version": "v1.0.0", "metrics": {}}
        with open(cls.METADATA_FILE, "r") as f:
            return json.load(f)
