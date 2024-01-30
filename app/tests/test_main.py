from fastapi.testclient import TestClient
from ..main import app  # Relative import of the FastAPI app
from dotenv import load_dotenv
import os

load_dotenv()

code_environment = os.getenv("CODE_ENVIRONMENT")    

client = TestClient(app)

def test_read_main():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!", "environment": code_environment, "version": 1.0} 
