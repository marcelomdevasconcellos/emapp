from django.contrib import admin
from datetime import datetime, timedelta
from config.mixins import (
    AuditoriaAdmin,
    AuditoriaAdminTabularInline,
    AuditoriaAdminStackedInline, )
from .models import (
    Projeto,
    Financeiro,
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



class AcompanhamentoFilter(admin.SimpleListFilter):

    title = 'Acompanhamento'
    parameter_name = 'acompanhamento'

    def lookups(self, request, model_admin):
        return (('atualizado', 'Atualizado'), ('atrasado', 'Atrasado'), )

    def queryset(self, request, queryset):
        if self.value() and self.value() == 'atualizado':
            data = datetime.now() - timedelta(days=30)
            return queryset.filter(data_ultimo_acompanhamento__gte=data)
        elif self.value() and self.value() == 'atrasado':
            data = datetime.now() - timedelta(days=30)
            return queryset.filter(data_ultimo_acompanhamento__lte=data)
        

@admin.register(Projeto)
class ProjetoAdmin(AuditoriaAdmin):
    change_form_template = "projetos_change_form.html"

    def acompanhamento(self, obj):
        return obj.acompanhamento()

    acompanhamento.short_description = 'Acompanhamento'
    acompanhamento.admin_order_field = 'data_ultimo_acompanhamento'

    actions = []
    search_fields = (
        'nome',
        'detalhamento',
    )
    list_filter = (
        AcompanhamentoFilter,
        'secretaria',
        'tipo',
        'unidade',
        'data_aprovacao',
        'responsavel',
        'status',
    )
    list_display = (
        'nome',
        'secretaria',
        'tipo',
        'data_aprovacao',
        'acompanhamento',
        'status',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
        'status',
        'data_aprovacao',
        'data_ultimo_acompanhamento',
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
            obj.data_aprovacao = datetime.now()
            obj.save()
            self.message_user(request, "Status atualizado com sucesso")
            return HttpResponseRedirect(".")

        return super().response_change(request, obj)
