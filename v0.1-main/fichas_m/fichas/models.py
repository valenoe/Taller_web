from django.db import models

class Especialidad(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Rol(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Usuario(models.Model):

    rut = models.CharField(max_length=13)
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut
    
class PersonalSalud(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario
    
class Horas(models.Model):

    fecha = models.DateTimeField()
    id_medico = models.ForeignKey(PersonalSalud, on_delete=models.CASCADE)
    ocupada = models.BooleanField()
    def __str__(self):
        return self.fecha
    
class Ficha(models.Model):

    rut = models.CharField(max_length=13)
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField()
    previcion_salud = models.CharField(max_length=13)
    domicilio = models.CharField(max_length=100)
    sexo= models.CharField(max_length=50)

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
    

class Antecedentes(models.Model):
    
    title = models.CharField(max_length=100)
    id_cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    presion = models.CharField(max_length=100)
    temperatura = models.CharField(max_length=100)
    peso = models.CharField(max_length=100)
    satO2 = models.CharField(max_length=100)
    pulso = models.CharField(max_length=100)
    alergias = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
class DatosAtencion(models.Model):
    title = models.CharField(max_length=100)
    id_cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    paologia_ges = models.CharField(max_length=100)
    diagnostico_principal  =models.CharField(max_length=100)
    disgnotico_complementario = models.TextField()
    def __str__(self):
        return self.title
    

