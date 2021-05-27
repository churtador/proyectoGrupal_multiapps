from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="cursos"),
    path("crear/", views.crear, name="crearCurso"),
    path("mostrar/", views.mostrar, name="mostrarCurso"),
    path("adminCurso/", views.adminCurso, name="adminCurso"),
    path("mostrar/<int:idCurso>", views.descripcionCurso, name="descripcionCurso"),
    path("mostrar/uploadFile/<int:idCurso>", views.uploadFile, name="uploadFile"),
    path("mostrar/<int:idCurso>/download/<str:fileName>", views.download, name="download"),
    path("eliminarCurso/<int:idCurso>", views.eliminarCurso, name="eliminarCurso"),

]
