from __future__ import unicode_literals
from django.db import models
from apps.cursos.models import *
from apps.usuarios.models import *


class Inscripcion(models.Model):
    participante = models.ForeignKey(Usuario, related_name="inscripcionUsuario", on_delete=models.CASCADE, blank=True, 
        null=True, 
        default=None)
    taller = models.ForeignKey(Curso, related_name="inscripcionCurso", on_delete=models.CASCADE, blank=True, 
        null=True, 
        default=None)
    confirmado = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
      

 #   def __str__(self):
 #       return f"{self.alias} acceso: {self.acceso}"

    class Meta:
        unique_together = (("participante", "taller"),)
        