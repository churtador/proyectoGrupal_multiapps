from django.shortcuts import render, HttpResponse, redirect
from apps.usuarios.formulario import * 

# Create your views here.
def index(request):
    context ={
           "formularioLogin":FormularioLogin(),
           "formularioRegistro":FormularioRegistro()
    }
    return render(request, "master/index.html", context)

def logout(request):
    if 'nombre' in request.session:
        del request.session['nombre']
    if 'id' in request.session:
        del request.session['id']
    if 'acceso' in request.session:
        del request.session['acceso']
    
    return redirect("/") 
    