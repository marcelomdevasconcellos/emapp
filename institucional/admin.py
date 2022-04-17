from django.contrib import admin

from config.mixins import (
    AuditoriaAdmin,
    AuditoriaAdminTabularInline,
    AuditoriaAdminStackedInline, )
# Register your models here.

from .models import (
    Secretaria,
    Orgao,
)

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
    readonly_fields = AuditoriaAdmin.readonly_fields + ()


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
    readonly_fields = AuditoriaAdmin.readonly_fields + ()
