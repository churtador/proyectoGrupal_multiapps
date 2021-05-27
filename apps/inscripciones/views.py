from django.shortcuts import render, HttpResponse, redirect
from .formulario import *
from .models import *
from apps.usuarios.models import *
from apps.cursos.models import *
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import relativedelta
from time import strftime

def index(request):
    return HttpResponse("inscripciones")

def crear(request):
    if request.method == "POST":
        formulario = FormularioInscripcion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("../../cursos/crear/")
        else:
            context={
                "formularioInscripcion":formulario
            }
            return render(request, "inscripciones/inscribir.html", context)
    else:
        context={
            "formularioInscripcion": FormularioInscripcion(),
        }
        return render(request, "inscripciones/inscribir.html", context)

def inscribirAlumno(request, idCurso):
    esteCurso=Curso.objects.filter(id=idCurso).first()
    esteAlumno=Usuario.objects.filter(id=request.session["id"]).first()
    existeInscripcion = Inscripcion.objects.filter(participante=esteAlumno).filter(taller=esteCurso)
    print(len(existeInscripcion))
    if len(existeInscripcion)>0:
        return redirect("../../cursos/mostrar/")
    estaInscripcion=Inscripcion.objects.create(
        participante = esteAlumno,
        taller = esteCurso)
    return redirect("../../cursos/mostrar/")

def miCalendario(request):
#################
    misCursos=Curso.objects.filter(inscripcionCurso__participante__id=request.session["id"])
    fecha_hoy = datetime.strptime(strftime("%Y-%m-%d"), '%Y-%m-%d')
    diadelasemana=strftime("%w")
    esteLunes=date.today() - timedelta(days=int(diadelasemana)-1)
    esteMartes= esteLunes + timedelta(days=1)
    esteMiercoles= esteLunes + timedelta(days=2)
    esteJueves=esteLunes + timedelta(days=3)
    esteViernes=esteLunes + timedelta(days=4)
    esteSabado=esteLunes + timedelta(days=5)
    lunes=Inscripcion.objects.filter(taller__fecha=esteLunes)
    martes=Inscripcion.objects.filter(taller__fecha=esteMartes)
    miercoles=Inscripcion.objects.filter(taller__fecha=esteMiercoles)
    jueves=Inscripcion.objects.filter(taller__fecha=esteJueves)
    viernes=Inscripcion.objects.filter(taller__fecha=esteViernes)
    print(esteViernes)
    print(viernes)
    context={
            "esteViernes":esteViernes,
            "lunes":lunes,
            "martes":martes,
            "miercoles":miercoles,
            "jueves":jueves,
            "viernes":viernes,
            "fecha_hoy":fecha_hoy,
    }
    return render(request, "inscripciones/miCalendario.html", context)
    
def mostrar(request):
    context={
        "inscripcionesTotales":Inscripcion.objects.filter(confirmado=1)
    }
    return render(request, "inscripciones/mostrar.html", context)

def misCursos(request):
    
    context={
        "misCursos":Inscripcion.objects.filter(participante__id=request.session["id"])
    }
    return render(request, "inscripciones/misCursos.html", context)

def eliminarInscripcion(request, idInscripcion):
    estaInscripcion=Inscripcion.objects.get(id=idInscripcion)
    estaInscripcion.delete()
    #estaInscripcion.confirmado = 0
    #estaInscripcion.save()
    return redirect("../mostrar/")
 


    pass
# Create your views here.
