from django import forms
from django.core.exceptions import ValidationError
from datetime import date, timedelta
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


class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = '__all__'  # To include all fields from the model

        labels = {
            'usuario':'Usuario',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'prevision_salud': 'Previsión de Salud',
            'tipo_isapre': 'Tipo de Isapre',
            'domicilio': 'Domicilio',
            'sexo': 'Sexo',
        }

        widgets = {
            'fecha_nacimiento': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'prevision_salud': forms.Select(attrs={'class': 'form-control'}),
            'tipo_isapre': forms.Select(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].queryset = Usuario.objects.all()



class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'

        labels = {
            'usuario': 'Usuario',
            'id_medico': 'Médico',
            'id_horario': 'Horario',
            'acompannante': 'Acompañante',
            'telefono': 'Teléfono',
            'correo': 'Correo Electrónico',
        }

        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'id_medico': forms.Select(attrs={'class': 'form-control'}),
            'id_horario': forms.Select(attrs={'class': 'form-control horario-select', 'placeholder': 'Select a Médico first'}),
            'acompannante': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_medico'].queryset = PersonalSalud.objects.all()

        if 'id_medico' in self.data:
            # Get the selected id_medico from the form data
            id_medico_id = self.data['id_medico']
            if id_medico_id:
                # Filter the id_horario choices based on the selected id_medico
                horarios = Horas.objects.filter(id_medico_id=id_medico_id, ocupada=False)
                self.fields['id_horario'].queryset = horarios
            else:
                # If no id_medico is selected, show all available id_horarios
                self.fields['id_horario'].queryset = Horas.objects.filter(ocupada=False)
        else:
            # If no form data is available, show all available id_horarios
            self.fields['id_horario'].queryset = Horas.objects.filter(ocupada=False)

    def clean(self):
        cleaned_data = super().clean()
        id_horario = cleaned_data.get('id_horario')
        id_medico = cleaned_data.get('id_medico')

        if id_horario and id_medico:
            if Cita.objects.filter(id_horario=id_horario, id_medico=id_medico).exists():
                raise ValidationError('This combination of horario and médico already exists.')

        return cleaned_data
        
    def save(self, commit=True):
        cita = super().save(commit=False)
        id_horario = self.cleaned_data.get('id_horario')
        if id_horario:
            # Update the ocupada field to True when an id_horario is selected
            cita.id_horario.ocupada = True
            cita.id_horario.save()

        if commit:
            cita.save()

        return cita



class HorasForm(forms.ModelForm):
    hora = forms.ChoiceField(
        choices=[('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), 
                 ('12:00', '12:00'), ('13:00', '13:00'), ('15:00', '15:00'), 
                 ('16:00', '16:00'), ('17:00', '17:00')], 
        widget=forms.Select(attrs={'class': 'form-control'}))
    
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
            'fecha': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date',
                'min': date.today().strftime('%Y-%m-%d')  # Establecer la fecha mínima como el día actual
            }),
            'id_medico': forms.Select(attrs={'class': 'form-select'}),
            'ocupada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_medico'].queryset = PersonalSalud.objects.all()

        if self.instance:
            self.initial['fecha'] = self.instance.fecha
            self.initial['hora'] = self.instance.hora

    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        hora = cleaned_data.get('hora')
        id_medico = cleaned_data.get('id_medico')

        # Check if an instance with the same fecha, hora, and id_medico exists
        if fecha and hora and id_medico:
            if Horas.objects.filter(fecha=fecha, hora=hora, id_medico=id_medico).exists():
                raise ValidationError('This combination of fecha, hora, and doctor already exists.')

        return cleaned_data
        
PATOLOGIAS_GES_CHOICES = [
    ('Sin Patología GES', 'Sin Patología GES'),
    ('Enfermedad renal crónica etapa 4 y 5', 'Enfermedad renal crónica etapa 4 y 5'),
    ('Cardiopatías congénitas operables en menores de 15 años', 'Cardiopatías congénitas operables en menores de 15 años'),
    ('Cáncer cérvico-uterino', 'Cáncer cérvico-uterino'),
    ('Alivio del dolor y cuidados paliativos por cáncer avanzado', 'Alivio del dolor y cuidados paliativos por cáncer avanzado'),
    ('Infarto agudo del miocardio', 'Infarto agudo del miocardio'),
    ('Diabetes Mellitus tipo I', 'Diabetes Mellitus tipo I'),
    ('Diabetes Mellitus tipo II', 'Diabetes Mellitus tipo II'),
    ('Cáncer de mama en personas de 15 años y más', 'Cáncer de mama en personas de 15 años y más'),
    ('Disrafias espinales', 'Disrafias espinales'),
    ('Tratamiento quirúrgico de escoliosis en personas menores de 25 años', 'Tratamiento quirúrgico de escoliosis en personas menores de 25 años'),
    ('Tratamiento quirúrgico de cataratas', 'Tratamiento quirúrgico de cataratas'),
    ('Endoprótesis total de cadera en personas de 65 años y más con artrosis de cadera con limitación funcional severa', 'Endoprótesis total de cadera en personas de 65 años y más con artrosis de cadera con limitación funcional severa'),
    ('Fisura Labiopalatina', 'Fisura Labiopalatina'),
    ('Cáncer en personas menores de 15 años', 'Cáncer en personas menores de 15 años'),
    ('Esquizofrenia', 'Esquizofrenia'),
    ('Cáncer de testículo en personas de 15 años y más', 'Cáncer de testículo en personas de 15 años y más'),
    ('Linfomas en personas de 15 años y más', 'Linfomas en personas de 15 años y más'),
    ('Síndrome de la inmunodeficiencia adquirida VIH/SIDA', 'Síndrome de la inmunodeficiencia adquirida VIH/SIDA'),
    ('Infección respiratoria aguda (IRA) de manejo ambulatorio en personas menores de 5 años', 'Infección respiratoria aguda (IRA) de manejo ambulatorio en personas menores de 5 años'),
    ('Neumonia adquirida en la comunidad de manejo ambulatorio en personas de 65 años y más', 'Neumonia adquirida en la comunidad de manejo ambulatorio en personas de 65 años y más'),
    ('Hipertensión arterial primaria o esencial en personas de 15 años y más', 'Hipertensión arterial primaria o esencial en personas de 15 años y más'),
    ('Epilepsia no refractaria en personas desde 1 año y menores de 15 años', 'Epilepsia no refractaria en personas desde 1 año y menores de 15 años'),
    ('Salud oral integral para niños y niñas de 6 años', 'Salud oral integral para niños y niñas de 6 años'),
    ('Prevención de parto prematuro', 'Prevención de parto prematuro'),
    ('Trastornos de generación del impulso y conducción en personas de 15 años y más, que requieren marcapaso', 'Trastornos de generación del impulso y conducción en personas de 15 años y más, que requieren marcapaso'),
    ('Colecistectomía preventiva del cáncer de vesícula en personas de 35 a 49 años', 'Colecistectomía preventiva del cáncer de vesícula en personas de 35 a 49 años'),
    ('Cáncer gástrico', 'Cáncer gástrico'),
    ('Cáncer de próstata en personas de 15 años y más', 'Cáncer de próstata en personas de 15 años y más'),
    ('Vicios de refracción en personas de 65 años y más', 'Vicios de refracción en personas de 65 años y más'),
    ('Estrabismo en personas menores de 9 años', 'Estrabismo en personas menores de 9 años'),
    ('Retinopatía diabética', 'Retinopatía diabética'),
    ('Desprendimiento de retina regmatógeno no traumático', 'Desprendimiento de retina regmatógeno no traumático'),
    ('Hemofilia', 'Hemofilia'),
    ('Depresión en personas de 15 años y más', 'Depresión en personas de 15 años y más'),
    ('Tratamiento de la hiperplasia benigna de la próstata en personas sintomáticas', 'Tratamiento de la hiperplasia benigna de la próstata en personas sintomáticas'),
    ('Órtesis (o ayudas técnicas) para personas de 65 años y más', 'Órtesis (o ayudas técnicas) para personas de 65 años y más'),
    ('Accidente cerebrovascular isquémico en personas de 15 años y más', 'Accidente cerebrovascular isquémico en personas de 15 años y más'),
    ('Enfermedad pulmonar obstructiva crónica de tratamiento ambulatorio', 'Enfermedad pulmonar obstructiva crónica de tratamiento ambulatorio'),
    ('Asma bronquial moderada y grave en menores de 15 años', 'Asma bronquial moderada y grave en menores de 15 años'),
    ('Síndrome de dificultad respiratoria en el recién nacido', 'Síndrome de dificultad respiratoria en el recién nacido'),
    ('Tratamiento médico en personas de 55 años y más con artrosis de cadera y/o rodilla, leve o moderada', 'Tratamiento médico en personas de 55 años y más con artrosis de cadera y/o rodilla, leve o moderada'),
    ('Hemorragia subaracnoidea secundaria a ruptura de aneurismas cerebrales', 'Hemorragia subaracnoidea secundaria a ruptura de aneurismas cerebrales'),
    ('Tumores primarios del sistema nervioso central en personas de 15 años y más', 'Tumores primarios del sistema nervioso central en personas de 15 años y más'),
    ('Tratamiento quirúrgico de hernia del núcleo pulposo lumbar', 'Tratamiento quirúrgico de hernia del núcleo pulposo lumbar'),
    ('Leucemia en personas de 15 años y más', 'Leucemia en personas de 15 años y más'),
    ('Urgencia odontológica ambulatoria', 'Urgencia odontológica ambulatoria'),
    ('Salud oral integral del adulto de 60 años', 'Salud oral integral del adulto de 60 años'),
    ('Politraumatizado grave', 'Politraumatizado grave'),
    ('Traumatismo cráneo encefálico moderado o grave', 'Traumatismo cráneo encefálico moderado o grave'),
    ('Trauma ocular grave', 'Trauma ocular grave'),
    ('Fibrosis quística', 'Fibrosis quística'),
    ('Artritis reumatoidea', 'Artritis reumatoidea'),
    ('Consumo perjudicial o dependencia de riesgo bajo a moderado de alcohol y drogas en personas menores de 20 años', 'Consumo perjudicial o dependencia de riesgo bajo a moderado de alcohol y drogas en personas menores de 20 años'),
    ('Analgesia del parto', 'Analgesia del parto'),
    ('Gran quemado', 'Gran quemado'),
    ('Hipoacusia bilateral en personas de 65 años y más que requieren uso de audífono', 'Hipoacusia bilateral en personas de 65 años y más que requieren uso de audífono'),
    ('Retinopatía del prematuro', 'Retinopatía del prematuro'),
    ('Displasia broncopulmonar del prematuro', 'Displasia broncopulmonar del prematuro'),
    ('Hipoacusia neurosensorial bilateral del prematuro', 'Hipoacusia neurosensorial bilateral del prematuro'),
    ('Epilepsia no refractaria en personas de 15 años y más', 'Epilepsia no refractaria en personas de 15 años y más'),
    ('Asma bronquial en personas de 15 años y más', 'Asma bronquial en personas de 15 años y más'),
    ('Enfermedad de Parkinson', 'Enfermedad de Parkinson'),
    ('Artritis idiopática juvenil', 'Artritis idiopática juvenil'),
    ('Prevención secundaria enfermedad renal crónica terminal', 'Prevención secundaria enfermedad renal crónica terminal'),
    ('Displasia luxante de caderas', 'Displasia luxante de caderas'),
    ('Salud oral integral de la embarazada', 'Salud oral integral de la embarazada'),
    ('Esclerosis múltiple remitente recurrente', 'Esclerosis múltiple remitente recurrente'),
    ('Hepatitis crónica por virus hepatitis B', 'Hepatitis crónica por virus hepatitis B'),
    ('Hepatitis C', 'Hepatitis C'),
    ('Cáncer colorectal en personas de 15 años y más', 'Cáncer colorectal en personas de 15 años y más'),
    ('Cáncer de ovario epitelial', 'Cáncer de ovario epitelial'),
    ('Cáncer vesical en personas de 15 años y más', 'Cáncer vesical en personas de 15 años y más'),
    ('Osteosarcoma en personas de 15 años y más', 'Osteosarcoma en personas de 15 años y más'),
    ('Tratamiento quirúrgico de lesiones crónicas de la válvula aórtica en personas de 15 años y más', 'Tratamiento quirúrgico de lesiones crónicas de la válvula aórtica en personas de 15 años y más'),
    ('Trastorno bipolar en personas de 15 años y más', 'Trastorno bipolar en personas de 15 años y más'),
    ('Hipotiroidismo en personas de 15 años y más', 'Hipotiroidismo en personas de 15 años y más'),
    ('Tratamiento de hipoacusia moderada en menores de 2 años', 'Tratamiento de hipoacusia moderada en menores de 2 años'),
    ('Lupus eritematoso sistémico', 'Lupus eritematoso sistémico'),
    ('Tratamiento quirúrgico de lesiones crónicas de las válvulas mitral y tricúspide en personas de 15 años y más', 'Tratamiento quirúrgico de lesiones crónicas de las válvulas mitral y tricúspide en personas de 15 años y más'),
    ('Tratamiento de erradicación del Helicobacter pylori', 'Tratamiento de erradicación del Helicobacter pylori'),
    ('Cáncer de Pulmón en personas de 15 años y más', 'Cáncer de Pulmón en personas de 15 años y más'),
    ('Cáncer de Tiroides diferenciado y medular en personas de 15 años', 'Cáncer de Tiroides diferenciado y medular en personas de 15 años'),
    ('Cáncer Renal en personas de 15 años y más', 'Cáncer Renal en personas de 15 años y más'),
    ('Mieloma Múltiple en personas de 15 años y más', 'Mieloma Múltiple en personas de 15 años y más'),
    ('Enfermedad de Alzheimer y otras demencias', 'Enfermedad de Alzheimer y otras demencias'),
]

class DatosAtencionForm(forms.ModelForm):
    patologia_ges = forms.ChoiceField(choices=PATOLOGIAS_GES_CHOICES, label='Patología GES')

    class Meta:
        model = DatosAtencion
        exclude = ['id_cita']
        fields = '__all__'
        labels = {
            'diagnostico_principal': 'Diagnóstico Principal',
            'disgnotico_complementario': 'Diagnóstico Complementario',
            'presion': 'Presión',
            'temperatura': 'Temperatura',
            'peso': 'Peso',
            'satO2': 'SatO2',
            'pulso': 'Pulso',
            'alergias': 'Alergias',
            'tratamiento': 'tratamiento',
        }
        widgets = {
            'diagnostico_principal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnóstico Principal'}),
            'disgnotico_complementario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnóstico Complementario'}),
            'presion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Presión'}),
            'temperatura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Temperatura'}),
            'peso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Peso'}),
            'satO2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SatO2'}),
            'pulso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pulso'}),
            'alergias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alergias'}),
            'tratamiento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tratamiento'}),
        }

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['name']
        labels = {
            'name': 'Nombre del Rol',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Administrador'}),
        }
        
class UsuarioPacienteForm(forms.ModelForm):
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
            'rol': forms.HiddenInput(),  # Hide the rol field from the user
        }
class FichaPacienteForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = '__all__'  # To include all fields from the model

        labels = {
            'usuario':'Usuario',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'prevision_salud': 'Previsión de Salud',
            'tipo_isapre': 'Tipo de Isapre',
            'domicilio': 'Domicilio',
            'sexo': 'Sexo',
        }

        widgets = {
            'fecha_nacimiento': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'prevision_salud': forms.Select(attrs={'class': 'form-control'}),
            'tipo_isapre': forms.Select(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.HiddenInput(),
        }

class CitaPacienteForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'

        labels = {
            'usuario': 'Usuario',
            'id_medico': 'Médico',
            'id_horario': 'Horario',
            'acompannante': 'Acompañante',
            'telefono': 'Teléfono',
            'correo': 'Correo Electrónico',
        }

        widgets = {
            'usuario': forms.HiddenInput(),
            'id_medico': forms.Select(attrs={'class': 'form-control'}),
            'id_horario': forms.Select(attrs={'class': 'form-control horario-select', 'placeholder': 'Select a Médico first'}),
            'acompannante': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_medico'].queryset = PersonalSalud.objects.all()

        if 'id_medico' in self.data:
            # Get the selected id_medico from the form data
            id_medico_id = self.data['id_medico']
            if id_medico_id:
                # Filter the id_horario choices based on the selected id_medico
                horarios = Horas.objects.filter(id_medico_id=id_medico_id, ocupada=False)
                self.fields['id_horario'].queryset = horarios
            else:
                # If no id_medico is selected, show all available id_horarios
                self.fields['id_horario'].queryset = Horas.objects.filter(ocupada=False)
        else:
            # If no form data is available, show all available id_horarios
            self.fields['id_horario'].queryset = Horas.objects.filter(ocupada=False)

    def clean(self):
        cleaned_data = super().clean()
        id_horario = cleaned_data.get('id_horario')
        id_medico = cleaned_data.get('id_medico')

        if id_horario and id_medico:
            if Cita.objects.filter(id_horario=id_horario, id_medico=id_medico).exists():
                raise ValidationError('This combination of horario and médico already exists.')

        return cleaned_data
        
    def save(self, commit=True):
        cita = super().save(commit=False)
        id_horario = self.cleaned_data.get('id_horario')
        if id_horario:
            # Update the ocupada field to True when an id_horario is selected
            cita.id_horario.ocupada = True
            cita.id_horario.save()

        if commit:
            cita.save()

        return cita
