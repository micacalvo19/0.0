from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Context, Template
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from App1.forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Avatar
from .forms import AvatarForm

def inicio(request):
    return render (request, "App1/inicio.html")

def login_request(request):
        if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                usu = form.cleaned_data.get('username')
                contra = form.cleaned_data.get('password')
                usuario = authenticate(username=usu, password=contra)
                if usuario is not None:
                    login(request, usuario)
                    return render(request, "App1/inicio.html", {"form":form, "mensaje": f"Bienvenido {usuario}"})
                else:
                    return render(request, "App1/login.html", {"form":form, "mensaje": "Datos incorrectos"})
            else:
                return render(request, "App1/login.html", {"form":form, "mensaje": "Formulario erroneo"})
        else:
            form = AuthenticationForm()
            return render(request, "App1/login.html", {'form':form})

def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request, "App1/inicio.html", {'form':form, "mensaje":"Usuario creado"})
    else:
            form = UserRegisterForm()
    return render(request, 'App1/register.html', {"form":form})

def recetas(request):
    return render (request, "App1/recetas.html")

def agregarAvatar(request):
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid:
            avatarViejo=Avatar.objects.get(user=request.user)
            if avatarViejo.imagen:
                avatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'App1/inicio.html')
    else:
        formulario=AvatarForm()
    return render(request, 'App1/agregaAvatar.html', {'formulario':formulario, 'usuario':request.user})

def about(request):
    return render (request, "App1/about.html")
