from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Customer(models.Model):
    user = models.OneToOneField(
        'User',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='customers',
        verbose_name='Usúario',
    )
    name = models.CharField(max_length=100, verbose_name='Nome')
    phone = models.CharField(
        max_length=15, 
        verbose_name='Telefone',
        blank=True,
        null=True,
        validators=[RegexValidator(
            regex=r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}',
            message='Número de telefone inválido. Utilize o formato (XX) XXXX-XXXX',
        )],
        help_text='Utilize o formato (XX) XXXX-XXXX'
    )
    cpf = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name='CPF',
        # validators=[RegexValidator(
        #     regex=r'/^\d{3}\.\d{3}\.\d{3}\-\d{2}$/',
        #     message='CPF Inválido. Digite somente números.',
        # )],
        # help_text='Digite somente números.',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name
