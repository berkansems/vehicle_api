from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myApp.serializers import VehicleSerializer, ModelsSerializer
from myApp.models import Vehicle, VehicleModel


@api_view(['GET'])
def vehicles(request):
    vehicles_object = Vehicle.objects.all()
    vehicles_ser = VehicleSerializer(vehicles_object, many=True)
    return Response(vehicles_ser.data, status= status.HTTP_200_OK)

@api_view(['POST'])
def vehicle_post(request):
    ser = VehicleSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def vehicle_operations(request,pk):
    try:
        vehicle = Vehicle.objects.get(id=pk)
    except:
        return Response({"Error":"Not Found!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        ser = VehicleSerializer(vehicle)
        return Response(ser.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        ser = VehicleSerializer(vehicle, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        vehicle.delete()
        return Response({"Message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)





@api_view(['GET'])
def vehicle_models(request):
    vehicles_object = VehicleModel.objects.all()
    vehicles_ser = ModelsSerializer(vehicles_object, many=True)
    return Response(vehicles_ser.data, status= status.HTTP_200_OK)

@api_view(['POST'])
def vehicle_model_post(request):
    ser = ModelsSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def vehicle_model_operations(request,pk):
    try:
        vehicle_model = VehicleModel.objects.get(id=pk)
    except:
        return Response({"Error":"Not Found!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        ser = ModelsSerializer(vehicle_model)
        return Response(ser.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        ser = ModelsSerializer(vehicle_model, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        vehicle_model.delete()
        return Response({"Message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
