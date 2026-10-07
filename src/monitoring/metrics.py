"""Prometheus metrics: request counter, latency histogram."""
from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter("ml_requests_total", "Total ML inference requests", ["endpoint", "status"])
INFERENCE_LATENCY = Histogram("ml_inference_latency_seconds", "Inference latency in seconds")
