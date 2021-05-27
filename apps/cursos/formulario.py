from django import forms
from django.core.exceptions import ValidationError
from .models import *
import apps.validaciones as validar
import apps.utilidades as util

   

class FormularioCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"
        widgets ={
            "nombre": forms.TextInput(
                attrs={
                    "placeholder":"ingresar nombre",
                    
                }
            ),
            "descripcion": forms.TextInput(
                attrs={
                    "placeholder":"ingrese Email",
                    "type":"E-mail"
                }
            ),
            "fecha": forms.DateInput(
                attrs={
                    "type":"Date"
                }
            ),
            "ubicacion": forms.TextInput(
                attrs={
                    "placeholder":"minimo 4 caracteres",
                    
                }
            ),
        }
    def clean_nombre(self):
        data = self.cleaned_data["nombre"]
        validar.longitud(data, campo="nombre")
        return data

    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"]
        validar.longitud(data, campo="descripcion")
        return data    

    def clean_fecha(self):
        data = self.cleaned_data["fecha"]
        validar.fechaEsFutura(data)
        return data    
    def clean_ubicacion(self):
        data = self.cleaned_data["ubicacion"]
        validar.longitud(data, campo="ubicacion")
        return data   
    
     
       

