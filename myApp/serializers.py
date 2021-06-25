from rest_framework import serializers
from .models import *

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"
        read_only_fields = ("created_on","modified_on")


class ModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = "__all__"
