from django.contrib import admin

from config.mixins import (
    AuditoriaAdmin,
    AuditoriaAdminTabularInline,
    AuditoriaAdminStackedInline, )
# Register your models here.

from .models import (
    Secretaria,
    Orgao,
    CorpoTecnico,
)


class OrgaoInline(AuditoriaAdminTabularInline):
    classes = ['collapse']
    model = Orgao

@admin.register(Secretaria)
class SecretariaAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
        'nome',
    )
    list_display = (
        'codigo',
        'nome',
        'data_criacao',
        'data_extincao',
    )
    inlines = [
        OrgaoInline,
    ]
    readonly_fields = AuditoriaAdmin.readonly_fields + ()



class CorpoTecnicoInline(AuditoriaAdminTabularInline):
    classes = ['collapse']
    model = CorpoTecnico


@admin.register(Orgao)
class OrgaoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo',
        'nome',
    )
    list_filter = (
        'secretaria',
    )
    list_display = (
        'secretaria',
        'codigo',
        'nome',
        'data_criacao',
        'data_extincao',
    )
    inlines = [
        CorpoTecnicoInline,
    ]
    readonly_fields = AuditoriaAdmin.readonly_fields + ()
