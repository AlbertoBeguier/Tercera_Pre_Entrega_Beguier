from django.db import models
from datetime import datetime

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    cuit = models.IntegerField()
    actividadPrincipal = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f"Razón Social: {self.nombre}  - Nro. CUIT:  {self.cuit}  - Actividad Principal:  {self.actividadPrincipal}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    cuil = models.IntegerField()
    legajo = models.IntegerField()
    fecha_ingreso = models.DateField(null=True)
    
    def __str__(self):
        return f"Legajo: {self.legajo}  - Nombre:  {self.nombre}"
    
class Tarea(models.Model):
    tarea = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Tarea: {self.tarea}"

class ConvenioColectivo(models.Model):
    nro_cct = models.CharField(max_length=10)
    nombre_cct = models.CharField(max_length=30)

    def __str__(self):
        return f"CCT: {self.nro_cct}-{self.nombre_cct}"

    
    







    

