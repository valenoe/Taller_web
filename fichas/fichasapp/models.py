from django.db import models
    
class Usuario(models.Model):
    ROL = (('Administrador', 'Administrador'),
    ('Funcionario', 'Funcionario'),
    ('Usuario', 'Usuario'),
    )
    nombre = models.CharField(max_length=50, null=True) 
    apellido = models.CharField(max_length=50, null=True)
    rut = models.CharField(max_length=13, null=True)
    correo = models.EmailField(max_length=50, null=True)
    rol = models.CharField(max_length=200, null=True, choices=ROL)

    def __str__(self):
        return self.nombre


class Especialidad(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Rol(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class PersonalSalud(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario
    
class Horas(models.Model):

    fecha = models.DateField(null=True)
    hora = models.TimeField(null=True)
    id_medico = models.ForeignKey(PersonalSalud, on_delete=models.CASCADE)
    ocupada = models.BooleanField()
    def __str__(self):
        return self.fecha
    
class Ficha(models.Model):
    PREVISION = (('Fonasa', 'Fonasa'),
    ('Isapre', 'Isapre'),
    )
    SEXO = (('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
    ('Intersexual', 'Intersexual'),
    )
    ISAPRE = (('Colmena', 'Colmena'),
    ('CruzBlanca', 'CruzBlanca'),
    ('Consalud', 'Consalud'),
    ('MasVda', 'MasVda'),
    ('BanMedica', 'BanMedica'),
    )
    rut = models.CharField(max_length=13)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField()
    prevision_salud = models.CharField(max_length=200, null=True, choices=PREVISION)
    tipo_isapre = models.CharField(max_length=200, null=True, choices=ISAPRE)
    domicilio = models.CharField(max_length=100)
    sexo = models.CharField(max_length=200, null=True, choices=SEXO)

    def __str__(self):
        return self.nombre
    
class Cita(models.Model):
    rut_paciente = models.CharField(max_length=13)
    id_horario = models.ForeignKey(Horas, on_delete=models.CASCADE)
    acompannante = models.CharField(max_length=100)
    id_medico = models.ForeignKey(PersonalSalud, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return self.rut_paciente
    
    
class DatosAtencion(models.Model):
    id_cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    paologia_ges = models.CharField(max_length=100)
    diagnostico_principal  =models.CharField(max_length=100)
    disgnotico_complementario = models.TextField()
    presion = models.CharField(max_length=100, default='')
    temperatura = models.CharField(max_length=100,default='')
    peso = models.CharField(max_length=100,default='')
    satO2 = models.CharField(max_length=100,default='')
    pulso = models.CharField(max_length=100,default='')
    alergias = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.diagnostico_principal
    
class Tratamiento(models.Model):
    medicamento = models.CharField(max_length=100)
    indicaciones = models.TextField()
    def __str__(self):
        return self.medicamento
    
    

