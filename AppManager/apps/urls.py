from django.urls import path
from .views import add_app, get_app, delete_app

# Define URL patterns
urlpatterns = [
    path('add-app', add_app, name='add_app'),
    path('get-app/<int:id>', get_app, name='get_app'),
    path('delete-app/<int:id>', delete_app, name='delete_app'),
]