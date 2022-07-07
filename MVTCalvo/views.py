from django.shortcuts import render
from MVTCalvo.models import Familiar
from django.http import HttpResponse
import datetime
from django.template import Context, Template

def crearDocumento(diccionario):
    archivoTemplate=open('C:/Users/micae/OneDrive/Escritorio/MVTMicaela/MVTMicaela/plantillas/template.html')
    template=Template(archivoTemplate.read())
    archivoTemplate.close()

    contexto=Context(diccionario)
    return template.render(contexto)


# Create your views here.
def papa(self):

    papa=Familiar(nombre="Jaime", edad=53, nacimiento='1953-12-5')
    papa.save()
    diccionario = {'nombre': papa.nombre, 'edad': papa.edad, 'nacimiento': papa.nacimiento}
    documento = crearDocumento(diccionario)
    return HttpResponse(documento)

def mama(self):

    mama=Familiar(nombre="Julia", edad=43, nacimiento='1963-12-5')
    mama.save()
    diccionario = {'nombre':mama.nombre, 'edad':mama.edad, 'nacimiento':mama.nacimiento}
    documento = crearDocumento(diccionario)
    return HttpResponse(documento)
def hermana(self):

    hermana=Familiar(nombre="Luisa", edad=9, nacimiento='2013-12-5')
    hermana.save()
    diccionario = {'nombre':hermana.nombre, 'edad':hermana.edad, 'nacimiento':hermana.nacimiento}
    documento = crearDocumento(diccionario)
    return HttpResponse(documento)