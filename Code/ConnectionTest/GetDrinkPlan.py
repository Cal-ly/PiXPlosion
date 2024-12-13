import requests

def fetch_data_from_api():
    # Replace with the API endpoint you want to call
    api_url = "https://api.chucknorris.io/jokes/random"  # Example: Joke API

    try:
        # Make the GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            print("Joke:", data.get("value", "No joke found."))
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Call the function
fetch_data_from_api()




