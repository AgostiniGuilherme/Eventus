from django.db import models
from django.contrib.auth.models import User

# Modelo de Evento
class Evento(models.Model):
  titulo = models.CharField(max_length=100)  # Nome do evento
  descricao = models.TextField()  # Descrição do evento
  local = models.CharField(max_length=255)  # Localização do evento
  data = models.DateTimeField()  # Data e hora do evento
  organizador = models.ForeignKey(User, related_name='eventos_criados', on_delete=models.CASCADE)  # O organizador do evento (relacionamento com User)

  def __str__(self):
    return self.titulo

# Modelo de Participação (relaciona usuários com eventos e define o organizador)
class Participacao(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionamento com o usuário
  evento = models.ForeignKey(Evento, related_name='participantes', on_delete=models.CASCADE)  # Relacionamento com o evento
  eh_organizador = models.BooleanField(default=False)  # Define se o usuário é o organizador do evento
  confirmado = models.BooleanField(default=False)  # Indica se o participante confirmou presença

  def __str__(self):
    return f'{self.usuario.username} - {self.evento.titulo}'

class Meta:
  verbose_name_plural = "Participações"  # Corrige o nome plural para "Participações"
