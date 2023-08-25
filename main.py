from fastapi import FastAPI
import ast
import gspread
from pydantic import BaseModel
import os

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


# Home route for testing purposes
@app.get("/")
def read_root():
    return {"Hello": "Augie"}


# Load google sheet based information
# get env variable called 'GOOGLE_CREDENTIAL_DICT'
GOOGLE_CREDENTIAL_DICT = ast.literal_eval(os.getenv("GOOGLE_CREDENTIAL_DICT"))
GOOGLE_SPREADSHEET_ID = os.getenv("GOOGLE_SPREADSHEET_ID")

# Authenticate with Google
gc = gspread.service_account_from_dict(GOOGLE_CREDENTIAL_DICT)
sh = gc.open_by_key(GOOGLE_SPREADSHEET_ID)
volunteer_worksheet = sh.sheet1


class VolunteerForm(BaseModel):
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


@app.post("/submit_volunteer_form")
async def submit_volunteer_form(volunteer_form: VolunteerForm):
    # extract data from volunteer_form
    name_first = volunteer_form.name_first
    name_middle = volunteer_form.name_middle
    name_last = volunteer_form.name_last
    email = volunteer_form.email
    primary_phone = volunteer_form.primary_phone
    street_address = volunteer_form.street_address
    city = volunteer_form.city
    state_province_region = volunteer_form.state_province_region
    postal_zip_code = volunteer_form.postal_zip_code
    country = volunteer_form.country

    # add all of these to a new row in volunteer_worksheet
    volunteer_worksheet.append_row(
        [
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
        ]
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
