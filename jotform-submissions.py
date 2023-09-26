import requests

# the URL of our submissions
api_url = "https://form.jotform.com/232643820759058"

# our account's unique API key for Python scripting
api_key = "1c704b6eae7498cfe1c2c3644dda96f6"

# the information that we will automatically enter into the form
form_data = {
    "submission[1]":"Yes",
    "submission[2]":"55555",
    "submission[3]":"Checking Account",
    "submission[4]":"500",
    "submission[5]":"Transfer from a current account",
    "submission[6]":"Social Media",
    "submission[7]":"1111",
    "submission[8]":"Yes",
}

# define the headers with our API key
headers = {"APIKEY":api_key}

# make a POST request to submit the data
response = requests.post(api_url, data = form_data, headers = headers)

# if the operation succeeds, send a success message
if response.status_code == 200:
    print("Form submission successful!")
# if not, send a failure message
else:
    print("Failure. Status code:", response.status_code)