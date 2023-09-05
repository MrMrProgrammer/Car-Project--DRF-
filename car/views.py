from django.shortcuts import render
from .models import Car
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import CarSerializer, CarSerializerDelete
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def show(request: Request):
    all_cars = Car.objects.all()
    car_serializer = CarSerializer(all_cars, many=True)
    return Response(car_serializer.data, status.HTTP_200_OK)


@api_view(['POST'])
def add(request: Request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        return Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update(request: Request):
    serializer = CarSerializer()


@api_view(['DELETE'])
def delete(request: Request):
    car_id = request.data.get('id', None)
    print(car_id)
    if car_id is not None:
        try:
            car = Car.objects.get(id=car_id)
            car.delete()
            return Response(None, status.HTTP_202_ACCEPTED)
        except Car.DoesNotExist:
            return Response({'detail': 'the car dose not exist'}, status.HTTP_404_NOT_FOUND)

    return Response({'detail': 'Entering the id field is mandatory'}, status.HTTP_400_BAD_REQUEST)
