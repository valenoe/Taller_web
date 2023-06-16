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
