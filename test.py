import requests

# URL of the FastAPI endpoint
url = "https://rescuethebirds-jfcaxndkka-uc.a.run.app/write_user_data"

# Data to send in the request
payload = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response
print(response.json())
