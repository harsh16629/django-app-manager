from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import AppDetails

# Add a view for adding app details
@csrf_exempt
def add_app(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            app_details = AppDetails.objects.create(
                app_name=data['app_name'],
                version=data['version'],
                description=data['description']
            )
            return JsonResponse({"message": "App added successfully", "id": app_details.id})
        except KeyError:
            return JsonResponse({"error": "Invalid data format"}, status=400)
    return JsonResponse({"error": "Invalid HTTP method"}, status=405)

# Add a view for retrieving app details by ID
def get_app(request, id):
    if request.method == 'GET':
        app_details = get_object_or_404(AppDetails, id=id)
        return JsonResponse({
            "id": app_details.id,
            "app_name": app_details.app_name,
            "version": app_details.version,
            "description": app_details.description
        })
    return JsonResponse({"error": "Invalid HTTP method"}, status=405)

# Add a view for deleting app details by ID
@csrf_exempt
def delete_app(request, id):
    if request.method == 'DELETE':
        app_details = get_object_or_404(AppDetails, id=id)
        app_details.delete()
        return JsonResponse({"message": "App deleted successfully"})
    return JsonResponse({"error": "Invalid HTTP method"}, status=405)
