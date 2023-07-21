from django.db import models

class Rol(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Usuario(models.Model):

    nombre = models.CharField(max_length=50, null=True) 
    apellido = models.CharField(max_length=50, null=True)
    rut = models.CharField(max_length=13, null=True, unique=True, error_messages={'unique':"This email has already been registered."})
    correo = models.EmailField(max_length=50, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Especialidad(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class PersonalSalud(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, default=None)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.RESTRICT, default=None)

    def __str__(self):
        return self.usuario.nombre


class Horas(models.Model):

    fecha = models.DateField(null=True)
    hora = models.TimeField(null=True)
    id_medico = models.ForeignKey(PersonalSalud, on_delete=models.RESTRICT, default=None)
    ocupada = models.BooleanField(default=False)

    def __str__(self):
        return str(self.fecha)


class Cita(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, default=None)
    id_horario = models.ForeignKey(Horas, on_delete=models.RESTRICT, default=None)
    acompannante = models.CharField(max_length=100)
    id_medico = models.ForeignKey(PersonalSalud, on_delete=models.RESTRICT, default=None)
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.rut


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
              ('MasVida', 'MasVida'),
              ('BanMedica', 'BanMedica'),
              )
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, default=None)
    fecha_nacimiento = models.DateTimeField()
    prevision_salud = models.CharField(max_length=200, null=True, choices=PREVISION)
    tipo_isapre = models.CharField(max_length=200, null=True, choices=ISAPRE, default=None)
    domicilio = models.CharField(max_length=100)
    sexo = models.CharField(max_length=200, null=True, choices=SEXO)

    def __str__(self):
        return self.usuario.rut


class DatosAtencion(models.Model):
    id_cita = models.ForeignKey(Cita, on_delete=models.RESTRICT, default=None)
    patologia_ges = models.CharField(max_length=100, default=None)
    diagnostico_principal = models.CharField(max_length=100, default=None)
    disgnotico_complementario = models.CharField(max_length=100, default=None)
    presion = models.CharField(max_length=100, default=None)
    temperatura = models.CharField(max_length=100, default=None)
    peso = models.CharField(max_length=100, default=None)
    satO2 = models.CharField(max_length=100, default=None)
    pulso = models.CharField(max_length=100, default=None)
    alergias = models.CharField(max_length=100, default=None)
    tratamiento = models.CharField(max_length=100, default='Tratamiento')
    def __str__(self):
        return self.diagnostico_principal


