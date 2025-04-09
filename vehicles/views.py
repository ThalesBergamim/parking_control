from rest_framework import viewsets
from vehicles.models import Vehicle, VehicleType
from vehicles.serializers import VehicleSerializer, VehicleTypeSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from core.permissions import IsOwnerOfVehicleOrRecord
from vehicles.filters import VehicleFilterClass, VehicleTypeFilterClass


class VehicleViewSet(viewsets.ModelViewSet):
    query_set = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filterset_class = VehicleFilterClass
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    filterset_class = VehicleTypeFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]
