from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('meus-eventos/', views.meus_eventos, name='meus_eventos'),
    path('auth/cadastrar/', views.cadastrar, name='cadastrar'),
    path('auth/login/', views.logar, name='login'),
    path('auth/logout/', views.custom_logout, name='custom_logout'),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/criar/', views.criar_evento, name='criar_evento'),
    path('eventos/<int:id>/', views.detalhar_evento, name='detalhar_evento'),
    path('eventos/<int:id>/editar/', views.editar_evento, name='editar_evento'),
    path('eventos/<int:id>/deletar/', views.deletar_evento, name='deletar_evento'),
    path('evento/<int:id>/inscrever/', views.inscricao_em_evento, name='inscricao_em_evento'),
    path('evento/<int:id>/cancelar-inscricao/', views.cancelar_inscricao, name='cancelar_inscricao'),
    path('evento/<int:evento_id>/remover_participante/<int:usuario_id>/', views.remover_participante, name='remover_participante'),
]