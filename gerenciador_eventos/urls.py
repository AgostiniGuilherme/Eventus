from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('eventos/', views.eventos, name='eventos'),
    path('meus-eventos/', views.meus_eventos, name='meus_eventos'),
    path('meus-eventos/detalhes/<int:id>', views.evento_detalhes, name='evento_detalhes'),
]