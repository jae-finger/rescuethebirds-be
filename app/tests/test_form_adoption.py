from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_submit_adoption_form():
    payload = {
        "current_time": "2023-01-01 12:00:00",
        "person_name": "Test Person",
        "person_email": "test@test.email",
        "person_phone": "123-456-7890",
        "person_address": "123 Test St",
        "hear_about_us": "Google",
        "num_household_people": "3",
        "primary_caregiver_age": "30",
        "ages_in_household": "30, 20, 10",
        "children_in_house": True,
        "have_other_birds": "Yes",
        "other_birds_species": "Cockatiel",
        "other_birds_checkup_date": "2022-01-01",
        "other_birds_diet": "Seeds",
        "previous_birds": "Parrot",
        "previous_birds_history": "Died of old age",
        "other_bird_experience": "Yes -- canaries",
        "has_avian_vet": True,
        "avian_vet_info": "Dr. Birdface",
        "residence_type": "Apartment",
        "renter_verification": True,
        "bird_hours_alone": "2",
        "smokers_in_house": False,
        "smoker_explanation": "N/A",
        "other_pets_in_home": True,
        "other_pets_explanation": "N/A",
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
