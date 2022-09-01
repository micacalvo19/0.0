from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    emisor= models.ForeignKey(User, on_delete=models.CASCADE, related_name="emisor")
    receptor= models.ForeignKey(User, on_delete=models.CASCADE)
    fecha= models.DateTimeField()
    cuerpo= models.TextField()
   
    def __str__(self):
        return f'{self.cuerpo}  {self.fecha} '

