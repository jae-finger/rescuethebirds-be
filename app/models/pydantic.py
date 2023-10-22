from pydantic import BaseModel


class VolunteerFormPayloadSchema(BaseModel):
    name_first: str


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
