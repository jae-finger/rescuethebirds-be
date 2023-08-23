from fastapi import FastAPI
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

import os

# from dotenv import load_dotenv

# # Get environment variables
# load_dotenv()
# SPREADSHEET_ID = os.getenv("TEST_SPREADSHEET_ID")

# Initialize the FastAPI app
app = FastAPI()


# @app.post("/submit")
# def submit(name: str, email: str):
#     # Load the credentials from the `token.json` file created during the Sheets API setup
#     creds = Credentials.from_authorized_user_file(
#         "token.json", ["https://www.googleapis.com/auth/spreadsheets"]
#     )

#     # Connect to the Sheets API
#     service = build("sheets", "v4", credentials=creds)
#     sheet = service.spreadsheets()

#     # Data to append
#     values = [[name, email]]
#     body = {"values": values}

#     # Append the data to the sheet
#     result = (
#         sheet.values()
#         .append(
#             spreadsheetId=SPREADSHEET_ID,
#             range="Sheet1!A1:B1",
#             valueInputOption="RAW",
#             body=body,
#         )
#         .execute()
#     )

#     return {"message": "Data added to the sheet"}


@app.get("/")
def read_root():
    return {"Hello": "Augie"}
