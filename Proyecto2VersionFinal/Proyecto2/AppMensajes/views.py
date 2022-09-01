from django.shortcuts import render
from .models import Mensaje
from django.contrib.auth.models import User
from .forms import MensajeFormulario

def listaUsuarios(request):
    lista= User.objects.all()
    return render(request, "chats.html", {"lista":lista})

def chat(request,receptor_id):
    receptor= User.objects.get(id=receptor_id)
    mensajes= Mensaje.objects.filter(emisor=request.user, receptor=receptor).order_by('fecha')
    return render(request, "chat.html", {"receptor":receptor, "emisor": request.user, "mensajes":mensajes})



def crear_mensaje(request):
       if (request.method == 'POST'):
            form = MensajeFormulario(request.POST)
            if form.is_valid:   
                  info = form.cleaned_data
                  cuerpo=info['cuerpo']
                  mensaje = Mensaje(cuerpo=cuerpo)
                  mensaje.save()
                  return render(request, "AppMensajes/") 
        else:         
            form= MensajeFormulario() 
        return render(request, "AppMensajes/", {"form":form})