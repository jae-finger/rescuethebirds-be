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


def get_volunteer_worksheet(credentials=Depends(get_google_credentials)):
    # Authenticate with Google
    gc = gspread.service_account_from_dict(credentials)

    # Open the spreadsheet by its ID
    sh = gc.open_by_key(GOOGLE_SPREADSHEET_ID)

    # Get the specific worksheet
    worksheet = sh.worksheet("Volunteer Form")
    return worksheet


# Mock the adoption_worksheet
app.dependency_overrides[get_volunteer_worksheet] = lambda: MagicMock()


def test_volunteer_form_submission():
    client = TestClient(app)
    response = client.post(
        "/forms/volunteer",
        json={
            "person_name": "Test Person",
            "person_email": "test_email@email.com",
            "person_phone": "1234567890",
            "person_address": "123 Sheridan",
            "person_city": "Rogers Park",
            "person_state": "IL",
            "person_zipcode": "60626",
            "person_dob": "01/01/1900",
            "dl_number": "1234567890",
            "emergency_contact": "Emergency Contact",
            "brief_synopsis_of_birds": "Here's a Brief Synopsis of Birds...",
            "why_interested": "I'm interested in volunteering because...",
            "interested_bird_care": True,
            "interested_fundraising": False,
            "interested_fostering": True
            
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        "message": "Volunteer form written to Google Sheet successfully!"
    }
