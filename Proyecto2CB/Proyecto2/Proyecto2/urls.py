"""Proyecto2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from App1.views import agregarAvatar, inicio
from App1.views import login_request
from App1.views import register
from App1.views import about
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('about/', about, name='about'),
    path ('logout/', LogoutView.as_view(template_name='App1/logout.html'), name='logout'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
    path('AppBlogs/', include('AppBlogs.urls')),
    path('AppMensajes/', include('AppMensajes.urls')),
    

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
