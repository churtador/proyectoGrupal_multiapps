from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from time import strftime
from django import forms
from apps.usuarios.models import *
import re
 
def longitud(cadena, minLength = 2, maxLength = 40, campo=""):
    if len(cadena) < minLength or len(cadena) > maxLength:
        if campo:
            message = f"El largo de {campo} debe ser entre {minLength} y {maxLength} caracteres."
        else:
            message = f"El largo es entre {minLength} y {maxLength} caracteres."
        raise ValidationError(message)

def validarEmail(email):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(email):
                raise ValidationError(
                    [
                        {"email": "revisar el formato del mail"}
                    ]
                )
def existeEmail(email):
    usuarios = Usuario.objects.filter(email=email)
    if len(Usuario.objects.filter(email=email))<1:
            
        raise ValidationError(
            [
                {"email": "Email no existe"}
            ])
def mayorDe18(fecha_Nacimiento):
    fecha_limite = datetime.now() + relativedelta(years=-18)
    fecNac = datetime.strptime(fecha_Nacimiento, '%Y-%m-%d')
    fecha_hoy = datetime.strptime(strftime("%Y-%m-%d"), '%Y-%m-%d')
    if fecha_limite < fecNac or fecNac > fecha_hoy:
        raise ValidationError(
            [
                {"fecha_Nacimiento": "El usuario debe ser mayor a 18 años"}
            ])
def fechaEsFutura(fecha):
    hoy = datetime.strptime(strftime("%Y-%m-%d"), '%Y-%m-%d')
    fechaAValidar = datetime.strptime(str(fecha), '%Y-%m-%d')
    if fechaAValidar <= hoy:
                raise ValidationError(
            [
                {"fecha": "la fecha debe estar en el futuro"}
            ])
def existeRepetido(email):
    usuarios = Usuario.objects.filter(email=email)
    if len(Usuario.objects.filter(email=email))>0:
        raise ValidationError(
            [
                {"email": "este Email ya existe en los registros, por favor intente logearse"}
            ])

def validacionEmail(email):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(email):
        return False

def ValidarExisteEmail(email):
    usuarios = Usuario.objects.filter(email=email)
    if len(Usuario.objects.filter(email=email))<1:
       return False    
       