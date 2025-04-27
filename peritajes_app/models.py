from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Rol(models.Model):
    codigo = models.CharField(max_length=10, unique=True, null=False , default='INS')
    nombre = models.CharField(max_length=50, unique=True, default="Instructor")
    
class Usuario(AbstractUser):
    telefono = models.CharField(max_length=10, blank=True, null=True)
    rol = models.ForeignKey('Rol', on_delete= models.PROTECT )
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
    def __str__(self):
        return self.username