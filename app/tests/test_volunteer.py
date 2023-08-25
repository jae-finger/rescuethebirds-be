from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_translate_user_text():
    payload = {
        "name_first": "TEST",
        "name_middle": "TEST",
        "name_last": "TEST",
        "email": "TEST.TEST@TEST.com",
        "primary_phone": "555-555-5555",
        "street_address": "123 TEST St",
        "city": "TestTown",
        "state_province_region": "CA",
        "postal_zip_code": "12345",
        "country": "USA",
        "emergency_contact": "Jane TEST",
        "date_of_birth": "1980-01-01",
        "drivers_license": "123456789",
        "days_hours_preferred": "Weekends",
        "special_skills": "CPR certified",
        "languages": "English, Spanish",
        "other_experiences_skills": "Volunteered at animal shelter",
        "bird_care_interest": "Yes",
        "reference_1": "John Smith Sr.",
        "reference_2": "Jane Doe",
        "reference_3": "Bob Johnson",
    }

    response = client.post("/forms/volunteer", json=payload)

    assert response.status_code == 201
    assert response.json() == {"message": "Data written to Google Sheet successfully!"}