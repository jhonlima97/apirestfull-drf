from rest_framework import serializers
from .models import *

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model= Developer
        fields = '__all__'
    def validate_fullname(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('The fullname can only contain letters.')
        return value

    def validate(self, data):
        if not data.get('fullname') or not data.get('nickname') or not data.get('age'):
            raise serializers.ValidationError('All fields are required.')
        return data

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields = '__all__'
    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('The name can only contain letters.')
        return value
    def validate(self, data):
        if not data.get('name') or not data.get('description') or not data.get('start_date') or not data.get('developer'):
            raise serializers.ValidationError('All fields are required.')
        return data