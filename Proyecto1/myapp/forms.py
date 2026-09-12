from django import forms
from .models import Cliente, Tecnico


class ClientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    telefono = forms.CharField(max_length=20, label="Teléfono")
    email = forms.EmailField(label="Correo Electrónico")
    direccion = forms.CharField(max_length=200, label="Dirección")
class ClientesFilter(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email']


class TecnicosFormulario(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    telefono = forms.CharField(max_length=20, label= "Telefono")
    especialidad = forms.CharField(max_length=100, label="Especialidad")
class TecnicosFilter(forms.ModelForm):
     class Meta:
        model = Tecnico
        fields = ['nombre', 'apellido', 'telefono', 'especialidad']