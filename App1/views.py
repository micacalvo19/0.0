from django.shortcuts import render
from App1.models import Formulario
from django.http import HttpResponse
import datetime
from django.template import Context, Template
from App1.forms import FormularioForm

# Create your views here.

def inicio(request):
    return render (request, "inicio.html")

def formulario(request):
    if(request.method=="POST"):
        form= FormularioForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            numero_de_socio= info["numero_de_socio"]
            formulario= Formulario(nombre=nombre, apellido=apellido, numero_de_socio=numero_de_socio)
            formulario.save()
            return render (request, "inicio.html")
    else:
        form= FormularioForm()
    return render(request, "formulario.html", {"form":form})

def busqueda_socio(request):
    return render(request, 'busqueda_socio.html')

def buscar(request):
    if request.GET['numero_de_socio']:
        numero_de_socio= request.GET["numero_de_socio"]
        socios= Formulario.objects.filter(numero_de_socio=numero_de_socio)
        return render(request, "resultados_busqueda.html", {"socios": socios})
    else:
        return render(request, "busqueda_socio.html", {"error": "No se ingreso numero de socio"})