import requests

# Set the API endpoint and headers
endpoint = "https://api.hubapi.com/contacts/v1/lists/all/contacts/all"
headers = {"Authorization": "Bearer Your_Token"}

# Make a GET request to the API
response = requests.get(endpoint, headers=headers)

# Parse the JSON data from the response
data = response.json()

# Loop through the contacts and print their information
for contact in data["contacts"]:
    print(contact)
