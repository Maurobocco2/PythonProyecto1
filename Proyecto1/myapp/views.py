from django.shortcuts import render, redirect
from .models import Cliente, Tecnico, Equipo, Reparacion
from .forms import ClientesFormulario, ClientesFilter, TecnicosFormulario
from django.db import models
from django.shortcuts import get_object_or_404 


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
    query = request.GET.get('q')
    if query:
        tecnicos = Tecnico.objects.filter(
            models.Q(nombre__icontains = query)|
            models.Q(apellido__icontains = query)
        )
    else:

        tecnicos = Tecnico.objects.all()
    return render(request, 'myapp/tecnicos.html', {
        'tecnicos': tecnicos, 
        'query': query
    })

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

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
   
    if request.method == 'POST':
        form = ClientesFilter(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('myapp:clientes')
    else:
        form = ClientesFilter(instance=cliente)
   
    return render(request, 'myapp/editar_cliente.html', {'form': form, 'cliente': cliente})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)


    if request.method == 'POST':
        cliente.delete()
        return redirect('myapp:clientes')
    return render(request, 'myapp/clientes.html', {'cliente': cliente})


# TECNICOS

def agregar_tecnico(request):
    if request.method == 'POST':
        form = TecnicosFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            especialidad = form.cleaned_data['especialidad']
            telefono = form.cleaned_data['telefono']

            tecnico = Tecnico(nombre = nombre, apellido = apellido, especialidad = especialidad, telefono = telefono)
            tecnico.save()
            return redirect('myapp:tecnicos')
    else:
        form = TecnicosFormulario()
        return render(request, 'myapp/agregar_tecnico.html', {'form': form})