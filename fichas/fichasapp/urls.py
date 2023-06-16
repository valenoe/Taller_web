from django.urls import *
from . import views

app_name = 'fichasapp'

urlpatterns  = [
    path('', views.home, name='index'),
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