from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_submit_volunteer_form():
    payload = {
        "current_time": "2023-01-01 12:00:00",
        "person_name": "Test Person",
        "person_email": "test@email.co",
        "person_phone": "555-555-5555",
        "person_address": "123 Test St.",
        "person_dob": "01/01/2000",
        "dl_number": "123456789",
        "emergency_contact_name": "Test Emergency Contact",
        "emergency_contact_phone": "111-111-1111",
        "interested_bird_care": True,
        "interested_fundraising": False,
        "interested_fostering": True,
    }

    response = client.post("/forms/volunteer", json=payload)

    assert response.status_code == 201
    assert response.json() == {
        "message": "Volunteer form written to Google Sheet successfully!"
    }
