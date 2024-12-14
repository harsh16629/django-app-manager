# myapp/views.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import App

# POST /add-app
@csrf_exempt
def add_app(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        app = App.objects.create(
            app_name=data.get('app_name'),
            version=data.get('version'),
            description=data.get('description')
        )
        return JsonResponse({"message": "App added successfully", "app_id": app.id}, status=201)

# GET /get-app/{id}
def get_app(request, id):
    app = get_object_or_404(App, id=id)
    return JsonResponse({
        "app_name": app.app_name,
        "version": app.version,
        "description": app.description
    })

# DELETE /delete-app/{id}
@csrf_exempt
def delete_app(request, id):
    if request.method == "DELETE":
        app = get_object_or_404(App, id=id)
        app.delete()
        return JsonResponse({"message": "App successfully deleted"}, status=204)

def list_apps(request):
    if request.method == "GET":
        apps = App.objects.all().values('id', 'app_name', 'version', 'description')
        return JsonResponse(list(apps), safe=False)