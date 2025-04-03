from django.contrib import admin
from vehicles.models import Vehicle, VehicleType


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'created_at']


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['plate', 'brand', 'model', 'color', 'owner', 'vehicle_type']
    search_fields = ['plate', 'brand', 'model', 'color']
    list_filter = ['vehicle_type']