from django.contrib import admin
from .models import Admin
from .models import Producto

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Register your models here.
admin.site.register(Admin,AdministrarModelo)
admin.site.register(Producto,AdministrarModelo)



