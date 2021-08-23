from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
def registroProducto(request):
    return render(request, "registros/registroProducto.html")

def registroAdmin(request):
    return render(request, "registros/registroAdmin.html")

def registros(request):
    productos=Producto.objects.all()
    return render(request, "registros/consultarProductos.html", {'producto':productos})

def eliminarProducto(request, id,
    confirmacion='registros/confirmarEliminacion.html'):
    producto = get_object_or_404(Producto, id=id)
    if request.method=='POST':
        producto.delete()
        productos=Producto.objects.all()
        return render(request, "registros/consultarProductos.html", {'producto': productos})

    return render(request, confirmacion, {'object':producto})

def registrar(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            productos=Producto.objects.all()
            return render(request,'registros/consultarProductos.html', {'producto':productos})
    form = ProductoForm()
            #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/consultarProductos.html',{'form': form}) 

def consultaProductoIndividual(request, id):
    producto=Producto.objects.get(id=id)

    return render(request, "registros/formEditarProducto.html", {'producto':producto})

def editarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST, instance=producto)

    if form.is_valid():
            form.save() #si el registro ya existe, se modifica.
            productos=Producto.objects.all()
            return render(request,"registros/consultarProductos.html",{'productos':productos})

    return render(request,"registros/formEditarProducto.html",{'producto':producto})

 