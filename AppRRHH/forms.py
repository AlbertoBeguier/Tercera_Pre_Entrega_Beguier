from django import forms


class EmpresaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    cuit = forms.IntegerField(label="CUIT", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    actividad_Principal = forms.CharField(max_length=50 , label="Actividad Principal", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    
class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    cuil = forms.IntegerField(label="CUIL", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    legajo = forms.IntegerField(label="Legajo", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'})) 
    fecha_ingreso = forms.DateField(label="Fecha de Ingreso", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))

class TareaFormulario(forms.Form):
    tarea = forms.CharField(max_length=40, label="Tarea", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))

class ConvenioColectivoFormulario(forms.Form):
    nro_cct = forms.CharField(max_length=10, label="Número", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
    nombre_cct = forms.CharField(max_length=30, label="Nombre", widget=forms.TextInput(attrs={'class': 'alineacion-horizontal'}))
   

  