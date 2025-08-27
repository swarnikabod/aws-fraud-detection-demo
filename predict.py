import requests
import json

# Replace with your actual API Gateway Invoke URL
api_url = "https://wm3a4n9qzj.execute-api.ap-south-1.amazonaws.com/v1/predict"
# A sample transaction from your test data
transaction_data = "-0.338,1.062,-1.334,-0.258,1.428,0.738,0.593,0.208,0.024,-0.781,-0.603,-0.751,1.064,0.364,-0.474,0.228,0.743,0.292,-1.895,0.428,-0.471,0.468,0.734,-0.124,0.141,0.301,-0.512,-0.086,0.086"

# The payload our Lambda function expects
payload = {
    "data": transaction_data
}

# Corrected line
print(f"Sending request to: {api_url}")
print(f"Payload: {json.dumps(payload)}")

try:
    # Send the POST request
    response = requests.post(api_url, json=payload)
    response.raise_for_status()  # Raises an exception for bad status codes (4xx or 5xx)

    # Print the results
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response: {response.json()}")

except requests.exceptions.RequestException as e:
    print(f"\nAn error occurred: {e}") 