from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_submit_volunteer_form():
    payload = {
        "person_name": "Test Person",
        "person_email": "test@email.co",
        "person_phone": "555-555-5555",
        "person_address": "123 Test St.",
        "person_city": "Test City",
        "person_state": "Test State",
        "person_zipcode": "12345",
        "person_dob": "01/01/2000",
        "dl_number": "123456789",
        "emergency_contact": "Test Emergency Contact",
        "brief_synopsis_of_birds": "Test synopsis of birds",
        "why_interested": "Test why interested",
        "interested_bird_care": "True",
        "interested_fundraising": "False",
        "interested_fostering": "True",
    }

    response = client.post("/forms/volunteer", json=payload)

    assert response.status_code == 201
    assert response.json() == {
        "message": "Volunteer form written to Google Sheet successfully!"
    }
