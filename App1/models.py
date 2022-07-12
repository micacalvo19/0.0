from django.db import models

# Create your models here.
class Formulario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_de_socio = models.IntegerField()
