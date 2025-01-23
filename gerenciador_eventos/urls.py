from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('eventos/', views.eventos, name='eventos'),
    path('meus-eventos/', views.meus_eventos, name='meus_eventos'),
    path('meus-eventos/detalhes/<int:id>', views.evento_detalhes, name='evento_detalhes'),
    path('auth/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
]