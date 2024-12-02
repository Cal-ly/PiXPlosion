import requests

BASE_URL = "http://backend-url/api" # Replace with the actual backend URL

def fetch_drinking_plan(desired_bac, time_period):
    endpoint = f"{BASE_URL}/drinkingplan" # Replace with the actual endpoint, e.g. vores endpoint /drinkingplan
    data = {
        "desiredBAC": desired_bac,
        "timePeriod": time_period
    }
    response = requests.post(endpoint, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch drinking plan:", response.status_code)
        return None
