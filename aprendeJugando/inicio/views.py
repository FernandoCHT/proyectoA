from django.shortcuts import render, HttpResponse

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
    return render(request, "inicio/principal.html")

def registro(request):
    return render(request, "inicio/registro.html")

def login(request):
    return render(request, "inicio/login.html")

def adminJ(request):
    return render(request, "inicio/adminJ.html")
