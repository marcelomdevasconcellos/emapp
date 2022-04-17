from django.db import models
from config.mixins import BaseModel
from planejamento.models import Projeto, Financeiro
from planejamento.choices import STATUS_APROVADO


class Secretaria(BaseModel):
    cols = {
        'codigo': 3,
        'nome': 9, }

    codigo = models.CharField(
        'Código',
        max_length=8, )
    nome = models.CharField(
        'Nome',
        max_length=200, )
    data_criacao = models.DateField(
        'Data de criação', )
    data_extincao = models.DateField(
        'Data de extinção', blank=True, null=True)

    def quant_projetos_aprovados(self):
        projetos = Projeto.objects.filter(secretaria_id=self.id, status=STATUS_APROVADO)
        return len(projetos)

    def valor_projetos_aprovados(self):
        from datetime import datetime
        year = datetime.now().year
        projetos = Projeto.objects.filter(secretaria_id=self.id, status=STATUS_APROVADO)
        projetos_financeiro = Financeiro.objects.filter(projeto__in=projetos, ano=year)
        return sum([financeiro.valor for financeiro in projetos_financeiro])


    def __str__(self):
        return '{} - {}'.format(self.codigo, self.nome)

    class Meta:
        verbose_name = 'Secretaria'
        verbose_name_plural = 'Secretarias'


class Orgao(BaseModel):
    cols = {
        'secretaria': 12,
        'codigo': 3,
        'nome': 9, }

    secretaria = models.ForeignKey(
        'Secretaria',
        on_delete=models.PROTECT,
        related_name='%(class)s_secretaria', )
    codigo = models.CharField(
        'Código',
        max_length=8, )
    nome = models.CharField(
        'Nome',
        max_length=200, )
    data_criacao = models.DateField(
        'Data de criação', )
    data_extincao = models.DateField(
        'Data de extinção', blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.nome)

    class Meta:
        verbose_name = 'Órgão'
        verbose_name_plural = 'Órgãos'


class CorpoTecnico(BaseModel):
    cols = {
        'secretaria': 12,
        'codigo': 3,
        'nome': 9, }

    orgao = models.ForeignKey(
        'Orgao',
        verbose_name="Órgão",
        on_delete=models.PROTECT,
        related_name='%(class)s_orgao', )
    user = models.ForeignKey(
        'users.User',
        verbose_name="Pessoa",
        on_delete=models.PROTECT,
        related_name='%(class)s_user', )
    data_inicio = models.DateField(
        'Data de inicio', )
    data_termino = models.DateField(
        'Data de término', blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.orgao, self.user)

    class Meta:
        verbose_name = 'Corpo técnico'
        verbose_name_plural = 'Corpo técnico'
