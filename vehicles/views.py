from rest_framework import viewsets
from vehicles.models import Vehicle, VehicleType
from vehicles.serializers import VehicleSerializer, VehicleTypeSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from core.permissions import IsOwnerOfVehicleOrRecord


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(ownder__user=user)

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]
