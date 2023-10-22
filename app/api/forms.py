from datetime import datetime
from fastapi import APIRouter
import ast
import os
import logging
from app.models.pydantic import (
    VolunteerFormPayloadSchema,
    VolunteerFormResponseSchema,
    BoardingFormPayloadSchema,
    BoardingFormResponseSchema,
    AdoptionFormPayloadSchema,
    AdoptionFormResponseSchema,
)
import gspread
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

log = logging.getLogger("uvicorn")

# Load google sheet based information
GOOGLE_CREDENTIAL_DICT = ast.literal_eval(os.getenv("GOOGLE_CREDENTIAL_DICT"))
GOOGLE_SPREADSHEET_ID = os.getenv("GOOGLE_SPREADSHEET_ID")
BASE_URL_PREFIX = os.getenv("BASE_URL_PREFIX")

# Authenticate with Google
gc = gspread.service_account_from_dict(GOOGLE_CREDENTIAL_DICT)
sh = gc.open_by_key(GOOGLE_SPREADSHEET_ID)

# open form google sheets
volunteer_worksheet = sh.worksheet("Volunteer Form")
boarding_worksheet = sh.worksheet("Boarding Form")
adoption_worksheet = sh.worksheet("Adoption Form")


@router.post("/volunteer", response_model=VolunteerFormResponseSchema, status_code=201)
async def submit_volunteer_form(
    payload: VolunteerFormPayloadSchema,
) -> VolunteerFormPayloadSchema:
    """
    Take in volutneer form POST request and append data to row in Google Sheet
    """

    # extract data from payload
    name_first = payload.name_first
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # add all of these to a new row in volunteer_worksheet
    volunteer_worksheet.append_row([current_time, name_first])

    # return response object saying data was written to google sheet
    response_object = {
        "message": "Volunteer form written to Google Sheet successfully!"
    }

    return response_object


@router.post("/boarding", response_model=BoardingFormResponseSchema, status_code=201)
async def submit_boarding_form(
    payload: BoardingFormPayloadSchema,
) -> BoardingFormPayloadSchema:
    """
    Take in boarding form POST request and append data to row in Google Sheet
    """

    # extract data from payload
    name_first = payload.name_first
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # add all of these to a new row in the appropriate google sheet
    volunteer_worksheet.append_row([current_time, name_first])

    # return response object saying data was written to google sheet
    response_object = {"message": "Boarding form written to Google Sheet successfully!"}

    return response_object


@router.post("/adoption", response_model=AdoptionFormResponseSchema, status_code=201)
async def submit_adoption_form(
    payload: AdoptionFormPayloadSchema,
) -> AdoptionFormPayloadSchema:
    """
    Take in adoption form POST request and append data to row in Google Sheet
    """

    # extract data from payload
    name_first = payload.name_first
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # add all of these to a new row in the appropriate google sheet
    adoption_worksheet.append_row([current_time, name_first])

    # return response object saying data was written to google sheet
    response_object = {"message": "Adoption form written to Google Sheet successfully!"}

    return response_object
