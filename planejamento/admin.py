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
    change_form_template = "projetos_change_form.html"
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

    def response_change(self, request, obj):
        from django.http import HttpResponseRedirect
        from .choices import STATUS_PROPOSTA, STATUS_PENDENTE, STATUS_NEGADO, STATUS_APROVADO

        if "_submeter" in request.POST:
            obj.status = STATUS_PROPOSTA
            obj.save()
            self.message_user(request, "Status atualizado com sucesso")
            return HttpResponseRedirect(".")

        elif "_pendente" in request.POST:
            obj.status = STATUS_PENDENTE
            obj.save()
            self.message_user(request, "Status atualizado com sucesso")
            return HttpResponseRedirect(".")

        elif "_negado" in request.POST:
            obj.status = STATUS_NEGADO
            obj.save()
            self.message_user(request, "Status atualizado com sucesso")
            return HttpResponseRedirect(".")

        elif "_aprovado" in request.POST:
            obj.status = STATUS_APROVADO
            obj.save()
            self.message_user(request, "Status atualizado com sucesso")
            return HttpResponseRedirect(".")

        return super().response_change(request, obj)


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
