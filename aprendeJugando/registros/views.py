from django.shortcuts import render
from .models import Productos
from .forms import ConsultaProductoForm
from .forms import ComentarioClienteForm
from .forms import AdministradorForm
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
def registroProducto(request):
    return render(request, "registros/registroProducto.html")

def registroAdmin(request):
    return render(request, "registros/registroAdmin.html")

def registros(request):
    productos=Productos.objects.all()
    return render(request, "registros/consultarProductos.html", {'productos':productos})

def eliminarProducto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    producto = get_object_or_404(Productos, id=id)
    if request.method == 'POST':
        producto.delete()
        producto = Productos.objects.all()
        return render(request, "registros/consultarProductos.html", {'productos': producto})

    return render(request, confirmacion, {'object': producto})

def registrar(request):
    if request.method == 'POST':
        form = ConsultaProductoForm(request.POST, request.FILES)
        if form.is_valid():
            productos = Productos.objects.all()
            nombre  = request.POST['nombre']
            marca = request.POST['marca']
            categoria = request.POST['categoria']
            subcategoria = request.POST['subcategoria']
            color = request.POST['color']
            precio = request.POST['precio']
            descripcion = request.POST['descripcion']
            cantidad= request.POST['cantidad']
            imagen = request.FILES['imagen']
            insert = Productos(nombre=nombre,marca=marca,categoria=categoria,subcategoria=subcategoria,color=color,precio=precio,descripcion=descripcion,cantidad=cantidad,imagen=imagen)
            insert.save()
            return render(request, "registros/consultarProductos.html", {'productos': productos})
        else:
            messages.error(request, "Error al procesar el formulario")
    form = ConsultaProductoForm()
    return render(request, 'registros/consultarProductos.html', {'form': form})

def consultarProductoIndividual(request, id):
    producto = Productos.objects.get(id=id)

    return render(request, "registros/formEditarProducto.html", {'producto': producto})

def editarProducto(request, id):
    producto = get_object_or_404(Productos, id=id)
    form = ConsultaProductoForm(request.POST, request.FILES, instance=producto)
    if form.is_valid():
        form.save()  # si el registro ya existe, se modifica.
        productos = Productos.objects.all()
        return render(request, "registros/consultarProductos.html", {'productos': productos})

    messages.error(request, "Error al procesar el formulario")
    return render(request, "registros/formEditarProducto.html", {'producto': producto})

def registrarComentario(request):
    if request.method == 'POST':
        form = ComentarioClienteForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'inicio/principal.html')
        form = ComentarioClienteForm()
        #Si algo sale mal se reenvian al formulario los datos ingresados
        return render(request,'inicio/principal.html',{'form': form})

def registrarAdministrador(request):
    if request.method == 'POST':
        form = AdministradorForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'registros/registroAdmin.html')
            form = AdministradorForm()
            #Si algo sale mal se reenvian al formulario los datos ingresados
            return render(request,'registros/registroAdmin.html',{'form': form})