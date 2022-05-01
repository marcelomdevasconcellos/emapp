from django.db import models
from django.contrib.auth.models import User
from config.mixins import BaseModel
from .choices import *
from datetime import datetime, timedelta


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
    data_ultimo_acompanhamento = models.DateTimeField(
        'Data do último acompanhamento', blank=True, null=True)
    prazo_execucao = models.IntegerField(
        'Prazo de execução (meses)', )
    responsavel = models.ForeignKey(
        'users.User',
        verbose_name='Responsável',
        on_delete=models.PROTECT,
        related_name='%(class)s_responsavel', )
    status = models.IntegerField(
        'Status',
        choices=CHOICES_STATUS,
        default=STATUS_CADASTRADO, )

    def acompanhamento(self):
        if self.data_ultimo_acompanhamento and \
                self.data_ultimo_acompanhamento >= datetime.now() - timedelta(days=30):
            return 'Atualizado'
        elif self.data_ultimo_acompanhamento and \
                self.data_ultimo_acompanhamento < datetime.now() - timedelta(days=30):
            return 'Atrasado'
        else:
            return 'Aguardando'

    def __str__(self):
        return '{} - {}'.format(
            self.id, self.nome)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        permissions = (
            ("can_approve_project", "Pode aprovar projeto"),
            ("can_submit_project", "Pode submeter projeto"),
        )


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


    def save(self, force_insert=False, force_update=False,
             using=None, update_fields=None):

        ultimo_acompanhamento = Acompanhamento.objects.filter(
            projeto_id=self.projeto_id).order_by('-data').first()
        projeto = Projeto.objects.filter(id=self.projeto_id)
        if ultimo_acompanhamento and ultimo_acompanhamento.data >= self.data:
            data_ultimo_acompanhamento = ultimo_acompanhamento.data
        else:
            data_ultimo_acompanhamento = self.data
        projeto.update(data_ultimo_acompanhamento=data_ultimo_acompanhamento)

        super(BaseModel, self).save(
            force_insert=False, force_update=False,
            using=None, update_fields=None, )

    def __str__(self):
        return '{} - {}'.format(
            self.id, self.data)

    class Meta:
        verbose_name = 'Acompanhamento'
        verbose_name_plural = 'Acompanhamentos'
