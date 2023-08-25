import requests

# URL of the devcontainer or other server
url = ""

# Data to send in the request
payload = {"name": "Augie", "email": "john.doe@example.com"}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response
print(response.json())
