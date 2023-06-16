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
    path("accounts/", include("django.contrib.auth.urls")),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('crear_usuario/', views.create_usuario, name='crear_usuario'), 
    path('modificar_usuario/<str:pk>', views.edit_usuario, name='modificar_usuario'),
    path('eliminar_usuario/<str:pk>', views.delete_usuario, name='eliminar_usuario'), 
    path('mostrar_usuario/<str:pk>', views.view_usuario, name='mostrar_usuario'), 
    path('fichas/', views.fichas, name='fichas'),
    path('crear_ficha/', views.create_ficha, name='crear_ficha'), 
    path('modificar_ficha/<str:pk>', views.edit_ficha, name='modificar_ficha'),
    path('eliminar_ficha/<str:pk>', views.delete_ficha, name='eliminar_ficha'), 
    path('mostrar_ficha/<str:pk>', views.view_ficha, name='mostrar_ficha'), 
]
