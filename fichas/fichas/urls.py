"""
URL configuration for fichas project.

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
from django.urls import include, path
from fichasapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fichasapp.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('usuario/', views.usuarios, name='usuario'),
    path('crear_usuario', views.crearUsuario, name='crear_usuario'),
    path('modificar_usuario/<str:pk>/', views.modificarUsuario, name='modificar_usuario'),
    path('eliminar_usuario/<str:pk>/', views.eliminarUsuario, name='eliminar_usuario'),
    path('mostrar_usuario/<str:pk>/', views.mostrar_usuario, name='mostrar_usuario'),
    
    path('personalsalud/', views.personalSalud, name='personalsalud'),
    path('crear_personal/', views.crearPersonal, name='crear_personal'),
    path('eliminar_personal/<str:pk>/', views.eliminarPersonal, name='eliminar_personal'),

    path('menu/', views.home, name='menu'),
    path('especialidad/', views.especialidad, name='especialidad'),
    path('crear_especialidad/', views.crear_especialidad, name='crear_especialidad'),
    path('modificar_especialidad/<str:pk>/', views.modificarEspecialidad, name='modificar_especialidad'),
    path('eliminar_especialidad/<str:pk>/', views.eliminarEspecialidad, name='eliminar_especialidad'),


]
