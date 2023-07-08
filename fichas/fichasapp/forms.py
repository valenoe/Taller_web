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

    def save(self, commit=True):
        instance = super().save(commit=commit)
        if commit:
            create_hours_for_doctor(instance)
        return instance


class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ('name',)
        labels = {'name': 'Nombre'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FichaForm(forms.ModelForm):

    class Meta:
        model = Ficha
        fields = ('rut', 'nombre', 'apellido', 'fecha_nacimiento', 'prevision_salud', 'tipo_isapre', 'domicilio', 'sexo')
        labels = {
            'rut': 'RUT',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'prevision_salud': 'Previsión de Salud',
            'tipo_isapre': 'Tipo_isapre',
            'domicilio': 'Domicilio',
            'sexo': 'Sexo',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'prevision_salud': forms.Select(attrs={'class': 'form-select'}),
            'tipo_isapre': forms.Select(attrs={'class': 'form-select'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
        }


class HorasForm(forms.ModelForm):
    hora = forms.TimeField(widget=forms.Select(
        choices=[('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'),
                 ('12:00', '12:00'), ('13:00', '13:00'), ('15:00', '15:00'),
                 ('16:00', '16:00'), ('17:00', '17:00')],
        attrs={'class': 'form-control'}))

    class Meta:
        model = Horas
        fields = ('fecha', 'hora', 'id_medico', 'ocupada')
        labels = {
            'fecha': 'Fecha',
            'hora': 'Hora',
            'id_medico': 'Médico',
            'ocupada': 'Ocupada',
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'id_medico': forms.Select(attrs={'class': 'form-select'}),
            'ocupada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_medico'].queryset = PersonalSalud.objects.all()


def create_hours_for_doctor(doctor_instance):
    working_hours = [('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'),
                     ('12:00', '12:00'), ('13:00', '13:00'), ('15:00', '15:00'),
                     ('16:00', '16:00'), ('17:00', '17:00')]

    for hour in working_hours:
        Horas.objects.create(hora=hour[0], id_medico=doctor_instance)


class CitaForm(forms.ModelForm):

    rut_paciente = forms.CharField(
        label='RUT del Paciente',
        max_length=13,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    id_medico = forms.ModelChoiceField(
        label='Médico',
        queryset=PersonalSalud.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    id_horario = forms.ModelChoiceField(
        label='Horario',
        queryset=Horas.objects.none(),  # Initialize with an empty queryset
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_horario'}),  # Add ID attribute
    )
    acompannante = forms.CharField(
        label='Acompañante',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    telefono = forms.CharField(
        label='Teléfono',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    correo = forms.EmailField(
        label='Correo Electrónico',
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Cita
        fields = ('rut_paciente', 'id_horario', 'acompannante', 'id_medico', 'telefono', 'correo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_horario'].queryset = self.get_available_horas()

    def get_available_horas(self):
        id_medico = self.initial.get('id_medico') or self.data.get('id_medico')
        if id_medico:
            return Horas.objects.filter(id_medico=id_medico, ocupada=False)
        else:
            return Horas.objects.none()
