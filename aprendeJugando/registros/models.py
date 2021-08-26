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

class Cliente(models.Model):  # Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.CharField(max_length=30, verbose_name="Nombre") 
    apellido_pat = models.CharField(max_length=20, verbose_name="Apellido Paterno")
    apellido_mat = models.CharField(max_length=20, verbose_name="Apellido Materno")
    fecha_nac = models.DateField (verbose_name="Fecha Nacimiento")
    usuario = models.CharField(max_length=20, verbose_name="Usuario") 
    email = models.EmailField(max_length=24, verbose_name="Correo Electrónico")
    password = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")  # Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado")
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["created"]
    def __str__(self):
        return self.usuario

class Productos(models.Model): #Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.CharField(max_length=30, verbose_name="Nombre Producto") 
    marca= models.CharField(max_length=20, verbose_name="Marca") 
    categoria= models.CharField(max_length=20, verbose_name="Categoria") 
    subcategoria = models.CharField(max_length=20, verbose_name="Subcategoria") 
    color = models.CharField(max_length=20, verbose_name="Color Producto") 
    precio = models.IntegerField(verbose_name="precio")
    descripcion = models.TextField(max_length=20, verbose_name="Descripcion Producto") 
    cantidad = models.DecimalField(max_digits=6, decimal_places=0,verbose_name="Cantidad")
    imagen = models.FileField(null=True, upload_to="fotos", blank=True,verbose_name="Fotografía Producto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")  # Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["created"]
    
    def __str__(self):
        return self.nombre

class ComentarioCliente(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    cliente = models.TextField(verbose_name="Cliente")
    asunto = models.TextField(verbose_name="Asunto")
    mensaje = models.TextField(verbose_name="Comentario")
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    class Meta:
        verbose_name = "Comentario Cliente"
        verbose_name_plural = "Comentarios Cliente"
        ordering = ["-created"]
    def __str__(self):
    
        return self.asunto

    def __str__(self):
    
        return self.mensaje
        #Indica que se mostrára el mensaje como valor en la tabla

class Administrador(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellidoPaterno=models.CharField(max_length=20, verbose_name="Apellido Paterno")
    apellidoMaterno=models.CharField(max_length=20, verbose_name="Apellido Materno")
    usuario = models.CharField(max_length=20, verbose_name="Usuario")
    correo=models.EmailField(verbose_name="Correo Electronico")
    password=models.CharField(max_length=8, verbose_name="Password")
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
   
    
    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        ordering = ["-created"]
    def __str__(self):
     return self.nombre
    #Indica que se mostrára el mensaje como valor en la tabla