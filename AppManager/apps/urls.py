# myapp/urls.py

from django.urls import path
from .views import add_app, get_app, delete_app

urlpatterns = [
    path('add-app', add_app),
    path('get-app/<int:id>', get_app),
    path('delete-app/<int:id>', delete_app),
]
