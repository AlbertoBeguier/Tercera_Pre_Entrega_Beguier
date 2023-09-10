from django.contrib import admin
from .models import Empresa,Empleado,Tarea,ConvenioColectivo
# Register your models here.
admin.site.register(Empresa)
admin.site.register(Empleado)
admin.site.register(Tarea)
admin.site.register(ConvenioColectivo)