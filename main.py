from fastapi import FastAPI
import gspread
from google.oauth2.service_account import Credentials
from pydantic import BaseModel

# Credentials from the Google Sheets API JSON file
creds = Credentials.from_service_account_file("credentials.json")
client = gspread.authorize(creds)

# Open the Google Sheet using its name or URL
sheet = client.open("SheetName").sheet1

app = FastAPI()

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

@app.get("/")
def read_root():
    return {"Hello": "Augie"}
