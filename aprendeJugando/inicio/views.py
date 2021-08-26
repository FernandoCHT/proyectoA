from django.shortcuts import render, HttpResponse
from registros.models import Productos


# Create your views here.

def principal(request):
    contenido="<h1>Hola mundo</h1>"
    return HttpResponse(contenido)

def contacto(request):
    contenido=""""""
    return render(request, "inicio/contacto.html")

def formulario(request):
    return render(request, "inicio/formulario.html")

def principal(request):
    productos=Productos.objects.all()
    return render(request, "inicio/principal.html", {'productos':productos})

def registro(request):
    return render(request, "inicio/registro.html")

def login(request):
    return render(request, "inicio/login.html")

def adminJ(request):
    return render(request, "inicio/adminJ.html")

def terminos(request):
    return render(request, "inicio/terminos.html")

def aviso(request):
    return render(request, "inicio/aviso.html")



