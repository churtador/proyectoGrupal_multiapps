from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


      
class Usuario(models.Model):
   
    nombre = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    apellido = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    fecha_Nacimiento =  models.DateField()
    email = models.EmailField(max_length=254, unique=True )
    password = models.CharField(max_length=100)
    ACCESOS= (
        ('0', 'alumno'),
        ('1', 'profesor'),
        ('9', 'administrador'),
         )
    acceso = models.CharField(max_length=1, choices=ACCESOS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        ordering = ["nombre", "apellido"]
        
