from django.contrib import admin
from .models import Cliente
from .models import Productos
from .models import ComentarioCliente
from .models import Administrador

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Register your models here.

admin.site.register(Productos,AdministrarModelo)

class AdministrarComentariosCliente(admin.ModelAdmin):
    list_display = ('id', 'asunto')
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    
admin.site.register(ComentarioCliente, AdministrarComentariosCliente)

class AdministrarAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_display = ('id', 'apellidoPaterno')
    list_display = ('id', 'apellidoMaterno')
    list_display = ('id', 'usuario')
    list_display = ('id', 'correo')
    list_display = ('id', 'password')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    
    
admin.site.register(Administrador, AdministrarAdmin)

class AdministrarCliente(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_display = ('id', 'apellido_pat')
    list_display = ('id', 'apellido_mat')
    list_display = ('id', 'fecha_nac')
    list_display = ('id', 'usuario')
    list_display = ('id', 'email')
    list_display = ('id', 'password')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    
    
admin.site.register(Cliente, AdministrarCliente)  


 
