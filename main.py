from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

# Get environment variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

# Create a FastAPI instance
app = FastAPI()


@app.post("/submit")
def submit(data: dict):
    google_script_url = "https://script.google.com/macros/s/SCRIPT_ID/exec"
    headers = {"Authorization": f"Bearer {SECRET_KEY}"}
    response = requests.post(google_script_url, json=data, headers=headers)

    if response.ok:
        return response.json()
    else:
        return {"error": "An error occurred"}, 500
