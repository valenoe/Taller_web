"""
URL configuration for fichas_m project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from fichas.views import *



urlpatterns  = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('usuario/', usuarios, name='usuario'),
    path('crear_usuario/', crearUsuario, name='crear_usuario'), 
    path('modificar_usuario/<str:pk>', modificarUsuario, name='modificar_usuario'),
    path('eliminar_usuario/<str:pk>', eliminarUsuario, name='eliminar_usuario'), 
    path('accounts/', include("django.contrib.auth.urls")),
 
]