
from django.urls import path
from AppBlogs.views import leer_recetas
from AppBlogs.views import editar_receta
from AppBlogs.views import borrar_receta
from AppBlogs.views import crear_receta
from re import template



urlpatterns = [
    path('leerrecetas/', leer_recetas, name='leer_recetas' ),
    path('editarreceta/<titulo_receta>', editar_receta, name='editar_receta'),
    path('crearreceta/', crear_receta, name='crear_receta'),
    path('borrarreceta/', borrar_receta, name='borrar_receta'),
    ] 
