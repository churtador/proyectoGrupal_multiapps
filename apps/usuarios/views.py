from django.shortcuts import render, HttpResponse, redirect
from .formulario import *
from .models import *
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import relativedelta
from time import strftime
from apps.cursos.models import *
from apps.inscripciones.models import *
import apps.utilidades as util
import calendar

def index(request):
    return HttpResponse("hola usuarios")

def crear(request):
    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            newForm = formulario.save(commit=False)
            print(formulario.cleaned_data["password"])
            newForm.password = util.encriptar(formulario.cleaned_data["password"])
            newForm.acceso = 0
            newForm.save()
            request.session["id"]=newForm.id
            request.session["nombre"]=newForm.nombre
            request.session["acceso"]=str(newForm.acceso)
            print(request.session["id"])
            print(request.session["acceso"])
            
            
            return redirect("../discriminador/")
        else:
            
            context={
                "formularioRegistro": formulario,
                "formularioLogin":FormularioLogin()
            }
            return render(request, "master/index.html", context)
    else:
        context={
            "formularioRegistro": FormularioRegistro(),
            "formularioLogin":FormularioLogin()
        }
        return render(request, "master/index.html", context)
    
def login(request):
    if request.method == "POST":
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid(): 
            newForm = formulario.save(commit=False)  
            
            esteUsuario=Usuario.objects.filter(email=newForm.email).first()
            request.session["id"] = esteUsuario.id
            request.session["nombre"] = esteUsuario.nombre  
            request.session["acceso"] = esteUsuario.acceso
            
            return redirect("../discriminador/")
        else:
            context={
                "formularioRegistro": FormularioRegistro(),
                "formularioLogin": formulario,
                
            }
            return render(request, "master/index.html", context)
    else:
        context={
            "formularioRegistro": FormularioRegistro(),
            "formularioLogin": FormularioLogin(),
        }
        return render(request, "master/index.html", context)

def discriminador(request):
    if request.session["acceso"] == "0":
        return render(request, "usuarios/indexAlumno.html")
    if request.session["acceso"] == "1":
        return render(request, "usuarios/indexProfesor.html")
    if request.session["acceso"] == "9":
        return render(request, "usuarios/indexAdmin.html")
    return HttpResponse("<p>no tiene acceso!</p><br><a  href='{% url 'index' %}'>volver</a>")

def registrarProfesor(request):
    if request.method == "POST":
        formulario = FormularioRegistroProfesor(request.POST)
        if formulario.is_valid():
            newForm = formulario.save(commit=False)
            newForm.password = util.encriptar(formulario.cleaned_data["password"])
            newForm.acceso = 1 #profesor
            newForm.save()
            return HttpResponse("<p>profesor creado!</p><br><a  href='../../cursos/crear/'>volver</a>") 
        else:
            context={
                "formularioRegistroProfesor": formulario,
            }
            return render(request, "usuarios/registrarProfesor.html", context)
    else:
        context={
            "formularioRegistroProfesor": FormularioRegistroProfesor()
        }
        return render(request, "usuarios/registrarProfesor.html", context)
      
      

# Create your views here.
