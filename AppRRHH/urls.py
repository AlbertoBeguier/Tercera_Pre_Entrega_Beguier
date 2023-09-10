
from django.urls import path
from AppRRHH.views import inicio,listaEmpresas,listaEmpleados,listaTareas,listaConveniosColectivos,empresasFormulario,empleadosFormulario,tareasFormulario,conveniosFormulario
from AppRRHH.forms import EmpresaFormulario, EmpleadoFormulario, TareaFormulario, ConvenioColectivoFormulario


urlpatterns = [
    path('', inicio, name="inicio"),
    path('listaEmpresas/',listaEmpresas, name="Empresas"),
    path('listaEmpleados/',listaEmpleados, name="Empleados"),
    path('listaTareas/',listaTareas, name="Tareas"),
    path('listaconveniosColectivos/',listaConveniosColectivos, name="ConveniosColectivos"),
    path('empresaFormularios/',empresasFormulario, name="EmpresaFormularios"),
    path('empleadoFormularios/',empleadosFormulario, name="EmpleadoFormularios"),
    path('tareaFormularios/',tareasFormulario, name="TareaFormularios"),
    path('convenioFormularios/',conveniosFormulario, name="ConvenioFormularios"),
]
