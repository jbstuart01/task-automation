import requests
import os

# Your Jotform API key and form ID
api_key = '1c704b6eae7498cfe1c2c3644dda96f6'
form_id = '232643820759058'

# Jotform API endpoint for form submissions
api_url = f'https://api.jotform.com/form/{form_id}/submissions'

# Directory to save downloaded PDF files
download_dir = '\\fs11\EmpProfiles$\jbstuart\Documents\AutomationTesting1'

# Create the download directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

# Define headers with the API key
headers = {
    'APIKEY': api_key
}

# Send a GET request to retrieve form submissions
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    print("response.status_code == 200")
    submissions = response.json()['content']

    for submission in submissions:
        # Check if the submission has a PDF file attached
        if 'pdf' in submission:
            print("pdf is in submission")
            pdf_url = submission['pdf']

            # Extract the filename from the URL
            pdf_filename = os.path.join(download_dir, os.path.basename(pdf_url))

            # Download the PDF file
            pdf_response = requests.get(pdf_url)
            if pdf_response.status_code == 200:
                with open(pdf_filename, 'wb') as pdf_file:
                    pdf_file.write(pdf_response.content)
                print(f'Downloaded: {pdf_filename}')
            else:
                print(f'Failed to download PDF for submission: {submission["id"]}')
else:
    print(f'Failed to retrieve form submissions. Status code: {response.status_code}')
