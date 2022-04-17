from django.contrib import admin
from config.mixins import (
    AuditoriaAdmin,
    AuditoriaAdminTabularInline,
    AuditoriaAdminStackedInline, )
from .models import (
    Projeto,
    Financeiro,
    Responsavel,
    Acompanhamento,
)


class FinanceiroInline(AuditoriaAdminTabularInline):
    classes = ['collapse']
    model = Financeiro
    fields = (
        'ano',
        'valor',
    )


class AcompanhamentoInline(AuditoriaAdminTabularInline):
    classes = ['collapse']
    model = Acompanhamento
    fields = (
        'data',
        'descricao',
    )


@admin.register(Projeto)
class ProjetoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'nome',
        'detalhamento',
    )
    list_filter = (
        'secretaria',
        'tipo',
        'unidade',
        'data_aprovacao',
        'responsavel',
        'status',
    )
    list_display = (
        'secretaria',
        'nome',
        'tipo',
        'data_aprovacao',
        'status',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
        'status',
    )
    inlines = [
        FinanceiroInline,
        AcompanhamentoInline,
    ]


@admin.register(Responsavel)
class ResponsavelAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'nome',
    )
    list_display = (
        'nome',
        'telefone',
        'email',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + ()
