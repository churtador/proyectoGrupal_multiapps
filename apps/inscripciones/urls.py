from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inscripciones"),
    path("crear/", views.crear, name="inscribirse"),
    path("mostrar/", views.mostrar, name="mostrar"),
    path("miCalendario/", views.miCalendario, name="miCalendario"),
    path("misCursos/", views.misCursos, name="misCursos"),
    path("inscribirAlumno/<int:idCurso>", views.inscribirAlumno, name="inscribirAlumno"),
    path("eliminarInscripcion/<int:idInscripcion>", views.eliminarInscripcion, name="eliminarInscripcion"),
]
