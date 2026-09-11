from django.shortcuts import render, redirect
from .models import Cliente, Tecnico, Equipo, Reparacion
from .forms import ClientesFormulario, ClientesFilter
from django.db import models



# Create your views here.
def index(request):
    context = {"mensaje": "Ofrecemos servicios de reparación de computadoras, mantenimiento y soporte técnico."}
    return render(request, "myapp/index.html", context)

def clientes(request):
    query = request.GET.get('q')  # Captura lo que se escribe en el buscador
    if query:
        clientes = Cliente.objects.filter(
            models.Q(nombre__icontains=query) |
            models.Q(apellido__icontains=query) |
            models.Q(email__icontains=query)
        )
    else:
        clientes = Cliente.objects.all()


    return render(request, 'myapp/clientes.html', {
        'clientes': clientes,
        'query': query,
    })


def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, "myapp/equipos.html", {"equipos": equipos})

def reparaciones(request):
    reparaciones= Reparacion.objects.all()
    return render(request, "myapp/reparaciones.html", {"reparaciones": reparaciones})

def tecnicos(request):
    tecnicos = Tecnico.objects.all()
    return render(request, "myapp/tecnicos.html", {"tecnicos": tecnicos})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClientesFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            direccion = form.cleaned_data['direccion']
            cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono, email=email, direccion=direccion)
            cliente.save()
            return redirect('myapp:clientes')
    else:
        form = ClientesFormulario()
        return render(request, 'myapp/agregar_cliente.html', {'form': form})
