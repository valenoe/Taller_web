from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'fichasapp'

urlpatterns= [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', views.home, name='index'),
    path('usuario/', views.usuarios, name='usuario'),
    path('crear_usuario/', views.crearUsuario, name='crear_usuario'), 
    path('modificar_usuario/<str:pk>', views.modificarUsuario, name='modificar_usuario'),
    path('eliminar_usuario/<str:pk>', views.eliminarUsuario, name='eliminar_usuario'),
    path('mostrar_usuario/<str:pk>', views.mostrar_usuario, name='mostrar_usuario'),
    path('personalsalud/', views.personalSalud, name='personalsalud'),
    path('crear_personal/', views.crearPersonal, name='crear_personal'),
    path('menu/', views.home, name='menu'),
    path('modificar_psalud/<str:pk>', views.modificarPersonal, name='modificar_personal'),
    path('eliminar_personal/<str:pk>', views.eliminarPersonal, name='eliminar_personal'),
    path('especialidad/', views.especialidad, name='especialidad'),
    path('crear_especialidad/', views.crear_especialidad, name='crear_especialidad'),
    path('modificar_especialidad/<str:pk>/', views.modificarEspecialidad, name='modificar_especialidad'),
    path('eliminar_especialidad/<str:pk>/', views.eliminarEspecialidad, name='eliminar_especialidad'),

]
