from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('salvar_presente/', views.salvar_presente, name='salvar_presente'),
    path('presentes_escolhidos/', views.presentes_escolhidos, name='presentes_escolhidos'),
    path('confirmar_presenca/', views.confirmar_presenca, name='confirmar_presenca'),
]
