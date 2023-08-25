from fastapi import FastAPI

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
google_credentials = os.getenv("GOOGLE_CREDENTIAL_DICT")

# Authenticate with Google
gc = gspread.service_account_from_dict(google_credentials)
client = gspread.authorize(google_credentials)

# Open the Google Sheet using its name or URL
sheet = client.open("SheetName").sheet1


# Data model for the request
class UserData(BaseModel):
    name: str
    email: str


@app.post("/write_user_data")
async def write_user_data(user_data: UserData):
    """
    Writes name and email to a Google Sheet
    - name: User's name 📝
    - email: User's email 📝
    """

    # Find the index of the "Name" and "Email" columns
    name_index = sheet.row_values(1).index("Name") + 1
    email_index = sheet.row_values(1).index("Email") + 1

    # Append the name and email to the respective columns
    sheet.update_cell(sheet.row_count + 1, name_index, user_data.name)
    sheet.update_cell(sheet.row_count + 1, email_index, user_data.email)

    return {"message": "Name and email written successfully!"}
