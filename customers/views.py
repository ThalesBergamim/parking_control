from rest_framework import viewsets
from customers.models import Customer
from customers.serializers import CustomerSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser, DjangoModelPermissions]
