from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    cuit = models.IntegerField()

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    cuil = models.IntegerField(max_length=11)
    legajo = models.IntegerField()
    fecha_ingreso = models.DateField

class Tarea(models.Model):
    tarea = models.CharField(max_length=20)





    

