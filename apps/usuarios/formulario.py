from django import forms
from django.core.exceptions import ValidationError
from .models import *
import apps.validaciones as validar
import apps.utilidades as util



class FormularioRegistro(forms.ModelForm):
    confirm = forms.CharField(max_length=100, label="confirmar password",)
    confirm.widget = forms.TextInput(
        attrs={
            "placeholder":"confirmar Password",
                    "class":" table-success",
                    "type":"password",

        }
    )
    class Meta:
        model = Usuario
        fields = ["nombre", "apellido", "fecha_Nacimiento", "email", "password"]  
        widgets ={
            "nombre": forms.TextInput(
                attrs={
                    "placeholder":"ingresar nombre",
                    "class":" w-3/5 table-success",
                }
            ),
            "apellido": forms.TextInput(
                attrs={
                    "placeholder":"ingresar apellido",
                    "class":" w-3/5 table-success",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "placeholder":"ingrese Email",
                    "class":" table-success",
                    "type":"E-mail"
                }
            ),
            "fecha_Nacimiento": forms.DateInput(
                attrs={
                    "type":"Date",
                    "class":" table-success",
                }
            ),
            "password": forms.TextInput(
                attrs={
                    "type":"password",
                    "placeholder":"minimo 4 caracteres",
                    "class":" table-success",
                }
            ),
        }
    def clean_nombre(self):
        data = self.cleaned_data["nombre"]
        validar.longitud(data, campo="nombre")
        return data

    def clean_apellido(self):
        data = self.cleaned_data["apellido"]
        validar.longitud(data, campo="apellido")
        return data
     
    def clean_email(self):
        data = self.cleaned_data["email"]
        validar.validarEmail(data)
        validar.existeRepetido(data)
        validar.longitud(data, campo="email")
        return data
    def clean_fecha_Nacimiento(self):
        data = self.cleaned_data["fecha_Nacimiento"]
        validar.mayorDe18(str(data))
        return data
    def clean(self):
        password = self.cleaned_data["password"]
        confirmPass = self.cleaned_data["confirm"]
        if password != confirmPass:
            raise ValidationError({"password": "las contraseñas no son iguales"})     
       



class FormularioLogin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["email", "password"]  
        widgets ={
            "email": forms.TextInput(
                attrs={
                    "placeholder":"ingrese Email",
                    "class":"form-control me-2",
                    "type":"text"
                }
            ),
             "password": forms.PasswordInput(
                attrs={
                    "placeholder":"password",
                    "class":"form-control me-2"
                }
            )
        }
        labels = {
            "email":"Login",
            "password":""
        }

    def clean(self):
        data = self.cleaned_data["email"]
        if validar.validacionEmail(data) == False:
           raise ValidationError({"email" : "error en el formato del email"}) 
        if validar.ValidarExisteEmail(data) == False:
            raise ValidationError({"email" : "no existe mail"}) 
        confirmPass = self.cleaned_data["password"]
        esteUsuario=Usuario.objects.filter(email=data).first()
        if not util.verificarPassword(confirmPass, esteUsuario.password):
           raise ValidationError({"password" : "la contraseña con corresponde"})
        
class FormularioRegistroProfesor(forms.ModelForm):
    confirm = forms.CharField(max_length=100, label="confirmar password",)
    confirm.widget = forms.TextInput(
        attrs={
            "placeholder":"confirmar Password",
                    "class":"ingresoDatos",
                    "type":"password",

        }
    )
    class Meta:
        model = Usuario
        fields = ["nombre", "apellido", "fecha_Nacimiento", "email", "password"]  
        widgets ={
            "nombre": forms.TextInput(
                attrs={
                    "placeholder":"ingresar nombre",
                    "class":"ingresoDatos"
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "placeholder":"ingrese Email",
                    "class":"ingresoDatos",
                    "type":"E-mail"
                }
            ),
            "fecha_Nacimiento": forms.DateInput(
                attrs={
                    "type":"Date"
                }
            ),
            "password": forms.TextInput(
                attrs={
                    "type":"password",
                    "placeholder":"minimo 4 caracteres",
                    "class":"ingresoDatos"
                }
            ),
        }
    def clean_nombre(self):
        data = self.cleaned_data["nombre"]
        validar.longitud(data, campo="nombre")
        return data

    def clean_apellido(self):
        data = self.cleaned_data["apellido"]
        validar.longitud(data, campo="apellido")
        return data
     
    def clean_email(self):
        data = self.cleaned_data["email"]
        validar.validarEmail(data)
        validar.existeRepetido(data)
        validar.longitud(data, campo="email")
        return data
    def clean_fecha_Nacimiento(self):
        data = self.cleaned_data["fecha_Nacimiento"]
        validar.mayorDe18(str(data))
        return data
    def clean(self):
        password = self.cleaned_data["password"]
        confirmPass = self.cleaned_data["confirm"]
        if password != confirmPass:
            raise ValidationError({"password": "las contraseñas no son iguales"})     
       
