import requests
import json

# Step 1: Generate Bearer Token
API_KEY = 'N13012TMq2SyWs0Zh-czXIYgRhU-7rUz6ytfy6PEf7DP'
IAM_URL = 'https://iam.cloud.ibm.com/identity/token'

token_response = requests.post(
    IAM_URL,
    headers={'Content-Type': 'application/x-www-form-urlencoded'},
    data=f'grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={API_KEY}'
)

if token_response.status_code != 200:
    print("Error fetching Bearer Token:", token_response.json())
    exit()

# Extract Bearer token
bearer_token = token_response.json().get('access_token')

print(bearer_token)

# Step 2: Set API Endpoint and Headers
# URL = 'https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/ac92af0f-ace3-4c87-b0c5-0a508f102965/predictions?version=2021-05-01'

# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': f'Bearer {bearer_token}',
# }

# # Step 3: Input Payload
# payload = {
#     "input_data": [
#         {
#             "fields": ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"],  # Replace with actual field names
#             "values": [[90, 42, 43, 20.87974, 82.00274, 6.502985, 202.9355]]        # Replace with actual values
#         }
#     ]
# }

# # Step 4: Send POST Request
# response = requests.post(URL, headers=headers, json=payload)

# # Step 5: Output the Response
# if response.status_code == 200:
#     print("Prediction Response:", response.json())
# else:
#     print("Error in Prediction API Call:", response.json())

