# Django API for App Management

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
