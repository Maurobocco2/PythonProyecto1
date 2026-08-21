from django.shortcuts import render
from .models import Cliente, Tecnico, Equipo, Reparacion

# Create your views here.
def index(request):
    context = {"mensaje": "Ofrecemos servicios de reparación de computadoras, mantenimiento y soporte técnico."}
    return render(request, "myapp/index.html", context)

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "myapp/clientes.html", {"clientes": clientes})

def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, "myapp/equipos.html", {"equipos": equipos})

def reparaciones(request):
    reparaciones= Reparacion.objects.all()
    return render(request, "myapp/reparaciones.html", {"reparaciones": reparaciones})

def tecnicos(request):
    tecnicos = Tecnico.objects.all()
    return render(request, "myapp/tecnicos.html", {"tecnicos": tecnicos})