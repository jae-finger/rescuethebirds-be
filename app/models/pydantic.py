from pydantic import BaseModel
from typing import List


class VolunteerFormPayloadSchema(BaseModel):
    person_name: str
    person_email: str
    person_phone: str
    person_address: str
    person_city: str
    person_state: str
    person_zipcode: str
    person_dob: str
    dl_number: str
    emergency_contact: str
    brief_synopsis_of_birds: str
    why_interested: str
    interested_bird_care: str
    interested_fundraising: str
    interested_fostering: str


class VolunteerFormResponseSchema(BaseModel):
    message: str


class BoardingFormPayloadSchema(BaseModel):
    person_name: str
    person_email: str
    person_phone: str
    person_address: str
    person_city: str
    person_state: str
    person_zipcode: str
    boarding_start_date: str
    boarding_end_date: str
    bird_list: List[str]  # fix to list of dictionaries


class BoardingFormResponseSchema(BaseModel):
    message: str


class AdoptionFormPayloadSchema(BaseModel):
    person_name: str
    person_dob: str
    person_email: str
    person_phone: str
    person_address: str
    person_city: str
    person_state: str
    person_zipcode: str
    hear_about_us: str
    num_household_people: str
    primary_caregiver_age: str
    ages_in_household: str
    children_in_house: str
    have_other_birds: str
    previous_birds: str
    other_bird_experience: str
    avian_vet_info: str
    residence_type: str
    renter_verification: str
    daily_routine: str
    weekend_routine: str
    bird_hours_alone: str
    smokers_in_house: str
    other_pets_in_home: str
    what_supp_info: str
    lifestyle_changes: str
    vacation_care: str
    death_plans: str
    looking_for_in_bird: str
    additional_comments: str


class AdoptionFormResponseSchema(BaseModel):
    message: str


class EmailRequest(BaseModel):
    to: str
    subject: str
    message_text: str