# Django API for App Management

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd <project-directory>
   ```

3. Create a virtual environment and activate it:
   ```
   python3 -m venv env
   source env/bin/activate
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

## API Endpoints

### Add App
- **Endpoint:** POST /add-app
- **Request Body:**
  ```json
  {
      "app_name": "App Name",
      "version": "1.0",
      "description": "App description."
  }
  ```
- **Response:**
  ```json
  {
      "message": "App added successfully",
      "id": 1
  }
  ```

### Get App
- **Endpoint:** GET /get-app/{id}
- **Response:**
  ```json
  {
      "id": 1,
      "app_name": "App Name",
      "version": "1.0",
      "description": "App description."
  }
  ```

### Delete App
- **Endpoint:** DELETE /delete-app/{id}
- **Response:**
  ```json
  {
      "message": "App deleted successfully"
  }
  ```