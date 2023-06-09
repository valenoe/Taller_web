from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'fichasapp'

urlpatterns  = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('usuario/', views.usuarios, name='usuario'),
    path('crear_usuario/', views.crearUsuario, name='crear_usuario'), 
    path('modificar_usuario/<str:pk>', views.modificarUsuario, name='modificar_usuario'),
    path('eliminar_usuario/<str:pk>', views.eliminarUsuario, name='eliminar_usuario'), 
    path('accounts/', include("django.contrib.auth.urls")),
]