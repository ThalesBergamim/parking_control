from rest_framework import serializers
from vehicles.models import VehicleType, Vehicle


class VehicleSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Vehicle
        fields = '__all__'

class VehicleTypeSerializer(serializers.ModelSerializer):

    class Meta: 
        model = VehicleType
        fields = '__all__'
