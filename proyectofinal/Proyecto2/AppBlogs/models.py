from django.db import models

# Create your models here.
class Receta(models.Model):

    titulo= models.CharField(max_length=20)
    cuerpo= models.CharField(max_length=10000)
 #   imagen= models.ImageField()
    fecha= models.DateField()

    def __str__(self):
       return self.titulo #, self.imagen

