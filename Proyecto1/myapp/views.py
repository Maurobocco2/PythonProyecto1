from django.shortcuts import render, redirect
from .models import Cliente, Tecnico, Equipo, Reparacion
from .forms import ClientesFormulario, ClientesFilter, TecnicosFormulario, TecnicosFilter, EquiposFormulario, EquiposFilter, ReparacionesFormulario, ReparacionesFilter
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

def editar_tecnico(request, id):
    tecnico = get_object_or_404(Tecnico, id=id)
    if request.method == "POST":
        form = TecnicosFilter(request.POST, instance=tecnico)
        if form.is_valid():
            form.save()
            return redirect('myapp:tecnicos')
    else:
        form = TecnicosFilter(instance=tecnico)
    return render(request, 'myapp/editar_tecnico.html', {'form': form, 'tecnico': tecnico})

def eliminar_tecnico(request, id):
    tecnico = get_object_or_404(Tecnico, id=id)
    if request.method == 'POST':
        tecnico.delete()
        return redirect('myapp:tecnicos')
    return render(request, 'myapp/tecnicos.html', {'tecnico': tecnico})

#EQUIPOS

def agregar_equipo(request):
    if request.method == 'POST':
        form = EquiposFormulario(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data['clientes']
            tipo = form.cleaned_data['tipo']
            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']
            numero_serie = form.cleaned_data['numero_serie']
            observaciones = form.cleaned_data['observaciones']
           
            equipo = Equipo(cliente = cliente, tipo = tipo, marca = marca, modelo = modelo, numero_serie = numero_serie, observaciones = observaciones)
            equipo.save()
            return redirect('myapp:equipos')
    else:
        form = EquiposFormulario()
        return render(request, 'myapp/agregar_equipo.html', {'form': form})


def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        form = EquiposFilter(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('myapp:equipos')
    else:
        form = EquiposFilter(instance=equipo)
    return render(request, 'myapp/editar_equipo.html', {'form': form, 'equipo': equipo})

def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('myapp:equipos')
    return render(request, 'myapp/equipos.html', {'equipo': equipo})


def agregar_reparacion(request):
    if request.method == 'POST':
        form = ReparacionesFormulario(request.POST)

        if form.is_valid():
            equipo = form.cleaned_data['equipo']
            tecnico = form.cleaned_data['tecnico']
            fecha_ingreso = form.cleaned_data['fecha_ingreso']
            problema_reportado = form.cleaned_data['problema_reportado']
            estado = form.cleaned_data['estado']

            reparacion = Reparacion(
                equipo=equipo,
                tecnico=tecnico,
                fecha_ingreso=fecha_ingreso,
                problema_reportado=problema_reportado,
                estado=estado
            )

            reparacion.save()

            return redirect('myapp:reparaciones')

    else:
        form = ReparacionesFormulario()

    return render(
        request,
        'myapp/agregar_reparacion.html',
        {'form': form}
    )


def editar_reparacion(request, id):
    reparacion = get_object_or_404(Reparacion, id=id)

    if request.method == 'POST':
        form = ReparacionesFilter(request.POST, instance=reparacion)

        if form.is_valid():
            form.save()
            return redirect('myapp:reparaciones')

    else:
        form = ReparacionesFilter(instance=reparacion)

    return render(
        request,
        'myapp/editar_reparacion.html',
        {
            'form': form,
            'reparacion': reparacion
        }
    )

def eliminar_reparacion(request, id):
    if request.method == 'POST':
        reparacion = get_object_or_404(Reparacion, id=id)
        reparacion.delete()

    return redirect('myapp:reparaciones')