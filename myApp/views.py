from django.core.cache import cache
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myApp.serializers import VehicleSerializer, ModelsSerializer
from myApp.models import Vehicle, VehicleModel


@api_view(['GET','POST'])
def vehicles_view(request):
    if request.method == "GET":
        vehicle_objects = cache.get('vehicle_objects')
        if vehicle_objects is None:
            vehicle_objects = Vehicle.objects.all()
            cache.set('vehicle_objects', vehicle_objects, timeout=30)
        vehicles_ser = VehicleSerializer(vehicle_objects, many=True)
        return Response(vehicles_ser.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        ser = VehicleSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def vehicle_operations(request,pk):

    if request.method == "GET":
        vehicle = cache.get(pk)
        if vehicle is None:
            try:
                vehicle = Vehicle.objects.get(id=pk)
                cache.set(pk,vehicle, timeout=None)
            except:
                return Response({"Error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)

        ser = VehicleSerializer(vehicle)
        return Response(ser.data,status=status.HTTP_200_OK)

    elif request.method == "PUT":
        try:
            vehicle = Vehicle.objects.get(id=pk)
        except:
            return Response({"Error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)

        ser = VehicleSerializer(vehicle, data=request.data)
        if ser.is_valid():
            ser.save()
            cache.set(pk, vehicle, timeout=None)
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        try:
            vehicle = Vehicle.objects.get(id=pk)
            if vehicle.is_deleted == True:
                return Response({"Error": "Already Deleted!"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"Error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        vehicle.delete()
        cache.delete(pk)
        return Response({"Message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def vehicle_models_view(request):
    if request.method == "GET":
        vehicle_model_objects = cache.get('vehicle_model_objects')
        if vehicle_model_objects is None:
            vehicle_model_objects = VehicleModel.objects.all()
            cache.set('vehicle_model_objects',vehicle_model_objects, timeout=30)
        vehicles_ser = ModelsSerializer(vehicle_model_objects, many=True)
        return Response(vehicles_ser.data, status= status.HTTP_200_OK)
    elif request.method == "POST":
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


class ModelsViewSet(viewsets.ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = ModelsSerializer


@api_view(['GET'])
def vehicles_search(request):
    search_results = Vehicle.objects.filter(chasis_no=request.query_params['chasis_no'])
    if len(search_results) != 0:
        ser = VehicleSerializer(search_results, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        return Response({"Error":"Not Found!"},status=status.HTTP_404_NOT_FOUND )
