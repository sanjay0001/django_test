import requests

api_url = "http://127.0.0.1:8000/show"

# try:
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         data = response.json()
#         print("API Response:")
#         print(data)
#     else:
#         print(f"Request failed with status code {response.status_code}")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")


payload = {
    "name": "TV",
    "price": "55000",
    "description": "55 inch TV"
}
api_url = "http://127.0.0.1:8000/add"
try:
    # Send a POST request to the API with the data
    response = requests.post(api_url, data=payload)

    # Check if the request was successful (status code 200)
    print(response)
    if response.status_code == 200:
        # Parse the JSON response (if applicable)
        data = response.json()
        print("API Response:")
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
