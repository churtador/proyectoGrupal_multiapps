from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


      
class Curso(models.Model):
   
    nombre = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    descripcion = models.CharField(max_length=250, validators=[MinLengthValidator(2)])
    fecha =  models.DateField()
    activo = models.BooleanField(default=1)
    ubicacion = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    capacidad = models.FloatField(default=10, validators=[
        MaxValueValidator(50),
        MinValueValidator(2)
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #inscripcionCurso
    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        ordering = ["fecha"]
# Create your models here.
    