from django.db import models
from config.mixins import BaseModel


class ProjetoTipo(BaseModel):
    codigo = models.CharField(
        'Código',
        max_length=8, )
    nome = models.CharField(
        'Nome',
        max_length=200, )

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.nome)

    class Meta:
        verbose_name = 'Tipo de projeto'
        verbose_name_plural = 'Tipos de projeto'


class UnidadeTipo(BaseModel):
    codigo = models.CharField(
        'Código',
        max_length=8, )
    nome = models.CharField(
        'Nome',
        max_length=200, )

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.nome)

    class Meta:
        verbose_name = 'Tipo de unidade'
        verbose_name_plural = 'Tipos de unidade'
