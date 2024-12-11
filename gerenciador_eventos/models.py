from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.TextField()
  local = models.CharField(max_length=255)
  data = models.DateTimeField()
  organizador = models.ForeignKey(User, related_name='eventos_criados', on_delete=models.CASCADE)

  def __str__(self):
    return self.titulo

class Participacao(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  evento = models.ForeignKey(Evento, related_name='participantes', on_delete=models.CASCADE)
  eh_organizador = models.BooleanField(default=False)

  def __str__(self):
    return f'{self.usuario.username} - {self.evento.titulo}'

class Meta:
  verbose_name_plural = "Participações"  # Corrige o nome plural para "Participações"
