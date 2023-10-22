import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL_PREFIX = os.getenv("ALLOWED_ORIGIN")

# URL of the devcontainer or other server
url = f"{BASE_URL_PREFIX}/forms/volunteer"

# Data to send in the request
payload = {"current_time": "2023-01-01 12:00:00", "name_first": "Jon"}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response
print(response.json())
