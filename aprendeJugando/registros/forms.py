from django import forms
from django.db import models
from .models import Producto
from django.forms.models import fields_for_model
from django.forms import ModelForm, ClearableFileInput, widgets

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca','categoria','subcategoria','color','precio','descripcion','cantidad']
        
        