from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Bienvenidos a mi app Django"}
    return render(request, "myapp/index.html", context)