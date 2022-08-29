from django.shortcuts import render
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppBlogs.models import Receta
from AppBlogs.forms import RecetaFormulario
from django.template import Context, Template

def crear_receta(request):

      if (request.method == 'POST'):
            form = RecetaFormulario(request.POST) #aquí mellega toda la información del html
            print(form)
            if form.is_valid:   #Si pasó la validación de Django
                  info = form.cleaned_data
                  print(info)
                  titulo=info['titulo'] 
                  cuerpo=info['cuerpo']
                  imagen=info['imagen'] 
                  fecha=info['fecha']
                  receta = Receta(titulo=titulo, cuerpo=cuerpo, fecha=fecha, imagen=imagen)
                  receta.save()
                  return render(request, "App1/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            form= RecetaFormulario() #Formulario vacio para construir el html

      return render(request, "AppBar/crearreceta.html", {"form":form})

def leer_recetas(request):
    recetas= Receta.objects.all()
    return render(request, "AppBar/leerrecetas.html", {"recetas":recetas})

def editar_receta(request, titulo_receta):
    receta= Receta.objects.get(titulo= titulo_receta)
    if request.method=="POST":
        form= RecetaFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            titulo=info['titulo']
            cuerpo=info['cuerpo']
            imagen=info['imagen']
            fecha=info['fecha']
            receta.save()
            return render (request, "App1/inicio.html")
    else:
        form= RecetaFormulario(initial={'titulo':receta.titulo, 'cuerpo':receta.cuerpo, 'fecha':receta.fecha})
                                     #   'imagen':receta.imagen,
                                        
    return render (request, "AppBar/editarreceta.html", {'form':form})

def borrar_receta(request, titulo_receta):
    receta=Receta.objects.get(titulo=titulo_receta)
    receta.delete()
    recetas=Receta.objects.all()
    return render(request, "App1/inicio.html", {"reccetas":recetas})



    