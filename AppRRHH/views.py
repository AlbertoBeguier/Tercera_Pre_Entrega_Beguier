from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from AppRRHH.models import Empresa,Empleado,Tarea,ConvenioColectivo
from .forms import EmpresaFormulario, EmpleadoFormulario,TareaFormulario,ConvenioColectivoFormulario


# Create your views here.
def inicio(request):
    return render(request, "inicio.html")


def listaEmpresas(request):
    listaEmpresas=Empresa.objects.all()
    return render(request, "listaEmpresas.html", {"listaEmpresas":listaEmpresas})

def listaEmpleados(request):
    listaEmpleados=Empleado.objects.all()
    return render(request, "listaEmpleados.html", {"listaEmpleados":listaEmpleados})

def listaTareas(request):
    listaTareas=Tarea.objects.all()
    return render(request, "listaTareas.html", {"listaTareas":listaTareas})

def listaConveniosColectivos(request):
    listaConveniosColectivos=ConvenioColectivo.objects.all()
    return render(request, "listaConveniosColectivos.html", {"listaConveniosColectivos":listaConveniosColectivos})

def empresasFormulario(request):
    if request.method == "POST":
        empFormulario = EmpresaFormulario(request.POST)
        if empFormulario.is_valid():
            data=empFormulario.cleaned_data
            empresa=Empresa(nombre=data["nombre"], cuit=data["cuit"], actividadPrincipal=data["actividadPrincipal"])
            empresa.save()
            return render(request, "inicio.html")
    else:
        empFormulario = EmpresaFormulario()
        return render(request, "empresasFormulario.html", {"empFormulario":empFormulario})

def empleadosFormulario(request):
    if request.method == "POST":
        empleadFormulario = EmpleadoFormulario(request.POST)
        if empleadFormulario.is_valid():
            data=empleadFormulario.cleaned_data
            empleado=Empleado(nombre=data["nombre"], cuil=data["cuil"], legajo=data["legajo"],fecha_ingreso=data["fecha_ingreso"])
            empleado.save()
            return render(request, "inicio.html")
    else:
        empleadFormulario = EmpleadoFormulario()
        return render(request, "empleadosFormulario.html", {"empleadFormulario":empleadFormulario})
    
    
def tareasFormulario(request):
    if request.method == "POST":
        tarFormulario = TareaFormulario(request.POST)
        if tarFormulario.is_valid():
            data=tarFormulario.cleaned_data
            tarea=Tarea(tarea=data["tarea"])
            tarea.save()
            return render(request, "inicio.html")
    else:
        tarFormulario = TareaFormulario()
        return render(request, "tareasFormulario.html", {"tarFormulario":tarFormulario})
    
def conveniosFormulario(request):
    if request.method == "POST":
        convFormulario = ConvenioColectivoFormulario(request.POST)
        if convFormulario.is_valid():
            data=convFormulario.cleaned_data
            convenio=ConvenioColectivo(nro_cct=data["nro_cct"],nombre_cct=data["nombre_cct"])
            convenio.save()
            return render(request, "inicio.html")
    else:
        convFormulario = ConvenioColectivoFormulario()
        return render(request, "conveniosFormulario.html", {"convFormulario":convFormulario})
    
    
def busquedaEmpleados(request):
    return render(request,"busquedaEmpleados.html")
    
def buscar(request:HttpRequest):
    try:
        if request.GET["busca_nombre"]:
            nombre = request.GET["busca_nombre"]
            
            empleado = Empleado.objects.filter(nombre__icontains=nombre)
            return render(request, "resultadosBusqueda.html", {"empleado": empleado})
   
    except:     
        return HttpResponse ("El empleado que está buscando no existe")