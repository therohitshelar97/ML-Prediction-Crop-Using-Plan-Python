import requests

# Replace with your actual API key
API_KEY = "N13012TMq2SyWs0Zh-czXIYgRhU-7rUz6ytfy6PEf7DP"

# Step 1: Get the Bearer Token
token_response = requests.post(
    'https://iam.cloud.ibm.com/identity/token',
    data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
)

if token_response.status_code != 200:
    print("Error fetching token:", token_response.json())
    exit()

mltoken = token_response.json().get("access_token")
# print("Bearer Token:", mltoken)  # You can print the token to check

# Step 2: Set Headers
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# Step 3: Define Input Data (replace with your actual fields and values)
payload_scoring = {
    "input_data": [
        {
            "fields": ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"],
            "values": [[87, 54, 20, 25.61707, 63.47118, 6.576418, 108.8304]]
        }
    ]
}

# Step 4: Make the Prediction Request
response_scoring = requests.post(
    'https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/a69a10e1-fdc2-4449-86ae-7eba4fa86dd8/predictions?version=2021-05-01',
    json=payload_scoring,
    headers=header,
    
)

print(response_scoring)
# Step 5: Output the Response
if response_scoring.status_code != 200:
    print("Error in prediction:", response_scoring.json())
else:
    # print("Scoring response:", response_scoring.json())
    print(response_scoring.json()['predictions'][0]['values'][0][0])


