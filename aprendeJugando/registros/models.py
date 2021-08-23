from django.db import models

# Create your models here.
class UserManager(models.Manager):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Hombre'), (GENDER_FEMALE, 'Mujer')]
    def males(self):
        return self.all().filter(gender=self.GENDER_MALE)
    def females(self):
        return self.all().filter(gender=self.GENDER_FEMALE)

class Admin(models.Model):  # Define la estructura de nuestra tabla

    nombre = models.CharField(max_length=30, verbose_name="Nombre") 
    apellido_pat = models.CharField(max_length=20, verbose_name="Apellido Paterno")
    apellido_mat = models.CharField(max_length=20, verbose_name="Apellido Materno")
    genero = models.IntegerField(choices=UserManager.GENDER_CHOICES,verbose_name="Genero")
    fecha_nac = models.DateField ( verbose_name="Fecha Nacimiento")
    usuario = models.CharField(max_length=20, verbose_name="Usuario") 
    email = models.EmailField(max_length=24, verbose_name="Correo Electrónico")
    password = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")  # Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado")
    
    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        ordering = ["created"]
    def __str__(self):
        return self.usuario

class Producto(models.Model):  # Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.CharField(max_length=30, verbose_name="Nombre Producto") 
    marca= models.CharField(max_length=20, verbose_name="Marca") 
    categoria= models.CharField(max_length=20, verbose_name="Categoria") 
    subcategoria = models.CharField(max_length=20, verbose_name="Subcategoria") 
    color = models.CharField(max_length=20, verbose_name="Color Producto") 
    precio = models.DecimalField(max_digits=6, decimal_places=0,verbose_name="Precio")
    descripcion = models.TextField(max_length=20, verbose_name="Descripcion Producto") 
    cantidad = models.DecimalField(max_digits=6, decimal_places=0,verbose_name="Cantidad")
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")  # Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["created"]
    def __str__(self):
        return self.nombre
