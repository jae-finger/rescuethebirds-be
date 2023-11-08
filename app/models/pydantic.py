from pydantic import BaseModel


class VolunteerFormPayloadSchema(BaseModel):
    person_name: str
    person_email: str
    person_phone: str
    person_address: str
    person_dob: str
    dl_number: str
    emergency_contact_name: str
    emergency_contact_phone: str
    interested_bird_care: bool
    interested_fundraising: bool
    interested_fostering: bool


class VolunteerFormResponseSchema(BaseModel):
    message: str


class BoardingFormPayloadSchema(BaseModel):
    name_first: str


class BoardingFormResponseSchema(BaseModel):
    message: str


class AdoptionFormPayloadSchema(BaseModel):
    person_name: str
    person_email: str
    person_phone: str
    person_address: str
    hear_about_us: str
    num_household_people: str
    primary_caregiver_age: str
    ages_in_household: str
    children_in_house: bool
    have_other_birds: str
    other_birds_species: str
    other_birds_checkup_date: str
    other_birds_diet: str
    previous_birds: str
    previous_birds_history: str
    other_bird_experience: str
    has_avian_vet: bool
    avian_vet_info: str
    residence_type: str
    renter_verification: bool
    bird_hours_alone: str
    smokers_in_house: bool
    smoker_explanation: str
    other_pets_in_home: bool
    other_pets_explanation: str
    what_organizations: str
    what_supp_info: str
    lifestyle_changes: str
    vacation_care: str
    death_plans: str


class AdoptionFormResponseSchema(BaseModel):
    message: str
