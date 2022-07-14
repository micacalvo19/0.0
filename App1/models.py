from django.db import models

# Create your models here.
class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_de_socio = models.IntegerField()

class Personal(models.Model):
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)

class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad_de_personas = models.IntegerField()


