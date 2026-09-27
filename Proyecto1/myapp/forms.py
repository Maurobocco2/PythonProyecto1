from django import forms
from .models import Cliente, Tecnico, Equipo, Reparacion


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


class EquiposFormulario(forms.Form):

    TIPOS_EQUIPO = [
        ('PC', 'PC de Escritorio'),
        ('NOTEBOOK', 'Notebook'),
        ('NETBOOK', 'Netbook'),
        ('IMPRESORA', 'Impresora'),
        ('OTRO', 'Otro'),
    ]

    clientes = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        empty_label="Seleccione un cliente"
    )

    tipo = forms.ChoiceField(choices=TIPOS_EQUIPO, label='Nombre')
    marca = forms.CharField(max_length=50, label='Marca')
    modelo = forms.CharField(max_length=100, label='Modelo')
    numero_serie = forms.CharField(max_length=100, required=False, label='Numero-serie')
    observaciones = forms.CharField(widget=forms.Textarea,  required=False, label='Observaciones')

class EquiposFilter(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['tipo', 'marca', 'modelo', 'numero_serie', 'observaciones']


class ReparacionesFormulario(forms.Form):

    equipo = forms.ModelChoiceField(
        queryset=Equipo.objects.all(),
        empty_label="Seleccione un equipo",
        label="Equipo"
    )

    tecnico = forms.ModelChoiceField(
        queryset=Tecnico.objects.all(),
        empty_label="Seleccione un técnico",
        label="Técnico"
    )

    fecha_ingreso = forms.DateField(
        label="Fecha de ingreso",
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    problema_reportado = forms.CharField(
        label="Problema reportado",
        widget=forms.Textarea
    )

    estado = forms.ChoiceField(
        choices=Reparacion.ESTADOS,
        label="Estado"
    )