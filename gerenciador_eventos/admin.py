from django.contrib import admin
from .models import Evento, Participacao

# Registra o modelo Evento
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'local', 'data', 'organizador')  # O que vai ser exibido na lista de eventos
    search_fields = ('titulo', 'descricao', 'local')  # Campos em que será possível realizar buscas
    list_filter = ('data', 'local')  # Filtros que podem ser aplicados
    date_hierarchy = 'data'  # Permite filtrar por data de forma hierárquica


# Registra o modelo Participacao
class ParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'evento', 'eh_organizador', 'confirmado')  # O que será exibido na lista de participações
    search_fields = ('usuario__username', 'evento__titulo')  # Possibilita buscas pelo nome do usuário e evento
    list_filter = ('eh_organizador', 'confirmado')  # Filtros para organizador e confirmação
    raw_id_fields = ('usuario', 'evento')  # Usar ID direto para campos de relacionamento

# Registra os modelos no painel administrativo
admin.site.register(Evento, EventoAdmin)
admin.site.register(Participacao, ParticipacaoAdmin)
