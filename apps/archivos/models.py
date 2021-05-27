from __future__ import unicode_literals
from django.db import models
from apps.cursos.models import *
from apps.usuarios.models import *

class Archivo(models.Model):
    nombre = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    curso_name = models.ForeignKey(Curso, related_name="archivosCurso", on_delete=models.CASCADE, null=False, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
      

 #   def __str__(self):
 #       return f"{self.alias} acceso: {self.acceso}"

