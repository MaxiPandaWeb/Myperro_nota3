from django.db import models
from django.contrib.auth.models import User

class Contacto(models.Model):
    email = models.EmailField()
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    telefono = models.IntegerField()
    region = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    tipo_vivienda = models.CharField(max_length=100)

    def __str__(self):
        return self.rut

class Nuevo(models.Model):
    rut_dueno = models.CharField(max_length=10)
    nom= models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='media')
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class UserProfileInfo(models.Model):

  user = models.OneToOneField(User,on_delete=models.CASCADE)
  rut = models.CharField(max_length=10,blank=True)
  comuna = models.CharField(max_length=100,blank=True)
  foto_perfil = models.ImageField(upload_to='media',blank=True)

def __str__(self):
  return self.user.username

# Create your models here.

