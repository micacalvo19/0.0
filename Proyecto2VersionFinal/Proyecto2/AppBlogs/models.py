from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Receta(models.Model):

    titulo= models.CharField(max_length=20)
    cuerpo= RichTextField(blank=True, null=True)    
  # cuerpo= models.CharField(max_length=10000)
    imagen= models.ImageField(null=True,blank=True, upload_to='images/')
    fecha= models.DateField()

    def __str__(self):
       return self.titulo #, self.imagen

