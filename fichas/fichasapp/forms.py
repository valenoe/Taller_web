from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'rut', 'correo', 'rol')
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'rut': 'RUT',
            'correo': 'Correo Electrónico',
            'rol': 'Rol',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-select'}),
        }

class PersonalSaludForm(forms.ModelForm):
    class Meta:
        model = PersonalSalud
        fields = ('usuario', 'especialidad')
        labels = {
            'usuario': 'Usuario',
            'especialidad': 'Especialidad'
        }
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-select'}),
            'especialidad': forms.Select(attrs={'class': 'form-select'}),
        }


class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ('name',)
        labels = {'name': 'Nombre'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
