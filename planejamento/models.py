from django.db import models

# Create your models here.

from config.mixins import BaseModel
from .choices import *
from contrib.choices import STATUS_INICIAL


class Projeto(BaseModel):
    cols = {
        'secretaria': 3,
        'nome': 9,
        'detalhamento': 12,
    }
    secretaria = models.ForeignKey(
        'institucional.Secretaria',
        on_delete=models.PROTECT,
        related_name='%(class)s_secretaria', )
    nome = models.CharField(
        'Nome',
        max_length=50, )
    detalhamento = models.TextField(
        'Detalhamento', )
    endereco = models.CharField(
        'Endereço',
        max_length=200, )
    latitude = models.DecimalField(
        'Latitude',
        max_digits=15,
        decimal_places=12, blank=True, null=True)
    longitude = models.DecimalField(
        'Longitude',
        max_digits=15,
        decimal_places=12, blank=True, null=True)
    tipo = models.ForeignKey(
        'contrib.ProjetoTipo',
        on_delete=models.PROTECT,
        related_name='%(class)s_orcamento', )
    unidade = models.ForeignKey(
        'contrib.UnidadeTipo',
        on_delete=models.PROTECT,
        related_name='%(class)s_orcamento', )
    quantidade = models.IntegerField(
        'Quantidade', )
    data_aprovacao = models.DateTimeField(
        'Data de aprovação', blank=True, null=True)
    prazo_execucao = models.IntegerField(
        'Prazo de execução (meses)', )
    responsavel = models.ForeignKey(
        'Responsavel',
        verbose_name='Responsável',
        on_delete=models.PROTECT,
        related_name='%(class)s_responsavel', )
    status = models.IntegerField(
        'Status',
        choices=CHOICES_STATUS,
        default=STATUS_CADASTRADO, )

    def __str__(self):
        return '{} - {}'.format(
            self.id, self.nome)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'


class Financeiro(BaseModel):

    projeto = models.ForeignKey(
        'Projeto',
        on_delete=models.PROTECT,
        related_name='%(class)s_projeto', )
    ano = models.IntegerField(
        'Ano',
        choices=CHOICES_ANOS)
    valor = models.DecimalField(
        'Valor',
        max_digits=15,
        decimal_places=2, )

    def __str__(self):
        return '{} - {} - {}'.format(
            self.id, self.ano, self.valor)

    class Meta:
        unique_together = ('projeto', 'ano')
        verbose_name = 'Planejamento Financeiro'
        verbose_name_plural = 'Planejamento Financeiro'


class Acompanhamento(BaseModel):

    projeto = models.ForeignKey(
        'Projeto',
        on_delete=models.PROTECT,
        related_name='%(class)s_projeto', )
    data = models.DateTimeField(
        'Data/Hora', )
    descricao = models.TextField(
        'Descricao', )

    def __str__(self):
        return '{} - {}'.format(
            self.id, self.data)

    class Meta:
        verbose_name = 'Acompanhamento'
        verbose_name_plural = 'Acompanhamentos'


class Responsavel(BaseModel):
    nome = models.CharField(
        'Nome',
        max_length=60, )
    telefone = models.CharField(
        'Telefone(s)',
        max_length=150, )
    email = models.EmailField(
        'E-mail', )

    def __str__(self):
        return '{} - {}'.format(
            self.id, self.nome)

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'