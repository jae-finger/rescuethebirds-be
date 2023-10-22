from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_submit_volunteer_form():
    payload = {"current_time": "2023-01-01 12:00:00", "name_first": "TEST"}

    response = client.post("/forms/boarding", json=payload)

    assert response.status_code == 201
    assert response.json() == {
        "message": "Boarding form written to Google Sheet successfully!"
    }
