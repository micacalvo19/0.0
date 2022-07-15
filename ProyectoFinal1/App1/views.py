from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Context, Template
from App1.models import Socio
from App1.models import Personal
from App1.models import Actividad
from App1.forms import SocioForm
from App1.forms import PersonalForm
from App1.forms import ActividadForm

# Create your views here.

def inicio(request):
    return render (request, "inicio.html")

def formularioSocio(request):
    if(request.method=="POST"):
        form= SocioForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            numero_de_socio= info["numero_de_socio"]
            formularioSocio= Socio(nombre=nombre, apellido=apellido, numero_de_socio=numero_de_socio)
            formularioSocio.save()
            return render (request, "inicio.html")
    else:
        form= SocioForm()
    return render(request, "formularioSocio.html", {"form":form})

def busquedaSocio(request):
    return render(request, 'busquedaSocio.html')

def buscar(request):
    if request.GET['numero_de_socio']:
        numero_de_socio= request.GET["numero_de_socio"]
        socios= Socio.objects.filter(numero_de_socio=numero_de_socio)
        return render(request, "resultadosBusqueda.html", {"socios": socios})
    else:
        return render(request, "busquedaSocio.html", {"error": "No se ingreso numero de socio"})

def formularioPersonal(request):
    if(request.method=="POST"):
        form= PersonalForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            cargo= info["cargo"]
            formularioPersonal= Personal(nombre=nombre, cargo=cargo)
            formularioPersonal.save()
            return render (request, "inicio.html")
    else:
        form= PersonalForm()
    return render(request, "formularioPersonal.html", {"form":form})

def formularioActividad(request):
    if(request.method=="POST"):
        form= ActividadForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            cantidad_de_personas= info["cantidad_de_personas"]
            formularioActividad= Actividad(nombre=nombre, cantidad_de_personas=cantidad_de_personas)
            formularioActividad.save()
            return render (request, "inicio.html")
    else:
        form= ActividadForm()
    return render(request, "formularioActividad.html", {"form":form})