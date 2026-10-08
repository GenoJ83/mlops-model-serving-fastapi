from locust import HttpUser, task, between

class MLUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task(3)
    def predict(self):
        self.client.post("/predict", json={
            "square_footage": 2400,
            "bedrooms": 3,
            "bathrooms": 2.5,
            "location_score": 8.5
        })

    @task(1)
    def health(self):
        self.client.get("/health")
