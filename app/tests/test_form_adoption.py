from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_submit_adoption_form():
    payload = {
        "person_name": "Test Person",
        "person_dob": "1990-01-01",
        "person_email": "test@test.email",
        "person_phone": "123-456-7890",
        "person_address": "123 Test St",
        "person_city": "Test City",
        "person_state": "Test State",
        "person_zipcode": "12345",
        "hear_about_us": "Google",
        "num_household_people": "3",
        "primary_caregiver_age": "30",
        "ages_in_household": "30, 20, 10",
        "children_in_house": "True",
        "have_other_birds": "Yes",
        "previous_birds": "Parrot",
        "other_bird_experience": "Yes -- canaries",
        "avian_vet_info": "Dr. Birdface",
        "residence_type": "Apartment",
        "renter_verification": "True",
        "bird_hours_alone": "2",
        "smokers_in_house": "False",
        "other_pets_in_home": "Yes",
        "what_organizations": "???",
        "what_supp_info": "Wikipedia",
        "lifestyle_changes": "Nope",
        "vacation_care": "Sitter",
        "death_plans": "No idea",
    }

    response = client.post("/forms/adoption", json=payload)

    assert response.status_code == 201
    assert response.json() == {
        "message": "Adoption form written to Google Sheet successfully!"
    }
