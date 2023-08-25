from pydantic import BaseModel


class VolunteerFormPayloadSchema(BaseModel):
    name_first: str
    name_middle: str
    name_last: str
    email: str
    primary_phone: str
    street_address: str
    city: str
    state_province_region: str
    postal_zip_code: str
    country: str
    emergency_contact: str
    date_of_birth: str
    drivers_license: str
    days_hours_preferred: str
    special_skills: str
    languages: str
    other_experiences_skills: str
    bird_care_interest: str
    reference_1: str
    reference_2: str
    reference_3: str


class VolunteerFormResponseSchema(BaseModel):
    message: str
