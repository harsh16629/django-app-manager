# AppManager API

## Overview

This is a Django-based RESTful API to manage app details.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd AppManager

2. **Create a Virtual Environment:**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt

4. **Run Migrations**:
    ```bash
    python manage.py migrate

5. **Run the Server**:
    ```bash
    python manage.py runserver

## API Endpoints

1. **POST /api/add-app**: Add new app details.
2. **GET /api/get-app/{id}**: Retrieve app details using the ID.
3. **DELETE /api/delete-app/{id}**: Delete an app by ID.
Please ensure your local server is running at http://127.0.0.1:8000.

## Dependencies
1. **Django**
2. **Django REST framework**
