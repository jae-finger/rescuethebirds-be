from datetime import datetime
from fastapi import APIRouter
import ast
import os
import logging
from app.models.pydantic import VolunteerFormPayloadSchema, VolunteerFormResponseSchema
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

# open voluteer worksheet
volunteer_worksheet =  sh.worksheet("Volunteer Form")


@router.post("/volunteer", response_model=VolunteerFormResponseSchema, status_code=201)
async def translate_user_text(
    payload: VolunteerFormPayloadSchema,
) -> VolunteerFormPayloadSchema:
    """
    Take in volutneer form POST request and append data to row in Google Sheet
    """

    # extract data from payload
    name_first = payload.name_first
    name_middle = payload.name_middle
    name_last = payload.name_last
    email = payload.email
    primary_phone = payload.primary_phone
    street_address = payload.street_address
    city = payload.city
    state_province_region = payload.state_province_region
    postal_zip_code = payload.postal_zip_code
    country = payload.country
    emergency_contact = payload.emergency_contact
    date_of_birth = payload.date_of_birth
    drivers_license = payload.drivers_license
    days_hours_preferred = payload.days_hours_preferred
    special_skills = payload.special_skills
    languages = payload.languages
    other_experiences_skills = payload.other_experiences_skills
    bird_care_interest = payload.bird_care_interest
    reference_1 = payload.reference_1
    reference_2 = payload.reference_2
    reference_3 = payload.reference_3
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # write object to google sheet
    # add all of these to a new row in volunteer_worksheet
    volunteer_worksheet.append_row(
        [
            current_time,
            name_first,
            name_middle,
            name_last,
            email,
            primary_phone,
            street_address,
            city,
            state_province_region,
            postal_zip_code,
            country,
            emergency_contact,
            date_of_birth,
            drivers_license,
            days_hours_preferred,
            special_skills,
            languages,
            other_experiences_skills,
            bird_care_interest,
            reference_1,
            reference_2,
            reference_3,
        ]
    )

    # return response object saying data was written to google sheet
    response_object = {"message": "Data written to Google Sheet successfully!"}

    return response_object
