import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL_PREFIX = os.getenv("ALLOWED_ORIGIN")

# URL of the devcontainer or other server
url = f"{BASE_URL_PREFIX}/forms/volunteer"

# Data to send in the request
payload = {
    "name_first": "Jon",
    "name_middle": "A",
    "name_last": "Finger",
    "email": "j@f.com",
    "primary_phone": "123456789",
    "street_address": "123 Main St.",
    "city": "Anytown",
    "state_province_region": "AnyState",
    "postal_zip_code": "12345",
    "country": "USA",
    "emergency_contact": "Jane Doe",
    "date_of_birth": "01/01/2000",
    "drivers_license": "123456789",
    "days_hours_preferred": "Anytime",
    "special_skills": "None",
    "languages": "English",
    "other_experiences_skills": "None",
    "bird_care_interest": "True",
    "reference_1": "Frodo Baggins",
    "reference_2": "Elton John",
    "reference_3": "Joe Biden",
}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response
print(response.json())
