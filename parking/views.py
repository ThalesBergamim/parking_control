from rest_framework import viewsets
from parking.models import ParkingRecord, ParkingSpot
from parking.serializers import ParkingSpotSerializer, ParkingRecordSerializer
from rest_framework.permissions import DjangoModelPermissions
from core.permissions import IsOwnerOfVehicleOrRecord
from parking.filters import ParkingRecordFilterClass, ParkingSpotFilterClass


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    filterset_class = ParkingSpotFilterClass
    permission_classes = [DjangoModelPermissions]

class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    filterset_class = ParkingRecordFilterClass
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def query_set(self):
        user = self.request.user
        if user.is_staff:
            return ParkingRecord.objects.all()
        return ParkingRecord.objects.filter(vehicle__owner__user=user)
