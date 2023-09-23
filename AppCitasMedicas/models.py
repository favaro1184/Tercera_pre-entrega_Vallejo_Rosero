from django.db import models

# Create your models here.
class Paciente(models.Model):
    id_paciente = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
class Medico(models.Model):
    id_medico = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    profesion = models.CharField(max_length=40)
    
class Clinica(models.Model):
    id_clinica = models.IntegerField()
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=80)
    
class Cita(models.Model):
    id_cita = models.IntegerField()
    id_paciente = models.IntegerField()
    id_medico = models.IntegerField()
    id_clinica = models.IntegerField()
    fecha_de_cita = models.DateField()