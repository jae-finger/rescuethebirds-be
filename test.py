import requests

# URL of the devcontainer or other server
url = "http://0.0.0.0:8000/write_user_data"

# Data to send in the request
payload = {"name": "Augie", "email": "john.doe@example.com"}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response
print(response.json())
