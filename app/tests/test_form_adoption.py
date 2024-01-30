import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from ..main import app
import gspread
from fastapi import Depends
from dotenv import load_dotenv
import json
import os
import ast

load_dotenv()


# Load google sheet based information
if os.getenv("CODE_ENVIRONMENT") == "prod":
    GOOGLE_CREDENTIAL_DICT = ast.literal_eval(os.getenv("GOOGLE_CREDENTIAL_DICT"))
elif os.getenv("CODE_ENVIRONMENT") == "dev":
    with open("credentials.json", "r") as creds:
        GOOGLE_CREDENTIAL_DICT = json.load(creds)
else:
    raise Exception("CODE_ENVIRONMENT not set properly!")

GOOGLE_SPREADSHEET_ID = os.getenv("GOOGLE_SPREADSHEET_ID")
BASE_URL_PREFIX = os.getenv("BASE_URL_PREFIX")


def get_google_credentials():
    # Load Google credentials
    credentials = GOOGLE_CREDENTIAL_DICT
    return credentials


def get_adoption_worksheet(credentials=Depends(get_google_credentials)):
    # Authenticate with Google
    gc = gspread.service_account_from_dict(credentials)

    # Open the spreadsheet by its ID
    sh = gc.open_by_key(GOOGLE_SPREADSHEET_ID)

    # Get the specific worksheet
    worksheet = sh.worksheet("Adoption Form")
    return worksheet


# Mock the adoption_worksheet
app.dependency_overrides[get_adoption_worksheet] = lambda: MagicMock()


def test_adoption_form_submission():
    client = TestClient(app)
    response = client.post(
        "/forms/adoption",
        json={
            "person_name": "Test Person",
            "person_dob": "01/01/1900",
            "person_email": "test_email@emails.com",
            "person_phone": "1234567890",
            "person_address": "123 Sheridan",
            "person_city": "Rogers Park",
            "person_state": "IL",
            "person_zipcode": "12345",
            "hear_about_us": "Google",
            "num_household_people": "2",
            "primary_caregiver_age": "30",
            "ages_in_household": "30, 37",
            "children_in_house": "0",
            "have_other_birds": "Yes",
            "previous_birds": "Canary",
            "other_bird_experience": "Yes; plenty of experience",
            "avian_vet_info": "Dr. Test Vet",
            "residence_type": "Apartment",
            "renter_verification": "Yes",
            "daily_routine": "Wake up, put on a little make up",
            "weekend_routine": "Friday Friday Friday Ohhhh",
            "bird_hours_alone": "Never alone!",
            "smokers_in_house": "Eww smoke",
            "other_pets_in_home": "A poodle",
            "what_supp_info": "No supporting info",
            "lifestyle_changes": "No lifestyle changes",
            "vacation_care": "Vacation care is set",
            "death_plans": "I have a death plan",
            "looking_for_in_bird": "Im looking for a stylish bird",
            "additional_comments": "Hello!",
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        "message": "Adoption form written to Google Sheet successfully!"
    }
