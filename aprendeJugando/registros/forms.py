from django import forms
from django.db import models
from .models import Productos
from .models import ComentarioCliente
from .models import Administrador
from django.forms.models import fields_for_model
from django.forms import ModelForm, ClearableFileInput, widgets

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class ConsultaProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre','marca','categoria','subcategoria','color','precio','descripcion','cantidad','imagen']
        widgets = {
            'imagen': CustomClearableFileInput
        }
        
class ComentarioClienteForm(forms.ModelForm):
    class Meta:
        model = ComentarioCliente
        fields = ['cliente','asunto','mensaje']

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombre','apellidoPaterno', 'apellidoMaterno', 'usuario', 'correo', 'password']