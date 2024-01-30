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


def get_boarding_worksheet(credentials=Depends(get_google_credentials)):
    # Authenticate with Google
    gc = gspread.service_account_from_dict(credentials)

    # Open the spreadsheet by its ID
    sh = gc.open_by_key(GOOGLE_SPREADSHEET_ID)

    # Get the specific worksheet
    worksheet = sh.worksheet("Boarding Form")
    return worksheet


# Mock the adoption_worksheet
app.dependency_overrides[get_boarding_worksheet] = lambda: MagicMock()


def test_boarding_form_submission():
    client = TestClient(app)
    response = client.post(
        "/forms/boarding",
        json={
            "person_name": "Test Person",
            "person_email": "test_person@email.com",
            "person_phone": "1234567890",
            "person_address": "123 Sheridan",
            "person_city": "Rogers Park",
            "person_state": "IL",
            "person_zipcode": "60626",
            "boarding_start_date": "2099-01-01",
            "boarding_end_date": "2099-12-31",
            "bird_list" : ["tuxedo", "blue", "darcy"]
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        "message": "Boarding form written to Google Sheet successfully!"
    }
