from django.contrib import admin
from config.mixins import (
    AuditoriaAdmin, )
from .models import (
    ProjetoTipo,
    UnidadeTipo,
)


@admin.register(ProjetoTipo)
class ProjetoTipoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
        'nome',
    )
    list_display = (
        'codigo',
        'nome',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + ()


@admin.register(UnidadeTipo)
class UnidadeTipoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
        'nome',
    )
    list_display = (
        'codigo',
        'nome',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + ()
