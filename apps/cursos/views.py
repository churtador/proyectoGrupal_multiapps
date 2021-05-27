
from django.http import response
from django.shortcuts import render, HttpResponse, redirect
from .formulario import *
from django.db.models import Count
from .models import *
from apps.inscripciones.models import *
from django.core.files.storage import FileSystemStorage, default_storage
from django.conf import settings

from os.path import isfile, join
from django.contrib.staticfiles.templatetags.staticfiles import static
from apps.usuarios.models import Usuario
import os


def index(request):
    return HttpResponse("bienvenido a cursos")

def crear(request):
    if request.session["acceso"] == '9':
        if request.method == "POST":
            formulario = FormularioCurso(request.POST)
            if formulario.is_valid():
                formulario.save() 
                print("cursocreado")
                context={
                "cursosTotales": Curso.objects.all(),
                "formularioCurso": FormularioCurso(),
            }
                return render(request, "cursos/crearCurso.html", context)
            else:
                context={
                    "formularioCurso": formulario,
                    "cursosTotales": Curso.objects.all()
                }
                return render(request, "cursos/crearCurso.html", context)
        else:
            context={
                "formularioCurso": FormularioCurso(),
                "cursosTotales": Curso.objects.all()
            }
            return render(request, "cursos/crearCurso.html", context)
    return HttpResponse("<p>sin atribuciones por nivel de acceso!</p><br><a  href='../../usuarios/discriminador/'>volver</a>")

"<p>profesor creado!</p><br><a  href='../../cursos/crear/'>volver</a>"

def mostrar(request):
    inscritosEnCurso=Curso.objects.annotate(contador=Count("inscripcionCurso__id")).filter(activo=1).exclude(inscripcionCurso__participante__id=request.session["id"]).order_by("fecha")
    context={
        "misCursos":Inscripcion.objects.filter(participante__id=request.session["id"]),
        "cursosActivosTotales":inscritosEnCurso
    }
    return render(request, "cursos/mostrar.html", context)

def adminCurso(request):
    inscritosEnCurso=Curso.objects.annotate(contador=Count("inscripcionCurso__id"))
    context={
        "cursosActivosTotales":inscritosEnCurso
    }
    return render(request, "cursos/adminCurso.html", context)

def eliminarCurso(request, idCurso):
    esteCurso=Curso.objects.get(id=idCurso)
   
    
    esteCurso.activo = 0
    esteCurso.save()
    return redirect("../adminCurso/")


def descripcionCurso(request, idCurso):
    print('*'*20)
    print('Descripcion Curso')

    thisUser = Usuario.objects.get(id = request.session["id"])

    access = int(thisUser.acceso)
    print(type(access))

    path = getattr(settings, "MEDIA_ROOT", None)
    path += "/"+str(idCurso)+"/"
    print(path)

    allFiles=[]
    filesPath = os.path.join(path)
    if os.path.exists(filesPath):
        with os.scandir(path) as files:
            for f in files:
                try:
                    nameIndex = 0
                    allFiles.append({
                            "url": f.name,
                            "name": f.name[nameIndex:]
                        }
                    )
                except:
                    pass
                        

    esteCurso=Curso.objects.get(id=idCurso)
    context={
        "curso": esteCurso,
        "files": allFiles,
        "path": path,
        "access": access
    }
    return render(request, "cursos/mostrarCurso.html", context)

def uploadFile(request, idCurso):
    # admin = Usuario.objects.get()
    if request.method == "POST":
        cursoId = idCurso
        cursoId = str(cursoId)
        archivoCargado = request.FILES["archivo"]
        fileSS = FileSystemStorage("media/" + cursoId)
        fileSS.save(archivoCargado.name, archivoCargado)

    return redirect('descripcionCurso', idCurso)

def download(request, idCurso, fileName):
    path = getattr(settings, "MEDIA_ROOT", None)
    path += "/"+str(idCurso)+"/"
    print(path)
    filePath = path+fileName
    if os.path.exists(filePath):
        with open(filePath, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/foce_download")
            return response
    return redirect('descripcionCurso', idCurso)