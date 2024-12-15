# Django API for App Management

## Requirements

- Python 3.7 or higher
- Django
- QEMU 
- ADB (Android Debug Bridge) 
- An Android system image 
- A sample APK file 

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/harsh16629/django-backend-app.git
   ```

2. Navigate to the project directory:
   ```
   cd <project-directory>
   ```

3. Create a virtual environment and activate it:
   ```
   python3 -m venv env
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Configure the database in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

6. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

## Verify API Endpoints in Powershell

### Add App
- **Endpoint: POST**
```
   Invoke-WebRequest -Uri http://127.0.0.1:8000/add-app `
   -Method POST `
   -Headers @{"Content-Type"="application/json"} `
   -Body '{"app_name": "[your_app_name]", "version": "[your_app_version]", "description": "[your_app_description]"}'
```
### Get App
- **Endpoint: GET**
```
   curl -Method GET http://127.0.0.1:8000/get-app/[your_app_id]
```
### Delete App
- **Endpoint: DELETE**
```
   curl -Method DELETE http://127.0.0.1:8000/delete-app/[your_app_id]
```
## How to Install an App on the Virtual Android System

- Place the APK file you want to install in the same directory as the script.
- Update the `apk_path` variable in the script to the correct APK file name.
- The script will automatically install the app using ADB once the virtual system is launched.

## System Information Logged

The script retrieves and logs the following system details:

- **OS Version**: The Android operating system version running on the virtual device.
- **Device Model**: The model name of the virtual Android device.
- **Available Memory**: The amount of free memory available on the system.

### Log File

System information is saved in a file named `system_info.log` in the script's directory. Check this file for details about the virtual Android environment.

## Configuration for Android_Server_Connector.py

Update the `BASE_URL` variable in the script to match your backend server address. For example:
```python
BASE_URL = "http://127.0.0.1:8000"
```

---

## How to Run the Script

1. Clone the repository or download the script file.
2. Open a terminal and navigate to the script's directory.
3. Run the script:
   ```bash
   python Android_Server_Connector.py
   ```

---

## How to Use

### Sending Mock Device Data
The script simulates device data and sends it to the `/add-app` endpoint. Example payload:
```json
{
  "app_name": "TestApp",
  "version": "1.2",
  "description": "Device: Pixel 9 running Android 13.0"
}
```

### Retrieving App Details
The script fetches app details by ID from the `/get-app/{id}` endpoint. Replace `app_id` in the script's `retrieve_app_details` function to retrieve specific entries.

### Deleting App Entries
The script deletes an app by ID using the `/delete-app/{id}` endpoint. Replace `app_id` in the script's `delete_app` function to specify which app to delete.

---

## Logging

- All actions and responses are logged to `android_connector.log`.
- Logs include timestamps, severity levels (INFO, ERROR), and details of the requests and responses.
- Example log entry:
  ```
  2024-12-15 10:00:00 - INFO - Sending POST request to /add-app with payload: {"app_name": "MockApp", "version": "1.2", "description": "Device: Pixel 9 running Android 13.0"}
  2024-12-15 10:00:01 - INFO - Server response: {"id": 1, "status": "success"}
  ```

---
## Notes

- Ensure the Android system image (`android.img`) is present in the directory and is compatible with QEMU.
- Adjust the AVD name (`test_avd_1`) in the QEMU command if using a custom AVD.
- Modify the memory allocation or other QEMU settings as needed for performance.
- Ensure the backend server is running before executing the script.
- Confirm that the backend API endpoints match those defined in the script.
