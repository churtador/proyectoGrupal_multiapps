from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="usuarios"),
    path("crear/", views.crear, name="crear"),
    path("login/", views.login, name="login"),
    path("discriminador/", views.discriminador, name="discriminador"),
    path("registrarProfesor/", views.registrarProfesor, name="registrarProfesor"),
]