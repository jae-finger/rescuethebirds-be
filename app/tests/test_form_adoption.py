from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_submit_adoption_form():
    payload = {"current_time": "2023-01-01 12:00:00", "name_first": "TEST"}

    response = client.post("/forms/adoption", json=payload)

    assert response.status_code == 201
    assert response.json() == {
        "message": "Adoption form written to Google Sheet successfully!"
    }
