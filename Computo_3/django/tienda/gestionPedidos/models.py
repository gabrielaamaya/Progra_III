from django.db import models

# Create your models here.
class clientes(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    tlno = models.CharField(max_length=10, blank=True, null=True)


class articulos(models.Model):
    nombre=models.CharField(max_length=20)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()

class pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

class proveedores(models.Model):
    nombre=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)
    e_mail=models.EmailField(blank=True, null=True)
    tlno=models.CharField(max_length=10)    




