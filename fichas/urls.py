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
    path('fichas/', views.fichas, name='fichas'),
    path('crear_ficha/', views.create_ficha, name='crear_ficha'),
    path('modificar_ficha/<str:pk>', views.edit_ficha, name='modificar_ficha'),
    path('eliminar_ficha/<str:pk>', views.delete_ficha, name='eliminar_ficha'),
    path('mostrar_ficha/<str:pk>', views.view_ficha, name='mostrar_ficha'),
    path('horas/', views.horas, name='horas'),
    path('crear_horas/', views.create_horas, name='crear_horas'),
    path('modificar_hora/<str:pk>', views.edit_hora, name='modificar_hora'),
    path('mostrar_hora/<str:pk>', views.view_hora, name='mostrar_hora'),
    path('eliminar_hora/<str:pk>', views.delete_hora, name='eliminar_hora'),
    path('citas/', views.citas, name='citas'),
    path('crear_citas/', views.create_cita, name='crear_citas'),
    path('modificar_cita/<str:pk>', views.edit_cita, name='modificar_cita'),
    path('mostrar_cita/<str:pk>', views.view_cita, name='mostrar_cita'),
    path('eliminar_cita/<str:pk>', views.delete_cita, name='eliminar_cita'),
    path('get_horario_choices/', views.get_horario_choices, name='get_horario_choices'),
    path('citas/<int:cita_id>/crear/', views.crear_datos_atencion, name='crear_datos_atencion'),
    path('datos_atencion/<int:datos_atencion_id>/', views.detalle_datos_atencion, name='detalle_datos_atencion'),
    path('datos_atencion/<int:datos_atencion_id>/modificar/', views.modificar_datos_atencion, name='modificar_datos_atencion'),
    path('datos_atencion/<int:datos_atencion_id>/eliminar/', views.eliminar_datos_atencion, name='eliminar_datos_atencion'),
    path('lista_datos_atencion/', views.lista_datos_atencion, name='lista_datos_atencion'),
    path('roles/', views.listar_roles, name='listar_roles'),
    path('roles/crear/', views.crear_rol, name='crear_rol'),
    path('roles/ver/<int:rol_id>/', views.ver_rol, name='ver_rol'),
    path('roles/modificar/<int:rol_id>/', views.modificar_rol, name='modificar_rol'),
    path('roles/eliminar/<int:rol_id>/', views.eliminar_rol, name='eliminar_rol'),
    path('crear_paciente/', views.crear_paciente, name='crear_paciente'),
    path('ficha_paciente/<int:pk>/', views.ficha_paciente, name='ficha_paciente'),
    path('cita_paciente/<int:pk>/', views.cita_paciente, name='cita_paciente'),
]
