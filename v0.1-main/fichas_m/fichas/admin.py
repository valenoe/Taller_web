from django.contrib import admin
from .models import *

admin.site.site_header = 'Administración Fichas Medicas'
admin.site.site_title = 'Administración Fichas Medicas'
admin.site.index_title = 'Bienvenido'

admin.site.register(Usuario)
admin.site.register(Especialidad)
admin.site.register(Rol)
admin.site.register(PersonalSalud)
admin.site.register(Horas)
admin.site.register(Ficha)
admin.site.register(Cita)
admin.site.register(DatosAtencion)
admin.site.register(Tratamiento)

