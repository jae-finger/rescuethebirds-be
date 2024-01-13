from fastapi.testclient import TestClient
from ..main import app  # Relative import of the FastAPI app

client = TestClient(app)

def test_read_main():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!", "environment": "dev"} 
