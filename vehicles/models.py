from django.db import models
from customers.models import Customer

class VehicleType(models.Model):
    name = models.CharField(
        max_length=50, 
        verbose_name='Nome', 
        unique=True,
    )
    description = models.TextField(
        verbose_name='Descrição',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Tipo de Veículo'
        verbose_name_plural = 'Tipos de Veículo'

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Tipo de Veículo',
    )
    plate = models.CharField(
        max_length=8,
        unique=True,
        verbose_name='Placa',
    )
    brand = models.CharField(
        max_length=50,
        verbose_name='Marca',
        blank=True, 
        null=True,
    )
    model = models.CharField(
        max_length=50,
        verbose_name='Modelo',
        blank=True, 
        null=True,
    )
    color = models.CharField(
        max_length=50,
        verbose_name='Cor',
        blank=True, 
        null=True,
    )
    owner = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Proprietário',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.plate
