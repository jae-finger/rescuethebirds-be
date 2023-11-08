from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_submit_boarding_form():
    payload = {
        "person_name": "Test Person",
        "person_email": "email@email.com",
        "person_phone": "123-456-7890",
        "person_address": "123 Test St",
        "person_city": "Test City",
        "person_state": "Test State",
        "person_zipcode": "12345",
        "person_dob": "01/01/1990",
        "boarding_start_date": "01/01/2021",
        "boarding_end_date": "01/01/2021",
        "bird_list": [
            "Test bird 1",
            "Test bird 2",
            "Test bird 3",
        ],
    }

    response = client.post("/forms/boarding", json=payload)

    assert response.status_code == 201
    assert response.json() == {
        "message": "Boarding form written to Google Sheet successfully!"
    }
