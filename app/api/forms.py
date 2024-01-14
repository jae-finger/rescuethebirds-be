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
import json

load_dotenv()

router = APIRouter()

log = logging.getLogger("uvicorn")

# Load google sheet based information
if os.getenv("CODE_ENVIRONMENT") == "prod":
    GOOGLE_CREDENTIAL_DICT = ast.literal_eval(os.getenv("GOOGLE_CREDENTIAL_DICT"))
elif os.getenv("CODE_ENVIRONMENT") == "dev":
    with open('credentials.json', 'r') as creds:
        GOOGLE_CREDENTIAL_DICT = json.load(creds)
else:
    raise Exception("CODE_ENVIRONMENT not set properly!")

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
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    person_name = payload.person_name
    person_email = payload.person_email
    person_phone = payload.person_phone
    person_address = payload.person_address
    person_city = payload.person_city
    person_state = payload.person_state
    person_zipcode = payload.person_zipcode
    person_dob = payload.person_dob
    dl_number = payload.dl_number
    emergency_contact = payload.emergency_contact
    brief_synopsis_of_birds = payload.brief_synopsis_of_birds
    why_interested = payload.why_interested

    interested_bird_care = payload.interested_bird_care
    interested_fundraising = payload.interested_fundraising
    interested_fostering = payload.interested_fostering

    try:
        # add all of these to a new row in volunteer_worksheet
        volunteer_worksheet.append_row(
            [
                current_time,
                person_name,
                person_email,
                person_phone,
                person_address,
                person_city,
                person_state,
                person_zipcode,
                person_dob,
                dl_number,
                emergency_contact,
                brief_synopsis_of_birds,
                why_interested,
                interested_bird_care,
                interested_fundraising,
                interested_fostering,
            ]
        )

        # return response object saying data was written to google sheet
        response_object = {
            "message": "Volunteer form written to Google Sheet successfully!"
        }

    # except and then return the error
    except Exception as e:
        response_object = {"message": f"Error: {e}"}

    return response_object


@router.post("/boarding", response_model=BoardingFormResponseSchema, status_code=201)
async def submit_boarding_form(
    payload: BoardingFormPayloadSchema,
) -> BoardingFormPayloadSchema:
    """
    Take in boarding form POST request and append data to row in Google Sheet
    """

    # extract data from payload
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    person_name = payload.person_name
    person_email = payload.person_email
    person_phone = payload.person_phone
    person_address = payload.person_address
    person_city = payload.person_city
    person_state = payload.person_state
    person_zipcode = payload.person_zipcode
    boarding_start_date = payload.boarding_start_date
    boarding_end_date = payload.boarding_end_date
    bird_list = ", ".join(payload.bird_list)

    # add all of these to a new row in the appropriate google sheet
    try:
        boarding_worksheet.append_row(
            [
                current_time,
                person_name,
                person_email,
                person_phone,
                person_address,
                person_city,
                person_state,
                person_zipcode,
                boarding_start_date,
                boarding_end_date,
                bird_list
            ]
        )

        # return response object saying data was written to google sheet
        response_object = {
            "message": "Boarding form written to Google Sheet successfully!"
        }

    # except and then return the error
    except Exception as e:
        response_object = {"message": f"Error: {e}"}

    return response_object


@router.post("/adoption", response_model=AdoptionFormResponseSchema, status_code=201)
async def submit_adoption_form(
    payload: AdoptionFormPayloadSchema,
) -> AdoptionFormPayloadSchema:
    """
    Take in adoption form POST request and append data to row in Google Sheet
    """

    # extract data from payload
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    person_name = payload.person_name
    person_email = payload.person_email
    person_phone = payload.person_phone
    person_address = payload.person_address
    person_city = payload.person_city
    person_state = payload.person_state
    person_zipcode = payload.person_zipcode
    hear_about_us = payload.hear_about_us
    num_household_people = payload.num_household_people
    primary_caregiver_age = payload.primary_caregiver_age
    ages_in_household = payload.ages_in_household
    children_in_house = payload.children_in_house
    have_other_birds = payload.have_other_birds
    previous_birds = payload.previous_birds
    other_bird_experience = payload.other_bird_experience
    avian_vet_info = payload.avian_vet_info
    residence_type = payload.residence_type
    renter_verification = payload.renter_verification
    bird_hours_alone = payload.bird_hours_alone
    smokers_in_house = payload.smokers_in_house
    other_pets_in_home = payload.other_pets_in_home
    what_organizations = payload.what_organizations
    what_supp_info = payload.what_supp_info
    lifestyle_changes = payload.lifestyle_changes
    vacation_care = payload.vacation_care
    death_plans = payload.death_plans
    looking_for_in_bird =  payload.looking_for_in_bird
    additional_comments =  payload.additional_comments

    # add all of these to a new row in the appropriate google sheet
    try:
        adoption_worksheet.append_row(
            [
                current_time,
                person_name,
                person_email,
                person_phone,
                person_address,
                person_city,
                person_state,
                person_zipcode,
                hear_about_us,
                num_household_people,
                primary_caregiver_age,
                ages_in_household,
                children_in_house,
                have_other_birds,
                previous_birds,
                other_bird_experience,
                avian_vet_info,
                residence_type,
                renter_verification,
                bird_hours_alone,
                smokers_in_house,
                other_pets_in_home,
                what_organizations,
                what_supp_info,
                lifestyle_changes,
                vacation_care,
                death_plans,
                looking_for_in_bird,
                additional_comments
            ]
        )

        # return response object saying data was written to google sheet
        response_object = {
            "message": "Adoption form written to Google Sheet successfully!"
        }

    # except and then return the error
    except Exception as e:
        response_object = {"message": f"Error: {e}"}

    return response_object
