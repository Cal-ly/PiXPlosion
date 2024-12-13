import requests
import socket
import time
import json
from FindLocalip import get_local_ip


url = 'https://promillepartnerbackend.azurewebsites.net/api/PromillePartnerPi/register'
headers = {
    'X-Api-Key': 'bob-api-key',
    'X-Pi-Ip': get_local_ip(),
    'Content-Type': 'application/json'  # This is the key part
}
data = { 
    "identifier":"bob",
}

# Send the correct JSON data with the Content-Type header
response = requests.post(url, headers=headers, json=data)
print(response.status_code)  # Print the status code
print(response.text)  # Print the response body

    
