
from fastapi.testclient import TestClient

from src.app import app  # Import your FastAPI app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello, from FastAPI-Lambda-AWS-Terraform"

def test_second_route():
    response = client.get("/second")
    assert response.status_code == 200
    assert response.json() == "Second Hello, from FastAPI-Lambda-AWS-Terraform"

