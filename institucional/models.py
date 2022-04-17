from django.db import models
from config.mixins import BaseModel


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
    data_criacao = models.DateTimeField(
        'Data de criação', )
    data_extincao = models.DateTimeField(
        'Data de extinção', blank=True, null=True)

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
    data_criacao = models.DateTimeField(
        'Data de criação', )
    data_extincao = models.DateTimeField(
        'Data de extinção', blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.nome)

    class Meta:
        verbose_name = 'Órgão'
        verbose_name_plural = 'Órgãos'
