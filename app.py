from flask import Flask
import requests

app = Flask(__name__)

@app.route("/contacts", methods=["GET"])
def get_contacts():
    # Set the API endpoint and headers
    endpoint = "https://api.hubapi.com/contacts/v1/lists/all/contacts/all"
    headers = {"Authorization": "Bearer Your_Token"}

    # Make a GET request to the API
    response = requests.get(endpoint, headers=headers)

    # Parse the JSON data from the response
    data = response.json()

    return data

if __name__ == "__main__":
    app.run(debug=True)
