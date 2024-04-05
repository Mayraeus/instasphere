from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length =15)
    nombre = models.CharField(max_length =50)
    apellidos = models.CharField(max_length =50)
    correo = models.EmailField()
    contrasena = models.TextField()

tipos = (
    ('image', 'Imagen'),
    ('video', 'Video'),
)

class Publicacion(models.Model):
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    id_usuario = models.IntegerField(null =False)
    tipo = models.CharField(max_length =10, choices =tipos)
    post = models.ImageField(upload_to = 'upload/', null=True, blank=True)


class Comentario(models.Model):
    fecha = models.DateTimeField()
    contenido = models.TextField()
    id_publicacion = models.IntegerField()
    id_usuario_comentario = models.IntegerField()


estatus = (
    ('enviado', 'Enviado'),
    ('recibido', 'Recibido'),
    ('leido', 'Leído'),
)   

class Conversacion(models.Model):
    fecha = models.DateTimeField()
    contenido = models.TextField()
    estatus= models.CharField(max_length =10, choices =estatus)
    id_usuario_orig = models.IntegerField()
    id_usuario_dest = models.IntegerField()
    
