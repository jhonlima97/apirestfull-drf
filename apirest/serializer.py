from rest_framework import serializers
from .models import *

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model= Developer
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields = '__all__'