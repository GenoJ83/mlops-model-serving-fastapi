# MLOps Model Serving: Production FastAPI & Drift Monitoring

![FastAPI](https://img.shields.io/badge/FastAPI-Production-009688)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-E6522C)
![Drift](https://img.shields.io/badge/Drift-KS--Test-brightgreen)
![Docker](https://img.shields.io/badge/Deployment-Docker%20Compose-2496ED)

Production-grade MLOps deployment architecture featuring real-time REST inference, telemetry monitoring, and automated distribution drift detection.

## Architecture
```mermaid
flowchart TD
    Client[Client Request] --> API[FastAPI Microservice]
    API --> Schema[Pydantic Validation]
    Schema --> Model[Trained Pipeline]
    Model --> Prom[Prometheus Telemetry]
    API --> Drift[KS Drift Engine]
```

## Quick Start
```bash
docker-compose up --build
```
