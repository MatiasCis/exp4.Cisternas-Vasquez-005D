from rest_framework import serializers
from MascotasCore.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields=['rut','nombre','apellido','email','direccion','telefono']