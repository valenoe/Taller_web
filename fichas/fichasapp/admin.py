from django.contrib import admin
from .models import Usuario
admin.site.site_header = 'Administración Fichas Medicas'
admin.site.site_title = 'Administración Fichas Medicas'
admin.site.index_title = 'Bienvenido'

admin.site.register(Usuario)

