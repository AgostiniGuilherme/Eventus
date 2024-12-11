from django.contrib import admin
from .models import Evento, Participacao

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'local', 'data', 'organizador')
    search_fields = ('titulo', 'descricao', 'local')
    list_filter = ('data', 'local')
    date_hierarchy = 'data'

class ParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'evento', 'eh_organizador')
    search_fields = ('usuario__username', 'evento__titulo')
    raw_id_fields = ('usuario', 'evento')

admin.site.register(Evento, EventoAdmin)
admin.site.register(Participacao, ParticipacaoAdmin)
