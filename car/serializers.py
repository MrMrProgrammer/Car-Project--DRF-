from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarSerializerDelete(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id']
