import requests

API_KEY = "cpd-apikey-IBMid-694000GICM-2024-09-10T06:16:20Z"
IAM_URL = "https://iam.cloud.ibm.com/identity/IAM"

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = f'grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={API_KEY}'

response = requests.post(IAM_URL, headers=headers, data=data)
token = response.json().get('access_token')
print("Bearer Token:", token)
