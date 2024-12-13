from rest_framework import serializers
from .models import App

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'app_name', 'version', 'description']