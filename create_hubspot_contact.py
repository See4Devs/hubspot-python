import requests

# Set the API endpoint
url = "https://api.hubapi.com/crm/v3/objects/contacts"

# Set the request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer Your_Token"
}

# Set the contact information
contact = {
    "properties": {
        "email": "example@python.com",
        "firstname": "Tutorial",
        "lastname": "Test1"
    }
}

# Send the request
response = requests.post(url, json=contact, headers=headers)

if response.status_code == 201:
    print("Contact Created Successfully")
else:
    print("Failed To Create Contact")