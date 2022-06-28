from django.db import models

# Create your models here.

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    nombre = models.CharField(max_length=50, verbose_name='Nombre de producto')
    marca = models.CharField(max_length=50, verbose_name='Marca de producto')
    fechaFabricacion = models.DateField()
    imagen = models.ImageField(upload_to="Productos", null=True)
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=9, verbose_name='Rut de cliente')
    nombre = models.CharField(max_length=25, verbose_name='Nombre de cliente')
    apellido = models.CharField(max_length=25, verbose_name='Apellido de cliente')
    email = models.CharField(max_length=50, verbose_name='Email de cliente')
    direccion = models.CharField(max_length=25, verbose_name='Direccion de cliente', null=True)
    telefono = models.IntegerField( verbose_name='Telefono de cliente', null=True)

    def __str__(self):
        return self.nombre
