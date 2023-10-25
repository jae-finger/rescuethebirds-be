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
    name_first: str


class AdoptionFormResponseSchema(BaseModel):
    message: str
