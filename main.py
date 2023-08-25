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
CONTACT_SPREADSHEET_ID = os.getenv("CONTACT_SPREADSHEET_ID")

# Authenticate with Google
gc = gspread.service_account_from_dict(GOOGLE_CREDENTIAL_DICT)
sh = gc.open_by_key(CONTACT_SPREADSHEET_ID)


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
    name_index = sh.row_values(1).index("Name") + 1
    email_index = sh.row_values(1).index("Email") + 1

    # Append the name and email to the respective columns
    sh.update_cell(sh.row_count + 1, name_index, user_data.name)
    sh.update_cell(sh.row_count + 1, email_index, user_data.email)

    return {"message": "Name and email written successfully!"}
