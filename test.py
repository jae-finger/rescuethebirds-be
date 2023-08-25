import requests

# URL of the devcontainer or other server
url = "http://0.0.0.0:8000/submit_volunteer_form"

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
    "country": "USA"
    }

# Send the POST request
response = requests.post(url, json=payload)

# Print the response
print(response.json())
