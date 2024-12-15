import requests, json
import logging

# Backend API endpoints 
BASE_URL = "http://127.0.0.1:8000"  
ADD_APP_ENDPOINT = "http://127.0.0.1:8000/add-app/add-app"
GET_APP_ENDPOINT = "http://127.0.0.1:8000/get-app/get-app/"
DELETE_APP_ENDPOINT = "http://127.0.0.1:8000/delete-appL/delete-app/"

# Mock data to send to the server
def get_device_info():
    #Retrieving mock device information.
    return {
        "device_id": "emulator-5554",
        "os_version": "13.0",
        "model": "Pixel 9",
        "available_memory": "8 GB"
    }

def send_device_info_to_server():
    #Send mock data to the backend server.
    mock_data = get_device_info()

    # Example payload for /add-app endpoint
    payload = {
        "app_name": "TestApp",
        "version": "1.2",
        "description": f"Device: {mock_data['model']} running Android {mock_data['os_version']}"
    }

    try:
        # Sending POST request to /add-app
        response = requests.post(ADD_APP_ENDPOINT, json=payload)
        response.raise_for_status()  # Raise an error for HTTP status codes 
        print("Server response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {e}")

def retrieve_app_details(app_id):
    #Retrieve app details by ID from the backend server.
    try:
        response = requests.get(f"{GET_APP_ENDPOINT}{app_id}")
        response.raise_for_status()
        print("Retrieved app details:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving app details: {e}")

def delete_app(app_id):
    #Delete app by ID from the backend server.
    try:
        response = requests.delete(f"{DELETE_APP_ENDPOINT}{app_id}")
        response.raise_for_status()
        print("Deleted app successfully. Response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error deleting app: {e}")

def main():
    logging.info("Script started.")
    logging.info("Sending mock device data to server...")
    send_device_info_to_server()

    logging.info("Retrieving app details with ID 1...")
    retrieve_app_details(app_id=1)

    logging.info("Deleting app with ID 1...")
    delete_app(app_id=1)
    logging.info("Script finished.")

if __name__ == "__main__":
    main()
