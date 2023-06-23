from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'fichasapp'

urlpatterns= [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', views.home, name='index'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('crear_usuario/', views.create_usuario, name='crear_usuario'),
    path('modificar_usuario/<str:pk>', views.edit_usuario, name='modificar_usuario'),
    path('eliminar_usuario/<str:pk>', views.delete_usuario, name='eliminar_usuario'),
    path('mostrar_usuario/<str:pk>', views.view_usuario, name='mostrar_usuario'),
    path('personalsalud/', views.personalSalud, name='personalsalud'),
    path('crear_personal/', views.create_personalSalud, name='crear_personal'),
    path('menu/', views.home, name='menu'),
    path('modificar_personal/<str:pk>', views.edit_personalSalud, name='modificar_personal'),
    path('eliminar_personal/<str:pk>', views.delete_personalSalud, name='eliminar_personal'),
    path('mostrar_personal/<str:pk>', views.view_personalSalud, name='mostrar_personal'),
    path('especialidad/', views.especialidad, name='especialidad'),
    path('crear_especialidad/', views.create_especialidad, name='crear_especialidad'),
    path('modificar_especialidad/<str:pk>/', views.edit_especialidad, name='modificar_especialidad'),
    path('eliminar_especialidad/<str:pk>/', views.delete_especialidad, name='eliminar_especialidad'),
    path('mostrar_especialidad/<str:pk>', views.view_especialidad, name='mostrar_especialidad'),

]
