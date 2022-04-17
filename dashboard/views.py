from django.shortcuts import render
import locale
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
import json
from planejamento.models import Projeto, Financeiro
from institucional.models import Secretaria
from planejamento.choices import (
    STATUS_CADASTRADO,
    STATUS_NEGADO,
    STATUS_APROVADO,
    STATUS_PENDENTE,
    STATUS_PROPOSTA,
)
from django.utils.numberformat import format


def cards(request):
    projetos_aprovados = Projeto.objects.filter(status=STATUS_APROVADO).all()
    context = {
        'propostas_cadastradas': len(Projeto.objects.filter(status=STATUS_PROPOSTA).all()),
        'projetos_aprovados': len(Projeto.objects.filter(status=STATUS_APROVADO).all()),
        'projetos_paralisados': len(Projeto.objects.filter(status=STATUS_PENDENTE).all()),
    }
    years = [year for year in range(0, 5)]
    years.sort(reverse=True)
    for year in years:
        financeiro_ano = Financeiro.objects.filter(
            projeto__in=projetos_aprovados, ano=datetime.now().year-year)
        context[f'year_{year}'] = datetime.now().year-year
        value_year = sum(
            [financeiro.valor for financeiro in financeiro_ano])
        context[f'value_year_{year}'] = format(
            value_year, decimal_sep=',', decimal_pos=2, grouping=3, thousand_sep='.')
    secretarias = Secretaria.objects.filter(data_criacao__lte=datetime.today())
    context['secretarias'] = []
    for secretaria in secretarias:
        dados_secretaria = {}
        dados_secretaria['codigo'] = secretaria.codigo
        dados_secretaria['nome'] = secretaria.nome
        dados_secretaria['quant_projetos_aprovados'] = secretaria.quant_projetos_aprovados()
        dados_secretaria['valor_projetos_aprovados'] = format(
            secretaria.valor_projetos_aprovados(),
            decimal_sep=',', decimal_pos=2, grouping=3, thousand_sep='.')
        context['secretarias'].append(dados_secretaria)
    return HttpResponse(json.dumps(context))