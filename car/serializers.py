from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'year', 'price']


class CarSerializerDelete(serializers.ModelSerializer):
    class Meta:
        model = Car
        # fields = ['id', 'brand']
        fields = '__all__'
