"""aprendeJugando URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="Principal"),
    path('contacto/', views.contacto, name="Contacto"),
    path('formulario/', views.formulario, name="Formulario"),
    path('registro/', views.registro, name="Registro"),
    path('login/', views.login, name="Login"),
    path('adminJ/', views.adminJ, name="AdminJ"),
    path('registrarProducto/', views_registros.registroProducto, name="RegistrarP"),
    path('registrarAdmin/', views_registros.registroAdmin, name="RegistrarA"),
    path('consultarProductos',views_registros.registros, name="ConsultarP"),
    path('registrar/',views_registros.registrar,name="Registrar"),
    path('eliminarProducto/<int:id>/', views_registros.eliminarProducto, name='Eliminar'),
    path('formEditarProducto/<int:id>/', views_registros.consultaProductoIndividual,name='ConsultaIndividual'),
    path('editarProducto/<int:id>/', views_registros.editarProducto, name='Editar'),



]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
