from django.urls import path
from .views import listaUsuarios, chat, crear_mensaje

urlpatterns = [
    path( '' , listaUsuarios, name='listaUsuario'),
    path('<int:receptor_id>/', chat, name='chat')
    path('crear_mensaje', crear_mensaje, name: crear_mensaje),


]