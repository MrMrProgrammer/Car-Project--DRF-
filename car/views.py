from django.shortcuts import render
from rest_framework.views import APIView

from .models import Car
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import CarSerializer, CarSerializerUpdate, CarSerializerDelete
from rest_framework import status
from rest_framework.decorators import api_view

from drf_spectacular.utils import extend_schema, OpenApiParameter


# =====================================================================================================================

@extend_schema(
    responses={201: CarSerializer},
    description='You can see the list of all cars in this section.',
)
@api_view(['GET'])
def show(request: Request):
    all_cars = Car.objects.all()
    car_serializer = CarSerializer(all_cars, many=True)
    return Response(car_serializer.data, status.HTTP_200_OK)


# =====================================================================================================================

@extend_schema(
    request=CarSerializer,
    responses={201: CarSerializer},
    description='You can add a new car by entering the specified fields.',
)
@api_view(['POST'])
def add(request: Request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        return Response(None, status.HTTP_400_BAD_REQUEST)


# =====================================================================================================================

@extend_schema(
    request=CarSerializerUpdate,
    responses={201: CarSerializerUpdate},
    description='You can update the previous information by entering the id and new specifications of the car you want.'
)
@api_view(['PUT'])
def update(request: Request):
    try:
        car_id = request.data.get('id')
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        return Response('This car does not exist !', status.HTTP_404_NOT_FOUND)

    serializer = CarSerializer(car, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    return Response('400 - BAD REQUEST', status.HTTP_400_BAD_REQUEST)


# =====================================================================================================================

@extend_schema(
    request=CarSerializer,
    responses={201: CarSerializer},
    description='You can delete the desired machine by entering the ID.',
)
@api_view(['DELETE'])
def delete(request: Request):
    car_id = request.data.get('id', None)
    print(car_id)
    if car_id is not None:
        try:
            car = Car.objects.get(id=car_id)
            car.delete()
            return Response('The desired car was removed', status.HTTP_202_ACCEPTED)
        except Car.DoesNotExist:
            return Response({'detail': 'the car dose not exist'}, status.HTTP_404_NOT_FOUND)

    return Response({'detail': 'Entering the id field is mandatory'}, status.HTTP_400_BAD_REQUEST)

# =====================================================================================================================
